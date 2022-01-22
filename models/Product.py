import sqlite3
import pandas as pd
import xml.etree.ElementTree as xml

con = sqlite3.connect("data.sqlite")
cur = con.cursor()

def addCurrencyHUF(price):
    return (price) + ' HUF' 

products = {} 
for row in cur.execute(
    'SELECT product_id, image, manufacturer_id, price '
    + 'FROM PRODUCT WHERE STATUS != 0 ; '): 
    #products.append(list(row))
    priceHUF = addCurrencyHUF(row[3]) 
    products[row[0]] = dict([('image',row[1]),('manufacturer_id',row[2]),('price', addCurrencyHUF(row[3]) )])

# products is a dict 
# key : product_id 
# value : [image, manufacturer_id , price ]

#print(products['196']) 
#print(products)

con.close()

# products = pd.read_sql_query(
#     'SELECT product_id, image, manufacturer_id, price '
#     + 'FROM PRODUCT WHERE STATUS != 0  ;', con , 'product_id')
# print (type(products)) #dataframe