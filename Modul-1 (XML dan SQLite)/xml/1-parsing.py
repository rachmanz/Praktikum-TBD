import xml.etree.ElementTree as ET

# Membaca file xml 
tree = ET.parse("../Modul-1 (XML dan SQLite)/xml/books.xml")
root = tree.getroot()

# Menampilkan informasi tentang setiap buku 
for boook in root.findall('book'):
    # Mengakses informasi buku 
    title = book.find('title').text
    author = book.find('author').text
    year = book.find('year').text
    price = book.find('price').text
    
    # Menampilkan informasi buku
    print("Title:", title)
    print("Author:", author)
    print("Year:", year)
    print("Price:", price)
    print()