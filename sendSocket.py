import socket

localIP     = "127.0.0.1"
sendPort   = 7500
recievePort   = 7501
bufferSize  = 1024
msgFromServer       = "Hello UDP Client"
bytesToSend         = str.encode(msgFromServer)

# set up the sender
sendSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
sendSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

print("UDP server up and broadcasting")

# output the data

while(True):

    sendSocket.sendto(bytesToSend, (localIP, recievePort))