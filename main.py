import sys

from PyQt6.QtWidgets import QApplication

from data.get_map import get_map
from data.mapapi_QT import MapWindow

if __name__ == '__main__':
    get_map()
    app = QApplication(sys.argv)
    window = MapWindow()
    window.show()
    sys.exit(app.exec())
