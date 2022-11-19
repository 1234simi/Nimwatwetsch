from Datenbank_json_files.libs.datenbank import datenbank_laden
from Datenbank_json_files.libs.gui import display_timestamp


def test_datenbank_laden(file_name = 'test_file_json.json'):
    inhalt = datenbank_laden(file_name)
    assert len(inhalt) == 3
    assert inhalt["2022-11-19 19:01:52.122781"] == "sdgf"

def test_datenbank_laden(file_name = 'test_empty_file.json'):
    inhalt = datenbank_laden(file_name)
    assert len(inhalt) == 0




def test_display_timestamp():
    timestamp = "2022-11-05 12:18:08.190088"
    new_timestamp = display_timestamp(timestamp)

    assert new_timestamp == "05. November 2022 12:18:08"

