import sqlite3 as sq 

def add_user(name, age):
    conn = sq.connect('D:/My Wish/Collage Data/Semester 6/Teknologi Basis Data/Praktikum-TBD/Modul-1 (XML dan SQLite)/sqlite/latihan.sqlite')
    c = conn.cursor() 
    c.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit() 
    conn.close()

    print("User berhasil ditambahkan")

add_user('John', 30)
add_user('Alice', 30)