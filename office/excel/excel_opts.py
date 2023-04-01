# excel 操作处理
import pandas as pd
from office.excel.model import records

SUFFIX = r'-unique'
TITLE = 0
# 定义标题行的列
cols = []
# 定义主键列表
primary_keys = []


# 将excel 转换成DataFrame
def load_excel(file):
    return pd.read_excel(file, header=None)


# 解析模板第一行标题
def analyze_excel_title(template):
    # 获取DataFrame 对象
    df = load_excel(template)
    # 循环所有的列
    for col in df.iloc[TITLE].tolist():
        str_col = str(col)
        if str_col.endswith(SUFFIX):
            primary_keys.append(str_col[:len(str_col) - len(SUFFIX)])
            cols.append(str_col[:len(str_col) - len(SUFFIX)])
        else:
            cols.append(str_col)


# 将excel 转换为record对象
def convert2records(file):
    df = load_excel(file)
    return records.Records(primary_keys, title=cols, df=df)


def compare_excel(file1, file2):
    # 读取第一个excel表
    df1 = load_excel(file1)

    # 读取第二个excel表
    df2 = load_excel(file2)
    # 对比两个DataFrame对象的不同，并返回一个布尔值矩阵
    diff = df1 != df2
    # 将不同的地方标记为红色
    style = diff.style.applymap(lambda x: "background-color: red" if x else "")
    # 将标记后的结果保存到一个新的excel文件中
    style.to_excel("diff.xlsx")  # 输出为一个2为TRUE FALSE的矩阵


if __name__ == '__main__':
    # args = sys.argv[1:]
    # # 短格式命令
    # shortopts = "hco:n:"
    # # 长格式命令
    # longopts = ["help", "compare=", "old=", "new="]
    # try:
    #     opts, args = getopt.getopt(args, shortopts, longopts)
    # except getopt.GetoptError:
    #     print("Error: invalid arguments")
    #     sys.exit(2)
    #
    # # ===================================== 参数解析 ================================================
    # command = None
    # old_file = None
    # new_file = None
    # for opt, value in opts:
    #     if opt in ("-h", "--help"):  # 如果 option 是 -h 或 --help （表示用户请求帮助信息）
    #         print("Usage: excel_opts.py -c/--compare -o/--old <old_file> -n/--new <new_file>")  # 打印使用说明
    #         sys.exit()  # 退出程序，并返回默认错误码 0 （表示正常退出）
    #     # 文件比较工具参数解析
    #     elif opt in ("-c", "--compare"):  # 使用比较工具
    #         command = "compare"
    #     elif opt in ("-o", "--old"):  # 如果 option 是 -o 或 --old
    #         old_file = value  # 将 value 赋值给 old_file 变量
    #     elif opt in ("-n", "--new"):
    #         new_file = value
    #
    # # ===================================== 逻辑执行 ================================================
    # # 文件对比
    # if command is not None and command == "compare":
    #     if old_file is not None and new_file is not None and os.path.exists(old_file) and os.path.exists(new_file):
    #         compare_excel(old_file, new_file)
    #     else:
    #         print("参数异常")

    analyze_excel_title("test/test1.xlsx")
    print(convert2records("test/test1.xlsx"))
    print(cols)
    print(primary_keys)

    print(load_excel("test/test1.xlsx"))
