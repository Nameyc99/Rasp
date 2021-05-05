import socket
import sys
import RPi.GPIO as GPIO
from motor import SetAngle
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('140.117.71.98',8888)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

while True :
    # Receive data
    data = sock.recv(1024)

    # Look for the response
    if data == b'water':
        SetAngle(180)
        time.sleep(5)
        SetAngle(0)
        time.sleep(1)
    sock.sendall(data)
