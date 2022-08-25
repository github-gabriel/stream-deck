# <img src="https://github.com/github-gabriel/stream-deck/blob/main/src/logo.png" width="75" height="75" align="center">Stream Deck

Das Stream Deck nutzt das Keypad für den Arduino und Python um die gedrückten Tasten des Keypads auszulesen und entsprechende, über die GUI zugewiesene, Befehle auszuführen. Bisher kann eine Taste entweder eine .exe Datei ausführen oder eine Website in einem Webbrowser öffnen. Die Befehle werden in ```stream_deck_commands.json``` gespeichert. Zuerst wurden die Befehle nur im Value des Dictionaries gespeichert, doch mein Freund [xImAnton](https://github.com/xImAnton) kam auf die Idee nested Dictionaries zu nutzen (und hat mir geholfen, das Projekt besser zu strukturieren), damit man weniger "String-Funktionen"(replace, strip, "in-Keyword" etc.) benutzen muss und Mode + Argument einfach getrennt abfragen kann. Außerdem hat die Applikation ein System Tray Icon, womit man die GUI öffnen/ schließen kann ("Stream Deck" funktioniert aber noch!) und das Programm komplett beenden kann.
## Jetzt zum Setup/ Aufbau:
### 1. Für den Arduino benötigt ihr ein Keypad, was ungefähr so aussehen sollte:
<img src="https://github.com/github-gabriel/stream-deck/blob/main/Images/arduino_keypad.jpg" width="500" align="center">

### 2. Lasst [das Keypad Programm](https://github.com/github-gabriel/stream-deck/blob/main/Keypad.ino) auf dem Arduino laufen. Jetzt werden die einzelnen Knopfdrücke auf dem Serial Monitor ausgegeben.

### 3. Jetzt müsst ihr euch nur noch [den src Ordner](https://github.com/github-gabriel/stream-deck/tree/main/src) downloaden und ```stream_deck.py``` ausführen.
