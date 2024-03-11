# Timer
import tkinter
from tkinter import *
import re
from threading import Thread
from time import sleep
import pygame


def startTimer(query):
    nums = re.findall(r'[0-9]+', query)
    time = 0
    if "minute" in query and "second" in query:
        time = int(nums[0])*60 + int(nums[1])
    elif "minute" in query:
        time = int(nums[0])*60
    elif "second" in query:
        time = int(nums[0])
    else:
        return

    print("Timer Started")
    sleep(time)
    print('playing sound using  pygame')
    Thread(target=time_up).start()


def time_up():
    win2 = Tk()
    win2.title('Nuvia Timer')

    # Window size
    win2.geometry('300x100')
    win2.minsize(300, 100)  # Minimum size of window
    win2.maxsize(300, 100)  # Maximum size of window
    win2.config(bg='#081923')

    # Label
    lb1 = Label(win2, text='Times UP', fg='orange', bg='#081923',
                font=('Times Now Romans', 20, 'bold'))
    lb1.place(x=80, y=10)

    pygame.init()
    pygame.mixer.music.load('sounds/timer_track.mp3')
    pygame.mixer.music.play()

    def pack_up():
        pygame.mixer.music.stop()

        win2.quit()

    # Button
    b1 = Button(win2, bg='#D50000', fg='white', text='STOP!!', bd=5, font=('Times Now Romans', 13, 'normal'),
                activebackground='#536DFE', activeforeground='white', command=pack_up)
    b1.place(x=110, y=57)

    win2.mainloop()


if __name__ == '__main__':
    startTimer('set time for 1 seconds')
