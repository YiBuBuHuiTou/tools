from enum import Enum
import os

DEFAULT_DATA_FILE = os.path.dirname(os.path.realpath(__file__)) + '/data/data.txt'


class Mode(Enum):
    ONLINE = 1
    OFFLINE = 2


class Remind(Enum):
    TRUE = 1
    FALSE = 2


class DataBase:
    def __init__(self):
        self.category = None
        self.host = None
        self.port = None
        self.data_base = None
        self.username = None
        self.password = None


class WinObj:
    def __init__(self):
        self.user_name = None
        self.job_number = None
        self.email = None
        self.local_data = DEFAULT_DATA_FILE
        self.mode = Mode.ONLINE
        self.remind = Remind.TRUE
        self.database = DataBase()

