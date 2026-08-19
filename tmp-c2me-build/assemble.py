import hashlib, io, json, sys, zipfile
from pathlib import Path

if len(sys.argv) != 6:
    raise SystemExit('usage: assemble.py BASE DFC OPENCL OUT LIBS_DIR')
base, dfc, opencl, out, libs_dir = map(Path, sys.argv[1:6])

with zipfile.ZipFile(base) as z:
    entries = {i.filename: z.read(i.filename) for i in z.infolist()}
    meta = json.loads(entries['META-INF/jarjar/metadata.json'])

original = {x['path']: hashlib.sha256(entries[x['path']]).hexdigest() for x in meta['jars']}
seen = {(x['identifier']['group'], x['identifier']['artifact']): x for x in meta['jars']}


def clean_module(module_path: Path):
    with zipfile.ZipFile(module_path) as zin:
        module_entries = {i.filename: zin.read(i.filename) for i in zin.infolist()}
    inner = json.loads(module_entries.get('META-INF/jarjar/metadata.json', b'{"jars":[]}'))
    inner_paths = {dep['path'] for dep in inner.get('jars', [])}
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as zout:
        for name, payload in module_entries.items():
            if name == 'META-INF/jarjar/metadata.json' or name in inner_paths:
                continue
            zout.writestr(name, payload)
    return buf.getvalue()


def add_outer(identifier_group, identifier_artifact, version, payload, filename, is_obfuscated=False):
    key = (identifier_group, identifier_artifact)
    if key in seen:
        raise SystemExit(f'Duplicate JarJar identifier: {key}')
    path = 'META-INF/jarjar/' + filename
    if path in entries:
        raise SystemExit(f'Duplicate JarJar path: {path}')
    entries[path] = payload
    item = {
        'identifier': {'group': identifier_group, 'artifact': identifier_artifact},
        'version': {'range': f'[{version},)', 'artifactVersion': version},
        'path': path,
        'isObfuscated': is_obfuscated,
    }
    meta['jars'].append(item)
    seen[key] = item
    return path


def add_module(artifact: str, module_path: Path, clean_name: str):
    return add_outer('c2me', artifact, '0.2.0+alpha.12.1', clean_module(module_path), clean_name, True)


def merge_jars(paths, output_name):
    merged = {}
    for jar_path in paths:
        with zipfile.ZipFile(jar_path) as zin:
            for info in zin.infolist():
                name = info.filename
                if info.is_dir():
                    continue
                upper = name.upper()
                if name == 'META-INF/MANIFEST.MF' or name.endswith('module-info.class'):
                    continue
                if upper.startswith('META-INF/') and upper.endswith(('.SF', '.RSA', '.DSA')):
                    continue
                payload = zin.read(name)
                prior = merged.get(name)
                if prior is not None and prior != payload:
                    raise SystemExit(f'Conflicting merged entry {name} while building {output_name}')
                merged[name] = payload
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as zout:
        for name in sorted(merged):
            zout.writestr(name, merged[name])
    return buf.getvalue()


add_module('c2me_opts_dfc', dfc, 'c2meF-opts-dfc-mc1.20.1-0.2.0+alpha.12.1.jar')
add_module('c2me_opts_accel_opencl', opencl, 'c2meF-opts-accel-opencl-mc1.20.1-0.2.0+alpha.12.1.jar')

opencl_runtime = merge_jars([
    libs_dir / 'lwjgl-3.3.3.jar',
    libs_dir / 'lwjgl-opencl-3.3.3.jar',
    libs_dir / 'lwjgl-3.3.3-natives-windows.jar',
], 'lwjgl-opencl-c2me-runtime-3.3.3.jar')
zstd_runtime = merge_jars([
    libs_dir / 'lwjgl-zstd-3.3.3.jar',
    libs_dir / 'lwjgl-zstd-3.3.3-natives-windows.jar',
], 'lwjgl-zstd-c2me-runtime-3.3.3.jar')
caffeine = (libs_dir / 'caffeine-3.2.1.jar').read_bytes()

runtime_paths = [
    add_outer('c2me.runtime', 'lwjgl-opencl-windows', '3.3.3', opencl_runtime, 'lwjgl-opencl-c2me-runtime-3.3.3.jar'),
    add_outer('c2me.runtime', 'lwjgl-zstd-windows', '3.3.3', zstd_runtime, 'lwjgl-zstd-c2me-runtime-3.3.3.jar'),
    add_outer('com.github.ben-manes.caffeine', 'caffeine', '3.2.1', caffeine, 'caffeine-3.2.1.jar'),
]

mods_toml = entries.get('META-INF/mods.toml')
if mods_toml:
    text = mods_toml.decode('utf-8')
    text = text.replace('version = "0.2.0+alpha.12"', 'version = "0.2.0+alpha.12.1-opencl-radiumcompat"', 1)
    entries['META-INF/mods.toml'] = text.encode('utf-8')

entries['META-INF/jarjar/metadata.json'] = json.dumps(meta, indent=2).encode()
entries['META-INF/c2me-opencl-radium-compat.txt'] = (
    'Base c2meF 0.2.0+alpha.12 SHA1 ad44f615a4b15afd1d6a4d907ccab1c3855451a1\n'
    'OpenCL source 342c5035d7251ca987c962a14997a21a36eace44\n'
    'Radium 0.12.4+git.26c9d8e: disable mixin.world.chunk_access and mixin.alloc.nbt\n'
    'Runtime hardening: LWJGL core/OpenCL Windows payload, Zstd Windows payload, and Caffeine 3.2.1 vendored in outer JarJar.\n'
    'Fallback hardening: OpenCL global-context failure skips world codegen cleanly.\n'
).encode()

with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
    for name, payload in entries.items():
        z.writestr(name, payload)

with zipfile.ZipFile(out) as z:
    names = set(z.namelist())
    final_meta = json.loads(z.read('META-INF/jarjar/metadata.json'))
    assert all(x['path'] in names for x in final_meta['jars'])
    assert all(hashlib.sha256(z.read(path)).hexdigest() == digest for path, digest in original.items())
    assert all(path in names for path in runtime_paths)
    with zipfile.ZipFile(io.BytesIO(z.read(runtime_paths[0]))) as rt:
        runtime_names = set(rt.namelist())
        assert 'org/lwjgl/system/CustomBuffer.class' in runtime_names
        assert 'org/lwjgl/system/MemoryUtil.class' in runtime_names
        assert 'org/lwjgl/opencl/CL.class' in runtime_names
    with zipfile.ZipFile(io.BytesIO(z.read(runtime_paths[1]))) as rt:
        assert 'org/lwjgl/util/zstd/Zstd.class' in rt.namelist()
    with zipfile.ZipFile(io.BytesIO(z.read(runtime_paths[2]))) as rt:
        assert 'com/github/benmanes/caffeine/cache/Caffeine.class' in rt.namelist()

print('output_sha256=', hashlib.sha256(out.read_bytes()).hexdigest())
print('preserved_original_nested_entries=', len(original))
print('runtime_entries_added=', len(runtime_paths))
for item in runtime_paths:
    print('runtime=', item)
print('final_nested_entries=', len(final_meta['jars']))
print('dfc=', dfc.name)
print('opencl=', opencl.name)
