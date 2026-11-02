#!/usr/bin/env python3
"""Kiểm catalog, CSV từng ô, ngày/nguồn và neo hồ sơ; chỉ chạy offline."""
import argparse
import csv
from datetime import date
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
CSV_FIELDS = ['name', 'repo', 'url', 'category', 'license', 'stars_est', 'open_source', 'section', 'notes']
LEVELS = {'unassessed', 'docs-read', 'code-read', 'checks-run', 'reproduced'}


def csv_row(p):
    return [p.get('name', ''), p.get('repo') or '', p.get('url') or '', p.get('category', ''),
            p.get('license') or '', str(p['stars']) if p.get('stars') is not None else '',
            str(p.get('open_source', '')), p.get('section', ''), p.get('notes', '')]


def valid_date(value):
    try:
        return isinstance(value, str) and date.fromisoformat(value).isoformat() == value
    except ValueError:
        return False


def valid_url(value):
    if not isinstance(value, str):
        return False
    try:
        p = urlsplit(value)
        return p.scheme in {'http', 'https'} and bool(p.netloc) and not p.username
    except ValueError:
        return False


def markdown_anchors(text):
    anchors, counts, fence = set(), {}, None
    text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
    for line in text.splitlines():
        marker = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', line)
        if marker:
            char = marker[1][0]
            if fence is None:
                fence = (char, len(marker[1]))
            elif fence[0] == char and len(marker[1]) >= fence[1] and not marker[2].strip():
                fence = None
            continue
        if fence:
            continue
        anchors.update(re.findall(r'^ {0,3}<a\s+(?:[^>]*?\s)?(?:id|name)=["\x27]([^"\x27]+)', line))
        h = re.match(r'^#{1,6}\s+(.+?)(?:\s+#+)?\s*$', line)
        if not h:
            continue
        label = re.sub(r'!?\[([^\]]+)\]\([^)]*\)', r'\1', h[1])
        label = re.sub(r'<[^>]+>', '', label).lower()
        slug = re.sub(r'[^\w\- ]', '', label).replace(' ', '-')
        n = counts.get(slug, 0)
        counts[slug] = n + 1
        anchors.add(slug if n == 0 else f'{slug}-{n}')
    return anchors


