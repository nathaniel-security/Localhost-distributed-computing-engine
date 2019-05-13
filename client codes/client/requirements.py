import os
from client_database_connection import mycursor
from ftp import *
from data import ftp_local , ftp_remotepath

#get requirements.txt if any
    mycursor.execute("SELECT requirements FROM data")
    re = mycursor.fetchone()

if(re == 0):
    print("no extra dependicies")
else:
    mycursor.execute("SELECT ftp_hostname FROM data")
    hostname = mycursor.fetchone()

    mycursor.execute("SELECT ftp_password FROM data")
    ftp_password = mycursor.fetchone()

    mycursor.execute("SELECT ftp_username FROM data")
    ftp_username = mycursor.fetchone()

    connect(hostname,ftp_username,ftp_password,localpath,ftp_remotepath)

    



command = 'pip install -r requirements.txt'
os.system(command)
os.system("python node_free.py")

