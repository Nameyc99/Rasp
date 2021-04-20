import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(15,GPIO.OUT)

pwm = GPIO.PWM(15,50)

pwm.start(0)

GPIO.output(15,True)

def SetAngle(angle):
    dutyCycle = 0.05 * angle + 3
    pwm.ChangeDutyCycle(dutyCycle)

if __name__ == "__main__":
    try :
        while(True):
            angle = input("input angle:")
            if angle <= 180 :
                SetAngle(angle)
            else :
                print("angle too large")

    except KeyboardInterrupt:
        GPIO.cleanup()