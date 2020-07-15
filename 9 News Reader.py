import urllib.request as urlr
import json
from gtts import gTTS
import os
import time

url = urlr.urlopen('https://newsapi.org/v2/top-headlines?country=us&apiKey=dc3fa72c4d1c4ec9901f46e5bfbdc823')
Json_news_byte = url.read()
Json_news = json.loads(Json_news_byte.decode())

for i in range(len(Json_news)):
    a = "Headline no "+ str(i+1) +" is:\n"
    f = open("News file","a")
    f.write(a)

    b = Json_news["articles"][i]["title"]
    f.write(b)
    f.write("\n")

f.close()

f1 = open("News file","r")
news = f1.read()

news_output = gTTS(text=news,lang='en',slow=False)
news_output.save("news_output.mp3")
os.system("start news_output.mp3")
f1.close()

time.sleep(30)

f2 = open("News file","r+")
f2.truncate(0)
f2.close()
#os.remove("News file")






















