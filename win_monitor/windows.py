from PyQt5.QtWidgets import QMainWindow
from ui import Main


class MainWindow(QMainWindow, Main.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
