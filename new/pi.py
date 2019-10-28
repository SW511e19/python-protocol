import socket

# Setting Up the Server Settings for Raspberry Pi
localIP     = "localhost"
localPort   = 20001
bufferSize  = 1024

#Defining Attributes
msgFromServer       = "This is sent from the server"
bytesToSend         = str.encode(msgFromServer)
address = None

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

# Listen for incoming datagrams
def readyToReceive():
    print("UDP server up and listening")
    while(True):
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

        message = bytesAddressPair[0]
        address = bytesAddressPair[1]

        clientMsg = "Message from Client:{}".format(message)
        clientIP  = "Client IP Address:{}".format(address)
    
        print(clientMsg)

        if b"STOP" in message:
            break;

        print(clientIP)
    return;

while(True):
    readyToReceive();

    # DO ML OPERATION HERE
    # Sending a reply to client
    UDPServerSocket.sendto(bytesToSend, "SO FAR HARDCORE ADDRESS HERE YIS?")

