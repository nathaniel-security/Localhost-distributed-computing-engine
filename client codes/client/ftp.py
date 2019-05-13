import os
import paramiko 

#ftp part
#hostname
# username 
# password 
# localpath 
# remotepath

def connect(hostname, username , password ,localpath ,remotepath):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username, password)
    sftp = ssh.open_sftp()
    sftp.put(localpath, remotepath)
    sftp.close()
    ssh.close()

def ftp_hostname():
    sql = "SELECT hostname FROM ftp_data'
    mycursor.execute(sql)
    ftp_hostname = mycursor.fetchone()

def ftp_password():
    sql = "SELECT password FROM ftp_data'
    mycursor.execute(sql)
    ftp_password = mycursor.fetchone()

def ftp_user():
    sql = "SELECT user FROM ftp_data'
    mycursor.execute(sql)
    ftp_user = mycursor.fetchone()