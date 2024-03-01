import xml.etree.ElementTree as ET

# Membaca file xml 
tree = ET.parse("D:/SMT 6/Praktikum TBD/Praktikum-TBD/Modul-1 (XML dan SQLite)/121450128/xml/mahasiswa.xml")
root = tree.getroot()

for mahasiswa in root.findall("./mahasiswa[jurusan='Arsitektur']"):
    nim = mahasiswa.find("nim").text
    nama = mahasiswa.find("nama").text
    alamat = mahasiswa.find("alamat").text
    print(f"NIM: {nim}, Nama: {nama}, Alamat: {alamat}")
# Lengkapi Code sesuai output ini

# Output; 
# Mahasiswa dengan jurusan Arsitektur 
# NIM: 111222333, Nama: Charlie, Alamat: Lampung
# NIM: 444555666, Nama: Diana, Alamat: Yogyakarta
