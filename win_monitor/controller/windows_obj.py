from enum import Enum
from db import log


# DEFAULT_DATA_FILE = os.path.dirname(os.path.realpath(__file__)) + '/../db/data/data.txt'


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
        self.database = None
        self.username = None
        self.password = None


class Attendance:
    def __init__(self):
        self.startTime = None
        self.endTime = None


class Tenant:
    def __init__(self):
        self.id = None
        self.name = None
        self.owner = None
        self.description = None


class User:
    def __init__(self):
        self.id = None
        self.user_name = None
        self.job_number = None
        self.email = None
        self.description = None
        self.tenant = None
        self.attendance = Attendance()


class WinObj:
    def __init__(self):
        self.cycle = None
        self.delay = None
        self.tenants = None
        self.local_data = log.DEFAULT_DATA_DIR
        self.multi_user = 1
        self.user = User()
        self.mode = Mode.OFFLINE.name
        self.remind = Remind.TRUE.name
        self.database = DataBase()
        self.external_tools = {}
