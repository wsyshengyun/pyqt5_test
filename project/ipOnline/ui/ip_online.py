# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ip_online.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1281, 1191)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 1241, 1051))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(12, 12, 12, 12)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lIpStart = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        self.lIpStart.setFont(font)
        self.lIpStart.setObjectName("lIpStart")
        self.horizontalLayout_2.addWidget(self.lIpStart)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lIpEnd = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lIpEnd.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lIpEnd.sizePolicy().hasHeightForWidth())
        self.lIpEnd.setSizePolicy(sizePolicy)
        self.lIpEnd.setMinimumSize(QtCore.QSize(0, 0))
        self.lIpEnd.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        self.lIpEnd.setFont(font)
        self.lIpEnd.setObjectName("lIpEnd")
        self.horizontalLayout_2.addWidget(self.lIpEnd)
        self.pushConfigIp = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(11)
        self.pushConfigIp.setFont(font)
        self.pushConfigIp.setObjectName("pushConfigIp")
        self.horizontalLayout_2.addWidget(self.pushConfigIp)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushCheckOneLine = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushCheckOneLine.setObjectName("pushCheckOneLine")
        self.horizontalLayout_2.addWidget(self.pushCheckOneLine)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(12, 12, 12, 12)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "到"))
        self.pushConfigIp.setText(_translate("Form", "保存"))
        self.pushCheckOneLine.setText(_translate("Form", "检查"))
