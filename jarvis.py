import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os


engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1])#engine.setproperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<16:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am here to help you sir please tell me how may i help you")
def takecommand():
    #it will take microphone input from the user and will run it
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        r.pause_threshold = .5
        
        audio = r.listen(source)
    try:
        print('recognizing')
        query = r.recognize_google(audio, language='en-in')
        print('user said:',query)
    except Exception as e:
        print("Say that again")
        return "None"
    return query
    pass
if __name__ == "__main__":
    wishme()
    while True:

        query = takecommand().lower()
        if 'wikipedia' in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=2)
            speak(results)
            print(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "play music" in query:
            music_dir = "C:\\Users\\vnind\\Desktop\\songs\\all tym fav"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[6]))
        elif "the time" in query:
            str=datetime.datetime.now().strftime("%H:%M:%S")
            print(str)
            speak(f"sir...the time is{str}")
        elif "friend" in query:
            str1="puorvi tiwari from jhannnnsi is your very good  friend from GLA university"
            print(str1)
            speak(str1)
        elif "goodbye" in query:
            str="good bye sir......have a great day ahead....thanks for using me"
            speak(str)
            break
        elif "open code" in query:
            path="C:\\Users\\vnind\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        elif "open whatsapp" in query:
            path="C:\\Users\\vnind\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(path)

        elif "fun" in query:
            try:
                speak("lets have fun....sir.....speak a word or sentence")
                while True:
                    speak("now speak")
                    content=takecommand()
                    speak(content)
                    speak("you got a great logic sir.........")
                    if content=="bye":
                        break
            except:
                speak("sorry.....something went wrong")
        elif "favourite sweet" in query:
            str="rabbbbdi and maaalpuaaa is her favourite sweet that tooooooo from brijjjjjwasiiiiiiii shop"
 
            print(str)
            speak(str)
        
