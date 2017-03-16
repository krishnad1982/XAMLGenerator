from Designs.About import Ui_AboutWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class AboutWindow(QtWidgets.QMainWindow,Ui_AboutWindow):
    def __init__(self):
       super(self.__class__,self).__init__()
       self.setupUi(self)

# main method
def main():
    myApp = QtWidgets.QApplication(sys.argv)
    form = AboutWindow()
    form.show()
    # Execute the Application and Exit
    sys.exit(myApp.exec_())
# main function
if __name__ == '__main__':
    main()
