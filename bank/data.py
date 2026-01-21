import sqlite3

class Data:
    def __init__(self):
        self.conn = sqlite3.connect("bank/database.db")
        self.cursor = self.conn.cursor()

    def starting_database(self):
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS bank
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            balance REAL NOT NULL DEFAULT 0.0)
                            """)
        self.conn.commit()

 