"""Mutation checks prove the validator rejects common broken deliverables."""
from pathlib import Path
import csv
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from validate import ROOT, risk_band, validate


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'toolkit'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', '__pycache__'))

    def edit_csv(self, name, action):
        p = self.root / name
        with p.open(encoding='utf-8', newline='') as f:
            reader = csv.DictReader(f)
            fields, rows = reader.fieldnames, list(reader)
        action(rows)
        with p.open('w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)

    def test_clean_repository(self):
        self.assertEqual(validate(self.root), [])

    def test_missing_deliverable(self):
        (self.root / 'templates/risk-register.csv').unlink()
        self.assertTrue(any('Missing required file' in e for e in validate(self.root)))

    def test_broken_local_link(self):
        with (self.root / 'README.md').open('a', encoding='utf-8') as f:
            f.write('\n[broken](missing-document.md)\n')
        self.assertTrue(any('Broken local link' in e for e in validate(self.root)))

    def test_mapping_disagreement(self):
        self.edit_csv('control-matrix/mapping-relationships.csv', lambda rows: rows[0].update(iso27001_annex_a='A.8.32'))
        self.assertTrue(any('Matrix/edge mismatch' in e for e in validate(self.root)))

    def test_risk_arithmetic(self):
        self.edit_csv('examples/risk-register.csv', lambda rows: rows[0].update(inherent_score='1'))
        self.assertTrue(any('Risk arithmetic' in e for e in validate(self.root)))

    def test_evidence_tampering(self):
        with (self.root / 'examples/control-evidence/ev-001.md').open('a', encoding='utf-8') as f:
            f.write('\nUnreviewed alteration.\n')
        self.assertTrue(any('Evidence digest mismatch' in e for e in validate(self.root)))

    def test_synthetic_marker_required(self):
        self.edit_csv('examples/access-review.csv', lambda rows: rows[0].update(synthetic='false'))
        self.assertTrue(any('Missing CSV synthetic marker' in e for e in validate(self.root)))

    def test_secret_pattern(self):
        (self.root / 'work-note.txt').write_text('AKIA' + 'A' * 16, encoding='utf-8')
        self.assertTrue(any('Potential secret pattern' in e for e in validate(self.root)))

    def test_table_shape(self):
        with (self.root / 'README.md').open('a', encoding='utf-8') as f:
            f.write('\n| A | B |\n| --- | --- |\n| only one |\n')
        self.assertTrue(any('Malformed Markdown table' in e for e in validate(self.root)))

    def test_risk_band_boundaries(self):
        self.assertEqual([risk_band(n) for n in [1,4,5,9,10,16,17,25]],
                         ['Low','Low','Medium','Medium','High','High','Critical','Critical'])


if __name__ == '__main__':
    unittest.main()
