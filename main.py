import time
import gemini
import pyttsx3
import speech_recognition as sr
import requests
import os
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 
engine.setProperty('rate', 160)
engine.setProperty('volume', 1.0)
NEWSAPI_KEY=os.getenv("NEWSAPI_KEY")
def news():

    r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWSAPI_KEY}")
    if r.status_code == 200:
        raw_data = r.json()
        headlines = raw_data.get("articles", [])
        for i, headlines in enumerate(headlines[:10], 1):
                speak(f"{i}. {headlines['title']}")
    else:
        print(f"Error news could not be fetched: {r.status_code}")
def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()
if __name__=="__main__":
    
    output=gemini.gemini_ai("open griet website")
    speak(output)
