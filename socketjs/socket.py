from socketIO_client import SocketIO
socketIO = SocketIO('localhost:3001')
 
def main():
	# Listen
	socketIO.on('connect', connect)
 
	# Receive a message from a react client!
	socketIO.on('updateState', updateState)