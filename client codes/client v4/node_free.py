import os
from client_database import *
from node import node_id



print('Trying to inserting node is free into database')

try:
    node_id = str(node_id)
    mycursor = mydb.cursor()
    sql = "INSERT INTO free_node (node_id) VALUES (%s)"
    val = (node_id,)
    mycursor.execute(sql, val)

    mydb.commit()
    print('Inserted node is free into database')

except:
    print('node already in database')
#
#sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
#val = ("John", "Highway 21")
#mycursor.execute(sql, val)
#
#mydb.commit()



os.system('python get_code.py')


