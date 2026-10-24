"""Rebuild local fixture digests after an intentional reviewed synthetic-data edit."""
from pathlib import Path
import csv
import hashlib

ROOT = Path(__file__).resolve().parents[1]

if __name__ == '__main__':
    rows = [dict(path=p.relative_to(ROOT).as_posix(), sha256=hashlib.sha256(p.read_bytes()).hexdigest(),
                 classification='Synthetic portfolio fixture')
            for p in sorted((ROOT / 'examples').rglob('*')) if p.is_file()]
    with (ROOT / 'evidence/manifest.csv').open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['path', 'sha256', 'classification'], lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)
    print(f'Indexed {len(rows)} synthetic fixture files. Review the manifest diff before committing.')
