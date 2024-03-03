import xml.etree.ElementTree as ET 


# Membaca File XML 
tree = ET.parse('D:/My Wish/Collage Data/Semester 6/Teknologi Basis Data/Praktikum-TBD/Modul-1 (XML dan SQLite)/xml/xpath/books.xml')
root = tree.getroot()

# XPath : /book/book
books = root.findall('book')

# Menampilkan judul buku 
for book in books:
    # Mengakses title buku yang berada dalam konteks saat ini 
    title = book.find('./title').text

    # Menampilkan informasi buku 
    print(f'Title : {title}')
    print()