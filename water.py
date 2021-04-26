import socket
import RPi.GPIO as GPIO
from motor import SetAngle
import time

bind_ip = "0.0.0.0"
bind_port = 8888

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind((bind_ip,bind_port))
server.listen(5)
print("Listening on %s:%d"% (bind_ip,bind_port))



try:
    client , addr = server.accept()
    print("Accepted connection from: %s:%d" % (addr[0],addr[1]))
    print('start')
    data = client.recv(1024)
    print('stop')
    if data == b'water':
        SetAngle(180)
        time.sleep(5)
        SetAngle(0)
        time.sleep(1)
    client.sendall(data)

except KeyboardInterrupt:
    server.close()
    GPIO.cleanup()