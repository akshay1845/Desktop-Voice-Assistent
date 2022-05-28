from sys import setcheckinterval
from types import CodeType
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser 
import os
import random

engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)

engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("GOOD MORNING!")

    elif hour>=12 and hour<18:
        speak("GOOD Afternoon!")

    else:
        speak("GOOD EVENING!")
    
    speak("I am your Assistant. how may i help you?")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        print(e)
        print("Say that again please!!")
        return "None"
    
    return query

def Goodbye_wish():
    hour=int(datetime.datetime.now().hour)
    speak("It's my pleasure to Help you.")
    if hour>=0 and hour<18:
        speak("GoodBye!")
        speak("Have a Nice Day!!!")

    else:
        speak("GoodBye!")
        speak("Goodnight!!!")

if __name__ ==  "__main__":
    # speak("Akshay is Clever")
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in  query:
            speak("searching wikipedia!")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\Akshay'
            songs = os.listdir(music_dir)
            random_song=random.randrange(0,len(songs))
            print(songs)
            os.startfile(os.path.join(music_dir,songs[random_song]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            os.startfile(os.path.join(music_dir,songs[random_song]))
            speak(f"sir, the time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        
        elif 'open teams' in query:
            codepath = "C:\\Users\\DELL\\AppData\\Local\\Microsoft\\Teams\\Update.exe" 
            os.startfile(codepath)

        elif 'cricket' in query:
            webbrowser.open("crickbuzz.com")

        elif 'bye' in query:
            Goodbye_wish()
            exit()

        
