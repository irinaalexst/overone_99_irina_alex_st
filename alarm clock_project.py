from tkinter.ttk import *
from tkinter import *

from PIL import ImageTk, Image
from pygame import mixer
from threading import Thread


from datetime import datetime
from time import sleep


root = Tk()
root.title('Do not wake me up')
root.geometry('900x450')



# to set label LABEL 'input time'
clock = Label(root, text='Input time',font=('arial',16))
clock.grid(row=1,column=1)

frame_line = Frame(root, width=400,height=5)
frame_line.grid(row=2,column=25)

frame_body = Frame(root,width=400,height=290)
frame_body.grid(row=3,column=25)



hour = Label(root, text ='hour', height=1, font=('comic sans',18))
hour.grid(row=1,column=2)
c_hour = Combobox(root,width=2,font=('comic sans',18))
c_hour['values']=('00','01','02','03','04','05', '06','07','08','09','10',
                   '11','12','13','14','15','16','17','18','19','20','21','22','23')
c_hour.current(0)
c_hour.grid(row=2,column=2)

minute = Label(root, text ='min', height=1, font=('comic sans',18))
minute.grid (row=1,column=3)
c_min = Combobox(root,width=2,font=('comic sans',18))
c_min['values']=('00','01','02','03','04','05', '06','07','08','09','10',
                   '11','12','13','14','15','16','17','18','19','20','21','22','23',
                  '24','25','26','27','28','29','30','31','32','33','34','35','36',
                  '37','38','39','40','41','42','43','44','45','46','47','48','49',
                  '50','51','52','53','54','55','56','57','58','59')
c_min.current(0)
c_min.grid (row=2,column=3)



def activate_alarm():
    th = Thread(target=alarm)
    th.start()

selected = IntVar()

submit1 = Button(frame_body, text='SUBMIT',font=('comic sans',18),command = activate_alarm)
submit1.grid(row=4,column=0)


def deactivate_alarm():
    print('Deactivated alarm:', selected.get())
    mixer.music.stop()


def sound_alarm():
    mixer.music.load('https://github.com//irinaalexst//overone_99_irina_alex_st//blob//master//tone.wav')
    mixer.music.play()
    # selected.set(0)
#run endlessly

submit = Button(frame_body, text='STOP',font=('comic sans',18),command = deactivate_alarm)
submit.grid(row=5,column=0)
    # submit2 = Radiobutton(frame_body, font=('arial 15 bold'), value=2, text='Deactivate', command=deactivate_alarm,
    #                      variable=selected)
    # submit2.place(x=187, y=95)

def alarm():
    while True:
        control = 1
        print(control)

        alarm_hour = c_hour.get()
        alarm_minute = c_min.get()


        now = datetime.now()

        hour = now.strftime('%H')
        minute = now.strftime('%M')

        if control == 1:
            if alarm_hour == hour:
                if alarm_minute == minute:
                    sound_alarm()



        sleep(1)

#import image + using import
Photo = PhotoImage(file ='https://github.com//irinaalexst//overone_99_irina_alex_st//blob//master//cute.png')

img = Label(frame_body,image=Photo)
img.grid(rowspan=3, column=0)



mixer.init()



root.mainloop()

#threat helps us to run the bg and execute main instructions to run the function
