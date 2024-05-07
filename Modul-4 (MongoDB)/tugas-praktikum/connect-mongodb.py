import pymongo 

client = pymongo.MongoClient("mongodb://localhost:27017")

# Pilih database yang akan digunakan 
my_db = client["sekolah"]
