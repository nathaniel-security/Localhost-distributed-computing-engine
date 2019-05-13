from ftp_data import *
import os
from client_database import *
from node import *
import time


import mysql.connector
code_name = 'helloworld'
node_id = 456
node_id = str(node_id)
code_name = str(code_name)
sql = "INSERT INTO node_code (node_id,code_name) VALUES (" + node_id + " , " + code_name+")"

mycursor.execute(sql)
mydb.commit()  
print('done')