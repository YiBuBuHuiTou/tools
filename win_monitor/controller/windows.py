from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTime
from configparser import SafeConfigParser
import functools
import subprocess
import os
from controller import windows_obj
from ui import Main
from action import action
from db import sql, log


# CONFIG_FILE = os.path.dirname(os.path.realpath(__file__)) + '/../config/config.ini'
LOGGER = log.LOGGER

# ini 配置文件解析
class ConfigIni:

    def __init__(self):
        self.config = SafeConfigParser()
        self.config.read(log.CONFIG_FILE, encoding="utf-8")

    # 获取 单个 配置
    def getConfig(self, section, option, default=None):
        data = None
        try:
            data = self.config.get(section=section, option=option)
            if data is None:
                data = default
        except Exception as e:
            data = default
            LOGGER.error("Method = ConfigIni#getConfig : ini 获取配置异常： section = " + section + " option = " + option)
            LOGGER.error("Method = ConfigIni#getConfig : 异常信息： Exception = " + str(e))
        return data

    # 获取 section下所有数据
    def getOptions(self, section="default", default=None):
        tools = []
        try:
            tools = self.config.options(section)
            if tools is None:
                tools = [default]
        except Exception as e:
            tools = [default]
            LOGGER.error("Method = ConfigIni#getOptions : ini 获取配置异常： section = " + section)
            LOGGER.error("Method = ConfigIni#getOptions : 异常信息： Exception = " + str(e))
        return tools

    # 追加section
    def addSection(self, section="default"):
        try:
            # 追加section
            self.config.add_section(section)
            # 写入文件
            with open(log.CONFIG_FILE, "w+", encoding="utf-8") as f:
                self.config.write(f)
        except Exception as e:
            print("addSection : " + e)
            LOGGER.error("Method = ConfigIni#addSection : ini 获取配置异常： section = " + section)
            LOGGER.error("Method = ConfigIni#addSection : 异常信息： Exception = " + str(e))

    # 更新指定section的option
    def setOption(self, section, key, value):
        try:
            # 更新数据
            self.config.set(section, key, value)
            # 写入文件
            with open(log.CONFIG_FILE, "w+", encoding="utf-8") as f:
                self.config.write(f)
        except Exception as e:
            LOGGER.error("Method = ConfigIni#setOption : ini 配置更新异常： section = " + section + " option: " + key + " value : " + value)
            LOGGER.error("Method = ConfigIni#setOption : 异常信息： Exception = " + str(e))



