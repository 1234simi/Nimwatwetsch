from datetime import datetime
import time

from Datenbank_json_files.libs.datenbank import datenbank_laden, in_datenbank_speichern, aus_datenbank_loeschen

def menu():
    print("Was willst du machen?")
    menu_punkte = ['Eingabe machen', 'Alles ausgeben', 'Etwas löschen']
    for index, punkt in enumerate(menu_punkte):
        # time.sleep(0.3)
        print(f"[{index + 1}] {punkt}")

    # time.sleep(0.3)
    auswahl = input("Bitte auswählen: ")
    if auswahl == "1":
        #Eingabe machen
        eintrag_erstellen()
    elif auswahl == "2":
        #Alles ausgeben
        inhalte_auflisten()
    elif auswahl == "3":
        #Etwas löschen
        todo_erledigen()
    else:
        print(f"Die Eingabe {auswahl} ist falsch")

#todo: test schreiben
def eintrag_erstellen():
    eintrag = input("Eintrag: ")
    timestamp = str(datetime.now())
    eintrag_dict = {
        timestamp: eintrag
    }
    in_datenbank_speichern("datenbank.db", eintrag_dict)


#todo: test schreiben
def inhalte_auflisten():
    eintrag = datenbank_laden("datenbank.db")
    for timestamp, eintrag in eintrag.items():
        timestamp = display_timestamp(timestamp)
        print(f"{timestamp} -> {eintrag}")


#todo: test schreiben
def todo_erledigen():
    eintrag = datenbank_laden("datenbank.db")
    for index, (timestamp, eintrag) in enumerate(eintrag.items()):
        timestamp = display_timestamp(timestamp)
        print(f"[{index}] {timestamp} -> {eintrag}")

    auswahl = input("Bitte auswählen: ")
    key = list(eintrag.keys())[int(auswahl)]
    erledigte = eintrag.pop(key)
    eintrag_dict = {
        key: erledigte
    }
    in_datenbank_speichern("datenbank_delited.db", eintrag_dict)
    aus_datenbank_loeschen("datenbank.db", key)


def display_timestamp(timestamp):
    """
    Das Format wird geändert. 'timestamp' kommt von der built in Funktion from datetime import datetime

    Args:
        timestamp: "2022-11-19 12:18:08.190088"

    Returns: "19. November 2022 12:18:08"

    """
    timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")
    eigenes_format = timestamp.strftime("%d. %B %Y %H:%M:%S")
    return eigenes_format
