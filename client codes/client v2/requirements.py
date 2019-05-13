from client_database_connection import mycursor
import os
from ftp import *






config = json.loads(open('config.json').read())
local_path = config['local path']

#check if and requirements are there
mycursor.execute("SELECT requirements FROM data")
re = mycursor.fetchone()

#get requirements.txt if any
if(re == 0):
    print("no extra dependicies")
else:
    mycursor.execute("SELECT ftp_hostname FROM data")
    hostname = mycursor.fetchone()

    mycursor.execute("SELECT ftp_password FROM data")
    ftp_password = mycursor.fetchone()

    mycursor.execute("SELECT ftp_username FROM data")
    ftp_username = mycursor.fetchone()

    mycursor.execute("SELECT ftp_remotepath FROM data")
    ftp_remotepath = mycursor.fetchone()



    connect(hostname,ftp_username,ftp_password,localpath,ftp_remotepath)

    #install requirements.txt
    command = 'pip install -r requirements.txt'
    os.system(command)
    os.system("python node_free.py")