def validate(root=ROOT):
    root, errors = Path(root).resolve(), []
    def fail(message):
        errors.append(message)
    def read_json(path):
        try:
            return json.loads(path.read_text(encoding='utf-8'))
        except (OSError, ValueError) as exc:
            fail(f'{path.name}: {exc}')
    def profile(value, label, require_anchor=False):
        if not isinstance(value, str):
            fail(f'{label}: hồ sơ phải là đường dẫn chuỗi'); return
        try:
            p = urlsplit(value)
        except ValueError:
            fail(f'{label}: đường dẫn hồ sơ không hợp lệ'); return
        try:
            target = (root / unquote(p.path)).resolve()
            is_file = target.is_file()
        except (OSError, ValueError, RuntimeError) as exc:
            fail(f'{label}: đường dẫn hồ sơ không hợp lệ: {exc}'); return
        if p.scheme or p.netloc or not target.is_relative_to(root):
            fail(f'{label}: hồ sơ phải nằm trong kho'); return
        if not is_file:
            fail(f'{label}: thiếu file {p.path}'); return
        if require_anchor and not p.fragment:
            fail(f'{label}: profile_anchor cần neo heading')
        if p.fragment:
            try:
                anchors = markdown_anchors(target.read_text(encoding='utf-8'))
            except (OSError, UnicodeError) as exc:
                fail(f'{label}: không đọc được hồ sơ UTF-8: {exc}'); return
            if unquote(p.fragment) not in anchors:
                fail(f'{label}: neo không tồn tại: {value}')
    data = read_json(root / 'data/projects.json')
    if not isinstance(data, dict):
        return errors or ['projects.json phải là object']
    ps, meta = data.get('projects'), data.get('meta')
    if not isinstance(ps, list) or not isinstance(meta, dict):
        return errors + ['projects cần list; meta cần object']
    categories = meta.get('categories', [])
    if not isinstance(categories, list) or any(not isinstance(c, str) or not c for c in categories):
        return errors + ['meta.categories cần list chuỗi không rỗng']
    if len(categories) != len(set(categories)):
        fail('meta.categories bị trùng')
    schema_version = meta.get('schema_version')
    if type(schema_version) is not int or schema_version != 2:
        fail('meta.schema_version phải là 2')
        schema_version = 2
    if not valid_date(meta.get('snapshot_date')):
        fail('meta.snapshot_date phải là ngày ISO hợp lệ')
    sections = {p.name[:2] for p in root.iterdir() if p.is_dir() and re.match(r'^\d{2}-', p.name)}
    names, ids = set(), set()
    if type(meta.get('count')) is not int or meta['count'] != len(ps):
        fail('meta.count không khớp số hồ sơ')
    for i, p in enumerate(ps):
        if not isinstance(p, dict):
            fail(f'projects[{i}]: phải là object'); continue
        label = p.get('name') if isinstance(p.get('name'), str) else f'projects[{i}]'
        for key, kind in {'name': str, 'category': str, 'open_source': bool, 'notes': str, 'section': str}.items():
            if type(p.get(key)) is not kind:
                fail(f'{label}: {key} phải là {kind.__name__}')
        name = p.get('name')
        if not isinstance(name, str):
            continue
        if not name.strip() or name in names:
            fail(f'{label}: tên rỗng hoặc trùng')
        names.add(name)
        if p.get('category') not in categories:
            fail(f'{label}: category chưa đăng ký')
        if not isinstance(p.get('section'), str) or p['section'] not in sections:
            fail(f'{label}: section không có thư mục')
        repo = p.get('repo')
        if repo is not None and (not isinstance(repo, str) or not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repo)):
            fail(f'{label}: repo cần owner/name')
        if not repo and not p.get('url'):
            fail(f'{label}: cần repo hoặc url')
        if p.get('url') is not None and not valid_url(p['url']):
            fail(f'{label}: url không hợp lệ')
        if p.get('license') is not None and not isinstance(p['license'], str):
            fail(f'{label}: license phải là chuỗi hoặc null')
        if p.get('stars') is not None and (type(p['stars']) is not int or p['stars'] < 0):
            fail(f'{label}: stars phải là số nguyên không âm hoặc null')
        if schema_version >= 2 or 'id' in p:
            pid = p.get('id')
            if not isinstance(pid, str) or not re.fullmatch(r'[a-z0-9][a-z0-9._-]*', pid):
                fail(f'{label}: id không hợp lệ')
            elif pid in ids:
                fail(f'{label}: id trùng {pid}')
            else:
                ids.add(pid)
        if 'profile_path' in p:
            profile(p['profile_path'], label)
        if 'profile_anchor' in p:
            profile(p['profile_anchor'], label, True)
        level = p.get('verification_level')
        if 'verification_level' in p and (not isinstance(level, str) or level not in LEVELS):
            fail(f'{label}: verification_level không hợp lệ')
        if 'last_verified_at' in p and not valid_date(p['last_verified_at']):
            fail(f'{label}: last_verified_at sai ngày ISO')
        sources = p.get('sources')
        if 'sources' in p and (not isinstance(sources, list) or not sources or any(not valid_url(u) for u in sources)):
            fail(f'{label}: sources cần list URL hợp lệ không rỗng')
        if 'verified_ref' in p and (not isinstance(p['verified_ref'], str) or not re.fullmatch(r'[a-f0-9]{40}', p['verified_ref'])):
            fail(f'{label}: verified_ref cần full commit SHA')
        if level and level != 'unassessed':
            if not valid_date(p.get('last_verified_at')) or not sources or not p.get('profile_anchor'):
                fail(f'{label}: mức kiểm cần ngày, nguồn và profile_anchor')
            if repo and (not isinstance(p.get('verified_ref'), str) or not re.fullmatch(r'[a-f0-9]{40}', p['verified_ref'])):
                fail(f'{label}: verified_ref cần full commit SHA')
    try:
        with (root / 'data/projects.csv').open(encoding='utf-8', newline='') as f:
            rows = list(csv.reader(f))
        expected = [CSV_FIELDS] + [csv_row(p) for p in ps if isinstance(p, dict)]
        if len(rows) != len(expected):
            fail(f'CSV có {len(rows)-1} dòng, JSON có {len(ps)} hồ sơ')
        for n, (actual, wanted) in enumerate(zip(rows, expected), 1):
            if actual != wanted:
                fail(f'CSV dòng {n} không khớp từng ô với JSON')
                if n > 10:
                    break
    except (OSError, csv.Error) as exc:
        fail(f'projects.csv: {exc}')
    hp = root / 'data/xt-handoff.json'
    if hp.exists():
        h = read_json(hp)
        if not isinstance(h, dict) or not isinstance(h.get('items'), list):
            return errors + ['xt-handoff cần object có items list']
        seen = set()
        for item in h['items']:
            if not isinstance(item, dict):
                fail('xt-handoff item phải là object'); continue
            hid = item.get('id', '?')
            if not isinstance(hid, str) or not re.fullmatch(r'XT-H-\d{3}', hid) or hid in seen:
                fail(f'xt-handoff id sai hoặc trùng: {hid}')
            seen.add(str(hid))
            if not isinstance(item.get('column'), str) or item['column'] not in {'deeper', 'shallower', 'missing', 'not_adding'}:
                fail(f'{hid}: column không hợp lệ')
            refs = item.get('stored_ref')
            if not isinstance(refs, list) or not refs or any(not isinstance(r, str) or r[:2] not in sections for r in refs):
                fail(f'{hid}: stored_ref không hợp lệ')
            anchors = item.get('profile_anchors', [])
            if not isinstance(anchors, list):
                fail(f'{hid}: profile_anchors cần list'); anchors = []
            for anchor in anchors:
                profile(anchor, hid, True)
            xt_ids = item.get('xt_ids', [])
            if not isinstance(xt_ids, list):
                fail(f'{hid}: xt_ids cần list'); xt_ids = []
            for xid in xt_ids:
                if not isinstance(xid, str) or not re.fullmatch(r'[A-Z]+-[A-Z0-9]+-\d{3}', xid):
                    fail(f'{hid}: xt_id sai dạng')
            if (item.get('column') in ['shallower', 'missing']) != ('proposal' in item):
                fail(f'{hid}: proposal không khớp column')
            if 'proposal' in item and (not isinstance(item['proposal'], dict) or not isinstance(item['proposal'].get('text'), str) or not item['proposal']['text'].strip()):
                fail(f'{hid}: proposal cần object có text không rỗng')
            if not valid_date(item.get('date')):
                fail(f'{hid}: date sai ngày ISO')
        handoff_meta = h.get('meta', {})
        if not isinstance(handoff_meta, dict):
            fail('xt-handoff meta cần object'); handoff_meta = {}
        if handoff_meta.get('count') is not None and handoff_meta['count'] != len(h['items']):
            fail('xt-handoff meta.count không khớp')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    errors = validate(args.root)
    if errors:
        print('\n'.join(errors)); return 1
    data = json.loads((args.root / 'data/projects.json').read_text(encoding='utf-8'))
    print(f"OK: {len(data['projects'])} hồ sơ, {len(data['meta']['categories'])} category; CSV khớp từng ô; nguồn và neo hợp lệ.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
