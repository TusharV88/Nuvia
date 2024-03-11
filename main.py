# Main file of the assistance
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
import Clock 
import cv2
import Face_Recognitiontv as Frtv
import codeword as passtv
import weather_main as weatv
import time
import speech_recognition as sr
from speech_recognition import  UnknownValueError, RequestError 
import commander as opb
import threading as thr
import Nuvia_Voice 
import json
from random import choice
from Nuvia_Timer import startTimer
import Whatsapp as watv
import Downloader
from PIL import ImageTk, Image
import os
import math
import random


def create_folder(folder_name):
    # Get the current working directory
    current_directory = os.getcwd()

    # Create the full path for the new folder
    new_folder_path = os.path.join(current_directory, folder_name)

    # Check if the folder already exists
    if not os.path.exists(new_folder_path):
        # Create the folder if it doesn't exist
        os.makedirs(new_folder_path)



for name in ['dataset', 'Downloads', 'Files_Document', 'recognizers', 'simple_images', 'Songs']:
    # Call the function to create the folder
    create_folder(name)


win = tk.Tk()

# Title
win.title('                                                                    Nuvia')

# Window size
win.geometry('600x400')
win.minsize(600, 400)  # Minimum size of window
win.maxsize(600, 400)  # Maximum size of window

# Set Icon for window
win.iconbitmap("Images/Others/nuvia_logo.ico")


# Images for buttons
log_pic = PhotoImage(file="Images/Buttons/Login.png")
reg_pic = PhotoImage(file="Images/Buttons/Register.png")
reg_back_b = PhotoImage(file="Images/Buttons/Back_1.png")
face_reco_img = PhotoImage(file="Images/Buttons/facel_b.png")
pass_b_img = PhotoImage(file="Images/Buttons/password_button.png")
both_b_img = PhotoImage(file="Images/Buttons/Both.png")
submit_bt = PhotoImage(file="Images/Buttons/submit_button.png")
pass_gen_bimg = PhotoImage(file="Images/Buttons/generate.png")
flock_bimg = PhotoImage(file="Images/Buttons/Start.png")
pass_log_bt = PhotoImage(file="Images/Buttons/log_bt.png")
for_pass_bt = PhotoImage(file="Images/Buttons/continue_bt.png")
ent_bt_img = PhotoImage(file="Images/Buttons/Enter_Button.png")


# Images for face and password
face = PhotoImage(file="Images/Others/face_id.png")
pass_img = PhotoImage(file="Images/Others/pass_label.png")
both_img = PhotoImage(file="Images/Others/Both_label.png")

# Images for Avatars
pp_avat = PhotoImage(file="Images/Others/pp_label.png")
avatar1 = PhotoImage(file="Images/Avatars/Avatar Button/Male_b1.png")
avatar2 = PhotoImage(file="Images/Avatars/Avatar Button/Male_b2.png")
avatar3 = PhotoImage(file="Images/Avatars/Avatar Button/Male_b3.png")
avatar4 = PhotoImage(file="Images/Avatars/Avatar Button/Male_b4.png")
avatar5 = PhotoImage(file="Images/Avatars/Avatar Button/Female_b1.png")
avatar6 = PhotoImage(file="Images/Avatars/Avatar Button/Female_b2.png")
avatar7 = PhotoImage(file="Images/Avatars/Avatar Button/Female_b3.png")
avatar8 = PhotoImage(file="Images/Avatars/Avatar Button/Female_b4.png")
Male_pp1 = PhotoImage(file="Images/Avatars/Avatar Label/male1.png")
Male_pp2 = PhotoImage(file="Images/Avatars/Avatar Label/male2.png")
Male_pp3 = PhotoImage(file="Images/Avatars/Avatar Label/male3.png")
Male_pp4 = PhotoImage(file="Images/Avatars/Avatar Label/male4.png")
Female_pp5 = PhotoImage(file="Images/Avatars/Avatar Label/female1.png")
Female_pp6 = PhotoImage(file="Images/Avatars/Avatar Label/female2.png")
Female_pp7 = PhotoImage(file="Images/Avatars/Avatar Label/female4.png")
Female_pp8 = PhotoImage(file="Images/Avatars/Avatar Label/female3.png")
user_log1 = PhotoImage(file="Images/Avatars/Avatar Label/male_log1.png")
user_log2 = PhotoImage(file="Images/Avatars/Avatar Label/male_log2.png")
user_log3 = PhotoImage(file="Images/Avatars/Avatar Label/male_log3.png")
user_log4 = PhotoImage(file="Images/Avatars/Avatar Label/male_log4.png")
user_log5 = PhotoImage(file="Images/Avatars/Avatar Label/female_log1.png")
user_log6 = PhotoImage(file="Images/Avatars/Avatar Label/female_log2.png")
user_log7 = PhotoImage(file="Images/Avatars/Avatar Label/female_log3.png")
user_log8 = PhotoImage(file="Images/Avatars/Avatar Label/female_log4.png")
male_pfp1 = PhotoImage(file="Images/Avatars/Avatar Button/male_pfp1.png")
male_pfp2 = PhotoImage(file="Images/Avatars/Avatar Button/male_pfp2.png")
male_pfp3 = PhotoImage(file="Images/Avatars/Avatar Button/male_pfp3.png")
male_pfp4 = PhotoImage(file="Images/Avatars/Avatar Button/male_pfp4.png")
female_pfp1 = PhotoImage(file="Images/Avatars/Avatar Button/female_pfp1.png")
female_pfp2 = PhotoImage(file="Images/Avatars/Avatar Button/female_pfp2.png")
female_pfp3 = PhotoImage(file="Images/Avatars/Avatar Button/female_pfp3.png")
female_pfp4 = PhotoImage(file="Images/Avatars/Avatar Button/female_pfp4.png")


# Male and Female Options
dot_m = PhotoImage(file="Images/Others/dot_gen.png")

# Red Cross
red_crs = PhotoImage(file="Images/Others/red_cross.png")

# Bot Image
bot = PhotoImage(file="Images/Others/bot_img.png")

# Face Recognition Login
face_reco_log = PhotoImage(file="Images/Others/face_log.png")

# Password Login
pass_log_img = PhotoImage(file="Images/Others/password_login.png")

# Generate Image
generte_img = PhotoImage(file="Images/Others/generate_template.png")

# OTP Image
otp_img = PhotoImage(file="Images/Others/Verify_img.png")

# Security Image
secur_img = PhotoImage(file="Images/Others/security_label.png")

# Weather Template
weather_temp = PhotoImage(file="Images/weather_images/weather_temp3.png")

# Weather Images
clear_day = PhotoImage(file="Images/weather_images/clear_day_img.png")
clear_night = PhotoImage(file="Images/weather_images/clear_night_img.png")
broken_clouds = PhotoImage(file="Images/weather_images/broken_clouds_img.png")
few_day = PhotoImage(file="Images/weather_images/few_clouds_day_img.png")
few_night = PhotoImage(file="Images/weather_images/few_clouds_night_img.png")
mist = PhotoImage(file="Images/weather_images/mist_img.png")
rain_day = PhotoImage(file="Images/weather_images/rain_day_img.png")
rain_night = PhotoImage(file="Images/weather_images/rain_night_img.png")
scattered_clouds = PhotoImage(file="Images/weather_images/scattered_clouds_img.png")
shower_rain = PhotoImage(file="Images/weather_images/shower_rain_img.png")
snow = PhotoImage(file="Images/weather_images/snow_img.png")
thunder_storm = PhotoImage(file="Images/weather_images/thunderstorm_img.png")

clear_day_big = PhotoImage(file="Images/weather_images/Clear_day_big.png")
clear_night_big = PhotoImage(file="Images/weather_images/Clear_night_big.png")
broken_clouds_big = PhotoImage(file="Images/weather_images/Broken_Clouds_big.png")
few_day_big = PhotoImage(file="Images/weather_images/Few_Clouds_Day_big.png")
few_night_big = PhotoImage(file="Images/weather_images/Few_Clouds_Night_big.png")
mist_big = PhotoImage(file="Images/weather_images/Mist_big.png")
rain_day_big = PhotoImage(file="Images/weather_images/Rain_Day_big.png")
rain_night_big = PhotoImage(file="Images/weather_images/Rain_Night_big.png")
scattered_clouds_big = PhotoImage(file="Images/weather_images/Scattered_Clouds_big.png")
shower_rain_big = PhotoImage(file="Images/weather_images/Shower_Rain_big.png")
snow_big = PhotoImage(file="Images/weather_images/Snow_big.png")
thunder_storm_big = PhotoImage(file="Images/weather_images/Thunderstorm_big.png")
humidity_img = PhotoImage(file="Images/weather_images/humidity_img.png")

# NO Internet Image
no_internet_img = PhotoImage(file="Images/Others/no_connection.png")

# Setting Image
set_img = PhotoImage(file="Images/Others/settings_img.png")

# Mic Image
mic_img = PhotoImage(file="Images/Others/mic_img.png")

# Activity Status Label Image
act_lb_img = PhotoImage(file="Images/Others/status.png")

# Keyboard Image
key_img = PhotoImage(file="Images/Others/keyboard_img.png")

# Nuvia Image
nuvia_img = PhotoImage(file="Images/Others/nuvia_logo1.png")

# Camera Image
camera_img = PhotoImage(file="Images/Others/cam_img.png")

# Edit Image
edit_img = PhotoImage(file="Images/Others/edit_img.png")


# Animation Images
speaker1 = PhotoImage(file="Images/Others/speaker_img1.png")
speaker2 = PhotoImage(file="Images/Others/speaker_img2.png")
speaker3 = PhotoImage(file="Images/Others/speaker_img3.png")
speaker4 = PhotoImage(file="Images/Others/speaker_img4.png")

# list object for each frames
frames = [speaker1, speaker2, speaker3, speaker4]

# Heads and Tails
tail = PhotoImage(file="Images/Others/tails_img.png")
head = PhotoImage(file="Images/Others/heads_img.png")

# Dice Numbers
num1_img = PhotoImage(file="Images/Dice/num1_img.png")
num2_img = PhotoImage(file="Images/Dice/num2_img.png")
num3_img = PhotoImage(file="Images/Dice/num3_img.png")
num4_img = PhotoImage(file="Images/Dice/num4_img.png")
num5_img = PhotoImage(file="Images/Dice/num5_img.png")
num6_img = PhotoImage(file="Images/Dice/num6_img.png")

# Text Field Image
key_field = PhotoImage(file="Images/Others/textField.png")


# Cpu Meter Image
meter1 = PhotoImage(file="Images/Others/meter_1.png")
meter2 = PhotoImage(file="Images/Others/meter_2.png")
meter3 = PhotoImage(file="Images/Others/meter_3.png")
meter4 = PhotoImage(file="Images/Others/meter_4.png")
meter5 = PhotoImage(file="Images/Others/meter_5.png")

# Memory Image
memory_image = PhotoImage(file="Images/Others/Memory_Image.png")

# Battery Image
battery1 = PhotoImage(file="Images/Others/battery_img1.png")
battery2 = PhotoImage(file="Images/Others/battery_img2.png")
battery3 = PhotoImage(file="Images/Others/battery_img3.png")
battery4 = PhotoImage(file="Images/Others/battery_img4.png")
battery5 = PhotoImage(file="Images/Others/battery_img5.png")
battery6 = PhotoImage(file="Images/Others/battery_img6.png")

# Date and Time Image
date_img = PhotoImage(file="Images/Others/Blank_Calender.png")
time_img = PhotoImage(file="Images/Others/clock_temp.png")
timer_img = PhotoImage(file="Images/Others/timer_temp.png")

# Settings Apply Image
apply_img = PhotoImage(file="Images/Buttons/apply_image.png")


