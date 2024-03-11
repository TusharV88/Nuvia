# Process Commands
import os
import time
import webbrowser
import requests
import json
from youtube_search import YoutubeSearch
import random
import pygame
import platform
import psutil
from geopy.geocoders import Nominatim
from geopy import distance
import math
from numpy import reciprocal
from googletrans import Translator
from difflib import get_close_matches
from bs4 import BeautifulSoup
from covid import Covid
from joke.jokes import *
import keyboard
from PIL.ImageGrab import grab
from simple_image_download import simple_image_download as simp
from googlesearch import search
import PIL.Image
from numerize import numerize
from datetime import datetime
import socket


# Read Gender File 
with open('user_info/user_gender.txt') as f:
    gender = f.read()

if gender == '1':
    gender = 'sir'
else:
    gender = 'mam'


data = json.load(open('json_work/dict_data.json', encoding='utf-8'))

# Check internet connection
def internet_connect():
    try:
        socket.create_connection(('Google.com', 80))
        return True
    except OSError:
        return False


# Open Sites
def open_site(query):

    if query in ['open youtube', 'youtube', 'youtube open']:
        webbrowser.open('https://www.youtube.com/')

    elif query in ['open google', 'google', 'google open']:
        webbrowser.open('https://www.google.co.in/')

    elif query in ['open apple', 'apple', 'apple open']:
        webbrowser.open('https://www.apple.com/')

    elif query in ['support google', 'google support']:
        webbrowser.open('https://www.support.google.com/')
        
    elif query in ['open microsoft', 'microsoft open', 'microsoft']:
        webbrowser.open('https://www.microsoft.com/')
        
    elif query in ['play store','google play','play google', 'open play store','open google play','open play google', 'play store open','google play open','play google open']:
        webbrowser.open('https://play.google.com/')

    elif query in ['open wikipedia', 'wikipedia open', 'wikipedia']:
        webbrowser.open('https://en.wikipedia.org/')

    elif query in ['open linkedin', 'linkedin open', 'linkedin']:
        webbrowser.open('https://linkedin.com/')

    elif query in ['open whatsapp', 'whatsapp open', 'whatsapp']:
        webbrowser.open('https://whatsapp.com/')
        
    elif query in ['open facebook', 'facebook open', 'facebook']:
        webbrowser.open('https://facebook.com/')

    elif query in ['open github', 'github open', 'github']:
        webbrowser.open('https://github.com/')

    elif query in ['open amazon', 'amazon open', 'amazon']:
        webbrowser.open('https://amazon.com/')
        
    elif query in ['open instagram', 'instagram open', 'instagram', 'insta']:
        webbrowser.open('https://instagram.com/')

    elif query in ['open stack overflow', 'stack overflow open', 'stack overflow']:
        webbrowser.open('https://stackoverflow.com/')

    elif query in ['open netflix', 'netflix open', 'netflix']:
        webbrowser.open('https://netflix.com/')

    elif query in ['open gmail', 'gmail open', 'gmail']:
        webbrowser.open('https://gmail.com/')
        
    elif query in ['open quora', 'quora open', 'quora']:
        webbrowser.open('https://quora.com/')

    elif query in ['open twitter', 'twitter open', 'twitter']:
        webbrowser.open('https://twitter.com/')

    elif query in ['open steam', 'steam open', 'steam']:
        webbrowser.open('https://steampowered.com/')

    elif query in ['open w3school', 'w3school open', 'w3school']:
        webbrowser.open('https://w3school.com/')

    elif query in ['open telegram', 'telegram open', 'telegram']:
        webbrowser.open('https://telegram.me/')

    elif query in ['open pinterest', 'pinterest open', 'pinterest']:
        webbrowser.open('https://pinterest.com/')

    elif query in ['open playstation', 'playstation open', 'playstation']:
        webbrowser.open('https://playstation.com/')

    elif query in ['open soundcloud', 'soundcloud open', 'soundcloud']:
        webbrowser.open('https://soundcloud.com/')



