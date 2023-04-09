import hashlib
from enum import Enum
from . import record

SUFFIX = r'-unique'
TITLE = 0
# 定义标题行的列
cols = []
# 定义主键列表
primary_keys = []

# 对象比较状态枚举
class Status(Enum):
    # 两对象完全相同
    ALL_SAME = 0,
    # 对象状态为追加（比较前对象不存在， 比较后存在）
    ADD = 1,
    # 对象状态为删除（比较前对象存在， 比较后对象不存在）
    DELETE = 2,
    # 对象内容发生变更（两边存在相同id的对象，但其中内容有所不同）
    MOD = 3


# 将指定字符串生成MD5摘要
def generate_id(key):
    return hashlib.md5(key.encode()).hexdigest()


class Records:

    # 动态接受收不定参数主键以及字典
    def __init__(self, primary_keys, df):
        # 主键列表
        self.primary_keys = primary_keys
        # DataFrame
        self.dataFrame = df
        # 转换后的数据
        self.records = []
        # 生成行记录
        self.generate_records()

    # 生成excel 行记录
    def generate_records(self):
        # 循环excel 标题行之后的数据
        # index  所在excel 行号
        # row    行数据
        for index, row in self.dataFrame.iterrows():
            # 获取字典类型的行数据
            row_raw = row.to_dict()
            # 生成key原始数据
            key_row = ""
            if self.primary_keys is not None and self.primary_keys != []:
                for primary_key in self.primary_keys:
                    # 生成 id原始数据
                    key_row += str(row_raw[primary_key])
            # key 的MD5值
            # 如果不存在主键，则使用行号作为主键
            if key_row == "":
                key_row = str(index)
            key = generate_id(key_row)
            # 生成record 对象
            self.records.append(record.Record(index=index, key=key, attrs=row_raw))
            print("index" + str(index) + str(row_raw))

    # 判断是否是同一条数据
    def is_same_key(self, another):
        result = True
        # 循环所有主键，判断主键对应内容是否相同
        for primary_key in self.primary_keys:
            # 当两个对象中存在某一主键对应内容不等时 返回false
            # 根据主键获取比较前数据
            cell = self.attrs.get(primary_key)
            if cell != another.attrs.get(primary_key):
                result = False
                break
        return result

    # 根据指定id 获取record 对象
    def search_record(self, key):
        for row in self.records:
            if key == row.key:
                return row
        return None

    # 差分两个对象，并合并差分
    def diff_to_all(self, another):
        # 获取本对象所有数据
        records1 = self.records
        # 获取比较对象所有数据
        records2 = another.records
        # 获取两个对象中的所有id 并取并集
        keys = [r1.key for r1 in records1] | [r2.key for r2 in records2]
        # 开始循环比较
        for key in keys:
            # 获取本对象数据
            r1 = self.search_record(key)
            # 获取比较对象数据
            r2 = another.earch_record(key)
            # TODO 比较对象


    # 当数据不想同时，更新数据（合并两个对象的差异）
    def updateRecords(self, another):
        pass
