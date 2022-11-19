import datetime
import time
import psutil
import pymysql
import sys

from PyQt5.QtWidgets import QApplication
from windows import MainWindow


def isLocked():
    lockFlag = False
    for proc in psutil.process_iter():
        if proc.name() == "LogonUI.exe":
            lockFlag = True
            break
    return lockFlag


def testisLocked():
    while (True):
        time.sleep(1)
        if isLocked():
            print("Locked")
        else:
            print("unLocked")


def testconnect():
    db = pymysql.connect(host='127.0.0.1',
                         port=3306,
                         user='root',
                         password='venus',
                         database='monitor',
                         charset='utf8')

    cursor = db.cursor()
    cursor.execute("select version()")
    data = cursor.fetchone()
    print("连接成功")
    db.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()

    mainWin.show()

    sys.exit(app.exec_())