# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pcip.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1417, 854)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 80, 108, 24))
        self.label.setObjectName("label")
        self.box_card = QtWidgets.QComboBox(Form)
        self.box_card.setGeometry(QtCore.QRect(180, 70, 371, 30))
        self.box_card.setObjectName("box_card")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 108, 24))
        self.label_2.setObjectName("label_2")
        self.line_gateway = QtWidgets.QLineEdit(Form)
        self.line_gateway.setGeometry(QtCore.QRect(190, 120, 361, 31))
        self.line_gateway.setObjectName("line_gateway")
        self.table = QtWidgets.QTableWidget(Form)
        self.table.setGeometry(QtCore.QRect(30, 240, 711, 531))
        self.table.setMinimumSize(QtCore.QSize(0, 0))
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(580, 70, 150, 46))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 800, 1351, 24))
        self.label_3.setObjectName("label_3")
        self.btn_del = QtWidgets.QPushButton(Form)
        self.btn_del.setGeometry(QtCore.QRect(750, 430, 150, 46))
        self.btn_del.setObjectName("btn_del")
        self.btn_add = QtWidgets.QPushButton(Form)
        self.btn_add.setGeometry(QtCore.QRect(750, 490, 150, 46))
        self.btn_add.setObjectName("btn_add")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "当前网卡"))
        self.label_2.setText(_translate("Form", "默认网关"))
        self.pushButton.setText(_translate("Form", "确认修改"))
        self.label_3.setText(_translate("Form", "信息:"))
        self.btn_del.setText(_translate("Form", "删除选中"))
        self.btn_add.setText(_translate("Form", "增加一行"))