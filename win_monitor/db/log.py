import logging
from logging import handlers
from configparser import SafeConfigParser
import os

CONFIG_FILE = os.path.dirname(os.path.realpath(__file__)) + '/../config/config.ini'
DEFAULT_DATA_DIR = os.path.dirname(os.path.realpath(__file__)) + '/../data/'




# 日志
class Logger:
    LOG_FORMAT = " %(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d, %(funcName)s] %(message)s"
    instance = None

    level = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "fatal": logging.FATAL,
        "notset": logging.NOTSET
    }

    # def __new__(cls, *args, **kwargs):
    #     if cls.instance is None:
    #         cls.instance = super().__new__(cls)
    #
    #     return cls.instance

    def __init__(self, filename, level="debug", when='W', backCount=10, fmt=LOG_FORMAT):
        self.logger = logging.getLogger(filename)
        # log 级别
        self.logger.setLevel(self.level.get(level))
        # log 格式
        formatter = logging.Formatter(fmt)
        # 向屏幕输出
        sh = logging.StreamHandler()
        sh.setFormatter(formatter)

        # 向log文件输出
        # Calculate the real rollover interval, which is just the number of
        # seconds between rollovers.  Also set the filename suffix used when
        # a rollover occurs.  Current 'when' events supported:
        # S - Seconds
        # M - Minutes
        # H - Hours
        # D - Days
        # midnight - roll over at midnight
        # W{0-6} - roll over on a certain day; 0 - Monday
        #
        # Case of the 'when' specifier is not important; lower or upper case
        th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backCount, encoding="utf-8")
        th.setFormatter(formatter)

        self.logger.addHandler(sh)
        self.logger.addHandler(th)


def getLogger():
    config = SafeConfigParser()
    # 判断配置文件是否存在，不存在则新创建
    if os.path.exists(CONFIG_FILE) is False:
        os.mknod(os.mknod)

    config.read(CONFIG_FILE, encoding="utf-8")
    log_dir = None
    try:
        # 读取日志文件目录
        log_dir = config.get(section="default", option="local_data")
        if log_dir is None:
            log_dir = DEFAULT_DATA_DIR
    except Exception as e:
        print(e)
        log_dir = DEFAULT_DATA_DIR
    try:
        # 读取日志级别
        log_level = config.get(section="default", option="level")
        if log_level is None or Logger.level[log_level] is None:
            log_level = "debug"
    except Exception as e:
        print(e)
        log_level = "debug"

    # 判断日志文件夹是否存在，不存在则创建
    if os.path.exists(log_dir) is False:
        os.mkdir(log_dir)

    # 日志对象
    logger = Logger(log_dir + '/Attendance.log', log_level, when='W0', backCount=10)

    return logger.logger


LOGGER = getLogger()