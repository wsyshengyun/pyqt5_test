# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'some.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1115, 984)
        self.pushButton_start = QtWidgets.QPushButton(Form)
        self.pushButton_start.setGeometry(QtCore.QRect(750, 160, 150, 46))
        self.pushButton_start.setObjectName("pushButton_start")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(70, 40, 431, 391))
        self.listWidget.setObjectName("listWidget")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(90, 460, 411, 361))
        self.textEdit.setObjectName("textEdit")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(640, 340, 401, 531))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton_stop = QtWidgets.QPushButton(Form)
        self.pushButton_stop.setGeometry(QtCore.QRect(760, 230, 150, 46))
        self.pushButton_stop.setObjectName("pushButton_stop")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_start.setText(_translate("Form", "start"))
        self.pushButton_stop.setText(_translate("Form", "stop"))
