import xm.etree.ElementTree as ET 

# Membaca file XML
tree = ET.parse('data.xml')
root = tree.getroot()

# Mencari semua buku dengan genre "fiction"
fiction_book = root.findall("book[genre='Fiction]")

# Menampilkan informasi buku 
for book in fiction_books:
    title = book.find('title').text
    author = book.find('author').text
    print(f"Title: {title}, Author : {author}")
