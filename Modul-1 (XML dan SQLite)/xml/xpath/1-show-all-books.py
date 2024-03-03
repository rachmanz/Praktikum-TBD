import xml.etree.ElementTree as ET

# Membaca file XML 
tree = ET.parse('D:/My Wish/Collage Data/Semester 6/Teknologi Basis Data/Praktikum-TBD/Modul-1 (XML dan SQLite)/xml/xpath/books.xml')
root = tree.getroot()


# Xpath : /books/books
books = root.findall("book")

# Menampilkan judul buku 
for book in books:
    # Mengakses informasi buku 
    title = book.find('title').text 
    author = book.find('author').text

    # Menampilkan informasi buku
    print(f"Title: {title}")
    print(f"Author: {author}")
    print()