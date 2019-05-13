import json
from ftplib import FTP




with open('config.json') as json_file:  
    data = json.load(json_file)
    for p in data['config']:
        ftp_ip = p['ftp ip']
        ftp_user=p['ftp user']
        ftp_password=p['ftp password']


print(ftp_ip)
print(ftp_user)
print(ftp_password)


ftp = FTP(ftp_ip)
ftp.login(user=ftp_user, passwd = ftp_password)