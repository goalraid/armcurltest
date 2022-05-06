#import serial
import time
#servo = serial.Serial("COM6", 9600)
def serC():
    while True:
        num = "70"
        servo.write(num.encode())
        time.sleep(2)

"""        
def serO():
    while True:
        num = "150"
        servo.write(num.encode())
        time.sleep(2)
        servo.close()
"""
serC()