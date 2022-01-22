import sqlite3
import pandas as pd
import xml.etree.ElementTree as xml

con = sqlite3.connect("data.sqlite")
cur = con.cursor()

# manufacturers = pd.read_sql_query(
#     'SELECT manufacturer_id, name FROM MANUFACTURER ;', con , 'manufacturer_id')
#print (manufacturers)

#global manufacturers
manufacturers = {}
for row in cur.execute(
    'SELECT manufacturer_id, name FROM MANUFACTURER;'):
    manufacturers[row[0]] = row[1]
#print(manufacturers)

def getName(id):
    return manufacturers.get(id)
#print(getName('13'))


# def getName(id):
#     return  pd.read_sql_query('SELECT NAME FROM MANUFACTURER WHERE manufacturer_id == ? ;' , con,  params =[id] ).to_string()
    
#print (getName("25")) 
#print (type(getName("25")))