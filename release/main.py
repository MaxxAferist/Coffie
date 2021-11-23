from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog
import sys
import  sqlite3


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(1000, 600)
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 980, 530))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 10, 170, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_2.setFont(font)

        self.retranslateUi()

    def retranslateUi(self):
        self.setWindowTitle("MainWindow")
        self.pushButton.setText("+")
        self.pushButton_2.setText("Изменить")
        self.con = sqlite3.connect('data\coffee.db')
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

    def setupUI(self, mode, other):
        self.resize(400, 300)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(170, 10, 221, 31))
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 50, 221, 31))
        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 90, 221, 31))
        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.lineEdit_4.setGeometry(QtCore.QRect(170, 130, 221, 31))
        self.lineEdit_5 = QtWidgets.QLineEdit(self)
        self.lineEdit_5.setGeometry(QtCore.QRect(170, 170, 221, 31))
        self.lineEdit_6 = QtWidgets.QLineEdit(self)
        self.lineEdit_6.setGeometry(QtCore.QRect(170, 210, 221, 31))
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 10, 151, 31))
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 151, 31))
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 151, 31))
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 151, 31))
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 151, 31))
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(10, 210, 151, 31))
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(285, 250, 101, 41))
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(10, 260, 231, 21))
        self.label_7.setText("")
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

        self.retranslateUi()

    def retranslateUi(self):
        self.label.setText("Сорт")
        self.label_2.setText("Степень обжарки")
        self.label_3.setText("Состояние")
        self.label_4.setText("Вкус")
        self.label_5.setText("Цена")
        self.label_6.setText("Объем упаковки")
        self.pushButton.setText("Принять")

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
