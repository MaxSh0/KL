from pymongo import MongoClient
import datetime

client = MongoClient()
client = MongoClient("mongodb://R15EN:dfhbhjuyfcjhju@clusternews-shard-00-00-gbs8l.mongodb.net:27017,clusternews-shard-00-01-gbs8l.mongodb.net:27017,clusternews-shard-00-02-gbs8l.mongodb.net:27017/test?ssl=true&replicaSet=ClusterNews-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.News
data = db.News.find({})
with open('documents/text_db.txt', 'w') as f: 
    for i in data:
        wow = i["Text"]    
        f.write(''.join(wow))

    