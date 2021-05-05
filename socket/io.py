import socketio

sio = socketio.Client()

sio.connect('http://192.168.1.113:3001')

@sio.event
def message(data):
    print('I received a message!')

@sio.on('temperature')
def on_message(data):
    print("Temperature is too high")

@sio.event
def connect():
    print("I'm connected!")

@sio.event
def connect_error():
    print("The connection failed!")

@sio.event
def disconnect():
    print("I'm disconnected!")

sio.emit('temperature',{
    "temp" : '50'
    "message" : "Temperature too high"
})