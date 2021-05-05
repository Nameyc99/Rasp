##my address b8:27:eb:1d:1a:a2
import bluetooth 
import RPi.GPIO as GPIO
import LED

server_socket = bluetooth.BluetoothSocket(RFCOMM)
server_socket.bind("",3)
server_socket.listen(1)

conn_socket, address = server_socket.accept()
LED.Setup(2,'OUT')
try :
    while True:
        data = conn_socket.recv(1024)
        print(data)
        if data == b'turn on led':
            print("received [%s]" % data)
            LED.TurnOnLED(2)

        senddata = input()
        conn_socket.send(senddata)

except KeyboardInterrupt:
    pass

conn_socket.close()
server_socket.close()
GPIO.cleanup