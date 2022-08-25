import json
import os
import threading
import webbrowser as wb

import PIL.Image
import pystray
import serial
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import *


APP_ICON = PIL.Image.open(r"D:\Windows\Desktop\pycharm\scripts\stream_deck\logo.png")
COMBO_BOX_ITEMS = {"execute .exe file": "exe", "open webbrowser": "wb"}


def read_commands():
    with open(r'D:\Windows\Desktop\pycharm\scripts\stream_deck\stream_deck_commands.json') as file:
        data = file.read()
    js = json.loads(data)
    return js


def write_commands(commands):
    with open(r'D:\Windows\Desktop\pycharm\scripts\stream_deck\stream_deck_commands.json', 'w') as file:
        json.dump(commands, file)


def open_wb(url):
    wb.register("chrome", None)
    wb.open(url)


def open_exe(path):
    os.system(path)


class StreamDeckApplication:
    def __init__(self):
        self.commands = read_commands()

        # https://www.pythonpool.com/python-serial-read/
        self.serial = serial.Serial(
            port='COM3',
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )

        self.icon = pystray.Icon("Logo", APP_ICON, menu=pystray.Menu(
            pystray.MenuItem("GUI", pystray.Menu(
                pystray.MenuItem("On", self.show_gui),
                pystray.MenuItem("Off", self.close_gui)
            )),
            pystray.MenuItem("Exit", self.stop)
        ))

        self.window = None

        self.running = True

    def show_gui(self):
        if self.window is not None:
            return

        threading.Thread(target=self.launch_gui).start()

    def close_gui(self):
        self.window.close()
        self.window = None

    def start(self):
        threading.Thread(target=self.serial_loop).start()
        self.show_gui()

        self.icon.run()

    def launch_gui(self):
        app = QApplication([])
        self.window = StreamDeckWindow(self)

        app.exec_()

    def serial_loop(self):
        while self.running:
            serial_output = self.serial.readline()
            serial_output = serial_output.decode("UTF-8").rstrip()
            if not len(serial_output) == 0:
                self.execute_command(serial_output)

    def execute_command(self, symbol):
        if "exe" in self.commands[symbol]['mode']:
            open_exe(self.commands[symbol]['args'])
        elif "wb" in self.commands[symbol]['mode']:
            open_wb(self.commands[symbol]['args'])

    def stop(self):
        self.icon.stop()
        self.close_gui()
        self.running = False

    def edit_command(self, x, mode, args):
        self.commands[x]['mode'] = mode
        self.commands[x]['args'] = args

        write_commands(self.commands)


class StreamDeckWindow(QMainWindow):
    def __init__(self, app):
        super(StreamDeckWindow, self).__init__()

        uic.loadUi(r"D:\Windows\Desktop\pycharm\scripts\stream_deck\stream_deck.ui", self)
        self.app = app
        self.show()
        self.rows = QVBoxLayout(self.mainLayout)
        self.command = None

        for i in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "A", "B", "C", "D", "*", "#"]:
            self.add_row(i)

    def closeEvent(self, event):
        self.app.window = None

    def on_ok(self, x, lineEdit, comboBox_text):
        self.app.edit_command(x, COMBO_BOX_ITEMS[comboBox_text], lineEdit)

    def add_row(self, x):
        widget = QWidget(self.mainLayout)

        row = QHBoxLayout(widget)
        row.setContentsMargins(10, 10, 10, 10)
        row.setObjectName("row")

        # Label
        label = QLabel(widget)
        label.setMinimumSize(QtCore.QSize(30, 70))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(40)
        label.setFont(font)
        label.setText(x)
        row.addWidget(label)

        # Combo Box
        comboBox = QComboBox(widget)
        comboBox.setMinimumSize(QtCore.QSize(100, 70))
        font = QtGui.QFont()
        font.setPointSize(26)
        comboBox.setFont(font)

        for item_type in COMBO_BOX_ITEMS.keys():
            comboBox.addItem(item_type)

        if self.app.commands[x]['mode'] == 'exe':
            comboBox.setCurrentIndex(0)
        elif self.app.commands[x]['mode'] == 'wb':
            comboBox.setCurrentIndex(1)

        row.addWidget(comboBox)

        # Line Edit
        lineEdit = QLineEdit(widget)
        lineEdit.setMinimumSize(QtCore.QSize(720, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        lineEdit.setFont(font)

        lineEdit.setText(self.app.commands[x]['args'])

        row.addWidget(lineEdit)

        # Ok Button
        okButton = QPushButton(widget)
        okButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(32)
        okButton.setFont(font)
        okButton.setText("Ok")
        row.addWidget(okButton)

        self.rows.addWidget(widget)

        def on_click():
            self.on_ok(x, lineEdit.text(), comboBox.currentText())

        okButton.clicked.connect(on_click)


def main():
    app = StreamDeckApplication()
    app.start()


if __name__ == '__main__':
    main()
