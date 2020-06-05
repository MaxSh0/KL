const express = require('express');
const app = express();
app.use('/', express.static('./public'));
const MongoClient = require('mongodb').MongoClient;

async function start() {
    const port = process.env.port || 3000;
    try {
        await app.listen(port);
        console.log('Server started on ' + port + ' port');
    } catch (err) {
        console.log('Server not started with error: ${err}');
    }
}
start().catch(console.error);

let dbClient;

//Подключаемся к БД
const uri = "mongodb+srv://Max:maxim1999@clusternews-gbs8l.mongodb.net/test?retryWrites=true&w=majority";
const mongoClient = new MongoClient(uri, { useNewUrlParser: true });
mongoClient.connect(function(err, client) {
    dbClient = client;
    app.locals.collectionNews = client.db("News").collection("News");
    app.locals.collectionPersonsAttractions = client.db("News").collection("PersonsAttractions");
    app.locals.collectionTonality = client.db("News").collection("Tonality");
    if (err) return console.log(err);
    console.log("Соединение с БД установлено")
});


app.get("/News", function(req, res) {
    const collection = app.locals.collectionNews;
    collection.find({}).toArray(function(err, News) {

        if (err) return console.log(err);
        res.send(News)
    });
})

app.get("/PersonsAttractions", function(req, res) {
    const collection = app.locals.collectionPersonsAttractions;
    collection.find({}).toArray(function(err, PersonsAttractions) {

        if (err) return console.log(err);
        res.send(PersonsAttractions)
    });
})

app.get("/Tonality", function(req, res) {
    const collection = app.locals.collectionTonality;
    collection.find({}).toArray(function(err, Tonality) {

        if (err) return console.log(err);
        res.send(Tonality)
    });
})

process.on("SIGINT", () => {
    dbClient.close();
    process.exit();
});