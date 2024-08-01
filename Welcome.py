import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import Ui_MainWindow
from functools import partial
import config
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="P@$$W0rd", database="food")
mycursor = mydb.cursor()

class Ui_WelcomeDialog(object):
    def __init__(self):
        super().__init__()

    def setupUi(self, WelcomeDialog):
        WelcomeDialog.setObjectName("WelcomeDialog")
        WelcomeDialog.resize(600, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WelcomeDialog.sizePolicy().hasHeightForWidth())
        WelcomeDialog.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        WelcomeDialog.setFont(font)
        icon = QtGui.QIcon.fromTheme("Food")
        WelcomeDialog.setWindowIcon(icon)
        self.WelcomeLabel = QtWidgets.QLabel(WelcomeDialog)
        self.WelcomeLabel.setGeometry(QtCore.QRect(60, 60, 401, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.WelcomeLabel.setFont(font)
        self.WelcomeLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.WelcomeLabel.setTextFormat(QtCore.Qt.RichText)
        self.WelcomeLabel.setObjectName("WelcomeLabel")
        self.splitter = QtWidgets.QSplitter(WelcomeDialog)
        self.splitter.setGeometry(QtCore.QRect(205, 229, 261, 41))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(25)
        self.splitter.setObjectName("splitter")
        self.Newbillbutton = QtWidgets.QPushButton(self.splitter)
        self.Newbillbutton.setObjectName("Newbillbutton")
        self.quit = QtWidgets.QPushButton(self.splitter)
        self.quit.setObjectName("quit")

        self.retranslateUi(WelcomeDialog)
        QtCore.QMetaObject.connectSlotsByName(WelcomeDialog)

    def retranslateUi(self, WelcomeDialog):
        _translate = QtCore.QCoreApplication.translate
        WelcomeDialog.setWindowTitle(_translate("WelcomeDialog", "Eat At Joys"))
        self.WelcomeLabel.setText(_translate("WelcomeDialog", "<html><head/><body><p><span style=\" color:#ff0000;\">WELCOME TO JOY'S EAT</span></p></body></html>"))
        self.Newbillbutton.setText(_translate("WelcomeDialog", "New Bill"))
        self.quit.setText(_translate("WelcomeDialog", "Quit"))

    def MainWindowGUI(self, WelcomeDialog):
        self.MainWindow = QtWidgets.QMainWindow()
        self.Gui = Ui_MainWindow()
        self.Gui.setupUi(self.MainWindow, WelcomeDialog)
        mycursor.execute("SELECT * FROM fooditems")
        myresult = mycursor.fetchall()
        self.MainWindow.setWindowIcon(QtGui.QIcon('Icon.ico'))
        foods = [list(i) for i in myresult]
        length = len(foods)
        print(foods)
        print(config.FoodItem)
        self.model = QtGui.QStandardItemModel()
        for i in foods:
            item = QtGui.QStandardItem(i[0])
            item.setCheckable(True)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.model.appendRow(item)
            config.FoodItem[i[0]] = i[1]
        print(config.FoodItem)
        self.model.itemChanged.connect(self.Gui.onChecked)
        self.Gui.listView.setModel(self.model)
        self.Gui.addbutton.clicked.connect(self.Gui.addToCart)
        self.Gui.okbutton.clicked.connect(partial(self.Gui.ViewCart, False))
        WelcomeDialog.hide()
        config.CartList.clear()
        self.MainWindow.show()

    def AppQuit(self):
        sys.exit()

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    WelcomeDialog = QtWidgets.QDialog()
    ui = Ui_WelcomeDialog()
    ui.setupUi(WelcomeDialog)
    WelcomeDialog.setWindowIcon(QtGui.QIcon('Icon.ico'))
    ui.Newbillbutton.clicked.connect(partial(ui.MainWindowGUI, WelcomeDialog))
    ui.quit.clicked.connect(ui.AppQuit)
    WelcomeDialog.show()
    sys.exit(app.exec_())
