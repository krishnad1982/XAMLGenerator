from Designs.General import Ui_GeneralWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from Config import *
from Utility import showMessage

class GeneralWindow(QtWidgets.QMainWindow,Ui_GeneralWindow):
    def __init__(self):
       super(self.__class__,self).__init__()
       self.setupUi(self)
       self.readConfigDetails()
       self.btnSave.clicked.connect(self.saveConfig)

    # read config details from json file
    def readConfigDetails(self):
        self.txtOutput.setText(readConfigProperties(self)["output"])
        self.txtCsv.setText(readConfigProperties(self)["csvpath"])
        if readConfigProperties(self)["importtype"] == "csv":
            self.rdCsv.setChecked(True)
        else:
            self.rdGui.setChecked(True)
        self.txtGroupName.setText(readConfigProperties(self)["groupbox"])
        self.txtGridName.setText(readConfigProperties(self)["gridname"])
        self.txtVersionBlock.setText(readConfigProperties(self)["versiontextblock"])
        self.txtSkin.setText(readConfigProperties(self)["skinversion"])
    # update config details
    def saveConfig(self):
        importtype = "csv" if self.rdCsv.isChecked() else "gui"
        saveConfigDetails(self,self.txtOutput.text(),self.txtCsv.text(),importtype,
                          self.txtGroupName.text(),self.txtGridName.text(),self.txtVersionBlock.text(),self.txtSkin.text())
        showMessage(self, "Information!", "Successfully updated, restart the app.", "Restart the app!")
        QtWidgets.QApplication.instance().quit()

# main method
def main():
    myApp = QtWidgets.QApplication(sys.argv)
    form = GeneralWindow()
    form.show()
    # Execute the Application and Exit
    sys.exit(myApp.exec_())
# main function
if __name__ == '__main__':
    main()