# Joke Fun
def nuvia_jokes():
    # using get_joke() to generate a single joke
    #language is english
    My_joke = icanhazdad()
    return My_joke


# Get News
def nuvia_news():
    # Creates a header
    headers = {'User-agent': 'Mozilla/5.0'}

    # Requests the webpage
    request = requests.get('https://www.bbc.com/news', headers=headers)
    html = request.content

    # Create some soup
    soup = BeautifulSoup(html, 'html.parser')

    news_list = []

    # Finds all the headers in BBC Home
    for h in soup.findAll('h3', class_='gs-c-promo-heading__title'):
        news_title = h.contents[0].lower()

        if news_title not in news_list:
            if 'bbc' not in news_title:
                news_list.append(news_title)
    return news_list



# Play youtube video
def play_yt(query):
    results = YoutubeSearch(query,max_results=1).to_dict()
    webbrowser.open('https://www.youtube.com/watch?v=' + results[0]['id'])


# Search youtube
def search_yt(query):
    webbrowser.open('https://www.youtube.com/results?search_query=' + query)


# Search google
def search_google(query):
    webbrowser.open('https://www.google.co.in/search?q=' + query)


# Toss Coin
def coin_toss():
    sides = ['tail', 'head']
    side = random.choice(sides)
    return side


# Roll Dice
def dice_roll():
    side = random.randint(1, 6)
    return side


# System info
def sys_info(text):
    if text == 'system info':
        mac = platform.machine()
        ver = platform.version()
        plat = platform.platform()
        psys = platform.system()
        pro = platform.processor()

        return mac, ver, plat, psys, pro

    elif text in ['cpu']:
        # gives a single float value
        cpu = psutil.cpu_percent()
        if cpu > 0.0:
            return cpu
        else:
            time.sleep(2)
            sys_info('cpu')
    elif text in ['memory']:
        mem = psutil.virtual_memory().percent

        return mem

    elif text in ['battery']:
        battery = psutil.sensors_battery()
        plug = battery.power_plugged

        if plug == True:
            return battery.percent, plug
        else:
            return battery.percent, plug


# Play Track 
def play_track():
    pygame.init()
    pygame.mixer.music.load('sounds/track.mp3')
    pygame.mixer.music.play()

    return


# Play Music
def play_music():
    songs = os.listdir('Songs')
    ran_song = random.choice(songs)
    os.startfile(os.path.join('Songs', ran_song))
    li = ['.mp3', '.wav']
    for i in li:
        ran_song = ran_song.replace(i, '')
    return ran_song



# To Do List
file = "user_info/toDoList.txt"
def createList():
	f = open(file,"w")
	present = datetime.now()
	dt_format = present.strftime("Date: " + "%d/%m/%Y"+ " Time: " + "%H:%M:%S" + "\n")
	f.write(dt_format)
	f.close()

def toDoList(text):
	if os.path.isfile(file) == False:
		createList()

	f = open(file,"r")
	x = f.read(8)
	f.close()
	y = x[6:]
	yesterday = int(y)
	present = datetime.now()
	today = int(present.strftime("%d"))
	if (today-yesterday) >= 1:
		createList()
	f = open(file,"a")
	dt_format = present.strftime("%H:%M")
	f.write(f"[{dt_format}] : {text}\n")
	f.close()


def showtoDoList():
	if os.path.isfile(file)==False:
		return ["It looks like that list is empty"]
	
	f = open(file, 'r')
	
	items = []
	for line in f.readlines():
		items.append(line.strip())

	speakList = [f"You have {len(items)-1} items in your list:"]
	for i in items[1:]:
		speakList.append(i.capitalize())
	return speakList


# Create any file.
def create_file(text):
    if text in ['ppt', 'powerpoint', 'power point']:
        file_name = 'sample_file.ppt'

    elif text in ['excel']:
        file_name = 'sample_file.csv'

    elif text in ['spreadsheet']:
        file_name = 'sample_file.xls'

    elif text in ['word', 'document']:
        file_name = 'sample_file.docx'

    elif text in ['text', 'normal', 'simple']:
        file_name = 'sample_file.txt'

    else:
        return 'Unable to create this type of file'

    if os.path.exists('Files_Document') == False:
        os.mkdir('Files_Document')

    file = open('Files_Document/' + file_name, "w") 
    file.close()
    os.startfile('Files_Document\\' + file_name)

    return 'File Created'


