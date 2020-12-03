import datetime
import pyttsx3
import speech_recognition as sr
import webbrowser as wb
import os
import time
import multiprocessing
import subprocess
from tkinter import *
engine = pyttsx3.init()


def sleep_for_a_bit(seconds):
    print(f"sleeping {seconds} second(s)")
    time.sleep(seconds)
    print("Done sleeping")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current  date is")
    speak(date)
    speak(month)
    speak(year)

def greeting():
    speak("How can i help you?")


def openother():
        os.startfile('window.py')





def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recongnizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)





        return "None"
    return query


def takesecondcommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recongnizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

        if 'time' in query:
            time()
        elif 'date' in query:
            date()

        elif 'thank you jay' in query:
            speak("see you later")
            exit()

        elif 'turn off' in query:
            speak("see you later")
            os.system("TASKKILL /F /IM py.exe")
            exit()

        elif 'i need you to search something' in query:
            speak("what should i search for you")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab(search+".com")

        elif 'open chrome' in query:
            speak("opening chrome")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab("www.google.com")



        elif 'open youtube' in query:
            speak("ok")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab('youtube.com')

        elif 'you to remember something' in query:
            speak("What should i remember")
            data = takecommand()
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()

        elif 'i need to remember' in query:
            speak("you said to remember "+data)
            remember.close()

        elif 'open steam' in query:
            os.startfile("C:/Program Files (x86)/Steam/steam.exe")
            speak("opening steam")

        elif 'play naruto' in query:
            os.startfile("C:/Program Files (x86)\Steam/steamapps/common/NARUTO SHIPPUDEN Ultimate Ninja STORM 4/NSUNS4.exe")
            speak("Opening naruto")

        elif 'close naruto' in query:
            os.system("TASKKILL /F /IM NSUNS4.exe")
            speak("closing naruto")

        elif 'play Norah Jones' in query:
            os.startfile("C:/Program Files (x86)\Steam/steamapps/common/NARUTO SHIPPUDEN Ultimate Ninja STORM 4/NSUNS4.exe")
            speak("Opening naruto")

        elif 'close Norah Jones' in query:
            os.system("TASKKILL /F /IM NSUNS4.exe")
            speak("closing naruto")

        elif 'play xenoverse 2' in query:
            os.startfile("C:/Program Files (x86)/Steam/steamapps/common/DB Xenoverse 2/START.exe")
            speak("playing xenoverse 2")

        elif 'close xenoverse 2' in query:
            os.system("TASKKILL /F /IM DBXV2.exe")
            speak("closing xenoverse 2")

        elif 'play which it' in query:
            os.startfile("C:/Program Files (x86)/Steam/steamapps/common/WitchIt/witchit.exe")
            speak("playing witch it")

        elif 'close which it' in query:
            os.system("TASKKILL /F /IM wichit.exe")
            speak("closing which it")

        elif 'play witches' in query:
            os.startfile("C:/Program Files (x86)/Steam/steamapps/common/WitchIt/witchit.exe")
            speak("playing witch it")

        elif 'close witches' in query:
            os.system("TASKKILL /F /IM wichit.exe")
            speak("closing wich it")

        elif 'play wicked' in query:
            os.startfile("C:/Program Files (x86)/Steam/steamapps/common/WitchIt/witchit.exe")
            speak("playing witch it")

        elif 'close wicked' in query:
            os.system("TASKKILL /F /IM witchit.exe")
            speak("closing naruto")

        elif 'you there' in query:
            speak("yes, what do you need?")

        elif 'dokkan' in query:
            speak("ok")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab('https://www.youtube.com/results?search_query=dokkan')

        elif 'docom' in query:
            speak("ok")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab('https://www.youtube.com/results?search_query=dokkan')

        elif 'gokhan' in query:
            speak("ok")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab('https://www.youtube.com/results?search_query=dokkan')

        elif 'go card' in query:
            speak("ok")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab('https://www.youtube.com/results?search_query=dokkan')

    except Exception as e:
        print(e)
        speak("sorry, I didn't catch that")
        os.system("TASKKILL /F /IM py.exe")

        return "None"
    return query


p1 = multiprocessing.Process(target=openother)

if __name__ == "__main__":

    while True:

        query = takecommand().lower()

        if query == 'hey jarvis':
            greeting()
            p1.start()
            takesecondcommand()


        elif 'thank you jarvis' in query:
            speak("you're welcome")

