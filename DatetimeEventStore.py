import datetime

from pymongo import MongoClient
import random

import validationDateTime


class Event:
    def __init__(self, dateTime, title, location, timestamp):
        self.DateTime = dateTime
        self.Title = title
        self.Location = location
        self.Timestamp = timestamp


def connectDB():
    cluster = MongoClient("mongodb+srv://mickdevv:Kitty-man3@cluster0.kv0ycs0.mongodb.net/?retryWrites=true&w=majority")
    db = cluster["DatetimeEventStore"]
    collection = db["Events"]

    return collection


def store_event(event):
    # Connexion a la BDD
    collection = connectDB()

    # Ajouter event a la BDD
    post = {"Title": event.Title, "Location": event.Location, "DateTime": event.DateTime, "Timestamp": event.Timestamp}
    collection.insert_one(post)

    print("Event ajoute a la BDD")


def get_events(startDate, startTime, endDate, endTime):
    # Connexion a la BDD
    collection = connectDB()

    startTS = validationDateTime.datetimeToTimestamp(startDate, startTime)
    endTS = validationDateTime.datetimeToTimestamp(endDate, endTime)
    for event in collection.find():
        if startTS <= int(event["Timestamp"]) <= endTS:
            print(event)
    print(1)


def get_all_events():
    # Connexion a la BDD
    collection = connectDB()
    for event in collection.find():
        print(event)


def generateEvent():
    amount = 0
    while 1 > int(amount) or int(amount) > 100 or amount == '0':
        try:
            amount = input("Veuillez specifier la quantite d'events a generer (max 100): ")
        except:
            print("Erreur : saisie non valide")

    for i in range(int(amount)):
        eventTitle = "Title" + str(random.randint(0, 10000))
        eventLocation = "Location" + str(random.randint(0, 10000))
        eventDateTime = datetime.datetime.now().replace(random.randint(1950, 2050), random.randint(1, 12),
                                                        random.randint(0, 23))
        eventTimestamp = eventDateTime.timestamp()
        store_event(Event(eventDateTime, eventTitle, eventLocation, eventTimestamp))


def clearEvents():
    # Connexion a la BDD
    collection = connectDB()

    d = collection.find()
    for document in d:
        print(document)
        collection.delete_one({"_id": document["_id"]})
    #print(d + " Documents supprimes !")
