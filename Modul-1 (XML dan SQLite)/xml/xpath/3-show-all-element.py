import xml.etree.ElementTree as ET 

# Membaca file XML
tree = ET.parse('D:/My Wish/Collage Data/Semester 6/Teknologi Basis Data/Praktikum-TBD/Modul-1 (XML dan SQLite)/xml/xpath/books.xml')
root = tree.getroot()

# Mencocokan semua elemen menggunakan ekspresi XPath 

all_elements = root.findall('.//')

# Menampilkan semua element yang cocok 
for element in all_elements:
    print(element.tag)
