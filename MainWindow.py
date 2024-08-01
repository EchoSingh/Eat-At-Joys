from PyQt5 import QtCore, QtGui, QtWidgets
from Checkout import Ui_Checkout
from Final import Ui_Final
import config
import sys
from functools import partial

class Cart:
    def __init__(self,name,price,quantity): 
        self.Name = name
        self.Price = price
        self.Quantity = quantity 


class Ui_MainWindow(object):
    def setupUi(self, MainWindow,WelcomeDialog):
        config.CartList=[]
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.WelcomeDialog = WelcomeDialog
        self.MainWindow = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.heading = QtWidgets.QLabel(self.centralwidget)
        self.heading.setGeometry(QtCore.QRect(350, 0, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.heading.setFont(font)
        self.heading.setTextFormat(QtCore.Qt.RichText)
        self.heading.setObjectName("heading")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(40, 90, 361, 431))
        self.listView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.listView.setObjectName("listView")
        self.heading_2 = QtWidgets.QLabel(self.centralwidget)
        self.heading_2.setGeometry(QtCore.QRect(40, 60, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.heading_2.setFont(font)
        self.heading_2.setTextFormat(QtCore.Qt.RichText)
        self.heading_2.setObjectName("heading_2")
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setGeometry(QtCore.QRect(560, 90, 221, 81))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter = QtWidgets.QSplitter(self.splitter_3)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.pricelabel = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pricelabel.setFont(font)
        self.pricelabel.setTextFormat(QtCore.Qt.RichText)
        self.pricelabel.setObjectName("pricelabel")
        self.price = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.price.setFont(font)
        self.price.setObjectName("price")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.quantitylabel = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.quantitylabel.setFont(font)
        self.quantitylabel.setTextFormat(QtCore.Qt.RichText)
        self.quantitylabel.setObjectName("quantitylabel")
        self.quantity = QtWidgets.QLineEdit(self.splitter_2)
        self.quantity.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.quantity.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.quantity.setFont(font)
        self.quantity.setObjectName("quantity")
        self.splitter_5 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_5.setGeometry(QtCore.QRect(560, 450, 221, 71))
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.addbutton = QtWidgets.QPushButton(self.splitter_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addbutton.setFont(font)
        self.addbutton.setObjectName("addbutton")
        self.splitter_4 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.okbutton = QtWidgets.QPushButton(self.splitter_4)
        self.okbutton.setObjectName("okbutton")
        self.cancelbutton = QtWidgets.QPushButton(self.splitter_4)
        self.cancelbutton.setObjectName("cancelbutton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.price.hide()
        self.quantity.hide()
        #self.pricelabel.hide()
        #self.quantitylabel.hide()
        self.retranslateUi(MainWindow)
        self.cancelbutton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.heading.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ff0000;\">Menu</span></p></body></html>"))
        self.heading_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ff0000;\">Select Item</span></p></body></html>"))
        self.pricelabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ff0000;\">Price</span></p></body></html>"))
        self.price.setText(_translate("MainWindow", "0"))
        self.quantitylabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ff0000;\">Quantity</span></p></body></html>"))
        self.quantity.setText(_translate("MainWindow", "1"))
        self.addbutton.setText(_translate("MainWindow", "Add to Cart"))
        self.okbutton.setText(_translate("MainWindow", "View Cart"))
        self.cancelbutton.setText(_translate("MainWindow", "Cancel"))

    def onChecked(self, it):
        if it.checkState() == QtCore.Qt.Checked:
            print(it.text(), "was checked")
            model = self.listView.model()
            for index in range(model.rowCount()):
                item = model.item(index)
                if item.isCheckable():
                    if item==it:
                        item.setCheckState(QtCore.Qt.Checked)
                    else:
                        item.setCheckState(QtCore.Qt.Unchecked)

            self.updatePrice(it)

        else:
            print(it.text(), "was unchecked")
            model = self.listView.model()
            allclear = True
            for index in range(model.rowCount()):
                item = model.item(index)
                if item.isCheckable():
                    if item.checkState() == QtCore.Qt.Checked:
                        allclear = False
            if (allclear):
                self.price.hide()
                self.quantity.hide()
                #self.pricelabel.hide()
                #self.quantitylabel.hide()
                self.price.setText(str(0))
                self.quantity.setText(str(0))
                
    def updatePrice(self, item):
        self.price.show()
        self.quantity.show()
        self.pricelabel.show()
        self.quantitylabel.show()
        self.price.setText(str(config.FoodItem[item.text()]))
        self.quantity.setText(str(1))

    def addToCart(self):
        model = self.listView.model()
        for index in range(model.rowCount()):
            item = model.item(index)
            if item.isCheckable():
                if item.checkState() == QtCore.Qt.Checked:
                    it = Cart(item.text(),self.price.text(),self.quantity.text())
                    newitem = True
                    for val in config.CartList:
                        if(val.Name == item.text()):
                            newitem = False
                            val.Quantity = str(int(val.Quantity)+int(self.quantity.text()))
                    if(newitem):
                        config.CartList.append(it)
                        
        for i in config.CartList:
            print (i.Name)
            
    def ViewCart(self,receipt):
        
        self.Checkout = QtWidgets.QMainWindow()
        self.ui = Ui_Checkout()
        self.ui.setupUi(self.Checkout)
        self.Checkout.setWindowIcon(QtGui.QIcon('Icon.ico'))
        
        if receipt:
            self.ui.checkout.hide()
            self.Checkout.setWindowTitle("Receipt")
            self.ui.label.setText("<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ff0000;\">Receipt</span></p></body></html>")
        header = [' Item Name ', ' Price ', ' Quantity ', ' Total Price ']
        myString = ";".join(header)
        model = QtGui.QStandardItemModel()
        head=[]
        for i in header:
            print(i)
            head.append(i)

        data=[]
        #data.append(head)
        #model.appendRow(QtGui.QStandardItem(head));
        model.appendRow(QtGui.QStandardItem(""));
        item=""
        a=1
        self.total=0
        for i in config.CartList:
            item=[]
            #item.append(str(a))
            #name
            item.append(i.Name)
            #price
            item.append(i.Price)
            #quantity
            item.append(i.Quantity)
            #Total
            self.total+=int(i.Price)*int(i.Quantity)
            item.append(str(int(i.Price)*int(i.Quantity)))

            #model.appendRow(QtGui.QStandardItem(item));
            data.append(item)
        print (data)
        self.ui.tableWidget.setRowCount(data.__len__())
        self.ui.tableWidget.setColumnCount(header.__len__())
        self.ui.tableWidget.setHorizontalHeaderLabels((myString).split(";"))
        for i,row in enumerate(data):
            for j,val in enumerate(row):
                self.ui.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(val)))

        self.ui.total.setText(str(self.total))
                
        self.ui.tableWidget.resizeColumnsToContents()
        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.ui.checkout.clicked.connect(self.ViewFinal)
        self.Checkout.show()

    def ViewFinal(self):
        self.Checkout.close()
        self.Final = QtWidgets.QDialog()
        self.uifinal = Ui_Final()
        self.uifinal.setupUi(self.Final)
        self.Final.setWindowIcon(QtGui.QIcon('Icon.ico'))
        
        self.uifinal.label_2.setText("<html><head/><body><p><span style=\" font-size:14pt; color:#000000;\">"+str(self.total)+"</span></p></body></html>")
        self.MainWindow.close()
        self.WelcomeDialog.show();
        self.Final.show()
        self.uifinal.reciept.clicked.connect(partial(self.ViewCart,True))

    def closeEvent(self, event):
            close = QtWidgets.QMessageBox.question(self,
                                         "QUIT",
                                         "Are you sure want to stop process?",
                                         QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if close == QtWidgets.QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow,MainWindow)
    foods = ['cake','cupcake','custard','gulabjamun']
    length = len(foods)
    
    model = QtGui.QStandardItemModel()
    for i in foods:
        item = QtGui.QStandardItem(i)
        item.setCheckable(True)
        item.setCheckState(QtCore.Qt.Unchecked)
        model.appendRow(item)
    model.itemChanged.connect(ui.onChecked)    
    ui.listView.setModel(model)
    ui.addbutton.clicked.connect(ui.addToCart)
    ui.okbutton.clicked.connect(partial(ui.ViewCart,False))
    MainWindow.show()
    sys.exit(app.exec_())

