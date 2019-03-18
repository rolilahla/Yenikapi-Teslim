import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton, QLineEdit, QDialog


class Window1(QMainWindow):
    textSaved = QtCore.pyqtSignal(str)
    def __init__(self):
        super(Window1,self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("PyQt Signal Signal Emitter")
        self.home()
        self.counter = 0
    def home(self):

        self.__line=QLineEdit("howdy", self)
        self.__line.move(120,100)

        btn=QPushButton("Send Signal", self)
        btn.clicked.connect(self.send_signal)
        btn.move(0,100)

        self.show()

    def send_signal(self):
        if self.counter == 0:
            signal=self.__line.displayText()
            self.Window2=Window2(signal, self)
            self.Window2.show()
            self.textSaved.connect(self.Window2.showMessage)
            self.counter = 1
        else:
            signal = self.__line.displayText()
            self.textSaved.emit(signal)

class Window2(QDialog):
    def __init__(self, txt, window1):
        self.text = txt
        self.signal1 = window1.textSaved
        super(Window2,self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("PyQt Signal Slot Receiver")
        self.home()
        self.signal1.connect(self.showMessage)

    def home(self):
        self.line_response=QLineEdit(self.text, self)
        self.line_response.move(120,100)

    def showMessage(self, message):
        self.line_response.setText(message)

def run():
    app=QApplication(sys.argv)
    GUI=Window1()
    sys.exit(app.exec_())
run()