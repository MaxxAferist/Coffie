from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import sys
import  sqlite3


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect('coffee.db')
        self.cur = self.con.cursor()
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cf = Coffee()
    cf.show()
    sys.exit(app.exec())