# Google Maps
def maps_dir(startPoint, destPoint):
    try:
        geocoder = Nominatim(user_agent='Nuvia')

        start_coord = geocoder.geocode(startPoint)
        dest_coord = geocoder.geocode(destPoint)

        start_location = (start_coord.latitude, start_coord.longitude) 
        dest_location = (dest_coord.latitude, dest_coord.longitude) 
        total = distance.great_circle(start_location, dest_location).km

        webbrowser.open(f'https://www.google.co.in/maps/dir/'+startPoint+'/'+destPoint+'/')
        return round(total, 2)

    except Exception as e:
        return 'none'


# Maths Functions
def maths_table(num):
    tabel = []

    if num <= 1:
        return 'no'

    else:
        for i in range(10):
            tabel.append(num*(i+1))
    return tabel


def maths_perform(trig,x):
    if trig == 'sin':
        rad_val = math.sin(math.radians(x))
        return '{0:.2f}'.format(rad_val)
    elif trig == 'cos':
        rad_val = math.cos(math.radians(x))
        return '{0:.2f}'.format(rad_val)
    elif trig == 'tan':
        rad_val = math.tan(math.radians(x))
        return '{0:.2f}'.format(rad_val)
    elif trig == 'sec':
        rad_val = math.cos(math.radians(x))
        rec_val = reciprocal(rad_val)
        return '{0:.2f}'.format(rec_val)
    elif trig == 'cosec':
        rad_val = math.sin(math.radians(x))
        rec_val = reciprocal(rad_val)
        return '{0:.2f}'.format(rec_val)
    elif trig == 'log':
        rad_val = math.log10(x)
        return '{0:.2f}'.format(rad_val)
    elif trig == 'factorial':
        if x < 0:
            return 
        elif isinstance(x, float):
            return 
        else:
            rad_val = math.factorial(x)
            return rad_val
    elif trig == 'left shift':
        rad_val = x << 1
        return rad_val
    elif trig == 'right shift':
        rad_val = x >> 1
        return rad_val
    elif trig == 'binary':
        if isinstance(x, float):
            return 
        else:
            rad_val = bin(x).replace("0b", "")
            return rad_val

def maths_equation(x):
    x = x.replace('plus', '+')
    x = x.replace('minus', '-')
    x = x.replace('x', '*')
    x = x.replace('multiply', '*')
    x = x.replace('multiply by', '*')
    x = x.replace('multiplied by', '*')
    x = x.replace('divide', '/')
    x = x.replace('division by', '/')
    x = x.replace('divide by', '/')
    x = x.replace('power', '**')
    x = x.replace('power of', '**')
    x = x.replace('to the power', '**')
    x = x.replace('and', '&')
    x = x.replace('or', '|')
    x = x.replace('not of', '~')
    x = x.replace('not', '~')
    x = x.replace('xor', '^')

    try:
        x = eval(x)
        return round(x, 2)
    except Exception as e:
        return e



# Translator
def nuv_translator(text, txt_lang):
    translate = Translator()
    check_lang = translate.detect(text)

    try:
        result = translate.translate(text, src=check_lang.lang, dest=txt_lang)
        return result
    except Exception as e:
        return e


# Dictionary
def nuv_dictionary(word):
    if word in data:
        return random.choice(data[word])
    elif len(get_close_matches(word, data.keys())) > 0:
        word = get_close_matches(word, data.keys())[0]
        return random.choice(data[word])
    else:
        return 'This word does not exit in the dictionary'

