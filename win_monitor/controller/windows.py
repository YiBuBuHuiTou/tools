from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTime
from configparser import ConfigParser
import functools
import subprocess
import os
from controller import windows_obj
from ui import Main
from action import action
from db import sql

CONFIG_FILE = os.path.dirname(os.path.realpath(__file__)) + '/../config/config.ini'


# ini 配置文件解析
class ConfigIni:

    def __init__(self):
        self.config = ConfigParser()
        self.config.read(CONFIG_FILE, encoding="utf-8")

    # 获取 单个 配置
    def getConfig(self, section, option, default=None):
        data = None
        try:
            data = self.config.get(section=section, option=option)
            if data is None:
                data = default
        except Exception as e:
            print(e)
            data = default
        return data

    # 获取 section下所有数据
    def getOptions(self, section="default", default=None):
        tools = []
        try:
            tools = self.config.options(section)
            if tools is None:
                tools = [default]
        except Exception as e:
            print(e)
            tools = [default]

        return tools

    # 追加section
    def addSection(self, section="default"):
        try:
            # 追加section
            self.config.add_section(section)
            # 写入文件
            with open(CONFIG_FILE, "w+", encoding="utf-8") as f:
                self.config.write(f)
        except Exception as e:
            print("addSection : " + e)

    # 更新指定section的option
    def setOption(self, section, key, value):
        try:
            # 更新数据
            self.config.set(section, key, value)
            # 写入文件
            with open(CONFIG_FILE, "w+", encoding="utf-8") as f:
                self.config.write(f)
        except Exception as e:
            print(e)


# 加载配置
def load_config():
    config = ConfigIni()
    # 读取配置文件
    win_obj = windows_obj.WinObj()
    # 监听周期
    win_obj.cycle = int(config.getConfig('default', 'cycle', default=1))
    # 延迟
    win_obj.delay = int(config.getConfig('default', 'delay', default=0))
    # 基本信息
    # 用户名
    win_obj.user_name = config.getConfig('user', 'name', default="test_user")
    # 工号
    win_obj.job_number = config.getConfig('user', 'job_number', default="000000")
    # 邮箱
    win_obj.email = config.getConfig('user', 'email', default="test@test.com")
    # 描述
    win_obj.description = config.getConfig('user', 'description', default="This is test user!!!!")

    # 考勤
    attendance = windows_obj.Attendance()
    # 考勤开始时间
    attendance.startTime = config.getConfig('attendance', 'start', default="9:00")
    # 考勤结束时间
    attendance.endTime = config.getConfig('attendance', 'end', default="18:00")
    win_obj.attendance = attendance

    # log 文件
    win_obj.local_data = config.getConfig('user', 'local_data', default=windows_obj.DEFAULT_DATA_FILE)

    # 模式  离线/在线
    win_obj.mode = config.getConfig('mode', 'mode', default=windows_obj.Mode.OFFLINE.name)

    # 是否开启提示
    win_obj.remind = config.getConfig('mode', 'remind', default=windows_obj.Remind.FALSE.name)

    # 数据库信息
    database = windows_obj.DataBase()
    # 数据库种类
    database.category = config.getConfig('database', 'category', default="Mysql")
    # 数据库ip
    database.host = config.getConfig('database', 'host', default="127.0.0.1")
    # 数据库端口
    database.port = config.getConfig('database', 'port', default=3306)
    # 数据库名字
    database.database = config.getConfig('database', 'database', default="test")
    # 数据库用户名
    database.username = config.getConfig('database', 'username', default="root")
    # 数据库密码
    database.password = config.getConfig('database', 'password', default="root")
    win_obj.database = database

    # 外部工具
    tool_names = config.getOptions('external_tools', default="追加")
    external_tools = {}
    for name in tool_names:
        external_tools[name] = config.getConfig("external_tools", name)
    win_obj.external_tools = external_tools

    print(win_obj.__dict__)
    print(win_obj.database.__dict__)
    print(win_obj.attendance.__dict__)
    return win_obj


