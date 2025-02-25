import socket
import threading

class SocketComms:
    def __init__(self, localIP, sendPort, receivePort):
        self.localIP = localIP
        self.sendPort = sendPort
        self.receivePort = receivePort
        self.bufferSize = 1024
        # Set up the sender
        self.sendSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sendSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # Set up the listener
        self.receiveSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.receiveSocket.bind((self.localIP, self.receivePort))

    def send(self, whoHit, equipmentHit):
        #Send whoHit and equipmentID 
        try:
            message = f"{whoHit},{equipmentHit}".encode()  # Encode as bytes
            self.sendSocket.sendto(message, (self.localIP, self.receivePort))
            print(f"Sent: Player {whoHit} hit Equipment {equipmentHit}")
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
                    print(f"Received: Player {whoHit} hit Equipment {equipmentHit}.")
                else:
                    print("Data is messed up:", actualVals)
            except Exception as e:
                print(f"Receive error: {e}")
                break

    def start(self):
        
        receive_thread = threading.Thread(target=self.receive, daemon=True)
        receive_thread.start()
        print("Listening...")