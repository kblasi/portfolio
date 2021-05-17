from socket import *
import datetime 

clientSocket = socket(AF_INET, SOCK_STREAM)
serverIP = "127.0.0.1"
serverPort = 5000
clientSocket.connect( (serverIP, serverPort) )

message = input("[CLIENT - {}] ---> Input lowercase sensence then press <Enter/Return>:".format( datetime.datetime.now(), serverIP, serverPort ))
