from pymongo import MongoClient

# Menghubungkan kedalam server mongodb
try:
    client = MongoClient('mongodb://localhost:27017/')  # Ganti mongodb string connection
    print("Connected successfully to MongoDB server!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

# Akses Spesifik Data 
db = client['Sasa_Rahma_LiaS']

# Akses Spesifik Collections
collection = db['buku']

# Mencari kriteria yang mau dihapus
filter_criteria = {"pengarang": "Lewis Carroll"}

# Eksekusi kriteria yang mau dihapus 
collection.delete_one(filter_criteria)

print("Berhasil menghapus 1 baris data")

# Disconnect dari MongoDB
client.close()