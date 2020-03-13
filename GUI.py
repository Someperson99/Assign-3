import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QDesktopWidget
from PyQt5.QtCore import QSize

from PyQt5.QtWidgets import QPushButton

from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QLabel

import search
from json_handler import get_json_content
import os
from time import time

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
        pybutton.show()

        self.body = QLabel(self)
        self.body.setText('results: ')
        self.body.move(35, 65)

        #depending on where you have the urldict.json stored you're going to want
        #to change this
        self.path = "C:\\Users\\geryj\\Documents\\Index Copy"



    def clickMethod(self):
        print('Searching ' + self.line.text())
        self.display()
        self.body.update()
        self.body.repaint()
        pybutton = QPushButton('Search', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(100,32)
        pybutton.move(500, 30)
        self.body.update()
        pybutton.show()




    def display(self):
        current_dir = os.getcwd()
        json = get_json_content(self.path + "urldict.json")
        x1 = time()
        try:
            list_posting = search.get_tfidf(search.merge_postings(search.get_postings(self.line.text().lower()))).items()
        except FileNotFoundError:
            list_posting = []
        finally:
            result = "Searching " + self.line.text().lower() + "... " + str(len(list_posting)) + " total results found. Top 10 results: \n\n"
            for (k, v) in sorted(list_posting, key=lambda kv: kv[1], reverse=True)[0:10]:
                title = json[str(k)][1].replace("\n", '')[:180]
                result += "URL:     " + json[str(k)][0] + "\n" + "TITLE:  " + title + "\n\n"
            x2 = time()
            print(x2-x1)
            result+= "time taken to search: " + str((x2-x1))
            self.body.setText(result)
            self.body.move(5, -150)
            self.body.resize(1500,1000)
            self.body.update()
            self.body.show()
            self.body.repaint()






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()
    sys.exit( app.exec_() )