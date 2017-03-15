import os
import sys
from Utility import *
from builtins import eval
from Config import *
from Design import Ui_GenerateXAML
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem


# custom class
class XamlWindow(QtWidgets.QMainWindow,Ui_GenerateXAML):
    # constructor
    def __init__(self):
       super(self.__class__,self).__init__()
       self.setupUi(self)
       # events
       self.btnExit.clicked.connect(self.exitApp)
       self.btnGenerate.clicked.connect(self.generateXAML)
       # txtAlgoAttribute txtchanged event
       self.txtAlgoAttribute.textChanged.connect(self.createAlgoHeader)
       # txtAlgoAttribute foucusoutevent
       self.txtAlgoAttribute.installEventFilter(self)
       self.createTable()

    # switch case for doe datatype functions
    options = {"DateTime" : DateTime,"TextBlock" : TextBlock,"ComboBox":ComboBox,"NumericUpDown":NumericUpDown,"CheckBox":CheckBox,"TextBox":TextBox,}

    # event filters
    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.FocusOut:
             if obj == self.txtAlgoAttribute:
                self.createAlgoHeader()
        return False

    def createDatatTypeCombo(self):
        cmbDataType = QtWidgets.QComboBox()
        for key,val in sorted(self.options.items()):
            cmbDataType.addItem(key)
        return cmbDataType

    def createTable(self):
       # Create table
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.setCellWidget(0, 2, self.createDatatTypeCombo())
        #self.tableWidget.setItem(0,0, QTableWidgetItem("krishna"))
        #self.tableWidget.move(0,0)
 
        # table selection change
        self.tableWidget.keyPressEvent = self.insertRow
        self.tableWidget.doubleClicked.connect(self.removeRow)

    def insertRow(self,event):
        currentColumn = self.tableWidget.currentColumn()
        if event.key() == QtCore.Qt.Key_Enter:
            currentRowCount = self.tableWidget.rowCount()
            self.tableWidget.insertRow(currentRowCount)
            self.tableWidget.setCellWidget(currentRowCount, 2, self.createDatatTypeCombo())
            
            self.tableWidget.focusNextChild()
        return QTableWidget.keyPressEvent(self.tableWidget, event)
        
    def removeRow(self,event):
        currentRow = self.tableWidget.currentRow()
        if currentRow is not 0:
            self.tableWidget.removeRow(currentRow)

    # generate xaml
    def generateXAML(self):
        count = self.tableWidget.rowCount()
        i = 0
        while i < count:
            zero = self.tableWidget.item(i,0).text()
            two = self.tableWidget.cellWidget(i,2).currentText()
            i+=1
            
        if self.txtSkinName.text() is not "" and self.txtRow.text() is not "" and self.txtCol.text() is not "" and self.txtAlgoAttribute.text() is not "" and self.txtHeader.text is not "" and self.cmbSkins.currentText() != "---Select Skin---":
            baseFileName = self.cmbSkins.currentText() + ".xaml"
            # header and version details
            header = self.txtHeader.text()
            version = "Version {}".format(self.txtVersion.text()) if self.txtVersion.text() is not "" else ""
            # creating a dummy file to add algo controls
            splitOne = baseFileName.split(".")
            fileName = "{}/{}_Copy.{}".format("./skins",splitOne[0],splitOne[1])
            skinName = self.txtSkinName.text() + ".xaml"
            copyfile("./skins/" + baseFileName,fileName)
            # creating dummy file ends here
            csvPath = (readConfigProperties(self))["csvpath"]
            generateXML(self,fileName,skinName,header,version,csvPath)
        else:
            showMessage(self,"Mandatory!","All the fields are mandatory to generate XAML","Skin name, Attribute name, row and column fileds are mandatory.")

    # txtattribute textchanged and focusout event
    def createAlgoHeader(self):
        if self.txtAlgoAttribute.text() is not "":
            attribValues = self.txtAlgoAttribute.text().split("-")
            if len(attribValues) > 2:
                self.txtHeader.setText("{} Algo Details".format(attribValues[2]))
            else:
                self.txtHeader.setText("")

    # check skins exist
    def isSkinsExist(self):
        files = []
        if os.path.isdir("skins"):
            files = list(filter(lambda it: it.endswith(".xaml"), os.listdir("skins")))
        else:
            self.cmbSkins.clear()
            self.cmbSkins.addItem("We could not find skins directory")
            self.btnGenerate.setEnabled(False)
            return False
        if len(files) == 0 :
            self.cmbSkins.clear()
            self.cmbSkins.addItem("No skins in the skins directory")
            self.btnGenerate.setEnabled(False)
            return False
        return True

    # fill the skins combobox
    def fillSkins(self):
        self.cmbSkins.clear()
        self.cmbSkins.addItem("---Select Skin---")
        if self.isSkinsExist():
            files = filter(lambda it: it.endswith(".xaml"), os.listdir("skins"))
            strip_list = map(lambda it: it.split(".")[0], files)
            self.cmbSkins.addItems(list(strip_list))

    # window closing event
    def closeEvent(self,event):
        respone = msgDialog(self,"Information","Do you want to exit from the app?")
        if respone == "Y":
           QtWidgets.QApplication.instance().quit()
           event.accept()
        else:
            event.ignore()

    # exit app
    def exitApp(self):
        respone = msgDialog(self,"Information","Do you want to exit from the app?")
        if respone == "Y":
           QtWidgets.QApplication.instance().quit()
        else:
            pass

# main method
def main():
    myApp = QtWidgets.QApplication(sys.argv)
    form = XamlWindow()
    form.fillSkins()
    form.show()
    # Execute the Application and Exit
    sys.exit(myApp.exec_())
# main function
if __name__ == '__main__':
    main()
