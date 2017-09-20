import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
import ytc

class Downloader(QMainWindow, ytc.Ui_MainWindow):
    def __init__(self, parent = None):
        super(Downloader, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = Downloader()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()