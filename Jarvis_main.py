import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening .....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, timeout=15, phrase_time_limit=10)

    try:
        print("Understanding.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(f"Error: {e}")
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from greetME import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "goodbye" in query:
                    speak("Goodbye sir!")
                    break

                elif "hello" in query:
                    speak("Hello sir!, How are you doing?")
                elif "i am fine" in query:
                    speak("That's great to hear sir!")
                elif "how are you" in query:
                    speak("I'm perfect sir!")
                elif "thank you" in query:
                    speak("You're welcome sir!")

                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                elif "temperature" in query:
                    search = "temperature in Naya Raipur"
                    url = f"https://search.brave.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe iBp4i AP7Wnd").text
                    speak(f"current {search} is {temp}")
                elif "weather" in query:
                    search = "temperature in Naya Raipur"
                    url = f"https://search.brave.com/search?q={search}"
                    search = "temperature in Naya Raipur"
                    url = f"https://www.google.com/search?q={search}"
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current {search} is {temp}")