class DDObj:

    def __init__(self):
        self.label = ''
        self.desc = ''
        self.label_min = ''
        self.label_max = ''
        self.resolution = ''
        self.code_label = ''
        self.code_min = ''
        self.code_max = ''
        self.code_lsb_nume = ''
        self.code_lsb_denomi = ''


class TypeLen:

    def __len__(self):
        self.label = ''
        self.data_len = ''

    def __init__(self, label, data_len):
        self.label = label
        self.data_len = data_len


class DDStruct:
    def __init__(self):
        self.elements = []
        self.struct_size = None



