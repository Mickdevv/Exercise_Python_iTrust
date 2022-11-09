import datetime
from tqdm import tqdm
from pymongo import MongoClient
import random

import validationDateTime


class Event:
    def __init__(self, dateTime, title, location, timestamp):
        self.DateTime = dateTime
        self.Title = title
        self.Location = location
        self.Timestamp = timestamp


# Connexion a la BDD
def connectDB():
    cluster = MongoClient("mongodb+srv://mickdevv:Kitty-man3@cluster0.kv0ycs0.mongodb.net/?retryWrites=true&w=majority")
    db = cluster["DatetimeEventStore"]
    collection = db["Events"]

    return collection


# Stockage d'un event
def store_event(event):
    # Connexion a la BDD
    collection = connectDB()

    # Ajouter event a la BDD
    post = {"Title": event.Title, "Location": event.Location, "DateTime": event.DateTime, "Timestamp": event.Timestamp}
    collection.insert_one(post)


# Recherche d'events
def get_events(startDate, startTime, endDate, endTime):
    # Connexion a la BDD
    collection = connectDB()

    # Demander a l'utilisateur d'entrer le creneau cible, puis conversion en timestamp pour la comparaison
    startTS, x = validationDateTime.datetimeToTimestamp(startDate, startTime)
    endTS, x = validationDateTime.datetimeToTimestamp(endDate, endTime)

    # Boucle pour parcourir la BDD pour des events correspondants
    for event in collection.find():
        if int(startTS) <= int(event["Timestamp"]) <= int(endTS):
            print(event)


# Montrer tous les events dans la BDD
def get_all_events():
    # Connexion a la BDD
    collection = connectDB()

    # Montrer toute la BDD
    for event in collection.find():
        print(event)


# Generation des events
def generateEvent():
    # Initialisation du variable pour stocker la quantite de donnees a generer
    amount = 0

    # Boucle pour saisie des donnees
    while 1 > int(amount) or int(amount) > 100 or amount == '0':
        try:
            amount = input("Veuillez specifier la quantite d'events a generer (max 100): ")
        except:
            print("Erreur : saisie non valide")

    # Boucle de generation. Les donnees sont generees aleatoirement
    for i in tqdm(range(0, int(amount))):
        eventTitle = "Title" + str(random.randint(0, 10000))
        eventLocation = "Location" + str(random.randint(0, 10000))
        eventDateTime = datetime.datetime.now().replace(random.randint(1950, 2050), random.randint(1, 12),
                                                        random.randint(1, 28))
        eventTimestamp = eventDateTime.timestamp()

        # Stockage de l'event dans la BDD
        store_event(Event(eventDateTime, eventTitle, eventLocation, eventTimestamp))


# Vidange de la BDD
def clearEvents():
    # Etape de verification pour eviter des pertes accidentaux de donnees
    verification = input("Etes-vous sur (Y/N) ? ")

    # Boucle de validation de la saisie
    while verification != "Y" and verification != "y" and verification != "N" and verification != "n":
        print("Veuillez reessayer")
        verification = input("Etes-vous sur (Y/N) ? ")
    if verification == "y" or verification == "Y":
        # Connexion a la BDD
        collection = connectDB()

        # Recherche et suppression des donnees
        d = collection.find()
        for document in d:
            print(document)
            collection.delete_one({"_id": document["_id"]})
