import sqlite3 as sq 


def get_all_users():
    conn = sq.connect("D:/My Wish/Collage Data/Semester 6/Teknologi Basis Data/Praktikum-TBD/Modul-1 (XML dan SQLite)/sqlite/latihan.sqlite")
    c = conn.cursor() 
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    conn.close()
    return rows


print(get_all_users())