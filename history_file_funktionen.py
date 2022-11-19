from datetime import datetime
import json

# todo: Test schreiben
def history_eintrag_erstellen(zahl_1, zeichen, zahl_2, resultat):
    ## Umwandeln in str()
    zahl_1, zeichen, zahl_2, resultat = umwandeln_in_str(zahl_1, zeichen, zahl_2, resultat)

    ## Strings werden aneinander gehängt
    eintrag = zahl_1 + zeichen +  zahl_2 + '=' + resultat
    # eintrag = input("Eintrag: ")
    timestamp = str(datetime.now())
    eintrag_dict = {
        timestamp: eintrag
    }
    in_datenbank_speichern("history_datenbank.db", eintrag_dict)


# todo: Test schreiben
def in_datenbank_speichern(db_file, inhalt_neu):
    inhalt = datenbank_laden(db_file)
    inhalt.update(inhalt_neu)
    with open(db_file, "w") as offene_datei:
        # offene_datei.write(json.dumps(inhalt))
        json.dump(inhalt, offene_datei, indent=4)


# todo: Test schreiben
def inhalte_auflisten():
    eintrag = datenbank_laden("history_datenbank.db")
    for timestamp, eintrag in eintrag.items():
        timestamp = display_timestamp(timestamp)
        print(f"{timestamp} -> {eintrag}")


## Test done
def umwandeln_in_str(zahl_1, zeichen, zahl_2, resultat):
    """
    Alle Zahlen und Werte werden in ein String umgewandelt
        :param zahl_1: (float) zahl_1
        :param zeichen: (ascii_int) zeichen
        :param zahl_2: (float) zahl_2
        :param resultat: (float) resultat
        :return: (str)
    """
    zahl_1 = str(zahl_1)
    zahl_2 = str(zahl_2)
    resultat = str(resultat)
    zeichen = str(chr(zeichen))
    return zahl_1, zeichen, zahl_2, resultat


## test done
def datenbank_laden(db_file):
    try:
        with open(db_file) as offene_datei:
            datei_inhalt = offene_datei.read()
            inhalt = json.loads(datei_inhalt)
    except FileNotFoundError:
        inhalt = {}
    return inhalt


##  Test done
def display_timestamp(timestamp):
    """
    Das Format wird geändert. 'timestamp' kommt von der built in Funktion 'from datetime import datetime'
        :param timestamp: "2022-11-19 12:18:08.190088"
        :return: "19. November 2022 12:18:08"
    """
    timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")
    eigenes_format = timestamp.strftime("%d. %B %Y %H:%M:%S")
    return eigenes_format





















