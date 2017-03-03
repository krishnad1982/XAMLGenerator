import sys
import time
from PySide.QtCore import *
from PySide.QtGui import *

# custom class
class SampleWindow(QWidget):
    # constructor
    def __init__(self):
        super(SampleWindow,self).__init__()
        self.initGUI()
    # initiating controls here
    def initGUI(self):
        self.setTooltipFont()
        self.loadWindow()
    # window design
    def loadWindow(self):
        self.resize(800, 600)
        self.setWindowTitle("Home")
        self.setToolTip("Main window")
        # center the screen
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        self.setIcon()
        self.setButton()
        self.show()
        print("simple window in the GUI")
    # setting up icon
    def setIcon(self):
        appIcon = QIcon("images/appicon.png")
        self.setWindowIcon(appIcon)
    # set tooltip
    def setTooltipFont(self):
        QToolTip.setFont(QFont("Decorative",8,QFont.Bold))
    # set button
    def setButton(self):
        btnExit = QPushButton("Exit",self)
        btnExit.move(50,100)
        btnExit.clicked.connect(self.exitApp)
    def exitApp(self):
        respone = self.msgDialog("Information","Do you want to exit from thje app?")
        if respone == "Y":
           QApplication.instance().quit()
        else:
            pass
    # contruct yes or no confirmation dialog box
    def msgDialog(self,title,msg):
        userInfo = QMessageBox.question(self,title,msg,QMessageBox.Yes | QMessageBox.No)
        if userInfo == QMessageBox.Yes:
            return "Y"
        if userInfo == QMessageBox.No:
            return "N"
            
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
