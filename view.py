# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 550)
        MainWindow.setMinimumSize(QtCore.QSize(500, 550))
        MainWindow.setMaximumSize(QtCore.QSize(500, 100110))
        MainWindow.setStyleSheet("background-color: rgb(199, 198, 200);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_Title = QtWidgets.QLabel(self.centralwidget)
        self.label_Title.setGeometry(QtCore.QRect(150, 10, 200, 15))
        self.label_Title.setMinimumSize(QtCore.QSize(200, 15))
        self.label_Title.setMaximumSize(QtCore.QSize(200, 15))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(14)
        self.label_Title.setFont(font)
        self.label_Title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Title.setObjectName("label_Title")
        self.label_Bound = QtWidgets.QLabel(self.centralwidget)
        self.label_Bound.setGeometry(QtCore.QRect(170, 30, 160, 15))
        self.label_Bound.setMinimumSize(QtCore.QSize(160, 15))
        self.label_Bound.setMaximumSize(QtCore.QSize(160, 15))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        self.label_Bound.setFont(font)
        self.label_Bound.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Bound.setObjectName("label_Bound")
        self.lineEdit_Bound = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Bound.setGeometry(QtCore.QRect(195, 50, 110, 15))
        self.lineEdit_Bound.setMinimumSize(QtCore.QSize(110, 15))
        self.lineEdit_Bound.setMaximumSize(QtCore.QSize(110, 15))
        self.lineEdit_Bound.setStyleSheet("background-color: rgb(252, 252, 252);")
        self.lineEdit_Bound.setObjectName("lineEdit_Bound")
        self.label_Primes = QtWidgets.QLabel(self.centralwidget)
        self.label_Primes.setGeometry(QtCore.QRect(75, 90, 350, 15))
        self.label_Primes.setMinimumSize(QtCore.QSize(350, 15))
        self.label_Primes.setMaximumSize(QtCore.QSize(350, 15))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_Primes.setFont(font)
        self.label_Primes.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Primes.setObjectName("label_Primes")
        self.label_Numbers = QtWidgets.QLabel(self.centralwidget)
        self.label_Numbers.setGeometry(QtCore.QRect(0, 110, 500, 440))
        self.label_Numbers.setMinimumSize(QtCore.QSize(500, 440))
        self.label_Numbers.setMaximumSize(QtCore.QSize(500, 100000))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_Numbers.setFont(font)
        self.label_Numbers.setText("")
        self.label_Numbers.setTextFormat(QtCore.Qt.PlainText)
        self.label_Numbers.setScaledContents(True)
        self.label_Numbers.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Numbers.setWordWrap(True)
        self.label_Numbers.setObjectName("label_Numbers")
        self.pushButton_Enter = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Enter.setGeometry(QtCore.QRect(220, 70, 60, 17))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        self.pushButton_Enter.setFont(font)
        self.pushButton_Enter.setObjectName("pushButton_Enter")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_Title.setText(_translate("MainWindow", "PRIME NUMBER GENERATOR"))
        self.label_Bound.setText(_translate("MainWindow", "Enter a maximum bound:"))
        self.label_Primes.setText(_translate("MainWindow", "All prime numbers less than that bound:"))
        self.pushButton_Enter.setText(_translate("MainWindow", "ENTER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
