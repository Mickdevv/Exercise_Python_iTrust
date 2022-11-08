import DBManagement
import EnterEvent
import EventClass
import sys
import datetime
import DBManagement as DB

import validationDateTime

if __name__ == '__main__':
    print(datetime.datetime.now())

    # Initialization de userInput
    userInput = ""

    #Boucle pour le menu
    while userInput != "exit":

        # Montrer menu principal
        print()
        print("Veuillez choisir une des options ci-dessous :")
        print("1 : Ajouter un evenement a la base de donnees")
        print("2 : Recuperer des evenements")
        print("3 : Afficher toutes les entrees")
        print("4 : Generer des entrees")
        userInput = input("Votre choix : ")
        print()

        if userInput == "1":
            # Ajouter l'evenement a la base de donnees
            DB.store_event(EnterEvent.enterEvent())

        if userInput == "2":
            # Recherche de la BDD
            pass

        if userInput == "3":
            # Tout afficher
            pass

        if userInput == "4":
            # Generation aleatoire des entrees
            pass

        else:
            print("Choix errone. Veuillez choisir une des options citees dans le menu")

    # elif len(sys.argv == 3):
    #     if sys.argv[0] == 0:
    #         #Ajouter un evenement
    #         x=1
    #     elif sys.argv[0] == 1:
    #         #Recuperer un evenement
    #         x=1
    #     else:
    #         print("Arguments invalides. Voici la syntaxe attendue : main.py argument1 argument2 argument3")
    #         print("argument1 represente si vous voulez ajouter ou recuperer un evenement de la BDD. Entrez 0 pour ajouter, 1 pour recuperer.")
    #         print("")
