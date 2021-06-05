import pyttsx3
import speech_recognition as sr
import datetime
from datetime import date
import os
import cv2
import pywhatkit
from requests import get
import wikipedia
import webbrowser
import smtplib
import sys


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

# text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# convert voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        audio = r.listen(source)


    try:
        print("Recognizing......")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}")


    except Exception as e:
        speak("could you please repeat......")
        return "none"
    return query

# to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning sir")
    elif hour>12 and hour<=17:
        speak("good afternoon sir")
    elif hour>17 and hour<=23:
        speak("good evening sir")
    speak("i am Ava, how may i assist you")

# to send mail
def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('bhayanaanmol@gmail.com','anmol2300')
    server.sendmail('bhayanaanmol@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wish()
    while True:
        query = takecommand().lower()
        #logic building
        if "open notepad" in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)
        elif "open adobe reader" in query:
            apath = "C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader"
            os.startfile(apath)
        elif "open command prompt" in query:
            os.system("start cmd")
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret , img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        elif "day" in query:
            day = date.today()
            print(day)
            speak("Today is " + day)
        elif "time" in query:
            time = datetime.datetime.now().strftime("%I%M %p")
            print(time)
            speak("Currently it is " + time)
        elif "music" in query:
            song = query.replace("play", " ")
            speak("playing " + song)
            print("playing " + song)
            pywhatkit.playonyt(song)
        elif "ip address" in query:
            ip = get('https://ipify.org').text
            speak(f" your ip address is {ip}")
        elif "wikipedia" in query:
            speak("searching wikipedia......")
            query = query.replace("wikipedia", " ")
            info = wikipedia.summary(query, sentences=3)
            speak(" according to wikipedia,   "+ info)
            print(" according to wikipedia,   "+ info)
        elif "open youtube" in query:
            speak("kholti hun,  lekin itna youtube nahi dekhna chahiye")
            webbrowser.open("www.youtube.com")
        elif "yourself" in query:
            speak("ab apni main kya hi taareef karun")
            speak("i am Ava, Anmol's virtual assistant")
            speak("i am a very smart artificial intelligence")
        elif "open facebook" in query:
            speak("opening facebook......")
            webbrowser.open("www.facebook.com")
        elif "open google" in query:
            speak("what should i be searching for......")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
        elif "send message on whatsapp" in query:
            speak("what message should i add......")
            msg = takecommand().lower()
            speak("to whom's number should i be sending this message......")
            num = int(takecommand().lower())
            speak("sending message......")
            pywhatkit.sendwhatmsg(f"+91{num}",f"{msg}",2,25)
        elif "open steam" in query:
            speak("opening steam store......")
            stpath = "C:\\Program Files (x86)\\Steam\\Steam.exe"
            os.startfile(stpath)
        elif "open epic games" in query:
            egpath = "E:\\EPIC GAMES STORE\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"
            speak("opening epic games store")
            os.startfile(egpath)
        elif "open watch dogs" in query:
            wdpath = "E:\\EPIC GAMES STORE\\Watchdogs2\\Installer\\autorun.exe"
            speak("opening game......")
            os.startfile(wdpath)
        elif "open gta" in query:
            gtapath = "E:\\EPIC GAMES STORE\\GTAV\\PlayGTAV.exe"
            speak("opening game......")
            os.startfile(gtapath)
        elif "open marvel avengers" in query:
            mapath = "E:\\SteamLibrary\\steamapps\\common\\Marvels Avengers\\avengers.exe"
            speak("opening game......")
            os.startfile(mapath)
        elif "open injustice" in query:
            inpath = "E:\\SteamLibrary\\steamapps\\common\\Injustice2\\Binaries\\Retail\\Injustice2.exe"
            speak("opening game......")
            os.startfile(inpath)
        elif "open teams" in query:
            tpath = "C:\\Users\\bhaya\\AppData\\Local\\Microsoft\\Teams\\current\\Teams.exe"
            speak("opening app......")
            os.startfile(tpath)
        elif "play song on youtube" in query:
            speak("which song to search for......")
            sng = takecommand().lower()
            pywhatkit.playonyt(f"{sng}")
        elif "send email" in query:
            try:
                speak("what message should i add......")
                content = takecommand().lower()
                speak("who should i send it to......")
                to = takecommand()
                sendEmail(to, content)
                speak("sending email......")
            except Exception as e:
                print(e)
                speak("sorry, email could not be sent")
        elif "calculate" in query:
            webbrowser.open(f"{query}")
        elif "shutdown" in query:
            speak("good day sir")
            sys.exit()
        elif "quit" in query:
            speak("good day sir")
            sys.exit()
        elif "no thanks" in query:
            speak("good day sir")
            sys.exit()
        elif "you can leave" in query:
            speak("good day sir")
            sys.exit()
        else:
            speak("i did not understand, please repeat")