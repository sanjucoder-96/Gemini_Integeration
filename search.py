import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import requests
import re
import webbrowser

def open_link(query):
    webbrowser.open(f"https://{query}")

def search_youtube(query):
    try:
        query=query.replace(' ','+')
        link= f"https://www.youtube.com/results?search_query={query}"
        r = requests.get(link)
        
        if r.status_code != 200:
            return "youtube search failed."
        video_ids = re.findall(r"watch\?v=(\S{11})", r.text)

        first_video= f"https://www.youtube.com/watch?v={video_ids[0]}"
        webbrowser.open(first_video)
        return f"playing the top result for {query} on youtube."
    
    except Exception as e:
        print(f"Error: {e}")
        return "search failed some error occured."