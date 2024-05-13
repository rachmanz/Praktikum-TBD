from pymongo import MongoClient

# Menghubungkan kedalam server mongodb
try:
    client = MongoClient('mongodb://localhost:27017/')  # Ganti mongodb string connection
    print("Connected successfully to MongoDB server!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

# Akses Spesifik Data 
db = client['Sasa_Rahma_Lia']

# Akses Spesifik Collections
collection = db['perpustakaan']

# List data yang akan dimasukan
data = [
    {
        "judul" : "The Hitchhiker's Guide to the Galaxy", 
        "pengarang" : "Douglas Adams", 
        "penerbit" : "Pan Books", 
        "tahun_terbit" : 1979, 
        "kategori" : "Fiksi Sains"
    },
    {
        "judul" : "The Da Vinci Code", 
        "pengarang" : "Dan Brown", 
        "penerbit" : "Doubleday", 
        "tahun_terbit" : 2003, 
        "kategori" : "Misteri"
    },
    {
        "judul" : "The Hunger Games", 
        "pengarang" : "Suzanne Collins", 
        "penerbit" : "Scholastic Corporation", 
        "tahun_terbit" : 2008, 
        "kategori" : "Fiksi Distopia"
    }, 
    {
        "judul" : "Harry Potter and the Sorcerer's Stone", 
        "pengarang" : "J. K. Rowling", 
        "penerbit" : "Bloomsbury", 
        "tahun_terbit" : 1997, 
        "kategori" : "Fantasi"
    },
    {
        "judul" : "A Brief History of Time", 
        "pengarang" : "Stephen Hawking", 
        "penerbit" : "Bantam Books", 
        "tahun_terbit" : 1988, 
        "kategori" : "Ilmu Pengetahuan"
    }
]


# Memasukan data yang ada
collection.insert_many(data)

# Notifikasi data sudah dimasukan
print("Data inserted successfully.")

# Menutup Koneksi dengan mongodb
client.close()
