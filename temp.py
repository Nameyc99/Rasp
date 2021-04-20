import Adafruit_DHT
import time
from LED import *

sensor = Adafruit_DHT.DHT11

GPIO = 14


while True:
	light = {
		'red' : 2,
		'yellow' : 3,
		'green' : 4
	}

	currentTime = time.strftime('%H:%M:%S')
	
	humidity, temperature = Adafruit_DHT.read_retry(sensor,GPIO)
	
	if humidity is not None and temperature is not None:
		print(currentTime,'->Temp={0}*C Humidity={1}%'.format(temperature,humidity))
		
	
	else:
		print('Failed to get reading. Try again!')
	time.sleep(10)
