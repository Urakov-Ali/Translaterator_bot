import sqlite3

class Infos:
    def __init__(self):
        self.conn =sqlite3.connect("kiril_data.db")
        self.c =self.conn.cursor()
        
    def create_table(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS users(
            id INTEGER,	
            username varchar(15),
            firstname varchar(15)
            )""")

    def insert(self, idi, username, firstname):
        self.c.execute("INSERT INTO users(id, username, firstname) VALUES(?,?,?)", (idi, username, firstname))
        return self.conn.commit()

    def check(self, idi):
        self.c.execute(f"SELECT id FROM users WHERE id={idi}")
        checking =self.c.fetchone()
        return checking

    def admin_notify(self, idi):
        self.c.execute(f"SELECT * FROM users WHERE id={idi}")
        data =self.c.fetchone()
        return data
    
    def count(self, idi):
        self.c.execute(f"SELECT COUNT(id) FROM users")
        data =self.c.fetchall()
        return data
    
    def users_id(self):
        self.c.execute("SELECT id,username FROM users")
        user_id =self.c.fetchall()
        return user_id

    def announce(self):
        self.c.execute("SELECT id FROM users")
        data =self.c.fetchall()
        return data





