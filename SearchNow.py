import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening .....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

query = takeCommand().lower()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis", "")
        query = query.replace("google", "")
        query = query.replace("google search", "")
        speak("This is what I found on the web")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query, 1)
            speak(result)

        except:
            speak("I'm sorry, I couldn't find anything on the web")

def searchYoutube(query):
    if "youtube" in query:
        query = query.replace("jarvis", "")
        query = query.replace("youtube", "")
        query = query.replace("search", "")
        speak("Here is what I found on youtube")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("I hope you found what you were looking for")

def searchWikipedia(query):
    if "wikipedia" in query:
        query = query.replace("jarvis", "")
        query = query.replace("wikipedia", "")
        query = query.replace("search", "")
        speak("This is what I found on wikipedia")
        results = wikipedia.summary(query, sentences = 1)
        print(results)
        speak(results)