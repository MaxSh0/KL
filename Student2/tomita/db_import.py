#import re
from pymongo import MongoClient

client = MongoClient()
client = MongoClient("mongodb://R15EN:dfhbhjuyfcjhju@clusternews-shard-00-00-gbs8l.mongodb.net:27017,clusternews-shard-00-01-gbs8l.mongodb.net:27017,clusternews-shard-00-02-gbs8l.mongodb.net:27017/test?ssl=true&replicaSet=ClusterNews-shard-0&authSource=admin&retryWrites=true&w=majority")
# Получаем базу данных новостей
db = client.News
i = 1
line1 =''
line2 =''
line3 =''
with open('documents/text.txt') as f:
    lines = f.readlines()
    for line in lines:        
        if i == 1:
            line1 = line
            line1 = line1[0:-1]
            i=i+1
            continue
        elif i == 2:
            line2 = line
            line2 = line2[0:-1]
            i=i+1
            continue
        elif i == 3:
            line3 = line
            line3 = line3[0:-1]
            i = 1
        # Экземпляр записи
        new = {                    
                    'Text': line1,
                    'Persona': line2,
                    'Attraction': line3
                }
        # Сама запись в БД
        db.PersonsAttractions.insert_one(new)
       

