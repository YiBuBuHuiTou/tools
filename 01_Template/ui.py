import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QLineEdit, QLabel, QDialog

class FilePickerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('File Picker App')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        # File pickers
        file1_layout = QHBoxLayout()
        self.file1_edit = QLineEdit(self)

        self.file1_button = QPushButton('输入1：', self)
        self.file1_button.clicked.connect(self.pick_file1)
        file1_layout.addWidget(self.file1_button)
        file1_layout.addWidget(self.file1_edit)


        file2_layout = QHBoxLayout()
        self.file2_edit = QLineEdit(self)
        self.file2_button = QPushButton('输入2', self)
        self.file2_button.clicked.connect(self.pick_file2)
        file2_layout.addWidget(self.file2_button)
        file2_layout.addWidget(self.file2_edit)


        output_layout = QHBoxLayout()
        self.output_edit = QLineEdit(self)
        self.output_button = QPushButton('输入3', self)
        self.output_button.clicked.connect(self.pick_output_folder)
        output_layout.addWidget(self.output_button)
        output_layout.addWidget(self.output_edit)


        # Execute and Exit buttons
        button_layout = QHBoxLayout()
        self.execute_button = QPushButton('Execute', self)
        self.exit_button = QPushButton('Exit', self)
        self.execute_button.clicked.connect(self.execute_action)
        self.exit_button.clicked.connect(self.close)
        button_layout.addWidget(self.execute_button)
        button_layout.addWidget(self.exit_button)

        layout.addLayout(file1_layout)
        layout.addLayout(file2_layout)
        layout.addLayout(output_layout)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def pick_file1(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File 1", "", "Excel Files (*.xlsx);;All Files (*)", options=options)
        self.file1_edit.setText(file_path)

    def pick_file2(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File 2", "", "Excel Files (*.xlsx);;All Files (*)", options=options)
        self.file2_edit.setText(file_path)

    def pick_output_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        self.output_edit.setText(folder)

    # 弹框
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
        # Add your code to perform the desired action with the selected files and output folder here
        pass

def main():
    app = QApplication(sys.argv)
    window = FilePickerApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
