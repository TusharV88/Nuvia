# Nuvia Voice

import pyttsx3
from time import localtime


# Speak
def speak(audio):
    # Read and check voice, voice rate and volume
    with open('user_info/nuvia_vocal.txt') as f:
        vocal = f.read()

    with open('user_info/vocal_rate.txt') as f:
        vocal_rate = f.read()

    with open('user_info/vocal_volume.txt') as f:
        vocal_vol = f.read()

    # Check Voice
    if vocal == 'Female':
        vocal = 1
    else:
        vocal = 0

    # Check Voice Rate
    if vocal_rate == 'Very Low':
        vocal_rate = 50
    elif vocal_rate == 'Low':
        vocal_rate = 100
    elif vocal_rate == 'Normal':
        vocal_rate = 180
    elif vocal_rate == 'Fast':
        vocal_rate = 250
    elif vocal_rate == 'Very Fast':
        vocal_rate = 350

    # Initalizing Speak Engine
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[int(vocal)].id)
    engine.setProperty('rate', vocal_rate)
    engine.setProperty('volume', int(vocal_vol)/100)
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = localtime()
    with open('user_info/greet_nuvia.txt', 'w') as f:
        if(hour.tm_hour >= 12 and hour.tm_hour < 17):
            f.write('Good Afternoon\nHow can I help you?')

        elif(hour.tm_hour >= 17 and hour.tm_hour < 21):
            f.write('Good Evening\nHow can I help you?')

        elif(hour.tm_hour >= 21 and hour.tm_hour < 6):
            f.write('How can I help you?')

        elif(hour.tm_hour >= 6 and hour.tm_hour < 12):
            f.write('Good Morning\nHow can I help you?')

        else:
            f.write('How can I help you?')

    print('Hour : ', hour.tm_hour)
    with open('user_info/greet_user.txt', 'w') as f:
        f.write('done')


if __name__ == '__main__':
    wishMe()
    speak('Hello, how are you. I am your personal assistance.')
