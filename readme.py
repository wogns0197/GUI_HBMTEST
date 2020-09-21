import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets as Qtw

class ReadMe(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)

        self.textbox = Qtw.QTextEdit()
        self.layout = Qtw.QBoxLayout(Qtw.QBoxLayout.LeftToRight, self)
        self.setLayout(self.layout)
        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("README")
        self.setGeometry(100,100,600,360)
        self.textbox.setReadOnly(True)
        self.textbox.setText("Hello, it's for explanation for gui\n"
		                        + "Let me explain about button:\n"
		                        + "There are four buttons as you can see:\n"
		                        + "At first, there is 'Mode' button, if it's not clicked, it's mode is just one chip\n"
		                        + "When it's clicked,it chages it's mode\n"
		                        + "and button's text and color are changed too\n"
		                        + "and other buttons like 'whole chip','log',and 'DRAM' are changed up to mode button\n"
		                        + "Righ console is for one chip, it means it always operates whenever mode is one chip mode or parallel mode\n"
		                        + "and Left console operate only when it's mode is parallel mode\n"
		                        + "If you want to find out log files,please read below one\n"
		                        + "\n"
		                        + "\n"
		                        + "\n"
		                        + "one chip path = '$execution_path/log.txt'\n"
		                        + "when parallel mode, you can find two log files\n"
		                        + "Fisrt one = '$execution_path/log.txt'\n"
		                        + "Second one = '$execution_path/log1.txt\n"
		                        + "thanks for reading'")
        self.layout.addWidget(self.textbox)


