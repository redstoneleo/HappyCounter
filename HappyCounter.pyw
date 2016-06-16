from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from UI.MainWindow import MainWindow


def main():
    import sys
    app = QApplication(sys.argv)

    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()  # 变成这个样子似乎不出错了哦         Python has stopped working
