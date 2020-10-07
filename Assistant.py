import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
from FBLogin import fbLogin
from EmailAttachment import emailAttach
from EmailMessage import sendMessageEmail

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!!")
    else:
        speak("Good Evening,sir!!")
    speak("what can i help you with...")


def takeCommand():
    """it takes input from user"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 500
        r.pause_threshold = 1  # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User : {query}\n")
    except Exception as e:
        # print("can't recognize say that again...")
        print(e)
        return "None"
    return query

if __name__ == "__main__":
    greet()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:  
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            chromePath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))
            webbrowser.get('chrome').open("youtube.com")
        elif 'open google' in query:
            chromePath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))
            webbrowser.get('chrome').open("google.com")
        elif 'open stack overflow' in query:
            chromePath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))
            webbrowser.get('chrome').open("stackoverflow.com")

        elif 'play songs' in query:
            music_dir = "E:\\Project\\Assistant - Copy\\songs"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[2]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is{strTime}")

        elif 'open pycharm' in query:
            appPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.2\\bin\\pyCharm64.exe"
            os.startfile(appPath)
        elif 'open word' in query:
            appPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(appPath)

        elif 'email' in query:
            speak("what you want to do?")
            workToDo = takeCommand().lower()
            try:
                if 'file' in workToDo:
                    emailAttach()
                    speak("Email has been sent !")
                    print("Email has been sent !")
                elif 'message' in workToDo:
                    speak("what should i sent???")
                    content = takeCommand()
                    to = "18it122@charusat.edu.in"
                    sendMessageEmail(to, content)
                    speak("Email has been sent !")
                    print("Email has been sent !")
            except Exception as e:
                print(e)
                speak("Sorry ,i am not able to send this email!")

        elif 'facebook' in query:
            speak('enter your username and password ')
            speak("logging in...")
            fbLogin()

        elif 'exit' in query:
            speak("okay than,bye!")
            print("okay than,bye!")
            exit()