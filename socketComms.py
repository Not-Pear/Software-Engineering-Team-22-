import socket
import threading
import tkinter as tk

class SocketComms:
    def __init__(self, localIP):
        self.localIP = localIP
        self.sendPort = 7500
        self.receivePort = 7501
        self.bufferSize = 1024
        self.actionScreen = None
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
    def sendHit(self, equipmentHit):
        #Send whoHit and equipmentID 
        try:
            message = f"{equipmentHit}".encode()  # Encode as bytes
            self.sendSocket.sendto(message, (self.localIP, self.sendPort))
        except Exception as e:
            print(f"Send error: {e}")
    def setActionScreen(self, actionScreen):
        self.actionScreen = actionScreen
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
            message = f"{eqpID}".encode()  # Encode as bytes
            self.sendSocket.sendto(message, (self.localIP, self.sendPort))
            print(f"Sent: Equipment ID {eqpID}")
        except Exception as e:
            print(f"Send error: {e}")
    def receive(self):
       #Listen for messages 
        while True:
            try:
                data, address = self.receiveSocket.recvfrom(self.bufferSize)
                actualVals = data.decode().split(":")  # Split into player sending and equipment ID hit
                
                if len(actualVals) == 2:  #check for validity
                    whoHit, equipmentHit = actualVals
                    if(equipmentHit != "53" and equipmentHit != "43"):
                        print(whoHit + " hit: " + equipmentHit)
                        playerHitting = self.actionScreen.getPlayerByID(whoHit)
                        playerGotHit = self.actionScreen.getPlayerByID(equipmentHit)
                        self.actionScreen.action_text_box.insert(tk.END, f'{playerHitting.getCodeName()} hit: {playerGotHit.getCodeName()}\n')
                        if(playerHitting.getTeam() != playerGotHit.getTeam()):
                            self.sendHit(equipmentHit)
                            playerHitting.setPoints(playerHitting.getPoints() + 10)
                            self.actionScreen.update_entries(playerHitting.getTeam(), playerHitting.getPlayerNum(), new_score = playerHitting.getPoints())
                        else:
                            self.sendHit(whoHit)
                            playerHitting.setPoints(playerHitting.getPoints() - 10)
                            self.actionScreen.update_entries(playerHitting.getTeam(), playerHitting.getPlayerNum(), new_score = playerHitting.getPoints())
                        
                        
                    elif(equipmentHit == "53"):
                        print(f'red base hit by {playerHitting.getCodeName()}')
                        if (playerHitting.getTeam() == "green"):
                            self.sendHit(53)
                            playerHitting.setPoints(playerHitting.getPoints() + 100)
                            self.actionScreen.update_entries(playerHitting.getTeam(), playerHitting.getPlayerNum(), new_name = None, new_score = playerHitting.getPoints(), baseHit=True)
                    elif(equipmentHit == "43"):
                        print(f'green base hit by {playerHitting.getCodeName()}')
                        if (playerHitting.getTeam() == "red"):
                            self.sendHit(43)
                            playerHitting.setPoints(playerHitting.getPoints() + 100)
                            self.actionScreen.update_entries(playerHitting.getTeam(), playerHitting.getPlayerNum(), new_name = None, new_score = playerHitting.getPoints(), baseHit=True)
                      
                    else:
                        print("somehting went wrong")
                        
                    
               
                else:
                    print("Data is messed up:", actualVals)
            except Exception as e:
                print(f"Receive error: {e}")
                break

    def start(self):
        
        receive_thread = threading.Thread(target=self.receive, daemon=True)
        receive_thread.start()
        print("Listening...")
