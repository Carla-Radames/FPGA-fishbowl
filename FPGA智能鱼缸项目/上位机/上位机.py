# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '上位机.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication,\
    QPushButton,QLineEdit,QVBoxLayout , QHBoxLayout
from PyQt5.QtGui import QIcon
from Russion import Tetris
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(657, 479)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.verticalLayout_2.addWidget(self.Title)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout1.setObjectName("horizontalLayout1")
        self.Name = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Name.setFont(font)
        self.Name.setObjectName("Name")
        self.horizontalLayout1.addWidget(self.Name)
        self.lineEdit_user = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.horizontalLayout1.addWidget(self.lineEdit_user)
        self.verticalLayout.addLayout(self.horizontalLayout1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Humi = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Humi.setFont(font)
        self.Humi.setObjectName("Humi")
        self.horizontalLayout_3.addWidget(self.Humi)
        self.lineEdit_humi = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_humi.setObjectName("lineEdit_humi")
        self.horizontalLayout_3.addWidget(self.lineEdit_humi)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Pres = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Pres.setFont(font)
        self.Pres.setObjectName("Pres")
        self.horizontalLayout_4.addWidget(self.Pres)
        self.lineEdit_pres = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pres.setObjectName("lineEdit_pres")
        self.horizontalLayout_4.addWidget(self.lineEdit_pres)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Temp = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Temp.setFont(font)
        self.Temp.setObjectName("Temp")
        self.horizontalLayout.addWidget(self.Temp)
        self.lineEdit_temp = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_temp.setObjectName("lineEdit_temp")
        self.horizontalLayout.addWidget(self.lineEdit_temp)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Kilo = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Kilo.setFont(font)
        self.Kilo.setObjectName("Kilo")
        self.horizontalLayout_5.addWidget(self.Kilo)
        self.lineEdit_kilo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_kilo.setObjectName("lineEdit_kilo")
        self.horizontalLayout_5.addWidget(self.lineEdit_kilo)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_allbuttons = QtWidgets.QHBoxLayout()
        self.horizontalLayout_allbuttons.setObjectName("horizontalLayout_allbuttons")
        self.horizontalLayout_button1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_button1.setObjectName("horizontalLayout_button1")
        spacerItem = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_button1.addItem(spacerItem)
        self.Mailbutton = QtWidgets.QPushButton(self.centralwidget)
        self.Mailbutton.setObjectName("Mailbutton")
        self.horizontalLayout_button1.addWidget(self.Mailbutton)
        self.horizontalLayout_button2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_button2.setObjectName("horizontalLayout_button2")
        self.Databutton = QtWidgets.QPushButton(self.centralwidget)
        self.Databutton.setObjectName("Databutton")
        self.horizontalLayout_button2.addWidget(self.Databutton)
        self.horizontalLayout_button1.addLayout(self.horizontalLayout_button2)
        self.horizontalLayout_button3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_button3.setObjectName("horizontalLayout_button3")
        self.Exitbutton = QtWidgets.QPushButton(self.centralwidget)
        self.Exitbutton.setObjectName("Exitbutton")
        self.horizontalLayout_button3.addWidget(self.Exitbutton)
        self.horizontalLayout_button1.addLayout(self.horizontalLayout_button3)
        self.horizontalLayout_allbuttons.addLayout(self.horizontalLayout_button1)
        self.verticalLayout.addLayout(self.horizontalLayout_allbuttons)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 1)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 657, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #自己的代码部分
        self.lineEdit_user.setStyleSheet(
            '''QLineEdit{
                border:1px solid gray;
                width:300px;
                border-radius:10px;
                padding:2px 4px;
            }''')
        self.lineEdit_temp.setStyleSheet(
            '''QLineEdit{
                border:1px solid gray;
                width:300px;
                border-radius:10px;
                padding:2px 4px;
            }''')
        self.lineEdit_humi.setStyleSheet(
            '''QLineEdit{
                border:1px solid gray;
                width:300px;
                border-radius:10px;
                padding:2px 4px;
            }''')
        self.lineEdit_pres.setStyleSheet(
            '''QLineEdit{
                border:1px solid gray;
                width:300px;
                border-radius:10px;
                padding:2px 4px;
            }''')
        self.lineEdit_kilo.setStyleSheet(
            '''QLineEdit{
                border:1px solid gray;
                width:300px;
                border-radius:10px;
                padding:2px 4px;
            }''')

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 657, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionRussion = QtWidgets.QAction(MainWindow)
        self.actionRussion.setObjectName("actionRussion")
        self.menu.addAction(self.actionExit)
        self.menu.addAction(self.actionRussion)
        self.menubar.addAction(self.menu.menuAction())
        # exitAct = QAction('Exit', self)
        # exitAct.setShortcut('Ctrl+Q')
        # #exitAct.setStatusTip('Exit application')
        # exitAct.triggered.connect(self.close)
        #
        # russionAct=QAction('Russian',self)
        # russionAct.setShortcut('ctrl+R')
        # #russionAct.setStatusTip('Play Tetris')
        # russionAct.triggered.connect(self.Russion)
        #
        # self.statusBar()
        #
        # menubar = self.menuBar()
        # fileMenu = menubar.addMenu('&File')
        # fileMenu.addAction(exitAct)
        # fileMenu.addAction(russionAct)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title.setText(_translate("MainWindow", "测试系统"))
        self.Name.setText(_translate("MainWindow", "使用人"))
        self.Humi.setText(_translate("MainWindow", "湿度(%)"))
        self.Pres.setText(_translate("MainWindow", "气压(kPa)"))
        self.Temp.setText(_translate("MainWindow", "温度(°C)"))
        self.Kilo.setText(_translate("MainWindow", "质量(kg)"))
        self.Mailbutton.setText(_translate("MainWindow", "发送邮件"))
        self.Databutton.setText(_translate("MainWindow", "显示数据"))
        self.Exitbutton.setText(_translate("MainWindow", "退出"))
        self.menu.setTitle(_translate("MainWindow", "开始"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionRussion.setText(_translate("MainWindow", "Russion"))

    #自定义函数
    def Russion(self):
        #调用了同一个根目录下另一个.py文件
        self.form2 = QtWidgets.QWidget()
        self.ui2 = Tetris()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()    # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Ui_MainWindow()                          # ui是你创建的ui类的实例化对象
    ui.setupUi(MainWindow)                  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
    MainWindow.show()                       # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())                   # 使用exit()或者点击关闭按钮退出QApplication