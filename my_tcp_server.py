from socket import *
import datetime
serverSocket = socket(AF_INET, SOCK_STREAM)
serverIP = "127.0.0.1"
serverPort = 5000
serverSocket.bind((serverIP, serverPort))

serverSocket.listen()

print("[SERVER]")

while(1):
    connectionSocket 