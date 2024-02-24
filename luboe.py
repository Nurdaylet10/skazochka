import requests
from bs4 import BeautifulSoup


headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
           'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}

req = requests.get('https://www.gismeteo.kz/weather-semey-5192/3-days/', headers=headers)

soup = BeautifulSoup(req.content, 'lxml')

temp = soup.findAll(class_='unit unit_temperature_c')
wind = soup.findAll(class_='wind-unit unit unit_wind_m_s')
if temp[3].text[0] == '+':
    print('Сегодня в городе Семей',temp[3].text.replace('+',''),'градусов тепла.Ветер',wind[42].text,'метров в секунду')
else:
    print('Сегодня в городе Семей',temp[3].text.replace('+',''),'градуса ниже нуля.Ветер',wind[42].text,'метров в секунду')

headers2 = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'User-Agent': 'User-Agent:'}