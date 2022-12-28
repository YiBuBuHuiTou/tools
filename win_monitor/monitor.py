import sys
import psutil
from PyQt5.QtWidgets import QApplication
from controller.windows import MainWindow
from db import log

LOGGER = log.LOGGER


# 判断进程是否已存在
def isRunning():
    is_running = False
    now_proc = None
    for proc in psutil.process_iter():
        if proc.name() == "monitor.exe":
            is_running = True
            now_proc = proc
            break
    return is_running,


# 杀进程
def destroyPid(proc):
    proc.kill()


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
