import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):#构造函数
        super().__init__()#用父级构造器的init()方法构造自己
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)#桌面宽度约为1600,高度约为800
                                            #第1，2个参数是坐标位置(x,y)3，4个参数是界面长宽
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())