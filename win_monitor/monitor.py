import sys
import os
import getopt
import signal
from PyQt5.QtWidgets import QApplication
from controller.windows import MainWindow
from db import log
from action import common

LOGGER = log.LOGGER


# 判断是否单例执行
def check_running():
    try:
        old_pid = None
        new_pid = None
        # 获取 monitor的进程id
        new_pid = common.get_pid()
        # 如果是第一次执行，则文件不存在
        if os.path.exists(common.DEFAULT_PID_FILE) is False:
            LOGGER.debug("Method = monitor#__name__ : 首次执行 pid： " + str(new_pid))
        else:
            # 如果是第二次执行
            old_pid = common.read_pid()
            # 删除pid文件
            common.remove_pid_file()
            # 杀死进程
            LOGGER.debug("Method = monitor#__name__ : 重复执行执行 杀死进程： " + str(old_pid))
            os.kill(int(old_pid), signal.SIGINT)

    except Exception as e:
        LOGGER.warning("Method = monitor#__name__ : 程序单例执行异常 Exception = " + str(e))
    finally:
        LOGGER.debug("Method = monitor#__name__ :  写入新pid： " + str(new_pid))
        common.write_pid(str(new_pid))


# 正常启动
def app_normal_start():
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())


def app_back_start():
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    # mainWin.show()
    mainWin.setVisible(False)
    sys.exit(app.exec_())


if __name__ == "__main__":
    # 启动检测
    check_running()

    # mode = None
    # try:
    #     options, err_args = getopt.getopt(sys.argv[1:], "m:", ["mode="])
    # except Exception as e:
    #     LOGGER.warning("程序参数 解析失败 Exception = " + str(e))
    #
    # LOGGER.debug("argvargvargvargvargv 启动参数：" + str(sys.argv))
    # LOGGER.debug("optionsoptionsoptionsoptionsoptionsoptions 启动参数：" + str(options))
    # LOGGER.debug("err_argserr_argserr_argserr_argserr_argserr_args 启动参数：" + str(err_args))

    # # 获取参数 -m -mode
    # for option, value in options:
    #     if option in ("-m", "-mode"):
    #         mode = value
    #         break
    # LOGGER.debug("modemodemodemodemodemode 启动参数：" + str(mode))

    # 普通模式
    # if mode == None:
    #     LOGGER.debug("程序正常启动 启动参数：" + str(sys.argv))
    #     app_normal_start()
    # # 后台运行
    # elif mode == "back":
    #     LOGGER.debug("程序后台启动 启动参数：" + str(sys.argv))
    #     app_back_start()
    # else:
    #     LOGGER.error("程序启动参数不正确，启动失败 启动参数：" + str(sys.argv))
    #     app_normal_start()

    # 普通模式
    if len(sys.argv) <= 1:
        LOGGER.debug("程序正常启动 启动参数：" + str(sys.argv))
        app_normal_start()
    # 后台运行
    elif sys.argv[-1] == "back":
        LOGGER.debug("程序后台启动 启动参数：" + str(sys.argv))
        app_back_start()
    else:
        LOGGER.error("程序启动参数不正确，启动失败 启动参数：" + str(sys.argv))
        app_normal_start()
