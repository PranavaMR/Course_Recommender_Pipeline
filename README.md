# BITS Course Recommender — data preprocessing

## Layout
```
timetable.py            timetable PDF  -> tables: courses, sections, equivalents
handouts.py             handout PDFs   -> table: handouts  (+ handouts_review.csv)
tests/                  pytest cases built from real lines of the PDFs
data/raw/               input PDFs (timetable.pdf, handouts/*.pdf)
data/processed/         output: academic.db (SQLite), handouts_review.csv
```

## Run
```
pip install -r requirements.txt
python -m pytest -q
python timetable.py data/raw/timetable.pdf data/processed/academic.db
python handouts.py  data/raw/handouts      data/processed/academic.db
```
Both scripts write into the same `academic.db`; each one replaces only its own tables.

## Output: `data/processed/academic.db`
| table | one row per | key columns |
|---|---|---|
| `courses` | timetable course entry | comp_code, code, title, units |
| `sections` | lecture / tutorial / practical section | comp_code, code, section, cancelled, slots ("M4 W4 T10"), midsem, compre, raw |
| `equivalents` | equivalent-course pair | code, equivalent_code |
| `handouts` | course handout | code, has_midsem, has_compre, components (JSON), makeup_level, attendance, topics, needs_review |

Value sets:
- `makeup_level`: none / strict / moderate / lenient / unknown (quote kept in `makeup_quote`)
- `attendance`: graded / required / not_graded / expected_only / unknown (quote kept in `attendance_quote`)
- `has_midsem`: 1 / 0 / NULL (NULL = could not tell)

Handouts the rules could not fully parse are listed in `handouts_review.csv`; these are
the only ones sent to the AI fallback. On the 23 sample handouts: 18 clean, 5 flagged.
