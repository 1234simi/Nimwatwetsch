# =============================================================================
# Taschenrechner
# =============================================================================


def eingaben_machen():
    ### Die Zahlen und das Operations-Zeichen wird eingegeben
    zahl_1 = input("Bitte gib die Erste Zahl ein: ")
    zeichen = input("Bitte gib das Operations-Zeichen ein: ")
    zahl_2 = input("Bitte gib die Zweite Zahl ein: ")
    print(" ")

    ### Die Eingaben werden ausgegeben
    print("Zahl 1: ", zahl_1)
    print("Das Operations-Zeichen ist: ", zeichen)
    print("Zahl 2: ", zahl_2)


    # Die beiden Zahlen und das Operations_Symbol werden zurückgegeben
    return zahl_1, zeichen, zahl_2





def berechnungen_machen (zahl_1, zeichen, zahl_2):
    print(" ")
    print("Die Berechnungen werden durchgeführt!")
    
    ### Die Eingaben werden ausgegeben
    print("Zahl 1: ", zahl_1)
    print("Das Operations-Zeichen ist: ", zeichen)
    print("Zahl 2: ", zahl_2)









# =============================================================================
# Main Programm beginnt:
# =============================================================================
if __name__ == '__main__':
    
    #Zuerst wird die Eingabe gemacht
    zahl_1, zeichen, zahl_2 = eingaben_machen()
    
    #Danach werden die Berecunungne durchgeführt
    berechnungen_machen (zahl_1, zeichen, zahl_2)






