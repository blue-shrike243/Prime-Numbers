from view import *
from PyQt5.QtWidgets import *
import math


QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.label_Title.setHidden(False)
        self.label_Bound.setHidden(False)
        self.label_Primes.setHidden(False)
        self.label_Numbers.setHidden(False)
        self.lineEdit_Bound.setHidden(False)
        self.pushButton_Enter.setHidden(False)

        self.upper_bound = 0

        self.pushButton_Enter.clicked.connect(lambda: self.enter())

    def enter(self):
        try:
            bound = self.lineEdit_Bound.text().strip()
            upperbound = float(bound)
            self.upper_bound = int(upperbound)

        except TypeError:
            self.lineEdit_Bound.setText('')
            self.label_Bound.setText('Please enter an integer:')

        except:
            self.lineEdit_Bound.setText('')
            self.label_Bound.setText('Please enter an integer:')

        else:
            self.lineEdit_Bound.setText('')
            self.prime_func()

    def prime_func(self):
        primes = []
        composites = []

        for x in range(1, (self.upper_bound + 1)):
            limit = math.sqrt(x)

            for i in range(2, (math.ceil(limit) + 1)):
                if x == 2:
                    continue
                elif x % i == 0:
                    composites.append(x)
                else:
                    continue

            if x not in composites:
                primes.append(x)

        self.label_Numbers.setText(f'{primes}')
