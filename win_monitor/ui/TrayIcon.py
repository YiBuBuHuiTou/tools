from PyQt5 import QtWidgets, QtGui, QtCore
import os


class TrayIcon(QtWidgets.QSystemTrayIcon):

    def __init__(self, main_window, parent=None):
        super(TrayIcon, self).__init__(parent)
        # 设置主界面
        self.main_ui = main_window
        # 创建托盘菜单
        self.create_menu()
        # 设置托盘图标
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setIcon(icon)
        # 托盘图标点击事件
        self.activated.connect(self.activated_icon)
        # 设置托盘图标
        self.setToolTip("系统监测")

    # 创建托盘图标右击菜单
    def create_menu(self):
        self.menu = QtWidgets.QMenu()
        # 右击菜单项
        # self.action_open = QtWidgets.QAction("恢复", self, triggered=self.open_main_window)
        self.action_attendance = QtWidgets.QAction("查看考勤记录", self, triggered=self.show_attendance)
        self.action_exit = QtWidgets.QAction("退出", self, triggered=self.exit)
        # 追加到菜单里
        # self.menu.addAction(self.action_open)
        self.menu.addAction(self.action_attendance)
        self.menu.addAction(self.action_exit)
        self.setContextMenu(self.menu)

    # 激活图标
    def activated_icon(self, reason):
        # 鼠标左键单击
        if reason == 3:
            # 显示主界面
            self.open_main_window()
        # 鼠标右键
        elif reason == 1:
            pass

    # 打开主界面
    def open_main_window(self):
        self.main_ui.showNormal()
        self.main_ui.activateWindow()

    # 显示考勤
    def show_attendance(self):
         # TODO
        pass

    # 弹框，用于提示加班 # TODO
    def show_pop_tip(self):
        # 右下角泡泡弹框
        self.showMessage("提示", "已最小化到托盘", self.Mess)

    # 退出程序
    def exit(self):
        # 隐藏托盘图标
        self.setVisible(False)
        # 关闭主程序
        self.main_ui.on_click_exit_handler()
