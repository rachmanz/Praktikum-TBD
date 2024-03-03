import sqlite3 as sq

def get_all_users():
    conn = sq.connect("../sqlite/latihan.sqlite")
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    conn.close() 
    return rows 

def delete_user(id):
    conn = sq.connect("../sqlite/latihan.sqlite")
    c = conn.cursor() 
    c.execute("DELETE FROM users WHERE id = ?", (id,)) 
    conn.commit() 
    conn.close() 

delete_user(5)
print(get_all_users())