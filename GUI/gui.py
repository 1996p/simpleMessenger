# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(548, 451)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QLabel#line {\n"
"border: 1px solid rgb(35, 0, 70)\n"
"}\n"
"QPushButton#sendMsgBtn {\n"
"border:1px solid black;\n"
"border-top-left-radius: 12px;\n"
"border-bottom-left-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:hover#sendMsgBtn {\n"
"background-color:rgb(130, 130, 130);\n"
"border:1px solid rgb(130, 130, 130);\n"
"border-top-left-radius: 12px;\n"
"border-bottom-left-radius: 12px;\n"
"\n"
"}\n"
"\n"
"QFrame#main {\n"
"background-color:rgb(167, 213, 255);\n"
"border:1px solid rgb(167, 213, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton#closeBtn {\n"
"border:1px solid transparent;\n"
"border-radius:6px;\n"
"color:red;\n"
"font-size:20px\n"
"}\n"
"\n"
"QPushButton:hover#closeBtn {\n"
"border:1px solid red;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.main = QtWidgets.QFrame(self.centralwidget)
        self.main.setGeometry(QtCore.QRect(0, 0, 551, 451))
        self.main.setStyleSheet("")
        self.main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main.setObjectName("main")
        self.sendMsgBtn = QtWidgets.QPushButton(self.main)
        self.sendMsgBtn.setGeometry(QtCore.QRect(460, 410, 80, 27))
        self.sendMsgBtn.setMaximumSize(QtCore.QSize(93, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.sendMsgBtn.setFont(font)
        self.sendMsgBtn.setStyleSheet("")
        self.sendMsgBtn.setObjectName("sendMsgBtn")
        self.line = QtWidgets.QLabel(self.main)
        self.line.setGeometry(QtCore.QRect(-10, 60, 550, 2))
        self.line.setText("")
        self.line.setObjectName("line")
        self.textMsg = QtWidgets.QLineEdit(self.main)
        self.textMsg.setGeometry(QtCore.QRect(20, 410, 321, 31))
        self.textMsg.setObjectName("textMsg")
        self.chatWindow = QtWidgets.QPlainTextEdit(self.main)
        self.chatWindow.setGeometry(QtCore.QRect(20, 70, 511, 331))
        self.chatWindow.setReadOnly(False)
        self.chatWindow.setObjectName("chatWindow")
        self.loginField = QtWidgets.QLineEdit(self.main)
        self.loginField.setGeometry(QtCore.QRect(20, 15, 141, 31))
        self.loginField.setObjectName("loginField")
        self.passwordField = QtWidgets.QLineEdit(self.main)
        self.passwordField.setGeometry(QtCore.QRect(390, 15, 141, 31))
        self.passwordField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordField.setObjectName("passwordField")
        self.authBtn = QtWidgets.QPushButton(self.main)
        self.authBtn.setGeometry(QtCore.QRect(230, 15, 93, 31))
        self.authBtn.setObjectName("authBtn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sendMsgBtn.setText(_translate("MainWindow", "send"))
        self.authBtn.setText(_translate("MainWindow", "SIGN IN"))
