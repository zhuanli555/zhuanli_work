from socket import *
serverName = "localhost"
serverPort = 12000
cs = socket(AF_INET,SOCK_DGRAM)
msg = raw_input("input:")
cs.sendto(msg,(serverName,serverPort))
momsg,serverAddress = cs.recvfrom(1024)
print momsg
print serverAddress
cs.close()
