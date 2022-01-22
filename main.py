import xml.etree.ElementTree as xml

from models.Product import products
from models.Manufacturer import getName
from models.ProductDescription import getTitle, getDescription

def GenerateXML(feed) :
    root = xml.Element("products")
    for product_id,value in products.items():     
       #print(value)
        p1 = xml.Element("product")
        root.append(p1)
        b1 = xml.SubElement(p1,"id") 
        b1.text = product_id
        b1 = xml.SubElement(p1,"title") 
        b1.text = getTitle(product_id)
        b1 = xml.SubElement(p1,"description") 
        b1.text = getDescription(product_id)
        b1 = xml.SubElement(p1,"link") 
        b1.text = 'butopea.com/p/' + product_id
        b1 = xml.SubElement(p1,"image_link") 
        b1.text = 'butopea.com/' + value['image']
        b1 = xml.SubElement(p1,"additionnal_image_link") 
        b1 = xml.SubElement(p1,"availbility") 
        b1 = xml.SubElement(p1,"price") 
        b1.text =  value['price']        
        b1 = xml.SubElement(p1,"brand") 
        brand = getName(value['manufacturer_id'])
        b1.text = brand
        b1 = xml.SubElement(p1,"condition") 
        b1.text = "new"

    tree = xml.ElementTree(root)
    with open(feed,"wb") as files : 
        tree.write(files)
        
if __name__=="__main__":
    GenerateXML("feed.xml")