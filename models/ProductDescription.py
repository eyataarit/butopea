import sqlite3
import pandas as pd
import xml.etree.ElementTree as xml

con = sqlite3.connect("data.sqlite")
cur = con.cursor()

productDescriptions = {}
for row in cur.execute('SELECT * FROM PRODUCT_DESCRIPTION;'):
    productDescriptions [row[0]] = dict([('title',row[1]),('description',row[2])])
#print(productDescriptions['196']['title'])

def getTitle(id):
    return productDescriptions[id]['title']
print (getTitle('196'))

# productDescriptions = pd.read_sql_query(
#     'SELECT * FROM PRODUCT_DESCRIPTION;', con)
def getDescription(id):
    return productDescriptions[id]['description']
print(getDescription('196'))
