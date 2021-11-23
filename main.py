from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog
import sys
import  sqlite3


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect('coffee.db')
        self.cur = self.con.cursor()
        self.pushButton.clicked.connect(self.new)
        self.pushButton_2.clicked.connect(self.update_c)
        self.loadTable()

    def loadTable(self):
        title = ['ID', 'Сорт', 'Степень обжарки', 'Состояние', 'Вкус', 'Цена', 'Обьем']
        self.tableWidget.setColumnCount(len(title))
        self.tableWidget.setHorizontalHeaderLabels(title)
        self.tableWidget.setRowCount(0)
        res = self.cur.execute('SELECT * FROM coffies').fetchall()
        for i in range(len(res)):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j in range(len(res[i])):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(res[i][j])))
        self.tableWidget.resizeColumnsToContents()

    def new(self):
        self.ed = EditNew()
        self.ed.setupUI(1, self)
        self.ed.show()

    def update_c(self):
        try:
            self.ed = EditNew()
            self.ed.setupUI(2, self)
            self.ed.show()
        except:
            pass


class EditNew(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.setWindowModality(2)

    def setupUI(self, mode, other):
        if mode == 1:
            self.setWindowTitle('Добавить')
            self.pushButton.clicked.connect(lambda: self.new(other))
        elif mode == 2:
            self.lineEdit.setText(other.tableWidget.item(other.tableWidget.currentRow(), 1).text())
            self.lineEdit_2.setText(other.tableWidget.item(other.tableWidget.currentRow(), 2).text())
            self.lineEdit_3.setText(other.tableWidget.item(other.tableWidget.currentRow(), 3).text())
            self.lineEdit_4.setText(other.tableWidget.item(other.tableWidget.currentRow(), 4).text())
            self.lineEdit_5.setText(other.tableWidget.item(other.tableWidget.currentRow(), 5).text())
            self.lineEdit_6.setText(other.tableWidget.item(other.tableWidget.currentRow(), 6).text())
            self.setWindowTitle('Изменить')
            self.pushButton.clicked.connect(lambda: self.update_c(other))

    def new(self, other):
        try:
            name = self.lineEdit.text()
            objarka = self.lineEdit_2.text()
            sost = self.lineEdit_3.text()
            vkus = self.lineEdit_4.text()
            price = self.lineEdit_5.text()
            v_upak = self.lineEdit_6.text()
            que = f"INSERT INTO coffies(name_of_sort, objarka, sostoyanie, vkus, price, v_upak) VALUES ('{name}', {objarka}, '{sost}', '{vkus}', {price}, {v_upak})"
            other.cur.execute(que)
            other.con.commit()
            other.loadTable()
            self.close()
        except:
            self.label_7.setText('Error')

    def update_c(self, other):
        try:
            name = self.lineEdit.text()
            objarka = self.lineEdit_2.text()
            sost = self.lineEdit_3.text()
            vkus = self.lineEdit_4.text()
            price = self.lineEdit_5.text()
            v_upak = self.lineEdit_6.text()
            id = other.tableWidget.item(other.tableWidget.currentRow(), 0).text()
            que = f"""UPDATE coffies
SET
    name_of_sort = '{name}',
    objarka = {objarka},
    sostoyanie = '{sost}',
    vkus = '{vkus}',
    price = {price},
    v_upak = {v_upak}
WHERE ID = {id}"""
            other.cur.execute(que)
            other.con.commit()
            other.loadTable()
            self.close()
        except:
            self.label_7.setText('Error')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cf = Coffee()
    cf.show()
    sys.exit(app.exec())