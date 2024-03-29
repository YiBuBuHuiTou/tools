# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(700, 650)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(700, 650))
        MainWindow.setMaximumSize(QtCore.QSize(705, 650))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.office_config = QtWidgets.QFrame(self.centralwidget)
        self.office_config.setGeometry(QtCore.QRect(10, 10, 661, 561))
        self.office_config.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.office_config.setFrameShadow(QtWidgets.QFrame.Raised)
        self.office_config.setObjectName("office_config")
        self.data_store = QtWidgets.QGroupBox(self.office_config)
        self.data_store.setGeometry(QtCore.QRect(0, 130, 631, 361))
        self.data_store.setObjectName("data_store")
        self.offline_config = QtWidgets.QGroupBox(self.data_store)
        self.offline_config.setGeometry(QtCore.QRect(0, 70, 521, 71))
        self.offline_config.setObjectName("offline_config")
        self.layoutWidget = QtWidgets.QWidget(self.offline_config)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 30, 471, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.local_data = QtWidgets.QLineEdit(self.layoutWidget)
        self.local_data.setMinimumSize(QtCore.QSize(200, 0))
        self.local_data.setStyleSheet("QLineEdit{\n"
"border-top-width:0px;\n"
"border-left-width:0px;\n"
"border-right-width:0px;\n"
"}")
        self.local_data.setObjectName("local_data")
        self.horizontalLayout_3.addWidget(self.local_data)
        self.data_dir = QtWidgets.QPushButton(self.layoutWidget)
        self.data_dir.setObjectName("data_dir")
        self.horizontalLayout_3.addWidget(self.data_dir)
        self.online_config = QtWidgets.QGroupBox(self.data_store)
        self.online_config.setGeometry(QtCore.QRect(0, 150, 219, 211))
        self.online_config.setObjectName("online_config")
        self.layoutWidget1 = QtWidgets.QWidget(self.online_config)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 22, 201, 170))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)
        self.db_host = QtWidgets.QLineEdit(self.layoutWidget1)
        self.db_host.setObjectName("db_host")
        self.gridLayout_2.addWidget(self.db_host, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)
        self.db_category = QtWidgets.QComboBox(self.layoutWidget1)
        self.db_category.setObjectName("db_category")
        self.db_category.addItem("")
        self.db_category.addItem("")
        self.gridLayout_2.addWidget(self.db_category, 0, 1, 1, 1)
        self.db_port = QtWidgets.QLineEdit(self.layoutWidget1)
        self.db_port.setObjectName("db_port")
        self.gridLayout_2.addWidget(self.db_port, 2, 1, 1, 1)
        self.db_username = QtWidgets.QLineEdit(self.layoutWidget1)
        self.db_username.setObjectName("db_username")
        self.gridLayout_2.addWidget(self.db_username, 4, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 3, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 4, 0, 1, 1)
        self.db_name = QtWidgets.QLineEdit(self.layoutWidget1)
        self.db_name.setObjectName("db_name")
        self.gridLayout_2.addWidget(self.db_name, 3, 1, 1, 1)
        self.db_password = QtWidgets.QLineEdit(self.layoutWidget1)
        self.db_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.db_password.setObjectName("db_password")
        self.gridLayout_2.addWidget(self.db_password, 5, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 5, 0, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(self.data_store)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 22, 211, 18))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.offline = QtWidgets.QRadioButton(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.offline.sizePolicy().hasHeightForWidth())
        self.offline.setSizePolicy(sizePolicy)
        self.offline.setObjectName("offline")
        self.horizontalLayout.addWidget(self.offline)
        self.online = QtWidgets.QRadioButton(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.online.sizePolicy().hasHeightForWidth())
        self.online.setSizePolicy(sizePolicy)
        self.online.setObjectName("online")
        self.horizontalLayout.addWidget(self.online)
        self.user_info = QtWidgets.QFrame(self.office_config)
        self.user_info.setGeometry(QtCore.QRect(20, 0, 195, 92))
        self.user_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.user_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.user_info.setObjectName("user_info")
        self.layoutWidget3 = QtWidgets.QWidget(self.office_config)
        self.layoutWidget3.setGeometry(QtCore.QRect(230, 10, 84, 54))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 0, 0, 1, 1)
        self.cycle = QtWidgets.QSpinBox(self.layoutWidget3)
        self.cycle.setMinimum(1)
        self.cycle.setMaximum(3600)
        self.cycle.setObjectName("cycle")
        self.gridLayout_3.addWidget(self.cycle, 0, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 1, 0, 2, 2)
        self.delay = QtWidgets.QSpinBox(self.layoutWidget3)
        self.delay.setMaximum(3599)
        self.delay.setObjectName("delay")
        self.gridLayout_3.addWidget(self.delay, 2, 1, 1, 1)
        self.description = QtWidgets.QPlainTextEdit(self.office_config)
        self.description.setGeometry(QtCore.QRect(360, 10, 281, 71))
        self.description.setObjectName("description")
        self.layoutWidget4 = QtWidgets.QWidget(self.office_config)
        self.layoutWidget4.setGeometry(QtCore.QRect(20, 10, 177, 111))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget4)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.job_number = QtWidgets.QLineEdit(self.layoutWidget4)
        self.job_number.setText("")
        self.job_number.setObjectName("job_number")
        self.gridLayout.addWidget(self.job_number, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget4)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.user_name = QtWidgets.QLineEdit(self.layoutWidget4)
        self.user_name.setEnabled(True)
        self.user_name.setAcceptDrops(False)
        self.user_name.setStyleSheet("border-top-width:0px;\n"
"border-left-width:0px;\n"
"border-right-width:0px;")
        self.user_name.setText("")
        self.user_name.setReadOnly(False)
        self.user_name.setObjectName("user_name")
        self.gridLayout.addWidget(self.user_name, 0, 1, 1, 1)
        self.email = QtWidgets.QLineEdit(self.layoutWidget4)
        self.email.setObjectName("email")
        self.gridLayout.addWidget(self.email, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 3, 0, 1, 1)
        self.tenant = QtWidgets.QComboBox(self.layoutWidget4)
        self.tenant.setEditable(True)
        self.tenant.setObjectName("tenant")
        self.gridLayout.addWidget(self.tenant, 3, 1, 1, 1)
        self.widget = QtWidgets.QWidget(self.office_config)
        self.widget.setGeometry(QtCore.QRect(0, 500, 661, 61))
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.attendance = QtWidgets.QGroupBox(self.widget)
        self.attendance.setObjectName("attendance")
        self.layoutWidget5 = QtWidgets.QWidget(self.attendance)
        self.layoutWidget5.setGeometry(QtCore.QRect(20, 30, 307, 22))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget5)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.start_time = QtWidgets.QTimeEdit(self.layoutWidget5)
        self.start_time.setObjectName("start_time")
        self.horizontalLayout_2.addWidget(self.start_time)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget5)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        self.end_time = QtWidgets.QTimeEdit(self.layoutWidget5)
        self.end_time.setObjectName("end_time")
        self.horizontalLayout_2.addWidget(self.end_time)
        self.gridLayout_4.addWidget(self.attendance, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget6 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget6.setGeometry(QtCore.QRect(10, 30, 124, 22))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.remind = QtWidgets.QRadioButton(self.layoutWidget6)
        self.remind.setObjectName("remind")
        self.horizontalLayout_4.addWidget(self.remind)
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.unremind = QtWidgets.QRadioButton(self.layoutWidget6)
        self.unremind.setObjectName("unremind")
        self.horizontalLayout_4.addWidget(self.unremind)
        self.gridLayout_4.addWidget(self.groupBox, 0, 1, 1, 1)
        self.layoutWidget7 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget7.setGeometry(QtCore.QRect(510, 570, 158, 41))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget7)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.save_btn = QtWidgets.QPushButton(self.layoutWidget7)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout_5.addWidget(self.save_btn)
        self.exit_btn = QtWidgets.QPushButton(self.layoutWidget7)
        self.exit_btn.setObjectName("exit_btn")
        self.horizontalLayout_5.addWidget(self.exit_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.external_tools = QtWidgets.QMenu(self.menubar)
        self.external_tools.setObjectName("external_tools")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.personal = QtWidgets.QAction(MainWindow)
        self.personal.setObjectName("personal")
        self.office = QtWidgets.QAction(MainWindow)
        self.office.setObjectName("office")
        self.add_tool = QtWidgets.QAction(MainWindow)
        self.add_tool.setObjectName("add_tool")
        self.auto_on_off = QtWidgets.QAction(MainWindow)
        self.auto_on_off.setObjectName("auto_on_off")
        self.alarm = QtWidgets.QAction(MainWindow)
        self.alarm.setObjectName("alarm")
        self.about = QtWidgets.QAction(MainWindow)
        self.about.setObjectName("about")
        self.menu.addAction(self.personal)
        self.menu.addAction(self.office)
        self.external_tools.addAction(self.add_tool)
        self.menu_2.addAction(self.about)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.external_tools.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "window 监听"))
        self.data_store.setTitle(_translate("MainWindow", "mode"))
        self.offline_config.setTitle(_translate("MainWindow", "本地配置"))
        self.label_6.setText(_translate("MainWindow", "数据存放位置"))
        self.data_dir.setText(_translate("MainWindow", "选择"))
        self.online_config.setTitle(_translate("MainWindow", "远程数据库配置"))
        self.label_9.setText(_translate("MainWindow", "端口"))
        self.label_7.setText(_translate("MainWindow", "数据库种类"))
        self.label_8.setText(_translate("MainWindow", "数据库ip"))
        self.db_category.setItemText(0, _translate("MainWindow", "Mysql"))
        self.db_category.setItemText(1, _translate("MainWindow", "Mariadb"))
        self.label_10.setText(_translate("MainWindow", "数据库名"))
        self.label_11.setText(_translate("MainWindow", "用户名"))
        self.label_12.setText(_translate("MainWindow", "密码"))
        self.label_4.setText(_translate("MainWindow", "模式选择"))
        self.offline.setText(_translate("MainWindow", "离线"))
        self.online.setText(_translate("MainWindow", "在线"))
        self.label_14.setText(_translate("MainWindow", "周期"))
        self.label_15.setText(_translate("MainWindow", "延迟"))
        self.description.setPlaceholderText(_translate("MainWindow", "个性签名！！！"))
        self.label_2.setText(_translate("MainWindow", "工号："))
        self.label.setText(_translate("MainWindow", "姓名："))
        self.label_3.setText(_translate("MainWindow", "邮箱："))
        self.label_16.setText(_translate("MainWindow", "组别"))
        self.attendance.setTitle(_translate("MainWindow", "考勤批次"))
        self.label_5.setText(_translate("MainWindow", "上班时间"))
        self.label_13.setText(_translate("MainWindow", "下班时间"))
        self.groupBox.setTitle(_translate("MainWindow", "加班提醒"))
        self.remind.setText(_translate("MainWindow", "是"))
        self.unremind.setText(_translate("MainWindow", "否"))
        self.save_btn.setText(_translate("MainWindow", "保存"))
        self.exit_btn.setText(_translate("MainWindow", "退出"))
        self.menu.setTitle(_translate("MainWindow", "模式"))
        self.external_tools.setTitle(_translate("MainWindow", "小工具"))
        self.menu_2.setTitle(_translate("MainWindow", "帮助"))
        self.personal.setText(_translate("MainWindow", "个人"))
        self.office.setText(_translate("MainWindow", "办公"))
        self.add_tool.setText(_translate("MainWindow", "添加"))
        self.auto_on_off.setText(_translate("MainWindow", "定时开关机"))
        self.alarm.setText(_translate("MainWindow", "闹钟"))
        self.about.setText(_translate("MainWindow", "关于"))

from ui import resources_rc
