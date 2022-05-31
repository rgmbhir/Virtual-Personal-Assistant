#importing required modules

import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import pyjokes
import time
import googletrans
import sys
import wikipedia
import os
from ecapture import ecapture as ec
import requests
import json
import random
import smtplib
from tkinter import *
import subprocess
import pyautogui as pg
import shutil
import ctypes
from PyQt5 import QtGui,QtCore,QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from gui import Ui_MainWindow


#defining web browser function
def wb(site):
    webbrowser.open(site)
    time.sleep(10)

#initializing pyttsx3 engine

gt= googletrans.Translator()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
nrate = 178
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',nrate)



# speak function

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#defining wish function
def greet():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak('Hello, Good morning Sir. How may i help you.')
    elif hour>=12 and hour<17:
        speak('Hello, Good Afternoon sir. How may i help you')
    else:
        speak('Hello, Good Evening Sir. How may i help you')

#sending email function
def sendmail(to, content):
    server= smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

#must enable acces to low secure devices

    server.login('raghav.gambhir59@gmail.com', 'xxxxx')
    server.sendmail('raghav.gambhir59@gmail.com', to, content)
    server.close()

class Mainthread(QThread):
    def __init__(self):
        super(Mainthread,self).__init__()

    def run(self):
        self.task()


