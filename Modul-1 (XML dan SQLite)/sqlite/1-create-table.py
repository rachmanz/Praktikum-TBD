import sqlite3 as sq


def create_table():
    conn = sq.connect('sqlite/latihan.sqlite')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

    conn.commit() 
    conn.close() 

    print('Table berhasil dibuat')

# Tambahan di bagian atas
create_table() 