import validationDateTime
from DatetimeEventStore import Event


# Fonction de saisie des infos de date et heure de l'event
def enterDateTime():
    # Validation de la date
    eventDate = input("Date (YYYY-MM-DD) : ")
    while not validationDateTime.validateDate(eventDate):
        eventDate = input("Date (YYYY-MM-DD) : ")

    # Validation de l'heure
    eventTime = input("Time (HH:MM:SS) : ")
    while not validationDateTime.validateTime(eventTime):
        eventTime = input("Time (HH:MM:SS) : ")

    return str(eventDate + " " + eventTime), eventDate, eventTime


# Fonction globale pour la saisie et ajout a la BDD d'un event
def enterEvent():
    # Boucle validation saisie du titre (ne pas laisser vide)
    eventTitle = input("Titre de l'event : ")
    while eventTitle == "":
        eventTitle = input("Titre de l'event : ")
        print("Ce champ est obligatoire. \n")

    # Boucle validation saisie de la localisation (ne pas laisser vide)
    eventLocation = input("Ou se situe l'event ? ")
    while eventLocation == "":
        eventLocation = input("Ou se situe l'event ? ")
        print("Ce champ est obligatoire. \n")

    print("Quand se passe l'event ?")

    # Fonction de saisie de la date et heure de l'event
    eventDateTime, eventDate, eventTime = enterDateTime()
    # Generation d'un timestamp de l'event pour les fonction ou une comparaison est necessaire
    eventTimestamp, eventDateTime = validationDateTime.datetimeToTimestamp(eventDate, eventTime)

    # Montrer les infos saisie
    print("Titre : " + eventTitle + " | Localisation : " + eventLocation + " | dateTime : " + str(
        eventDateTime) + " | Timestamp : " + str(eventTimestamp))

    return Event(eventDateTime, eventTitle, eventLocation, eventTimestamp)