# Wikipedia
def nuv_wiki(query):
    soup = BeautifulSoup(requests.get(f'https://uk.search.yahoo.com/search?p={query} + wikipedia').content, 'html.parser')
    yahoo_links = []
    for a in soup.find_all('a', href=True):
        word = 'https://en.wikipedia.org/wiki/'
        start_index = a['href'].find(word)
        if start_index == 0:
            yahoo_links.append(a['href'])

    url = yahoo_links[0]
    re = requests.get(url)
    soup = BeautifulSoup(re.text, 'html.parser')
    
    # getting wikipedia title 
    title = soup.find('title').text
    for i in ['-', ' Wikipedia', 'wikipedia']:
        title = title.replace(i, '')

    paragraphs = []
    # getting all the paragraphs
    for para in soup.find_all("p"):
        paragraphs.append(para.get_text())

    paragraphs = [i for i in paragraphs if i != '\n']
    paras = []
    for para in paragraphs:
        para_len = len(para)
        if para == 'Other reasons this message may be displayed:\n':
            return 'none'

        paras.append(para)
        if para_len > 200:
            elements = ['[a]', r'\n', r'\xa0']
            count = 0
            paras = str(paras)
            
            while True:
                str_count = f'[{count}]'
                elements.append(str_count)
                count += 1
                if count > 100:
                    break

            for i in elements:
                paras = paras.replace(i, '')

            for j in ['[', ']', "'", '"']:
                paras = paras.replace(j, '')

            return paras, title


# Inbuild Image Search
def image_search(query, cog='no'):
    response = simp.simple_image_download
    if cog == 'no':
        response().download(query, limit=1, extensions='.jpeg')
        query_1 = query.replace(' ', '_')
        img_ext = ['.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif']
        for ext in img_ext:
            try:
                if ext == '.png':
                    im = PIL.Image.open(f"simple_images/{query_1}/{query}_1{ext}")
                    rgb_im = im.convert('RGB')
                    rgb_im.save(f'simple_images/{query_1}/{query}_1.jpg')
                else:
                    im = PIL.Image.open(f"simple_images/{query_1}/{query}_1{ext}")
                    im.save(f'simple_images/{query_1}/{query}_1.jpg')
            except:
                return 'File not exist!!'

    else:
        response().download(query, limit=3, extensions='.jpeg')
        query_1 = query.replace(' ', '_')
        img_ext = ['.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif']
        for num in range(1,4):
            for ext in img_ext:
                try:    
                    if ext == '.png':
                        im = PIL.Image.open(f"simple_images/{query_1}/{query}_{num}{ext}")
                        rgb_im = im.convert('RGB')
                        rgb_im.save(f'simple_images/{query_1}/{query}_{num}convert.jpg')
                    else:
                        im = PIL.Image.open(f"simple_images/{query_1}/{query}_{num}{ext}")
                        im.save(f'simple_images/{query_1}/{query}_{num}convert.jpg')
                except:
                    return 'File not exist!!'

# Covid
def covid_tracker():
    covid = Covid(source="worldometers")
    world = covid.get_total_active_cases()
    world = numerize.numerize(world)
    confirmed = covid.get_total_confirmed_cases()
    confirmed = numerize.numerize(confirmed)

    recovered = covid.get_total_recovered()
    recovered = numerize.numerize(recovered)

    deaths = covid.get_total_deaths()
    deaths = numerize.numerize(deaths)
    return world, confirmed, recovered, deaths




# Shutdown 
def shutdown_pc():
    device = platform.system()
    if device == 'Windows':
        os.system("shutdown /s /t 1")

    else:
        os.system("shutdown now -h")


# Restart
def restart_pc():
    device = platform.system()
    if device == 'Windows':
        os.system("shutdown -t 0 -r -f")

    else:
        os.system('reboot now')


# Automate Keys
def auto_keys(query, text='none'):
    if query == 'save':
        # Save 
        keyboard.press('ctrl')
        keyboard.press('s')
        keyboard.release('s')
        keyboard.release('ctrl')

    elif query == 'delete':
        # Delete
        keyboard.press_and_release('backspace')

    elif query == 'enter':
        # Enter
        keyboard.press_and_release('enter')

    elif query == 'select':
        # Select
        keyboard.press('ctrl')
        keyboard.press('a')
        keyboard.release('a')
        keyboard.release('ctrl')

    elif query == 'type':
        # Type
        keyboard.write(text, delay=0.3)


