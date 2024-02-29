import xml.etree.ElementTree as ET 

# Membaca file XML 
tree = ET.parse("../Modul-1 (XML dan SQLite)/xml/books.xml")
root = tree.getroot() 


# Mencari semua buku dengan genre "Fiction"
fiction_books = root.findall(".//book[genre='Fiction']")

# Menampilkan informasi buku 
for book in fiction_books:
    title = book.find('title').text 
    author = book.find('author').text 
    print(f"Title : {title}, Author : {author}")


# Mencari semua buku dengan judul '1984'
fiction_books = root.find(".//book[title='1984']")

# Jika buku ditemukan, tampilkan informasi buku 
if book is not None:
    title = book.find('title').text 
    author = book.find('author').text 
    print(f"Title : {title}, Author : {author}")
else:
    print("Book not found")

# Mencari buku dengan judul "1985" yang tidak ada didalam books.xml 
book = root.find(".//book[title='1985']")

# Jika buku ditemukan, tampilkan informasi buku 
if book is not None:
    title = book.find('title').text 
    author = book.find('author').text 
    print(f"Title : {title}, Author : {author}")
else:
    print("Book not found")
