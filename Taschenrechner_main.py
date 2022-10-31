# =============================================================================
# Taschenrechner
# =============================================================================

def eingaben_machen():
    ### Die Zahlen und das Operations-Zeichen wird eingegeben
    zahl_1 = input("Bitte gib die Erste Zahl ein: ")
    zeichen = operations_zeichen_eingabe()
    zahl_2 = input("Bitte gib die Zweite Zahl ein: ")

    ### Die Eingaben werden ausgegeben
    print("Zahl 1: ", zahl_1)
    print("Zahl 2: ", zahl_2)

    ## Es wird geprüft, ob das Operations-Zeichen valid ist
    zeichen = operations_zeichen_valid(zeichen)
    print("Operations-Zeichen: ", zeichen)

    ## es wird die erste Zahl geprüft 
    # zahl_1 = zahl_1_valid(zahl_1)

    # Die beiden Zahlen und das Operations_Symbol werden zurückgegeben
    return float(zahl_1), zeichen, float(zahl_2)





def operations_zeichen_eingabe():
    zeichen = input("Bitte gib das Operations-Zeichen ein: ")
    zeichen_liste = []
    for i in range(len(zeichen)):
        # print(ord(zeichen[i]))
        zeichen_liste.append(ord(zeichen[i]))

    zeichen_liste_real = []
    for j in range(len(zeichen_liste)):
        if (zeichen_liste[j] != 32):
            zeichen_liste_real.append(zeichen_liste[j])
    print(f"Zeichen_liste_real: {zeichen_liste_real}")
    return zeichen_liste_real


def operations_zeichen_valid(zeichen_liste_real):
    if(len(zeichen_liste_real) == 1):
        ### Prüfen, ob das Operations-Zeichen valid ist
        ## Zeichen in ASCII-Code umwandeln
        ascii_zeichen = int(zeichen_liste_real[0])
        if ascii_zeichen == 42 or ascii_zeichen == 43 or ascii_zeichen == 45 or ascii_zeichen == 47:
            zeichen = ascii_zeichen
            return zeichen
        else:
            print(f"\tDas Operations-Zeichen ist nicht valide!")
            print("\tBitte die Eingabe Wiederholen!")
            zeichen = operations_zeichen_eingabe()
            zeichen = operations_zeichen_valid(zeichen)
            return zeichen
    if (len(zeichen_liste_real) >= 1):
        pass

# def zahl_1_valid(zahl1):
#     zahlvalid = zahl1



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
    # print(type(zeichen))
    ## Ascii code zu Ascii str umwandeln
    if (type(zeichen) == int):
        zeichen = chr(zeichen)
    else:
        pass



    ### Operstionen auswählen:
    if (zeichen == '*'):
        result = multiplikation(zahl_1, zahl_2)

    elif (zeichen == '+'):
        result = addition(zahl_1, zahl_2)

    elif (zeichen == '-'):
        result = subtraktion(zahl_1, zahl_2)

    elif (zeichen == '/'):
        result = division(zahl_1, zahl_2)

    else:
        print("Keine Rechenoperation möglich")
        result = 'NaN'

    return result

def ausgabe_trenner(zeichen):
    # print(type(zeichen))
    ## Ascii code zu Ascii str umwandeln
    if (type(zeichen) == int):
        zeichen = chr(zeichen)
    else:
        pass

    print(type(zeichen))
    if (zeichen == '+'):
        trenner = "++"
    elif (zeichen == '-'):
        trenner = "--"
    elif (zeichen == '*'):
        trenner = "**"
    elif (zeichen == '/'):
        trenner = "//"
    else:
        trenner = "%%"
    return trenner



def ausgabe_resultat(resultat, trenner):
    titel = f"Das Resultat lautet: {float(resultat)} "
    ## // = Nur durch eine Ganzzahl teilen
    trenner_length = len(titel) // len(trenner)
    print(f"\n{trenner_length * trenner}\n{titel}\n{trenner_length * trenner}")


# =============================================================================
# Main Programm beginnt:
# =============================================================================
if __name__ == '__main__':
    # Zuerst wird die Eingabe gemacht
    zahl_1, zeichen, zahl_2 = eingaben_machen()


    # Danach werden die Berechnungen durchgeführt
    resultat = berechnungen_machen(zahl_1, zeichen, zahl_2)

    #Je nach Operations-Zeichen wird die Ausgaben andest sein
    trenner = ausgabe_trenner(zeichen)
    ## Das Resultat mit dem jeweiligen Trenner wird ausgegeben
    ausgabe_resultat(resultat, trenner)
    print("hallo")