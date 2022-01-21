from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
 
W_WIDTH = 400
W_HEIGHT = 400
W_X = 725
W_Y = 350
 
 
class CreateButton:
    def __init__(self, window, text, width, height, x, y):
        self.button = QtWidgets.QPushButton(window)
        self.button.setText(text)
        self.button.resize(width, height)
        self.button.move(x, y)
 
    def get_instance(self):
        return self.button
 
 
class MainFrame(QMainWindow):
    def __init__(self):
        super(MainFrame, self).__init__()
        self.init()
        self.show()
 
    def writetextbox(self):
        self.textbox.setPlainText("test")
 
    def textboxcreate(self):
        self.textbox = QPlainTextEdit(self)
        self.textbox.move(150,25)
        self.textbox.resize(75, 25)
 
    def init(self):
        self.resize(W_WIDTH, W_HEIGHT)
        self.move(W_X, W_Y)
        self.setWindowTitle("www.langpy.com | Python GUI Tutorial")
 
        self.list_view = QListWidget(self)
        self.list_view.setGeometry(5,5,135,250)
 
 
        self.textbox = QPlainTextEdit(self)
        self.textbox.move(145,5)
        self.textbox.resize(75, 25)
 
        self.button_add_item = CreateButton(self, "Add Item", 120, 25, 225, 5).get_instance()
        self.button_add_item.clicked.connect(self.additem)
 
        self.button_remove_item = CreateButton(self, "Remove Item", 200, 25, 145, 35).get_instance()
        self.button_remove_item.clicked.connect(self.delitem)
 
    def additem(self):
        if self.textbox.toPlainText() == "" or self.textbox.toPlainText() is None:
            msgbox = QMessageBox()
            msgbox.setIcon(QMessageBox.Critical)
            msgbox.setText("Item cannot be empty")
            msgbox.setWindowTitle("Error")
            msgbox.setStandardButtons(QMessageBox.Ok)
            msgbox.exec()
        else:
            self.list_view.addItem(QListWidgetItem(self.textbox.toPlainText()))
            self.textbox.setPlainText(None)
 
    def delitem(self):
            selected_row = self.list_view.currentRow()
            item = self.list_view.takeItem(selected_row)
            del item
 
 
app = QApplication(sys.argv)
win = MainFrame()
sys.exit(app.exec_())