import xml.etree.ElementTree as ET 

# Membaca file XML
tree = ET.parse('../xml/xpath/books.xml')
root = tree.getroot()

# Mencari semua buku dengan genre "fiction"
fiction_books = root.findall("book[genre='Fiction']")

# Menampilkan informasi buku 
for book in fiction_books:
    title = book.find('title').text
    author = book.find('author').text
    print(f"Title: {title}, Author : {author}")
