import sqlite3 as sq3

def create_table():
    conn = sq3.connect("D:/My Wish/Collage Data/Semester 6/Teknologi Basis Data/Praktikum-TBD/Modul-1 (XML dan SQLite)/121450128/sqlite/mahasiswa2.sqlite")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS mahasiswa
                (id INTEGER PRIMARY KEY, name TEXT, prodi TEXT)''')

    conn.commit() 
    conn.close() 

    print('Table berhasil dibuat')

create_table() 

def addmahasiswa(id, name, prodi):
    conn = sq3.connect('D:/My Wish/Collage Data/Semester 6/Teknologi Basis Data/Praktikum-TBD/Modul-1 (XML dan SQLite)/121450128/sqlite/mahasiswa2.sqlite')
    c = conn.cursor() 
    c.execute("INSERT INTO mahasiswa (id, name, prodi) VALUES (?, ?, ?)", (id, name, prodi))
    conn.commit() 
    conn.close()

    print("User berhasil ditambahkan")

def delete_mahasiswa(id):
    conn = sq3.connect("D:/My Wish/Collage Data/Semester 6/Teknologi Basis Data/Praktikum-TBD/Modul-1 (XML dan SQLite)/121450128/sqlite/mahasiswa2.sqlite")
    c = conn.cursor() 
    c.execute("DELETE FROM mahasiswa WHERE id = ?", (id,)) 
    conn.commit() 
    conn.close() 

    print("Mahasiswa berhasil di drop out (DO)")

def get_all_mahasiswa():
    conn = sq3.connect("D:/My Wish/Collage Data/Semester 6/Teknologi Basis Data/Praktikum-TBD/Modul-1 (XML dan SQLite)/121450128/sqlite/mahasiswa2.sqlite")
    c = conn.cursor() 
    c.execute("SELECT * FROM mahasiswa")
    rows = c.fetchall()
    conn.close()
    return rows

def update_mahasiswa(id, name, prodi): 
    conn = sq3.connect("D:/My Wish/Collage Data/Semester 6/Teknologi Basis Data/Praktikum-TBD/Modul-1 (XML dan SQLite)/121450128/sqlite/mahasiswa2.sqlite")
    c = conn.cursor()
    c.execute("UPDATE mahasiswa SET name = ?, prodi = ? WHERE id = ?", (name, prodi, id))
    conn.commit() 
    conn.close() 

    print("Mahasiswa berhasil ditambahkan")

# Menambahkan Mahasiswa 
addmahasiswa(101, "Arya Wicaksono Pratama", "Program Studi Teknik Industri")
addmahasiswa(102, "Sofia Elara", "Program Studi Teknik Pertambangan")
addmahasiswa(103, "Sasa Rahma Lia", "Program Studi Sains Data")

# Mencetak seluruh mahasiswa 
print("All Mahasiswa")
print(get_all_mahasiswa())

# Update Mahasiswa 
update_mahasiswa(101, "Arya Wicaksono Pratama", "Program Studi Teknik Perkeretaapian")
update_mahasiswa(103, "Sasa Rahma Lia", "Program Studi Arsitektur Lanskap")

print("After Update:")
print(get_all_mahasiswa())

# Delete Mahasiswa 
delete_mahasiswa(102)
print("After delete:")
print(get_all_mahasiswa())