# Automate Tabs
def auto_tabs(query):
    if query == 'switch':
        # Switch Tab
        keyboard.press('ctrl')
        keyboard.press('tab')
        keyboard.release('tab')
        keyboard.release('ctrl')

    elif query == 'new':
        # New Tab
        keyboard.press('ctrl')
        keyboard.press('n')
        keyboard.release('n')
        keyboard.release('ctrl')

    elif query == 'close':
        # Close tab
        keyboard.press('ctrl')
        keyboard.press('w')
        keyboard.release('w')
        keyboard.release('ctrl')


# Automate Windows
def auto_win(query):
    if query == 'close':
        # Close window
        keyboard.press('alt')
        keyboard.press('f4')
        keyboard.release('f4')
        keyboard.release('alt')

    elif query in ['minimize', 'minimise']:
        # Minize Window
        keyboard.press('cmd')
        keyboard.press('down')
        keyboard.release('down')
        keyboard.release('cmd')

    elif query in ['maximize', 'maximise']:
        # Max window
        keyboard.press('cmd')
        keyboard.press('up')
        keyboard.release('up')
        keyboard.release('cmd')

    elif query == 'switch':
        # Switch Window
        keyboard.press('alt')
        keyboard.press('tab')
        keyboard.release('tab')
        keyboard.release('alt')

    elif query in ['screenshot']:
        # ScreenShot
        img = grab()
        img.save('Files_Document/ss.jpg')
        img.show()

# Volume Up and Down Control
def vol_up():
    for i in range(5):
        keyboard.press_and_release('volume up')

def vol_down():
    for i in range(5):
        keyboard.press_and_release('volume down')


