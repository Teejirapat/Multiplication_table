# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mydesigncal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btncal = QtWidgets.QPushButton(self.centralwidget)
        self.btncal.setGeometry(QtCore.QRect(110, 70, 93, 28))
        self.btncal.setObjectName("btncal")
        self.inputtext = QtWidgets.QLineEdit(self.centralwidget)
        self.inputtext.setGeometry(QtCore.QRect(40, 30, 231, 22))
        self.inputtext.setObjectName("inputtext")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(40, 120, 231, 291))
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.btncal.clicked.connect(self.calculate)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btncal.setText(_translate("MainWindow", "calculate"))

    def calculate(self):
        result = self.inputtext.text()
        self.plainTextEdit.setPlainText("")
        for i in range(1,13):
            cal=int(result)*i
            self.plainTextEdit.appendPlainText(result+"x"+str(i)+"="+str(cal))
        self.inputtext.setText("")
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
