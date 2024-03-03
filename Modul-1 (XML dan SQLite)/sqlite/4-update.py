import sqlite3 as sq

def get_all_users():
    conn = sq.connect("../sqlite/latihan.sqlite")
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    conn.close() 
    return rows 


def update_user(id, name, age): 
    conn = sq.connect("../sqlite/latihan.sqlite")
    c = conn.cursor()
    c.execute("UPDATE users SET name = ?, age = ? WHERE id = ?", (name, age, id))
    conn.commit() 
    conn.close() 

    print("User berhasil ditambahkan")

update_user(4, "Jhonny Editer", 32)
print(get_all_users())