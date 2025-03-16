import socket

localIP     = "127.0.0.1"
sendPort   = 7500
recievePort   = 7501
bufferSize  = 1024        

# set up the listener
recieveSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
recieveSocket.bind((localIP, sendPort))


print("UDP server up and listening")

# Listen for incoming datagrams

while(True):

    bytesAddressPair = recieveSocket.recvfrom(bufferSize)
    whoSent = bytesAddressPair[0]
    whoGotHit = bytesAddressPair[1]
    if(whoSent == 0):
        if(whoGotHit == 202):
            print("Game Start")
        else:
            print(whoGotHit  + " is active")
    else:
        print(whoSent + " hit: " + whoGotHit)
    