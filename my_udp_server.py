
import socket
serverAddress = "127.00.1"
serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind((serverAddress, serverPort))

# forever statment
while True:
    #message is in bytes
    message,clientAddress = serverSocket.recvFrom(2048)

    #turn back to string and make uppercase
    mod_msg = message.decode().upper()

    #send it back to the client by encoding to back to bytes
    serverSocket.sendto(mod_msg.encode(), clientAddress)