# All Frames
def main_fr():
    # ================Welcome Frame
    welcome_frame = Frame(win, bg='#081923')
    welcome_frame.pack(fill=BOTH, expand=True)

    # =================Register Frame
    reg_fr = Frame(win, bg='#081923')

    # =================Password Frame
    pass_fr = Frame(win, bg='#081923')

    # =================Face Lock Frame
    flock_fr = Frame(win, bg='#081923')

    # ================Account Frame
    acc_fr = Frame(win, bg='#081923')

    # ================Login Frame when No Register
    no_fr = Frame(win, bg='#081923')

    # ================Login Frame when Face Lock
    flog_fr = Frame(win, bg='#081923')

    # ================Login Frame when Password
    plog_fr = Frame(win, bg='#081923')

    # ================otp Frame
    otp_fr = Frame(win, bg='#081923')

    # ================Both Login Frame
    both_log_fr = Frame(win, bg='#081923')

    # ================Reset Password Frame
    reset_fr = Frame(win, bg='#081923')


    # Adding image on welcome page in Welcome Frame
    render = PhotoImage(file="Images/welcome/Nuvia-Welcome.png")

    img = Label(welcome_frame, image=render, bg='#081923')
    img.image = render
    img.place(x=140, y=10)

    # Label for hr, min and sec
    lb_hr = Label(welcome_frame, text='12', font=(
        'Brush Script MT', 27, 'bold'), bg='#081923', fg='#00bfff')
    lb_hr.place(x=35, y=170)

    lb_hr2 = Label(welcome_frame, text='HOUR', font=(
        'Perpetua', 15, 'bold'), bg='#081923', fg='#00bfff')
    lb_hr2.place(x=25, y=240)

    lb_min = Label(welcome_frame, text='12', font=(
        'Brush Script MT', 27, 'bold'), bg='#081923', fg='#00bfff')
    lb_min.place(x=140, y=170)

    lb_min2 = Label(welcome_frame, text='MINUTE', font=(
        'Perpetua', 15, 'bold'), bg='#081923', fg='#00bfff')
    lb_min2.place(x=120, y=240)

    lb_sec = Label(welcome_frame, text='12', font=(
        'Brush Script MT', 27, 'bold'), bg='#081923', fg='#7CFC00')
    lb_sec.place(x=405, y=170)

    lb_sec2 = Label(welcome_frame, text='SECOND', font=(
        'Perpetua', 15, 'bold'), bg='#081923', fg='#7CFC00')
    lb_sec2.place(x=385, y=240)

    lb_noon = Label(welcome_frame, text='PM', font=(
        'Brush Script MT', 25, 'bold'), bg='#081923', fg='#7CFC00')
    lb_noon.place(x=507, y=170)

    lb_noon2 = Label(welcome_frame, text='NOON', font=(
        'Perpetua', 15, 'bold'), bg='#081923', fg='#7CFC00')
    lb_noon2.place(x=505, y=240)

    lb_date = Label(welcome_frame, text='date', font=(
        'Perpetua', 23, 'bold'), bg='#081923', fg='#00bfff')
    lb_date.place(x=430, y=120)

    lb_day = Label(welcome_frame, text='day', font=(
        'Brush Script MT', 40, 'bold'), bg='#081923', fg='#7CFC00')
    lb_day.place(x=25, y=280)

    # Bar Lines
    bar1 = Label(welcome_frame,  bg='#FFFF00')
    bar1.place(x=380, y=160, width=355, height=5)

    bar2 = Label(welcome_frame,  bg='#FFFF00')
    bar2.place(x=0, y=270, width=230, height=5)

    # Greet file
    with open('user_info/greet_user.txt', 'w') as f:
        f.write('not done')

    # Normal Chat JSON File
    chat_data = json.load(open('json_work/NormalChat.json', encoding='utf-8'))
   
   # Read sites names
    with open('user_info/web_sites.txt') as f:
        sites = f.read()
    
    # Change Mode
    with open('user_info/thread_manage.txt', 'w') as f:
        f.write('none')
    
    with open('user_info/keyboard_cog.txt', 'w') as f:
        f.write('not pass')
    

    # NUVIA VA
    def nuvia():
        chat_bg = '#081923' 
        
        # ================Nuvia Frame
        nuvia_fr = Frame(win, bg=chat_bg)
        nuvia_fr.pack(fill=BOTH, expand=True)

        # Speaker Label
        speaker_anim = Label(nuvia_fr, bg=chat_bg)

        # All Labels 
        lisn_lb3 =  Label(nuvia_fr,  bg=chat_bg)
        lisn_lb3.place(x=140, y=110, width=40, height=27)


        def animation(count=0):
            im2 = frames[count]

            speaker_anim.configure(image=im2)
            count += 1
            if count == 4:
                count = 0
            nuv_b1.after(200, lambda: animation(count))
            
        def clear_screen(bonk):
            if bonk == 1:
                # Chats
                clear_lb = Label(nuvia_fr, bg=chat_bg)
                clear_lb.place(x=30, y=155, width=600, height=170)
                
                # Status
                clear_lb2 = Label(nuvia_fr, bg=chat_bg)
                clear_lb2.place(x=181, y=100, width=280, height=45)
            
            else:
                #Chats
                clear_lb = Label(nuvia_fr, bg=chat_bg)
                clear_lb.place(x=30, y=155, width=600, height=170)
                

        # Speech to Keyboard
        def spm_key():
            with open('user_info/thread_manage.txt', 'w') as f:
                f.write('stop thread')
            
            speech_medium()


        # Take Commands from user
        def takeCommand():
            with open('user_info/greet_user.txt') as f:
                greet = f.read()

            lisn_lb2 = Label(nuvia_fr, text='Speaking...', font=('Times Now Romans', 18, 'bold'), fg= 'white', bg='#203647')
            if greet == 'not done':
                lisn_lb5 = Label(nuvia_fr, text='Welcome', font=('Times Now Romans', 25, 'bold'), fg= '#8BC34A', bg='#081923')
                lisn_lb5.place(x=235, y=100)
                Nuvia_Voice.wishMe()
                with open('user_info/greet_nuvia.txt') as f:
                    greet = f.read()
                lisn_lb4 = Label(nuvia_fr, text=greet, font=('Times Now Romans', 15, 'bold'), fg= 'white', bg='#03A9F4', justify=LEFT)
                lisn_lb4.place(x=30, y=160)
                lisn_lb2.place(x=220, y=345, width=153)
                Nuvia_Voice.speak(greet)    
                clear_screen(1)
            
            nuv_b2.place(x=20, y=330)  # Keyboard Button

            # Speaker Label
            speaker_anim.place(x=140, y=110)

            with open('user_info/thread_manage.txt', 'r') as f:
                    check = f.read()

            #It takes microphone input from the user and returns string output
            if check == 'none':
                lisn_lb = Label(nuvia_fr, text='Listening...', font=('Times Now Romans', 18, 'bold'), fg='white', bg='#203647')
                lisn_lb.place(x=220, y=345, width=153)
                r = sr.Recognizer()
                r.dynamic_energy_threshold = False
                r.energy_threshold = 300
                r.pause_threshold = 1
                with sr.Microphone() as source:
                    audio = r.listen(source)
                    
            elif check == 'settings': pass

            try:
                with open('user_info/thread_manage.txt', 'r') as f:
                    check = f.read()
                if check == 'none':
                    lisn_lb = Label(nuvia_fr, text='Processing...', font=('Times Now Romans', 18, 'bold'), fg='white', bg='#203647')
                    lisn_lb.place(x=220, y=345)
                    recognized = r.recognize_google(audio, language='en-In')
                    recognized = recognized[0].upper() + recognized[1:]
                else: 
                    pass

            except RequestError as e:   # If internet is not working
                return 'none'

            except UnknownValueError:  # If can't recognize voice properly
                return 'none'
            
            if check == 'none': 
                return recognized
            else:
                return 'none'

        # Handle Speech Recognition
        def speech_medium():
            while True:
                with open('user_info/thread_manage.txt', 'r') as f:
                    check = f.read()
                
                if check == 'stop thread':
                    key_commands()
                    break
                elif check == 'settings': pass
                else: 
                    nuv_b2.place(x=20, y=330)
                    query = takeCommand()
                    
                    if query == 'none': continue
                    elif query in ['exit']:
                        Nuvia_Voice.speak('Shutting down the system, good bye')
                    else: 
                        process_commands(query.lower())
                

        # Keyboard Commands 
        def key_commands():
            # Label
            field_lb = Label(nuvia_fr, image=key_field, bg='white')
            field_lb.place(x=140, y=330)
            # Keyboard Entry
            key_en = Entry(nuvia_fr, font=('Times Now Romans', 14, 'normal'), fg='white', bg='#203647', bd=0)
            key_en.insert(0,'Type Your Query Here...')
            key_en.place(x=160, y=350, width=285)
            nuv_b2.place_forget()
            # Mic Button
            nuv_b3.place(x=20, y=330)

            # Keyboard Event
            def key_getter(e):
                user_input = key_en.get().lower()
                
                if user_input != '': 
                    if user_input in ['exit']:
                            Nuvia_Voice.speak('Shutting down the system, good bye')
                    else: 
                        thr.Thread(target=process_commands, args=(user_input,)).start()
                key_en.delete(0, END)
                    
            key_en.bind('<Return>', key_getter)

            # Mouse Event
            def invisble_labels(e):
                field_lb.place_forget()
                key_en.place_forget()

            nuv_b3.bind("<Button-1>", invisble_labels)

        # keyboard to speech medium
        def key_spm():
            nuv_b3.place_forget()
            with open('user_info/thread_manage.txt', 'w') as f:
                f.write('none')
                
            with open('user_info/check_recog.txt', 'r') as f:
                recog = f.read()
                
            if recog == 'not recognized': 
                thr.Thread(target=speech_medium).start()
            else:
                thr.Thread(target=takeCommand).start()


        # Process user commands
        def process_commands(query):  
            with open('user_info/screen_wipe.txt', 'r') as f:
                wipe = f.read()

            if wipe == 'not clear':            
                clear_screen(1)

            lisn_lb2 = Label(nuvia_fr, text='Speaking...', font=('Times Now Romans', 18, 'bold'), fg= 'white', bg='#203647')
            lisn_lb5 = Label(nuvia_fr, font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#081923', wraplength=350)
            lisn_lb5.place(x=30, y=160)

            # Query Filter
            text = opb.speech_filter(query)
            with open('user_info/thread_manage.txt') as f:
                check = f.read()

            if text in chat_data:
                lisn_lb3.place(x=1240, y=110)
                chat = choice(chat_data[text])
                lisn_lb5.config(text=chat, bg='#03A9F4')
                lisn_lb4 = Label(nuvia_fr, text=query.capitalize(), font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', wraplength=200)
                lisn_lb4.place(x=400, y=157)
                if check != 'stop thread':
                    lisn_lb2.place(x=220, y=345, width=153)
                    Nuvia_Voice.speak(chat)
                else:
                    Nuvia_Voice.speak(chat)
                lisn_lb3.place(x=140, y=110, width=40, height=27)

            elif text in ['joke', 'jokes']:
                lisn_lb4 = Label(nuvia_fr, text=query.capitalize(), font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', wraplength=200)
                lisn_lb4.place(x=400, y=157)
                joke = opb.nuvia_jokes()
                lisn_lb5.config(text=joke, bg='#03A9F4', justify='left')
                lisn_lb3.place(x=1240, y=110)                
                if check != 'stop thread':
                    lisn_lb2.place(x=220, y=345, width=153)
                    Nuvia_Voice.speak(joke)
                else:
                    Nuvia_Voice.speak(joke)
                lisn_lb3.place(x=140, y=110, width=40, height=27)


            elif text in ['news', 'read news']:
                lisn_lb4 = Label(nuvia_fr, text=query.capitalize(), font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', wraplength=200)
                lisn_lb4.place(x=400, y=157)
                lisn_lb5.place(x=210, y=100)
                if check != 'stop thread':
                    lisn_lb2.place(x=220, y=345, width=153)
                lisn_lb3.place(x=1240, y=110)
                lisn_lb5 = Label(nuvia_fr, text='Today Top Headlines', font=('Times Now Romans', 18, 'bold'), fg= '#8BC34A', bg='#081923')
                lisn_lb5.place(x=180, y=100)
                
                Nuvia_Voice.speak(f"today top headlines are")
                news_count = 1
                topic = opb.nuvia_news()
                for news in topic:
                    clear_lb = Label(nuvia_fr, bg='#081923')
                    clear_lb.place(x=30, y=190, width=600, height=140)
                    lisn_lb5 = Label(nuvia_fr,text=f'{news_count}. {news.title()}' ,font = ('Times Now Romans',
                        13, 'bold'), fg= 'white', bg='#03A9F4', justify='left', wraplength=400)
                    lisn_lb5.place(x=30, y=190)
                    Nuvia_Voice.speak(news)
                    news_count += 1
                    if news_count == 6:
                        lisn_lb3.place(x=140, y=110, width=40, height=27)
                        break


            elif text in ['play youtube']: 
                lisn_lb7 = Label(nuvia_fr, text='YouTube Player', font=('Times Now Romans', 18, 'bold'), fg= '#8BC34A', bg='#081923')
                lisn_lb7.place(x=210, y=100)
                lisn_lb4 = Label(nuvia_fr, text=query.capitalize(), font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', wraplength=200)
                lisn_lb4.place(x=400, y=157)
                lisn_lb3.place(x=1240, y=110)
                lisn_lb5.config(text='Tell me a video name', bg='#03A9F4')
                Nuvia_Voice.speak('tell me a video name')
                lisn_lb3.place(x=140, y=110, width=40, height=27)
                
                if check != 'stop thread':
                    lisn_lb2.place(x=220, y=345, width=153)
                    
                    while True:
                        topic = takeCommand()
                        if topic == 'none': 
                            continue
                        
                        else:
                            opb.play_yt(topic)
                            lisn_lb2.place(x=220, y=345, width=153)
                            lisn_lb3.place(x=1240, y=110)
                            lisn_lb5.config(text='Have Fun!!')
                            Nuvia_Voice.speak('have fun')
                            lisn_lb3.place(x=140, y=110, width=40, height=27)

                        return
                else:
                    # Keyboard Entry
                    key_en2 = Entry(nuvia_fr, font=('Times Now Romans', 14, 'normal'), fg='white', bg='#203647', bd=0)
                    key_en2.place(x=160, y=350, width=285)
                    def key_getter(e):
                        user_input = key_en2.get().lower()

                        if user_input == 'none' : ''
                        else: 
                            opb.play_yt(user_input)
                            
                        key_en2.destroy()

                    key_en2.bind('<Return>', key_getter)


            elif text in ['search youtube']:
                lisn_lb7 = Label(nuvia_fr, text='YouTube Search', font=('Times Now Romans', 18, 'bold'), fg= '#8BC34A', bg='#081923')
                lisn_lb7.place(x=210, y=100)
                lisn_lb4 = Label(nuvia_fr, text=query.capitalize(), font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', wraplength=200)
                lisn_lb4.place(x=400, y=157)
                lisn_lb3.place(x=1240, y=110)
                lisn_lb5.config(text='What do you want to search ?', bg='#03A9F4')
                Nuvia_Voice.speak('what do you want to search')
                lisn_lb3.place(x=140, y=110, width=40, height=27)
                
                if check != 'stop thread':
                    lisn_lb2.place(x=220, y=345, width=153)
                    
                    while True:
                        topic = takeCommand()
                        if topic == 'none': 
                            continue
                        
                        else:
                            opb.search_yt(topic)
                            lisn_lb2.place(x=220, y=345, width=153)
                            lisn_lb3.place(x=1240, y=110)
                            lisn_lb5.config(text='Here you go')
                            Nuvia_Voice.speak('here you go')
                            lisn_lb3.place(x=140, y=110, width=40, height=27)

                        return
                else:
                    # Keyboard Entry
                    key_en2 = Entry(nuvia_fr, font=('Times Now Romans', 14, 'normal'), fg='white', bg='#203647', bd=0)
                    key_en2.place(x=160, y=350, width=285)
                    def key_getter(e):
                        user_input = key_en2.get().lower()

                        if user_input == 'none' : ''
                        else: 
                            opb.search_yt(user_input)
                            
                        key_en2.destroy()

                    key_en2.bind('<Return>', key_getter)
                    

            elif text in ['search google', 'google search']:
                lisn_lb7 = Label(nuvia_fr, text='Google Search', font=('Times Now Romans', 18, 'bold'), fg= '#8BC34A', bg='#081923')
                lisn_lb7.place(x=210, y=100)
                lisn_lb4 = Label(nuvia_fr, text=query.capitalize(), font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', wraplength=200)
                lisn_lb4.place(x=400, y=157)
                lisn_lb3.place(x=1240, y=110)
                lisn_lb5.config(text='What do you want to search ?', bg='#03A9F4')
                Nuvia_Voice.speak('what do you want to search')
                lisn_lb3.place(x=140, y=110, width=40, height=27)
                
                if check != 'stop thread':
                    lisn_lb2.place(x=220, y=345, width=153)
                    while True:
                        topic = takeCommand()
                        if topic == 'none': 
                            continue
                        
                        else:
                            opb.search_google(topic)
                            lisn_lb2.place(x=220, y=345, width=153)
                            lisn_lb3.place(x=1240, y=110)
                            lisn_lb5.config(text='Here you go')
                            Nuvia_Voice.speak('here you go')
                            lisn_lb3.place(x=140, y=110, width=40, height=27)

                        return
                else:
                    # Keyboard Entry
                    key_en2 = Entry(nuvia_fr, font=('Times Now Romans', 14, 'normal'), fg='white', bg='#203647', bd=0)
                    key_en2.place(x=160, y=350, width=285)
                    def key_getter(e):
                        user_input = key_en2.get().lower()

                        if user_input == 'none' : ''
                        else: 
                            opb.search_google(user_input)
                            
                        key_en2.destroy()

                    key_en2.bind('<Return>', key_getter)
                    

            elif text in ['toss a coin']:
                lisn_lb4 = Label(nuvia_fr, text=query.capitalize(), font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', wraplength=200)
                lisn_lb4.place(x=400, y=157)
                side = opb.coin_toss()
                if side == 'head':
                    lisn_lb5.place(x=130, y=170)
                    lisn_lb5.config(image=head, bg='#081923')
                else:
                    lisn_lb5.place(x=130, y=170)
                    lisn_lb5.config(image=tail, bg='#081923')
                
                if check != 'stop thread': 
                    lisn_lb2.place(x=220, y=345, width=153)
                lisn_lb3.place(x=1240, y=110)
                Nuvia_Voice.speak(f"it's a {side}")
                lisn_lb3.place(x=140, y=110, width=40, height=27)

            elif text in ['roll a dice']:
                lisn_lb4 = Label(nuvia_fr, text=query.capitalize(), font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', wraplength=200)
                lisn_lb4.place(x=400, y=157)
                num = opb.dice_roll()
                if num == 1:
                    lisn_lb5.place(x=130, y=165)
                    lisn_lb5.config(image=num1_img, bg='#081923')
                elif num == 2:
                    lisn_lb5.place(x=130, y=165)
                    lisn_lb5.config(image=num2_img, bg='#081923')
                elif num == 3:
                    lisn_lb5.place(x=130, y=165)
                    lisn_lb5.config(image=num3_img, bg='#081923')
                elif num == 4:
                    lisn_lb5.place(x=130, y=165)
                    lisn_lb5.config(image=num4_img, bg='#081923')
                elif num == 5:
                    lisn_lb5.place(x=130, y=165)
                    lisn_lb5.config(image=num5_img, bg='#081923')
                else:
                    lisn_lb5.place(x=130, y=165)
                    lisn_lb5.config(image=num6_img, bg='#081923')

                if check != 'stop thread': 
                    lisn_lb2.place(x=220, y=345, width=153)
                lisn_lb3.place(x=1240, y=110)
                Nuvia_Voice.speak(f"Number {num}")
                lisn_lb3.place(x=140, y=110, width=40, height=27)


            elif text in ['system info', 'system', 'system information']:
                lisn_lb5 = Label(nuvia_fr, text='System Information', font=('Times Now Romans', 18, 'bold'), fg= '#8BC34A', bg='#081923')
                lisn_lb5.place(x=210, y=100)
                mac, ver, plat, psys, pro = opb.sys_info(text)
                lisn_lb4 = Label(nuvia_fr, text=query.capitalize(), font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', wraplength=200)
                lisn_lb4.place(x=400, y=157)
                lisn_lb5 = Label(nuvia_fr,text='Machine : {} \nVersion : {} \nPlatform : {}\nSystem : {}\nProcessor : {}'.format(mac,ver,plat,psys, pro) ,font = ('Times Now Romans',
                        13, 'bold'), fg= 'white', bg='#03A9F4', justify='left', wraplength=350)
                lisn_lb5.place(x=30, y=170)
                if check != 'stop thread': 
                    lisn_lb2.place(x=220, y=345, width=153)
                lisn_lb3.place(x=1240, y=110)
                Nuvia_Voice.speak('here is your system information')
                Nuvia_Voice.speak(f'Machine : {mac}\nVersion : {ver}\nPlatform : {plat}\nSystem : {psys}\nProcessor : {pro}')
                lisn_lb3.place(x=140, y=110, width=40, height=27)


            elif text in ['cpu']:
                lisn_lb5 = Label(nuvia_fr, text='Cpu Usage', font=('Times Now Romans', 18, 'bold'), fg= '#8BC34A', bg='#081923')
                lisn_lb5.place(x=230, y=100)
                lisn_lb4 = Label(nuvia_fr, text=query.capitalize(), font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', wraplength=200)
                lisn_lb4.place(x=400, y=157)
                cpu = opb.sys_info(text)
                
                if cpu < 20:
                    meter_lb = Label(nuvia_fr, image=meter1, bg='#081923')
                    col = '#5dc764'
                elif cpu < 40:
                    meter_lb = Label(nuvia_fr, image=meter2, bg='#081923')
                    col = '#a3c75f'
                elif cpu < 60:
                    meter_lb = Label(nuvia_fr, image=meter3, bg='#081923')
                    col = '#fec65d'
                elif cpu < 80:
                    meter_lb = Label(nuvia_fr, image=meter4, bg='#081923')
                    col = '#ffa660'
                else:
                    meter_lb = Label(nuvia_fr, image=meter5, bg='#081923')
                    col = '#fa314b'

                meter_lb.place(x=80, y=155)
                lisn_lb5 = Label(nuvia_fr, text=f'{cpu}%', font=('Times Now Romans', 14, 'bold'), fg= col, bg='#081923')
                lisn_lb5.place(x=149, y=270)
                if check != 'stop thread': 
                    lisn_lb2.place(x=220, y=345, width=153)
                lisn_lb3.place(x=1240, y=110)
                Nuvia_Voice.speak(f'cpu is {cpu}%')
                lisn_lb3.place(x=140, y=110, width=40, height=27)


            elif text in ['memory']:
                lisn_lb5 = Label(nuvia_fr, text='Memory Usage', font=('Times Now Romans', 18, 'bold'), fg= '#8BC34A', bg='#081923')
                lisn_lb5.place(x=213, y=100)
                lisn_lb4 = Label(nuvia_fr, text=query.capitalize(), font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', wraplength=200)
                lisn_lb4.place(x=400, y=157)
                mem = opb.sys_info(text)
                memory_lb = Label(nuvia_fr, image=memory_image, bg='#081923')
                memory_lb.place(x=30, y=160) 
                lisn_lb5 = Label(nuvia_fr, text=f'{mem}%', font=('Times Now Romans', 14, 'bold'), fg= 'white', bg='#0f1e26')
                lisn_lb5.place(x=68, y=185)
                if check != 'stop thread': 
                    lisn_lb2.place(x=220, y=345, width=153)
                lisn_lb3.place(x=1240, y=110)
                Nuvia_Voice.speak(f'memory is {mem}%')
                lisn_lb3.place(x=140, y=110, width=40, height=27)

            elif text in ['music', 'song']:
                lisn_lb5 = Label(nuvia_fr, text='Music', font=('Times Now Romans', 20, 'bold'), fg= '#8BC34A', bg='#081923')
                lisn_lb5.place(x=240, y=100)
                lisn_lb4 = Label(nuvia_fr, text=query.capitalize(), font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', wraplength=200)
                lisn_lb4.place(x=400, y=157)
                song = opb.play_music()
                lisn_lb5 = Label(nuvia_fr,text=f'{song}' ,font = ('Times Now Romans',
                        13, 'bold'), fg= 'white', bg='#03A9F4', justify='left', wraplength=400)
                lisn_lb5.place(x=30, y=190)
                if check != 'stop thread': 
                    lisn_lb2.place(x=220, y=345, width=153)
                lisn_lb3.place(x=1240, y=110)
                Nuvia_Voice.speak(f'playing {song}')
                lisn_lb3.place(x=140, y=110, width=40, height=27)

            elif text in ['battery']:
                lisn_lb5 = Label(nuvia_fr, text='Battery Info', font=('Times Now Romans', 20, 'bold'), fg= '#8BC34A', bg='#081923')
                lisn_lb5.place(x=225, y=100)
                lisn_lb4 = Label(nuvia_fr, text=query.capitalize(), font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', wraplength=200)
                lisn_lb4.place(x=400, y=157)
                battery, plug = opb.sys_info(text)

                if plug == True:
                    battery_lb = Label(nuvia_fr, image=battery6, bg='#081923')
                    battery_lb.place(x=80, y=155)
                    lisn_lb5 = Label(nuvia_fr, text=f'{battery}%', font=('Times Now Romans', 16, 'bold'), fg= 'white', bg='#081923')
                    lisn_lb5.place(x=205, y=175)
                    # lisn_lb5.config(text=f'{battery}%') 
                    if check != 'stop thread': 
                        lisn_lb2.place(x=220, y=345, width=153)
                    lisn_lb3.place(x=1240, y=110)
                    Nuvia_Voice.speak(f'Battery {battery}% Charging')
                    lisn_lb3.place(x=140, y=110, width=40, height=27)

                else:    
                    if battery < 20:
                        battery_lb = Label(nuvia_fr, image=battery1, bg='#081923')
                        battery_lb.place(x=80, y=155)
                    elif battery < 40:
                        battery_lb = Label(nuvia_fr, image=battery2, bg='#081923')
                        battery_lb.place(x=80, y=155)
                    elif battery < 60:
                        battery_lb = Label(nuvia_fr, image=battery3, bg='#081923')
                        battery_lb.place(x=80, y=155)
                    elif battery < 80:
                        battery_lb = Label(nuvia_fr, image=battery4, bg='#081923')
                        battery_lb.place(x=80, y=155)
                    else:
                        battery_lb = Label(nuvia_fr, image=battery5, bg='#081923')
                        battery_lb.place(x=80, y=155)

                    lisn_lb5 = Label(nuvia_fr, text=f'{battery}%', font=('Times Now Romans', 16, 'bold'), fg= 'white', bg='#081923')
                    lisn_lb5.place(x=205, y=175)
                    if check != 'stop thread': 
                        lisn_lb2.place(x=220, y=345, width=153)
                    lisn_lb3.place(x=1240, y=110)
                    Nuvia_Voice.speak(f'Battery {battery}%')
                    lisn_lb3.place(x=140, y=110, width=40, height=27)


            elif text in ['date', 'time']:
                lisn_lb4 = Label(nuvia_fr, text=query.capitalize(), font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', wraplength=200)
                lisn_lb4.place(x=400, y=157)
                hr, min, sec, noon, date, month, year, day = Clock.current_time()
                if text == 'date':
                    lisn_lb5 = Label(nuvia_fr, text='Date', font=('Times Now Romans', 20, 'bold'), fg= '#8BC34A', bg='#081923')
                    lisn_lb5.place(x=250, y=100)
                    date_lb = Label(nuvia_fr, image=date_img, bg='#081923')
                    date_lb.place(x=80, y=155)
                    
                    month = str(time.strftime('%B'))
                    lisn_lb5 = Label(nuvia_fr, text=f'{day}', font=('Times Now Romans', 12, 'bold'), fg= 'white', bg='#f64143')
                    if day == 'Monday' or day == 'Tuesday' or day == 'Sunday':
                        lisn_lb5.place(x=120, y=183)
                    elif day == 'Thursday' or day == 'Saturday':
                        lisn_lb5.place(x=112, y=183)
                    elif day == 'Friday':
                        lisn_lb5.place(x=125, y=183)
                    else:
                        lisn_lb5.place(x=104, y=183)

                    lisn_lb5 = Label(nuvia_fr, text=f'{date}', font=('Times Now Romans', 35, 'bold'), fg= 'grey', bg='#f2f4fb')
                    lisn_lb5.place(x=122, y=213)

                    lisn_lb5 = Label(nuvia_fr, text=f'{month}', font=('Times Now Romans', 10, 'bold'), fg= 'grey', bg='#f2f4fb')
                    if month == 'February' or month == 'September' or month == 'November' or month == 'December':
                        lisn_lb5.place(x=118, y=273)
                    elif month == 'January' or month == 'October' or month == 'August' or month == 'March':
                        lisn_lb5.place(x=126, y=273)
                    else:
                        lisn_lb5.place(x=134, y=273)

                    lisn_lb5 = Label(nuvia_fr, text='Date', font=('Times Now Romans', 20, 'bold'), fg= '#8BC34A', bg='#081923')
                    if check != 'stop thread': 
                        lisn_lb2.place(x=220, y=345, width=153)
                    lisn_lb3.place(x=1240, y=110)
                    Nuvia_Voice.speak(f'{date} {month}')
                    lisn_lb3.place(x=140, y=110, width=40, height=27)

                elif text == 'time':
                    lisn_lb5 = Label(nuvia_fr, text='Time', font=('Times Now Romans', 20, 'bold'), fg= '#8BC34A', bg='#081923')
                    lisn_lb5.place(x=250, y=100)
                    time_lb = Label(nuvia_fr, image=time_img, bg='#081923')
                    time_lb.place(x=80, y=155)
                    lisn_lb5 = Label(nuvia_fr, text=f'{hr}', font=('Times Now Romans', 18, 'bold'), fg= '#8a5403', bg='#feffff')
                    lisn_lb5.place(x=117, y=185)
                    lisn_lb5 = Label(nuvia_fr, text=f'{min}', font=('Times Now Romans', 18, 'bold'), fg= '#8a5403', bg='#feffff')
                    lisn_lb5.place(x=175, y=185)

                    if check != 'stop thread': 
                        lisn_lb2.place(x=220, y=345, width=153)
                    lisn_lb3.place(x=1240, y=110)

                    if min == 00:
                        Nuvia_Voice.speak(f'{hr} hour {noon}')
                    else:
                        hr = int(hr)
                        min = int(min)
                        Nuvia_Voice.speak(f'{hr} hour {min} minute {noon}')
                    lisn_lb3.place(x=140, y=110, width=40, height=27)
                    
            elif text in ['timer']:
                lisn_lb5 = Label(nuvia_fr, text='Timer', font=('Times Now Romans', 20, 'bold'), fg= '#8BC34A', bg='#081923')
                lisn_lb5.place(x=250, y=100)
                lisn_lb4 = Label(nuvia_fr, text=query.capitalize(), font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', wraplength=200)
                lisn_lb4.place(x=400, y=157)
                timer_lb = Label(nuvia_fr, image=timer_img, bg='#081923')
                timer_lb.place(x=80, y=155)
                lisn_lb3.place(x=1240, y=110)
                Nuvia_Voice.speak('timer started')
                lisn_lb3.place(x=140, y=110, width=40, height=27)
                words = ['set', 'a', 'timer', 'for', 'second', 'seconds', ' ']
                thr.Thread(target=startTimer, args=(query,)).start()

            
            elif text in ['message', 'msg']:
                lisn_lb5 = Label(nuvia_fr, text='Whatsapp Message', font=('Times Now Romans', 18, 'bold'), fg= '#8BC34A', bg='#081923')
                lisn_lb5.place(x=180, y=100)
                lisn_lb4 = Label(nuvia_fr, text=query.capitalize(), font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', wraplength=200)
                lisn_lb4.place(x=400, y=157)
                lisn_lb5 = Label(nuvia_fr, text= 'To whom you want to send message?', font = ('Times Now Romans',13, 'bold'), fg= 'white', bg='#03A9F4', justify='left', wraplength=400)
                lisn_lb5.place(x=30, y=190)
                if check != 'stop thread':
                    lisn_lb2.place(x=220, y=345, width=153)
                lisn_lb3.place(x=1240, y=110)
                Nuvia_Voice.speak('To whom you want send msg')
                lisn_lb3.place(x=140, y=110, width=40, height=27)
                lisn_lb2.place(x=200000, y=30000)

                watv.watsup()
                if check != 'stop thread':
                    lisn_lb2.place(x=220, y=345, width=153)
                lisn_lb5.destroy()
                lisn_lb6 = Label(nuvia_fr, text= 'What messsage you want to send?', font = ('Times Now Romans',13, 'bold'), fg= 'white', bg='#03A9F4', justify='left', wraplength=400)
                lisn_lb6.place(x=30, y=190)
                lisn_lb3.place(x=1240, y=110)
                Nuvia_Voice.speak('what message you want to send')
                lisn_lb3.place(x=140, y=110, width=40, height=27)
                if check != 'stop thread':
                    while True:
                        msg = takeCommand()
                    
                        if msg == 'none': continue
                        else:
                            break

                else:
                    with open('user_info/watsapp_msg.txt', 'w') as f:
                        f.write('')
                    # Keyboard Entry
                    key_en2 = Entry(nuvia_fr, font=('Times Now Romans', 14, 'normal'), fg='white', bg='#203647', bd=0)
                    key_en2.place(x=160, y=350, width=285)
                    def key_getter2(e):
                        user_input = key_en2.get().lower()

                        if user_input == 'none' : ''
                        else: 
                            with open('user_info/watsapp_msg.txt', 'w') as f:
                                f.write(user_input)
                            
                    while True:
                        with open('user_info/watsapp_msg.txt', 'r') as f:
                            msg = f.read()
                        
                        key_en2.bind('<Return>', key_getter2)
                        if msg == '': continue
                        else:    
                            key_en2.destroy()
                            break

                thr.Thread(target=watv.sender, args=(msg,)).start()

            elif text in ['add list']:
                lisn_lb4 = Label(nuvia_fr, text=query.capitalize(), font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', wraplength=200)
                lisn_lb4.place(x=400, y=157)
                lisn_lb5 = Label(nuvia_fr, text='List', font=('Times Now Romans', 25, 'bold'), fg= '#8BC34A', bg='#081923')
                lisn_lb5.place(x=235, y=100)
                lisn_lb5 = Label(nuvia_fr, text='What do you want to add ?', font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4')
                lisn_lb5.place(x=30, y=190)
                if check != 'stop thread': 
                        lisn_lb2.place(x=220, y=345, width=153)
                lisn_lb3.place(x=1240, y=110)
                Nuvia_Voice.speak('what do you want to add')
                lisn_lb3.place(x=140, y=110, width=40, height=27)
                if check != 'stop thread':
                    while True:
                        query = takeCommand()

                        if query == 'none': continue
                        else:
                            break

                else:
                    with open('user_info/list_items.txt', 'w') as f:
                        f.write('')
                    # Keyboard Entry
                    key_en2 = Entry(nuvia_fr, font=('Times Now Romans', 14, 'normal'), fg='white', bg='#203647', bd=0)
                    key_en2.place(x=160, y=350, width=285)
                    def key_getter(e):
                        user_input = key_en2.get().lower()

                        if user_input == 'none' : ''
                        else: 
                            with open('user_info/list_items.txt', 'w') as f:
                                f.write(user_input)
                            
                    while True:
                        with open('user_info/list_items.txt', 'r') as f:
                            query = f.read()
                        
                        key_en2.bind('<Return>', key_getter)
                        if query == '': continue
                        else:    
                            key_en2.destroy()
                            break

                opb.toDoList(query)
                lisn_lb5 = Label(nuvia_fr, text='An item is added in your list', font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4')
                lisn_lb5.place(x=30, y=190)
                if check != 'stop thread': 
                        lisn_lb2.place(x=220, y=345, width=153)
                lisn_lb3.place(x=1240, y=110)
                Nuvia_Voice.speak('An item is added in your list')
                lisn_lb3.place(x=140, y=110, width=40, height=27)


            elif text in ['show list']:
                lisn_lb4 = Label(nuvia_fr, text=query.capitalize(), font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', wraplength=200)
                lisn_lb4.place(x=400, y=157)
                lisn_lb5 = Label(nuvia_fr, text='List', font=('Times Now Romans', 25, 'bold'), fg= '#8BC34A', bg='#081923')
                lisn_lb5.place(x=235, y=100)
                lisn_lb5 = Label(nuvia_fr, text='Here are your list items', font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4')
                lisn_lb5.place(x=30, y=190)
                if check != 'stop thread': 
                        lisn_lb2.place(x=220, y=345, width=153)
                lisn_lb3.place(x=1240, y=110)
                Nuvia_Voice.speak('Here are your list items')
                lisn_lb3.place(x=140, y=110, width=40, height=27)
                clear_screen(0)
                list = opb.showtoDoList()
                scroll_y = Scrollbar(nuvia_fr)
                tt = Text(nuvia_fr, height = 8, width = 55, bd=0, state='disabled', fg= 'white', bg='#03A9F4', font=('Times Now Romans', 11, 'bold'), yscrollcommand=scroll_y.set)
                scroll_y.place(x=475, y=160, height=146)
                scroll_y.config(command=tt.yview)
                tt.config(state='normal')

                for i in list:
                    tt.insert(END, i + '\n')
                tt.config(state='disabled')
                tt.place(x=30, y=160)
                
                for i in list:
                    lisn_lb3.place(x=1240, y=110)
                    Nuvia_Voice.speak(i)
                lisn_lb3.place(x=140, y=110, width=40, height=27)


            elif text in ['download youtube']:
                lisn_lb7 = Label(nuvia_fr, text='YouTube Downloader', font=('Times Now Romans', 18, 'bold'), fg= '#8BC34A', bg='#081923')
                lisn_lb7.place(x=180, y=100)
                lisn_lb4 = Label(nuvia_fr, text=query.capitalize(), font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', wraplength=200)
                lisn_lb4.place(x=400, y=157)
                lisn_lb5.config(text='Enter a youtube video url', bg='#03A9F4', justify='left')
                lisn_lb3.place(x=1240, y=110)
                Nuvia_Voice.speak('Enter a youtube video url')
                lisn_lb3.place(x=140, y=110, width=40, height=27)
                Downloader.yt_down()

                lisn_lb5.config(text='Download Starts', bg='#03A9F4', justify='left')
                lisn_lb3.place(x=1240, y=110)
                Nuvia_Voice.speak('Download starts')
                lisn_lb3.place(x=140, y=110, width=40, height=27)


            elif text in ['ppt', 'excel', 'powerpoint', 'power point','text', 'simple', 'normal', 'spreadsheet', 'word', 'document']:
                lisn_lb7 = Label(nuvia_fr, text=f'{text.title()} File', font=('Times Now Romans', 18, 'bold'), fg= '#8BC34A', bg='#081923')
                lisn_lb7.place(x=220, y=100)
                lisn_lb4 = Label(nuvia_fr, text=query.capitalize(), font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', wraplength=200)
                lisn_lb4.place(x=400, y=157)
                lisn_lb5.config(text='Sure Creating...', bg='#03A9F4', justify='left')
                lisn_lb3.place(x=1240, y=110)
                Nuvia_Voice.speak('Sure creating')
                lisn_lb3.place(x=140, y=110, width=40, height=27)
                file = opb.create_file(text)
                lisn_lb5.config(text='File Created', bg='#03A9F4', justify='left')
                lisn_lb3.place(x=1240, y=110)
                Nuvia_Voice.speak(file)
                lisn_lb3.place(x=140, y=110, width=40, height=27)


            elif text in ['direction']:            
                lisn_lb7 = Label(nuvia_fr, text='Google Maps', font=('Times Now Romans', 18, 'bold'), fg= '#8BC34A', bg='#081923')
                lisn_lb7.place(x=210, y=100)
                lisn_lb4 = Label(nuvia_fr, text=query.capitalize(), font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', wraplength=200)
                lisn_lb4.place(x=400, y=157)
                lisn_lb5.config(text='Tell me your start point', bg='#03A9F4', justify='left')
                lisn_lb2.place(x=220, y=345, width=153)
                lisn_lb3.place(x=1240, y=110)
                Nuvia_Voice.speak('Tell me your Start Point')
                lisn_lb3.place(x=140, y=110, width=40, height=27)
                if check != 'stop thread':
                    while True:
                        query = takeCommand()

                        if query == 'none': continue
                        else:
                            start_point = query
                            lisn_lb4.config(text=start_point.title())
                            break
                    
                    lisn_lb5 = Label(nuvia_fr, text='Tell me your Destination Point', font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4')
                    lisn_lb5.place(x=30, y=190)
                    lisn_lb3.place(x=1240, y=110)
                    Nuvia_Voice.speak('Tell me your Destination Point')
                    lisn_lb3.place(x=140, y=110, width=40, height=27)
                    while True:
                        query = takeCommand()

                        if query == 'none': continue
                        else:
                            dest_point = query
                            lisn_lb4.config(text=dest_point.title())
                            break
                else:
                    with open('user_info/start_point.txt', 'w') as f:
                        f.write('')

                    with open('user_info/dest_point.txt', 'w') as f:
                        f.write('')


                    # Keyboard Entry
                    key_en2 = Entry(nuvia_fr, font=('Times Now Romans', 14, 'normal'), fg='white', bg='#203647', bd=0)
                    key_en2.place(x=160, y=350, width=285)
                    
                    def key_getter(e):
                        user_input = key_en2.get().lower()

                        if user_input == 'none' : ''
                        else: 
                            with open('user_info/start_point.txt', 'w') as f:
                                f.write(user_input)
                            

                    while True:
                        with open('user_info/start_point.txt', 'r') as f:
                            start_point = f.read()
                        
                        key_en2.bind('<Return>', key_getter)
                        if start_point == '': continue
                        else:    
                            lisn_lb4 = Label(nuvia_fr, text=start_point.title(), font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', wraplength=200)
                            lisn_lb4.place(x=400, y=157)
                            key_en2.destroy()
                            break

                    lisn_lb5.config(text='Tell me your destination point', bg='#03A9F4', justify='left')
                    lisn_lb3.place(x=1240, y=110)
                    Nuvia_Voice.speak('Tell me your Destination Point')
                    lisn_lb3.place(x=140, y=110, width=40, height=27)
                    # Keyboard Entry
                    key_en2 = Entry(nuvia_fr, font=('Times Now Romans', 14, 'normal'), fg='white', bg='#203647', bd=0)
                    key_en2.place(x=160, y=350, width=285)
                    def key_getter2(e):
                        user_input = key_en2.get().lower()

                        if user_input == 'none' : ''
                        else: 
                            with open('user_info/dest_point.txt', 'w') as f:
                                f.write(user_input)
                            

                    while True:
                        with open('user_info/dest_point.txt', 'r') as f:
                            dest_point = f.read()
                        
                        key_en2.bind('<Return>', key_getter2)
                        if dest_point == '': continue
                        else:    
                            lisn_lb4 = Label(nuvia_fr, text=dest_point.title(), font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', wraplength=200)
                            lisn_lb4.place(x=400, y=157)
                            key_en2.destroy()
                            break

                clear_screen(0)
                total_dest = opb.maps_dir(start_point, dest_point)
                if total_dest == 'none':
                    lisn_lb5 = Label(nuvia_fr,text='There are some connectivity error occurs. Please, try again later',font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', wraplength=500, justify='left')
                    lisn_lb5.place(x=30, y=190)
                    lisn_lb3.place(x=1240, y=110)
                    Nuvia_Voice.speak('There are some connectivity error occurs. Please, try again later')
                    lisn_lb3.place(x=140, y=110, width=40, height=27)
                else:
                    lisn_lb5 = Label(nuvia_fr,text=f'Total Distance from {start_point.title()} to {dest_point.title()} is {total_dest}km',font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', wraplength=500, justify='left')
                    lisn_lb5.place(x=30, y=190)
                    lisn_lb3.place(x=1240, y=110)
                    Nuvia_Voice.speak(f'Total Distance from {start_point} to {dest_point} is {total_dest}km')
                    lisn_lb3.place(x=140, y=110, width=40, height=27)

            elif text in ['table']:
                lisn_lb7 = Label(nuvia_fr, text='Maths Table', font=('Times Now Romans', 18, 'bold'), fg= '#8BC34A', bg='#081923')
                lisn_lb7.place(x=220, y=100)
                lisn_lb4 = Label(nuvia_fr, text=query.capitalize(), font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', wraplength=200)
                lisn_lb4.place(x=400, y=157)
                words = ['what', 'is', 'the', 'table', 'of', ' ' , 's']
                querywords = query.split()
                resultwords  = [word for word in querywords if word.lower() not in words]
                result = ' '.join(resultwords)

                number = int(result) 
                table = opb.maths_table(number)
                if table == 'no':
                    math_lb = Label(nuvia_fr, text=f"Sorry, {number} has no table",font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', wraplength=300)
                    math_lb.place(x=30, y=180)
                    lisn_lb3.place(x=1240, y=110)
                    Nuvia_Voice.speak(f"Sorry, {number} has no table")
                    lisn_lb3.place(x=140, y=110, width=40, height=27)
                else:
                    for i in ['[', ']']:
                        table = str(table).replace(i, '')
                    math_lb = Label(nuvia_fr, text=f"Result : {table}",font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', wraplength=300)
                    math_lb.place(x=30, y=180)
                    lisn_lb3.place(x=1240, y=110)
                    Nuvia_Voice.speak(f"Here are the table of {number}")
                    lisn_lb3.place(x=140, y=110, width=40, height=27)

            elif text in ['sin', 'cos', 'tan', 'sec', 'cosec', 'left shift', 'right shift', 'binary', 'factorial', 'log']:
                lisn_lb4 = Label(nuvia_fr, text=query.capitalize(), font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', wraplength=200)
                lisn_lb4.place(x=400, y=157)
                words = ['what', 'is', 'the', 'value', 'of', ' ' , 'sin', 'cos', 'tan', 'sec', 'cosec', 'left', 'right', 'shift', 'left shift', 'leftshift', 'rightshift', 'right shift', 'binary', 'factorial', 'log']
                querywords = query.split()
                resultwords  = [word for word in querywords if word.lower() not in words]
                result = ' '.join(resultwords).replace('log', '')

                number = int(result) 
                result = opb.maths_perform(text, number)
                math_lb = Label(nuvia_fr, text=f"Result : {result}",font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4')
                math_lb.place(x=80, y=155)
                lisn_lb3.place(x=1240, y=110)
                Nuvia_Voice.speak(f"Result is {result}")
                lisn_lb3.place(x=140, y=110, width=40, height=27)


            elif text in ['evalue']:
                lisn_lb7 = Label(nuvia_fr, text='Maths Equation', font=('Times Now Romans', 18, 'bold'), fg= '#8BC34A', bg='#081923')
                lisn_lb7.place(x=210, y=100)
                lisn_lb4 = Label(nuvia_fr, text=query.capitalize(), font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', wraplength=200)
                lisn_lb4.place(x=400, y=157)
                result = opb.maths_equation(query)
                math_lb = Label(nuvia_fr, text=f"Result : {result}",font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4')
                math_lb.place(x=80, y=155)
                lisn_lb3.place(x=1240, y=110)
                Nuvia_Voice.speak(f"Result is {result}")
                lisn_lb3.place(x=140, y=110, width=40, height=27)

            elif text in ['translate', 'translator']:
                lisn_lb7 = Label(nuvia_fr, text='Translator', font=('Times Now Romans', 18, 'bold'), fg= '#8BC34A', bg='#081923')
                lisn_lb7.place(x=220, y=100)
                lisn_lb4 = Label(nuvia_fr, text=query.capitalize(), font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', wraplength=200)
                lisn_lb4.place(x=400, y=157)
                lisn_lb5 = Label(nuvia_fr, text='What do you want to tranlate?', font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4')
                lisn_lb5.place(x=30, y=190)
                lisn_lb3.place(x=1240, y=110)
                Nuvia_Voice.speak('What do you want to translate')
                lisn_lb3.place(x=140, y=110, width=40, height=27)
                og_txt = ''
                if check != 'stop thread':
                    while True:
                        query = takeCommand()

                        if query == 'none': continue
                        else:
                            sentence = query
                            break

                    clear_screen(0)
                    og_txt = query
                    lisn_lb4 = Label(nuvia_fr, text=query.capitalize(), font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', wraplength=200)
                    lisn_lb4.place(x=400, y=157)
                    lisn_lb5 = Label(nuvia_fr, text='In which language you want to translate ?', font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4')
                    lisn_lb5.place(x=30, y=190)
                    lisn_lb3.place(x=1240, y=110)
                    Nuvia_Voice.speak('In which language you want to translate')
                    lisn_lb3.place(x=140, y=110, width=40, height=27)
                    while True:
                        query = takeCommand()

                        if query == 'none': continue
                        else:
                            clear_screen(0)
                            lang = query
                            break

                else:
                    with open('user_info/trans_sent.txt', 'w') as f:
                        f.write('')

                    with open('user_info/trans_lang.txt', 'w') as f:
                        f.write('')

                    # Keyboard Entry
                    key_en2 = Entry(nuvia_fr, font=('Times Now Romans', 14, 'normal'), fg='white', bg='#203647', bd=0)
                    key_en2.place(x=160, y=350, width=285)
                    def key_getter2(e):
                        user_input = key_en2.get().lower()

                        if user_input == 'none' : ''
                        else: 
                            with open('user_info/trans_sent.txt', 'w') as f:
                                f.write(user_input)

                    while True:
                        with open('user_info/trans_sent.txt', 'r') as f:
                            sentence = f.read()

                        key_en2.bind('<Return>', key_getter2)
                        if sentence == '': continue
                        else:    
                            key_en2.destroy()
                            break

                    og_txt = sentence
                    clear_screen(0)
                    lisn_lb4 = Label(nuvia_fr, text=query.capitalize(), font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', wraplength=200)
                    lisn_lb4.place(x=400, y=157)
                    lisn_lb5 = Label(nuvia_fr, text='In which language you want to translate ?', font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4')
                    lisn_lb5.place(x=30, y=190)
                    lisn_lb3.place(x=1240, y=110)
                    Nuvia_Voice.speak('In which language you want to translate')
                    lisn_lb3.place(x=140, y=110, width=40, height=27)
                    # Keyboard Entry
                    key_en2 = Entry(nuvia_fr, font=('Times Now Romans', 14, 'normal'), fg='white', bg='#203647', bd=0)
                    key_en2.place(x=160, y=350, width=285)
                    def key_getter2(e):
                        user_input = key_en2.get().lower()

                        if user_input == 'none':  ''
                        else: 
                            with open('user_info/trans_lang.txt', 'w') as f:
                                f.write(user_input)
                            

                    while True:
                        with open('user_info/trans_lang.txt', 'r') as f:
                            lang = f.read()
                        
                        key_en2.bind('<Return>', key_getter2)
                        if lang == '': continue
                        else:    
                            key_en2.destroy()
                            break

                clear_screen(0)
                result = opb.nuv_translator(sentence, lang)
                lisn_lb5 = Label(nuvia_fr, text=f'Original Text : {og_txt.capitalize()}\nTranslated Text : {result.text}', font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', justify='left', wraplength=400)
                lisn_lb5.place(x=30, y=190)
                lisn_lb3.place(x=1240, y=110)
                Nuvia_Voice.speak('Here is translated text')
                lisn_lb3.place(x=140, y=110, width=40, height=27)

            elif text in ['meaning', 'means', 'dictionary', 'definition']:
                lisn_lb5 = Label(nuvia_fr, text='Dictionary', font=('Times Now Romans', 25, 'bold'), fg= '#8BC34A', bg='#081923')
                lisn_lb5.place(x=230, y=100)
                if text == 'dictionary':
                    lisn_lb5 = Label(nuvia_fr, text='Tell me a word or sentence', font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4')
                    lisn_lb5.place(x=30, y=190)
                    lisn_lb3.place(x=1240, y=110)
                    Nuvia_Voice.speak('Tell me a word or sentence')
                    lisn_lb3.place(x=140, y=110, width=40, height=27)
                    if check != 'stop thread':
                        while True:
                            query = takeCommand()

                            if query == 'none': continue
                            else:
                                break

                    else:
                        with open('user_info/dict_sent.txt', 'w') as f:
                            f.write('')
                        # Keyboard Entry
                        key_en2 = Entry(nuvia_fr, font=('Times Now Romans', 14, 'normal'), fg='white', bg='#203647', bd=0)
                        key_en2.place(x=160, y=350, width=285)
                        def key_getter2(e):
                            user_input = key_en2.get().lower()

                            if user_input == 'none':  ''
                            else: 
                                with open('user_info/dict_sent.txt', 'w') as f:
                                    f.write(user_input)
                                
                        while True:
                            with open('user_info/dict_sent.txt', 'r') as f:
                                query = f.read()
                            
                            key_en2.bind('<Return>', key_getter2)
                            if query == '': continue
                            else:    
                                key_en2.destroy()
                                break

                    result = opb.nuv_dictionary(query)
                    dict_lb = Label(nuvia_fr, text=result, font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', justify='left', wraplength=500)
                    dict_lb.place(x=80, y=155)
                    lisn_lb3.place(x=1240, y=110)
                    Nuvia_Voice.speak(result)
                    lisn_lb3.place(x=140, y=110, width=40, height=27)

                else:
                    words = ['what', 'is', 'the', 'meaning', 'means', 'of', 's', ' ']
                    querywords = query.split()
                    resultwords  = [word for word in querywords if word.lower() not in words]
                    result = ' '.join(resultwords)

                    result = opb.nuv_dictionary(result)
                    dict_lb = Label(nuvia_fr, text=result, font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', justify='left', wraplength=500)
                    dict_lb.place(x=80, y=155)
                    if check != 'stop thread':
                        lisn_lb2.place(x=220, y=345, width=153)
                    lisn_lb3.place(x=1240, y=110)
                    Nuvia_Voice.speak(result)
                    lisn_lb3.place(x=140, y=110, width=40, height=27)

            elif text in ['wiki', 'wikipedia', 'who']:
                stopwords = ['wiki', 'who', 'is', 'a', 'wikipedia', 'Wikipedia']
                querywords = query.split()

                resultwords  = [word for word in querywords if word.lower() not in stopwords]
                result = ' '.join(resultwords)

                lisn_lb5 = Label(nuvia_fr, text='Searching...', font=('Times Now Romans', 25, 'bold'), fg= '#8BC34A', bg='#081923')
                lisn_lb5.place(x=200, y=100)
                summary_result, wiki_title = opb.nuv_wiki(result)
                if summary_result != 'none':
                    global wiki_image

                    # Delete files and folder 
                    def del_fun():
                        os.remove(f'simple_images/{query_1}/{result}_1.jpeg')
                        os.rmdir(f'simple_images/{query_1}')

                    opb.image_search(result)
                    query_1 = result.replace(' ', '_')

                    w, h = 110, 160
                    wiki_image = ImageTk.PhotoImage(Image.open(f"simple_images/{query_1}/{result}_1.jpeg").resize((w,h), Image.Resampling.LANCZOS))
                    photo_lb = Label(nuvia_fr, image=wiki_image, bg='#081923')
                    photo_lb.place(x=30, y=155)
                    summary_length = len(summary_result)

                    lisn_lb5.destroy()
                    lisn_lb5 = Label(nuvia_fr, text=wiki_title, font=('Times Now Romans', 20, 'bold'), fg= '#8BC34A', bg='#081923')
                    lisn_lb5.place(x=200, y=100)
                    if summary_length > 465:
                        scroll_y = Scrollbar(nuvia_fr)
                        tt = Text(nuvia_fr, height = 8, width = 52, bd=0, state='disabled', fg= 'white', bg='#03A9F4', font=('Times Now Romans', 11, 'bold'), yscrollcommand=scroll_y.set)
                        tt.place(x=153, y=170)
                        scroll_y.place(x=573, y=170, height=146)
                        scroll_y.config(command=tt.yview)
                        tt.config(state='normal')
                        tt.insert('end', summary_result)
                        tt.config(state='disabled')
                    else:                    
                        tt = Text(nuvia_fr, height = 8, width = 52, bd=0, state='disabled', fg= 'white', bg='#03A9F4', font=('Times Now Romans', 11, 'bold'))
                        tt.place(x=153, y=170)
                        tt.config(state='normal')
                        tt.insert('end', summary_result)
                        tt.config(state='disabled')
                        
                    if check != 'stop thread':
                        lisn_lb2.place(x=220, y=345, width=153)
                    
                    lisn_lb3.place(x=1240, y=110)
                    Nuvia_Voice.speak(summary_result)
                    lisn_lb3.place(x=140, y=110, width=40, height=27)
                    thr.Thread(target=del_fun).start()

                else:
                    lisn_lb3.place(x=1240, y=110)
                    Nuvia_Voice.speak('Sorry, this page does not exists')
                    lisn_lb3.place(x=140, y=110, width=40, height=27)


            elif text in ['image', 'images']:
                global image1, image2, image3
                
                # Delete files and folder 
                def del_fun():
                    for i in range(1, 4):
                        os.remove(f'simple_images/{query_1}/{result}_{i}.jpeg')
                    os.rmdir(f'simple_images/{query_1}')

                stopwords = ['show', 'me', 'image', 'images', 'search', 'of' ,' ']
                querywords = query.split()
                resultwords  = [word for word in querywords if word.lower() not in stopwords]
                result = ' '.join(resultwords)
                
                lisn_lb5 = Label(nuvia_fr, text='Searching...', font=('Times Now Romans', 25, 'bold'), fg= '#8BC34A', bg='#081923')
                lisn_lb5.place(x=200, y=100)
                opb.image_search(result, cog='yes')
                lisn_lb5.destroy()
                query_1 = result.replace(' ', '_')

                w, h = 150, 150
                image1 = ImageTk.PhotoImage(Image.open(f"simple_images/{query_1}/{result}_1.jpeg").resize((w,h), Image.Resampling.LANCZOS))
                image2 = ImageTk.PhotoImage(Image.open(f"simple_images/{query_1}/{result}_2.jpeg").resize((w,h), Image.Resampling.LANCZOS))
                image3 = ImageTk.PhotoImage(Image.open(f"simple_images/{query_1}/{result}_3.jpeg").resize((w,h), Image.Resampling.LANCZOS))
                
                Label(nuvia_fr, image=image1).place(x=30, y=155)
                Label(nuvia_fr, image=image2).place(x=210, y=155)
                Label(nuvia_fr, image=image3).place(x=390, y=155)
                thr.Thread(target=del_fun).start()


            elif text in ['covid cases']:
                world, confrom, recover, deaths = opb.covid_tracker()
                
                # Cases labels
                lisn_lb5 = Label(nuvia_fr, text='Covid Cases', font=('Times Now Romans', 20, 'bold'), fg= '#8BC34A', bg='#081923')
                lisn_lb5.place(x=200, y=100)
                lisn_lb5 = Label(nuvia_fr, text=f'World Cases : {world} \nConfrom Cases : {confrom}\nRecovered : {recover}\nDeaths : {deaths}', font=('Times Now Romans', 12, 'bold'), fg= 'white', bg='#03A9F4', justify='left')
                lisn_lb5.place(x=50, y=165)
                if check != 'stop thread':
                    lisn_lb2.place(x=220, y=345, width=153)
                lisn_lb3.place(x=1240, y=110)
                Nuvia_Voice.speak('Here are the covid cases all over world')
                lisn_lb3.place(x=140, y=110, width=40, height=27)


            elif text in ['covid symptoms']:
                symptoms1 = '1. Fever or chills \n2. Cough \n3. Shortness of breath or difficulty breathing\n4. Fatigue \n5. Muscle or body aches \n6. Headache \n7. New loss of taste or smell \n8. Sore throat'
                lisn_lb5 = Label(nuvia_fr, text='Covid Symptoms', font=('Times Now Romans', 20, 'bold'), fg= '#8BC34A', bg='#081923')
                lisn_lb5.place(x=200, y=100)
                lisn_lb5 = Label(nuvia_fr, text=symptoms1, font=('Times Now Romans', 12, 'bold'), fg= 'white', bg='#03A9F4', justify='left')
                lisn_lb5.place(x=50, y=165)
                if check != 'stop thread':
                    lisn_lb2.place(x=220, y=345, width=153)
                lisn_lb3.place(x=1240, y=110)
                Nuvia_Voice.speak('Here are some covid symptoms')
                lisn_lb3.place(x=140, y=110, width=40, height=27)


            elif text in ['covid prevention']:
                preventions = '''1. Get Vaccinated \n2. Wear a mask \n3. Stay 6 feet away from others \n4. Avoid crowds and poorly ventilated spaces \n5. Wash your hands often \n6. Cover coughs and sneezes \n7. Clean and disinfect'''
                lisn_lb5 = Label(nuvia_fr, text='Covid Preventions', font=('Times Now Romans', 20, 'bold'), fg= '#8BC34A', bg='#081923')
                lisn_lb5.place(x=200, y=100)
                lisn_lb5 = Label(nuvia_fr, text=preventions, font=('Times Now Romans', 13, 'bold'), fg= 'white', bg='#03A9F4', justify='left')
                lisn_lb5.place(x=50, y=160)
                if check != 'stop thread':
                    lisn_lb2.place(x=220, y=345, width=153)
                lisn_lb3.place(x=1240, y=110)
                Nuvia_Voice.speak('Here are some covid preventions')
                lisn_lb3.place(x=140, y=110, width=40, height=27)

            elif text in ['weather', 'weather info']:
                with open('user_info/user_city.txt', 'r') as f:
                    city = f.read()
                
                lisn_lb5 = Label(nuvia_fr, text='Weather', font=('Times Now Romans', 23, 'bold'), fg= '#8BC34A', bg='#081923')
                lisn_lb5.place(x=235, y=100)
                temp_bg= '#3CADFF'
                hr, min, sec, noon, date, month, year, day = Clock.current_time()
                thr.Thread(target=weatv.get_weather).start
                with open('user_info/weather_data.txt', 'r') as f:
                    data = f.read().splitlines()
                description = data[1].lower()
                des_len = len(description)
                mytime = time.localtime()
                
                template_lb = Label(nuvia_fr,  image=weather_temp, bg='#081923')
                template_lb.place(x=50, y=155)
                city_lb = Label(nuvia_fr,  text=city, bg=temp_bg, font=('Comic Sans MS', 18, 'bold'), fg='white')
                city_lb.place(x=60, y=165)
                day_lb = Label(nuvia_fr,  text=day, bg=temp_bg, font=('Arial', 12, 'normal'), fg='white')
                day_lb.place(x=60, y=210)
                date_lb = Label(nuvia_fr,  text=f'{date}/ {month}/ {year}', bg=temp_bg, font=('Arial', 10, 'normal'), fg='white')
                date_lb.place(x=60, y=237)
                temperature_lb = Label(nuvia_fr,  text=f"{data[0]}°", bg=temp_bg, font=('Arial', 40, 'normal'), fg='white')
                temperature_lb.place(x=245, y=205)
                humidity_lb = Label(nuvia_fr, image=humidity_img, bg=temp_bg)
                humidity_lb.place(x=60, y=259)
                text_lb = Label(nuvia_fr, text=data[2], bg=temp_bg, font=('Arial', 12, 'normal'), fg='white')
                text_lb.place(x=93, y=265)
                
                disp_img = Label(nuvia_fr,  bg=temp_bg)
                disp_img.place(x=160, y=205)
                des_lb = Label(nuvia_fr,  text=description.title(), bg=temp_bg, font=('Arial', 12, 'bold'), fg='white')
                if des_len >= 15 and des_len < 20:
                    des_lb.place(x=135, y=285)
                elif des_len >= 20:
                    des_lb.place(x=105, y=285)
                else:    
                    des_lb.place(x=165, y=285)
                

                # Show weather images
                if description in ['thunderstorm with light rain','thunderstorm with rain','thunderstorm with heavy rain','light thunderstorm','thunderstorm','heavy thunderstorm','ragged thunderstorm','thunderstorm with light drizzle','thunderstorm with drizzle','thunderstorm with heavy drizzle', 'scattered thunderstorms', 'chance of storm', 'storm', 'chance of tstorm']:
                    disp_img.config(image=thunder_storm_big)

                elif description in ['light intensity drizzle','drizzle','heavy intensity drizzle','light intensity drizzle rain','drizzle rain','heavy intensity drizzle rain','shower rain and drizzle','heavy shower rain and drizzle','shower drizzle','light intensity shower rain','shower rain','heavy intensity shower rain','ragged shower rain', 'showers', 'hail']:
                    disp_img.config(image=shower_rain_big)

                elif description in ['light rain','moderate rain','heavy intensity rain','very heavy rain','extreme rain', 'scattered showers', 'freezing drizzle', 'chance of rain', 'rain']:
                    if mytime.tm_hour < 6 or mytime.tm_hour > 18:
                        disp_img.config(image=rain_night_big)
                    else:
                        disp_img.config(image=rain_day_big)

                elif description in ['freezing rain','light snow','snow','heavy snow','sleet','light shower sleet','shower sleet','light rain and snow','rain and snow','light shower snow','heavy shower snow', 'rain and snow', 'chance of snow', 'icy', 'sleet', 'flurries', 'snow showers']:
                    disp_img.config(image=snow_big)

                elif description in ['mist','smoke','haze','sand/ dust whirls','fog','sand','dust','volcanic ash','squalls','tornado']:
                    disp_img.config(image=mist_big)

                elif (description in ['clear sky', 'sunny', 'clear', 'mostly sunny']):
                    if mytime.tm_hour < 6 or mytime.tm_hour > 18:
                        disp_img.config(image=clear_night_big)
                    else:
                        disp_img.config(image=clear_day_big)

                elif (description in ['few clouds', 'partly sunny', 'partly cloudy']):
                    if mytime.tm_hour < 6 or mytime.tm_hour > 18:
                        disp_img.config(image=few_night_big)
                    else:
                        disp_img.config(image=few_day_big)
                
                elif (description in ['scattered clouds', 'fair']):
                    disp_img.config(image=scattered_clouds_big)
                
                else:
                    disp_img.config(image=broken_clouds_big)

                if check != 'stop thread':
                    lisn_lb2.place(x=220, y=345, width=153)
                lisn_lb3.place(x=1240, y=110)
                Nuvia_Voice.speak(f'today temperature is {data[0]}° with {data[1]} and humidity is {data[2]}')
                lisn_lb3.place(x=140, y=110, width=40, height=27)


            elif text in ['tab']:
                query = query.replace('tab', '')
                query = query.replace(' ', '')
                opb.auto_tabs(query)

            elif text in ['window', 'screenshot']:
                word = ['windows', 'take', 'window', ' ']
                for i in word:
                    query = query.replace(i, '')

                opb.auto_win(query)

            elif text in ['save', 'enter', 'delete', 'select', 'type']:
                if text == 'type':
                    query = query.replace('type', '')
                    opb.auto_keys(query=text, text=query)
                
                else:
                    opb.auto_keys(text)

            elif text in sites:
                opb.open_site(text)
                opb.play_track()

            elif text in ['volume up', 'inc']:
                opb.vol_up()

            elif text in ['volume down', 'dec']:
                opb.vol_down()

            elif text in ['screenpet', 'pet']:
                time.sleep(1)
                os.startfile('screenpet.pyw')


            elif text in ['egg catcher', 'egg catcher game']:
                time.sleep(1)
                os.startfile('egg_catcher.pyw')

            elif text in ['restart']:
                Nuvia_Voice.speak('Restarting the system')
                opb.restart_pc()

            elif text in ['shutdown']:
                Nuvia_Voice.speak('shuting down the system. Goodbye')
                opb.shutdown_pc()


            # Clear Screen txt file
            with open('user_info/screen_wipe.txt', 'w') as f:
                f.write('not clear')

            with open('user_info/thread_manage.txt', 'r') as f:
                check = f.read()

            with open('user_info/thread_gui.txt', 'r') as f:
                gui = f.read()


        # Nuvia Settings
        def nuv_settings():
            global nuv_voice_box, voice_rate_box, volume_bar
            setting_lb = Frame(win, bg='#081923')
            setting_lb.pack(fill=BOTH, expand=True)

            def apply_set():
                with open('user_info/editor.txt', 'r') as f:
                    editor = f.read()

                new_name = temp_name.get()

                if new_name == '' and editor == 'ON':
                    messagebox.showerror('Error', 'Please Enter a Username!')

                elif (len(new_name) < 3 or len(new_name) > 6) and editor == 'ON':
                    messagebox.showerror('Error', 'Username length should be between 3 to 6 characters')

                else:
                    if new_name == ' ' or new_name == '':
                        with open('user_info/user_name.txt', 'w') as f:
                            f.write(owner_name)
                    else:
                        with open('user_info/user_name.txt', 'w') as f:
                            f.write(new_name)
                        

                    with open('user_info/nuvia_vocal.txt', 'w') as f:
                        f.write(nuv_voice_box.get())

                    with open('user_info/vocal_rate.txt', 'w') as f:
                        f.write(voice_rate_box.get())

                    with open('user_info/vocal_volume.txt', 'w') as f:
                        f.write(str(volume_bar.get()))

                    with open('user_info/thread_manage.txt', 'w') as f:
                        f.write('none')

                    with open('user_info/editor.txt', 'w') as f:
                        f.write('OFF')
                    # Destroy frame and call nuvia
                    setting_lb.destroy()
                    nuvia()


            def onEnter(event):
                set_bt1.config(image=camera_img)

            def onLeave(event):
                if user_pfp == 'male_1':
                    set_bt1.config(image=Male_pp1)

                elif user_pfp == 'male_2':
                    set_bt1.config(image=Male_pp2)

                elif user_pfp == 'male_3':
                    set_bt1.config(image=Male_pp3)

                elif user_pfp == 'male_4':
                    set_bt1.config(image=Male_pp4)

                elif user_pfp == 'female_1':
                    set_bt1.config(image=Female_pp5)

                elif user_pfp == 'female_2':
                    nuv_user.config(image=Female_pp6)

                elif user_pfp == 'female_3':
                    set_bt1.config(image=Female_pp7)

                else:
                    set_bt1.config(image=Female_pp8)

            # Entry Variable
            temp_name = StringVar()

            # Edit User Name
            def edit_name():
                with open('user_info/editor.txt', 'w') as f:
                    f.write('ON')

                set_lb2.destroy()
                set_bt2.destroy()

                name_en = Entry(setting_lb, text='day', font=('Times Now Romans', 14, 'normal'), textvariable=temp_name)
                name_en.insert(0,owner_name)
                name_en.place(x=240,y=180, width=100, height=20)


            # User Pfp changing
            def change_pfp():

                # Label
                pfp_lb1 = Label(setting_lb, text='pfp', bg='#081923')
                pfp_lb1.place(x=250,y=70)

                if user_pfp == 'male_1':
                    pfp_lb1.config(image=Male_pp1)

                elif user_pfp == 'male_2':
                    pfp_lb1.config(image=Male_pp2)

                elif user_pfp == 'male_3':
                    pfp_lb1.config(image=Male_pp3)

                elif user_pfp == 'male_4':
                    pfp_lb1.config(image=Male_pp4)

                elif user_pfp == 'female_1':
                    pfp_lb1.config(image=Female_pp5)

                elif user_pfp == 'female_2':
                    nuv_user.config(image=Female_pp6)

                elif user_pfp == 'female_3':
                    pfp_lb1.config(image=Female_pp7)

                else:
                    pfp_lb1.config(image=Female_pp8)

                
                def pp_lb1():
                    pfp_lb1.config(image=Male_pp1)

                    # File Contain Profile pic info
                    with open('user_info/user_pp.txt', 'w') as f:
                        f.write('male_1')

                def pp_lb2():
                    pfp_lb1.config(image=Male_pp2)

                    # File Contain Profile pic info
                    with open('user_info/user_pp.txt', 'w') as f:
                        f.write('male_2')

                def pp_lb3():
                    pfp_lb1.config(image=Male_pp3)

                    # File Contain Profile pic info
                    with open('user_info/user_pp.txt', 'w') as f:
                        f.write('male_3')

                def pp_lb4():
                    pfp_lb1.config(image=Male_pp4)

                    # File Contain Profile pic info
                    with open('user_info/user_pp.txt', 'w') as f:
                        f.write('male_4')

                def pp_lb5():
                    pfp_lb1.config(image=Female_pp5)

                    # File Contain Profile pic info
                    with open('user_info/user_pp.txt', 'w') as f:
                        f.write('female_1')

                def pp_lb6():
                    pfp_lb1.config(image=Female_pp6)

                    # File Contain Profile pic info
                    with open('user_info/user_pp.txt', 'w') as f:
                        f.write('female_2')

                def pp_lb7():
                    pfp_lb1.config(image=Female_pp7)

                    # File Contain Profile pic info
                    with open('user_info/user_pp.txt', 'w') as f:
                        f.write('female_4')

                def pp_lb8():
                    pfp_lb1.config(image=Female_pp8)

                    # File Contain Profile pic info
                    with open('user_info/user_pp.txt', 'w') as f:
                        f.write('female_3')


                # Buttons
                pfp_bt1 = Button(setting_lb, image=male_pfp1, bg='#081923', activebackground='#081923', bd=0,command=pp_lb1)
                pfp_bt1.place(x=20,y=70)

                pfp_bt2 = Button(setting_lb, image=male_pfp2, bg='#081923', activebackground='#081923', bd=0,command=pp_lb2)
                pfp_bt2.place(x=120,y=70)

                pfp_bt3 = Button(setting_lb, image=male_pfp3, bg='#081923', activebackground='#081923', bd=0,command=pp_lb3)
                pfp_bt3.place(x=20,y=140)

                pfp_bt4 = Button(setting_lb, image=male_pfp4, bg='#081923', activebackground='#081923', bd=0,command=pp_lb4)
                pfp_bt4.place(x=120,y=140)

                pfp_bt5 = Button(setting_lb, image=female_pfp1, bg='#081923', activebackground='#081923', bd=0,command=pp_lb5)
                pfp_bt5.place(x=420,y=70)

                pfp_bt6 = Button(setting_lb, image=female_pfp2, bg='#081923', activebackground='#081923', bd=0,command=pp_lb6)
                pfp_bt6.place(x=515,y=70)

                pfp_bt7 = Button(setting_lb, image=female_pfp3, bg='#081923', activebackground='#081923', bd=0,command=pp_lb8)
                pfp_bt7.place(x=420,y=140)

                pfp_bt8 = Button(setting_lb, image=female_pfp4, bg='#081923', activebackground='#081923', bd=0,command=pp_lb7)
                pfp_bt8.place(x=515,y=140)


            with open('user_info/destory_label.txt') as f:
                dest = f.read()

            if dest == 'not destory':
                # Destory all labels and buttons
                nuvia_fr.destroy()


                with open('user_info/thread_manage.txt', 'w') as f:
                    f.write('settings')

                # Write that it is destory
                with open('user_info/destory_label.txt', 'w') as f:
                    f.write('destory')

            # Labels
            lisn_lb = Label(setting_lb, bg='#081923')
            lisn_lb.place(x=220, y=345, width=158, height=40)
            
            set_lb1 = Label(setting_lb, text='Settings', bg='#081923', font=('Garamond', 30, 'bold italic'), fg='#18FFFF')
            set_lb1.place(x=230,y=5)

            set_lb3 = Label(setting_lb, bg='#081923')
            set_lb3.place(x=235,y=180, width=120)

            set_lb4 = Label(setting_lb, bg='#081923')
            set_lb4.place(x=20,y=70, width=165, height=130)

            set_lb5 = Label(setting_lb, bg='#081923')
            set_lb5.place(x=420,y=70, width=165, height=130)

            with open('user_info/user_name.txt') as f:
                owner_name = f.read()
            name_len2 = len(owner_name)

            set_lb2 = Label(setting_lb, text=owner_name, bg='#081923', font=('Perpetua', 25, 'normal'), fg='#FF5722')
            
            # Check name length
            if name_len2 == 3:
                set_lb2.place(x=268, y=170)    

            elif name_len2 == 4:
                set_lb2.place(x=265, y=170)    

            elif name_len2 == 5:
                set_lb2.place(x=263, y=170) 

            else:
                set_lb2.place(x=260, y=170)


            with open('user_info/user_pp.txt') as f:
                user_pfp = f.read()

            # Buttons
            set_bt1 = Button(setting_lb, text='image', bg='#081923', activebackground='#081923', bd=0, command=change_pfp)
            set_bt1.place(x=250,y=70)

            set_bt2 = Button(setting_lb, image=edit_img, bg='#081923', activebackground='#081923', bd=0, command=edit_name)
            set_bt2.place(x=362,y=175)


            # Check Cursor Position
            set_bt1.bind('<Enter>',  onEnter)
            set_bt1.bind('<Leave>',  onLeave)

            if user_pfp == 'male_1':
                set_bt1.config(image=Male_pp1)

            elif user_pfp == 'male_2':
                set_bt1.config(image=Male_pp2)

            elif user_pfp == 'male_3':
                set_bt1.config(image=Male_pp3)

            elif user_pfp == 'male_4':
                set_bt1.config(image=Male_pp4)

            elif user_pfp == 'female_1':
                set_bt1.config(image=Female_pp5)

            elif user_pfp == 'female_2':
                nuv_user.config(image=Female_pp6)

            elif user_pfp == 'female_3':
                set_bt1.config(image=Female_pp7)

            else:
                set_bt1.config(image=Female_pp8)

            # Other Settings
            bar3 = Label(setting_lb,  bg='#E040FB')
            bar3.place(x=0, y=210, width=150, height=5)

            bar4 = Label(setting_lb,  bg='#E040FB')
            bar4.place(x=449, y=210, width=150, height=5)

            # Read settings files
            with open('user_info/nuvia_vocal.txt', 'r') as f:
                read_vocal = f.read()

            with open('user_info/vocal_rate.txt', 'r') as f:
                read_rate = f.read()

            with open('user_info/vocal_volume.txt', 'r') as f:
                read_vol = f.read()

            # Nuvia Voice
            if read_vocal == 'Female':
                read_vocal = 0
            else:
                read_vocal = 1

            # Voice Rate
            if read_rate == 'Very Low':
                read_rate = 0
            elif read_rate == 'Low':
                read_rate = 1
            elif read_rate == 'Normal':
                read_rate = 2
            elif read_rate == 'Fast':
                read_rate = 3
            else:
                read_rate = 4

            nuv_voicelb = Label(setting_lb, text='Nuvia Voice',bg='#081923', fg='white', font=('Lucida Sans Unicode', 15, 'normal'))
            nuv_voicelb.place(x=10, y=230)

            nuv_voice_box = ttk.Combobox(setting_lb, width=15, state='readonly')
            nuv_voice_box['values'] = ('Female', 'Male')
            nuv_voice_box.place(x=150, y=235)
            nuv_voice_box.current(read_vocal)
            nuv_voice_box.focus()

            voice_ratelb = Label(setting_lb, text='Voice Rate',bg='#081923', fg='white', font=('Lucida Sans Unicode', 15, 'normal'))
            voice_ratelb.place(x=10, y=300)

            voice_rate_box = ttk.Combobox(setting_lb, width=15, state='readonly')
            voice_rate_box['values'] = ('Very Low', 'Low', 'Normal', 'Fast', 'Very Fast')
            voice_rate_box.place(x=150, y=305)
            voice_rate_box.current(read_rate)
            voice_rate_box.focus()

            volumelb = Label(setting_lb, text='Volume',bg='#081923', fg='white', font=('Lucida Sans Unicode', 15, 'normal'))
            volumelb.place(x=355, y=230)

            volume_bar = Scale(setting_lb, from_=0, to=100, orient=HORIZONTAL, bg='#081923', fg='white', sliderlength=30, length=126, width=13, highlightbackground='#081923')
            volume_bar.place(x=450, y=217)
            volume_bar.set(int(read_vol))


            apply_bt = Button(setting_lb, image=apply_img, bd=0, bg='#081923', activebackground='#081923', command=apply_set)
            apply_bt.place(x=250, y=350)


        with open('user_info/destory_label.txt', 'w') as f:
            f.write('not destory')

        # Colors for Days
        left_col = '#FFEA00'
        right_col = '#D500F9'
        mid_col = '#FF3D00'

        # UI Label
        nuv_ui = Label(nuvia_fr, bg='#F5F5F5')
        nuv_ui.place(x=0, y=330, width=600, height=80)

        nuv_act = Label(nuvia_fr, image=act_lb_img, bg='#F5F5F5')
        nuv_act.place(x=200, y=330)

        nuv_logo = Label(nuvia_fr, image=nuvia_img, bg=chat_bg)
        nuv_logo.place(x=10, y=110)

        nuv_name = Label(nuvia_fr, text='Nuvia', fg='#00BCD4',font=(
        'Times Now Romans', 15, 'bold'), bg=chat_bg)
        nuv_name.place(x=65, y=110)

        # Read user name
        with open('user_info/user_name.txt') as f:
            user_name = f.read() 

        name_len = len(user_name)
        user_name2 = user_name.title()  # capitalized first letter  

        nuv_user_name = Label(nuvia_fr, text=user_name2, fg='#00BCD4',font=('Times Now Romans', 15, 'bold'), bg=chat_bg)

        if name_len == 3:
            nuv_user_name.place(x=483, y=110)    

        elif name_len == 4:
            nuv_user_name.place(x=480, y=110)    

        elif name_len == 5:
            nuv_user_name.place(x=473, y=110) 

        else:
            nuv_user_name.place(x=466, y=110)


        nuv_bar1 = Label(nuvia_fr, bg='red')
        nuv_bar1.place(x=0, y=100, width=130, height=3)
        
        nuv_bar2 = Label(nuvia_fr, bg='red')
        nuv_bar2.place(x=470, y=100, width=130, height=3)


        nuv_user = Label(nuvia_fr, bg=chat_bg)
        nuv_user.place(x=540, y=110)

        # Read pfp 
        with open('user_info/user_pp.txt') as f:
            user_pfp = f.read()

        if user_pfp == 'male_1':
            nuv_user.config(image=user_log1)

        elif user_pfp == 'male_2':
            nuv_user.config(image=user_log2)

        elif user_pfp == 'male_3':
            nuv_user.config(image=user_log3)

        elif user_pfp == 'male_4':
            nuv_user.config(image=user_log4)

        elif user_pfp == 'female_1':
            nuv_user.config(image=user_log5)

        elif user_pfp == 'female_2':
            nuv_user.config(image=user_log6)

        elif user_pfp == 'female_3':
            nuv_user.config(image=user_log7)

        else:
            nuv_user.config(image=user_log8)

        # Buttons
        nuv_b1 = Button(nuvia_fr, image=set_img, bd=0, bg='#F5F5F5', activebackground='#F5F5F5', command=nuv_settings)
        nuv_b1.place(x=530, y=340)

        # Keyboard, Mic
        nuv_b2 = Button(nuvia_fr, image=key_img, bd=0, bg='#F5F5F5', activebackground='#F5F5F5', command=spm_key)
        nuv_b3 = Button(nuvia_fr, image=mic_img, bd=0, bg='#F5F5F5', activebackground='#F5F5F5', command=key_spm)
        
        # Label for hr, min and sec
        nuv_hr = Label(nuvia_fr, text='12', font=(
        'Garamond', 27, 'italic'), bg=chat_bg, fg='#D500F9')
        nuv_hr.place(x=200, y=5)
        
        nuv_min = Label(nuvia_fr, text='12', font=(
        'Garamond', 27, 'italic'), bg=chat_bg, fg='#D500F9')
        nuv_min.place(x=250, y=5)

        nuv_sec = Label(nuvia_fr, text='12', font=(
        'Garamond', 27, 'italic'), bg=chat_bg, fg='#FFEA00')
        nuv_sec.place(x=300, y=5)

        nuv_noon = Label(nuvia_fr, text='12', font=(
        'Garamond', 27, 'italic'), bg=chat_bg, fg='#FFEA00')
        nuv_noon.place(x=350, y=5)

        nuv_mon = Label(nuvia_fr, text='Mon', font=(
        'Rockwell', 12, 'normal'), bg=chat_bg, fg='#424242')
        nuv_mon.place(x=160, y=50)

        nuv_tue = Label(nuvia_fr, text='Tue', font=(
        'Rockwell', 12, 'normal'), bg=chat_bg, fg='#424242')
        nuv_tue.place(x=205, y=50)
        
        nuv_wed = Label(nuvia_fr, text='Wed', font=(
        'Rockwell', 12, 'normal'), bg=chat_bg, fg='#424242')
        nuv_wed.place(x=245, y=50)

        nuv_thu = Label(nuvia_fr, text='Thu', font=(
        'Rockwell', 12, 'normal'), bg=chat_bg, fg='#424242')
        nuv_thu.place(x=293, y=50)

        nuv_fri = Label(nuvia_fr, text='Fri', font=(
        'Rockwell', 12, 'normal'), bg=chat_bg, fg='#424242')
        nuv_fri.place(x=335, y=50)

        nuv_sat = Label(nuvia_fr, text='Sat', font=(
        'Rockwell', 12, 'normal'), bg=chat_bg, fg='#424242')
        nuv_sat.place(x=370, y=50)

        nuv_sun = Label(nuvia_fr, text='Sun', font=(
        'Rockwell', 12, 'normal'), bg=chat_bg, fg='#424242')
        nuv_sun.place(x=408, y=50)

        nuv_date = Label(nuvia_fr, text='date', font=(
        'Garamond', 18, 'normal'), bg=chat_bg, fg='#00E676')
        nuv_date.place(x=480, y=50)

        nuv_temp = Label(nuvia_fr, text='Na', font=(
        'Garamond', 10, 'normal'), bg=chat_bg, fg='white')
        nuv_temp.place(x=60, y=50)

        nuv_deg = Label(nuvia_fr, text='℃', font=(
        'Garamond', 18, 'normal'), bg=chat_bg, fg='white')
        nuv_deg.place(x=85, y=50)

        weather_images = Label(nuvia_fr, image=clear_day, bg=chat_bg)
        weather_images.place(x=0, y=38)

        # Read if there is city name or not
        with open('user_info/user_city.txt') as f:
            city_name = f.read()


        # Nuvia Weather 
        def nuvia_weather():
            
            # Check Internet Connection
            connect = opb.internet_connect()

            if connect == True:
            
                # Check if city name is written or not
                if (city_name == 'none') or (city_name == ''):
                    weatv.ip_location()  # Call to get the city name

                    # Get the temperature 
                    thr.Thread(target=weatv.get_weather).start()
                else:
                    # Get the temperature 
                    thr.Thread(target=weatv.get_weather).start()

                with open('user_info/weather_data.txt', 'r') as f:
                    data = f.read().splitlines() 

                temperature = data[0]
                description = data[1].lower()
                
                temperature = int(temperature.replace('°', ''))

                # Get the time in hours
                mytime = time.localtime()

                # Show the current temperature
                nuv_temp.config(text=temperature, font=('Garamond', 18, 'normal'))
                nuv_deg.config(text='℃', font=('Garamond', 18, 'normal'))

                # Color according to temperature
                if temperature >= 40:
                    nuv_temp.config(fg='#D50000')
                    
                elif temperature >= 30 and temperature < 40:
                    nuv_temp.config(fg='#FB8C00')

                elif temperature >= 20 and temperature < 30:
                    nuv_temp.config(fg='#FFD600')

                elif temperature >= 10 and temperature < 20:
                    nuv_temp.config(fg='#76FF03')

                else:
                    nuv_temp.config(fg='#00B0FF')

                # Show weather images
                if description in ['thunderstorm with light rain','thunderstorm with rain','thunderstorm with heavy rain','light thunderstorm','thunderstorm','heavy thunderstorm','ragged thunderstorm','thunderstorm with light drizzle','thunderstorm with drizzle','thunderstorm with heavy drizzle', 'scattered thunderstorms', 'chance of storm', 'storm', 'chance of tstorm']:
                    weather_images.config(image=thunder_storm)

                elif description in ['light intensity drizzle','drizzle','heavy intensity drizzle','light intensity drizzle rain','drizzle rain','heavy intensity drizzle rain','shower rain and drizzle','heavy shower rain and drizzle','shower drizzle','light intensity shower rain','shower rain','heavy intensity shower rain','ragged shower rain', 'showers', 'hail']:
                    weather_images.config(image=shower_rain)

                elif description in ['light rain','moderate rain','heavy intensity rain','very heavy rain','extreme rain', 'scattered showers', 'freezing drizzle', 'chance of rain', 'rain']:
                    if mytime.tm_hour < 6 or mytime.tm_hour > 18:
                        weather_images.config(image=rain_night)
                    else:
                        weather_images.config(image=rain_day)

                elif description in ['freezing rain','light snow','snow','heavy snow','sleet','light shower sleet','shower sleet','light rain and snow','rain and snow','light shower snow','heavy shower snow', 'rain and snow', 'chance of snow', 'icy', 'sleet', 'flurries', 'snow showers']:
                    weather_images.config(image=snow)

                elif description in ['mist','smoke','haze','sand/ dust whirls','fog','sand','dust','volcanic ash','squalls','tornado']:
                    weather_images.config(image=mist)

                elif (description in ['clear sky', 'sunny', 'clear', 'mostly sunny']):
                    if mytime.tm_hour < 6 or mytime.tm_hour > 18:
                        weather_images.config(image=clear_night)
                    else:
                        weather_images.config(image=clear_day)

                elif (description in ['few clouds', 'partly sunny', 'partly cloudy']):
                    if mytime.tm_hour < 6 or mytime.tm_hour > 18:
                        weather_images.config(image=few_night)
                    else:
                        weather_images.config(image=few_day)
                
                elif (description in ['scattered clouds', 'fair']):
                    weather_images.config(image=scattered_clouds)
                
                else:
                    weather_images.config(image=broken_clouds)

            else:
                weather_images.config(image=no_internet_img)
                nuv_temp.config(text='No', font=('Garamond', 13, 'normal'), fg='white')
                nuv_deg.config(text='Internet', font=('Garamond', 13, 'normal'))

                nuv_temp.after(30000, nuvia_weather)

            nuv_temp.after(900000, nuvia_weather) # Can't Return Value


        # Nuvia Clock
        def clock_time2():
            # Get the Current Time with pm or am, Day and Date
            hr, min, sec, noon, date, month, year, day = Clock.current_time()
            
            
            # Show current time, day and date on screen
            nuv_hr.config(text=hr)
            nuv_min.config(text=min)
            nuv_sec.config(text=sec)
            nuv_noon.config(text=noon)
            nuv_date.config(text=f'{date}-{month}-{year}')

            # Check current day
            if day == 'Monday':
                nuv_mon.config(fg=left_col)
                nuv_sun.config(fg='#424242')

            elif day == 'Tuesday':
                nuv_tue.config(fg=left_col)
                nuv_mon.config(fg='#424242')


            elif day == 'Wednesday':
                nuv_wed.config(fg=left_col)
                nuv_tue.config(fg='#424242')
                

            elif day == 'Thursday':
                nuv_thu.config(fg=mid_col)
                nuv_wed.config(fg='#424242')


            elif day == 'Friday':
                nuv_fri.config(fg=right_col)
                nuv_thu.config(fg='#424242')
                

            elif day == 'Saturday':
                nuv_sat.config(fg=right_col)
                nuv_fri.config(fg='#424242')
                

            else:
                nuv_sun.config(fg=right_col)
                nuv_sat.config(fg='#424242')


            nuv_hr.after(200, clock_time2)


        nuvia_weather()  # call the weather function

        clock_time2()  # call the clock function
        
        animation()  # call the animatio function
        
        # Handle Speech Threads
        thr.Thread(target=speech_medium).start()


    # Login Frame(virtual assistance)
    def login_va():

        # Both Login
        def both_log():
            
            both_log_fr.pack(fill=BOTH, expand=True)

            # Back Button
            blog_back_b = Button(both_log_fr, bd=0, image=reg_back_b, bg='#081923',
                                activebackground='#081923', command=blog_to_wel)
            blog_back_b.place(x=20, y=20)

            # Labels
            both_lb1 = Label(both_log_fr, text='Login', font=('Brush Script MT', 50, 'bold'), bg='#081923', fg='#FB8C00')
            both_lb1.place(x=230, y=5)
            
            both_lb2 = Label(both_log_fr, image=face, bg='#081923')
            both_lb2.place(x=20, y=90)

            both_lb3 = Label(both_log_fr, image=pass_img, bg='#081923')
            both_lb3.place(x=450, y=92)

            both_lb4 = Label(both_log_fr, image=secur_img, bg='#081923')
            both_lb4.place(x=200, y=92)

            both_lb5 = Label(both_log_fr, text='Login through\nface protection', bg='#081923', font=('Perpetua', 15, 'bold'), fg='#9C27B0')
            both_lb5.place(x=20, y=300)

            both_lb6 = Label(both_log_fr, text='Login through\npassword protection', bg='#081923', font=('Perpetua', 15, 'bold'), fg='#9C27B0')
            both_lb6.place(x=420, y=300)

            # Buttons
            bface_bt = Button(both_log_fr, bd=0, image=face_reco_img,
                        bg='#081923', activebackground='#081923',command=face_log)
            bface_bt.place(x=23, y=230)

            bpass_bt = Button(both_log_fr, bd=0, bg='#081923',
                        activebackground='#081923', image=pass_b_img, command=pass_login)
            bpass_bt.place(x=465, y=220)


        # Password Login
        def pass_login():

            with open('user_info/LoginAcess.txt') as f:
                dest = f.read()

            if dest == '3':
                both_log_fr.destroy()


            # Entry Variable for getting password
            pass_check = StringVar()

            # Entry Variable for getting username
            forg_name = StringVar()

            # Entry Variable for getting email
            get_mail = StringVar()

            # Entry Variable for getting otp
            get_otp = StringVar()

            # Reset Password
            def reset_pass():

                # Entry Variables for getting passwords
                get_new = StringVar()

                get_conform = StringVar()

                # Password Generator
                def re_gen():

                    # Call to generate password
                    passtv.Pass_generator()

                    # Get the generated password
                    with open('user_info/gen_pass.txt') as f:
                        password1 = f.read()

                    re_ls.delete(0)
                    re_ls.insert(END, password1)

                # Password is valid or not
                def re_check():
                    # Get the password
                    new_pass = get_new.get()
                    conform_pass = get_conform.get()


                    # Check all conditions
                    if (new_pass == conform_pass) and (new_pass != '') and (conform_pass != ''):
                        # Store the input password
                        with open("user_info/input_password.txt", 'w') as f:
                                f.write(new_pass)

                        passtv.Pass_Checker()  # call the password manager

                        # Read if it is valid or not
                        with open("user_info/password_validty.txt") as f:
                            valdo = f.read()

                        if (valdo == 'valid'):

                            re_to_nuvia()

                        else:
                            messagebox.showerror('Error', 'Invalid Password!!')          

                    elif (new_pass == '') or (conform_pass == ''):
                        messagebox.showerror('Error', 'Please, Enter your password')

                    else:
                        messagebox.showerror('Error', 'Password did not match!!')
                        

                otp_fr.destroy() # Destory previous frame

                reset_fr.pack(fill=BOTH, expand=True)

                # Labels
                re_lb1 = Label(reset_fr, text='Reset Password', bg='#081923', font=('Brush Script MT', 30, 'bold'), fg='#3F51B5')
                re_lb1.place(x=200, y=10)

                re_info = Label(reset_fr, text='Password policies mention below :',
                                bg='#081923', font=('Perpetua', 13, 'bold'), fg='red')
                re_info.place(x=5, y=90)

                re_info2 = Label(reset_fr, text=' 1.Password should not contain any space.',
                                bg='#081923', font=('Perpetua', 13, 'bold'), fg='red')
                re_info2.place(x=5, y=120)

                re_info3 = Label(reset_fr, text=' 2.Password should contain at least one digit(0-9) and\nlowercase letter(a-z) and one uppercase letter(A-Z).',
                                bg='#081923', font=('Perpetua', 13, 'bold'), fg='red')
                re_info3.place(x=5, y=150)

                re_info4 = Label(reset_fr, text=' 3.Password length should be between 8 to 15 \ncharacters.',
                                bg='#081923', font=('Perpetua', 13, 'bold'), fg='red')
                re_info4.place(x=5, y=200)

                re_info5 = Label(reset_fr, text=' 4.Password should contain at least one special \ncharacter ( @, #, %, &, !, $, etc….).',
                                bg='#081923', font=('Perpetua', 13, 'bold'), fg='red')
                re_info5.place(x=5, y=250)

                re_lb2 = Label(reset_fr, text='New Password', bg='#081923', font=('Brush Script MT', 20, 'bold'), fg='#3F51B5')
                re_lb2.place(x=420, y=90)

                re_lb3 = Label(reset_fr, text='Conform Password', bg='#081923', font=('Brush Script MT', 20, 'bold'), fg='#3F51B5')
                re_lb3.place(x=400, y=180)

                        
                re_bar = Label(reset_fr, bg='yellow')
                re_bar.place(x=0, y=305, width=600, height=3)

                re_info6 = Label(reset_fr, text='Password Genrator', bg='#081923', font=(
                    'Perpetua', 15, 'bold'), fg='#FF9800')
                re_info6.place(x=220, y=310)

                re_info7 = Label(reset_fr, text='Click on Password\nthen "ctrl+c" to copy,\n"ctrl+v" for paste.',
                                bg='#081923', font=('Perpetua', 13, 'bold'), fg='#00E5FF')
                re_info7.place(x=430, y=320)

                # Entry
                re_en1 = Entry(reset_fr, font=('Times New Roman',10, 'bold'), textvariable=get_new)
                re_en1.place(x=420, y=140, width=150)

                re_en2 = Entry(reset_fr, font=('Times New Roman',10, 'bold'), textvariable=get_conform)
                re_en2.place(x=420, y=230, width=150)

                # Password Listbox
                re_ls = Listbox(reset_fr, font=('Times New Roman', 13, 'bold'))
                re_ls.place(x=215, y=350, width=178, height=25)
                
                
                # Password Generator
                re_gen_b = Button(reset_fr, image=pass_gen_bimg, bd=0, bg='#081923',
                                    activebackground='#081923', command=re_gen)
                re_gen_b.place(x=100, y=347)

                # Submit Button
                re_sub = Button(reset_fr, text='Submit', bd=0, image=submit_bt,
                                bg='#081923', activebackground='#081923', command=re_check)
                re_sub.place(x=450, y=260)


            # Check otp
            def check_otp():

                with open('user_info/user_otp.txt', 'r') as f:
                    owner_otp = f.read()

                # Get input from user
                take_otp = get_otp.get()

                if take_otp == owner_otp:
                    with open('user_info/user_otp.txt', 'w') as f:
                        f.write('xxx-xxx-xxx')
                    reset_pass()

                elif take_otp == '':
                    messagebox.showerror('Error', 'Please, Enter your OTP.')

                else:
                    messagebox.showerror('Error', 'Incorrect OTP!!')


            # Verify otp
            def otp_verify():
                # Destory previous frame
                plog_fr.destroy()

                otp_fr.pack(fill=BOTH, expand=True)

                def generator():
                    # Declare a string variable
                    # which stores all string
                    string = '0123456789'
                    OTP_get = ""
                    length = len(string)
                    for i in range(6):
                        OTP_get += string[math.floor(random.random() * length)]

                    with open('user_info/user_otp.txt', 'w') as f:
                        f.write(OTP_get)

                    messagebox.showinfo("One-Time Password", f"{OTP_get} is your one time password for password verification")

                # Labels
                otp_lb1 = Label(otp_fr, text='OTP Verification', font=(
                    'Perpetua', 30, 'bold'), bg='#081923', fg='#76FF03')
                otp_lb1.place(x=160, y=10)

                otp_lb2 = Label(otp_fr, image=otp_img, bg='#081923')
                otp_lb2.place(x=170, y=60)


                otp_lb4 = Label(otp_fr, bg='#FF1744')
                otp_lb4.place(x=166, y=275, width=280, height=3)

                otp_lb2 = Label(otp_fr, text='OTP  :', font=(
                    'Perpetua', 25, 'bold'), bg='#081923', fg='#00B0FF')
                otp_lb2.place(x=50, y=288)

                # Entry
                ent2 = Entry(otp_fr, font=('Times New Roman', 11, 'bold'), textvariable=get_otp)
                ent2.place(x=200, y=300, width=220)

                # Button
                otp_b1 = Button(otp_fr, image=submit_bt, bg='#081923',
                                bd=0, activebackground='#081923', command=check_otp)
                otp_b1.place(x=260, y=350)

                otp_b2 = Button(otp_fr, image=generte_img, bg='#081923', bd=0, activebackground='#081923', command=generator)
                otp_b2.place(x=470, y=294)


            # Forget Password
            def forget_pass():

                # Read the User Name
                with open("user_info/user_name.txt") as f:
                    store_name = f.read()

                # Get the input name
                input_name = forg_name.get()

                if input_name == store_name:
                    otp_verify()

                elif input_name == '':
                    messagebox.showerror(
                        'Error', 'Please, Enter your user name.')

                else:
                    messagebox.showerror('Error', 'Incorrect Username!')

            # Check user password
            def user_pcheck():
                # Read password from file
                with open("user_info/user_password.txt") as f:
                    user_plog = f.read()

                # Get the user login time password
                plog_time = pass_check.get()

                # Read all account files
                with open('user_info/user_name.txt') as f:
                    acc_name = f.read()

                with open('user_info/user_pp.txt') as f:
                    acc_pp = f.read()

                with open('user_info/user_gender.txt') as f:
                    acc_gender = f.read()

                # Check all account info before login
                if (acc_name == 'none' and acc_gender == 'none' and acc_pp == 'none'):
                    messagebox.showerror('Error', 'Please make an account.')

                elif (acc_name == 'none' or acc_gender == 'none' or acc_pp == 'none'):
                    messagebox.showerror(
                        'Error', 'Please make an account properly.')

                else:
                    # Check if password are same or not
                    if user_plog == plog_time:
                        pass_to_nuvia()

                    elif plog_time == '':
                        messagebox.showerror(
                            'Error', 'Please, Enter your password.')

                    else:
                        messagebox.showerror('Error', 'Incorrect Password!')

            plog_fr.pack(fill=BOTH, expand=True)  # initializing  Frame

            # Back Button
            plog_back_b = Button(plog_fr, bd=0, image=reg_back_b, bg='#081923',
                                activebackground='#081923', command=plog_to_wel)
            plog_back_b.place(x=20, y=20)

            # Label
            plog_lb1 = Label(plog_fr, image=pass_log_img, bg='#081923')
            plog_lb1.place(x=200, y=70)

            plog_lb2 = Label(plog_fr, text='Password Login', font=(
                'Perpetua', 30, 'bold'), bg='#081923', fg='#FF9800')
            plog_lb2.place(x=170, y=20)

            plog_lb3 = Label(plog_fr, bg='yellow')
            plog_lb3.place(x=0, y=280, width=210, height=4)

            plog_lb4 = Label(plog_fr, bg='yellow')
            plog_lb4.place(x=405, y=280, width=200, height=4)

            plog_lb5 = Label(plog_fr, text='Forget Password?', bg='#081923',
                            fg='#03A9F4', font=('Brush Script MT', 20, 'bold'))
            plog_lb5.place(x=5, y=230)

            plog_lb6 = Label(plog_fr, text='Password', bg='#081923',
                            fg='#00BCD4', font=('Brush Script MT', 20, 'bold'))
            plog_lb6.place(x=460, y=230)

            plog_lb7 = Label(plog_fr, text='Username', bg='#081923',
                            fg='#00BCD4', font=('Perpetua', 15, 'bold'))
            plog_lb7.place(x=55, y=290)

            # Entry
            plog_ent = Entry(plog_fr, font=('Times New Roman',
                                            13, 'bold'), textvariable=pass_check, show='*')
            plog_ent.place(x=415, y=308, width=173)

            plog_ent2 = Entry(plog_fr, font=(
                'Times New Roman', 11, 'bold'), textvariable=forg_name)
            plog_ent2.place(x=35, y=320, width=130)

            # Submit Button
            plog_sub = Button(plog_fr, bd=0, image=pass_log_bt, bg='#081923',
                            activebackground='#081923', command=user_pcheck)
            plog_sub.place(x=455, y=350)

            plog_sub2 = Button(plog_fr, image=for_pass_bt, bd=0, bg='#081923',
                            activebackground='#081923', command=forget_pass)
            plog_sub2.place(x=55, y=350)

        # Face Recognition Button Fun
        def flog_rec():
            # Check if user make account properly or not
            # Read all account files
            with open('user_info/user_name.txt') as f:
                acc_name = f.read()

            with open('user_info/user_pp.txt') as f:
                acc_pp = f.read()

            with open('user_info/user_gender.txt') as f:
                acc_gender = f.read()

            # Check all account info before login
            if (acc_name == 'none' and acc_gender == 'none' and acc_pp == 'none'):
                messagebox.showerror('Error', 'Please make an account.')

            elif (acc_name == 'none' or acc_gender == 'none' or acc_pp == 'none'):
                messagebox.showerror(
                    'Error', 'Please make an account properly.')

            else:
                # Camera variable
                cap2 = cv2.VideoCapture(0)

                cam2 = cap2.isOpened()  # Check if camera is connected or not

                # Start face recognition
                if cam2 == True:
                    Frtv.face_check()  # Call the face recoginition
                    with open('user_info/user_recognition.txt') as f:
                        user_reco = f.read()

                    if user_reco == 'known':
                        face_to_nuvia()
                    else:
                        messagebox.showerror(
                            'Error', 'Face not detected, try again!')
                else:
                    messagebox.showerror('Error', 'Camera not detected!')

        # Face Lock Login

        def face_log():
            
            with open('user_info/LoginAcess.txt') as f:
                dest = f.read()

            if dest == '3':
                both_log_fr.destroy()

            flog_fr.pack(fill=BOTH, expand=True)  # initializing  Frame

            # Back Button
            flog_back_b = Button(flog_fr, bd=0, image=reg_back_b, bg='#081923',
                                activebackground='#081923', command=flog_to_wel)
            flog_back_b.place(x=20, y=20)

            # Label
            flog_lb = Label(flog_fr, text='Face Recognition Login', font=(
                'Perpetua', 30, 'bold'), bg='#081923', fg='#9C27B0')
            flog_lb.place(x=140, y=20)

            flog_lb2 = Label(flog_fr, image=face_reco_log, bg='#081923')
            flog_lb2.place(x=220, y=80)

            flog_lb3 = Label(flog_fr, text='Warnings :', bg='#081923', font=(
                'Times Now Romans', 13, 'bold'), fg='#F44336')
            flog_lb3.place(x=20, y=310)

            flog_lb4 = Label(flog_fr, text='1. Make sure that your face is visible.',
                            bg='#081923', font=('Times Now Romans', 13, 'bold'), fg='#F44336')
            flog_lb4.place(x=20, y=335)

            flog_lb5 = Label(flog_fr, text='2. You must have a camera that is connected to your device!',
                            bg='#081923', font=('Times Now Romans', 13, 'bold'), fg='#F44336')
            flog_lb5.place(x=20, y=360)

            # Button
            flog_bt = Button(flog_fr, image=flock_bimg, bd=0, bg='#081923',
                            activebackground='#081923', command=flog_rec)
            flog_bt.place(x=300, y=265)

        # Not Register

        def no_log():

            no_fr.pack(fill=BOTH, expand=True)   # initializing  Frame

            # Back Button
            no_back_b = Button(no_fr, bd=0, image=reg_back_b, bg='#081923',
                            activebackground='#081923', command=no_to_wel)
            no_back_b.place(x=20, y=20)

            # Labels
            no_lb1 = Label(no_fr, text='Not Registered', font=(
                'Perpetua', 30, 'bold'), fg='#F44336', bg='#081923')
            no_lb1.place(x=190, y=20)

            no_lb2 = Label(no_fr, text='Please register and make an account!', font=(
                'Times Now Romans', 18, 'bold'), fg='#03A9F4', bg='#081923')
            no_lb2.place(x=110, y=200)

            no_lb3 = Label(no_fr, image=red_crs, bg='#081923')
            no_lb3.place(x=270, y=80)

            no_lb4 = Label(no_fr, image=bot, bg='#081923')
            no_lb4.place(x=270, y=250)

        # File Contain Login Acess
        with open("user_info/LoginAcess.txt") as f:
            log_ac = f.read()

        # Check which protection is used
        if log_ac == '1':
            welcome_frame.destroy()  # Destory the welcome frame

            face_log()  # Call the Face Login Function

        elif log_ac == '2':
            welcome_frame.destroy()  # Destory the welcome frame

            pass_login()  # Call the Password Function

        elif log_ac == '3':
            welcome_frame.destroy()   # Destory the welcome frame

            both_log()   # Call the Both Function

        else:
            welcome_frame.destroy()  # Destory the Welcome Frame

            no_log()  # Call the No log function

    # Account Page Frame
    def account():
        # Check all info of user
        def acc_info():

            # Read file of user info
            with open('user_info/user_pp.txt') as f:
                user_ppc = f.read()

            # Get the Username
            user_id = user_name.get()

            with open('user_info/user_name.txt', 'w') as f:  # Store user name
                f.write(user_id)

            # Get the Gender
            user_gen = gender.get()

            with open('user_info/user_gender.txt', 'w') as f:  # Store user gender
                f.write(str(user_gen))

            # Check all Conditions
            if user_ppc == 'none':
                messagebox.showerror('Error', 'Please Select an Avatar!')

            elif user_id == '':
                messagebox.showerror('Error', 'Please Enter a Username!')

            elif user_gen == 0:
                messagebox.showerror('Error', 'Please Select a Gender!')

            elif (len(user_id) < 3 or len(user_id) > 6):
                messagebox.showerror('Error', 'Username length should be between 3 to 6 characters')
            
            else:
                acc_to_nuvia()

        # Male Radio Button Dot

        def male_dot():
            # Label
            male_lb = Label(acc_fr, image=dot_m, bg='#081923')
            male_lb.place(x=70, y=50)

            female_rem = Label(acc_fr, bg='#081923')
            female_rem.place(x=500, y=50, width=40, height=27)

        # Female Radio Button Dot

        def female_dot():
            # Label
            female_lb = Label(acc_fr, image=dot_m, bg='#081923')
            female_lb.place(x=500, y=50)

            male_rem = Label(acc_fr, bg='#081923')
            male_rem.place(x=70, y=50, width=40, height=27)

        # File clear previous record
        with open('user_info/user_pp.txt', 'w') as f:
            f.write('none')

        with open('user_info/user_name.txt', 'w') as f:
            f.write('none')

        with open('user_info/user_gender.txt', 'w') as f:
            f.write('none')

        # Account Page Frame
        acc_fr.pack(fill=BOTH, expand=True)

        # Labels
        acc_lb1 = Label(acc_fr, text='Your Profile Pic', font=(
            'Brush Script MT', 28, 'bold'), fg='#039BE5', bg='#081923')
        acc_lb1.place(x=190, y=5)

        acc_lb2 = Label(acc_fr, image=pp_avat, bg='#081923')
        acc_lb2.place(x=260, y=60)

        acc_lb3 = Label(acc_fr, text='Choose an Avatar', font=(
            'Perpetua', 17, 'bold'), fg='#FFB300', bg='#081923')
        acc_lb3.place(x=215, y=153)

        acc_lb4 = Label(acc_fr, text='Username', font=(
            'Times New Romans', 18, 'bold'), fg='#00E5FF', bg='#081923')
        acc_lb4.place(x=240, y=200)

        acc_lb5 = Label(acc_fr, text='Gender', font=(
            'Times New Romans', 18, 'bold'), fg='#00E5FF', bg='#081923')
        acc_lb5.place(x=255, y=280)

        acc_lb6 = Label(acc_fr,  bg='yellow')
        acc_lb6.place(x=0, y=150, width=150, height=3)

        acc_lb7 = Label(acc_fr, text='Male', bg='#081923', font=(
            'Brush Script MT', 40, 'bold'), fg='#F44336')
        acc_lb7.place(x=20, y=90, height=50)

        acc_lb8 = Label(acc_fr,  bg='yellow')
        acc_lb8.place(x=445, y=150, width=200, height=3)

        acc_lb9 = Label(acc_fr, text='Female', bg='#081923', font=(
            'Brush Script MT', 40, 'bold'), fg='#4CAF50')
        acc_lb9.place(x=455, y=90, height=50)

        # Functions for changing Profile Pic

        def pp_lb1():
            acc_lb12 = Label(acc_fr, image=Male_pp1, bg='#081923')
            acc_lb12.place(x=260, y=60)

            # File Contain Profile pic info
            with open('user_info/user_pp.txt', 'w') as f:
                f.write('male_1')

        def pp_lb2():
            acc_lb13 = Label(acc_fr, image=Male_pp2, bg='#081923')
            acc_lb13.place(x=260, y=60)

            # File Contain Profile pic info
            with open('user_info/user_pp.txt', 'w') as f:
                f.write('male_2')

        def pp_lb3():
            acc_lb13 = Label(acc_fr, image=Male_pp3, bg='#081923')
            acc_lb13.place(x=260, y=60)

            # File Contain Profile pic info
            with open('user_info/user_pp.txt', 'w') as f:
                f.write('male_3')

        def pp_lb4():
            acc_lb14 = Label(acc_fr, image=Male_pp4, bg='#081923')
            acc_lb14.place(x=260, y=60)

            # File Contain Profile pic info
            with open('user_info/user_pp.txt', 'w') as f:
                f.write('male_4')

        def pp_lb5():
            acc_lb15 = Label(acc_fr, image=Female_pp5, bg='#081923')
            acc_lb15.place(x=260, y=60)

            # File Contain Profile pic info
            with open('user_info/user_pp.txt', 'w') as f:
                f.write('female_1')

        def pp_lb6():
            acc_lb16 = Label(acc_fr, image=Female_pp6, bg='#081923')
            acc_lb16.place(x=260, y=60)

            # File Contain Profile pic info
            with open('user_info/user_pp.txt', 'w') as f:
                f.write('female_2')

        def pp_lb7():
            acc_lb17 = Label(acc_fr, image=Female_pp7, bg='#081923')
            acc_lb17.place(x=260, y=60)

            # File Contain Profile pic info
            with open('user_info/user_pp.txt', 'w') as f:
                f.write('female_4')

        def pp_lb8():
            acc_lb18 = Label(acc_fr, image=Female_pp8, bg='#081923')
            acc_lb18.place(x=260, y=60)

            # File Contain Profile pic info
            with open('user_info/user_pp.txt', 'w') as f:
                f.write('female_3')

        # Buttons for Avatars
        Avatar_b1 = Button(acc_fr, image=avatar1, bg='#081923',
                        bd=0, activebackground='#081923', command=pp_lb1)
        Avatar_b1.place(x=20, y=190)

        Avatar_b2 = Button(acc_fr, image=avatar2, bg='#081923',
                        bd=0, activebackground='#081923', command=pp_lb2)
        Avatar_b2.place(x=120, y=190)

        Avatar_b3 = Button(acc_fr, image=avatar3, bg='#081923',
                        bd=0, activebackground='#081923', command=pp_lb3)
        Avatar_b3.place(x=20, y=300)

        Avatar_b4 = Button(acc_fr, image=avatar4, bg='#081923',
                        bd=0, activebackground='#081923', command=pp_lb4)
        Avatar_b4.place(x=120, y=300)

        Avatar_b5 = Button(acc_fr, image=avatar5, bg='#081923',
                        bd=0, activebackground='#081923', command=pp_lb5)
        Avatar_b5.place(x=500, y=190)

        Avatar_b6 = Button(acc_fr, image=avatar6, bg='#081923',
                        bd=0, activebackground='#081923', command=pp_lb6)
        Avatar_b6.place(x=400, y=190)

        Avatar_b7 = Button(acc_fr, image=avatar7, bg='#081923',
                        bd=0, activebackground='#081923', command=pp_lb7)
        Avatar_b7.place(x=500, y=300)

        Avatar_b8 = Button(acc_fr, image=avatar8, bg='#081923',
                        bd=0, activebackground='#081923', command=pp_lb8)
        Avatar_b8.place(x=400, y=300)

        # Username Variable
        user_name = StringVar()

        # Entry Username
        acc_ent = Entry(acc_fr, font=('Times New Roman', 11, 'bold'), textvariable=user_name)
        acc_ent.place(x=230, y=240, width=140)

        # Radio Button Variable
        gender = IntVar()

        # Radio Buttons
        acc_rd = Radiobutton(acc_fr, text='Male', bg='#081923', fg='#FFB300', variable=gender, value=1,
                            activebackground='#081923', activeforeground='#FFB300', font=('Perpetua', 14, 'bold'), command=male_dot)
        acc_rd.place(x=210, y=320)

        acc_rd2 = Radiobutton(acc_fr, text='Female', bg='#081923', fg='#FFB300', variable=gender, value=2,
                            activebackground='#081923', activeforeground='#FFB300', font=('Perpetua', 14, 'bold'), command=female_dot)
        acc_rd2.place(x=300, y=320)

        # Submit Button
        acc_sub = Button(acc_fr, text='Submit', bd=0, image=submit_bt,
                        bg='#081923', activebackground='#081923', command=acc_info)
        acc_sub.place(x=250, y=360)

    # Both Face Lock and Password Frame
    def both_fr():
        reg_fr.destroy()

        # For Password and Face Lock Both Checker
        Pcheck = 1

        faceLock_fr(Pcheck)

    # Face Lock Page Frame

    def faceLock_fr(Pcheck2):

        # Face Recognition
        def face_reco():
            # Camera variable
            cap1 = cv2.VideoCapture(0)

            cam = cap1.isOpened()  # Check if camera is connected or not

            if (cam == True):
                Frtv.face_capture()
                if Pcheck2 == 1:
                    face_to_pass()
                else:
                    # File Contain Login Acess
                    with open("user_info/LoginAcess.txt", "w") as f:
                        f.write("1")
                    # Interchange Function
                    fl_to_acc()
            else:
                messagebox.showerror('Error', 'Camera not detected!!')

        # Face Lock Frame
        flock_fr.pack(fill=BOTH, expand=True)

        # Back Button
        flock_back_b = Button(flock_fr, bd=0, image=reg_back_b,
                            bg='#081923', activebackground='#081923', command=flock_back)
        flock_back_b.place(x=20, y=20, width=54, height=54)

        # Labels
        flock_lb = Label(flock_fr, text='Face Lock Protection', bg='#081923',
                        fg='#448AFF', font=('Times New Roman', 30, 'bold'))
        flock_lb.place(x=150, y=15)

        flock_lb2 = Label(flock_fr, image=face, bg='#081923')
        flock_lb2.place(x=250, y=90)

        flock_lb3 = Label(flock_fr, text='It takes 20 seconds for recognizing your face',
                        bg='#081923', fg='#FFC107', font=('Times New Roman', 20, 'bold'))
        flock_lb3.place(x=40, y=220)

        flock_lb4 = Label(flock_fr, text='Warning: You must have a camera that is connected to your device!',
                        bg='#081923', fg='#D50000', font=('Times New Roman', 15, 'bold'))
        flock_lb4.place(x=8, y=360)

        # Buttton
        flock_bt = Button(flock_fr, image=flock_bimg, bd=0, bg='#081923',
                        activebackground='#081923', command=face_reco)
        flock_bt.place(x=280, y=270)

    # Password Page Frame
    def password_fr(Pcheck3):

        # Password Generator
        def password_gen():

            # Call to generate password
            passtv.Pass_generator()

            # Get the generated password
            with open('user_info/gen_pass.txt') as f:
                password1 = f.read()

            pass_ls.delete(0)
            pass_ls.insert(END, password1)


        # Password Checker
        def pass_check():

            # Driver code
            password2 = user_pass.get()

            # Store the input password
            with open("user_info/input_password.txt", "w") as f:
                    f.write(password2)

            # Call the password chechker
            passtv.Pass_Checker()

            # Read if it is valid or not
            with open("user_info/password_validty.txt") as f:
                valdo = f.read()


            # Check if password is Valid or not
            if (valdo == 'valid'):

                # Only for Password Protection
                if Pcheck3 == 0:
                    # File Contain Login Acess
                    with open("user_info/LoginAcess.txt", "w") as f:
                        f.write("2")

                # For Both Protection
                if Pcheck3 == 1:
                    # File Contain Login Acess
                    with open("user_info/LoginAcess.txt", "w") as f:
                        f.write("3")

                pass_to_acc()  # Interchange Function
            else:
                messagebox.showerror('Error', 'Invalid Password!')

        # Password Frame
        pass_fr.pack(fill=BOTH, expand=True)

        # Check if Both Option is selected or not
        if Pcheck3 == 0:

            # Back Button
            pass_back_b = Button(pass_fr, bd=0, image=reg_back_b,
                                bg='#081923', activebackground='#081923', command=pass_back)
            pass_back_b.place(x=20, y=20, width=54, height=54)

        else:
            pass_lb12 = Label(pass_fr, text='  ', bg='#081923', fg='#081923')
            pass_lb12.place(x=20, y=20, width=54, height=54)

        # Label for password protection amd image
        pass_lb2 = Label(pass_fr, text='Password Protection', font=(
            'Times New Roman', 30, 'bold'), bg='#081923', fg='#76FF03')
        pass_lb2.place(x=150, y=15)

        pass_lb3 = Label(pass_fr, image=pass_img, bg='#081923')
        pass_lb3.place(x=410, y=80)

        # Labels
        pass_lb4 = Label(pass_fr, text='Password', bg='#081923',
                        font=('Perpetua', 18, 'bold'), fg='#00bfff')
        pass_lb4.place(x=420, y=193)

        pass_info = Label(pass_fr, text='Password policies mention below :',
                        bg='#081923', font=('Perpetua', 13, 'bold'), fg='red')
        pass_info.place(x=5, y=90)

        pass_info2 = Label(pass_fr, text=' 1.Password should not contain any space.',
                        bg='#081923', font=('Perpetua', 13, 'bold'), fg='red')
        pass_info2.place(x=5, y=120)

        pass_info3 = Label(pass_fr, text=' 2.Password should contain at least one digit(0-9) and\nlowercase letter(a-z) and one uppercase letter(A-Z).',
                        bg='#081923', font=('Perpetua', 13, 'bold'), fg='red')
        pass_info3.place(x=5, y=150)

        pass_info4 = Label(pass_fr, text=' 3.Password length should be between 8 to 15 \ncharacters.',
                        bg='#081923', font=('Perpetua', 13, 'bold'), fg='red')
        pass_info4.place(x=5, y=200)

        pass_info5 = Label(pass_fr, text=' 4.Password should contain at least one special \ncharacter ( @, #, %, &, !, $, etc….).',
                        bg='#081923', font=('Perpetua', 13, 'bold'), fg='red')
        pass_info5.place(x=5, y=250)

        pass_bar = Label(pass_fr, bg='yellow')
        pass_bar.place(x=0, y=305, width=600, height=3)

        pass_info6 = Label(pass_fr, text='Password Genrator', bg='#081923', font=(
            'Perpetua', 15, 'bold'), fg='#FF9800')
        pass_info6.place(x=220, y=310)

        pass_info7 = Label(pass_fr, text='Click on Password\nthen "ctrl+c" to copy,\n"ctrl+v" for paste.',
                        bg='#081923', font=('Perpetua', 13, 'bold'), fg='#00E5FF')
        pass_info7.place(x=430, y=320)

        # Submit Button
        pass_sub = Button(pass_fr, text='Submit', bd=0, image=submit_bt,
                        bg='#081923', activebackground='#081923', command=pass_check)
        pass_sub.place(x=430, y=270, width=87, height=30)

        # Password Generator
        pass_gen_b = Button(pass_fr, image=pass_gen_bimg, bd=0, bg='#081923',
                            activebackground='#081923', command=password_gen)
        pass_gen_b.place(x=100, y=347)

        # Store user password
        user_pass = StringVar()

        # Password Entry
        pass_ent = Entry(pass_fr, font=('Times New Roman',
                                        13, 'bold'), textvariable=user_pass)
        pass_ent.place(x=390, y=230, width=173)

        # Password Listbox
        pass_ls = Listbox(pass_fr, font=('Times New Roman', 13, 'bold'))
        pass_ls.place(x=215, y=350, width=178, height=25)

    # Register Page Frame
    def register_fr():
        # Register frame
        reg_fr.pack(fill=BOTH, expand=True)

        # Back Button
        back_b = Button(reg_fr, text='back', bd=0, command=reg_back,
                        image=reg_back_b, bg='#081923', activebackground='#081923')
        back_b.place(x=20, y=20, width=54, height=54)

        # Label for images
        face_lb = Label(reg_fr, image=face, bg='#081923')
        face_lb.place(x=20, y=100)

        pass_lb = Label(reg_fr, image=pass_img, bg='#081923')
        pass_lb.place(x=230, y=100)

        both_lb = Label(reg_fr, image=both_img, bg='#081923')
        both_lb.place(x=450, y=100)

        # Face Lock Button
        face_bt = Button(reg_fr, text='Face Lock', bd=0, image=face_reco_img,
                        bg='#081923', activebackground='#081923', command=reg_dest2)
        face_bt.place(x=23, y=230, width=120, height=42)

        # Password Button
        pass_bt = Button(reg_fr, text='Password', bd=0, bg='#081923',
                        activebackground='#081923', image=pass_b_img, command=reg_dest)
        pass_bt.place(x=243, y=230, width=98, height=48)

        # Both pass and face Button
        both_bt = Button(reg_fr, text='Password', bd=0, bg='#081923',
                        activebackground='#081923', image=both_b_img, command=both_fr)
        both_bt.place(x=460, y=230, width=110, height=45)

        # Infomation Labels
        info_lb1 = Label(reg_fr, text='This feature provides\nFace Lock \n    Protection', font=(
            'Arial', 11, 'bold'), bg='#081923', fg='#0AFFFF')
        info_lb1.place(x=20, y=300)

        info_lb2 = Label(reg_fr, text='This feature provides\nPassword \n     Protection', font=(
            'Arial', 11, 'bold'), bg='#081923', fg='#0AFFFF')
        info_lb2.place(x=225, y=300)

        info_lb3 = Label(reg_fr, text='This feature provides\nFace Lock And\nPassword Protection', font=(
            'Arial', 11, 'bold'), bg='#081923', fg='#0AFFFF')
        info_lb3.place(x=430, y=300)

        info_lb4 = Label(reg_fr, text='Select any one of the security protection', font=(
            'Perpetua', 20, 'bold'), bg='#081923', fg='orange')
        info_lb4.place(x=100, y=20)

    # Destory Welcome Frame
    def wel_dest():
        welcome_frame.destroy()

        register_fr()  # Call the register frame

    # Register Back
    def reg_back():
        reg_fr.destroy()  # Destory the register frame

        main_fr()     # Call the Main Function

    # Destory Register Frame
    def reg_dest():
        reg_fr.destroy()  # Destory the register frame

        password_fr(0)  # Call the Password Frame

    # Password Back
    def pass_back():
        pass_fr.destroy()  # Destory the password frame

        main_fr()  # Call the Main Function

    # Destory Register Frame
    def reg_dest2():
        reg_fr.destroy()  # Destory the register frame

        faceLock_fr(0)  # Call the FaceLock Frame

    # Face Lock Back
    def flock_back():
        flock_fr.destroy()  # Destory the password frame

        main_fr()  # Call the Main Function

    # Face Lock to Account Frame
    def fl_to_acc():
        flock_fr.destroy()  # Destory the Face Lock frame

        account()  # Call the Account Funtion

    # Password to Account Frame
    def pass_to_acc():
        pass_fr.destroy()  # Destroy the Password Frame

        account()

    # Face Lock to Password Frame
    def face_to_pass():
        flock_fr.destroy()   # Destory the Face Lock Frame

        password_fr(1)  # Call the password frame

    # NO Log to Welcome Frame
    def no_to_wel():
        no_fr.destroy()  # Destory the No Register Frame

        main_fr()  # Call main function

    # Face Login to Welcome Frame
    def flog_to_wel():
        flog_fr.destroy()  # Destory the Face Login Frame

        main_fr()  # Call main function

    # Password Login to Welcome Frame
    def plog_to_wel():
        plog_fr.destroy()   # Destory the Password Frame

        main_fr()  # Call the main function

    # Both Login to Welcome Frame
    def blog_to_wel():
        both_log_fr.destroy()   # Destory the Both Frame

        main_fr()  # Call the main function

    # Face Login to Nuvia(virtual assistance)
    def face_to_nuvia():
        flog_fr.destroy() # Destory the face login frame

        nuvia()

    # Account to Nuvia(virtual assistance)
    def acc_to_nuvia():
        acc_fr.destroy() # Destory the  Account frame

        nuvia()

    # Password Login to Nuvia(virtual assistance)
    def pass_to_nuvia():
        plog_fr.destroy() # Destory the pass login frame

        nuvia()

    # Face Login to Nuvia(virtual assistance)
    def re_to_nuvia():
        reset_fr.destroy() # Destory the Reset frame

        nuvia()



    # Buttons for Login and Singup
    login_b = Button(welcome_frame, text='Login', bg='#081923',
                    image=log_pic, bd=0, activebackground='#081923', command=login_va)
    login_b.place(x=200, y=150, width=94, height=40)

    register_b = Button(welcome_frame, text='Register', bg='#081923',
                        image=reg_pic, bd=0, activebackground='#081923', command=wel_dest)
    register_b.place(x=275, y=250, width=100, height=33)


    # Digital Clock
    def clock_time():
        # Get the Current Time with pm or am, Day and Date
        hr, min, sec, noon, date, month, year, day = Clock.current_time()

        # Show current time, day and date on screen
        lb_hr.config(text=hr)
        lb_min.config(text=min)
        lb_sec.config(text=sec)
        lb_noon.config(text=noon)
        lb_date.config(text=f'{date}-{month}-{year}')
        lb_day.config(text=day)


        lb_hr.after(200, clock_time)
    # Call the clock fun
    clock_time()


# This is Global Variable for Password to check if user select both option
Pcheck = 0


# Main Frame
main_fr()

win.mainloop()