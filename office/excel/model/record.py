class Record:

    def __init__(self, index, key, attrs):
        # 行号
        self.index = index
        # 根据主键生成的id
        self.key = key
        # 所有的{“列名”：内容}
        self.attrs = attrs

    # 比较record 对象是否相同
    def compare(self, another):
        # 取两个对象属性的并集
        keys = set(self.attrs) | set(another.attrs.keys)
        # 判断属性值是否全部相等
        result = all(self.attrs.get(key) == another.attrs.get(key) for key in keys)

        return result
