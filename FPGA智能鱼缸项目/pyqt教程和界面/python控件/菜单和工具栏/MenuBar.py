#菜单栏
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')#简单说明，一般为操作缩写
        exitAct.setStatusTip('Exit application')#statusbar的简单说明
        exitAct.triggered.connect(qApp.quit)#这个事件与quit行为相关联

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')#增加菜单
        fileMenu.addAction(exitAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())