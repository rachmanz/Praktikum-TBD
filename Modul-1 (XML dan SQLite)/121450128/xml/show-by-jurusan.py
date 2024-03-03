import xml.etree.ElementTree as ET 

# Membaca file XML
tree = ET.parse("../121450128/xml/mahasiswa.xml")
root = tree.getroot()

# Pembacaan dari nama jurusan yang ada didalam data
for data in root.findall("./data['Arsitektur']"):
    nim = data.get('nim')
    nama = data.find("nama").text
    alamat = data.find("alamat").text
    print(f"NIM: {nim}, Nama: {nama}, Alamat: {alamat}")