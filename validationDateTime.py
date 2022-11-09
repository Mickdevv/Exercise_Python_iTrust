import datetime


def datetimeToTimestamp(date, time):
    dateArray = date.split("-")
    timeArray = time.split(":")
    print(timeArray)
    dtime = datetime.datetime(int(dateArray[0]), int(dateArray[1]), int(dateArray[2]), int(timeArray[0]),
                              int(timeArray[1]), int(timeArray[2]))
    print()
    return dtime.timestamp().__int__(), dtime


def validateDate(date):
    try:
        # Separation des valeurs dans le string
        if date[4] == "-" and date[7] == "-":
            dateArray = date.split("-")

            # Validation de l'annee. L'utilisateur peux ajouter des evenements au passe comme au futur
            if 1950 <= int(dateArray[0]) <= 2050:
                if len(dateArray[0]) == 4:
                    pass
                else:
                    print("(DA0) Erreur : veuillez saisir la date dans le format suivant : YYYY-MM-DD")
                    return False
            else:
                print("La date selectionee est trop loin")
                return False
            # Validation du mois
            if 1 <= int(dateArray[1]) <= 12 and len(dateArray[1]) == 2 and 1 <= int(dateArray[2]) <= 31 and len(
                    dateArray[2]) == 2:
                pass
            else:
                return False
        else:
            print("(-) Erreur : veuillez saisir la date dans le format suivant : YYYY-MM-DD")
            return False

    except:
        print("(Int) Erreur de validation de la date. Veuillez la saisir en utilisant le format suivant : YYYY-MM-DD")
        return False

    return True


def validateTime(time):
    try:
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
