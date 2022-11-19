import json


def datenbank_laden(db_file):
    try:
        with open(db_file) as offene_datei:
            datei_inhalt = offene_datei.read()
            inhalt = json.loads(datei_inhalt)
    except FileNotFoundError:
        inhalt = {}
    return inhalt


#todo: test schreiben
def in_datenbank_speichern(db_file, inhalt_neu):
    inhalt = datenbank_laden(db_file)
    inhalt.update(inhalt_neu)
    with open(db_file, "w") as offene_datei:
        # offene_datei.write(json.dumps(inhalt))
        json.dump(inhalt, offene_datei, indent=4)

#todo: test schreiben
def aus_datenbank_loeschen(db_file, key):
    inhalt = datenbank_laden(db_file)
    inhalt.pop(key)
    with open(db_file, "w") as offene_datei:
        json.dump(inhalt, offene_datei, indent=4)
