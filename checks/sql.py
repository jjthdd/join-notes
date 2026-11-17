import json
import sqlite3
from pathlib import Path

page = (Path(__file__).resolve().parents[1] / "index.html").read_text(encoding="utf-8")
examples, _ = json.JSONDecoder().raw_decode(page.split("const examples = ", 1)[1])
db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE student(id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE enrolment(student_id INTEGER, active INTEGER);
""")
for table, columns, rows in examples["sources"]:
    db.executemany(f"INSERT INTO {table} VALUES (?, ?)", rows)
for question in examples["questions"]:
    for example in question:
        result = db.execute(example["sql"])
        actual = [list(row) for row in result]
        assert actual == example["rows"], (example["title"], actual)
        assert [field[0] for field in result.description] == ["name", "active"]
        print(example["title"], actual)