# Query Filter
def speech_filter(query):
    chat_data = json.load(open('json_work/NormalChat.json', encoding='utf-8'))
    for i in chat_data.keys():
        lword = len(i)
        start_index = query.find(i)

        extracted_word= query[start_index:start_index+lword]

        if (i in extracted_word):    
            return extracted_word


    word = ['images', 'image', 'joke', 'jokes', 'news', 'read news', 'youtube', 'google', 'toss a coin', 'roll a dice', 'system info', 'system', 'system information', 'cpu', 'memory', 'battery', 'music', 'song', 'date', 'timer', 'day', 'month', 'year', 'time', 'msg', 'message', 'whatsapp message', 'whatsapp msg', 'list', 'ppt', 'excel', 'powerpoint', 'power point','text', 'simple', 'normal', 'spreadsheet', 'word', 'document', 'direction', 'table', 'left shift', 'right shift', 'binary', 'factorial', 'log', '+', '-', '*', '/', 'plus', 'minus', 'multiply', 'multiply by', 'multiplied by', 'divide', 'divide by', 'division by', 'power', 'power of', 'to the power', 'translate', 'translator', 'meaning', 'means', 'dictionary', 'wiki', 'wikipedia', 'who', 'egg catcher', 'egg catcher game', 'quora','twitter','steam','soundcloud','w3shcool','telegram','pinterest','playstation','wordpress','linkedin', 'whatsapp','facebook','github','amazon','instagram','insta','stack overflow','netflix', 'microsoft', 'apple','play store', 'pet', 'movie', 'corona', 'covid', 'definition', 'shutdown', 'restart', 'volume up','volume down', 'volume', 'weather', 'weather info', 'tab', 'window', 'x', 'screenshot', 'save', 'enter', 'delete', 'select', 'type', 'sin', 'cos', 'tan', 'sec', 'cosec', 'and', 'or', 'not', 'not of', 'xor']

    for i in word:
        lword = len(i)
        start_index = query.find(i)

        extracted_word= query[start_index:start_index+lword]


        if (i in extracted_word) and (extracted_word in ['image', 'images', 'definition','joke', 'jokes', 'news', 'read news', 'toss a coin', 'roll a dice', 'cpu', 'memory', 'battery', 'music', 'song', 'date', 'timer', 'day', 'month', 'year', 'system info', 'system', 'system information', 'time', 'msg', 'message', 'whatsapp message', 'whatsapp msg', 'ppt', 'excel', 'powerpoint', 'power point','text', 'simple', 'normal', 'spreadsheet', 'word', 'document', 'direction', 'table', 'left shift', 'right shift', 'binary', 'factorial', 'log', 'translate', 'translator', 'meaning', 'means', 'dictionary', 'wiki', 'wikipedia', 'who', 'egg catcher', 'egg catcher game', 'quora','twitter','steam','soundcloud','w3shcool','telegram','pinterest','playstation','wordpress','linkedin', 'whatsapp','facebook','github','amazon','instagram','insta','stack overflow','netflix', 'microsoft', 'apple', 'play store', 'pet', 'screenpet', 'movie', 'volume up', 'volume down', 'weather', 'weather info', 'tab', 'window', 'screenshot', 'save', 'enter', 'delete', 'select', 'type', 'sin', 'cos', 'tan', 'sec', 'cosec',]):    
            return extracted_word
            

        elif (i in extracted_word) and (extracted_word in ['+', '-', '*', '/', 'plus', 'minus', 'x', 'multiply', 'multiply by', 'multiplied by', 'divide', 'divide by', 'division by', 'power', 'power of', 'to the power', 'and', 'or', 'not', 'not of', 'xor']):    
            return 'evalue'

            
        elif (i in extracted_word) and (extracted_word in ['youtube']):    
            word = ['play', 'download', 'search', 'youtube']
        
            for yt in word:
                lword = len(yt)
                start_index = query.find(yt)

                extracted_word= query[start_index:start_index+lword]

                if extracted_word == 'play': 
                    return 'play youtube'

                elif extracted_word == 'download':
                    return 'download youtube'

                elif extracted_word == 'search':
                    return 'search youtube'

                elif extracted_word == 'youtube':
                    return 'youtube'


        elif (i in extracted_word) and (extracted_word in ['google']):    
            word = ['search', 'play', 'support', 'google']
        
            for yt in word:
                lword = len(yt)
                start_index = query.find(yt)

                extracted_word= query[start_index:start_index+lword]

                if extracted_word == 'search':
                    return 'google search'

                elif extracted_word == 'play':
                    return 'google play'

                elif extracted_word == 'support':
                    return 'google support'

                elif extracted_word == 'google':
                    return 'google'

        elif (i in extracted_word) and (extracted_word in ['list']):    
            word = ['add', 'show']
        
            for yt in word:
                lword = len(yt)
                start_index = query.find(yt)

                extracted_word= query[start_index:start_index+lword]

                if extracted_word == 'add':
                    return 'add list'

                elif extracted_word == 'show':
                    return 'show list'

        elif (i in extracted_word) and (extracted_word in ['covid', 'corona']):    
            word = ['cases', 'case', 'symptoms', 'prevention', 'preventions']
        
            for yt in word:
                lword = len(yt)
                start_index = query.find(yt)

                extracted_word= query[start_index:start_index+lword]

                if extracted_word in ['cases', 'case']:
                    return 'covid cases'

                elif extracted_word == 'symptoms':
                    return 'covid symptoms'

                elif extracted_word in ['preventions', 'prevention']:
                    return 'covid prevention'

        elif (i in extracted_word) and (extracted_word in ['volume']):    
                word = ['increase', 'decrease']
            
                for yt in word:
                    lword = len(yt)
                    start_index = query.find(yt)

                    extracted_word= query[start_index:start_index+lword]

                    if extracted_word == 'increase': 
                        return 'inc'

                    elif extracted_word == 'decrease':
                        return 'dec'

    return 'garbage'   


if __name__ == '__main__':
    while True:
        x = input('To Do List Items Add : ')

        if x == 'stop':
            break

        toDoList(x)
    pass
