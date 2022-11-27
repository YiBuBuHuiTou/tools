from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from configparser import ConfigParser
import os
from controller import windows_obj
from ui import Main
from action import action

CONFIG_FILE = os.path.dirname(os.path.realpath(__file__)) + '/../config/config.ini'


# 加载配置
def load_config(file):
    config = ConfigParser()
    # 读取配置文件
    config.read(file, encoding="utf-8")
    print(config)
    win_obj = windows_obj.WinObj()
    # 监听周期
    win_obj.cycle = int(config.get(section='default', option='cycle'))
    # 延迟
    win_obj.delay = int(config.get(section='default', option='delay'))
    # 基本信息
    win_obj.user_name = config.get(section='user', option='name')
    win_obj.job_number = config.get(section='user', option='job_number')
    win_obj.email = config.get(section='user', option='email')
    data_dir = config.get(section='user', option='local_data')
    win_obj.local_data = data_dir if data_dir != '' else windows_obj.DEFAULT_DATA_FILE
    # 模式  个人/办公
    mode = config.get(section='mode', option='mode')
    win_obj.mode = windows_obj.Mode.ONLINE if mode == 'ONLINE' else windows_obj.Mode.OFFLINE

    # 数据库信息
    database = windows_obj.DataBase()
    database.category = config.get(section='database', option='category')
    database.host = config.get(section='database', option='host')
    database.port = config.get(section='database', option='port')
    database.database = config.get(section='database', option='database')
    database.username = config.get(section='database', option='username')
    database.password = config.get(section='database', option='password')
    win_obj.database = database

    # 外部工具
    # TODO

    print(win_obj.__dict__)
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
        self.data = load_config(CONFIG_FILE)

        # self.config_save_signal.connect(self.config_save_handler)
        # self.buttonBox.standardButton(QtWidgets.QDialogButtonBox.OK).clicked.connect(self.config_save_handler)
        self.buttonBox.accepted.connect(self.config_save_handler)
        self.buttonBox.rejected.connect(self.on_click_cancel_handler)

        try:
            thread = action.BackGroundTask("backgroundTask", "sleep_monitor", self.data)
            # 设置为非守护线程
            thread.daemon = False
            thread.start()
        except:
            print("线程启动异常")

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
