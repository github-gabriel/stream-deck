# Stream Deck

<p align="center">
  <img src="https://github.com/github-gabriel/stream-deck/blob/main/src/logo.png" width="240">
</p>

Das Stream Deck nutzt das Keypad für den Arduino und Python um die gedrückten Tasten des Keypads über die Serial Console auszulesen und entsprechende, über die GUI zugewiesene, Befehle auszuführen. Bisher kann eine Taste entweder eine .exe Datei ausführen oder eine Website in einem Webbrowser öffnen. Die Befehle werden in ```stream_deck_commands.json``` gespeichert, welches nested Dictionaries zum Speichern der unterschiedlichen Befehle nutzt. Außerdem hat die Applikation ein System Tray Icon, womit man die GUI öffnen/ schließen kann und das Programm komplett beenden kann.

## Setup

1. [Keypad.ino](https://github.com/github-gabriel/stream-deck/blob/main/Keypad.ino) auf dem Arduino ausführen lassen.

2. [Src Ordner](https://github.com/github-gabriel/stream-deck/tree/main/src) downloaden und ```stream_deck.py``` ausführen.

Projekt klonen
```
git clone https://github.com/github-gabriel/stream-deck
```

In src Folder navigieren
```
cd .\stream-deck\src\
```

Programm starten
```
python .\stream_deck.py
```


