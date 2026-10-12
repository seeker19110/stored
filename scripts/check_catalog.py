#!/usr/bin/env python3
"""Kiểm tra tính nhất quán của catalog: JSON hợp lệ, trường bắt buộc, không trùng tên,
category nằm trong meta.categories, section có thư mục tương ứng, CSV khớp số dòng với JSON."""
import csv
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JSON_PATH = os.path.join(ROOT, "data", "projects.json")
CSV_PATH = os.path.join(ROOT, "data", "projects.csv")
REQUIRED = ("name", "category", "open_source", "notes", "section")

errors = []
with open(JSON_PATH, encoding="utf-8") as f:
    data = json.load(f)

projects = data.get("projects", [])
categories = set(data.get("meta", {}).get("categories", []))
sections = {d[:2] for d in os.listdir(ROOT) if os.path.isdir(os.path.join(ROOT, d)) and d[:2].isdigit()}
seen = set()
for i, p in enumerate(projects):
    for k in REQUIRED:
        if k not in p:
            errors.append(f"projects[{i}] thiếu trường '{k}'")
    name = p.get("name")
    if name in seen:
        errors.append(f"trùng tên dự án: {name}")
    seen.add(name)
    if p.get("category") not in categories:
        errors.append(f"{name}: category '{p.get('category')}' không có trong meta.categories")
    if p.get("section") not in sections:
        errors.append(f"{name}: section '{p.get('section')}' không có thư mục tương ứng")
    if not p.get("repo") and not p.get("url"):
        errors.append(f"{name}: cần ít nhất 'repo' hoặc 'url'")
    if "stars" in p and p["stars"] is not None and not isinstance(p["stars"], int):
        errors.append(f"{name}: stars phải là số nguyên hoặc null")

with open(CSV_PATH, encoding="utf-8", newline="") as f:
    rows = list(csv.reader(f))
if len(rows) - 1 != len(projects):
    errors.append(f"CSV có {len(rows) - 1} dòng, JSON có {len(projects)} dự án (chạy lại bước sinh CSV trong TEMPLATE.md)")
csv_names = {r[0] for r in rows[1:]}
missing = seen - csv_names
if missing:
    errors.append(f"CSV thiếu: {sorted(missing)[:5]}...")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK: {len(projects)} dự án, {len(categories)} category, CSV khớp.")
