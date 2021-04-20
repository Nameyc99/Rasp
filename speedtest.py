import RPi.GPIO as GPIO

import time
GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 7
GPIO_ECHO = 12

GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)

#Disable warnings (optional)
GPIO.setwarnings(False)
#Select GPIO mode
GPIO.setmode(GPIO.BCM)
#Set buzzer - pin 5 as output
buzzer=5
GPIO.setup(buzzer,GPIO.IN)

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
	
def Setup(GPIOnum,OUT_IN):
    GPIO.setmode(GPIO.BCM)
    
    if OUT_IN=="OUT":
        GPIO.setup(GPIOnum,GPIO.OUT)
    else:
        GPIO.setup(GPIOnum,GPIO.IN)
        
def TurnOnLED(GPIOnum):
    GPIO.output(GPIOnum,True)
    
def TurnOffLED(GPIOnum):
    GPIO.output(GPIOnum,False)
    
def GetGPIOStatus(GPIOnum):
    GPIO_State = GPIO.input(GPIOnum)
    return GPIO_State
	
if __name__ == '__main__':
	try:
		x = {
			'red' : 2,
			'yellow' : 3,
			'green'  : 4,
		}
		
		for i in x:
			Setup(x[i],'OUT')
			
		speed = get_speed()
		

		
		while True:
			print('We are starting in 3 seconds')
			time.sleep(1)
			print('2')
			time.sleep(1)
			print('1')
			time.sleep(1)
			dist1 = distance(speed)
			print(dist1)
			time.sleep(1)
			dist2 = distance(speed)
			print(dist2)
			velocity = (dist2 - dist1)
			
			if velocity >30:
				TurnOnLED(x['red'])
				GPIO.setup(buzzer,GPIO.OUT)
				GPIO.output(buzzer,GPIO.LOW)
				print ("Beep")
				time.sleep(1)#Delay in seconds
				GPIO.output(buzzer,GPIO.HIGH)
				print ("No Beep")
				time.sleep(1)
				TurnOffLED(x['red'])
			elif velocity>20 and velocity <=30:
				TurnOnLED(x['yellow'])
				time.sleep(3)
				TurnOffLED(x['yellow'])
			elif velocity >10 and velocity<=20:
				TurnOnLED(x['green'])
				time.sleep(3)
				TurnOffLED(x['green'])
		
			print('Measured velocity is %.1f cm' %velocity)
			GPIO.setup(buzzer,GPIO.IN)
		
			
	except KeyboardInterrupt:
		print('Measure stopped by user')
		GPIO.cleanup
			
