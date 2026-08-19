import hashlib, io, json, sys, zipfile
from pathlib import Path

base, dfc, opencl, out = map(Path, sys.argv[1:5])

with zipfile.ZipFile(base) as z:
    entries = {i.filename: z.read(i.filename) for i in z.infolist()}
    meta = json.loads(entries['META-INF/jarjar/metadata.json'])

original = {x['path']: hashlib.sha256(entries[x['path']]).hexdigest() for x in meta['jars']}
seen = {(x['identifier']['group'], x['identifier']['artifact']): x for x in meta['jars']}
flattened = []


def clean_module(module_path: Path):
    with zipfile.ZipFile(module_path) as zin:
        module_entries = {i.filename: zin.read(i.filename) for i in zin.infolist()}
    inner = json.loads(module_entries.get('META-INF/jarjar/metadata.json', b'{"jars":[]}'))
    inner_paths = set()
    for dep in inner.get('jars', []):
        dep_path = dep['path']
        inner_paths.add(dep_path)
        if dep_path not in module_entries:
            raise SystemExit(f'{module_path.name}: missing declared JarJar dependency {dep_path}')
        key = (dep['identifier']['group'], dep['identifier']['artifact'])
        payload = module_entries[dep_path]
        existing = seen.get(key)
        if existing is not None:
            existing_payload = entries.get(existing['path'])
            if existing_payload is not None and existing_payload != payload:
                raise SystemExit(f'Conflicting JarJar dependency {key}: {existing["path"]} vs {dep_path}')
            continue
        flat_path = 'META-INF/jarjar/' + Path(dep_path).name
        if flat_path in entries and entries[flat_path] != payload:
            raise SystemExit(f'Conflicting outer path {flat_path}')
        dep_copy = json.loads(json.dumps(dep))
        dep_copy['path'] = flat_path
        entries[flat_path] = payload
        meta['jars'].append(dep_copy)
        seen[key] = dep_copy
        flattened.append(flat_path)

    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as zout:
        for name, payload in module_entries.items():
            if name == 'META-INF/jarjar/metadata.json' or name in inner_paths:
                continue
            zout.writestr(name, payload)
    return buf.getvalue()


def add_module(artifact: str, module_path: Path, clean_name: str):
    payload = clean_module(module_path)
    dst = 'META-INF/jarjar/' + clean_name
    entries[dst] = payload
    item = {
        'identifier': {'group': 'c2me', 'artifact': artifact},
        'version': {'range': '[0.2.0,)', 'artifactVersion': '0.2.0+alpha.12.1'},
        'path': dst,
        'isObfuscated': True,
    }
    if (item['identifier']['group'], item['identifier']['artifact']) in seen:
        raise SystemExit(f'Duplicate module identifier: {artifact}')
    meta['jars'].append(item)
    seen[(item['identifier']['group'], item['identifier']['artifact'])] = item


add_module('c2me_opts_dfc', dfc, 'c2meF-opts-dfc-mc1.20.1-0.2.0+alpha.12.1.jar')
add_module('c2me_opts_accel_opencl', opencl, 'c2meF-opts-accel-opencl-mc1.20.1-0.2.0+alpha.12.1.jar')

# Make the custom build identifiable without altering any preserved nested c2meF module bytes.
mods_toml = entries.get('META-INF/mods.toml')
if mods_toml:
    text = mods_toml.decode('utf-8')
    text = text.replace('version = "0.2.0+alpha.12"', 'version = "0.2.0+alpha.12.1-opencl-radiumcompat"', 1)
    entries['META-INF/mods.toml'] = text.encode('utf-8')

entries['META-INF/jarjar/metadata.json'] = json.dumps(meta, indent=2).encode()
entries['META-INF/c2me-opencl-radium-compat.txt'] = (
    'Base c2meF 0.2.0+alpha.12 SHA1 ad44f615a4b15afd1d6a4d907ccab1c3855451a1\n'
    'OpenCL source 342c5035d7251ca987c962a14997a21a36eace44\n'
    'Radium 0.12.4+git.26c9d8e compatibility: disable mixin.world.chunk_access and mixin.alloc.nbt\n'
    'OpenCL hardening: flattened runtime JarJar dependencies; allowIncompatibilityFallback default true\n'
).encode()

with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
    for name, payload in entries.items():
        z.writestr(name, payload)

with zipfile.ZipFile(out) as z:
    names = set(z.namelist())
    final_meta = json.loads(z.read('META-INF/jarjar/metadata.json'))
    assert all(x['path'] in names for x in final_meta['jars'])
    assert all(hashlib.sha256(z.read(path)).hexdigest() == digest for path, digest in original.items())
    assert 'META-INF/jarjar/c2meF-opts-dfc-mc1.20.1-0.2.0+alpha.12.1.jar' in names
    assert 'META-INF/jarjar/c2meF-opts-accel-opencl-mc1.20.1-0.2.0+alpha.12.1.jar' in names

print('output_sha256=', hashlib.sha256(out.read_bytes()).hexdigest())
print('preserved_original_nested_entries=', len(original))
print('flattened_runtime_dependencies=', len(flattened))
for item in flattened:
    print('flattened=', item)
print('final_nested_entries=', len(final_meta['jars']))
print('dfc=', dfc.name)
print('opencl=', opencl.name)
