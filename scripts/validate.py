"""Validate local toolkit integrity, not framework compliance or live effectiveness."""
from pathlib import Path
from urllib.parse import unquote
import csv
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CRITERIA = {f'CC6.{n}' for n in range(1, 9)} | {f'CC7.{n}' for n in range(1, 6)} | {'CC8.1'}
REQUIRED = [
    'README.md', 'LICENSE', '.gitignore', '.gitattributes', '.github/workflows/validate.yml',
    'control-matrix/README.md', 'control-matrix/control-matrix.csv',
    'control-matrix/mapping-relationships.csv', 'control-matrix/iso-reference-catalog.csv',
    'templates/README.md', 'templates/audit-evidence-checklist.csv', 'templates/access-review.csv',
    'templates/risk-register.csv', 'templates/control-testing-procedures.csv',
    'templates/incident-record.md', 'templates/test-execution-record.md', 'templates/change-request.md',
    'examples/README.md', 'examples/access-review.csv', 'examples/risk-register.csv',
    'examples/control-test-results.csv', 'examples/wazuh-alerts.jsonl', 'examples/ad-events.jsonl',
    'examples/sophos-events.jsonl', 'examples/cloudtrail-events.json', 'examples/aws-findings.json',
    'examples/change-record.json', 'examples/incident-record.md', 'evidence/README.md',
    'evidence/manifest.csv', 'evidence/chain-of-custody.csv', 'diagrams/architecture.md',
    'diagrams/control-evidence-workflow.md', 'docs/mapping-methodology.md', 'docs/operating-model.md',
    'docs/risk-methodology.md', 'docs/incident-response-runbook.md', 'docs/glossary.md',
    'docs/sources.md', 'docs/interview-guide.md', 'docs/publishing.md', 'docs/delivery-report.md',
    'scripts/README.md', 'scripts/validate.py', 'scripts/update_manifest.py', 'tests/test_validate.py',
] + [f'examples/control-evidence/ev-{n:03}.md' for n in range(1, 15)]


def risk_band(score):
    return 'Low' if score <= 4 else 'Medium' if score <= 9 else 'High' if score <= 16 else 'Critical'


