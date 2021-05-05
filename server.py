import socket
import RPi.GPIO as GPIO
import LED
from motor import SetAngle

bind_ip = "192.168.50.115"
bind_port = 8888

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind((bind_ip,bind_port))
server.listen(5)
print("Listening on %s:%d"% (bind_ip,bind_port))

light = {
    "red" : 2,
    "yellow" : 3,
    "green" : 4,
}
for i in light :
            LED.Setup(light[i],"OUT")


try:
    client , addr = server.accept()
    print("Accepted connection from: %s:%d" % (addr[0],addr[1]))
    while True:
        print('start')
        data = client.recv(1024)
        print('stop')
        if data == b'red':
            if LED.GetGPIOStatus(light['red']) is 1 :
                LED.TurnOffLED(light['red'])
                SetAngle(0)
            else :
                LED.TurnOnLED(light['red'])
                SetAngle(180)
        elif data == b'green':
            if LED.GetGPIOStatus(light['green']) is 1 :
                LED.TurnOffLED(light['green'])
                SetAngle(0)
            else :
                LED.TurnOnLED(light['green'])
                SetAngle(180)
        elif data == b'yellow':
            if LED.GetGPIOStatus(light['yellow']) is 1 :
                LED.TurnOffLED(light['yellow'])
                SetAngle(0)
            else :
                LED.TurnOnLED(light['yellow'])
                SetAngle(180)
        client.sendall(data)

except KeyboardInterrupt:
    server.close()
    GPIO.cleanup()