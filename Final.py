from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Final(object):
    def setupUi(self, Final):
        Final.setObjectName("Final")
        Final.resize(400, 300)
        self.splitter = QtWidgets.QSplitter(Final)
        self.splitter.setGeometry(QtCore.QRect(30, 60, 311, 71))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        self.label_2.setObjectName("label_2")
        self.splitter_2 = QtWidgets.QSplitter(Final)
        self.splitter_2.setGeometry(QtCore.QRect(150, 217, 221, 41))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.reciept = QtWidgets.QPushButton(self.splitter_2)
        self.reciept.setObjectName("reciept")
        self.pushButton = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Final)
        self.pushButton.clicked.connect(Final.close)
        QtCore.QMetaObject.connectSlotsByName(Final)
        

    def retranslateUi(self, Final):
        _translate = QtCore.QCoreApplication.translate
        Final.setWindowTitle(_translate("Final", "Dialog"))
        self.label.setText(_translate("Final", "<html><head/><body><p><span style=\" font-size:14pt; color:#ff0000;\">Please Pay :</span></p></body></html>"))
        self.label_2.setText(_translate("Final", "<html><head/><body><p><span style=\" font-size:14pt; color:#000000;\">0</span></p></body></html>"))
        self.reciept.setText(_translate("Final", "View Reciept"))
        self.pushButton.setText(_translate("Final", "Close"))

    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Final = QtWidgets.QDialog()
    ui = Ui_Final()
    ui.setupUi(Final)
    Final.show()
    sys.exit(app.exec_())

