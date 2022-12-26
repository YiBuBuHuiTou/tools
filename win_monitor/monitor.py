import sys

from PyQt5.QtWidgets import QApplication
from controller.windows import MainWindow
from db import log

LOGGER = log.LOGGER

if __name__ == "__main__":

    if len(sys.argv) <= 1:
        LOGGER.debug("程序正常启动")
        app = QApplication(sys.argv)
        mainWin = MainWindow()
        mainWin.show()
        sys.exit(app.exec_())
    # 后台运行
    elif sys.argv[1] == "back":
        LOGGER.debug("程序后台启动")
        app = QApplication(sys.argv)
        mainWin = MainWindow()
        # mainWin.show()
        sys.exit(app.exec_())
    else:
        LOGGER.error("程序启动参数不正确，启动失败")