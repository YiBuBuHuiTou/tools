import dd_obj
import json


# 字节对齐判断，简单判断是否能被偏移整除
def check_byte_align(offset, size):
    status = True
    if offset % size != 0:
        status = False
    return status


# 数字格式化，整形将小数点后数字去掉
def data_format(data):
    if data == int(data):
        data = int(data)
    return data


def load_struct():
    # 测试用假数据
    #####################外部名    类型  长度 最小值  最大值    lsb
    ele1 = dd_obj.Ele('ele_1', 'UW', 2,   0,     500,   1, 4)
    eler = dd_obj.Ele('ele_reserve', '', 2, 0, 2500, 2, 4)
    ele2 = dd_obj.Ele('ele_2', 'DD', 4, 0, 500, 2, 4)
    ele3 = dd_obj.Ele('ele_3', 'UB', 1, 0, 100, 1, 1)
    ele4 = dd_obj.Ele('ele_4', 'SB', 1, -24, 100, 2, 1)
    ele5 = dd_obj.Ele('ele_5', 'SW', 2, 0, 500, 2, 5)
    ele_array = [ele1, eler, ele2, ele3, ele4, ele5]
    struct = dd_obj.DDStruct(ele_array, 'test_name')
    return struct


# 转换为DD对象
def convert2DD(struct_name, ele, index):
    ddobj = dd_obj.DDObj()
    ddobj.label = ele.label
    ddobj.desc = ''  # TODO
    # .......#TODO
    ddobj.label_min = ele.min
    ddobj.label_max = ele.max

    ddobj.code_label = struct_name + '[{}]'.format(index)
    ddobj.code_type = ele.data_type
    #计算最小值
    ddobj.code_min = data_format(ele.min * ele.lsb_denomi / ele.lsb_numi)
    #计算最大值
    ddobj.code_max = data_format(ele.max * ele.lsb_denomi / ele.lsb_numi)
    #LSB
    ddobj.code_lsb_nume = ele.lsb_denomi
    ddobj.code_lsb_denomi = ele.lsb_numi

    return ddobj


if __name__ == '__main__':
    message = ''
    dd_struct = load_struct()
    dd_eles = dd_struct.elements
    ddobjs = []
    data_offset = 0
    for ele in dd_eles:
        # 判断字节是否对齐
        status = check_byte_align(data_offset, ele.data_len)
        if not status:
            message += 'Error: 字节没有对齐! Name :' + ele.label
            print(message)
            # 异常退出
            exit(1)
        else:
            # 计算偏移量,强转为int，不然是float类型有小数点
            index = int( data_offset / ele.data_len )
            # 生成DD对象
            ddobjs.append(convert2DD(dd_struct.struct_name, ele, index))
        # 字节偏移量变更 -> 下一个变量相对于结构体的地址
        data_offset += ele.data_len

    #打印数据 测试用
    for obj in ddobjs:
        print(json.dumps(obj.__dict__))