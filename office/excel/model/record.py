class Record:

    def __init__(self, index, key, attrs):
        # 行号
        self.index = index
        # 根据主键生成的id
        self.key = key
        # 所有的{“列名”：内容}
        self.attrs = attrs




