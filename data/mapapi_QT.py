from PyQt6 import uic
from PyQt6.QtWidgets import QWidget


class MapWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/main.ui')
