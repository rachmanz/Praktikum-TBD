from pymongo import MongoClient

# Menghubungkan kedalam server mongodb
try:
    client = MongoClient('mongodb://localhost:27017/')  # Ganti mongodb string connection
    print("Connected successfully to MongoDB server!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

# Akses Spesifik Data 
db = client['Abdurrahman_Alatsary']

# Akses Spesifik Collections
collection = db['perpustakaan']

# List data yang akan dimasukan
data = [
    {
        "judul" : "Laskar Pelangi", 
        "pengarang" : "Abdurrahman A", 
        "penerbit" : "ITERA", 
        "tahun_terbit" : 2024, 
        "kategori" : "Fiksi"
    },
    {
        "judul" : "Machine Learning for Beginner", 
        "pengarang" : "Abdurrahman A", 
        "penerbit" : "Databits Corp", 
        "tahun_terbit" : 2024, 
        "kategori" : "Pemrograman"
    },
    {
        "judul" : "Soft Skill to Show", 
        "pengarang" : "Abdurrahman A", 
        "penerbit" : "Databits Corp", 
        "tahun_terbit" : 2024, 
        "kategori" : "Motivation"
    }
]


# Memasukan data yang ada
collection.insert_many(data)

# Notifikasi data sudah dimasukan
print("Data inserted successfully.")

# Menutup Koneksi dengan mongodb
client.close()