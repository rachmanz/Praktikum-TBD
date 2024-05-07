import pymongo 

client = pymongo.MongoClient("mongodb://localhost:27017")

# Pilih database yang akan digunakan 
my_db = client["sekolah"]

mycol = my_db["mahasiswa"]

myquery = {"nama" : "Syifa"}
mycol.delete_one(myquery)


for i in mycol.find():
    print(i)