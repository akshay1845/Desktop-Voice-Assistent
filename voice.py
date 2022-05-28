from tkinter import *
from sys import setcheckinterval
from types import CodeType
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser 
import os
import random
import PIL.Image, PIL.ImageTk

window = Tk()

global var
global var1

var = StringVar()
var1 = StringVar()

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
        var.set("Good Morning Sir") 
        window.update()
        speak("GOOD MORNING!")

    elif hour>=12 and hour<18:
        var.set("Good Afternoon")
        window.update()
        speak("Good Afternoon!")

    else:
        var.set("Good Evening")
        window.update()
        speak("GOOD EVENING!")
    
    speak("I am Ruby, your Assistant. how may i help you?")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        var.set("Say that again please!!")
        window.update()
        print(e)
        print("Say that again please!!")
        return "None"
    var1.set(query)
    window.update()
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

def play():
    btn2['state'] = 'disabled'
    btn0['state'] = 'disabled'
    btn1.configure(bg = 'orange')
    # speak("Akshay is Clever")
    wishMe()
    while True:
        btn1.configure(bg = 'orange')
        query = takeCommand().lower()

        if 'exit' in query:
            var.set("Bye sir")
            btn1.configure(bg = '#5C85FB')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            window.update()
            speak("Bye sir")
            break
        
        elif 'your name' in query:
            var.set('I am Ruby.')
            window.update()
            speak("I am Ruby.")

        elif 'how are you' in query:
            var.set('I am fine. Thank you. How are you?')
            window.update()
            speak("I am fine. Thank you. How are you?")

        elif 'wikipedia' in query:
            if 'open wikipedia' in query:
                webbrowser.open('wikipedia.com')
            else:
                try:
                    speak("searching wikipedia")
                    query = query.replace("according to wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to wikipedia")
                    var.set(query)
                    window.update()
                    speak(results)
                except Exception as e:
                    var.set('sorry sir could not find any results')
                    window.update()
                    speak('sorry sir could not find any results')

        elif 'open youtube' in query:
            var.set('opening Youtube')
            window.update()
            speak('opening Youtube')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            var.set('opening google')
            window.update()
            speak('opening google')
            webbrowser.open("google.com")

        elif 'say hello' in query:
            var.set('Hello Everyone!')
            window.update()
            speak('Hello Everyone!')

        elif 'hello' in query:
            var.set('Hello Sir')
            window.update()
            speak("Hello Sir")

        elif 'open stackoverflow' in query:
            var.set('opening stackoverflow')
            window.update()
            speak('opening stackoverflow')
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            var.set('Here are your favorites')
            window.update()
            speak('Here are your favorites')
            music_dir = 'D:\\Akshay'
            songs = os.listdir(music_dir)
            random_song=random.randrange(0,len(songs))
            print(songs)
            os.startfile(os.path.join(music_dir,songs[random_song]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            os.startfile(os.path.join(music_dir,songs[random_song]))
            var.set("Sir the time is %s" % strTime)
            window.update()
            speak(f"sir, the time is {strTime}")

        elif 'open code' in query:
            var.set('opening VS code')
            window.update()
            speak('opening VS code')
            codepath = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        
        elif 'open teams' in query:
            var.set('opening Teams')
            window.update()
            speak('opening Teams')
            codepath = "C:\\Users\\DELL\\AppData\\Local\\Microsoft\\Teams\\Update.exe" 
            os.startfile(codepath)

        elif 'open notepad' in query:
            var.set('opening Notepad')
            window.update()
            speak('opening Notepad')
            codepath = "%windir%\\system32\\notepad.exe" 
            os.startfile(codepath)

        elif 'open paint' in query:
            var.set('opening Paint')
            window.update()
            speak('opening Paint')
            codepath = "%windir%\\system32\\mspaint.exe" 
            os.startfile(codepath)

        elif 'open paint' in query:
            var.set('opening Paint')
            window.update()
            speak('opening Paint')
            codepath = "%windir%\\system32\\mspaint.exe" 
            os.startfile(codepath)

        elif 'cricket' in query:
            var.set('opening Cricbuzz')
            window.update()
            speak('opening Cricbuzz')
            webbrowser.open("crickbuzz.com")

        elif 'thank you' in query:
            var.set("Welcome Sir")
            window.update()
            speak("Welcome Sir")


def update(ind):
    frame = frames[(ind)%100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)

label2 = Label(window, textvariable = var1, bg = '#FAB60C')
label2.config(font=("Courier", 20))
var1.set('User Said:')
label2.pack()

label1 = Label(window, textvariable = var, bg = '#ADD8E6')
label1.config(font=("Courier", 20))
var.set('Welcome')
label1.pack()

frames = [PhotoImage(file='assist.gif',format = 'gif -index %i' %(i)) for i in range(100)]
window.title('RUBY' )

label = Label(window, width = 500, height = 500)
label.pack()
window.after(0, update, 0)

btn0 = Button(text = 'WISH ME',width = 20, command = wishMe, bg = '#5C85FB')
btn0.config(font=("Courier", 12))
btn0.pack()
btn1 = Button(text = 'START',width = 20,command = play, bg = '#5C85FB')
btn1.config(font=("Courier", 12))
btn1.pack()
btn2 = Button(text = 'EXIT',width = 20, command = window.destroy, bg = '#5C85FB')
btn2.config(font=("Courier", 12))
btn2.pack()


window.mainloop()     
