import datetime


def datetimeToTimestamp(date, time):
    # Séparation de la date et heure en liste pour vérification individus des éléments
    dateArray = date.split("-")
    timeArray = time.split(":")

    # Conversion entype datetime.datetime
    dtime = datetime.datetime(int(dateArray[0]), int(dateArray[1]), int(dateArray[2]), int(timeArray[0]),
                              int(timeArray[1]), int(timeArray[2]))
    return dtime.timestamp().__int__(), dtime


# Fonction de validation de la date saisie par l'utilisateur
def validateDate(date):
    try:
        # Séparation des valeurs dans le string
        if date[4] == "-" and date[7] == "-":
            dateArray = date.split("-")

            # Validation de l'année. L'utilisateur peux ajouter des events au passé comme au futur
            if 1950 <= int(dateArray[0]) <= 2050:
                if len(dateArray[0]) == 4:
                    pass
                else:
                    print("(DA0) Erreur : veuillez saisir la date dans le format suivant : YYYY-MM-DD")
                    return False
            else:
                print("La date sélectionée est trop loin")
                return False
            # Validation du mois
            if 1 <= int(dateArray[1]) <= 12 and len(dateArray[1]) == 2 and 1 <= int(dateArray[2]) <= 31 and len(
                    dateArray[2]) == 2:
                pass
            else:
                return False
        else:
            print("Erreur : veuillez saisir la date dans le format suivant : YYYY-MM-DD")
            return False

    except:
        print("Erreur de validation de la date. Veuillez la saisir en utilisant le format suivant : YYYY-MM-DD")
        return False

    return True

# Fonction de validation de l'heure saisie par l'utilisateur
def validateTime(time):
    try:
        # Séparation de l'heure en éléments individus pour validation
        if time[2] == ":" and time[5] == ":":
            timeArray = time.split(":")

            try:
                # Validation de l'heure
                if 0 <= int(timeArray[0]) <= 23 and 0 <= int(timeArray[1]) <= 59 and 0 <= int(timeArray[2]) <= 59:
                    pass
                else:
                    print("Erreur : veuillez saisir l'heure dans le format suivant : HH:MM:SS")
                    return False

            except:
                print("Erreur : veuillez saisir l'heure dans le format suivant : HH:MM:SS")
                return False

        else:
            print("Erreur : veuillez saisir l'heure dans le format suivant : HH:MM:SS")
            return False

    except:
        print("Erreur : veuillez saisir l'heure dans le format suivant : HH:MM:SS")
        return False

    return True
