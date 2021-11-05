# import library
import os
from typing import Text
import speech_recognition as sr  # for speech detection
import pyttsx3
import datetime  # for date and time
import wikipedia
import webbrowser
# in pyttsx3 library call microsoft speech API called sapi5

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)  # to check voices available on device
engine.setProperty('voices', voices[1])  # to set the voice of the bot
# voice was set to english female us accent


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# function to greet

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    elif hour >= 20 and hour < 24:
        speak("Good Night!")
    else:
        speak("Good Evening!")


speak("Hey there!! I am A P R  , Your personal assistant")

# function to input from mic and convert it into string


def acceptCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening..")
        r.pause_threshold = 1
        r.non_speaking_duration = 0.2
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Recognizing...")
        queryTest = r.recognize_google(audio, language='en-in')
        print("user said ", queryTest)

    except Exception as e:
        speak("say that again please")
        return "None"
    return queryTest


test = wish()
# just to  test the bot
if __name__ == "__main__":

    if 1:
        queryTest = acceptCommand().lower()

        # logic for executing tasks on basis of query using wikipedia  module
        if 'wikipedia' in queryTest:
            speak("searching wiki..")
            queryTest = queryTest.replace("wikipedia", "")
            results = wikipedia.summary(queryTest, sentences=1)
            speak("ACCORDING TO WIKIPEDIA.. ")
            print(results)
            speak(results)

        # FOR OPENING YOUTUBE using module webbrowser
        elif 'open youtube' in queryTest:
            webbrowser.open("youtube.com")
        # FOR OPENING GOOGLE using module webbrowser
        elif'open google search' in queryTest:
            webbrowser.open("google.com")
        # FOR GETTING TIME using module datetime
        elif'the time' in queryTest:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        # FOR OPENING APPS
        # FOR OPENING VS CODE using os module
        elif'program' in queryTest:
            codePath = "C:\\Users\\pratheek\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codePath)
        elif 'anaconda' in queryTest:
            codepath1 = "C:\\Users\\pratheek\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)"
            os.startfile(codepath1)
