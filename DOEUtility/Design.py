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
        GenerateXAML.resize(750, 600)
        GenerateXAML.setMaximumSize(QtCore.QSize(750, 600))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        GenerateXAML.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../Python/DOE/DoeUtility/DoeUtility/images/appicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GenerateXAML.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(GenerateXAML)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setObjectName("btnExit")
        self.gridLayout.addWidget(self.btnExit, 29, 0, 1, 1)
        self.txtRow = QtWidgets.QLineEdit(self.centralwidget)
        self.txtRow.setObjectName("txtRow")
        self.gridLayout.addWidget(self.txtRow, 24, 0, 1, 1)
        self.txtSkinName = QtWidgets.QLineEdit(self.centralwidget)
        self.txtSkinName.setObjectName("txtSkinName")
        self.gridLayout.addWidget(self.txtSkinName, 5, 0, 1, 1)
        self.btnGenerate = QtWidgets.QPushButton(self.centralwidget)
        self.btnGenerate.setObjectName("btnGenerate")
        self.gridLayout.addWidget(self.btnGenerate, 28, 0, 1, 1)
        self.lblCol = QtWidgets.QLabel(self.centralwidget)
        self.lblCol.setMaximumSize(QtCore.QSize(250, 20))
        self.lblCol.setObjectName("lblCol")
        self.gridLayout.addWidget(self.lblCol, 17, 0, 1, 1)
        self.lblAlgoAttribute = QtWidgets.QLabel(self.centralwidget)
        self.lblAlgoAttribute.setMaximumSize(QtCore.QSize(250, 20))
        self.lblAlgoAttribute.setObjectName("lblAlgoAttribute")
        self.gridLayout.addWidget(self.lblAlgoAttribute, 6, 0, 1, 1)
        self.txtHeader = QtWidgets.QLineEdit(self.centralwidget)
        self.txtHeader.setObjectName("txtHeader")
        self.gridLayout.addWidget(self.txtHeader, 14, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(250, 20))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 15, 0, 1, 1)
        self.txtAlgoAttribute = QtWidgets.QLineEdit(self.centralwidget)
        self.txtAlgoAttribute.setObjectName("txtAlgoAttribute")
        self.gridLayout.addWidget(self.txtAlgoAttribute, 8, 0, 1, 1)
        self.lblRow = QtWidgets.QLabel(self.centralwidget)
        self.lblRow.setMaximumSize(QtCore.QSize(250, 20))
        self.lblRow.setObjectName("lblRow")
        self.gridLayout.addWidget(self.lblRow, 25, 0, 1, 1)
        self.lblSkinName = QtWidgets.QLabel(self.centralwidget)
        self.lblSkinName.setMaximumSize(QtCore.QSize(250, 20))
        self.lblSkinName.setObjectName("lblSkinName")
        self.gridLayout.addWidget(self.lblSkinName, 3, 0, 1, 1)
        self.cmbSkins = QtWidgets.QComboBox(self.centralwidget)
        self.cmbSkins.setObjectName("cmbSkins")
        self.gridLayout.addWidget(self.cmbSkins, 2, 0, 1, 1)
        self.txtCol = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCol.setObjectName("txtCol")
        self.gridLayout.addWidget(self.txtCol, 26, 0, 1, 1)
        self.txtVersion = QtWidgets.QLineEdit(self.centralwidget)
        self.txtVersion.setObjectName("txtVersion")
        self.gridLayout.addWidget(self.txtVersion, 16, 0, 1, 1)
        self.lblHeader = QtWidgets.QLabel(self.centralwidget)
        self.lblHeader.setMaximumSize(QtCore.QSize(250, 20))
        self.lblHeader.setObjectName("lblHeader")
        self.gridLayout.addWidget(self.lblHeader, 13, 0, 1, 1)
        self.lblSkin = QtWidgets.QLabel(self.centralwidget)
        self.lblSkin.setMaximumSize(QtCore.QSize(250, 20))
        self.lblSkin.setObjectName("lblSkin")
        self.gridLayout.addWidget(self.lblSkin, 1, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.gridLayout.addWidget(self.tableWidget, 27, 0, 1, 1)
        GenerateXAML.setCentralWidget(self.centralwidget)

        self.retranslateUi(GenerateXAML)
        QtCore.QMetaObject.connectSlotsByName(GenerateXAML)
        GenerateXAML.setTabOrder(self.cmbSkins, self.txtSkinName)
        GenerateXAML.setTabOrder(self.txtSkinName, self.txtAlgoAttribute)
        GenerateXAML.setTabOrder(self.txtAlgoAttribute, self.txtHeader)
        GenerateXAML.setTabOrder(self.txtHeader, self.txtVersion)
        GenerateXAML.setTabOrder(self.txtVersion, self.txtRow)
        GenerateXAML.setTabOrder(self.txtRow, self.txtCol)
        GenerateXAML.setTabOrder(self.txtCol, self.btnGenerate)
        GenerateXAML.setTabOrder(self.btnGenerate, self.btnExit)

    def retranslateUi(self, GenerateXAML):
        _translate = QtCore.QCoreApplication.translate
        GenerateXAML.setWindowTitle(_translate("GenerateXAML", "Skin Manager"))
        GenerateXAML.setToolTip(_translate("GenerateXAML", "Main window"))
        self.btnExit.setText(_translate("GenerateXAML", "Exit"))
        self.txtRow.setPlaceholderText(_translate("GenerateXAML", "Enter number of rows"))
        self.txtSkinName.setPlaceholderText(_translate("GenerateXAML", "Enter Skin Name : [SA_Hermes_Hidden]"))
        self.btnGenerate.setText(_translate("GenerateXAML", "Generate XAML!"))
        self.lblCol.setText(_translate("GenerateXAML", "Number Of Rows:"))
        self.lblAlgoAttribute.setText(_translate("GenerateXAML", "Attribute Name:"))
        self.txtHeader.setPlaceholderText(_translate("GenerateXAML", "Enter algo header text : [Hidden Algo Details]"))
        self.label.setText(_translate("GenerateXAML", "Skin Version:"))
        self.txtAlgoAttribute.setPlaceholderText(_translate("GenerateXAML", "Enter algo attribute name : [SA-Hermes-Hidden]"))
        self.lblRow.setText(_translate("GenerateXAML", "Number Of Columns:"))
        self.lblSkinName.setText(_translate("GenerateXAML", "Skin Name:"))
        self.txtCol.setPlaceholderText(_translate("GenerateXAML", "Enter number of columns"))
        self.txtVersion.setText(_translate("GenerateXAML", "1.0.0"))
        self.lblHeader.setText(_translate("GenerateXAML", "Algo Header Text:"))
        self.lblSkin.setText(_translate("GenerateXAML", "Select Skin:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("GenerateXAML", "Row"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("GenerateXAML", "Column"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("GenerateXAML", "Datat Type"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("GenerateXAML", "Attributes"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("GenerateXAML", "Is Mandatory"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("GenerateXAML", "Minimum"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("GenerateXAML", "Maximum"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GenerateXAML = QtWidgets.QMainWindow()
    ui = Ui_GenerateXAML()
    ui.setupUi(GenerateXAML)
    GenerateXAML.show()
    sys.exit(app.exec_())