def validate(root=ROOT):
    errors = []

    def check(condition, message):
        if not condition:
            errors.append(message)

    for name in REQUIRED:
        check((root / name).is_file(), f'Missing required file: {name}')
    if errors:
        return errors

    files = [p for p in root.rglob('*') if p.is_file() and not any(
        part in {'.git', '__pycache__', '.venv'} for part in p.relative_to(root).parts)]
    tables = {}
    # shortcut: repository uses simple inline links and pipe tables; extend if reference links or HTML are introduced.
    for p in files:
        rel = p.relative_to(root).as_posix()
        try:
            text = p.read_text(encoding='utf-8')
        except (UnicodeError, OSError):
            errors.append(f'Unreadable UTF-8 file: {rel}')
            continue
        check(bool(text.strip()), f'Empty file: {rel}')
        if p.suffix == '.csv':
            reader = csv.DictReader(text.splitlines())
            check(bool(reader.fieldnames) and len(reader.fieldnames) == len(set(reader.fieldnames or [])),
                  f'Invalid CSV headers: {rel}')
            rows = list(reader)
            for row in rows:
                check(None not in row and all(v is not None for v in row.values()), f'Malformed CSV row: {rel}')
                check(all(not str(v).startswith(('=', '+', '-', '@')) for v in row.values()),
                      f'Potential spreadsheet formula cell: {rel}')
            tables[rel] = rows
        if p.suffix in {'.json', '.jsonl'}:
            try:
                records = [json.loads(line) for line in text.splitlines() if line.strip()] if p.suffix == '.jsonl' else [json.loads(text)]
                if rel.startswith('examples/'):
                    check(all(r.get('synthetic') is True for r in records), f'Missing synthetic JSON marker: {rel}')
            except (ValueError, AttributeError):
                errors.append(f'Invalid JSON record: {rel}')
        if p.suffix == '.md':
            in_code, columns = False, None
            for line in text.splitlines():
                if line.lstrip().startswith('```'):
                    in_code = not in_code
                    columns = None
                    continue
                if in_code:
                    continue
                if line.strip().startswith('|'):
                    cells = len(re.split(r'(?<!\\)\|', line.strip())) - 2
                    if columns is None:
                        columns = cells
                    check(cells == columns, f'Malformed Markdown table: {rel}')
                else:
                    columns = None
                for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', line):
                    if re.match(r'^[a-z]+:', target, re.I) or target.startswith('#'):
                        continue
                    path = unquote(target.split('#')[0])
                    resolved = (p.parent / path).resolve()
                    check(resolved.is_relative_to(root.resolve()) and resolved.exists(), f'Broken local link: {rel} -> {target}')
            check(not in_code, f'Unclosed Markdown fence: {rel}')
        if p.suffix in {'.md', '.csv', '.json', '.jsonl'}:
            check(not re.search(r'\b(?:TODO|TBD|FIXME)\b|lorem ipsum|<YOUR[_ -]', text, re.I), f'Unresolved placeholder: {rel}')
        # Heuristic only; these patterns do not replace mature secret scanning or a human review.
        for pattern in [r'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b', r'gh[pousr]_[A-Za-z0-9]{20,}',
                        r'github_pat_[A-Za-z0-9_]{20,}', r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
                        r'(?i)(?:password|secret_access_key|api_key)\s*[:=]\s*["\x27][^"\x27\s]{8,}["\x27]']:
            check(not re.search(pattern, text), f'Potential secret pattern: {rel}')
        if rel.startswith('examples/') and p.suffix == '.md':
            check('synthetic' in text.lower(), f'Missing synthetic prose marker: {rel}')

    if errors:
        return errors
    matrix = tables['control-matrix/control-matrix.csv']
    edges = tables['control-matrix/mapping-relationships.csv']
    catalog = tables['control-matrix/iso-reference-catalog.csv']
    checklist = tables['templates/audit-evidence-checklist.csv']
    tests = tables['templates/control-testing-procedures.csv']
    results = tables['examples/control-test-results.csv']
    refs = {r['iso27001_annex_a'] for r in catalog}
    cids = {r['control_id'] for r in matrix}
    eids = {r['evidence_id'] for r in checklist}
    tids = {r['test_id'] for r in tests}
    check(len(matrix) == len(cids) == 14, 'Control IDs must be unique and total 14')
    check({r['soc2_criterion'] for r in matrix} == CRITERIA, 'SOC 2 coverage must be CC6.1-8, CC7.1-5 and CC8.1')
    check(len(catalog) == len(refs), 'Duplicate ISO catalog reference')
    for ref in refs:
        match = re.fullmatch(r'A\.([5-8])\.(\d+)', ref)
        check(bool(match) and 1 <= int(match[2]) <= {'5':37,'6':8,'7':14,'8':34}[match[1]], f'Invalid ISO reference range: {ref}')
    edge_keys = [(e['control_id'], e['iso27001_annex_a']) for e in edges]
    check(len(edge_keys) == len(set(edge_keys)), 'Duplicate mapping edge')
    for e in edges:
        check(e['control_id'] in cids and e['iso27001_annex_a'] in refs, 'Mapping references unknown ID')
        check(e['relationship'] in {'Direct', 'Partial'}, 'Unknown relationship class')
        check(bool(e['rationale'] and e['separate_treatment']), 'Mapping lacks rationale or separate treatment')
        check(e['reference_review'] == 'Pending licensed-text and practitioner review', 'Mapping review claim changed; record qualified review before updating validator')
    for m in matrix:
        related = [e for e in edges if e['control_id'] == m['control_id']]
        check({e['iso27001_annex_a'] for e in related} == set(m['iso27001_annex_a'].split('; ')), f'Matrix/edge mismatch: {m["control_id"]}')
        check(all(e['soc2_criterion'] == m['soc2_criterion'] for e in related), f'Criterion mismatch: {m["control_id"]}')
        check(m['implementation_status'] == 'Designed only - synthetic demonstration', 'Unsupported implementation claim')
        check(m['test_id'] in tids, 'Matrix has unknown test ID')
        check(all(m.values()), f'Incomplete matrix row: {m["control_id"]}')
        index_line = next((line for line in (root / 'control-matrix/README.md').read_text(encoding='utf-8').splitlines() if line.startswith(f'| {m["control_id"]} |')), '')
        check(all(m[k] in index_line for k in ['description', 'soc2_criterion', 'iso27001_annex_a', 'control_owner']), 'Readable matrix differs from canonical CSV')
    for rows, label in [(checklist, 'Checklist'), (tests, 'Tests'), (results, 'Results')]:
        check(len(rows) == 14 and {r['control_id'] for r in rows} == cids, f'{label} must cover each control exactly once')
    check(len(eids) == len(checklist), 'Duplicate evidence ID')
    check(len(tids) == len(tests), 'Duplicate test ID')
    check(len({r['test_id'] for r in results}) == 14, 'Duplicate result test ID')
    for e in checklist:
        check((root / e['sample_reference']).is_file(), f'Missing sample reference: {e["evidence_id"]}')
        sample = (root / e['sample_reference']).read_text(encoding='utf-8') if (root / e['sample_reference']).is_file() else ''
        check(e['control_id'] in sample and e['evidence_id'] in sample, 'Evidence narrative ID mismatch')
    for t in tests:
        check(t['sample_evidence_id'] in eids, 'Test evidence ID missing')
        check(any(m['test_id'] == t['test_id'] and m['control_id'] == t['control_id'] for m in matrix), 'Test/control mismatch')
    for r in results:
        check(r['test_id'] in tids and r['evidence_id'] in eids, 'Result ID is unknown')
        check(any(t['test_id'] == r['test_id'] and t['control_id'] == r['control_id'] and t['sample_evidence_id'] == r['evidence_id'] for t in tests), 'Result/test/evidence mismatch')
        check(any(e['evidence_id'] == r['evidence_id'] and e['control_id'] == r['control_id'] for e in checklist), 'Result/checklist mismatch')
        check(r['result'] in {'Pass', 'Fail', 'Not tested'}, 'Invalid result')
        check(r['execution_mode'] == 'Synthetic desk review' and r['live_effectiveness'] == 'Not assessed', 'Unsupported live test claim')
    for name in ['examples/access-review.csv', 'examples/risk-register.csv', 'evidence/chain-of-custody.csv']:
        check(all(r['synthetic'] == 'true' for r in tables[name]), f'Missing CSV synthetic marker: {name}')
    risks = tables['examples/risk-register.csv']
    check(len({r['risk_id'] for r in risks}) == len(risks), 'Duplicate risk ID')
    for r in risks:
        check(set(r['control_ids'].split('; ')) <= cids, 'Risk references unknown control')
        for prefix, lkey, ikey in [('', 'likelihood', 'impact'), ('residual_', 'residual_likelihood', 'residual_impact')]:
            try:
                likelihood, impact = int(r[lkey]), int(r[ikey])
                scorekey = 'inherent_score' if not prefix else 'residual_score'
                bandkey = 'inherent_band' if not prefix else 'residual_band'
                check(1 <= likelihood <= 5 and 1 <= impact <= 5, 'Risk rating out of range')
                check(int(r[scorekey]) == likelihood * impact and r[bandkey] == risk_band(likelihood * impact), f'Risk arithmetic/band mismatch: {r["risk_id"]}')
            except ValueError:
                errors.append('Non-numeric risk rating')
    check(len(tables['templates/access-review.csv']) == len(tables['templates/risk-register.csv']) == 0, 'Blank forms must remain header-only')
    for row in tables['examples/access-review.csv']:
        check(row['control_id'] in cids, 'Access review references unknown control')
        check(row['decision'] in {'Retain', 'Remove', 'Modify'}, 'Invalid access decision')
        if row['decision'] == 'Remove' and row['status'] == 'Closed':
            check(row['closure_evidence'] != 'Not collected' and row['closure_date'] != 'Not closed', 'Removal closed without evidence')

    manifest = tables['evidence/manifest.csv']
    expected_files = {p.relative_to(root).as_posix() for p in files if p.relative_to(root).as_posix().startswith('examples/')}
    check({r['path'] for r in manifest} == expected_files and len(manifest) == len(expected_files), 'Manifest file coverage mismatch')
    for r in manifest:
        p = root / r['path']
        if p.is_file():
            check(hashlib.sha256(p.read_bytes()).hexdigest() == r['sha256'], f'Evidence digest mismatch: {r["path"]}')
        else:
            errors.append(f'Manifest path missing: {r["path"]}')
    return errors


if __name__ == '__main__':
    try:
        errors = validate()
    except (KeyError, ValueError, OSError, TypeError, csv.Error) as exc:
        errors = [f'Validation could not complete: {exc}']
    for error in errors:
        print(f'FAIL: {error}')
    if errors:
        sys.exit(1)
    print('PASS: required files; readable data; links/tables; 14 controls/tests/evidence requests; mapping IDs; risk scores; synthetic markers; evidence digests; common secret patterns.')
    print('LIMIT: no normative review, live effectiveness, external URL check, diagram render or exhaustive secret/sensitivity scan.')
