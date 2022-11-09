import EnterEvent
import datetime
import DatetimeEventStore

# les packages a installer : pymongo, tdqm

# Fonction main pour lancer l'application
if __name__ == '__main__':
    print(datetime.datetime.now())

    # Initialization de userInput
    userInput = ""

    #Boucle pour le menu
    while userInput != "exit":

        # Menu principal
        print()
        print("Veuillez choisir une des options ci-dessous :")
        print("1 : Ajouter un event a la base de données")
        print("2 : Récupérer des events")
        print("3 : Afficher toutes les entrées")
        print("4 : Générer des entrées")
        print("5 : Vider la BDD")
        print("exit : Sortie de l'application")
        userInput = input("Votre choix : ")
        print()

        # Ajouter l'event a la base de donnees
        if userInput == "1":

            event = EnterEvent.enterEvent()
            DatetimeEventStore.store_event(event)

        # Saisie d'un event
        elif userInput == "2":
            print("\nSaisissez la date de début de la recherche : ")
            x, startDate, startTime = EnterEvent.enterDateTime()
            print("\nSaisissez la date de fin de la recherche : ")
            x, endDate, endTime = EnterEvent.enterDateTime()
            # Recherche de la BDD
            DatetimeEventStore.get_events(startDate, startTime, endDate, endTime)

        # Afficher tout les events
        elif userInput == "3":
            # Tout afficher
            DatetimeEventStore.get_all_events()

        # Generation aleatoire des events
        elif userInput == "4":
            DatetimeEventStore.generateEvent()

        # Suppression de tout events
        elif userInput == "5":
            DatetimeEventStore.clearEvents()

        else:
            print("Choix erroné. Veuillez choisir une des options citées dans le menu")

