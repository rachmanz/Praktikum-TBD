import pymongo 

client = pymongo.MongoClient("mongodb://localhost:27017")

# Pilih database yang akan digunakan 
my_db = client["sekolah"]

mycol = my_db["mahasiswa"]

myquery = {"nim" : 121450113}
newvalues = {"$set" : {"kelas" : "RB"}}
mycol.update_one(myquery, newvalues)


for x in mycol.find():
    print(x)