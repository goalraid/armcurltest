import time
#from servotest import serC
import serial
import cv2
import numpy as np
from pyzbar.pyzbar import decode
from pynput.keyboard import Key, Controller
#from bigarmcurltest import curl
from jumpinjack import jj
from PushUp import push
from legsup import legups
from lat import lat
from plank import plank
from situp import sit
from Squats import squat
from wallsit import wall
from glute import glute
from highknees import knee
from climb import climb
from bent import bent


keyboard = Controller()
servo = serial.Serial("COM6", 9600)
import time
#def serC():




#serC()


"""        
def serO():
    while True:
        num = "150"
        servo.write(num.encode())
        time.sleep(2)
        servo.close()
"""

def start():
    num = "70"
    if num == "70":
        servo.write(num.encode())
    # img = cv2.imread('1.png')
    cap = cv2.VideoCapture(0)
    window_name = 'SCAN QR CODE'

    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    total = 0
    myData = 0

    #with open('workouts.txt') as f:
        #workoutList = f.read().splitlines()
    while True:

        success, img = cap.read()
        for barcode in decode(img):

            servo.write(num.encode())
            myData = barcode.data.decode('utf-8')
            print(myData)

        cv2.imshow(window_name, img)
        if myData == 'curl':
            total = 2
            print('armcurl')
            keyboard.press('q')
            keyboard.release('q')
            cap.release()
            cv2.destroyAllWindows()

        elif myData == 'jj':
            total = 3

            print('jumping jacks')
            keyboard.press('q')
            keyboard.release('q')
            cap.release()
            cv2.destroyAllWindows()

        elif myData == 'push':
            total = 4
            print('pushup')
            keyboard.press('q')
            keyboard.release('q')
            cap.release()
            cv2.destroyAllWindows()

        elif myData == 'leg':
            total = 5
            print('leg ups')
            keyboard.press('q')
            keyboard.release('q')
            cap.release()
            cv2.destroyAllWindows()

        elif myData == 'sit':
            total = 6
            print('sit ups')
            keyboard.press('q')
            keyboard.release('q')
            cap.release()
            cv2.destroyAllWindows()

        elif myData == 'squat':
            total = 7
            print('squats')
            keyboard.press('q')
            keyboard.release('q')
            cap.release()
            cv2.destroyAllWindows()

        elif myData == 'plank':
            total = 8
            print('plank')
            keyboard.press('q')
            keyboard.release('q')
            cap.release()
            cv2.destroyAllWindows()

        elif myData == 'climber':
            total = 9
            print('Mountain Climber')
            keyboard.press('q')
            keyboard.release('q')
            cap.release()
            cv2.destroyAllWindows()

        elif myData == 'wall':
            total = 10
            print('WALL SIT')
            keyboard.press('q')
            keyboard.release('q')
            cap.release()
            cv2.destroyAllWindows()

        elif myData == 'glute':
            total = 11
            print('Glute Bridge')
            keyboard.press('q')
            keyboard.release('q')
            cap.release()
            cv2.destroyAllWindows()


        elif myData == 'bent':
            total = 12
            print('BENT BODY ROW')
            keyboard.press('q')
            keyboard.release('q')
            cap.release()
            cv2.destroyAllWindows()

        elif myData == 'lat':
            total = 13
            print('LATERAL DUMBBELL RAISE')
            keyboard.press('q')
            keyboard.release('q')
            cap.release()
            cv2.destroyAllWindows()

        elif myData == 'knee':
            total = 14
            print('LATERAL DUMBBELL RAISE')
            keyboard.press('q')
            keyboard.release('q')
            cap.release()
            cv2.destroyAllWindows()


        key = cv2.waitKey(25)
        if key == ord('q'):
            print("Your next workout is")

        if total == 2:
            #curl()

            return total

        if total == 3:
            jj()
            num = "150"
            servo.write(num.encode())
            return total

        if total == 4:
            push()

            return total

        if total == 5:
            legups()

            return total

        if total == 6:
            sit()

            return total

        if total == 7:
            squat()

            return total



        if total == 9:
            climb()

            return total

        if total == 11:
            glute()

            return total

        if total == 12:
            bent()
            num = "150"
            servo.write(num.encode())
            return total

        if total == 13:
            lat()

            return total

        if total == 14:
            knee()

            return total


        if total == 10:
            wall()

            break

        if total == 8:
            plank()

            break


start()






