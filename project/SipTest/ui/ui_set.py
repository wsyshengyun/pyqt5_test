# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_set.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(680, 722)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 20, 623, 641))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hlay_1 = QtWidgets.QHBoxLayout()
        self.hlay_1.setObjectName("hlay_1")
        self.lab1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lab1.setObjectName("lab1")
        self.hlay_1.addWidget(self.lab1)
        self.line_sip_ip = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.line_sip_ip.setObjectName("line_sip_ip")
        self.hlay_1.addWidget(self.line_sip_ip)
        self.verticalLayout.addLayout(self.hlay_1)
        self.hlay_3 = QtWidgets.QHBoxLayout()
        self.hlay_3.setObjectName("hlay_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_2.setObjectName("textEdit_2")
        self.hlay_3.addWidget(self.textEdit_2)
        self.verticalLayout.addLayout(self.hlay_3)
        self.hlay_2 = QtWidgets.QHBoxLayout()
        self.hlay_2.setObjectName("hlay_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.hlay_2.addWidget(self.label_2)
        self.line_cfg_path = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.line_cfg_path.setObjectName("line_cfg_path")
        self.hlay_2.addWidget(self.line_cfg_path)
        self.btn_open = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_open.setObjectName("btn_open")
        self.hlay_2.addWidget(self.btn_open)
        self.verticalLayout.addLayout(self.hlay_2)
        self.hlay_4 = QtWidgets.QHBoxLayout()
        self.hlay_4.setObjectName("hlay_4")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.hlay_4.addWidget(self.label_3)
        self.line_ip_section = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.line_ip_section.setObjectName("line_ip_section")
        self.hlay_4.addWidget(self.line_ip_section)
        self.label_31 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_31.setObjectName("label_31")
        self.hlay_4.addWidget(self.label_31)
        self.line_ip_start = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.line_ip_start.setObjectName("line_ip_start")
        self.hlay_4.addWidget(self.line_ip_start)
        self.lab_32 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lab_32.setObjectName("lab_32")
        self.hlay_4.addWidget(self.lab_32)
        self.line_ip_step = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.line_ip_step.setObjectName("line_ip_step")
        self.hlay_4.addWidget(self.line_ip_step)
        self.verticalLayout.addLayout(self.hlay_4)
        self.btn_ok = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_ok.setObjectName("btn_ok")
        self.verticalLayout.addWidget(self.btn_ok)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lab1.setText(_translate("Form", "SIP服务器地址"))
        self.label_2.setText(_translate("Form", "配置文件地址"))
        self.btn_open.setText(_translate("Form", "打开"))
        self.label_3.setText(_translate("Form", "配置IP网段"))
        self.label_31.setText(_translate("Form", "起始IP值"))
        self.lab_32.setText(_translate("Form", "步进"))
        self.btn_ok.setText(_translate("Form", "保存"))
