from tkinter import *
from tkinter import messagebox
import time
import datetime
import threading
from pygame import mixer

root = Tk()
root.title("Do not wake me up")
root.geometry("900x500")

mixer.init()

#thread function
def thread():
    t1 = threading.Thread(target=alarm, args=())
    t1.start()


def alarm():
    alarm = time_entry.get()
    if alarm == "":
        msg = messagebox.showerror('Invalid data', 'Please enter valid time')
    else:
        Alarmtime = alarm
        CurrentTime = time.strftime("%H:%M")

        while Alarmtime != CurrentTime:
            CurrentTime = time.strftime("%H:%M")

        if Alarmtime == CurrentTime:
            mixer.music.load('tone.wav')
            mixer.music.play()
            msg = messagebox.showinfo('It is time', f'{message_entry.get()}')
            if msg == 'ok':
                mixer.music.stop()


body = Frame(root)
body.place(x=5, y=5)

name = Label(root,fg='black', text="ALARM CLOCK", font=('Ebrima', 20))
name.pack(fill=X)

panel = Frame(root)
panel.place(x=5, y=70)

photo = PhotoImage(file='cute.png')

photo_set = Label(panel, image=photo)
photo_set.grid(rowspan=4, column=0)

time_set = Label(panel, text="Alarm Time \n(Hr:Min)", font=('Ebrima', 18))
time_set.grid(row=0, column=1, padx=10, pady=5)

time_entry = Entry(panel, font=('Ebrima', 20), relief=GROOVE, width=5)
time_entry.grid(row=0, column=2, padx=10, pady=5)

message_label = Label(panel, text="Message", font=('Ebrima', 20))
message_label.grid(row=1, column=1, columnspan=2, padx=10, pady=5)

message_entry = Entry(panel, font=('Ebrima', 15), relief=GROOVE, width=25)
message_entry.grid(row=2, column=1, columnspan=2, padx=10, pady=5)

start = Button(panel, text="Start alarm", font=('Ebrima', 20), command=thread)
start.grid(row=3, column=1, columnspan=2, padx=10, pady=5)

root.mainloop()






















