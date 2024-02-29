import xml.etree.ElementTree as ET 

# Membuat root element 
root = ET.Element("books")

# Membuat child elemens untuk setiap buku 
book1 = ET.SubElement(root, "book")
book1.set("id", "1")

title1 = ET.SubElement(book1, "title")
title1.text = "The Catcher in the Rye"

author1 = ET.SubElement(book1, "author")
author1.text = "J.D Salinger"

genre1 = ET.SubElement(book1, "genre")
genre1.text = "Fiction"

price1 = ET.SubElement(book1, "price")
price1.text = "20.00"

