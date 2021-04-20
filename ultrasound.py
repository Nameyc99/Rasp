import RPi.GPIO as GPIO
from LED import *
import time

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 7
GPIO_ECHO = 12

GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)

def send_trigger_pulse():
	GPIO.output(GPIO_TRIGGER,True)
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER,False)
	
def get_speed():
	speed = 33100 + 26*60
	return speed
	
def distance(speed):
	send_trigger_pulse()
	
	while GPIO.input(GPIO_ECHO) == 0:
		StartTime = time.time()
		
	while GPIO.input(GPIO_ECHO) == 1:
		StopTime = time.time()
		
	TimeElapsed = StopTime - StartTime
	distance = (TimeElapsed * speed) /2
	
	return distance

	
if __name__ == '__main__':
	try:
		x = {
			'red' : 2,
			'yellow' : 3,
			'green'  : 4,
		}
		
		for i in x:
			Setup(x[i],'OUT')
			
		while True:
			speed = get_speed()
			dist = distance(speed)
			if dist < 5:
				TurnOnLED(x['red'])
				time.sleep(1)
				TurnOffLED(x['red'])
				
			elif dist>=5 and dist<10 :
				TurnOnLED(x['yellow'])
				time.sleep(1)
				TurnOffLED(x['yellow'])
				
			elif dist>=10 and dist<15 :
				TurnOnLED(x['green'])
				time.sleep(1)
				TurnOffLED(x['green'])
				
			print('Measure distance %.1f cm' %dist)
			time.sleep(1)
			
	except KeyboardInterrupt:
		print('Measure stopped by user')
		GPIO.cleanup
			
