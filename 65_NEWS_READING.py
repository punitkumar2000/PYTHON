import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    print("News for today.. Lets begin")
    speak("News for today.. Lets begin")
    print("NEWS ARE AS FOLLOWS")
    speak("NEWS ARE AS FOLLOWS")
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=07c1d60a29ac4d6cb7bda40fa363e949"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    for article in arts:
        speak("listen carefully!")
        print(article['title'])
        speak(article['title'])
        speak("FOR MORE INFORMATION CLICK ON THE LINK:")
        print(article['url'])

    speak("Thanks for listening...")


