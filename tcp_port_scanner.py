import socket
import time


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target1 = '31.13.74.36'
target2 = '40.97.142.194'
target3 = '172.217.14.174'

ports = []
ports2 = []
ports3 = []

count = 1

for port in range(1,1001):
    try:
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.settimeout(0.2)
        clientSocket.connect( ('31.13.74.36', port) )

        ports.append(count)
        count+=1
        clientSocket.close()

    except Exception as e:
        count+=1

print("Ports open for IP address 31.13.74.36 are: " + str(ports))

count2 = 1
for port in range(1,1001):
    try:
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.settimeout(0.2)
        clientSocket.connect( ('40.97.142.194', port) )

        ports2.append(count2)
        count2+=1
        clientSocket.close()

    except Exception as e:
        count2+=1

print("Ports open for IP address 40.97.142.194 are: " + str(ports2))

count3 = 1
for port in range(1,1001):
    try:
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.settimeout(0.2)
        clientSocket.connect( ('172.217.14.174', port) )

        ports3.append(count3)
        count3+=1
        clientSocket.close()

    except Exception as e:
        count3+=1

print("Ports open for IP address 172.217.14.174 are: " + str(ports3))