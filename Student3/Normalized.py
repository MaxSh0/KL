import nltk
import pymorphy2
import gensim
import random
import re, string
import pandas as pd
from nltk import FreqDist
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import classify
from nltk import NaiveBayesClassifier
from pymongo import MongoClient

PositiveTwits = pd.read_csv('positive.csv', sep = ';')
PositiveTwitsText = PositiveTwits.drop(PositiveTwits.columns[[0,1,2,4,5,6,7,8,9,10,11]], axis='columns')
PositiveTwitsText = PositiveTwitsText[0:100000]
PositiveTwitsText.columns = ['PosText']

NegativeTwits = pd.read_csv('negative.csv', sep = ';')
NegativeTwitsText = NegativeTwits.drop(NegativeTwits.columns[[0,1,2,4,5,6,7,8,9,10,11]], axis='columns')
NegativeTwitsText = NegativeTwitsText[0:100000]
NegativeTwitsText.columns = ['NegText']


# получаем экземпляр класса MorphAnalyzer
morph = pymorphy2.MorphAnalyzer()

def tokenize_ru (text):
    # разбиваем на слова
    tokens = word_tokenize(text)

    # удаляем пунктуацию
    tokens = [i for i in tokens if (i not in string.punctuation)]

    # удаляем русские стоп слова
    stop_words = stopwords.words('russian')
    tokens = [i for i in tokens if (i not in stop_words)]

    # чистим токены от кавычек
    tokens = [i.replace("«", "").replace("»", "") for i in tokens]

    cleaned_tokens = []
    for token in tokens:
        #отчищаем от ссылок
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', token)
        # отчищаем от отметок пользователей
        token = re.sub("(@[A-Za-z0-9_]+)", "", token)
        # отчищаем от английских слов
        token = re.sub("([A-Za-z]+)", "", token)
        # отчищаем от небуквенных и числовых символов
        token = re.sub("\W+", "", token)
        # отчищаем от цифр
        token = re.sub("\d+", "", token)
        # отчищаем от знаков подчеркивания
        token = re.sub("_+", "", token)
        cleaned_tokens.append(token)
    cleaned_tokens = [i for i in cleaned_tokens if (len(i) > 0)]
    return  cleaned_tokens


def norm_sent(text):
    norm_text = []
    text = tokenize_ru(text)
    for word in text:
        norm_text.append(normalize_ru(word))
    return norm_text

# функция для нормализации одного слова при помощи библиотеки pymorphy2
def normalize_ru(word):
    word_norm = morph.parse(word)[0]
    return word_norm.normal_form



# функция которая нормализует текст разбитый на токены
def Normalize_tokens (All_token_text):
    NumTwit = 0
    NormalizeTwitsText = []
    for twit in All_token_text :
        NumTwit+=1
        print('Обрабатываем твит №', NumTwit)
        token_text = tokenize_ru(twit)
        normalize_text = []
        for token in token_text:
            normalize_text.append(normalize_ru(token))
        NormalizeTwitsText.append(normalize_text)
    return NormalizeTwitsText

#функция которая возвращает все токены одним объектом
def get_all_words(cleaned_tokens_list):
    for tokens in cleaned_tokens_list:
        for token in tokens:
            yield token

print("Нормализированный текст:", Normalize_tokens(PositiveTwitsText['PosText'].values))

#разбиваем на токены и нормализуем считанные данные
NormalizePositiveTwitsText = Normalize_tokens(PositiveTwitsText['PosText'].values)
NormalizeNegativeTwitsText = Normalize_tokens(NegativeTwitsText['NegText'].values)

#Считываем все слова и выводим в консоль наиболее часто повторяющиеся из них для каждого типа твитов
all_pos_words = get_all_words(NormalizePositiveTwitsText)
all_neg_words = get_all_words(NormalizeNegativeTwitsText)

freq_dist_pos=FreqDist(all_pos_words)
freq_dist_neg=FreqDist(all_neg_words)

print("Позитивные ",freq_dist_pos.most_common(20))
print("Негативные ",freq_dist_neg.most_common(20))

# функция для преобразования данных которые понимает модель
def get_tweets_for_model(cleaned_tokens_list):
    for tweet_tokens in cleaned_tokens_list:
        yield dict([token,True]for token in tweet_tokens)

positive_tokens_for_model=get_tweets_for_model(NormalizePositiveTwitsText)
negative_tokens_for_model=get_tweets_for_model(NormalizeNegativeTwitsText)

# прикрепляем метки к твитам в датасете
positive_dataset=[(tweet_dict,"Positive") for tweet_dict in positive_tokens_for_model]
negative_dataset=[(tweet_dict,"Negative") for tweet_dict in negative_tokens_for_model]

# объединяем датасет
dataset=positive_dataset+negative_dataset

# перемешиваем чтобы избавиться от последовательности
random.shuffle(dataset)

# устанавливаем размеры тестовой и обучающей выборки
train_data=dataset[:150000]
test_data=dataset[50000:]


#Обучение модели
classifier = NaiveBayesClassifier.train(train_data)

print("Accuracy is:", classify.accuracy(classifier, test_data))
print(classifier.show_most_informative_features(50))

# Подключаемся к базе данных
client = MongoClient()
client = MongoClient("mongodb://Nastya:20041999a@clusternews-shard-00-00-gbs8l.mongodb.net:27017,clusternews-shard-00-01-gbs8l.mongodb.net:27017,clusternews-shard-00-02-gbs8l.mongodb.net:27017/test?ssl=true&replicaSet=ClusterNews-shard-0&authSource=admin&retryWrites=true&w=majority")
# Получаем базу данных новостей
db = client.News


for text in db.PersonsAttractions.find():
    # Токенезируем текст из БД
    custom_tokens = norm_sent(text['Text'])
    # Создаем запись для БД
    record = {
        'Text': text['Text'],
        'Tonality': classifier.classify(dict([token, True] for token in custom_tokens))}
    # Записываем тональность и БД если данное предложение раньше не анализировалось
    if(db.PersonsAttractions.find({'Text':record['Text']})):
        {
            db.Tonality.insert_one(record)
        }



