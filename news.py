import requests
import json
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    api_dict = {
               "business":"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=a1e439f139654f3481fefea4a7d3ae7b", 
               "entertainment":"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=a1e439f139654f3481fefea4a7d3ae7b", 
               "health":"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=a1e439f139654f3481fefea4a7d3ae7b", 
               "science":"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=a1e439f139654f3481fefea4a7d3ae7b", 
               "sports":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=a1e439f139654f3481fefea4a7d3ae7b", 
               "technology":"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=a1e439f139654f3481fefea4a7d3ae7b"}
    content = None
    url = None
    speak("Which category of news would you like to hear? Business, Entertainment, Health, Science, Sports or Technology?")
    while True:
        query = input("Which category of news would you like to hear? Business, Entertainment, Health, Science, Sports or Technology? ").lower()
        if query in api_dict:
            url = api_dict[query]
            break
        else:
            speak("I didn't catch that. Could you please repeat?")

    news  = requests.get(url).text
    news_dict = json.loads(news)
    speak("Here is the first news headline")
    arts = news_dict['articles']
    for article in arts:
        article = article['title']
        print(article)
        speak(article)
        news_url = article['url']
        print(f"For more information, visit: {news_url}")
        speak(f"For more information, visit: {news_url}")

        a = input("[press 1 to continue], [press 0 to stop]")
        if str(a) == "0":
            break
        elif str(a) == "1":
            pass
        
        speak("That's all for now")

