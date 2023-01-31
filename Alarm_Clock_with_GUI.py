# Here's a simple alarm clock with GUI code in Python using the Tkinter library

import tkinter as tk
import time

def alarm():
    print("Time's up!")

def set_alarm():
    alarm_time = entry.get()
    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            alarm()
            break
        time.sleep(1)

root = tk.Tk()
root.title("Alarm Clock")

entry = tk.Entry(root)
entry.pack()

set_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_button.pack()

root.mainloop()

