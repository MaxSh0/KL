import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import warnings
import re
warnings.filterwarnings('ignore')

# Подключаемся к базе данных
client = MongoClient()
client = MongoClient("mongodb://Max:maxim1999@clusternews-shard-00-00-gbs8l.mongodb.net:27017,clusternews-shard-00-01-gbs8l.mongodb.net:27017,clusternews-shard-00-02-gbs8l.mongodb.net:27017/test?ssl=true&replicaSet=ClusterNews-shard-0&authSource=admin&retryWrites=true&w=majority")
# Получаем базу данных новостей
db = client.News

# URL для ленты новостей о политике
URL_politics = 'https://gorvesti.ru/politics'
# URL для ленты новостей о благоустройстве
URL_blagoustr = 'https://gorvesti.ru/blagoustr'
# Заголовки которые передаются серверу
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36', 'accept': '*/*'}
# хост
HOST = "https://gorvesti.ru/"

# функция которая возвращает html разметку
def get_html(url,params = None):
    r = requests.get(url, headers = HEADERS, params = params)
    return r

# функция которая получает контент и заносит его в БД
def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find('article', class_='feed news').find_all('div', class_="itm")

    for item in items:
        new = {
            'Header': item.find('h2').get_text(),
            'Time':item.find('span',class_="dt").get_text(strip=True),
            'Link':HOST + item.find('a').findNext('a').get('href'),
            'Text': get_main_text(HOST + item.find('a').findNext('a').get('href'))
        }
        if(db.News.find({'Header':new['Header']}).count() == 0): #Записываем новость в БД только если новости с таким заголовком еще нет
            {
                db.News.insert_one(new)
            }




# Функция которая возвращает текст новости со страницы
def get_main_text(URL):
    html = get_html(URL)
    soup = BeautifulSoup(html.text, 'html.parser')
    AllText = soup.find('article',class_='block item news').findAll('p')
    text = ''
    for i in range(1,len(AllText)-1):
        text += AllText[i].get_text(strip=True)+' '
    #Разбиваем текст на отдельные предложения
    split_regex = re.compile(r'[.|!|?|…|:]')
    text = filter(lambda t: t, [t.strip() for t in split_regex.split(text)])
    sents = []
    for s in text:
        sents.append(s);
    return sents

# функция парсинга
def parse():
    page_count = 10;
    # Парсим 10 страниц с новостями о политике
    for page in range(1, page_count+1):
        print(f'Парсинг страницы о политике {page} из {page_count}...')
        html = get_html(URL_politics+f'/{page}')
        get_content(html.text)

    #Парсим 10 страниц с новостями о благоустройстве
    for page in range(1,page_count+1):
        print(f'Парсинг страницы о благоустройстве {page} из {page_count}...')
        html = get_html(URL_blagoustr + f'/{page}')
        get_content(html.text)

parse()