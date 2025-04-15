import socket
import threading

class SocketComms:
    def __init__(self, localIP):
        self.localIP = localIP
        self.sendPort = 7500
        self.receivePort = 7501
        self.bufferSize = 1024
        # Set up the sender
        self.sendSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sendSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # Set up the listener
        self.receiveSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.receiveSocket.bind((self.localIP, self.receivePort))
    def redTeamScores(self):
        #Send whoHit and equipmentID 
        try:
            message = f"{53}".encode()  # Encode as bytes
            self.sendSocket.sendto(message, (self.localIP, self.sendPort))
            print(f"Sent: Code 53")
        except Exception as e:
            print(f"Send error: {e}")
    def greenTeamScores(self):
        #Send whoHit and equipmentID 
        try:
            message = f"{43}".encode()  # Encode as bytes
            self.sendSocket.sendto(message, (self.localIP, self.sendPort))
            print(f"Sent: Code 43")
        except Exception as e:
            print(f"Send error: {e}")   
    def sendEnd(self):
        try:
            message = f"{221}".encode()  # Encode as bytes
            for i in range(3):
                self.sendSocket.sendto(message, (self.localIP, self.sendPort))
                print(f"Sent: Code 221")
        except Exception as e:
            print(f"Send error: {e}")
    def sendHit(self, whoHit, equipmentHit):
        #Send whoHit and equipmentID 
        try:
            message = f"{whoHit},{equipmentHit}".encode()  # Encode as bytes
            self.sendSocket.sendto(message, (self.localIP, self.sendPort))
            print(f"Sent: Player {whoHit} hit Equipment {equipmentHit}")
        except Exception as e:
            print(f"Send error: {e}")
    def sendStart(self):
        #Send whoHit and equipmentID 
        try:
            message = f"{202}".encode()  # Encode as bytes
            self.sendSocket.sendto(message, (self.localIP, self.sendPort))
            print(f"Sent: Code 202")
        except Exception as e:
            print(f"Send error: {e}")
    def sendEqpID(self, eqpID):
        #Send whoHit and equipmentID 
        try:
            message = f"{0},{eqpID}".encode()  # Encode as bytes
            self.sendSocket.sendto(message, (self.localIP, self.sendPort))
            print(f"Sent: Equipment ID {eqpID}")
        except Exception as e:
            print(f"Send error: {e}")
    def receive(self):
       #Listen for messages 
        while True:
            try:
                data, address = self.receiveSocket.recvfrom(self.bufferSize)
                actualVals = data.decode().split(",")  # Split into player sending and equipment ID hit
                
                if len(actualVals) == 2:  #check for validity
                    whoHit, equipmentHit = actualVals
                    if(whoHit == 0):
                        if(equipmentHit == 202):
                            print("Game Start! :D")
                        else:
                            print(equipmentHit  + " is active")
                    else:
                        print(whoHit + " hit: " + equipmentHit)
                elif len(actualVals) == 1:  
                    whoHit = actualVals
                    if(whoHit == 202):
                            print("Game Start! :D")
                    elif whoHit == 221:
                            print("Game End! :D")
                    elif whoHit == 53:  
                            print("Red Team Scores! :D")
                    elif whoHit == 43:
                            print("Green Team Scores! :D")
                    else:
                        print(whoHit + " is active")
                else:
                    print("Data is messed up:", actualVals)
            except Exception as e:
                print(f"Receive error: {e}")
                break

    def start(self):
        
        receive_thread = threading.Thread(target=self.receive, daemon=True)
        receive_thread.start()
        print("Listening...")
