import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QLineEdit, QComboBox, QLabel, QDialog
import pandas as pd

class FilePickerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.option = 'outer'

    def init_ui(self):
        self.setWindowTitle('两个excel数据merge')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        id_layout = QHBoxLayout()
        label = QLabel('id')
        self.id_edit = QLineEdit(self)
        id_layout.addWidget(label)
        id_layout.addWidget(self.id_edit)

        # File pickers
        file1_layout = QHBoxLayout()
        self.file1_edit = QLineEdit(self)

        self.file1_button = QPushButton('输入文件1：', self)
        self.file1_button.clicked.connect(self.pick_file1)
        file1_layout.addWidget(self.file1_button)
        file1_layout.addWidget(self.file1_edit)


        file2_layout = QHBoxLayout()
        self.file2_edit = QLineEdit(self)
        self.file2_button = QPushButton('输入文件2：', self)
        self.file2_button.clicked.connect(self.pick_file2)
        file2_layout.addWidget(self.file2_button)
        file2_layout.addWidget(self.file2_edit)


        output_layout = QHBoxLayout()
        self.output_edit = QLineEdit(self)
        self.output_button = QPushButton('输出路径', self)
        self.output_button.clicked.connect(self.pick_output_folder)
        output_layout.addWidget(self.output_button)
        output_layout.addWidget(self.output_edit)


        # Execute and Exit buttons
        button_layout = QHBoxLayout()
        # 创建一个下拉框
        self.comboBox = QComboBox(self)

        # 向下拉框添加选项
        self.comboBox.addItem('左连接')
        self.comboBox.addItem('右连接')
        self.comboBox.addItem('外连接')
        self.comboBox.addItem('交叉连接')
        # 默认显示外连接
        self.comboBox.setCurrentText('外连接')
        # 将下拉框的选中项更改连接到处理函数
        self.comboBox.currentIndexChanged.connect(self.on_combobox_changed)
        button_layout.addWidget(self.comboBox)


        self.execute_button = QPushButton('Execute', self)
        self.exit_button = QPushButton('Exit', self)
        self.execute_button.clicked.connect(self.execute_action)
        self.exit_button.clicked.connect(self.close)
        button_layout.addWidget(self.execute_button)
        button_layout.addWidget(self.exit_button)

        layout.addLayout(id_layout)
        layout.addLayout(file1_layout)
        layout.addLayout(file2_layout)
        layout.addLayout(output_layout)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def on_combobox_changed(self):
        # 处理选中项更改事件
        selected_option = self.comboBox.currentText()
        if selected_option == '外连接':
            self.option = 'outer'
        elif selected_option == '左连接':
            self.option = 'left'
        elif selected_option == '右连接':
            self.option = 'right'
        elif selected_option == '内连接':
            self.option = 'inner'
        elif selected_option == '交叉连接':
            self.option == 'cross'
        else:
            self.option == 'outer'

    def pick_file1(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File 1", "", "Excel Files (*.xlsx);;All Files (*)", options=options)
        print(file_path)
        self.file1_edit.setText(file_path)

    def pick_file2(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File 2", "", "Excel Files (*.xlsx);;All Files (*)", options=options)
        self.file2_edit.setText(file_path)

    def pick_output_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        self.output_edit.setText(folder)

    def show_custom_dialog(self):
        dialog = QDialog()
        dialog.setWindowTitle("自定义弹出框")
        dialog.setGeometry(200, 200, 300, 100)

        label = QLabel("结果已输出", dialog)
        label.setGeometry(20, 20, 260, 30)

        ok_button = QPushButton("确定", dialog)
        ok_button.setGeometry(110, 60, 80, 30)
        ok_button.clicked.connect(dialog.accept)

        dialog.exec_()
    def execute_action(self):
        print(self.file1_edit.text())
        print(self.file2_edit.text())

        # 读取第一个Excel文件
        file1_df = pd.read_excel(self.file1_edit.text())

        # 读取第二个Excel文件
        file2_df = pd.read_excel(self.file2_edit.text())

        # 指定用于匹配的列名称
        match_column_name = 'id' if self.id_edit.text() == '' else self.id_edit.text()
        print(match_column_name)
        print(self.option)

        # 合并两个数据帧，使用 left join
        merged_df = file1_df.merge(file2_df, on=match_column_name, how=self.option)

        # 填充 NaN 值，以防止缺少匹配的行
        merged_df = merged_df.fillna('')

        # 保存合并后的数据到新的 Excel 文件
        merged_df.to_excel(self.output_edit.text() + '/merged_data.xlsx', index=False)

        self.show_custom_dialog()

def main():
    app = QApplication(sys.argv)
    window = FilePickerApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
