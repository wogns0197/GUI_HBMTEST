# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analyzing_RA.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Analyzing(object):
    def setupUi(self, analyzing):
        analyzing.setObjectName("analyzing")
        analyzing.resize(360, 147)
        self.centralwidget = QtWidgets.QWidget(analyzing)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 361, 121))
        self.textBrowser.setObjectName("textBrowser")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 120, 331, 23))
        self.progressBar.setMaximum(3)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        analyzing.setCentralWidget(self.centralwidget)

        self.retranslateUi(analyzing)
        QtCore.QMetaObject.connectSlotsByName(analyzing)

    def retranslateUi(self, analyzing):
        _translate = QtCore.QCoreApplication.translate
        analyzing.setWindowTitle(_translate("analyzing", "Analyzing_RA"))
        self.textBrowser.setHtml(_translate("analyzing", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600;\">Analyzing RA.....</span></p></body></html>"))

