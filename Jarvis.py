import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser as wb
eng=pyttsx3.init()
def speak(audio):
    eng.say(audio)
    eng.runAndWait()
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)
def Date():
    year = int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak(month)
    speak(year)
    speak(day)
def wishme():
    hour=datetime.datetime.now().hour
    speak("Welcome back")
    if hour>=6 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<17:
        speak("Good afternoon")
    elif hour>=17 and hour<19:
        speak("Good evening")
    else:
        speak("Good night")
    speak("How can i help you")
#wishme()
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognising...")
        query=r.recognize_google(audio,language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("say it again")
        return "None"
    return query
if __name__=="__main__":
    wishme()
    while True:
        query=takecommand().lower()
        if "time" in query:
            time()
        elif "date" in query:
            Date()
        elif "wikipedia" in query:
            speak("searching...")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        elif "play songs" in query:
            songsdir="B:\\songs"
            songs=os.listdir(songsdir)
            os.startfile(os.path.join(songsdir,songs[0]))
        elif "search in chrome" in query:
            speak("What should i search ")
            chromepath="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search=takecommand().lower()
            wb.get(chromepath).open_new_tab(search+".com")
        elif "offline" in query:
            quit()