# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GenerateXAML(object):
    def setupUi(self, GenerateXAML):
        GenerateXAML.setObjectName("GenerateXAML")
        GenerateXAML.resize(330, 300)
        GenerateXAML.setMaximumSize(QtCore.QSize(330, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/appicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GenerateXAML.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(GenerateXAML)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.txtAlgoAttribute = QtWidgets.QLineEdit(self.centralwidget)
        self.txtAlgoAttribute.setObjectName("txtAlgoAttribute")
        self.gridLayout.addWidget(self.txtAlgoAttribute, 2, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMaximumSize(QtCore.QSize(320, 50))
        self.groupBox.setObjectName("groupBox")
        self.radioSatndard = QtWidgets.QRadioButton(self.groupBox)
        self.radioSatndard.setGeometry(QtCore.QRect(10, 20, 67, 17))
        self.radioSatndard.setObjectName("radioSatndard")
        self.radioPairs = QtWidgets.QRadioButton(self.groupBox)
        self.radioPairs.setGeometry(QtCore.QRect(100, 20, 46, 17))
        self.radioPairs.setObjectName("radioPairs")
        self.gridLayout.addWidget(self.groupBox, 5, 0, 1, 1)
        self.lblRow = QtWidgets.QLabel(self.centralwidget)
        self.lblRow.setMaximumSize(QtCore.QSize(250, 20))
        self.lblRow.setObjectName("lblRow")
        self.gridLayout.addWidget(self.lblRow, 12, 0, 1, 1)
        self.txtCol = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCol.setObjectName("txtCol")
        self.gridLayout.addWidget(self.txtCol, 13, 0, 1, 1)
        self.btnGenerate = QtWidgets.QPushButton(self.centralwidget)
        self.btnGenerate.setObjectName("btnGenerate")
        self.gridLayout.addWidget(self.btnGenerate, 14, 0, 1, 1)
        self.lblCol = QtWidgets.QLabel(self.centralwidget)
        self.lblCol.setMaximumSize(QtCore.QSize(250, 20))
        self.lblCol.setObjectName("lblCol")
        self.gridLayout.addWidget(self.lblCol, 10, 0, 1, 1)
        self.lblAlgoAttribute = QtWidgets.QLabel(self.centralwidget)
        self.lblAlgoAttribute.setMaximumSize(QtCore.QSize(250, 20))
        self.lblAlgoAttribute.setObjectName("lblAlgoAttribute")
        self.gridLayout.addWidget(self.lblAlgoAttribute, 0, 0, 1, 1)
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setObjectName("btnExit")
        self.gridLayout.addWidget(self.btnExit, 15, 0, 1, 1)
        self.txtRow = QtWidgets.QLineEdit(self.centralwidget)
        self.txtRow.setObjectName("txtRow")
        self.gridLayout.addWidget(self.txtRow, 11, 0, 1, 1)
        GenerateXAML.setCentralWidget(self.centralwidget)

        self.retranslateUi(GenerateXAML)
        QtCore.QMetaObject.connectSlotsByName(GenerateXAML)

    def retranslateUi(self, GenerateXAML):
        _translate = QtCore.QCoreApplication.translate
        GenerateXAML.setWindowTitle(_translate("GenerateXAML", "Generate XAML"))
        GenerateXAML.setToolTip(_translate("GenerateXAML", "Main window"))
        self.txtAlgoAttribute.setPlaceholderText(_translate("GenerateXAML", "Enter algo attribute naming"))
        self.groupBox.setTitle(_translate("GenerateXAML", "Select Algo Skin"))
        self.radioSatndard.setText(_translate("GenerateXAML", "Standard"))
        self.radioPairs.setText(_translate("GenerateXAML", "Pairs"))
        self.lblRow.setText(_translate("GenerateXAML", "Number of columns:"))
        self.txtCol.setPlaceholderText(_translate("GenerateXAML", "Enter number of columns"))
        self.btnGenerate.setText(_translate("GenerateXAML", "Generate XAML!"))
        self.lblCol.setText(_translate("GenerateXAML", "Number of rows:"))
        self.lblAlgoAttribute.setText(_translate("GenerateXAML", "Attribute naming:"))
        self.btnExit.setText(_translate("GenerateXAML", "Exit"))
        self.txtRow.setPlaceholderText(_translate("GenerateXAML", "Enter number of rows"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GenerateXAML = QtWidgets.QMainWindow()
    ui = Ui_GenerateXAML()
    ui.setupUi(GenerateXAML)
    GenerateXAML.show()
    sys.exit(app.exec_())
