import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import datetime
import os
import pygame

class Aru:
    def today(self):
        d = datetime.datetime.today().strftime("%d-%m-%Y-%H-%M").split('-')
        w = datetime.date.today()
        week = datetime.datetime.weekday(w)
        weeks = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
        today = 'Сегодня {}'.format(d[0], d[1], d[2], weeks[week])
        tts = gTTS(text=today, lang='ru')
        tts.save("output.mp3")
        pygame.mixer.init()
        # Initialize pygame mixer here
        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    def time(self):
        d = datetime.datetime.today().strftime("%d-%m-%Y-%H-%M").split('-')
        vremya = 'сейчас время {}, {}!'.format(d[3], d[4])
        tts = gTTS(text=vremya, lang='ru')
        tts.save("output2.mp3")
        pygame.mixer.init()
        # Initialize pygame mixer here
        pygame.mixer.music.load("output2.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    def privetstvie(self):
        hello = 'Здравствуйте!'
        tts = gTTS(text=hello, lang='ru')
        tts.save("output3.mp3")
        pygame.mixer.init()
        # Initialize pygame mixer here
        pygame.mixer.music.load("output3.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    def affairs(self):
        affairs = 'Хорошо, а у вас как?'
        tts = gTTS(text=affairs, lang='ru')
        tts.save("output4.mp3")
        pygame.mixer.init()
        # Initialize pygame mixer here
        pygame.mixer.music.load("output4.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    def song(self):
        song = 'Уютноеее кааааафеееееееее на улицах с плетённной мебелью ,Где красное винооооо из местных погребов больших Шато ,Ты можешь говоооорииииить, что это только глупые мечты ,Но в планах у мееееееняя всё видимо немного круче, ведь ,Завтра в семь двадцать две, я буду в Борисполе ,Сидеть в самолёте и думать о пилоте ,Чтобы он хорошо взлетел и крайне удачно сел ,Где-нибудь в Париже, а там ещё немного и - Прованс'
        tts = gTTS(text=song, lang='ru')
        tts.save("output5.mp3")
        pygame.mixer.init()
        # Initialize pygame mixer here
        pygame.mixer.music.load("output5.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    def temp(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}

        req = requests.get('https://www.gismeteo.kz/weather-semey-5192/3-days/', headers=headers)

        soup = BeautifulSoup(req.content, 'lxml')

        temp = soup.findAll(class_='unit unit_temperature_c')
        wind = soup.findAll(class_='wind-unit unit unit_wind_m_s')
        if temp[3].text[0] == '+':
            text1 = 'Сегодня в городе Семей', temp[3].text.replace('+', ''), 'градусов тепла.Ветер', wind[42].text,'метров в секунду'
        else:
            text1 = 'Сегодня в городе Семей', temp[3].text.replace('+', ''), 'градуса ниже нуля.Ветер', wind[42].text,'метров в секунду'
        tts = gTTS(text=str(text1), lang='ru')
        tts.save("output6.mp3")
        pygame.mixer.init()
        # Initialize pygame mixer here
        pygame.mixer.music.load("output6.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    def news(self):
        req = requests.get('https://tengrinews.kz')
        soup = BeautifulSoup(req.content, 'lxml')  # 'html.parser'

        last_news = soup.findAll(class_='main-news_top_item_title')
        massive_news = {}

        for news in last_news:
            title = news.findNext('a')
            href = title.attrs.get('href')
            if not href.startswith('https://tengrinews.kz'):  # if href[0:4] == 'https:'
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
            count += 1

    def tale(self):
        req = requests.get('https://deti-online.com/skazki/russkie-narodnye-skazki/kolobok/')
        soup = BeautifulSoup(req.content, 'lxml')
        skazka_tail = soup.findAll(class_='folded')
        tts = gTTS(text=str(skazka_tail[0].text), lang='ru')
        tts.save("output8.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load("output8.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.quit()  #Close the pygame mixer
        #Remove the file now that it's no longer in use
        if os.path.exists("output.mp3"):
            os.remove("output.mp3")

