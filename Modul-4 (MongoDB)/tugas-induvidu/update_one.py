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


# Criteria to find the document to update
filter_criteria = {"pengarang": "Stephen Hawking"}

# New values to set
new_values = {"$set": {"kategori": "Popular Science"}}

# Perform the update
collection.update_one(filter_criteria, new_values)

print("Data updated successfully.")