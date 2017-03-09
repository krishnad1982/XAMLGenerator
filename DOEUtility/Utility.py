import os
import sys
from PyQt5.QtWidgets import QMessageBox
from xml.dom import minidom
from DoeTypes import *
import csv
from Config import *
from shutil import copyfile

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

# contruct yes or no confirmation dialog box
def msgDialog(self,title,msg):
    userInfo = QMessageBox.question(self,title,msg,QMessageBox.Yes | QMessageBox.No)
    if userInfo == QMessageBox.Yes:
        return "Y"
    if userInfo == QMessageBox.No:
        return "N"

 # generate XAML
def generateXML(self,fileName,csvPath):
    try:
        dom = minidom.parse(r"{}".format(fileName))
        for node in dom.getElementsByTagName('Grid'):
            if node.getAttribute('x:Name') == "AlgoGrid":
                rowCount = int(self.txtRow.text())
                colCount = int(self.txtCol.text())
                attributeName = self.txtAlgoAttribute.text()
                # creating rows
                i = 0
                while i < rowCount:
                    if i == 0:
                        parent = dom.createElement("Grid.RowDefinitions")
                    node.appendChild(CreateRows(self, dom, parent))
                    i+=1
                # creating cols
                i = 0
                currWidth = "Auto"
                while i < rowCount:
                    if i == 0:
                        parent = dom.createElement("Grid.ColumnDefinitions")
                    node.appendChild(CreateColumns(self, dom,parent,currWidth))
                    currWidth = "2*" if currWidth is "Auto" else "Auto"
                    i+=1
                # create algo controls
                with open(csvPath) as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        node.appendChild(self.options["TextBlock"](self, dom, row["Param"], row["Row"], int(row["Column"]) - 1))
                        node.appendChild(self.options[row["Type"]](self, dom, row["Param"], row["Row"], row["Column"], attributeName,row["Mandatory"]))
        dom.writexml(open(fileName, "w"))
        copyFile(self,fileName)
        showMessage(self, "Information", "Click show details to see the output file path ", (readOutputPath(self))["output"])
    except IOError:
        showMessage(self, "File information!", "No such file or directory found ", "No such file or directory found")
# copy file
def copyFile(self,fileName):
    try:
        src = (readOutputPath(self))["output"]
        splitOne = fileName.split("/")
        copyfile(fileName,src + splitOne[1])
        # remove temp file from the project root skin directory
        if os.path.isfile(fileName):
            os.remove(fileName)
    except IOError:
         showMessage(self, "File information!", "Something went wrong", "Something happened while copying the output file to the destination. Try again!")

