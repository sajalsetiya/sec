import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QPushButton, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Photo Converter'

        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        lable  = QLabel('  Folder  ', self)
        lable.move(100,80)
        text = QTextEdit(self)
        text.resize(200,25)
        text.move(150,80)

        lable = QLabel('Width', self)
        lable.move(150,150)
        text = QTextEdit(self)
        text.resize(50, 25)
        text.move(200, 150)

        lable = QLabel('Hight', self)
        lable.move(150, 200)
        text = QTextEdit('  ',self)
        text.resize(50, 25)
        text.move(200, 200)

        button = QPushButton('Submit', self)
        button.move(250,250)

        button = QPushButton('Open', self)
        button.move(400, 80)
        button.clicked.connect(self.openFileNameDialog)

        self.show()

    def openFileNameDialog(self):
        foldername = QFileDialog.getExistingDirectory(self, 'Select Folder')
        print(foldername)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())