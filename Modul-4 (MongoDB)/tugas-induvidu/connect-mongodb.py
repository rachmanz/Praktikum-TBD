from pymongo import MongoClient

# menghubungkan kedalam server mongodb
try:
    client = MongoClient('mongodb://localhost:27017/')  # Ganti mongodb string connection
    print("Connected successfully to MongoDB server!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

# Akses Spesifik Data 
db = client['Abdurrahman_Alatsary']

# Akses Spesifik Collections
collection = db['perpustakaan']

# Menutup Koneksi dengan mongodb
client.close()