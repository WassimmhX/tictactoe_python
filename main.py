from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from tictactoe import Ui_Dialog
import sys
class mainwindow:
    def __init__(self):
        self.window = QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.p=1
        self.window.show()
        self.ui.pushButton.clicked.connect(lambda:self.change(1))
        self.ui.pushButton_2.clicked.connect(lambda:self.change(2))
        self.ui.pushButton_3.clicked.connect(lambda:self.change(3))
        self.ui.pushButton_4.clicked.connect(lambda:self.change(4))
        self.ui.pushButton_5.clicked.connect(lambda:self.change(5))
        self.ui.pushButton_6.clicked.connect(lambda:self.change(6))
        self.ui.pushButton_7.clicked.connect(lambda:self.change(7))
        self.ui.pushButton_8.clicked.connect(lambda:self.change(8))
        self.ui.pushButton_9.clicked.connect(lambda:self.change(9))
        self.ui.pushButton_10.clicked.connect(self.reset)
    def change(self,me):
        def testp():
            if self.p==1:
                self.p=2
            else:
                self.p=1

        if not ("Wins" in self.ui.label_3.text()):
            if self.p==1:
                self.ui.label_3.setText("Player2's turn")
                self.ui.label_3.setStyleSheet("font: 75 12pt \"Times New Roman\";")
                if me == 1 and self.ui.pushButton.text() == "":
                    self.ui.pushButton.setText("X")
                    testp()
                if me == 2 and self.ui.pushButton_2.text() == "":
                    self.ui.pushButton_2.setText("X")
                    testp()
                if me == 3 and self.ui.pushButton_3.text() == "":
                    self.ui.pushButton_3.setText("X")
                    testp()
                if me == 4 and self.ui.pushButton_4.text() == "":
                    self.ui.pushButton_4.setText("X")
                    testp()
                if me == 5 and self.ui.pushButton_5.text() == "":
                    self.ui.pushButton_5.setText("X")
                    testp()
                if me == 6 and self.ui.pushButton_6.text() == "":
                    self.ui.pushButton_6.setText("X")
                    testp()
                if me == 7 and self.ui.pushButton_7.text() == "":
                    self.ui.pushButton_7.setText("X")
                    testp()
                if me == 8 and self.ui.pushButton_8.text() == "":
                    self.ui.pushButton_8.setText("X")
                    testp()
                if me == 9 and self.ui.pushButton_9.text() == "":
                    self.ui.pushButton_9.setText("X")
                    testp()
            else:
                self.ui.label_3.setText("Player1's turn")
                self.ui.label_3.setStyleSheet("font: 75 12pt \"Times New Roman\";")
                if me == 1 and self.ui.pushButton.text() == "":
                    self.ui.pushButton.setText("O")
                    testp()
                if me == 2 and self.ui.pushButton_2.text() == "":
                    self.ui.pushButton_2.setText("O")
                    testp()
                if me == 3 and self.ui.pushButton_3.text() == "":
                    self.ui.pushButton_3.setText("O")
                    testp()
                if me == 4 and self.ui.pushButton_4.text() == "":
                    self.ui.pushButton_4.setText("O")
                    testp()
                if me == 5 and self.ui.pushButton_5.text() == "":
                    self.ui.pushButton_5.setText("O")
                    testp()
                if me == 6 and self.ui.pushButton_6.text() == "":
                    self.ui.pushButton_6.setText("O")
                    testp()
                if me == 7 and self.ui.pushButton_7.text() == "":
                    self.ui.pushButton_7.setText("O")
                    testp()
                if me == 8 and self.ui.pushButton_8.text() == "":
                    self.ui.pushButton_8.setText("O")
                    testp()
                if me == 9 and self.ui.pushButton_9.text() == "":
                    self.ui.pushButton_9.setText("O")
                    testp()
            t1 = self.ui.pushButton.text()
            t2 = self.ui.pushButton_2.text()
            t3 = self.ui.pushButton_3.text()
            t4 = self.ui.pushButton_4.text()
            t5 = self.ui.pushButton_5.text()
            t6 = self.ui.pushButton_6.text()
            t7 = self.ui.pushButton_7.text()
            t8 = self.ui.pushButton_8.text()
            t9 = self.ui.pushButton_9.text()
            if t1 == t2 == t3 == "X":
                self.ui.label_3.setText("***Player1 Wins***")
                self.ui.label_3.setStyleSheet("font: 75 12pt \"Times New Roman\";color:green\n")

            if t4 == t5 == t6 == "X":
                self.ui.label_3.setText("***Player1 Wins***")
                self.ui.label_3.setStyleSheet("font: 75 12pt \"Times New Roman\";color:green\n")

            if t7 == t8 == t9 == "X":
                self.ui.label_3.setText("***Player1 Wins***")
                self.ui.label_3.setStyleSheet("font: 75 12pt \"Times New Roman\";color:green\n")
            if t1 == t4 == t7 == "X":
                self.ui.label_3.setText("***Player1 Wins***")
                self.ui.label_3.setStyleSheet("font: 75 12pt \"Times New Roman\";color:green\n")

            if t5 == t2 == t8 == "X":
                self.ui.label_3.setText("***Player1 Wins***")
                self.ui.label_3.setStyleSheet("font: 75 12pt \"Times New Roman\";color:green\n")

            if t6 == t9 == t3 == "X":
                self.ui.label_3.setText("***Player1 Wins***")
                self.ui.label_3.setStyleSheet("font: 75 12pt \"Times New Roman\";color:green\n")

            if t1 == t5 == t9 == "X":
                self.ui.label_3.setText("***Player1 Wins***")
                self.ui.label_3.setStyleSheet("font: 75 12pt \"Times New Roman\";color:green\n")

            if t5 == t7 == t3 == "X":
                self.ui.label_3.setText("***Player1 Wins***")
                self.ui.label_3.setStyleSheet("font: 75 12pt \"Times New Roman\";color:green\n")

            if t1 == t2 == t3 == "O":
                self.ui.label_3.setText("***Player2 Wins***")
                self.ui.label_3.setStyleSheet("font: 75 12pt \"Times New Roman\";color:green\n")

            if t4 == t5 == t6 == "O":
                self.ui.label_3.setText("***Player2 Wins***")
                self.ui.label_3.setStyleSheet("font: 75 12pt \"Times New Roman\";color:green\n")

            if t7 == t8 == t9 == "O":
                self.ui.label_3.setText("***Player2 Wins***")
                self.ui.label_3.setStyleSheet("font: 75 12pt \"Times New Roman\";color:green\n")

            if t5 == t2 == t8 == "O":
                self.ui.label_3.setText("***Player2 Wins***")
                self.ui.label_3.setStyleSheet("font: 75 12pt \"Times New Roman\";color:green\n")
            if t1 == t4 == t7 == "O":
                self.ui.label_3.setText("***Player2 Wins***")
                self.ui.label_3.setStyleSheet("font: 75 12pt \"Times New Roman\";color:green\n")

            if t6 == t9 == t3 == "O":
                self.ui.label_3.setText("***Player2 Wins***")
                self.ui.label_3.setStyleSheet("font: 75 12pt \"Times New Roman\";color:green\n")

            if t1 == t5 == t9 == "O":
                self.ui.label_3.setText("***Player2 Wins***")
                self.ui.label_3.setStyleSheet("font: 75 12pt \"Times New Roman\";color:green\n")

            if t5 == t7 == t3 == "O":
                self.ui.label_3.setText("***Player2 Wins***")
                self.ui.label_3.setStyleSheet("font: 75 12pt \"Times New Roman\";color:green\n")

            if t1 != "" and t2 != "" and t3 != "" and t4 != "" and t5 != "" and t6 != "" and t7 != "" and t8 != "" and t9 != "":
                self.ui.label_3.setText("***its a tie***")
                self.ui.label_3.setStyleSheet("font: 75 12pt \"Times New Roman\";color:red\n")
    def reset(self):
        self.ui.label_3.setText("Player1's turn")
        self.ui.label_3.setStyleSheet("font: 75 12pt \"Times New Roman\";color:black\n")
        self.p=1
        self.ui.pushButton.setText("")
        self.ui.pushButton_2.setText("")
        self.ui.pushButton_3.setText("")
        self.ui.pushButton_4.setText("")
        self.ui.pushButton_5.setText("")
        self.ui.pushButton_6.setText("")
        self.ui.pushButton_7.setText("")
        self.ui.pushButton_8.setText("")
        self.ui.pushButton_9.setText("")

app = QtWidgets.QApplication(sys.argv)
window = mainwindow()
app.exec_()
