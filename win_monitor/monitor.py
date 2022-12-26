import sys

from PyQt5.QtWidgets import QApplication
from controller.windows import MainWindow
import pidfile

# @pidfile
def run():
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()