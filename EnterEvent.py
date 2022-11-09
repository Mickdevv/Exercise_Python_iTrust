import validationDateTime
from DatetimeEventStore import Event


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


def enterEvent():
    eventTitle = input("Titre de l'evenement : ")
    while eventTitle == "":
        eventTitle = input("Titre de l'evenement : ")
        print("Ce champ est obligatoire. \n")

    eventLocation = input("Ou se situe l'evenement ? ")
    while eventLocation == "":
        eventLocation = input("Ou se situe l'evenement ? ")
        print("Ce champ est obligatoire. \n")

    print("Quand se passe l'evenement ?")

    eventDateTime, eventDate, eventTime = enterDateTime()
    eventTimestamp, eventDateTime = validationDateTime.datetimeToTimestamp(eventDate, eventTime)


    print("Title : " + eventTitle + " | Location : " + eventLocation + " | dateTime : " + str(eventDateTime) + " | Timestamp : " + str(eventTimestamp))

    return Event(eventDateTime, eventTitle, eventLocation, eventTimestamp)
