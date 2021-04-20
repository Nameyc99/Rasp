import RPi.GPIO as GPIO
import time
from random import randint

global gpionum
def Setup2(GPIOnum, frequency):
    global gpionum
    GPIO.setmode(GPIO.BCM)
    gpionum = GPIOnum
    GPIO.setup(gpionum,GPIO.OUT)
    
    gpionum= GPIO.PWM(gpionum,frequency)
    gpionum.start(0)
        

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
    
def light_on(GPIOnum):
    TurnOnLED(GPIOnum)
    time.sleep(1)
    TurnOffLED(GPIOnum)

def cycle(dc) :
    rand = randint(2,4)
    Setup2(rand,100)
    gpionum.ChangeDutyCycle(dc)
    time.sleep(0.1)
    

if __name__ == "__main__":
    try:
        x = {
			5 : 4,
			2 : 3,
			0 : 2
        }
        for i in x :
            Setup(x[i],"OUT")   
                     
            
        while(True) :
            
            
            j = input('Please make your move: 0 = stone 2 = scissor 5 = paper')
               
            if j in x :
                light_on(x[j])
                
                
            else :
                for dc in range(0,101,5):
                    cycle(dc)
                    
                for dc in range(100,-1,-5):
                    cycle(dc)
                
                
            
   
             
    except KeyboardInterrupt:
        GPIO.cleanup()

