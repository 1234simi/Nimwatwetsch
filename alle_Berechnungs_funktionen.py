## Tested
def operations_zeichen_eingabe():
    """
    Eingabe Aufforderung (str) zeichen
    :return: (str) zeichen
    """
    ## input ist immer vom typ 'str'
    zeichen = input("Bitte gib das Operations-Zeichen ein: ")
    return zeichen

## Tested
def operations_zeichen_auswertung(zeichen: str):
    """
    Je nach Länge von der Eingabe wird eine Liste erstellt, die Eingabe wird in ascii umgewandelt und
    alle Leerzeichen werden aus der Eingabe herausgelöscht
        :param zeichen: (str) liste
        :return: (list[ascii int]) ohne Leerzeichen
    """
    ## Je nach Länge von der Eingabe wird eine Liste erstellt, die Eingabe wird in ascii umgewandelt
    zeichen_liste = []
    for i in range(len(zeichen)):
        # print(ord(zeichen[i]))
        zeichen_liste.append(ord(zeichen[i]))

    ### Alle Leerzeichen werden aus der Eingabe herausgelöscht
    zeichen_liste_real = []
    ## Ascii 32 = Leerzeichen
    for j in range(len(zeichen_liste)):
        if (zeichen_liste[j] != 32):
            zeichen_liste_real.append(zeichen_liste[j])
    # print(f"Zeichen_liste_real: {zeichen_liste_real}")
    return zeichen_liste_real



## Tested
def operations_zeichen_valid(zeichen_liste_real):
    if (len(zeichen_liste_real) == 1):
        ### Prüfen, ob das Operations-Zeichen valid ist
        ## Zeichen in ASCII-Code umwandeln
        ascii_zeichen = int(zeichen_liste_real[0])
        print(f"Operations-Zeichen: {chr(ascii_zeichen)}")
        if ascii_zeichen == 42 or ascii_zeichen == 43 or ascii_zeichen == 45 or ascii_zeichen == 47:
            zeichen = ascii_zeichen
            return zeichen
        else:
            return -1

    if (len(zeichen_liste_real) >= 1):
        ganzzahl_division_true = []
        counter = 0
        for i in range(len(zeichen_liste_real)):
            if (zeichen_liste_real[i] == 47):
                ganzzahl_division_true.append("True")
                counter += 1
        if len(zeichen_liste_real) == 2 and counter == 2:
            print("Operations-Zeichen: //")
            ## Es wird ein '~' zurückgegeben
            return 126
        else:
            return -1
    # ascii()
    #     +    -   *   /   ~
    #     43, 45, 42, 47, 126


## Tested
def addition(zahl_1, zahl_2):
    return zahl_1 + zahl_2


def subtraktion(zahl_1, zahl_2):
    return zahl_1 - zahl_2


def multiplikation(zahl_1, zahl_2):
    return zahl_1 * zahl_2


def division(zahl_1, zahl_2):
    ### Achtung, division durch 0 möglich! --> Abfangen
    try:
        result = zahl_1 / zahl_2
    except ZeroDivisionError:
        raise ZeroDivisionError("Durch Null Teilen ist nicht definiert")
    else:
        return result


def ganzzahl_division(zahl_1, zahl_2):
    try:
        return zahl_1 // zahl_2
    except ZeroDivisionError:
        raise ZeroDivisionError("Durch Null Teilen ist nicht definiert")
    # else:
    #     return result


## Tested
def berechnungen_machen(zahl_1, zeichen, zahl_2):
    # print(type(zeichen))
    ## Ascii code zu Ascii str umwandeln
    if (type(zeichen) == int):
        zeichen = chr(zeichen)
        # print(f"ASCII str = {zeichen}")
    else:
        ...
    #todo: evt löschen?

    ### Operstionen auswählen:
    if (zeichen == '*'):
        result = multiplikation(zahl_1, zahl_2)

    elif (zeichen == '+'):
        result = addition(zahl_1, zahl_2)

    elif (zeichen == '-'):
        result = subtraktion(zahl_1, zahl_2)

    elif (zeichen == '/'):
        result = division(zahl_1, zahl_2)

    elif (zeichen == '~'):
        result = ganzzahl_division(zahl_1, zahl_2)

    else:
        print("Keine Rechenoperation möglich")
        result = 'NaN'

    return result


## Tested
def ausgabe_trenner(zeichen):
    # print(type(zeichen))
    ## Ascii code zu Ascii str umwandeln
    if (type(zeichen) == int):
        zeichen = chr(zeichen)
    else:
        ...
    # print(type(zeichen))
    if (zeichen == '+'):
        trenner = "++"
    elif (zeichen == '-'):
        trenner = "--"
    elif (zeichen == '*'):
        trenner = "**"
    elif (zeichen == '/'):
        trenner = "/_"
    elif (zeichen == '~'):
        trenner = "//"
    else:
        trenner = "%%"
    return trenner


#todo: test schreiben
def ausgabe_resultat(resultat, trenner, zeichen, zahl_1, zahl_2):
    ## Ausgabe von den eingegebenen Werten
    if zeichen == 126:
        # print(f'({zahl_1} // {zahl_2} = {resultat})')
        titel = f"Das Resultat lautet: {zahl_1} // {zahl_2} = {resultat} "
    else:
        # print(f'({zahl_1} {chr(zeichen)} {zahl_2} = {resultat})')
        titel = f'Das Resultat lautet: {zahl_1} {chr(zeichen)} {zahl_2} = {resultat}'

    ## // = Nur durch eine Ganzzahl teilen
    trenner_length = len(titel) // len(trenner)
    ## Die Schluss-Ausgabe wird gemacht, mit den jeweiligen operationszeichen ober- und unterhalb vom Resultat
    print(f'\n{trenner_length * trenner}\n{titel}\n{trenner_length * trenner}')
