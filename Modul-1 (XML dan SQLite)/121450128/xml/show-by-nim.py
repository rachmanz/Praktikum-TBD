import xml.etree.ElementTree as ET

# Membaca file xml
tree = ET.parse("../121450128/xml/mahasiswa.xml")
root = tree.getroot()


target_nim = "777888999"
found = False

for data in root.findall('data'):
    nim = data.get('nim')  # Mengambil nilai atribut nim
    if nim == target_nim:
        found = True
        nama = data.find('nama').text
        jurusan = data.find('jurusan').text
        alamat = data.find('alamat').text
        
        # Menampilkan informasi mahasiswa
        print("Data Mahasiswa:")
        print(f"NIM: {nim}")
        print(f"Nama: {nama}")
        print(f"Jurusan: {jurusan}")
        print(f"Alamat: {alamat}")

if not found:
    print(f"Data mahasiswa dengan NIM {target_nim} tidak ditemukan.")

