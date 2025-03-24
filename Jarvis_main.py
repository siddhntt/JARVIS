import datetime
import os
import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import pyautogui
import random



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening .....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)
    try:
        print("Understanding.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(f"Error: {e}")
        speak("I didn't catch that. Could you please repeat?")
        print("Say that again please...")
        return "None"
    return query


def alarm(query):
    os.startfile("alarm.py")


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
                elif "good job" in query:
                    speak("I am happy that you liked it sir!")
                elif "how are you" in query or "how r u" in query:
                    speak("I'm perfect sir!")
                elif "thank you" in query or "thanks" in query or "thank u" in query or "thankyou" in query:
                    speak("You're welcome sir!")
                

                # elif "tired" in query:
                #     speak("Playing your favourite songs sir!")
                #     a = (1,2,3)
                #     b = random.choice(a)
                #     if b == 1:
                #         os.startfile("music1.mp3")

                

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("Paused sir!")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("Playing sir!")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("Muted sir!")
                elif "unmute" in query:
                    pyautogui.press("m")
                    speak("Unmuted sir!")
                elif "volume up" in query:
                    from keyboard import volumeup
                    volumeup()
                    speak("Volume increased sir!")
                elif "volume down" in query:
                    from keyboard import volumedown
                    volumedown()
                    speak("Volume decreased sir!")

# Want to add same things for Spotify


                


                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeapp
                    closeapp(query)



                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                elif "news" in query:
                    from news import latestnews
                    latestnews()


                elif "temperature" in query:
                     speak("Please tell me the location for which you want to know the temperature.")
                     location = takeCommand().lower()
                     search = f"temperature in {location}"
                     url = f"https://search.brave.com/search?q={search}"
                     r = requests.get(url)
                     data = BeautifulSoup(r.text, "html.parser")
                     temp_element = data.find("div", class_="temps-current t-primary svelte-15dg5t9 desktop-heading-h1")  

                     if temp_element:
                        temp = temp_element.text
                        speak(f"The current temperature in {location} is {temp}")
                     else:
                        speak(f"Sorry, I couldn't find anything for {search}.")
                
                elif "set an alarm" in query:
                    print("Input time example: 15:15:15")
                    speak("What time do you want to set the alarm for?")
                    alarm(query)
                    speak("Alarm set sir!")


                elif "time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")

                elif "sleep" in query:
                    speak("going to sleep sir!")
                    exit()


                elif "remember that" in query:
                    remembermessage = query.replace("remember that", "")
                    remembermessage = remembermessage.replace("jarvis", "")
                    speak("You told me" + remembermessage)
                    remember = open("Remember.txt", "w")
                    remember.write(remembermessage)
                    remember.close() 
                elif "what do you remember" in query:
                    remember = open("Remember.txt", "r")
                    speak("You told me" + remember.read())
                    remember.close()