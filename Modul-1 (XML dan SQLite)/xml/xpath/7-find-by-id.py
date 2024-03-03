import xml.etree.ElementTree as ET 

# Membaca file XML 
tree = ET.parse('D:/My Wish/Collage Data/Semester 6/Teknologi Basis Data/Praktikum-TBD/Modul-1 (XML dan SQLite)/xml/xpath/books.xml')
root = tree.getroot() 

# ID Buku yang ingin dicari 
book_id = 2

# Mencari buku berdasarkan id 
found_book = root.find(f".//book[@id='{book_id}']")


# Jika buku ditemukan, tampilkan informasinya 
if found_book is not None:
    title = found_book.find('title').text
    author = found_book.find('author').text
    print(f"Book found - Title : {title}, Author :{author}")
else:
    print(f"Book with id '{book_id}' not found.")