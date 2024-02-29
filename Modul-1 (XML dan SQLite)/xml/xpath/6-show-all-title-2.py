# .//title : mencocockan semua element "title" didalam dokumen menggunakan tanda

import xml.etree.ElementTree as ET 

# Membaca file XML 
tree = ET.parse('xml/books.xml')
root = tree.getroot() 


# Ekspresi xpath 
titles = root.findall('.//title')

# Menampilkan judul buku
for title in titles:
    print(title.text)