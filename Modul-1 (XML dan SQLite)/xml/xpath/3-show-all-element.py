import xm.etree.ElementTree as ET 

# Membaca file XML
tree = ET.parse('data.xml')
root = tree.getroot()

# Mencocokan semua elemen menggunakan ekspresi XPath 

all_element = root.findall('.//')

# Menampilkan semua element yang cocok 
for element in all_elements:
    print(element.tag)
