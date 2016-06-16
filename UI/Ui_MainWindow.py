# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\360云盘\编程\Python\Project\HappyCounter\UI\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.countDataEdit = QtWidgets.QTextEdit(self.groupBox)
        self.countDataEdit.setObjectName("countDataEdit")
        self.verticalLayout.addWidget(self.countDataEdit)
        self.horizontalLayout.addWidget(self.groupBox)
        self.countButton = QtWidgets.QPushButton(self.centralWidget)
        self.countButton.setObjectName("countButton")
        self.horizontalLayout.addWidget(self.countButton)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.resultEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.resultEdit.setReadOnly(True)
        self.resultEdit.setObjectName("resultEdit")
        self.verticalLayout_2.addWidget(self.resultEdit)
        self.horizontalLayout.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.about = QtWidgets.QAction(MainWindow)
        self.about.setObjectName("about")
        self.menu.addAction(self.about)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hi统计"))
        self.groupBox.setTitle(_translate("MainWindow", "要统计的数据"))
        self.countButton.setText(_translate("MainWindow", "统计>>"))
        self.groupBox_2.setTitle(_translate("MainWindow", "统计结果"))
        self.resultEdit.setPlaceholderText(_translate("MainWindow", "点击“统计>>”按钮就可以在这里看到统计结果"))
        self.menu.setTitle(_translate("MainWindow", "帮助"))
        self.about.setText(_translate("MainWindow", "关于"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

