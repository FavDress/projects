import json, csv
from pathlib import Path
import pytest
from src.lab05.json_csv import json_to_csv, csv_to_json


def write_json(path: Path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def read_csv_rows(path: Path):
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [{"name": "Alice", "age": 22}, {"name": "Bob", "age": 25}]
    write_json(src, data)

    json_to_csv(str(src), str(dst))
    rows = read_csv_rows(dst)
    assert len(rows) == 2
    assert set(rows[0]) >= {"name", "age"}


def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    src.write_text("name,age\nAlice,22\nBob,25\n", encoding="utf-8")

    csv_to_json(str(src), str(dst))
    obj = json.loads(dst.read_text(encoding="utf-8"))
    assert isinstance(obj, list) and len(obj) == 2
    assert set(obj[0]) == {"name", "age"}


def test_json_to_csv_invalid_json(tmp_path: Path):
    src = tmp_path / "invalid.txt"
    src.write_text("invalid content", encoding="utf-8")
    with pytest.raises(ValueError):
        json_to_csv(str(src), str(tmp_path / "out.csv"))


def test_json_to_csv_invalid_csv(tmp_path: Path):
    csv_path = tmp_path / "invalid.txt"
    csv_path.write_text("invalid content", encoding="utf-8")
    with pytest.raises(ValueError):
        json_to_csv(tmp_path / "input.json", str(csv_path))


def test_json_to_csv_not_exist(tmp_path: Path):
    src = tmp_path / "no_exist.json"
    with pytest.raises(FileNotFoundError):
        json_to_csv(str(src), str(tmp_path / "out.csv"))


def test_json_to_csv_empty_raises(tmp_path: Path):
    src = tmp_path / "empty.json"
    src.write_text("[]", encoding="utf-8")
    with pytest.raises(ValueError):
        json_to_csv(str(src), str(tmp_path / "out.csv"))


def test_csv_to_json_suffix_json(tmp_path: Path):
    json_invalid = tmp_path / "invalid.txt"
    json_invalid.write_text("[]", encoding="utf-8")
    with pytest.raises(ValueError):
        csv_to_json(tmp_path / "input.csv", json_invalid)


def test_csv_to_json_suffix_csv(tmp_path: Path):
    csv_invalid = tmp_path / "invalid.txt"
    csv_invalid.write_text("1,2", encoding="utf-8")
    with pytest.raises(ValueError):
        csv_to_json(csv_invalid, str(tmp_path / "out.json"))


def test_csv_to_json_no_header_raises(tmp_path: Path):
    src = tmp_path / "bad.csv"
    src.write_text("", encoding="utf-8")
    with pytest.raises(ValueError):
        csv_to_json(str(src), str(tmp_path / "out.json"))


def test_missing_file_raises():
    with pytest.raises(FileNotFoundError):
        csv_to_json("nope.csv", "out.json")
