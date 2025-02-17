from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow

from forms.main import Ui_MainWindow


class MapWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        pixmap = QPixmap('maps_folder/map.png')
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
