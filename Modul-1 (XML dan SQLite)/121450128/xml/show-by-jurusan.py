import xml.etree.ElementTree as ET

# Membaca file xml
tree = ET.parse("D:/My Wish/Collage Data/Semester 6/Teknologi Basis Data/Praktikum-TBD/Modul-1 (XML dan SQLite)/121450128/xml/mahasiswa.xml")
root = tree.getroot()

# Loop through mahasiswa elements with jurusan 'Arsitektur'
for data in root.findall("./data[jurusan='Arsitektur']"):
    nim = data.get("nim")
    nama = data.find("nama").text
    alamat = data.find("alamat").text
    print(f"NIM: {nim}, Nama: {nama}, Alamat: {alamat}")