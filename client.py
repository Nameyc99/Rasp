import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('140.117.71.98', 8888)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    while True:
        # Send data
        message = input("input:")
        b = message.encode('utf-8')
        print('sending "%s"' % message)
        sock.sendall(b)

        # Look for the response
        amount_received = 0
        amount_expected = len(b)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print('received "%s"' % data)

finally:
    print('closing socket')
    sock.close()