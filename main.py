from socketComms import SocketComms


comms = SocketComms("127.0.0.1", 7500, 7501)
comms.start()


while True:
    #just for testing
    comms.send(1, 5)
    comms.send(100, 24)