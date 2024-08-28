import sqlite3

def setup_db(db_name: str):
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS GPSFILES (
            id INTEGER PRIMARY KEY,
            name char(40) NOT NULL,
            hash_of_file char(50) NOT NULL,
            date DATETIME NOT NULL,
            distance FLOAT NOT NULL,
            duration FLOAT NOT NULL,
            file BLOB NOT NULL
        );
        """)
    con.commit()
    con.close()

def clear_db(db_name: str):
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    cur.execute("""
        DROP TABLE GPSFILES;
        """)
    con.commit()
    con.close()

