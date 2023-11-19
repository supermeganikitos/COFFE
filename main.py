import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
from PyQt5.QtWidgets import QMainWindow


class Coffe(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.load()

    def load(self):
        self.con = sqlite3.connect('coffee.sqlite3')
        cur = self.con.cursor()
        query = f"""SELECT * FROM coffee;"""
        self.result = cur.execute(query).fetchall()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах',
                                                    'описание вкуса', 'цена', 'объем упаковки'])
        for i, row in enumerate(self.result):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                if j == 3:
                    if str(elem) == '0':
                        self.tableWidget.setItem(
                            i, j, QTableWidgetItem('молотый'))
                    else:
                        self.tableWidget.setItem(
                            i, j, QTableWidgetItem('в зернах'))
                else:
                    self.tableWidget.setItem(
                        i, j, QTableWidgetItem(str(elem)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffe()
    ex.show()
    sys.exit(app.exec())
