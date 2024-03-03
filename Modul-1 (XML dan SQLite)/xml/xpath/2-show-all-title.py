import xml.etree.ElementTree as ET

# Membaca file XML 
tree = ET.parse('../xml/xpath/books.xml')
root = tree.getroot()

# Ekspresi XPath
titles = root.findall('book/title')

# Menampilkan data
for title in titles:
    print(title.text)