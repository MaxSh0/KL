#import re
from pymongo import MongoClient

client = MongoClient()
client = MongoClient("mongodb://R15EN:dfhbhjuyfcjhju@clusternews-shard-00-00-gbs8l.mongodb.net:27017,clusternews-shard-00-01-gbs8l.mongodb.net:27017,clusternews-shard-00-02-gbs8l.mongodb.net:27017/test?ssl=true&replicaSet=ClusterNews-shard-0&authSource=admin&retryWrites=true&w=majority")
# Получаем базу данных новостей
db = client.News

db.PersonsAttractions.remove({})
       