class MainWindow(QMainWindow, Main.Ui_MainWindow):
    # 保存用户配置信号
    # config_save_signal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.config = ConfigIni()
        self.data = self.load_config()
        self.setDefaultData()
        self.singal_and_slot()
        sql.user_regist(self.data)
        try:
            thread = action.BackGroundTask("backgroundTask", "sleep_monitor", self.data)
            # 设置为非守护线程
            thread.daemon = False
            thread.start()
        except Exception as e:
            LOGGER.error("Method = MainWindow#__init__ : 线程启动异常")
            LOGGER.error("Method = MainWindow#__init__ : 异常信息： Exception = " + str(e))

    # 信号与槽， 追加监听事件
    def singal_and_slot(self):
        # 菜单栏追加外部工具按钮
        self.add_tool.triggered.connect(self.add_tool_handler)
        # 日志文件选择按钮
        self.data_dir.clicked.connect(self.change_log_dir_hamdler)
        # 离线按钮
        self.offline.clicked.connect(functools.partial(self.on_change_mode_handler, windows_obj.Mode.OFFLINE.name ))
        # 在线按钮
        self.online.clicked.connect(functools.partial(self.on_change_mode_handler, windows_obj.Mode.ONLINE.name ))
        # 保存按钮
        self.save_btn.clicked.connect(self.config_save_handler)
        # 取消按钮
        self.cancel_btn.clicked.connect(self.on_click_cancel_handler)


    # 加载配置
    def load_config(self):
        # 读取配置文件
        win_obj = windows_obj.WinObj()
        # 监听周期
        win_obj.cycle = int(self.config.getConfig('default', 'cycle', default=1))
        # 延迟
        win_obj.delay = int(self.config.getConfig('default', 'delay', default=0))
        # log 文件
        win_obj.local_data = self.config.getConfig('default', 'local_data', default=log.DEFAULT_DATA_FILE)

        # 基本信息
        # 用户名
        win_obj.user_name = self.config.getConfig('user', 'name', default="test_user")
        # 工号
        win_obj.job_number = self.config.getConfig('user', 'job_number', default="000000")
        # 邮箱
        win_obj.email = self.config.getConfig('user', 'email', default="test@test.com")
        # 描述
        win_obj.description = self.config.getConfig('user', 'description', default="This is test user!!!!")

        # 考勤
        attendance = windows_obj.Attendance()
        # 考勤开始时间
        attendance.startTime = self.config.getConfig('attendance', 'start', default="9:00")
        # 考勤结束时间
        attendance.endTime = self.config.getConfig('attendance', 'end', default="18:00")
        win_obj.attendance = attendance

        # 模式  离线/在线
        win_obj.mode = self.config.getConfig('mode', 'mode', default=windows_obj.Mode.OFFLINE.name)

        # 是否开启提示
        win_obj.remind = self.config.getConfig('mode', 'remind', default=windows_obj.Remind.FALSE.name)

        # 数据库信息
        database = windows_obj.DataBase()
        # 数据库种类
        database.category = self.config.getConfig('database', 'category', default="Mysql")
        # 数据库ip
        database.host = self.config.getConfig('database', 'host', default="127.0.0.1")
        # 数据库端口
        database.port = self.config.getConfig('database', 'port', default=3306)
        # 数据库名字
        database.database = self.config.getConfig('database', 'database', default="test")
        # 数据库用户名
        database.username = self.config.getConfig('database', 'username', default="root")
        # 数据库密码
        database.password = self.config.getConfig('database', 'password', default="root")
        win_obj.database = database

        # 外部工具
        tool_names = self.config.getOptions('external_tools', default="追加")
        external_tools = {}
        for name in tool_names:
            external_tools[name] = self.config.getConfig("external_tools", name)
        win_obj.external_tools = external_tools

        LOGGER.debug("Method = MainWindow#load_config : ini 配置取得 主体信息： + " + str(win_obj.__dict__))
        LOGGER.debug("Method = MainWindow#load_config : ini 配置取得 数据库信息： + " + str(win_obj.database.__dict__))
        LOGGER.debug("Method = MainWindow#load_config : ini 配置取得 考勤信息： + " + str(win_obj.attendance.__dict__))

        return win_obj

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
        self.db_category.setCurrentIndex(0)  # TODO  固定值
        # 本地数据
        self.local_data.setText(self.data.local_data)
        # 数据库host
        self.db_host.setText(self.data.database.host)
        # 数据库端口
        self.db_port.setText(str(self.data.database.port))
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
            action.triggered.connect(functools.partial(self.open_exe_handler,value))
            self.external_tools.addAction(action)

    # 打开外部工具
    def open_exe_handler(self, exe):
        LOGGER.debug("Method = MainWindow#open_exe_handler : 打开外部工具： + " + exe)
        try:
            subprocess.run(exe)
        except Exception as e:
            LOGGER.error("Method = MainWindow#open_exe_handler : 打开外部工具异常 Exception =  " + e)

    # 追加外部配置
    def add_tool_handler(self):
        file, _ = QFileDialog.getOpenFileName(self, "选择文件", "C:\\", "All Files (*.exe *.html *.htm)")
        LOGGER.debug("Method = MainWindow#add_tool_handler : 追加外部工具 工具 = " + file)
        try:
            self.config.setOption("external_tools", os.path.splitext(os.path.basename(file))[0], file)
        except Exception as e:
            LOGGER.error("Method = MainWindow#add_tool_handler : 追加外部工具异常 Exception = " + str(e))

        finally:
            # self.data = self.load_config()
            pass

    # 选择log文件夹
    def change_log_dir_hamdler(self):
        dir = QFileDialog.getExistingDirectory(self, "选择文件夹", "./")
        self.local_data.setText(dir)

    # 变更模式时的事件
    def on_change_mode_handler(self, mode):
        if mode == windows_obj.Mode.ONLINE.name:
            # 数据库种别
            self.db_category.setDisabled(False)
            # 数据库host
            self.db_host.setDisabled(False)
            # 数据库端口
            self.db_port.setDisabled(False)
            # 数据库名
            self.db_name.setDisabled(False)
            # 数据库用户名
            self.db_username.setDisabled(False)
            # 数据库密码
            self.db_password.setDisabled(False)

        elif mode == windows_obj.Mode.OFFLINE.name:
            # 数据库种别
            self.db_category.setDisabled(True)
            # 数据库host
            self.db_host.setDisabled(True)
            # 数据库端口
            self.db_port.setDisabled(True)
            # 数据库名
            self.db_name.setDisabled(True)
            # 数据库用户名
            self.db_username.setDisabled(True)
            # 数据库密码
            self.db_password.setDisabled(True)

    # OK按钮事件
    def config_save_handler(self):
        try:
            # 监听周期
            self.config.setOption('default','cycle', str(self.cycle.value()))
            # 延迟
            self.config.setOption('default','delay', str(self.delay.value()))
            # log 文件
            self.config.setOption('default','local_data', self.local_data.text())

            # 基本信息
            # 用户名
            self.config.setOption('user','name', self.user_name.text())
            # 工号
            self.config.setOption('user','job_number', self.job_number.text())
            # 邮箱
            self.config.setOption('user','email', self.email.text())
            # 描述
            self.config.setOption('user','description', self.description.toPlainText())

            # 考勤
            # 考勤开始时间
            self.config.setOption('attendance','start', self.start_time.time().toString("hh:mm"))
            # 考勤结束时间
            self.config.setOption('attendance','end', self.end_time.time().toString("hh:mm"))

            # 模式  离线/在线
            if self.online.isChecked() is True:
                self.config.setOption('mode', 'mode', windows_obj.Mode.ONLINE.name)
            elif  self.offline.isChecked() is True:
                self.config.setOption('mode', 'mode', windows_obj.Mode.OFFLINE.name)

            # 是否开启提示
            if self.remind.isChecked() is True:
                self.config.setOption('mode', 'remind', windows_obj.Remind.TRUE.name)
            elif self.unremind.isChecked() is True:
                self.config.setOption('mode', 'remind', windows_obj.Remind.FALSE.name)

            # 数据库信息
            # 数据库种类
            self.config.setOption('database','category', self.db_category.currentText())
            # 数据库ip
            self.config.setOption('database','host', self.db_host.text())
            # 数据库端口
            self.config.setOption('database','port', self.db_port.text())
            # 数据库名字
            self.config.setOption('database','database', self.db_name.text())
            # 数据库用户名
            self.config.setOption('database','username', self.db_username.text())
            # 数据库密码
            self.config.setOption('database','password', self.db_password.text())


            LOGGER.debug("Method = MainWindow#config_save_handler : 保存数据结束")
        except Exception as e:
            LOGGER.error("Method = MainWindow#config_save_handler : 保存数据异常 Exception = " + str(e))

        self.close()

    # CANCEL 按钮事件
    def on_click_cancel_handler(self):
        LOGGER.debug("Method = MainWindow#on_click_cancel_handler : 画面关闭")
        self.close()


