"""Kiểm các sai lệch có thể làm catalog/CI báo xanh sai; không gọi mạng."""
import csv
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("check_catalog", Path(__file__).with_name("check_catalog.py"))
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class CatalogIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "data").mkdir()
        (self.root / "01-sample").mkdir()
        (self.root / "01-sample/README.md").write_text("# Sample\n\n## Evidence\n", encoding="utf-8")
        self.project = dict(id="sample", name="Sample", repo="owner/sample", category="tool", license="MIT",
                            stars=0, open_source=True, notes="Read source", section="01",
                            last_verified_at="2026-11-02", verified_ref="a" * 40, verification_level="code-read",
                            sources=["https://github.com/owner/sample"], profile_anchor="01-sample/README.md#evidence")
        self.data = dict(meta=dict(schema_version=2, snapshot_date="2026-11-02", categories=["tool"], count=1), projects=[self.project])
        self.write()

    def write(self):
        (self.root / "data/projects.json").write_text(json.dumps(self.data), encoding="utf-8")
        with (self.root / "data/projects.csv").open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow(checker.CSV_FIELDS)
            writer.writerows(checker.csv_row(p) for p in self.data["projects"])

    def test_valid_fixture(self):
        self.assertEqual(checker.validate(self.root), [])

    def test_same_names_and_row_count_cannot_hide_changed_license(self):
        path = self.root / "data/projects.csv"
        path.write_text(path.read_text().replace(",MIT,", ",GPL-3.0,"), encoding="utf-8")
        self.assertTrue(any("từng ô" in e for e in checker.validate(self.root)))

    def test_stars_boolean_is_not_integer_measurement(self):
        self.project["stars"] = True
        self.write()
        self.assertTrue(any("stars" in e for e in checker.validate(self.root)))

    def test_missing_anchor_and_source_do_not_claim_code_read(self):
        self.project["profile_anchor"] = "01-sample/README.md#missing"
        self.project["sources"] = []
        self.write()
        errors = checker.validate(self.root)
        self.assertTrue(any("neo không tồn tại" in e for e in errors))
        self.assertTrue(any("nguồn" in e or "sources" in e for e in errors))

    def test_invalid_calendar_date_rejected(self):
        self.project["last_verified_at"] = "2026-02-30"
        self.write()
        self.assertTrue(any("ngày" in e for e in checker.validate(self.root)))

    def test_entity_ids_are_unique_even_when_names_differ(self):
        self.data["projects"].append(dict(self.project, name="Different entity"))
        self.data["meta"]["count"] = 2
        self.write()
        self.assertTrue(any("id trùng" in e for e in checker.validate(self.root)))

    def test_profile_cannot_escape_repository(self):
        self.project["profile_anchor"] = "../outside.md#evidence"
        self.write()
        self.assertTrue(any("nằm trong kho" in e for e in checker.validate(self.root)))

    def test_same_upstream_can_have_distinct_entities(self):
        self.data["projects"].append(dict(self.project, id="sample-plugin", name="Sample plugin"))
        self.data["meta"]["count"] = 2
        self.write()
        self.assertEqual(checker.validate(self.root), [])

    def test_fenced_example_is_not_real_anchor(self):
        text = "# Heading\n```md\n## Example\n```\n## Real\n## Real\n"
        self.assertEqual(checker.markdown_anchors(text), {"heading", "real", "real-1"})

    def test_malformed_optional_values_fail_without_crashing(self):
        for field, value in [("section", []), ("verification_level", []), ("profile_anchor", "http://[")]:
            with self.subTest(field=field):
                original = self.project[field]
                self.project[field] = value
                self.write()
                self.assertTrue(checker.validate(self.root))
                self.project[field] = original
        self.data["meta"]["schema_version"] = "2"
        self.write()
        self.assertTrue(checker.validate(self.root))

    def test_null_handoff_fields_report_validation_errors(self):
        handoff = dict(meta=None, items=[dict(id="XT-H-001", date="2026-11-02", column="deeper",
                                            stored_ref=["01 §1"], profile_anchors=None, xt_ids=None)])
        (self.root / "data/xt-handoff.json").write_text(json.dumps(handoff), encoding="utf-8")
        errors = checker.validate(self.root)
        self.assertTrue(any("profile_anchors" in e for e in errors))
        self.assertTrue(any("xt_ids" in e for e in errors))
        self.assertTrue(any("meta" in e for e in errors))

    def test_metadata_contract_rejects_missing_or_wrong_values(self):
        for field, value in [("snapshot_date", "2026-02-30"), ("count", None), ("schema_version", 3)]:
            with self.subTest(field=field):
                original = self.data["meta"][field]
                self.data["meta"][field] = value
                self.write()
                self.assertTrue(checker.validate(self.root))
                self.data["meta"][field] = original
        del self.data["meta"]["snapshot_date"]
        self.write()
        self.assertTrue(checker.validate(self.root))

    def test_present_optional_fields_cannot_hide_invalid_types(self):
        for field, value in [("verification_level", None), ("sources", None), ("verified_ref", "bad"), ("repo", "chủ/repo")]:
            with self.subTest(field=field):
                original = self.project[field]
                self.project[field] = value
                self.write()
                self.assertTrue(checker.validate(self.root))
                self.project[field] = original

    def test_binary_profile_reports_error_instead_of_crash(self):
        (self.root / "01-sample/binary.bin").write_bytes(b"\xff\xfe")
        self.project["profile_anchor"] = "01-sample/binary.bin#evidence"
        self.write()
        self.assertTrue(any("UTF-8" in e for e in checker.validate(self.root)))

    def test_nested_short_fence_does_not_invent_anchor(self):
        text = "````md\n```\n## Fake\n```\n````\n## Real\n"
        self.assertEqual(checker.markdown_anchors(text), {"real"})

    def test_html_examples_and_comments_are_not_real_anchors(self):
        text = '`<a id="inline"></a>`\n<!-- <a id="comment"></a> -->\n<a id="real"></a>\n'
        self.assertEqual(checker.markdown_anchors(text), {"real"})

    def test_null_byte_in_path_reports_error(self):
        self.project["profile_anchor"] = "01-sample/%00#evidence"
        self.write()
        self.assertTrue(any("đường dẫn" in e for e in checker.validate(self.root)))


if __name__ == "__main__":
    unittest.main()
