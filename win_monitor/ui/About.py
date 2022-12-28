# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'About.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(359, 145)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(About.sizePolicy().hasHeightForWidth())
        About.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        About.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(About)
        self.label.setGeometry(QtCore.QRect(30, 20, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(About)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 141, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(About)
        self.label_3.setGeometry(QtCore.QRect(30, 70, 301, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(About)
        self.label_4.setGeometry(QtCore.QRect(30, 100, 321, 21))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "关于"))
        self.label.setText(_translate("About", "版本： 1.0"))
        self.label_2.setText(_translate("About", "许可证: MIT License"))
        self.label_3.setText(_translate("About", "Copyright (c) 2022 YiBuBuHuiTou"))
        self.label_4.setText(_translate("About", "项目地址：<a href=\"https://github.com/YiBuBuHuiTou/tools\">https://github.com/YiBuBuHuiTou/tools</a>"))

import resources_rc
