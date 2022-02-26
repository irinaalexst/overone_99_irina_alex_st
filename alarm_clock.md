## Alarm Clock

As [J.M. POWER] once mentioned:

> IF YOU WANT TO MAKE YOUR DREAMS COME TRUE,
> THE FIRST THING YOU HAVE TO DO IS
> WAKE UP.

# My goal was ..

to create the alarm clock that can help
- to organise your sleeping hours
- to wake up with music of your soul
- not to keep your mind busy
- to build 'to do list' for the day

## Import

Alarm clock requires to import:

```from tkinter import *
from tkinter import messagebox
import time
import datetime
import threading
from pygame import mixer
```
## Thread
Using thread improves execution time, and is very useful when we need to perform multiple tasks at the same time.

The Thread() accepts many parameters. The main ones are: target: specifies a function (fn) to run in the new thread. args: specifies the arguments of the function (fn). The args argument is a tuple. 

For the project I've realized 

```def thread():
    t1 = threading.Thread(target=alarm, args=())
    t1.start()
```
where is ' args' is the argument tuple for the target invocation
         'target' is the thread function
         
## Pygame Mixer

```from pygame import mixer```

The Python Pygame Mixer Library brings in support Audio and Sound playback. The great thing about it is that it’s not just restricted to making games. You can use the Mixer library all on it’s own as a stand alone library to play sound and music in your average Python program.

```
mixer.init()
mixer.music.load('tone.wav')
mixer.music.play()
mixer.music.stop()
```

## Setting a Tkinter Window
Import of necessary libraries:

```from tkinter import *```

Creating a simple Tkinter window in some steps:

```
root = Tk()
root.title("Name your window")
root.geometry("900x500")
```
At the end of a code, don't forget to run the function:
```
root.mainloop()
```
## Adding a picture

```
from PIL import ImageTk, Image
```
You can import images in 2 ways:

1. You can copy the path and add  '\\\\'
```
photo = PhotoImage(file='C:\\Users\\Hp\\PycharmProjects\\pythonProject1\\img2\\cute.png')
```
or
2. You can simply write
```
photo = PhotoImage(file='cute.png')
```
Second variant didn't work for me in Pycharm, so I found rather helpful the second variant.

Grid() method in Tkinter organizes widgets in a table-like structure in the parent widget.
```
photo_set = Label(panel, image=photo)
photo_set.grid(rowspan=4, column=0)
```
# Syntax

Here is the list of used -grid options −

- column − The column to put widget in; default 0 (leftmost column).
- columnspan − How many columns widgetoccupies; default 1.
- row − The row to put widget in; default the first row that is still empty.
- padx, pady − How many pixels to pad widget, horizontally and vertically, outside v's borders.













