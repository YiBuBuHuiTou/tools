import datetime
import time
import psutil
import pymysql


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
# 周期： cycle
def locke_monitor(cycle):
    while True:
        if isLocked():
            print("Locked")
        else:
            print("unLocked")
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
