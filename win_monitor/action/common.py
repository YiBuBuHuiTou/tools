import psutil
import os
from db import log

LOGGER = log.LOGGER

DEFAULT_PID_FILE = os.path.dirname(os.path.realpath(__file__)) + '/../lock/.pid'
DEFAULT_PID_DIR = os.path.dirname(os.path.realpath(__file__)) + '/../lock/'


# 获取monitor的pid
def get_pid():
    pid = None
    for proc in psutil.process_iter():
        if proc.name() == "monitor.exe":
            pid = proc.pid
            break
    return pid


# 写pid
def write_pid(pid):
    if os.path.exists(DEFAULT_PID_DIR) is False:
        os.mkdir(DEFAULT_PID_DIR)
    pid_file = open(DEFAULT_PID_FILE, "w+", encoding="utf-8")
    # 写入pid
    pid_file.write(str(pid))
    pid_file.flush()
    pid_file.close()


# 读取pid
def read_pid():
    file = open(DEFAULT_PID_FILE, "r", encoding="utf-8")
    # 读取上回写入的pid
    pid = file.readline()
    file.close()
    return int(pid)


# 删除pid文件
def remove_pid_file():
    os.remove(DEFAULT_PID_FILE)
