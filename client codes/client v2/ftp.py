import os
import paramiko 
import sys
#ftp part
#hostname
# username 
# password 
# localpath 
# remotepath

def connect(hostname, username , password ,remotepath):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username, password)
    sftp = ssh.open_sftp()

                 
    pathname = os.path.dirname(sys.argv[0])        
    
    localpath= os.path.abspath(pathname)

    sftp.put(localpath, remotepath)
    sftp.close()
    ssh.close()

