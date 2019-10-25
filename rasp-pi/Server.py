from socket import *
from time import ctime

HOST = 'localhost'
PORT = 23567
BUFSIZE = 1024
ADDR = (HOST,PORT)

udpSerSock = socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print ("...waiting for message...")
    data,ADDR = udpSerSock.recvfrom(BUFSIZE)
    if data is None:
        break
    print ("[%s]: From Address %s:%s receive data: %s" %(ctime(),ADDR[0],ADDR[1],data))
    print (data)
    if b"exit" in data:
        break
udpSerSock.close()