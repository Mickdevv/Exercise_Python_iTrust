import validationDateTime
from EventClass import Event

def enterEvent():
    eventTitle = input("Titre de l'evenement : ")
    eventlocation = input("Ou se situe l'evenement ? ")
    print("Quand se passe l'evenement ?")

    # Validation de la date
    eventDate = input("Date (YYYY-MM-DD) : ")
    while not validationDateTime.validateDate(eventDate):
        eventDate = input("Date (YYYY-MM-DD) : ")

    # Validation de l'heure
    eventTime = input("Time (HH:MM:SS) : ")
    while not validationDateTime.validateTime(eventTime):
        eventTime = input("Time (HH:MM:SS) : ")

    eventDateTime = (eventDate + " " + eventTime)

    print("Title : " + eventTitle + " | Location : " + eventlocation + " | dateTime : " + eventDateTime)

    return Event(eventDateTime, eventTitle, eventlocation)