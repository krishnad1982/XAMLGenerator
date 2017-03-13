import os
import sys
from Utility import *
from builtins import eval
from Config import *
from Design import Ui_GenerateXAML
from PyQt5 import QtCore, QtGui, QtWidgets

# custom class
class XamlWindow(QtWidgets.QMainWindow,Ui_GenerateXAML):
    # constructor
    def __init__(self):
       super(self.__class__,self).__init__()
       self.setupUi(self)
       # events
       self.btnExit.clicked.connect(self.exitApp)
       self.btnGenerate.clicked.connect(self.generateXAML)
    
    # switch case for doe datatype functions
    options = {"DateTime" : DateTime,"TextBlock" : TextBlock,"ComboBox":ComboBox,"NumericUpDown":NumericUpDown,"CheckBox":CheckBox,"TextBox":TextBox,}

    # generate xaml
    def generateXAML(self):
        if self.txtRow.text() is not "" and self.txtCol.text() is not "" and self.txtAlgoAttribute.text() is not "":
            baseFileName = "skins/standard.xaml" if self.radioSatndard.isChecked() else "skins/pairs.xaml"
            # creating a dummy file to add algo controls
            splitOne = baseFileName.split("/")
            splitTwo = splitOne[1].split(".")
            fileName = "{}/{}prg.{}".format(splitOne[0],splitTwo[0],splitTwo[1])
            skinName=self.txtSkinName.text()+ ".xaml"
            copyfile(baseFileName,fileName)
            # creating dummy file ends here
            csvPath = (readOutputPath(self))["csvpath"]
            generateXML(self,fileName,skinName,csvPath)
        else:
            showMessage(self,"Mandatory!","All the fields are mandatory to generate XAML","Attribute naming structure, row and column fileds are mandatory.")

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
    form.show()
    # Execute the Application and Exit
    sys.exit(myApp.exec_())
# main function
if __name__ == '__main__':
    main()
