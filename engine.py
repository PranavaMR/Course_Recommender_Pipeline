import sqlite3
con = sqlite3.connect("data/processed/academic.db")
#written by hand


# list of programmes for the dropdown
# [('CS F211',)]
con.execute("SELECT DISTINCT programme FROM programme_courses WHERE programme != 'ALL'").fetchall()

# a programme's core / DEL codes
con.execute("SELECT code FROM programme_courses WHERE programme = ? AND category = 'core'", (prog,)).fetchall()
con.execute("SELECT code FROM programme_courses WHERE programme = ? AND category = 'del'",  (prog,)).fetchall()

# the humanities pool
con.execute("SELECT code FROM programme_courses WHERE category = 'huel'").fetchall()

# unit targets
con.execute("SELECT del_units FROM programme_targets WHERE programme = ?", (prog,)).fetchone()

# courses actually running this semester (at least one non-cancelled section)
con.execute("""SELECT DISTINCT c.comp_code, c.code, c.title, c.units FROM courses c
               JOIN sections s ON s.comp_code = c.comp_code WHERE s.cancelled = 0""").fetchall()

# equivalents
con.execute("SELECT code, equivalent_code FROM equivalents").fetchall()