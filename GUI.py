import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QDesktopWidget
from PyQt5.QtCore import QSize

from PyQt5.QtWidgets import QPushButton

from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QLabel

import search



class HelloWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(800, 600))
        self.setWindowTitle("THE BEST GODDAMN SEARCH ENGINE")

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        gridLayout = QGridLayout(self)
        centralWidget.setLayout(gridLayout)

        title = QLabel(" THE BEST GODDAMN SEARCH ENGINE ", self)
        title.setAlignment(QtCore.Qt.AlignTop)
        gridLayout.addWidget(title, 0, 0)


        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Search:')
        self.line = QLineEdit(self)
        # position
        self.line.move(100, 35)
        # size
        self.line.resize(400, 32)
        self.nameLabel.move(35, 25)

        pybutton = QPushButton('Search', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(100,32)
        pybutton.move(500, 30)

        self.body = QLabel(self)
        self.body.setText('results: ')
        self.body.move(35, 80)
        self.body.resize(400,200)

    def clickMethod(self):
        print('Searching ' + self.line.text())
        self.display()

    def display(self):
        result = "we should display url later but i dont have that rn\nresults: \n"
        for (k,v) in sorted(search.get_tfidf(search.get_postings(self.line.text())).items(), key=lambda kv: kv[1], reverse=True)[0:10]:
            result += "DOC ID: " + str(k) + "\n"
        self.body.setText(result)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()
    sys.exit( app.exec_() )