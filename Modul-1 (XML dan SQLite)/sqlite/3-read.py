import sqlite3 as sq 


def get_all_users():
    conn = sq.connect("sqlite/latihan.sqlite")
    c = conn.cursor() 
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    conn.close()
    return rows


print(get_all_users())