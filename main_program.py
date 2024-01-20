import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMessageBox
from PyQt5.QtWidgets import QMainWindow
import main
import addEditCoffeeForm


class AddFilmWidget(QMainWindow, addEditCoffeeForm.Ui_MainWindow):
    def __init__(self, parent=None, idd=None, add_or_edit=True):
        QMainWindow.__init__(parent)
        self.setupUi(self)
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.con = sqlite3.connect('coffee.sqlite3')
        cur = self.con.cursor()
        self.idd = idd
        self.comboBox.addItems(['0', '1'])
        if idd is not None:
            self.pushButton.setText('Отредактировать')
            self.setWindowTitle('Редактирование записи')
            q1 = f'SELECT sort_title FROM coffee WHERE id == {self.idd}'
            q2 = f'SELECT price FROM coffee WHERE id == {self.idd}'
            q3 = f'SELECT volume_of_packaging FROM coffee WHERE id == {self.idd}'
            q4 = f'''SELECT ground_or_grains FROM coffee WHERE id == {self.idd}'''
            self.title.setPlainText(str(*cur.execute(q1).fetchone()))
            self.year.setPlainText((str(*cur.execute(q2).fetchone())))
            self.duration.setPlainText((str(*cur.execute(q3).fetchone())))
            self.comboBox.setCurrentText(f"{str(*cur.execute(q4).fetchone())}")

        self.add_or_edit = add_or_edit
        if self.add_or_edit:
            self.pushButton.clicked.connect(self.get_adding_verdict)
        else:
            self.pushButton.clicked.connect(self.get_editing_verdict)

    def get_adding_verdict(self):
        if any((len(self.title.toPlainText()) == 0,
                len(self.year.toPlainText()) == 0,
                len(self.duration.toPlainText()) == 0)):
            self.statusBar().showMessage('Неверно заполнена форма')
            print(1)
            return False
        elif any((not float(self.year.toPlainText()), not float(self.duration.toPlainText()))):
            self.statusBar().showMessage('Неверно заполнена форма')
            print(2)
            return False
        else:
            self.con = sqlite3.connect('coffee.sqlite3')
            cur = self.con.cursor()
            q = "SELECT MAX(id) FROM coffee;"
            res1 = cur.execute(q).fetchone()
            query = f"""INSERT  INTO coffee (id, sort_title,
                      price,
                      ground_or_grains,
                      volume_of_packaging)
                      VALUES ({res1[0] + 1},
                      '{self.title.toPlainText()}',
                      {self.year.toPlainText()},
                      {self.comboBox.currentText()}, 
                      {self.duration.toPlainText()}
                  );"""
            cur.execute(query).fetchall()
            self.con.commit()
            self.parent().update_films()
            self.close()
            return True

    def get_editing_verdict(self):
        if self.idd:
            if any((len(self.title.toPlainText()) == 0,
                    len(self.year.toPlainText()) == 0,
                    len(self.duration.toPlainText()) == 0)):
                self.statusBar().showMessage('Неверно заполнена форма')
                print(1)
                return False
            elif any((not float(self.year.toPlainText()), not float(self.duration.toPlainText()))):
                self.statusBar().showMessage('Неверно заполнена форма')
                print(2)
                return False
            else:
                self.con = sqlite3.connect('coffee.sqlite3')
                cur = self.con.cursor()
                query = f"""UPDATE coffee SET
                          sort_title = '{self.title.toPlainText()}',
                          price = {self.year.toPlainText()},
                          ground_or_grains = {self.comboBox.currentText()},
                          volume_of_packaging = {self.duration.toPlainText()}
                          WHERE id = {self.idd};"""
                cur.execute(query).fetchall()
                self.con.commit()
                self.parent().update_films()
                self.close()
                return True


class MyWidget(QMainWindow, main.Ui_MainWindow):
    def __init__(self, ):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.result = None
        self.selected_f_ids = []
        self.selected_g_ids = []
        self.selected_f_id = False
        self.selected_g_id = False
        self.f_idd = None
        self.g_idd = None
        self.deselectedidd = None
        self.filmsTable.selectionModel().selectionChanged.connect(self.on_selectionChanged)
        self.con = sqlite3.connect('coffee.sqlite3')
        self.filmsTable.setRowCount(0)
        self.add_film_widget = AddFilmWidget(self, idd=self.f_idd)
        self.edit_film_widget = AddFilmWidget(self)
        self.filmsTable.setColumnCount(5)
        self.filmsTable.setHorizontalHeaderLabels(['ИД', 'Сорт', 'Молотое(0)\В зернах(1)',
                                                   'Цена(руб)', 'В пачке(кг)'])
        self.addFilmButton.clicked.connect(self.add_film)
        self.editFilmButton.clicked.connect(self.edit_film)
        self.deleteFilmButton.clicked.connect(self.delete_film)
        self.update_films()

    def on_selectionChanged(self, selected, deselected):
        for ix in selected.indexes():
            a, b = ix.row(), ix.column()
            self.selected_f_id = True
            self.f_idd = self.filmsTable.item(a, 0).text()
            self.selected_f_ids.append(self.f_idd)
        for ix in deselected.indexes():
            try:
                a, b = ix.row(), ix.column()
                self.deselectedidd = self.filmsTable.item(a, 0).text()
                self.selected_f_ids.remove(self.deselectedidd)
            except ValueError:
                pass
        print(self.selected_f_ids)

    def update_films(self):
        self.con = sqlite3.connect('coffee.sqlite3')
        cur = self.con.cursor()
        query = f"""SELECT * FROM coffee;"""
        self.result = cur.execute(query).fetchall()
        self.filmsTable.setRowCount(0)
        for i, row in enumerate(self.result):
            self.filmsTable.setRowCount(
                self.filmsTable.rowCount() + 1)
            for j, elem in enumerate(row):
                self.filmsTable.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def edit_film(self):
        self.statusBar().showMessage('')
        if self.selected_f_id:
            self.edit_film_widget.close()
            self.edit_film_widget = AddFilmWidget(self, self.f_idd, add_or_edit=False)
            self.edit_film_widget.show()
        else:
            self.statusBar().showMessage('Ничего не выбрано')

    def add_film(self):
        self.statusBar().showMessage('')
        self.edit_film_widget.close()
        self.add_film_widget = AddFilmWidget(self)
        self.add_film_widget.show()

    def delete_film(self):
        if self.selected_f_id:
            ok_pressed = (
                QMessageBox.question(self, "python", f'''Действительно хотите 
                удалить элементы с id {' '.join(i for i in self.selected_f_ids)}''', QMessageBox.Yes, QMessageBox.No))
            if ok_pressed == QMessageBox.Yes:
                self.con = sqlite3.connect('coffee.sqlite3')
                cur = self.con.cursor()
                for i in self.selected_f_ids:
                    query = f"""DELETE FROM coffee
                                WHERE id == '{i}';"""
                    cur.execute(query)
                    self.con.commit()
                self.selected_f_ids.clear()
                self.update_films()
        else:
            self.statusBar().showMessage('Ничего не выбрано')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())