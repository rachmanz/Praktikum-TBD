import xml.etree.ElementTree as ET 

# Membaca file XML
tree = ET.parse('../xml/xpath/books.xml')
root = tree.getroot()

# Mencocokan semua elemen menggunakan ekspresi XPath 

all_elements = root.findall('.//')

# Menampilkan semua element yang cocok 
for element in all_elements:
    print(element.tag)
