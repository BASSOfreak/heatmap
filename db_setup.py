import sqlite3
con = sqlite3.connect("db")

cur = con.cursor()


cur.execute("""
    CREATE TABLE IF NOT EXISTS GPSFILES (
        id INTEGER PRIMARY KEY,
        name char(40) NOT NULL,
        date DATETIME NOT NULL,
        distance FLOAT NOT NULL,
        duration FLOAT NOT NULL,
        file BLOB NOT NULL
    );
    """)
con.commit()
con.close()