# 保存配置
def save_config():
    pass


class MainWindow(QMainWindow, Main.Ui_MainWindow):
    # 保存用户配置信号
    # config_save_signal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.data = load_config()
        self.setDefaultData()
        self.add_tool.triggered.connect(self.add_tool_handler)
        # self.config_save_signal.connect(self.config_save_handler)
        # self.buttonBox.standardButton(QtWidgets.QDialogButtonBox.OK).clicked.connect(self.config_save_handler)
        self.buttonBox.accepted.connect(self.config_save_handler)
        self.buttonBox.rejected.connect(self.on_click_cancel_handler)
        sql.user_regist(self.data)
        try:
            thread = action.BackGroundTask("backgroundTask", "sleep_monitor", self.data)
            # 设置为非守护线程
            thread.daemon = False
            thread.start()
        except:
            print("线程启动异常")

    # 显示读取的数据
    def setDefaultData(self):
        # 姓名
        self.user_name.setText(self.data.user_name)
        # 工号
        self.job_number.setText(self.data.job_number)
        # 邮箱
        self.email.setText(self.data.email)
        # 描述
        self.description.setPlainText(self.data.description)
        # 周期
        self.cycle.setValue(self.data.cycle)
        # 延迟
        self.delay.setValue(self.data.delay)
        # 模式
        if self.data.mode == windows_obj.Mode.ONLINE.name:
            self.online.setChecked(True)
            self.offline.setChecked(False)

        else:
            self.online.setChecked(False)
            self.offline.setChecked(True)
        # 数据库种别
        self.db_category.setCurrentIndex(0)
        # 本地数据
        self.local_data.setText(self.data.local_data)
        # 数据库host
        self.db_host.setText(self.data.database.host)
        # 数据库端口
        self.db_port.setText(self.data.database.port)
        # 数据库名
        self.db_name.setText(self.data.database.database)
        # 数据库用户名
        self.db_username.setText(self.data.database.username)
        # 数据库密码
        self.db_password.setText(self.data.database.password)
        # 上班时间
        start = self.data.attendance.startTime.split(":")
        self.start_time.setTime(QTime(int(start[0]), int(start[1])))
        # 下班时间
        end = self.data.attendance.endTime.split(":")
        self.end_time.setTime(QTime(int(end[0]), int(end[1])))
        # 是否提示
        if self.data.remind == windows_obj.Remind.TRUE.name:
            self.remind.setChecked(True)
            self.unremind.setChecked(False)
        else:
            self.unremind.setChecked(True)
            self.remind.setChecked(False)

        # 追加菜单外部工具
        for key, value in self.data.external_tools.items():
            action = QtWidgets.QAction(self)
            action.setObjectName(key)
            action.setText(key)
            # action.triggered.connect(lambda: self.openExeHandler(value))
            action.triggered.connect(functools.partial(self.openExeHandler,value))
            self.external_tools.addAction(action)

    # 打开外部工具
    def openExeHandler(self, exe):
        print("打开外部工具: " + exe)
        try:
            subprocess.run(exe)
        except Exception as e:
            print("openExeHandler: " + e)

    # 追加外部配置
    def add_tool_handler(self):
        file, _ = QFileDialog.getOpenFileName(self, "选择文件", "C:\\", "All Files (*.exe *.html *.htm)")
        print("file : " + file)
        try:
            config = ConfigIni()
            config.setOption("external_tools", os.path.splitext(os.path.basename(file))[0], file)
        except Exception as e:
            print(e)
        finally:
            self.data = load_config()

    # 变更模式时的事件
    def on_change_mode_handler(self):
        print("变更配置模式")
        # TODO

    # OK按钮事件
    def config_save_handler(self, win_obj):
        print("配置保存")
        # TODO

    # CANCEL 按钮事件
    def on_click_cancel_handler(self):
        print("画面关闭")
        self.close()
        # TODO

    # TODO
    def startEmbedTool(self, tool):
        pass
