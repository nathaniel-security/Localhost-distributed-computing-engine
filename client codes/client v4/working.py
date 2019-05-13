from ftp_data import *
import os
from client_database import *
from node import node_id
from ftp_data import *


filename = 'requirements.txt'
localfile = open(filename, 'wb')
ftp.retrbinary('RETR ' + filename, localfile.write, 1024)



sql = "SELECT node_id FROM node_data where node_id = '"+node_id +"' AND node_password = '"+node_password + "'"
mycursor.execute(sql)
myresult = mycursor.fetchone()
for x in myresult:
    print(x)









node_id = str(node_id)
mycursor = mydb.cursor()
sql = "INSERT INTO node_code (node_id,code_name) VALUES (%s,%s)"
val = (node_id,code_name,)
mycursor.execute(sql, val)

mydb.commit()          