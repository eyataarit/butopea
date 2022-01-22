import sqlite3
import pandas as pd
import xml.etree.ElementTree as xml

con = sqlite3.connect("data.sqlite")
productImages = pd.read_sql_query(
    'SELECT * FROM PRODUCT_IMAGE ', con )
#print (productImages.head())

def getImage(id):
    return  pd.read_sql_query('SELECT IMAGE FROM PRODUCT_IMAGE WHERE PRODUCT_id == ? ;' , con,  params =[id] ).to_string()
#print (getImage("196"))
