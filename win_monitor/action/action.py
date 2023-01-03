import time
import psutil
from enum import Enum
from PyQt5.QtCore import pyqtSignal, QObject
import threading
import datetime

from db import sql, log
from controller import windows_obj

LOGGER = log.LOGGER


class OsStatus(Enum):
    UNLOCK = 0
    LOCKED = 1


# Monitor信号与槽
class Monitor(QObject):
    # 用户登录状态信号
    win_status_signal = pyqtSignal(int, str, int)

    def __init__(self, database):
        super(Monitor, self).__init__()
        self.win_status_signal.connect(self.win_change_handler)
        self.database = database

    # 用户登录状况变化处理函数
    def win_change_handler(self, user_id, mode, status):
        if status == OsStatus.LOCKED.value:
            LOGGER.info("屏幕已锁定，当前时间：" + str(datetime.datetime.now()))
            if mode == windows_obj.Mode.ONLINE.name:
                sql.addLockRecord(self.database, user_id)

        elif status == OsStatus.UNLOCK.value:
            LOGGER.info("屏幕已解锁，当前时间：" + str(datetime.datetime.now()))
            if mode == windows_obj.Mode.ONLINE.name:
                sql.addUNLockRecord(self.database, user_id)

    # 监听windows 是否登录
    # 周期： cycle, 灵敏度：delay
    def locke_monitor(self, multi, user_id, mode, cycle, delay):
        delay_clone = delay
        status_old = OsStatus.LOCKED if isLocked(multi) else OsStatus.UNLOCK
        # 初始信号
        self.win_status_signal.emit(user_id, mode, status_old.value)

        while True:
            lock_status = isLocked(multi)
            status_change = False
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
                self.win_status_signal.emit(user_id, mode, status_old.value)
            # 检测周期
            time.sleep(cycle)


class BackGroundTask(threading.Thread):
    def __init__(self, thread_id, thread_name, win_obj):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.thread_name = thread_name
        self.win_obj = win_obj

    def run(self):
        Monitor(self.win_obj.database).locke_monitor(self.win_obj.multi_user, self.win_obj.user.id, self.win_obj.mode,
                                                     self.win_obj.cycle, self.win_obj.delay)

    def stop(self):
        # threading.async_raise(threading.Thread.ident, SystemExit)
        raise Exception("线程关闭")


# 判断windows 是否锁屏  用户登录状态下，没有LogonUI.exe进程
# 多用户状态（switch user？ 服务器系统开启多用户远程？）下失效，多用户状态下会存在多个LogonUI.exe进程
# 性能有点低 会导致监测周期不正确，大约0.6秒 TODO 下次改善
def isLocked(multi=1):
    lockFlag = False
    index = 0
    for proc in psutil.process_iter():
        if proc.name() == "LogonUI.exe":
            index = index + 1
            if index == multi:
                lockFlag = True
                break

    return lockFlag
