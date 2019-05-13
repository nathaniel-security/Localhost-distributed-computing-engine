import os 
from ftp_data import *
import time


print('\n\ngetting requiremenys.txt\n\n')
filename = 'requirements.txt'
localfile = open(filename, 'wb')
ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
time.sleep(2)
print('\n\nrunning requirements.txt\n\n')
os.system('pip install -r requirements.txt')


os.system('python node_free.py')
