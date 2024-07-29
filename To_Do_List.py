from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize)
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QLineEdit, QListWidget,
    QMainWindow, QMenuBar, QPushButton, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(470, 540)
        
 
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.additem_pushButton = QPushButton(self.centralwidget, clicked = lambda: self.add_it())
        self.additem_pushButton.setObjectName(u"additem_pushButton")
        self.additem_pushButton.setGeometry(QRect(320, 50, 31, 24))
        self.deleteitem_pushButton = QPushButton(self.centralwidget, clicked = lambda: self.delete_it())
        self.deleteitem_pushButton.setObjectName(u"deleteitem_pushButton")
        self.deleteitem_pushButton.setGeometry(QRect(360, 50, 31, 24))
        self.clearall_pushButton = QPushButton(self.centralwidget, clicked = lambda: self.clear_it())
        self.clearall_pushButton.setObjectName(u"clearall_pushButton")
        self.clearall_pushButton.setGeometry(QRect(80, 470, 81, 21))
        self.myline_lineEdit = QLineEdit(self.centralwidget)
        self.myline_lineEdit.setObjectName(u"myline_lineEdit")
        self.myline_lineEdit.setGeometry(QRect(80, 50, 231, 21))
        self.mylist_listWidget = QListWidget(self.centralwidget)
        self.mylist_listWidget.setObjectName(u"mylist_listWidget")
        self.mylist_listWidget.setGeometry(QRect(80, 90, 311, 361))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # Add item to the list
    def add_it(self):
        item = self.myline_lineEdit.text()
        self.mylist_listWidget.addItem(item)
        # clear the item box
        self.myline_lineEdit.setText('')

    # Delete item from the list
    def delete_it(self):
        # grab the selected row or current row
        clicked = self.mylist_listWidget.currentRow()
        # delete selected row
        self.mylist_listWidget.takeItem(clicked)

    # Clear the list
    def clear_it(self):
        self.mylist_listWidget.clear()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"To Do List", None))
        self.additem_pushButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.additem_pushButton.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
        self.deleteitem_pushButton.setText(QCoreApplication.translate("MainWindow", u"Del", None))
        self.deleteitem_pushButton.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
        self.clearall_pushButton.setText(QCoreApplication.translate("MainWindow", u"Delete the list", None))
        self.clearall_pushButton.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))


if __name__ == '__main__':
    app = QApplication([])
    app.setStyle('Fusion')
    app.setWindowIcon(QIcon("sword1.ico"))
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    exit(app.exec())