# audio recognizing function (it takes input from mic)

    def listner(self):
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening..............')
            r.pause_threshold = 0.5
            audio = r.listen(source)

            try:
                speak('recognizing')
                print('Recognizing..........')
                query = r.recognize_google(audio, language='en-in')
                print(query)
                speak(query)

            except Exception as e:
                speak("Say  That  again. Or Speak loudly")
                #print("Say  That  again or Speak loudly")

        return query

    def task(self):
        import time
        name = "asimo"
        # Clear = lambda: os.system('cls')

        # Clear()
        greet()
        while True:
            # Clear()

            self.query = self.listner().lower()
            #text = gt.translate(self.query)
            #self.query = text.text
            #self.query = self.query.lower()

            if 'time' in self.query:
                t = datetime.datetime.now().strftime("%H:%M:%S")
                print(t)
                speak(f"The time is  {t}")

            if 'open google ' in self.query:
                speak('launching google')
                wb('https://www.google.com')
                time.sleep(3)

            elif 'open map' in self.query:
                speak("opening google maps")
                wb("https://www.google.co.in/maps/@29.282929,76.026532,8z")

            elif 'open youtube' in self.query:
                speak('opening youtube')
                wb('youtube.com')

            elif 'open github ' in self.query:
                speak('loading github')
                wb("github.com")

            elif 'open stackoverflow' in self.query:
                wb('stackoverflow.com')

            elif 'open gmail' in self.query:
                speak('opening gmail')
                wb('gmail.com')

            elif 'wikipedia' in self.query:
                speak("Searching Wikipedia")
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=5)
                speak("According to Wikipedia")
                speak(results)
                print(results)
                time.sleep(3)

            elif 'search' in self.query:
                self.query = self.query.replace("search", "")
                wb(self.query)

            elif 'your name' in self.query:
                speak(f'My friends call me {name}')

            elif "can i change your name" in self.query:
                speak("What name you wanna give to me.")
                name = self.listner()
                speak("Thanks! for giving me the new name.")

            elif 'change my name to' in self.query:
                self.query = self.query.replace('change my name to', "")
                name = self.query

            elif "who i am" in self.query or 'about me' in self.query:
                speak("You are a great human. May be you are too lazy or too busy that's why you are using me.")

            elif 'who are you' in self.query:
                speak("I am your virtual assistant. Designed to reduce your workload.")

            elif 'end' in self.query or 'exit' in self.query or 'stop' in self.query or 'good bye' in self.query or 'bye' in self.query:
                speak('Ok, your personal assistant is shutting down.')
                speak('Thanks for giving me your valuable time')
                sys.exit()


            elif 'why you came to this world' in self.query or 'why you came in this universe' in self.query:
                speak("Even I also do not know it. May be it's a secret")

            elif 'is love' in self.query:
                speak("It is the 7th sense that destroy all other senses.")

            elif "don't listen" in self.query or 'stop listening' in self.query:
                speak(f"for how much time you wanna stop {name} from listening")
                a = int(self.listner())
                time.sleep(a)

            elif 'how are you' in self.query:
                speak('I am Fine')
                speak('how are you, sir')

            elif 'good morning' in self.query:
                speak('A warm good morning to you. Have a nice day.')

            elif 'good afternoon' in self.query:
                speak("Good afternoon sir. Have a nice day")

            elif 'good night' in self.query:
                speak("good night to you too")

            elif 'good evening' in self.query:
                speak('Good evening sir/mam')

            elif 'I love you' in self.query:
                speak("It's Hard to understand")

            elif 'fine' in self.query or 'good' in self.query:
                speak("It's good to hear that you are fine.")

            elif 'not fine' in self.query or 'feeling low' in self.query or 'not good' in self.query:
                speak('What happen sir.\n listen to the jokes. May be it will ')
                speak(pyjokes.get_jokes())

            elif 'chrome' in self.query or 'google chrome' in self.query:
                speak('launching google chrome')
                os.startfile(r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

            elif 'who created you' in self.query or 'who discovered you' in self.query or 'who made you' in self.query:
                speak(f'I am {name}. I was built by Raghav')

            elif 'date' in self.query:
                Today = datetime.date.today()
                speak(Today)

            elif 'photo' in self.query or 'take picture' in self.query or 'camera' in self.query:
                speak("Capturing Photo. Say cheese!")
                ec.capture(0, "test", "img.jpg")

            elif 'ms office' in self.query or "microsoft office" in self.query:
                speak('opening Microsoft office')
                os.startfile(r"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office")

            elif 'git' in self.query or 'gitbash' in self.query:
                speak('opening git terminal')
                os.startfile(r"C:\\Program Files\\Git\\git-bash.exe")

            elif "powerpoint" in self.query or 'ppt' in self.query:
                speak('Launching Power point for you')
                os.startfile(
                    r"C:\\ProgramData\\Microsoft\Windows\\Start Menu\\Programs\Microsoft Office\\Microsoft PowerPoint 2010.lnk")

            elif "switch window" in self.query:
                pg.hotkey('alt','tab')

            elif 'copy' in self.query:
                pg.hotkey('ctrl','c')
                speak('data copied to clipboard')

            elif 'select all' in self.query:
                pg.hotkey('ctrl','a')

            elif'close thi window' in self.query or 'close' in self.query:
                pg.hotkey('alt','f4')

            elif 'undo' in self.query:
                pg.hotkey('ctrl','z')

            elif 'redo' in self.query:
                pg.hotkey('ctrl',)

            elif'open new window'in self.query:
                pg.hotkey('ctrl','n')

            elif'paste' in self.query:
                pg.htokey('ctrl','v')

            elif 'type' in self.query:
                speak('Ok,I am listening')
                pg.typewrite(listner())

            elif 'save' in self.query:
                pg.hotkey('ctrl','s')

            elif 'back' in self.query:
                pg.hotkey('browseback')

            elif 'go up' in self.query:
                pg.hotkey('pageup')

            elif 'go down' in self.query:
                pg.hotkey('pagedown')

            elif "word" in self.query or 'ms word' in self.query or 'microsoft word' in self.query:
                speak('Launching wordpad for you')
                os.startfile(
                    r"C:\\ProgramData\\Microsoft\Windows\\Start Menu\\Programs\Microsoft Office\\Microsoft Word 2010.lnk")
                time.sleep(2)

            elif 'excel' in self.query:
                speak('Launching Excel sheets for you')
                os.startfile(
                    r"C:\\ProgramData\\Microsoft\Windows\\Start Menu\\Programs\Microsoft Office\\Microsoft Excel 2010.lnk")
                time.sleep(3)

            elif "play music" in self.query or "play songs" in self.query or 'song' in self.query:
                speak("playing songs")
                wb("https://www.youtube.com/watch?v=_MqGhYihNr0&list=RD_MqGhYihNr0&start_radio=1&t=0")

            elif 'open pycharm' in self.query or 'pycharm' in self.query:
                speak('Loading pycharm')
                os.startfile(r"C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.1\\bin\\pycharm64.exe")
                time.sleep(2)

            elif "something funny" in self.query or 'bored' in self.query or 'bore' in self.query:
                speak('Showing something that will make you laugh.')
                wb("https://www.youtube.com/watch?v=d72vXhJDE6M&list=RDd72vXhJDE6M&start_radio=1&t=2")
                time.sleep(5)

            elif 'news' in self.query or 'headlines' in self.query or 'headline' in self.query:
                speak("In which language you want to listen .English or Hindi")
                lang = self.listner().lower()
                if 'english' in lang:
                    url = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=6206970d0089453e99fd9e1e774cab59"
                    news = requests.get(url).text
                    n_dict = json.loads(news)
                    articls = n_dict['articles']
                    speak("Today's headlines are")
                    time.sleep(2)
                    for article in articls:
                        speak(article['title'])
                        print(article['title'])
                        time.sleep(3)
                else:
                    speak('Displaying news for you')
                    wb("https://www.indiatoday.in/top-stories")

            elif 'snake game' in self.query or 'games' in self.query:
                speak('Here you go to snake game.')
                os.startfile(r"C:\\Users\\Dell\\PycharmProjects\\pythonProject\\snake.py")

            elif 'bol game' in self.query or 'ball game' in self.query:
                os.startfile(r"C:\\Users\\Dell\\PycharmProjects\\pythonProject\\tiny tennis.py")

            elif 'notepad' in self.query:
                os.startfile(r"C:\\Users\\Dell\\PycharmProjects\\pythonProject\\n.py")

            elif 'restart' in self.query or 'restart pc' in self.query:
                subprocess.call(["shutdown", "/r"])

            elif 'hibernate' in self.query or 'sleep' in self.query:
                subprocess.call("shutdown /h")

            elif 'log off' in self.query or 'sign out' in self.query:
                speak("your pc will log off in 5 seconds.")
                time.sleep(5)
                subprocess.call(["shutdown", "/l"])

            elif 'shutdown' in self.query:
                speak('Hold on, your pc is shutting down.')
                subprocess.call('shutdown /p /f')

            elif 'write' in self.query or 'write a note' in self.query or 'write note' in self.query:
                speak('What to write sir, ')
                note = self.listner()
                with open('note.txt', 'a') as f:
                    speak("Would you like to add date or time")
                    ans = self.listner().lower()
                    if 'am' in ans or 'haa' in ans:
                        time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                        f.write(time)
                        f.write("\n \n")
                        f.write(note)

                    else:
                        f.write(note)
                        f.write("\n\n")

            elif 'show note' in self.query:
                with open('note.txt', 'r') as f:
                    print(f.read())
                    speak(f.read())

            elif 'email to rahul' in self.query:
                try:
                    speak("Speak, what to send")
                    content = self.listner()
                    to = 'rahulgmbhir15@gmail.com'
                    sendmail(to, content)
                    speak('Email has sent')

                except Exception as e:
                    speak('unable to send the e-mail')

            elif 'send email' in self.query:
                try:
                    speak('what to send')
                    content = self.listner()
                    speak('Whom to send')
                    to = self.listner()
                    sendmail(to, content)
                    speak("send succesfully")

                except Exception as e:
                    speak("unable to send this email")

            elif 'weather' in self.query:
                url = "https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}"
                speak("City name")
                name = self.listner()
                id = 'c75ee48afedd9397ba5c41aa1fcfffff'
                complete_url = f"https://api.openweathermap.org/data/2.5/weather?q={name}&appid={id}"
                response = requests.get(complete_url)
                x = response.json()

                if x['cod'] != '404':
                    y = x["main"]
                    c_temprature = y["temp"]
                    c_humidity = y["humidity"]
                    z = x["weather"]
                    wthr_description = z[0]["description"]
                    speak("Current temperature is" + str(c_temprature))

                else:
                    speak("city not found")

startexecution = Mainthread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
     #   self.ui.pushButton_2.clicked.connect(self.startTask)
        self.ui.pushButton.clicked.connect(self.close)

    #def startTask(self):

        self.ui.movie= QtGui.QMovie("j/39f6a005763b37e2237b320df0e68e31.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("j/T8bahf.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("j/2RNb.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        startexecution.start()
#main function

if __name__ == '__main__':
    app=QApplication(sys.argv)
    jarvis= Main()
    jarvis.show()
    exit(app.exec_())

