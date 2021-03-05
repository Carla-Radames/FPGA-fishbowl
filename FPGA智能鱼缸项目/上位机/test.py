    # import serial
    #
    #
    # serialPort = "COM8"  # 串口
    # baudRate = 9600  # 波特率
    # ser = serial.Serial(serialPort, baudRate, timeout=0.5)
    # print("参数设置：串口=%s ，波特率=%d" % (serialPort, baudRate))
    #
    #
    # while 1:
    #     str = ser.readline()
    #     print(str)
    #
    # ser.close()


# # -*- coding: utf-8 -*-
# import serial
#
# serialPort = "COM8"  # 串口
# baudRate = 9600  # 波特率
# ser = serial.Serial(serialPort, baudRate, timeout=0.5)
# print("参数设置：串口=%s ，波特率=%d" % (serialPort, baudRate))
#
# demo1=b"0"#将0转换为ASCII码方便发送
# demo2=b"1"#同理
# while 1:
#     c=input('请输入指令:')
#     #c=ord(c)#将c转换为UTF-8标准数字
#     if(c=="0"):
#         ser.write(demo1)#ser.write在于向串口中写入数据
#         print("you have 0")
#     if(c=="1"):
#         ser.write(demo2)

import sys
import serial

from PyQt5 import QtWidgets,QtCore
from Russion import Tetris #尝试导入一个class

from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication,\
    QPushButton,QLineEdit,QVBoxLayout , QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
serialPort = "COM8"  # 串口
baudRate = 9600  # 波特率
ser = serial.Serial(serialPort, baudRate, timeout=0.5)
print("参数设置：串口=%s ，波特率=%d" % (serialPort, baudRate))
demo1=b"0"#将0转换为ASCII码方便发送
demo2=b"1"#同理

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        #菜单栏
        #动作可以附加到菜单栏/工具栏上
        exitAct = QAction(QIcon('exit24.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        #exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)

        russionAct=QAction('Russian',self)
        russionAct.setShortcut('ctrl+R')
        #russionAct.setStatusTip('Play Tetris')
        russionAct.triggered.connect(self.Russion)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        fileMenu.addAction(russionAct)

        #文本显示
        line1 = QLineEdit(self)
        line1.move(100, 400)#位置不对，太短啦
        line1.setStyleSheet(
            '''QLineEdit{
                border:1px solid gray;
                width:300px;
                border-radius:10px;
                padding:2px 4px;
            }''')

        #按钮
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)  # instance 事例,注意这里quit后面没有括号!!!
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(600, 550)

        qbtn1 = QPushButton('Send1', self)
        qbtn1.clicked.connect(self.send1)  # 联系按下按钮的行为和某个函数
        qbtn1.resize(qbtn.sizeHint())
        qbtn1.move(400, 550)

        qbtn0 = QPushButton('Send0', self)
        qbtn0.clicked.connect(self.send0)  #
        qbtn0.resize(qbtn.sizeHint())
        qbtn0.move(200, 550)
        #color #默认为字体颜色
        qbtn.setStyleSheet('''
          QPushButton{
            border:1.5px solid black;
            color:red;
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
        qbtn0.setStyleSheet('''
          QPushButton{
            border:1.5px solid black;
            color:blue;
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
        qbtn1.setStyleSheet('''
          QPushButton{
            border:1.5px solid black;
            color:green;
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


        self.setGeometry(700, 200, 700, 600)
        self.setWindowTitle('Main window')
        self.show()
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

    def send1(self):
        ser.write(demo2)
    def send0(self):
        ser.write(demo1)
    def Russion(self):
        #调用了同一个根目录下另一个.py文件
        self.form2 = QtWidgets.QWidget()
        self.ui2 = Tetris()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())