import datetime
import time
import psutil
import pymysql
from enum import Enum
from PyQt5.QtCore import pyqtSignal, QObject


class OsStatus(Enum):
    UNLOCK = 0
    LOCKED = 1


# 判断windows 是否锁屏  用户登录状态下，没有LogonUI.exe进程
# 多用户状态（switch user？ 服务器系统开启多用户远程？）下失效，多用户状态下会存在多个LogonUI.exe进程
def isLocked():
    lockFlag = False
    for proc in psutil.process_iter():
        if proc.name() == "LogonUI.exe":
            lockFlag = True
            break
    return lockFlag


# 监听windows 是否登录
# 周期： cycle, 灵敏度：delay
def locke_monitor(monitor, cycle, delay):
    delay_clone = delay
    status_old = OsStatus.LOCKED if isLocked() else OsStatus.UNLOCK
    # 初始信号
    monitor.win_status_signal.emit(status_old.value)

    while True:
        lock_status = isLocked()
        status_change = False
        print("start =" + str(datetime.datetime.now()))
        # 判断锁屏状态是否变化
        if lock_status is True and status_old == OsStatus.UNLOCK or lock_status is False and status_old == OsStatus.LOCKED:
            delay = delay - 1
        else:
            delay = delay_clone

        if delay <= 0:
            status_old = OsStatus.LOCKED if lock_status is True else OsStatus.UNLOCK
            status_change = True
            delay = delay_clone

        if status_change is True:
            monitor.win_status_signal.emit(status_old.value)
        print("end =" + str(datetime.datetime.now()))
        print("cycle =" + str(cycle))

        # 检测周期
        time.sleep(cycle)


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


# Monitor信号与槽
class Monitor(QObject):
    # 用户登录状态信号
    win_status_signal = pyqtSignal(int)

    def __init__(self):
        super(Monitor, self).__init__()
        self.win_status_signal.connect(self.win_change_handler)

    # 用户登录状况变化处理函数
    def win_change_handler(self, status):
        if status == OsStatus.LOCKED.value:
            print("屏幕已锁定")
        elif status == OsStatus.UNLOCK.value:
            print("屏幕已解锁")
