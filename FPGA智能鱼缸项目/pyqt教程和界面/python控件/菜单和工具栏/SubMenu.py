#嵌套在主菜单中的二级、三级菜单
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        #使用QMenu创建菜单，使用QAction添加动作,树叶节点为动作，非树叶节点为子菜单
        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct)

        newMenu = QMenu('New',self)
        newAct =  QAction('New output', self)
        newMenu.addAction(newAct)

        fileMenu.addMenu(newMenu)
        fileMenu.addMenu(impMenu)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Submenu')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())