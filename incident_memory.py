import sqlite3

def init_db():
    conn = sqlite3.connect("incidents.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS incidents(
        id INTEGER PRIMARY KEY,
        issue TEXT,
        root_cause TEXT,
        resolution TEXT
    )
    """)

    conn.commit()
    conn.close()

def add_incident(issue, cause, resolution):
    conn = sqlite3.connect("incidents.db")
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO incidents(issue, root_cause, resolution)
    VALUES(?,?,?)
    """, (issue, cause, resolution))

    conn.commit()
    conn.close()

def get_incidents():
    conn = sqlite3.connect("incidents.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM incidents")

    rows = cur.fetchall()

    conn.close()

    return rows

def clear_incidents():
    conn = sqlite3.connect("incidents.db")
    cur = conn.cursor()

    cur.execute("DELETE FROM incidents")

    conn.commit()
    conn.close()