import hashlib


# excel 行对象
class Records:

    # 动态接受收不定参数主键以及字典
    def __init__(self,*primary_keys,title, df):
        # 主键列表
        self.primary_keys = primary_keys
        #attr_names
        self.attr_names = title
        # DataFrame
        self.dataFrame = df
        #转换后的数据
        self.records = []

    # 判断是否是同一条数据
    def is_same_key(self, another):
        result = True
        # 循环所有主键，判断主键对应内容是否相同
        for primary_key in self.primary_keys:
            #当两个对象中存在某一主键对应内容不等时 返回false
            #根据主键获取比较前数据
            cell = self.attrs.get(primary_key)
            if cell != another.attrs.get(primary_key):
                result = False
                break
        return result

    # 根据主键对应属性值生成id
    def generate_id(self, ):
        return hashlib.md5(str.encode()).hexdigest()

    def compare(self,another_records):
        pass



    # 当数据不想同时，更新数据（合并两个对象的差异）
    def updateRecords(self, another):
        pass