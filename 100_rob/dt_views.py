# -*- coding: utf-8 -*-
"""
Created on Fri Apr 01 09:30:27 2016

@author: Administrator
"""
import sys 

from PyQt4 import QtGui, uic
qtCreatormainFile = "./rob/dtv.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatormainFile)
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    
    def __init__(self,str01):
        self.x_data = list()
        self.y_data = list()
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.dt_edit.setText(str01)
    

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())  