import sys
import time
from PySide.QtCore import *
from PySide.QtGui import *
import xml.etree.ElementTree as ET
from xml.dom import minidom
import csv
from DoeTypes import *

# custom class
class SampleWindow(QWidget):
    # constructor
    def __init__(self):
        super(SampleWindow,self).__init__()
        self.initGUI()
    # initiating controls here
    def initGUI(self):
        # all controls
        self.layout = QFormLayout()
        self.lblAlgoAttribute = QLabel("Algo attribute name structure:")
        self.txtAlgoAttribute = QLineEdit()
        self.lblRow = QLabel("Number of rows:")
        self.txtRow = QLineEdit()
        self.lblCol = QLabel("Number of columns:")
        self.txtCol = QLineEdit()
        self.btnGenerate = QPushButton("Generate")
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
        self.layout.addWidget(self.lblRow)
        self.layout.addWidget(self.txtRow)
        self.layout.addWidget(self.lblCol)
        self.layout.addWidget(self.txtCol)
        self.layout.addWidget(self.btnGenerate)
        self.layout.addWidget(self.btnExit)
        self.setLayout(self.layout)
    # window closing event
    def closeEvent(self,event):
        respone = self.msgDialog("Information","Do you want to exit from the app?")
        if respone == "Y":
           QApplication.instance().quit()
           event.accept()
        else:
            event.ignore()
    # window design
    def loadWindow(self):
        self.resize(400, 600)
        self.setWindowTitle("Home")
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
        appIcon = QIcon("images/appicon.png")
        self.setWindowIcon(appIcon)
    # set tooltip
    def setTooltipFont(self):
        QToolTip.setFont(QFont("Decorative",8,QFont.Bold))

    # contruct yes or no confirmation dialog box
    def msgDialog(self,title,msg):
        userInfo = QMessageBox.question(self,title,msg,QMessageBox.Yes | QMessageBox.No)
        if userInfo == QMessageBox.Yes:
            return "Y"
        if userInfo == QMessageBox.No:
            return "N"
    # switch dictionary values
    options = {"DateTime" : DateTime,"TextBlock" : TextBlock,}
    # xml filtering
    def generateXML(self):
        dom = minidom.parse(r"skins/standard.xaml")
        for node in dom.getElementsByTagName('Grid'):
            if node.getAttribute('x:Name') == "AlgoGrid":
                rowCount = int(self.txtRow.text())
                colCount = int(self.txtCol.text())
                attributeName = self.txtAlgoAttribute.text()
                # creating rows
                i = 0
                while i < rowCount:
                    node.appendChild(CreateRows(self,dom))
                    i = i + 1
                # creating cols
                i = 0
                currWidth = "Auto"
                while i < rowCount:
                    node.appendChild(CreateColumns(self,dom,currWidth))
                    currWidth = "2*" if currWidth is "Auto" else "Auto"
                    i = i + 1
                #create algo controls
                with open("storage/test.csv") as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        node.appendChild(self.options["TextBlock"](self,dom,row["Param"],row["Row"],int(row["Column"]) - 1))
                        node.appendChild(self.options[row["Type"]](self,dom,row["Param"],row["Row"],row["Column"],attributeName))
                dom.writexml(open("skins/standard.xaml","w"))
            else:
                pass
    # generate xaml
    def generate(self):
        if self.txtRow.text() is not "" and self.txtCol.text() is not "" and self.txtAlgoAttribute.text() is not "":
            self.generateXML()
        else:
            self.showMessage("Mandatory!","Values required to generate XAML","Attribute name structure, row and col fileds are mandatory")
    # generate info messsage
    def showMessage(self,title,shortmsg,detailmsg):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(shortmsg)
        #msg.setInformativeText(message)
        msg.setWindowTitle(title)
        msg.setDetailedText(detailmsg)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()
    # exit app
    def exitApp(self):
        respone = self.msgDialog("Information","Do you want to exit from the app?")
        if respone == "Y":
           QApplication.instance().quit()
        else:
            pass
# main method
def main():
    try:
        myApp = QApplication(sys.argv)
        myWindow = SampleWindow()
        
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
