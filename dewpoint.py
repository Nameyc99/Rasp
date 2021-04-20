import Adafruit_DHT
import time
from LED import *
import math

sensor = Adafruit_DHT.DHT11

GPIO = 14

def HeatstrokeCoefficient(celsius,humidity):
	heatstrokeCoefficient = celsius + humidity * 0.1
	return heatstrokeCoefficient
	
def Dewpoint(celsius,humidity):
	a = 17.271
	b = 237.7
	temp = (a*celsius)/(b+celsius)+math.log(humidity/100)
	td = (b*temp)/(a-temp)
	return td
	

while True:
	light = {
		'red' : 2,
		'yellow' : 3,
		'green' : 4
	}
	
	Setup(light['red'],'OUT')
	currentTime = time.strftime('%H:%M:%S')
	
	humidity, temperature = Adafruit_DHT.read_retry(sensor,GPIO)
	dewpoint = Dewpoint(temperature,humidity)
	heatstrokeCoef = HeatstrokeCoefficient(temperature,humidity)
	
	if humidity is not None and temperature is not None:
		print(currentTime,'->HeatstrokCoef={0} Dewpoint={1:0.1f}*C'.format(heatstrokeCoef,dewpoint))

	
	else:
		print('Failed to get reading. Try again!')
	time.sleep(5)
