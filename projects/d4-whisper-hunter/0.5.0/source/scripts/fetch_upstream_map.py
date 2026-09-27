from __future__ import annotations
import hashlib
from pathlib import Path
import urllib.request

URL='https://raw.githubusercontent.com/mxtsdev/d4-map-overlay/main/map_images/map_5_small.jpg'
SIZE=4424290
BLOB='4394f963aff1545d928bcf160809fbd05a5a4bfd'
OUT=Path(__file__).resolve().parents[1]/'assets'/'map_5_small.jpg'

def blob_sha(data: bytes) -> str:
    return hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()

def main():
    if OUT.exists():
        data=OUT.read_bytes()
        if len(data)==SIZE and blob_sha(data)==BLOB:
            print(OUT)
            return 0
    OUT.parent.mkdir(parents=True,exist_ok=True)
    tmp=OUT.with_suffix('.download')
    req=urllib.request.Request(URL,headers={'User-Agent':'D4WhisperHunter-build/0.4'})
    with urllib.request.urlopen(req,timeout=60) as r,tmp.open('wb') as f:
        while True:
            b=r.read(262144)
            if not b: break
            f.write(b)
    data=tmp.read_bytes()
    if len(data)!=SIZE or blob_sha(data)!=BLOB:
        tmp.unlink(missing_ok=True)
        raise SystemExit('upstream map integrity check failed')
    tmp.replace(OUT)
    print(OUT)
    return 0
if __name__=='__main__': raise SystemExit(main())
