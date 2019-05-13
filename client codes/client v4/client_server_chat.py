import socket
import sys

import os
#os.system('cls')
#s=socket.socket()
#host = input('Enter hostname :- ')
#port = 9000
#hi = (host,port)
#s.connect(hi)
#print('connected to server')
#while True:
#    message = s.recv(1024)
#    message = message.decode()
#    print('>',message)

import os
from socket import *
import socket 
hostname = socket.gethostname()
host = socket.gethostbyname(hostname)
port = 13000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print ("Waiting to receive messages...")
while True:
    (data, addr) = UDPSock.recvfrom(buf)
    print ("Received message: " + data)
    if data == "exit":
        break
UDPSock.close()
os._exit(0)