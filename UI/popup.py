# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'popup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PopupWindow(object):
    def setupUi(self, PopupWindow):
        PopupWindow.setObjectName("PopupWindow")
        PopupWindow.resize(358, 387)
        self.centralwidget = QtWidgets.QWidget(PopupWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 40, 361, 301))
        self.textBrowser.setObjectName("textBrowser")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(100, 340, 171, 32))
        self.nextButton.setObjectName("nextButton")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 0, 361, 41))
        self.textBrowser_2.setObjectName("textBrowser_2")
        PopupWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(PopupWindow)
        self.statusbar.setObjectName("statusbar")
        PopupWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PopupWindow)
        self.nextButton.clicked.connect(PopupWindow.nbclicked)
        QtCore.QMetaObject.connectSlotsByName(PopupWindow)

    def retranslateUi(self, PopupWindow):
        _translate = QtCore.QCoreApplication.translate
        PopupWindow.setWindowTitle(_translate("PopupWindow", "PopupWindow"))
        self.nextButton.setText(_translate("PopupWindow", "Next"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PopupWindow = QtWidgets.QMainWindow()
    ui = Ui_PopupWindow()
    ui.setupUi(PopupWindow)
    PopupWindow.show()
    sys.exit(app.exec_())

