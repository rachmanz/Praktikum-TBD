import xml.etree.ElementTree as ET

# Membaca file xml 
tree = ET.parse("121450128/xml/mahasiswa.xml")
root = tree.getroot()

# Menampilkan informasi tentang setiap buku 
for data in root.findall('data'):
    # Mengakses informasi buku
    nim = data.get('nim')
    nama = data.find('nama').text
    jurusan = data.find('jurusan').text
    alamat = data.find('alamat').text
    
    # Menampilkan informasi buku
    print(f"NIM: {nim}")
    print(f"Nama: {nama}")
    print(f"Jurusan: {jurusan}")
    print(f"Alamat: {alamat}")
    print()