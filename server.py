from socket import *
serverPort = 12000
ss = socket(AF_INET,SOCK_DGRAM)
ss.bind(("127.0.0.1",serverPort))
while True:
    msg = ss.recv(1024)
    mmsg = msg.upper()
    ss.send(mmsg)
    