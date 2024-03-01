import xml.etree.ElementTree as ET

# Membaca file xml 
tree = ET.parse("121450128/xml/mahasiswa.xml")
root = tree.getroot()

# Membuat elemen untuk buku baru 
new_mahasiswa = ET.Element('data')
new_mahasiswa.set('nim', '121450128')

# Menambahkan sub-elemen untuk buku baru 
nama = ET.SubElement(new_mahasiswa, 'nama')
nama.text = 'Abdurrahman Al-atsary'

jurusan = ET.SubElement(new_mahasiswa, 'jurusan')
jurusan.text = 'Sains Data'

alamat = ET.SubElement(new_mahasiswa, 'alamat')
alamat.text = 'Lampung'

# Menambahkan buku baru ke dalam root
root.append(new_mahasiswa)
ET.indent(tree, space="\t", level=0)

# Menyimpan perubahan kedalam file XML 
tree.write('D:/My Wish/Collage Data/Semester 6/Teknologi Basis Data/Praktikum-TBD/Modul-1 (XML dan SQLite)/121450128/xml/mahasiswa.xml')