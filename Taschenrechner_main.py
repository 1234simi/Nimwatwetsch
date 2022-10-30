# =============================================================================
# Taschenrechner
# =============================================================================


def eingaben_machen():
    ### Die Zahlen und das Operations-Zeichen wird eingegeben
    zahl_1 = input("Bitte gib die Erste Zahl ein: ")
    zeichen = input("Bitte gib das Operations-Zeichen ein: ")
    zahl_2 = input("Bitte gib die Zweite Zahl ein: ")

    ### Die Eingaben werden ausgegeben
    print("Zahl 1: ", zahl_1)
    print("Zahl 2: ", zahl_2)

    ## Es wird geprüft, ob das Operations-Zeichen valid ist
    zeichen = operations_zeichen_valid(zeichen)

    # Die beiden Zahlen und das Operations_Symbol werden zurückgegeben
    return float(zahl_1), zeichen, float(zahl_2)


def operations_zeichen_valid(zeichen: str):
    ### Prüfen, ob das Operations-Zeichen valid ist
    ascii_zeichen = ord(zeichen)
    # print(ascii_zeichen)
    if (ascii_zeichen == 42 or ascii_zeichen == 43 or ascii_zeichen == 45 or ascii_zeichen == 47):
        print("Das Operations-Zeichen ist valide!")
        print("Das Operations-Zeichen ist: ", zeichen)
    else:
        print("Das Operations-Zeichen ist nicht valide!")
        return False

    print("Datentyp zahl_1:", type(zeichen))
    return zeichen


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

def berechnungen_machen(zahl_1, zeichen, zahl_2):

    ### Operstionen auswählen:
    if (ord(zeichen) == 42):
        # print("Multiplikation")
        result = multiplikation(zahl_1, zahl_2)

    elif (ord(zeichen) == 43):
        # print("Addition")
        result = addition(zahl_1, zahl_2)

    elif (ord(zeichen) == 45):
        # print("Subtraktion")
        result = subtraktion(zahl_1, zahl_2)

    elif (ord(zeichen) == 47):
        # print("Division")
        result = division(zahl_1, zahl_2)

    else:
        print("Keine Rechenoperation möglich")
        result = 'NaN'

    return result, zeichen



# =============================================================================
# Main Programm beginnt:
# =============================================================================
if __name__ == '__main__':
    # Zuerst wird die Eingabe gemacht
    zahl_1, zeichen, zahl_2 = eingaben_machen()

    # Danach werden die Berechnungen durchgeführt
    result, zeichen = berechnungen_machen(zahl_1, zeichen, zahl_2)
    print(" ")

    if zeichen == '+':
        trenner = "++"
    if zeichen == '-':
        trenner = "--"

    titel = f"Das Resultat lautet {float(result)} "
    # trenner = "++"
    ## // = Nur durch eine Ganzzahl teilen
    trenner_length = len(titel) // len(trenner)
    print(f"\n{trenner_length * trenner}\n{titel}\n{trenner_length * trenner}")

    # print(f"\tDas Resultat lautet: {float(result)}")

