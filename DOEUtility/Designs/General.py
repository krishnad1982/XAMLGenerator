

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GeneralWindow(object):
    def setupUi(self, GeneralWindow):
        GeneralWindow.setObjectName("GeneralWindow")
        GeneralWindow.resize(450, 250)
        GeneralWindow.setMaximumSize(QtCore.QSize(450, 250))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        GeneralWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/appicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GeneralWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(GeneralWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 411, 61))
        self.groupBox.setObjectName("groupBox")
        self.rdCsv = QtWidgets.QRadioButton(self.groupBox)
        self.rdCsv.setGeometry(QtCore.QRect(20, 30, 82, 17))
        self.rdCsv.setObjectName("rdCsv")
        self.rdGui = QtWidgets.QRadioButton(self.groupBox)
        self.rdGui.setGeometry(QtCore.QRect(100, 30, 82, 17))
        self.rdGui.setObjectName("rdGui")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 80, 411, 101))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lblOutput = QtWidgets.QLabel(self.groupBox_2)
        self.lblOutput.setGeometry(QtCore.QRect(10, 30, 51, 16))
        self.lblOutput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblOutput.setObjectName("lblOutput")
        self.txtOutput = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtOutput.setGeometry(QtCore.QRect(70, 30, 331, 20))
        self.txtOutput.setObjectName("txtOutput")
        self.txtCsv = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtCsv.setGeometry(QtCore.QRect(70, 60, 331, 20))
        self.txtCsv.setObjectName("txtCsv")
        self.lblCsv = QtWidgets.QLabel(self.groupBox_2)
        self.lblCsv.setGeometry(QtCore.QRect(0, 60, 51, 16))
        self.lblCsv.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblCsv.setObjectName("lblCsv")
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(130, 200, 171, 41))
        self.btnSave.setObjectName("btnSave")
        GeneralWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(GeneralWindow)
        QtCore.QMetaObject.connectSlotsByName(GeneralWindow)

    def retranslateUi(self, GeneralWindow):
        _translate = QtCore.QCoreApplication.translate
        GeneralWindow.setWindowTitle(_translate("GeneralWindow", "General Settings"))
        self.groupBox.setTitle(_translate("GeneralWindow", "Import Type"))
        self.rdCsv.setText(_translate("GeneralWindow", "CSV"))
        self.rdGui.setText(_translate("GeneralWindow", "GUI"))
        self.groupBox_2.setTitle(_translate("GeneralWindow", "Path Settings"))
        self.lblOutput.setText(_translate("GeneralWindow", "Output:"))
        self.lblCsv.setText(_translate("GeneralWindow", "Csv:"))
        self.btnSave.setText(_translate("GeneralWindow", "Save!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GeneralWindow = QtWidgets.QMainWindow()
    ui = Ui_GeneralWindow()
    ui.setupUi(GeneralWindow)
    GeneralWindow.show()
    sys.exit(app.exec_())

