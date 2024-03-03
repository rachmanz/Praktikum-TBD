import xml.etree.ElementTree as ET

# Membaca file XML 
tree = ET.parse('D:/My Wish/Collage Data/Semester 6/Teknologi Basis Data/Praktikum-TBD/Modul-1 (XML dan SQLite)/xml/xpath/books.xml')
root = tree.getroot()

# Ekspresi XPath
titles = root.findall('book/title')

# Menampilkan data
for title in titles:
    print(title.text)