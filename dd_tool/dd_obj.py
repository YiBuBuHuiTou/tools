class DDObj:

    def __init__(self):
        self.label = None
        self.desc = None
        self.label_min = None
        self.label_max = None
        self.resolution = None
        self.code_label = None
        self.code_type = None
        self.code_min = None
        self.code_max = None
        self.code_lsb_nume = None
        self.code_lsb_denomi = None


class Ele:

    def __init__(self, label,data_type, data_len,min, max,lsb_nume,lsb_denomi):
        self.label = label
        self.data_type = data_type
        self.data_len = data_len
        self.min = min
        self.max = max
        self.lsb_nume = lsb_nume
        self.lsb_denomi = lsb_denomi

class DDStruct:
    def __init__(self, elements, struct_name):
        self.elements = elements
        self.struct_name = struct_name
        self.struct_size = None



