import xml.etree.ElementTree as ET

# Membaca file xml
tree = ET.parse("121450128/xml/mahasiswa.xml")
root = tree.getroot()

# Loop through mahasiswa elements with jurusan 'Arsitektur'
for data in root.findall("./data[jurusan='Arsitektur']"):
    nim = data.get("nim")
    nama = data.find("nama").text
    alamat = data.find("alamat").text
    print(f"NIM: {nim}, Nama: {nama}, Alamat: {alamat}")