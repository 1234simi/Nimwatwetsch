# https://www.geeksforgeeks.org/python-docstrings/

def ditcty_zahlen_soll_int():
    """
        Dictionary mit den jeweilig-gültigen Ziffern 0 bis 9 und, auch mit '.' und '-'
            :return: (dict) --> {int: str}
        """
    return {48: '0', 49: '1', 50: '2', 51: '3', 52: '4', 53: '5', 54: '6', 55: '7',
            56: '8', 57: '9', 46: '.', 45: '-'}


def zahl_eingabe():
    """
    Aufforderung eine Zahl einzugeben mit input()
        :return: (str) zahl_eingabe
    """
    zahl_eingabe = input("Zahl eingeben: ")
    return zahl_eingabe


def zahl_eingabe_valid(zahl_eingabe):
    """
    Die eingegebene Zahl wird geprüft. Dafür wird die 'zahl_eingabe' in ascii umgewandelt,
    wenn es sich bei der Eingabe um eine Ziffer oder einen '.' handelt wird diese in die Liste aufgenommen.
    Falls etwas anderes erkennt wurde, wird ein False zurückgegeben.
        :param zahl_eingabe: (str)
        :return: (list) or (False)
    """
    ## Die Eingabe wird in eine Liste abgefüllt und in ascii umgewandelt
    zeichen_liste = []
    for i in range(len(zahl_eingabe)):
        zahl_ascii = ord(zahl_eingabe[i])
        if zahl_ascii in ditcty_zahlen_soll_int().keys():
            zeichen_liste.append(zahl_ascii)
        else:
            return False
    return zeichen_liste


def zahl_eingabe_valid_to_float(zeichen_liste):
    """
    Falls mehrere '.' oder '-' nach einander folgen wird nur das Erste Zeichen übernommen.
    Zum Schluss wird eine Umwandlung in float vorgenommen.
        :param zeichen_liste: (list)
        :return: (float) Zahl, (bool) null_flag --> if 0.0 == True
    """
    null_flag = False
    zeichen_liste_real = []
    flag_punkt = False
    flag_minus = False

    for i in range(len(zeichen_liste)):
        ## Falls mehrere '.' oder '-' nach einander folgen wird nur das Erste Zeichen übernommen
        # if (not flag_punkt or zeichen_liste[i] != 46 or zeichen_liste[i] != 45 or not flag_minus):

        # Nur der Erste '.' wird übernommen
        if (zeichen_liste[i] == 46):
            if not flag_punkt:
                zeichen_liste_real.append(chr(zeichen_liste[i]))
                flag_punkt = True
            else:
                flag_punkt = True

        # Nur das Erste '-' wird übernommen
        elif (zeichen_liste[i] == 45):
            if not flag_minus:
                zeichen_liste_real.append(chr(zeichen_liste[i]))
                flag_minus = True
            else:
                flag_minus = True

        else:
            zeichen_liste_real.append(chr(zeichen_liste[i]))

    # Die Listen Elemente werden zusammengefügt
    trenner = ""
    zeichen_liste_real_str = trenner.join(zeichen_liste_real)

    # umwandeln von 'str' to 'float'
    try:
        # string to float
        zahl_eingabe_float = float(zeichen_liste_real_str)
        # print(f'zeichen_liste float: {zahl_eingabe_float}')
    except ValueError:
        print('ValueError, converting to (float) not valid')
        return False, False

    else:
        # Die Zahl wird als float zurückgegeben
        if zahl_eingabe_float == 0.0:
            null_flag = True
            return zahl_eingabe_float, null_flag
        else:
            return zahl_eingabe_float, null_flag


def zahl_eingabe_real():
    """
    Zusammenfassung von allen 'Zahlen-Eingabe-Funktionen', von der Eingabe über die validierung bis zur Rückgabe.
    Falls die Funktion 'zahl_eingabe_valid(zahl_eingabe)' ein 'False' zurückgibt,
    wird die Eingabe noch einmal wiederholt.
        :return: (float) zahl
    """

    z_1 = zahl_eingabe()

    y_1 = zahl_eingabe_valid(z_1)

    # Falls die eingegebene Zahl nicht nur gültige Ziffern, bez. Zeichen beinhaltet, wird die Eingabe wiederholt
    if not y_1:
        null_flag = False
        zahl_1 = False
        while not y_1 and not null_flag or not zahl_1 and not null_flag:
            z_1 = zahl_eingabe()
            y_1 = zahl_eingabe_valid(z_1)
            # Dieses Error-handling ist nötig, weil es sein kann, dass ein 'False'
            # in die Funktion 'zahl_eingabe_valid_to_float' gelangen kann
            try:
                zahl_1, null_flag = zahl_eingabe_valid_to_float(y_1)
            except TypeError:
                zahl_1 = False
    # Wenn die eingegebenen Ziffern bez. Zeichen gültig waren werden sie nun in folat umgewandelt
    else:
        try:
            zahl_1, null_flag = zahl_eingabe_valid_to_float(y_1)
        except TypeError:
            zahl_1 = False
            null_flag = False

        if not zahl_1 and not null_flag:
            while not y_1 and not null_flag or not zahl_1 and not null_flag:
                z_1 = zahl_eingabe()
                y_1 = zahl_eingabe_valid(z_1)
                # Dieses Error-handling ist Nötig, weil es sein kann, dass ein 'False'
                # in die Funktion 'zahl_eingabe_valid_to_float' gelangen kann
                try:
                    zahl_1, null_flag = zahl_eingabe_valid_to_float(y_1)
                except TypeError:
                    zahl_1 = False

    print(f'\t Eingabe gültig --> {zahl_1}')
    return zahl_1


if __name__ == '__main__':
    help(zahl_eingabe)
    help(zahl_eingabe_valid)
    help(zahl_eingabe_valid_to_float)
    help(zahl_eingabe_real)
