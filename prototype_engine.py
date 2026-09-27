import sqlite3
con = sqlite3.connect("data/processed/academic.db")
prog = "COMPUTER SCIENCE"

rows = con.execute("SELECT code FROM programme_courses WHERE programme = ? AND category = 'core'", (prog,)).fetchall()
print(rows)                    # list of tuples
print({r[0] for r in rows})    # set of codes

row = con.execute("SELECT del_units FROM programme_targets WHERE programme = ?", (prog,)).fetchone()
print(row, row[0])