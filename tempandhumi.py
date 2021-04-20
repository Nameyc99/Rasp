import Adafruit_DHT
import time
from LED import *

sensor = Adafruit_DHT.DHT11

GPIO = 14

def HeatstrokeCoefficient(celsius,humidity):
	heatsrokeCoefficient = celsius + humidity * 0.1
	return heatstrokeCoefficient
	
def Dewpoint(celsius,humidity):
	a = 17.271
	b = 237.7
	temp = (a*celsius)/(b+celsius)+math.log(humidity/100)
	td = (b*temp)/(a-temp)
	return td
	

while True:
	try:
		light = {
			'red' : 2,
			'yellow' : 3,
			'green' : 4
		}
		
		Setup(light['red'],'OUT')
		currentTime = time.strftime('%H:%M:%S')
		
		humidity, temperature = Adafruit_DHT.read_retry(sensor,GPIO)
		print(humidity)
		print(temperature)
		
		if humidity is not None and temperature is not None:
			print(currentTime,'->Temp={0}*C Humidity={1}%'.format(temperature,humidity))
			
			if(temperature <=25 and humidity <= 60) :
				TurnOnLED(light['red'])
				time.sleep(1)
				TurnOffLED(light['red'])
				time.sleep(1)
		
		else:
			print('Failed to get reading. Try again!')
		time.sleep(5)
	
	except KeyboardInterrupt:
		GPIO.cleanup();
