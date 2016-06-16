# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from collections import Counter
from .Ui_MainWindow import Ui_MainWindow
import os


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.countDataEdit.setPlaceholderText(
            '在此输入要统计数据，确保每个数据独占一行,例如\r\n900*77\n900*88\n786*34\n900*34\n900*77\n888*78')

    @pyqtSlot()
    def on_countButton_clicked(self):
        countData = self.countDataEdit.toPlainText().split()
        c = Counter(countData)
        countResult = c.most_common()
        print(countResult)
        text = '类型         数量{}{}'.format(os.linesep, os.linesep)
        for (name, value) in countResult:
            # print(name, value)
            text += '{}         {}{}'.format(name, value, os.linesep)
        print('-----------', repr(text))
        self.resultEdit.setText(text)

    @pyqtSlot()
    def on_about_triggered(self):
        QDesktopServices.openUrl(
            QUrl('http://mathjoy.lofter.com/post/42208d_afa1552'))
