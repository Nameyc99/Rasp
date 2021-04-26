import RPi.GPIO as GPIO
import time

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
    
def traffic_light(GPIOnum,onsleep,offsleep,flick):
    i = 1
    while i <= flick :
        TurnOnLED(GPIOnum)
        time.sleep(onsleep)
        TurnOffLED(GPIOnum)
        time.sleep(offsleep)
        i += 1

if __name__ == "__main__":
    try:
        x = {
			'red' : 2,
			'yellow' : 3,
			'green' : 4
        }
        
        for i in x :
            Setup(x[i],"OUT")
        
        
        while(True) :
            traffic_light(x['red'],2,1,1)
            traffic_light(x['green'],1,1,1)
            traffic_light(x['yellow'],0.1,0.1,5)
            
                    
                

                
    except KeyboardInterrupt:
        GPIO.cleanup()

