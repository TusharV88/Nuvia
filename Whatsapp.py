import tkinter
from tkinter import *
from tkinter import messagebox
import webbrowser


def watsup():
    global Num

    master = Tk()
    master.title("Whatsapp")
    master.geometry('400x150')
    master.minsize(400, 150)
    master.maxsize(400, 150)
    master.config(bg='#081923')

    def get_num():
        ph_num = Num.get()

        if ph_num == '':
            messagebox.showerror('Error', 'Please, Enter a phone number')

        else:
            with open('user_info/watsup_num.txt', 'w') as f:
                f.write(ph_num)

            master.destroy()

    lb = Label(master, text='Receiver Phone Number', font=(
        'Times Now Romans', 18, 'bold'), fg='#76FF03', bg='#081923')
    lb.place(x=60, y=10)

    Num = Entry(master,  font=('Times Now Romans', 13, 'bold'))
    Num.insert(0, 'For E.g. : +91xxxxxxxxx')
    Num.place(x=60, y=60, width=280)
    Num.focus()

    bt = Button(master, text='Ok', bd=5, font=('Times Now Romans', 14, 'normal'), bg='#536DFE',
                fg='white', activebackground='#536DFE', activeforeground='white', command=get_num)
    bt.place(x=170, y=100)

    master.mainloop()


def sender(message):
    with open('user_info/watsup_num.txt') as f:
        phone_no = f.read()

    webbrowser.open('https://web.whatsapp.com/send?phone=' +
                    phone_no+'&text='+message)

    from pynput.mouse import Button, Controller
    import time
    my_mouse = Controller()
    time.sleep(15)
    my_mouse.position = (840, 648)
    my_mouse.click(Button.left, 1)
    time.sleep(3)
    import keyboard
    keyboard.press_and_release('enter')
