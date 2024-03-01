import sqlite3 as sq


def create_table():
    conn = sq.connect('D:/My Wish/Collage Data/Semester 6/Teknologi Basis Data/Praktikum-TBD/Modul-1 (XML dan SQLite)/sqlite/latihan.sqlite')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

    conn.commit() 
    conn.close() 

    print('Table berhasil dibuat')

create_table() 