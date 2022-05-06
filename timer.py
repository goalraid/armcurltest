import time
import datetime

import tkinter as tk
from random import seed, choice
from string import ascii_letters
seed(42)

colors = ('red', 'yellow', 'green', 'cyan', 'blue', 'magenta')

def countdown():
    # Calculate the total number of seconds
    total_seconds = 60

    # While loop that checks if total_seconds reaches zero
    # If not zero, decrement total time by one second
    while total_seconds > 0:
        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds=total_seconds)

        # Prints the time left on the timer
        print(timer, end="\r")

        # Delays the program one second
        time.sleep(1)

        # Reduces total time by one second
        total_seconds -= 1

        #print(timer)







    s = timer
    color = choice(colors)
    l.config(text=timer, fg=color)
    root.after(100,countdown())

root = tk.Tk()
root.wm_overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.bind("<Button-1>", lambda evt: root.destroy())

l = tk.Label(text='', font=("Helvetica", 60))
l.pack(expand=True)
# Inputs for hours, minutes, seconds on timer
h = 0
m = 1
s = 0
countdown()

root.mainloop()
# Create class that acts as a countdown