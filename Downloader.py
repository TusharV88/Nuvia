# Youtube  Downloader
import os
import requests
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from pytube import YouTube
from threading import Thread
from win10toast_click import ToastNotifier

# Download Video
def video_down(mp4files, link, qual):
    vid = YouTube(link)
    title = vid.title

    def notifyMe():
        f = os.getcwd() + '\Downloads'

        def open_fold():
            os.startfile(f)

        toast = ToastNotifier()
        toast.show_toast(title='Download Complete', msg=title,
                        duration=10, callback_on_click=open_fold)

    if qual in ['720p', '480p', '360p', '240p', '144p']:

        dict = mp4files.itag_index
        li = []
        for key, value in dict.items():
            li.append(key)

        itage = int(li[0])
        try:
            # Download Starts
            stream = vid.streams.get_by_itag(itage)
            stream.download('Downloads/')
            notifyMe()
        except:
            messagebox.showerror(
                'Error', 'Oops!! An Error Occur\nCheck your internet connection')

    else:
        try:
            # Download Starts
            stream = vid.streams.get_by_itag(251)
            stream.download('Downloads/')
            notifyMe()
        except:
            messagebox.showerror(
                'Error', 'Oops!! An Error Occur\nCheck your internet connection')

# Get Youtube video link 
def yt_down():
    global URL

    root = Tk()
    root.title("Youtube Downloader")
    root.geometry('400x150')
    root.minsize(400, 150)
    root.maxsize(400, 150)
    url_fr = Frame(root, bg='#081923')
    str_fr = Frame(root, bg='#081923')

    def stream_yt(link):
        global quality_box

        url_fr.destroy()

        str_fr.pack(fill=BOTH, expand=True)

        def get_qual():
            qual = quality_box.get()
            video = YouTube(link)
            if qual in ['720p', '480p', '360p', '240p', '144p', 'only audio']:

                if qual == 'only audio':
                    mp4files = video.streams.filter(only_audio=True)
                else:
                    mp4files = video.streams.filter(
                        file_extension='mp4', progressive=True, res=qual)
                if len(mp4files) == 0:
                    messagebox.showerror(
                        'Error', 'This video quality not avaliable, please try another')
                else:
                    root.destroy()
                    Thread(target=video_down, args=(
                        mp4files, link, qual,)).start()
            else:
                messagebox.showerror('Error', 'Please, select given option')

        lb = Label(str_fr, text='Select Video Quality', font=(
            'Times Now Romans', 18, 'bold'), fg='#76FF03', bg='#081923')
        lb.place(x=60, y=10)

        quality_box = ttk.Combobox(str_fr, width=20, state='readonly')
        quality_box['values'] = (
            '720p', '480p', '360p', '240p', '144p', 'only audio')
        quality_box.place(x=100, y=60)
        quality_box.current(0)
        quality_box.focus()

        bt = Button(str_fr, text='Download', bd=5, font=('Times Now Romans', 12, 'normal'), bg='#FB8C00',
                    fg='white', activebackground='#FB8C00', activeforeground='white', command=get_qual)
        bt.place(x=130, y=100)

    def yt_url():
        url_fr.pack(fill=BOTH, expand=True)

        def get_url():
            link = URL.get()
            split = link[:4]
            word = 'youtube.com/watch?v'
            lword = len(word)
            start_index = link.find(word)
            extracted_string = link[start_index:start_index+lword]
            if link == '':
                messagebox.showerror('Error', 'Enter a url')
            elif split != 'http':
                messagebox.showerror('Error', 'Enter a correct url')
            elif extracted_string != 'youtube.com/watch?v':
                messagebox.showerror('Error', 'Enter a correct youtube url')
            else:
                r = requests.get(link)
                response = "Video unavailable" in r.text

                if response == False:
                    try:
                        stream_yt(link)
                    except:
                        messagebox.showerror(
                            'Error', 'Check your internet connection')

                else:
                    messagebox.showerror(
                        'Error', 'Something went worng!!\nPlease check your entered url')

        lb = Label(url_fr, text='Youtube Video URL', font=(
            'Times Now Romans', 18, 'bold'), fg='#76FF03', bg='#081923')
        lb.place(x=60, y=10)

        URL = Entry(url_fr,  font=('Times Now Romans', 13, 'bold'))
        URL.place(x=60, y=60, width=280)
        URL.focus()

        bt = Button(url_fr, text='Next', bd=5, font=('Times Now Romans', 14, 'normal'), bg='#FB8C00',
                    fg='white', activebackground='#FB8C00', activeforeground='white', command=get_url)
        bt.place(x=170, y=100)

    yt_url()

    root.mainloop()


if __name__ == '__main__':
    yt_down()
