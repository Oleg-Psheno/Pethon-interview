import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import uic, QtSql




class MainWindow(QMainWindow):

    def __init__(self, parent = None):
        QMainWindow.__init__(self,parent)
        uic.loadUi('untitled.ui',self)
        self.pushButton.clicked.connect(self.but_handler)
        self.conn = QtSql.QSqlDatabase.addDatabase('QSQLITE')


    def get_query(self,view, table):
        if self.conn.open():
            query = QtSql.QSqlQueryModel()
            query.setQuery(f'SELECT * FROM {table}')
            view.setModel(query)
            self.conn.close()
        else:
            print(self.conn.lastError().text())

    def db(self, file):
        self.conn.setDatabaseName(file[0])
        self.get_query(self.tableView, 'categories')
        self.get_query(self.tableView_3, 'goods')


    def but_handler(self):
        file = QFileDialog.getOpenFileName(self, 'title')
        self.lineEdit.setText(f'{file[0]}')
        self.db(file)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    CMW = MainWindow()
    CMW.setWindowTitle('Test')
    CMW.show()
    sys.exit(app.exec_())