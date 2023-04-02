import hashlib
from . import record

SUFFIX = r'-unique'
TITLE = 0
# 定义标题行的列
cols = []
# 定义主键列表
primary_keys = []


# excel 行对象
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
        for index, row in self.dataFrame.iterrows():
            # 获取字典类型的行数据
            row_raw = row.to_dict()
            # 生成key原始数据
            key_row = str(index)
            if self.primary_keys is not None and self.primary_keys != []:
                for primary_key in self.primary_keys:
                    # 生成 id原始数据
                    key_row += str(row_raw[primary_key])
            # key 的MD5值
            key = self.generate_id(key_row)
            # # 保存数据索引 （未使用）
            # row_raw["index"] = index
            # # 保存id （未使用）
            # row_raw["id"] = id
            # 生成record 对象
            self.records.append(record.Record(index=index, key=key, attrs=row_raw))
            print(row_raw)

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

    # 根据主键对应属性值生成id
    def generate_id(self, tempstr):
        return hashlib.md5(tempstr.encode()).hexdigest()

    def compare(self, another_records):
        pass

    # 当数据不想同时，更新数据（合并两个对象的差异）
    def updateRecords(self, another):
        pass
