#import the socket
import socket

#Assign IP of server
serverIP = "127.00.1"
#Assign port number of server
serverPort = 8001

#call socket from the import statement
#AF_INET specificies the IP address format (ipv.4)
# sock_dgram indicates protocol we're sending in udp
clientSocket = socket(AF_INET, SOCK_DGRAM)

# read input from keyboard to be message
msg = input("Enter message: ")

# use the socket function on the socket
# takes 2 parameters: 1st: bytes(change from str to bytes using encode)
    #2nd: ip and ports of server
clientSocket.sendTo(msg.encode(), (serverIP, serverPort))

# construct message to capture response from the server
# is returning 2 things (on left of equals)
#       recvfrom() allocates bytes; if you don't give enough bytes, you don't get the message
modifiedMessage,serverAddress = clientSocket.recvfrom(2048)

#turn bytes object into a string
msg2 = modifiedMessage.decode()

#closing the socket
clientSocket.close()

#idk if we need this
print(msg2)

