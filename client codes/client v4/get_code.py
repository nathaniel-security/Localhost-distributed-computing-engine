from ftp_data import *
import os
from client_database import *
from node import *
import time



print('getting code...')

a = 0
while True:
    time.sleep(2)
    a=a+1
    try:
        sql = "SELECT code_name FROM node_code where node_id = '"+node_id +"'"
        mycursor.execute(sql)
        myresult = mycursor.fetchone()
        for x in myresult:
            filename=x
        print(filename)
        mydb.commit()
        break
    
    except Exception as error:
        
        print("\nNothing in database\n")
        mydb.commit()
        #print(error)

    print('Try number:- ',a)

#filename = 'requirements.txt'
localfile = open(filename, 'wb')
ftp.retrbinary('RETR ' + filename, localfile.write, 1024)

print("Running code")
command = 'python ' + filename
print(command)
os.system(command)
