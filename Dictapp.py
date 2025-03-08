import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictapp = {"commandprompt": "cmd", "notepad": "notepad", "chrome": "chrome", "paint":"paint", "word":"winword", "excel":"excel", "vscode":"code", "calculator":"calc", "camera":"start microsoft.windows.camera:", "calendar":"start outlookcal:", "mail":"start outlookmail:", "edge":"msedge", "firefox":"firefox", "whatsapp":"whatsapp", "telegram":"telegram", "zoom":"zoom", "teams":"teams", "skype":"skype", "instagram":"instagram", "facebook":"facebook", "linkedin":"linkedin", "twitter":"twitter", "youtube":"youtube", "spotify":"spotify", "netflix":"netflix", "prime":"primevideo", "hotstar":"hotstar", "amazon":"amazon", "flipkart":"flipkart", "snapdeal":"snapdeal", "myntra":"myntra", "paytm":"paytm", "phonepe":"phonepe", "google":"google", "bing":"bing", "duckduckgo":"duckduckgo", "yahoo":"yahoo", "wikipedia":"wikipedia", "github":"github", "stackoverflow":"stackoverflow", "geeksforgeeks":"geeksforgeeks", "hackerrank":"hackerrank", "hackerearth":"hackerearth", "codechef":"codechef", "codeforces":"codeforces", "atcoder":"atcoder", "leetcode":"leetcode", "gfg":"geeksforgeeks", "github": "github"}

def openappweb(query):
    speak(f"Launching sir!")
    if ".com" in query or ".in" in query or ".org" in query:
        query = query.replace("open", "")
        query = query.replace("jarvis", "")
        query = query.replace("launch", "")
        query = query.replace(" ", "")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")
def closeapp(query):
    speak(f"Closing {query} for you!")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs are closed!")
    elif "two tab" in query or "2 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs are closed!")
    elif "three tab" in query or "3 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs are closed!")
    elif "four tab" in query or "4 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs are closed!")
    elif "five tab" in query or "5 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs are closed!")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
            
