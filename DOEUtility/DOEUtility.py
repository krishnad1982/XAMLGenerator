import os
import sys
from Utility import *
from builtins import eval
from Config import *
from Design import Ui_GenerateXAML
from General import GeneralWindow
from About import AboutWindow
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
       # creating the ui grid if import type is gui
       if readConfigProperties(self)["importtype"] == "gui":
           self.createTable()
       self.hideControls()
       # triggering menu items
       self.actionGeneral.triggered.connect(self.showSettings)
       self.actionAbout.triggered.connect(self.showAbout)
       # set skin version from config
       self.txtVersion.setText(readConfigProperties(self)["skinversion"])

    # switch case for doe datatype functions
    options = {"DateTime" : DateTime,"TextBlock" : TextBlock,"ComboBox":ComboBox,"NumericUpDown":NumericUpDown,"CheckBox":CheckBox,"TextBox":TextBox,}

    # autocalculate gui rows and columns
    def autoCalcualteTotalRowsAndColumns(self,csvPath):
        try:
            lstrow = []
            lstcol = []
            if readConfigProperties(self)["importtype"] == "csv":
                with open(csvPath) as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        lstrow.append(row["Row"])
                        lstcol.append(row["Column"])
            else:
                count = self.tableWidget.rowCount()
                i = 0
                while i < count:
                    lstrow.append(self.tableWidget.item(i,0).text())
                    lstcol.append(self.tableWidget.item(i,1).text())
                    i+=1
            totrow = int(max(lstrow)) + 1
            totcol = int(max(lstcol)) + 1
            self.txtRow.setText(str(totrow))
            self.txtCol.setText(str(totcol))
        except:
            showMessage(self, "Information!", "Something went wrong", "Auto row and column calculations went wrong. Please provide values in the row and column textboxes!")
            return

    # show settings window
    def showSettings(self):
        self.settings = GeneralWindow()
        self.settings.show()
    
    # show about window
    def showAbout(self):
        self.about = AboutWindow()
        self.about.show()

    # event filters
    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.FocusOut:
             if obj == self.txtAlgoAttribute:
                self.createAlgoHeader()
             elif obj == self.tableWidget:
                self.testing()
        return False

    # datatype list for gui grid
    def createDatatTypeList(self):
        cmbDataType = QtWidgets.QComboBox()
        for key,val in sorted(self.options.items()):
            cmbDataType.addItem(key)
        return cmbDataType

    # mandatory list for gui grid
    def createIsMandatoryList(self):
        cmbMandatory = QtWidgets.QComboBox()
        cmbMandatory.addItem("False")
        cmbMandatory.addItem("True")
        return cmbMandatory

    # visibility list for gui grid
    def createVisibilityList(self):
        cmbVisibility = QtWidgets.QComboBox()
        cmbVisibility.addItem("Visible")
        cmbVisibility.addItem("Collapsed")
        cmbVisibility.addItem("Hidden")
        return cmbVisibility

    # hide cols and rows if import type is csv
    def hideControls(self):
        if readConfigProperties(self)["importtype"] == "csv":
            self.tableWidget.setEnabled(False)

    # create gui grid with default values
    def createTable(self):
       # Create table
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.setCellWidget(0, 2, self.createDatatTypeList())
        self.tableWidget.setCellWidget(0, 4, self.createIsMandatoryList())
        self.tableWidget.setCellWidget(0, 7, self.createVisibilityList())
        self.tableWidget.setItem(0,5, QTableWidgetItem("0"))
        self.tableWidget.setItem(0,6, QTableWidgetItem("100"))
 
        # table selection change
        self.tableWidget.keyPressEvent = self.insertRow
        self.tableWidget.doubleClicked.connect(self.removeRow)

    # insert rows into the gui grid
    def insertRow(self,event):
        currentColumn = self.tableWidget.currentColumn()
        if event.key() == QtCore.Qt.Key_Enter:
            currentRowCount = self.tableWidget.rowCount()
            self.tableWidget.insertRow(currentRowCount)
            self.tableWidget.setCellWidget(currentRowCount, 2, self.createDatatTypeList())
            self.tableWidget.setCellWidget(currentRowCount, 4, self.createIsMandatoryList())
            self.tableWidget.setCellWidget(currentRowCount, 7, self.createVisibilityList())
            self.tableWidget.setItem(currentRowCount,5, QTableWidgetItem("0"))
            self.tableWidget.setItem(currentRowCount,6, QTableWidgetItem("100"))
            self.tableWidget.selectRow(currentRowCount)
        return QTableWidget.keyPressEvent(self.tableWidget, event)
    
    # remove rows from the gui grid
    def removeRow(self,event):
        currentRow = self.tableWidget.currentRow()
        if currentRow is not 0:
            respone = msgDialog(self,"Information","Do you really want to delete this row?")
            if respone == "Y":
                self.tableWidget.removeRow(currentRow)

    # generate xaml
    def generateXAML(self):
        if self.cmbSkins.currentText() != "---Select Skin---" and self.txtSkinName.text() is not "" and self.txtAlgoAttribute.text() is not "":
            # assign csv path
            csvPath = (readConfigProperties(self))["csvpath"]
            if self.txtRow.text() == "" and self.txtCol.text() == "":
                # auto rows and columns calculation
                self.autoCalcualteTotalRowsAndColumns(csvPath)
            baseFileName = self.cmbSkins.currentText() + ".xaml"
            # header and version details
            header = self.txtHeader.text()
            version = "Version - {}".format(self.txtVersion.text()) if self.txtVersion.text() is not "" else ""
            # creating a dummy file to add algo controls
            splitOne = baseFileName.split(".")
            fileName = "{}/{}_Copy.{}".format("./skins",splitOne[0],splitOne[1])
            skinName = self.txtSkinName.text() + ".xaml"
            copyfile("./skins/" + baseFileName,fileName)
           
            generateXML(self,fileName,skinName,header,version,csvPath)
            self.txtRow.setText("")
            self.txtCol.setText("")
        else:
            showMessage(self,"Mandatory!","All the fields are mandatory to generate XAML","Skins, Skin name, Attribute Prefix, Rows and Columns are mandatory.")
            return

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
    # fill skins in the combobox
    form.fillSkins()
    form.show()
    # Execute the Application and Exit
    sys.exit(myApp.exec_())
# main function
if __name__ == '__main__':
    main()
