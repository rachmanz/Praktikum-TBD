import pymongo 

client = pymongo.MongoClient("mongodb://localhost:27017")

# Pilih database yang akan digunakan 
my_db = client["sekolah"]

mycol = my_db["mahasiswa"]

mydict = {
    "nama" : "Syifa",
    "nim" : 121450113, 
    "kelas": "RC" 
}

x = mycol.insert_one(mydict)
print(x.inserted_id)

for i in mycol.find():
    print(i)