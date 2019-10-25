if __name__ == "__main__":
#print("Sending message '{}' to UDP server on {} port {} ...".format(message, UDP_IP_ADDRESS_SERVER, UDP_PORT_SERVER))
  from socket import *
  import time


  #Setup the Connection to the Raspberry Pi
  UDP_IP_ADDRESS_SERVER = "localhost"
  UDP_PORT_SERVER = 23567

  #Setup Own Connection Details
  OWN_ADDRESS = ("localhost",23000)
  udpSerSock = socket(AF_INET,SOCK_DGRAM)
  udpSerSock.bind(OWN_ADDRESS)
  BUFSIZE = 1024

  def sendPackage(message):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    client.sendto(message.encode('utf-8'), (UDP_IP_ADDRESS_SERVER, UDP_PORT_SERVER))
    socket.close()
  
  def receiveResponse():
    max_time = 10
    start_time = time.time()  # remember when we started
    upcode = b"00"

    while (time.time() - start_time) < max_time:
      data,ADDR = udpSerSock.recvfrom(BUFSIZE)
      if data is None:
        break
      if b"exit" in data:
        break  
      if b"test" in data:
        upcode = data
        break  
    return upcode


  # First Initial Wakeup call check
  sendPackage("WKUPEV")
  upcode = receiveResponse()
  # (TODO) Spin until response has been received, should be a timeout as well, generating an error.
  if b"test" in upcode:
    print("FK YIS")

  if b"00" in upcode:
    print("MB YEIIS?")

  # Send a Ready state to the PI, which will respond with an upcode when analysed the card.
  sendPackage("READY")
  # (TODO) Spin until response has been received, should be a timeout as well, generating an error.

