import xml.etree.ElementTree as ET 


# Membaca File XML 
tree = ET.parse('xml/books.xml')
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