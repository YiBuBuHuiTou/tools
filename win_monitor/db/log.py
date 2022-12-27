import logging
from logging import handlers
from configparser import SafeConfigParser
import os

CONFIG_FILE = os.path.dirname(os.path.realpath(__file__)) + '/../config/config.ini'
DEFAULT_DATA_FILE = os.path.dirname(os.path.realpath(__file__)) + '/../db/data/'




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
    config.read(CONFIG_FILE)
    file_name = None
    try:
        file_name = config.get(section="default", option="local_data")
        if file_name is None:
            file_name = DEFAULT_DATA_FILE
    except Exception as e:
        print(e)
        file_name = DEFAULT_DATA_FILE
    try:
        loglevel = config.get(section="default", option="level")
        if loglevel is None or Logger.level[loglevel] is None:
            loglevel = "debug"
    except Exception as e:
        print(e)
        loglevel = "debug"

    logger = Logger(file_name + '/Attendance.log', loglevel, when='W0', backCount=10)

    return logger.logger


LOGGER = getLogger()