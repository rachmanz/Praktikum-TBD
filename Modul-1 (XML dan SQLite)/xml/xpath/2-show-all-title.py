import xml.etree.ElementTree as ET

# Membaca file XML 
tree = ET.parse('/xml/books.xml')
root = tree.getroot()

# Ekspresi XPath
