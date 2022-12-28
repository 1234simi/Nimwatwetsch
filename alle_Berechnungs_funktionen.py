## Tested

def dicty_operations_zeichen_soll_int():
    """
    Alle gültigen Operations-Zeichen sind in einem Dictionary gespeichert
        :return: (dict) --> {int: str}
    """
    return {43: '+', 45: '-', 42: '*', 47: '/'}


def operations_zeichen_eingabe():
    """
    Aufforderung ein Operations-Zeichen einzugeben mit input()
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
        if zeichen_liste[j] != 32:
            zeichen_liste_real.append(zeichen_liste[j])
    return zeichen_liste_real


## Tested
def operations_zeichen_valid(zeichen_liste_real):
    """
    Die Funktion prüft, ob die Eingabe ein valides Operationszeichen ist, mit einer Umwandlung in ascii.
    Wenn die Länge vom Input >1 ist, wird geprüft, ob es sich um '//' handelt.
    Falls die Eingabe ungültig ist, wird ein '-1' zurückgegeben.

        :param zeichen_liste_real: (list)
        :return: (ascii_int) 42, 43, 45, 47, 126 or -1 (False)
    """
    if len(zeichen_liste_real) == 1:
        ### Prüfen, ob das Operations-Zeichen valid ist
        ## Zeichen in ASCII-Code umwandeln
        ascii_zeichen = int(zeichen_liste_real[0])
        print(f"\tOperations-Zeichen --> {chr(ascii_zeichen)}")

        if ascii_zeichen in dicty_operations_zeichen_soll_int().keys():
            zeichen = ascii_zeichen
            return zeichen
        else:
            return -1

    if len(zeichen_liste_real) >= 1:
        ganzzahl_division_true = []
        counter = 0
        for i in range(len(zeichen_liste_real)):
            if zeichen_liste_real[i] == 47:
                ganzzahl_division_true.append("True")
                counter += 1
        if len(zeichen_liste_real) == 2 and counter == 2:
            print("\tOperations-Zeichen --> //")
            ## Es wird ein '~' zurückgegeben
            return 126
        else:
            return -1
    # ascii()
    #     +    -   *   /   ~
    #     43, 45, 42, 47, 126


## Tested
def addition(zahl_1, zahl_2):
    """
    Addition von 2 Zahlen.
        :param zahl_1: (float)
        :param zahl_2: (float)
        :return: (float)
    """
    return zahl_1 + zahl_2


def subtraktion(zahl_1, zahl_2):
    """
    Subtraktion von 2 Zahlen.
        :param zahl_1: (float)
        :param zahl_2: (float)
        :return: (float)
    """
    return zahl_1 - zahl_2


def multiplikation(zahl_1, zahl_2):
    """
    Multiplikation von 2 Zahlen.
        :param zahl_1: (float)
        :param zahl_2: (float)
        :return: (float)
    """
    return zahl_1 * zahl_2


def division(zahl_1, zahl_2):
    """
    Division von 2 Zahlen.
    Achtung, division durch 0 möglich! --> Abfangen mit error handling
        :param zahl_1: (float)
        :param zahl_2: (float)
        :return: (float)
    """
    ### Achtung, division durch 0 möglich! --> Abfangen
    try:
        result = zahl_1 / zahl_2
    except ZeroDivisionError:
        raise ZeroDivisionError("Durch Null Teilen ist nicht definiert")
    else:
        return result


def ganzzahl_division(zahl_1, zahl_2):
    """
    Ganzzahl-Division von 2 Zahlen.
    Achtung, division durch 0 möglich! --> Abfangen mit error handling
        :param zahl_1: (float)
        :param zahl_2: (float)
        :return: (float)
    """
    try:
        return zahl_1 // zahl_2
    except ZeroDivisionError:
        raise ZeroDivisionError("Durch Null Teilen ist nicht definiert")
    # else:
    #     return result


def berechnungen_machen(zahl_1, zeichen, zahl_2):
    """
    Diese Funktion führt die Berechnung von den beiden Zahlen aus, je nach dem welches Operations-Zeichen gewählt wurde,
    wird eine andere Berechnungs-Funktion aufgerufen.
    Falls das Operations-Zeichen nicht vorhanden ist, wird 'NaN' zurückgegeben
        :param zahl_1: (float)
        :param zeichen: (ascii_int) -> 42, 43, 45, 47, 126
        :param zahl_2: (float)
        :return: (float) resultat or 'NaN'
    """
    ## Ascii code zu Ascii str umwandeln
    if type(zeichen) == int:
        zeichen = chr(zeichen)

    elif type(zeichen) == str:
        zeichen = zeichen
    else:
        print("Keine Rechenoperation möglich")
        result = 'NaN'
        return result

    # Operstionen auswählen:
    if zeichen == '*':
        result = multiplikation(zahl_1, zahl_2)

    elif zeichen == '+':
        result = addition(zahl_1, zahl_2)

    elif zeichen == '-':
        result = subtraktion(zahl_1, zahl_2)

    elif zeichen == '/':
        result = division(zahl_1, zahl_2)

    elif zeichen == '~':
        result = ganzzahl_division(zahl_1, zahl_2)

    else:
        print("Keine Rechenoperation möglich")
        result = 'NaN'

    return result


def ausgabe_trenner(zeichen):
    """
    Je nach Operations-Zeichen wird ein anderes 'Schluss-Zeichen' zurückgegeben.
    Dieses 'Schluss-Zeichen' um das Schluss-Resultat benötigt, als Verzierung :-)
        :param zeichen: (ascii_int) -> 42, 43, 45, 47, 126
        :return: (str) ++, --, **, /_, // or %%
    """
    # print(type(zeichen))
    ## Ascii code zu Ascii str umwandeln
    if type(zeichen) == int:
        zeichen = chr(zeichen)
    else:
        print(f'Fehler bei der Funktion "ausgabe_trenner"!')
        trenner = "%%"
        return trenner
    # print(type(zeichen))
    if zeichen == '+':
        trenner = "++"
    elif zeichen == '-':
        trenner = "--"
    elif zeichen == '*':
        trenner = "**"
    elif zeichen == '/':
        trenner = "/_"
    elif zeichen == '~':
        trenner = "//"
    else:
        trenner = "%%"
    return trenner


def ausgabe_resultat(resultat: float, trenner: str, zeichen: int, zahl_1: float, zahl_2: float):
    """
    Diese Funktion Printet die Berechnung mit dem Resultat. Um den Text wird der 'trenner' ausgegeben
        :param resultat: (float)
        :param trenner: (str) ++, --, **, /_, // or %%
        :param zeichen: (ascii_int) -> 42, 43, 45, 47, 126
        :param zahl_1: (float)
        :param zahl_2: (float)
        :return: True --> alles in Ordnung or False --> exception geworfen

    """
    ## Ausgabe von den eingegebenen Werten
    if zeichen == 126:
        # print(f'({zahl_1} // {zahl_2} = {resultat})')
        titel = f"Das Resultat lautet: {zahl_1} // {zahl_2} = {resultat} "
    else:
        # Es wird im Dictionary geschaut, ob das Operationszeichen vorkommt
        if zeichen in dicty_operations_zeichen_soll_int().keys():
            # print(f'({zahl_1} {chr(zeichen)} {zahl_2} = {resultat})')
            titel = f'Das Resultat lautet: {zahl_1} {chr(zeichen)} {zahl_2} = {resultat}'
        else:
            return False

    ## // = Nur durch eine Ganzzahl teilen
    trenner_length = len(titel) // len(trenner)
    ## Die Schluss-Ausgabe wird gemacht, mit den jeweiligen operationszeichen ober- und unterhalb vom Resultat
    print(f'\n{trenner_length * trenner}\n{titel}\n{trenner_length * trenner}')
    return True


if __name__ == '__main__':
    help(operations_zeichen_eingabe)
    help(operations_zeichen_auswertung)
    help(operations_zeichen_valid)
    help(addition)
    help(subtraktion)
    help(multiplikation)
    help(division)
    help(ganzzahl_division)
    help(berechnungen_machen)
    help(ausgabe_trenner)
    help(ausgabe_resultat)
