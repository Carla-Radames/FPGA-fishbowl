# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '上位机2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Russion import Tetris
import sys
import time
#import os
# smtplib 用于邮件的发信动作
import smtplib
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header
from PyQt5.QtCore import QFile
from PyQt5.QtCore import QTimer

#下一步：导入serial库,尝试连接串口
import serial
flag = 1;
serialPort = "COM3"  # 串口
baudRate = 9600  # 波特率
ser = serial.Serial(serialPort, baudRate, timeout=0.5)
#只要能读到一条，就会停止ser
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #申明这是一个全局变量
        global serialPort
        global baudRate
        global ser
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
        #按钮
        self.Mailbutton = QtWidgets.QPushButton(self.centralwidget)
        self.Mailbutton.setObjectName("Mailbutton")
        self.Mailbutton.clicked.connect(self.sendmail)

        self.horizontalLayout_button1.addWidget(self.Mailbutton)
        self.horizontalLayout_button2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_button2.setObjectName("horizontalLayout_button2")
        #button
        self.Databutton = QtWidgets.QPushButton(self.centralwidget)
        self.Databutton.setObjectName("Databutton")
        self.Databutton.clicked.connect(self.savefile)#尝试保存到文件
        # 联系按下按钮的行为和某个函数在这里可行


        self.horizontalLayout_button2.addWidget(self.Databutton)
        self.horizontalLayout_button1.addLayout(self.horizontalLayout_button2)
        self.horizontalLayout_button3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_button3.setObjectName("horizontalLayout_button3")

        self.Exitbutton = QtWidgets.QPushButton(self.centralwidget)
        self.Exitbutton.setObjectName("Exitbutton")
        self.Exitbutton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        #布局
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
        #菜单栏设置
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
        self.actionExit.setShortcut('Ctrl+Q')
        self.actionExit.setStatusTip('Exit application')
        self.actionExit.triggered.connect(self.close)

        self.actionRussion = QtWidgets.QAction(MainWindow)
        self.actionRussion.setObjectName("actionRussion")
        self.actionRussion.setShortcut('ctrl+R')
        self.actionRussion.setStatusTip('Play Tetris')
        self.actionRussion.triggered.connect(self.Russion)

        self.menu.addAction(self.actionExit)
        self.menu.addAction(self.actionRussion)
        self.menubar.addAction(self.menu.menuAction())

        #lineEdit连接到serial库
        # self.lineEdit_user
        # self.lineEdit_kilo
        # self.lineEdit_temp
        # self.lineEdit_humi
        # self.lineEdit_pres
        file = open("user.txt", "r+")
        self.lineEdit_user.setText(file.read())#理论上可以在setupUi里setText
        file.close()


        # 自己的代码部分,CSS美化
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
        self.Mailbutton.setStyleSheet('''
          QPushButton{
            border:1.5px solid black;
            color:#8a2be2;
            border-radius:10px;
            font-size:16px;
            font-family:Microsoft YaHei;
            font-weight: bold;
            height:40px;
            padding-left:5px;
            padding-right:10px;
            text-align:left;
          }
          QPushButton:hover{
            color:black;
            border:1px solid #F3F3F5;
            border-radius:10px;
            background:LightGray;
          }
        ''')
        self.Databutton.setStyleSheet('''
          QPushButton{
            border:1.5px solid black;
            color:#20b2aa;
            border-radius:10px;
            font-size:16px;
            font-family:Microsoft YaHei;
            font-weight: bold;
            height:40px;
            padding-left:5px;
            padding-right:10px;
            text-align:left;
          }
          QPushButton:hover{
            color:black;
            border:1px solid #F3F3F5;
            border-radius:10px;
            background:LightGray;
          }
        ''')
        self.Exitbutton.setStyleSheet('''
          QPushButton{
            border:1.5px solid black;
            color:#daa520;
            border-radius:10px;
            font-size:16px;
            font-family:Microsoft YaHei;
            font-weight: bold;
            height:40px;
            padding-left:5px;
            padding-right:10px;
            text-align:left;
          }
          QPushButton:hover{
            color:black;
            border:1px solid #F3F3F5;
            border-radius:10px;
            background:LightGray;
          }
        ''')
        global flag
        if (flag):
            self.starttimer()
            flag=0


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def starttimer(self):
        # 定时器更新函数：refresh
        #循环计时
        self.timer = QTimer()
        self.timer.timeout.connect(self.refresh)
        self.timer.start(1000)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "欢迎使用智能鱼缸系统"))
        self.Title.setText(_translate("MainWindow", "测试系统"))
        self.Name.setText(_translate("MainWindow", "使用人"))
        self.Humi.setText(_translate("MainWindow", "湿度(%)"))
        self.Pres.setText(_translate("MainWindow", "气压(Pa)"))
        self.Temp.setText(_translate("MainWindow", "温度(°C)"))
        self.Kilo.setText(_translate("MainWindow", "质量(kg)"))
        self.Mailbutton.setText(_translate("MainWindow", "发送邮件"))
        self.Databutton.setText(_translate("MainWindow", "修改用户"))
        self.Exitbutton.setText(_translate("MainWindow", "退出"))

        self.menu.setTitle(_translate("MainWindow", "开始"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionRussion.setText(_translate("MainWindow", "Russion"))

    def savefile(self):
        self.savetext=self.lineEdit_user.text()
        print(self.savetext)
        file=open("user.txt","r+")
        file.write(self.savetext)
        file.close()

    def Russion(self):
        #调用了同一个根目录下另一个.py文件
        self.form2 = QtWidgets.QWidget()
        self.ui2 = Tetris()
    def sendmail(self):
        #os.system('python Mail.py')#按键可以了，这是直接执行另一个纯代码文本的好方法
        # 用于构建邮件头

        # 发信方的信息：发信邮箱，QQ 邮箱授权码
        from_addr = '1967724180@qq.com'
        password = 'nmqzdjvogqgkbihc'

        # 收信方邮箱3178627218
        to_addr = '3178627218@qq.com'

        # 发信服务器
        smtp_server = 'smtp.qq.com'

        # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
        text='使用人： '+self.lineEdit_user.text()+'\n'+'温度： '+self.lineEdit_temp.text()+'\n'+ \
             '湿度： ' + self.lineEdit_humi.text() + '\n' +'质量： '+self.lineEdit_kilo.text()+'\n'+ \
             '压强： ' + self.lineEdit_pres.text() + '\n'+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+ '\n'

        #var = 'This is a message from TangLiyuan\'s father'
        msg = MIMEText(text, 'plain', 'utf-8')

        # 邮件头信息
        msg['From'] = Header(from_addr)
        msg['To'] = Header(to_addr)
        msg['Subject'] = Header('python test')

        # 开启发信服务，这里使用的是加密传输
        server = smtplib.SMTP_SSL(smtp_server)
        server.connect(smtp_server, 465)
        # 登录发信邮箱
        server.login(from_addr, password)
        # 发送邮件
        server.sendmail(from_addr, to_addr, msg.as_string())
        # 关闭服务器
        server.quit()
    def close(self):
        exit()
    def refresh(self):
        #print('refresh')  # 这一块没有执行?
        tmp = ser.readline()
        str=tmp.decode()
        print(str)
        #压强全部是数字 温度第三个字节是小数点 湿度后四位都是0 重量第二位是小数点
        if (str):
            if (str[2] == '.'):
                ui.lineEdit_temp.setText(str)
            if (str[-4:] == '0000'):
                ui.lineEdit_humi.setText(str[0:2])
            if (str[1] == '.'):
                ui.lineEdit_kilo.setText(str)
            if ((str.isdigit())&(str[-4:] != '0000')):
                ui.lineEdit_pres.setText(str)

if __name__ == "__main__":
    # 不知道这段代码能不能放这里,希望ser位置没放错……


    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()    # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Ui_MainWindow()                          # ui是你创建的ui类的实例化对象
    ui.setupUi(MainWindow)                  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
    MainWindow.show()                       # 执行QMainWindow的show()方法，显示这个QMainWindow



    sys.exit(app.exec_())                   # 使用exit()或者点击关闭按钮退出QApplication
