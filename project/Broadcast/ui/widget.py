# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1201, 1090)
        self.Ip = QtWidgets.QLineEdit(Form)
        self.Ip.setGeometry(QtCore.QRect(140, 190, 261, 71))
        self.Ip.setObjectName("Ip")
        self.Next = QtWidgets.QPushButton(Form)
        self.Next.setGeometry(QtCore.QRect(430, 190, 131, 71))
        self.Next.setObjectName("Next")
        self.Send = QtWidgets.QPushButton(Form)
        self.Send.setGeometry(QtCore.QRect(590, 190, 181, 71))
        self.Send.setObjectName("Send")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 200, 108, 24))
        self.label.setObjectName("label")
        self.Sends_listView = QtWidgets.QListView(Form)
        self.Sends_listView.setGeometry(QtCore.QRect(110, 410, 531, 551))
        self.Sends_listView.setObjectName("Sends_listView")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 360, 211, 24))
        self.label_2.setObjectName("label_2")
        self.Port = QtWidgets.QLineEdit(Form)
        self.Port.setGeometry(QtCore.QRect(140, 270, 161, 71))
        self.Port.setObjectName("Port")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 290, 108, 24))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        self.Ip.editingFinished.connect(Form.Ip_edit_finish) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Next.setText(_translate("Form", "下一个"))
        self.Send.setText(_translate("Form", "发送"))
        self.label.setText(_translate("Form", "IP:"))
        self.label_2.setText(_translate("Form", "已经发送的列表:"))
        self.label_3.setText(_translate("Form", "Port"))
