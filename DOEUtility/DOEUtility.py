import os
import sys
import time
from PySide.QtCore import *
from PySide.QtGui import *
from Utility import *
from builtins import eval
from Config import *

# custom class
class XamlWindow(QWidget):
    # constructor
    def __init__(self):
        super(XamlWindow,self).__init__()
        self.initGUI()
    # initiating controls here
    def initGUI(self):
        # all controls
        self.layout = QFormLayout()
        self.vbox = QVBoxLayout()

        self.lblAlgoAttribute = QLabel("Algo attribute name structure:")
        self.txtAlgoAttribute = QLineEdit()
        # radio buttons and its groups
        self.groupBox = QGroupBox("Select Skin Design")
        self.radioSatndard = QRadioButton("Standard")
        self.radioPairs = QRadioButton("Pairs")

        self.lblRow = QLabel("Number of rows:")
        self.txtRow = QLineEdit()
        self.lblCol = QLabel("Number of columns:")
        self.txtCol = QLineEdit()
        self.btnGenerate = QPushButton("Generate XAML!")
        self.btnExit = QPushButton("Exit")
        #controls end here
        self.addWidget()
        self.setTooltipFont()
        self.loadWindow()
     # add widgets
    def addWidget(self):
        self.txtAlgoAttribute.setPlaceholderText("Enter algo attribute naming")
        self.txtRow.setPlaceholderText("Enter number of rows")
        self.txtCol.setPlaceholderText("Enter number of columns")
        self.btnGenerate.clicked.connect(self.generate)
        self.btnExit.clicked.connect(self.exitApp)
        
        self.layout.addWidget(self.lblAlgoAttribute)
        self.layout.addWidget(self.txtAlgoAttribute)
        # group box for radio buttons
        self.vbox.addWidget(self.radioSatndard)
        self.vbox.addWidget(self.radioPairs)
        self.groupBox.setLayout(self.vbox)
        self.layout.addWidget(self.groupBox)
        # radio button group button ends here
        self.layout.addWidget(self.lblRow)
        self.layout.addWidget(self.txtRow)
        self.layout.addWidget(self.lblCol)
        self.layout.addWidget(self.txtCol)
        self.layout.addWidget(self.btnGenerate)
        self.layout.addWidget(self.btnExit)
        
       
        self.setLayout(self.layout)
    # window closing event
    def closeEvent(self,event):
        respone = msgDialog(self,"Information","Do you want to exit from the app?")
        if respone == "Y":
           QApplication.instance().quit()
           event.accept()
        else:
            event.ignore()
    # window design
    def loadWindow(self):
        self.resize(400, 600)
        self.setWindowTitle("XAML Generator")
        self.setToolTip("Main window")
        self.setWindowFlags(Qt.CustomizeWindowHint and Qt.WindowMinimizeButtonHint)
        # center the screen
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.setIcon()
        self.show()
        print("simple window in the GUI")
    # setting up icon
    def setIcon(self):
        appIcon = QIcon("images/appicon.ico")
        self.setWindowIcon(appIcon)
    # set tooltip
    def setTooltipFont(self):
        QToolTip.setFont(QFont("Decorative",8,QFont.Bold))

    # switch dictionary values
    options = {"DateTime" : DateTime,"TextBlock" : TextBlock,"ComboBox":ComboBox,"NumericUpDown":NumericUpDown,"CheckBox":CheckBox,}

    # generate xaml
    def generate(self):
        if self.txtRow.text() is not "" and self.txtCol.text() is not "" and self.txtAlgoAttribute.text() is not "":
            baseFileName = "skins/standard.xaml" if self.radioSatndard.isChecked() else "skins/pairs.xaml"
            # creating a dummy file to add algo controls
            splitOne = baseFileName.split("/")
            splitTwo = splitOne[1].split(".")
            fileName = "{}/{}prg.{}".format(splitOne[0],splitTwo[0],splitTwo[1])
            copyfile(baseFileName,fileName)
            # creating dummy ends here
            csvPath = (readOutputPath(self))["csvpath"]
            generateXML(self,fileName,csvPath)
        else:
            showMessage(self,"Mandatory!","Values required to generate XAML","Attribute name structure, row and col fileds are mandatory")

    # exit app
    def exitApp(self):
        respone = msgDialog(self,"Information","Do you want to exit from the app?")
        if respone == "Y":
           QApplication.instance().quit()
        else:
            pass
# main method
def main():
    try:
        myApp = QApplication(sys.argv)
        myWindow = XamlWindow()
        # Execute the Application and Exit
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("name error", sys.exc_info()[1])
    except SystemExit:
        print("closing window")
    except Exception:
        print(sys.exc_info()[1])
# main function
if __name__ == '__main__':
    main()
