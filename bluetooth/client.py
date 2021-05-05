from bluetooth import *

PORT = 3
client_socket = BluetoothSocket(RFCOMM)

client_socket.connect(("",PORT))

while True:
    senddata = input("Please input message:")
    client_socket.send(senddata)
    data = client_socket.recv(1024)
    print("received [%s]" % data)

client_socket.close()