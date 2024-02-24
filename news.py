import requests
from bs4 import BeautifulSoup
import pygame
from gtts import gTTS

req = requests.get('https://tengrinews.kz')
soup = BeautifulSoup(req.content,'lxml')#'html.parser'

last_news = soup.findAll(class_='main-news_top_item_title')
massive_news = {}

for news in last_news:
    title = news.findNext('a')
    href = title.attrs.get('href')
    if not href.startswith('https://tengrinews.kz'): #if href[0:4] == 'https:'
        massive_news[title.text] = 'https://tengrinews.kz' + href
    else:
        massive_news[title.text] = href
    if len(massive_news) == 5:
        break
count = 7
for n in massive_news.keys():
    tts = gTTS(text=str(n), lang='ru')
    tts.save(f"output{count}.mp3")
    pygame.mixer.init()
    # Initialize pygame mixer here
    pygame.mixer.music.load(f"output{count}.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    count+= 1
#zapros = input('Новость которую хотите послушать:')

#if zapros in massive_news:
    #req = requests.get(massive_news[zapros])
    #soup = BeautifulSoup(req.content,'lxml')
    #texts = soup.findAll('p')
    #news_text = []
    #for t in texts:
        #news_text.append(t.text)
    #for x in range(3,7):
        #print(news_text[x])

