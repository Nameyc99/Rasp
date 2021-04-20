import ultrasound
import LED
import motor
import time
from datetime import datetime

if __name__ == "__main__" :

    enter_time = []
    exit_time = []
    try :
        motor.SetAngle(0)
        occupied = False
        LED.Setup(2,"OUT")
        
        while True :
            speed = ultrasound.get_speed()
            dist = ultrasound.distance(speed)
            if dist <= 10 :
                if not occupied :
                    now = datetime.now()
                    enter_time.append(now.strftime("%H:%M:%S"))
                    print("Current Time =" + enter_time[-1])
                    print("Someone entered, turning on light")
                    motor.SetAngle(180)
                    LED.TurnOnLED(2)
                    occupied = not occupied
                else :
                    now = datetime.now()
                    exit_time.append(now.strftime("%H:%M:%S"))
                    print("Current Time =" + exit_time[-1])
                    print("Person left, turning off light")
                    LED.TurnOffLED(2)
                    motor.SetAngle(0)
                    occupied = not occupied
            time.sleep(1)
        
    except KeyboardInterrupt :
        date = datetime.now().strftime("%D %H:%M:%S")

        f = open("log.txt","a")
        f.write("\nToday's date is :" + date + "\n")
        for x in range(len(enter_time)) :
            f.write("Current time :")
            f.write(enter_time[x])
            f.write("\n")
            f.write("Exit Time :")
            f.write(exit_time[x])
            f.write("\n")
        f.close()

        
        