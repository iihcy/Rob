#!C:\Anaconda
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 14:07:33 2016

@author: Administrator
"""

import sys 
from PyQt4 import QtGui, uic
import inputdata

qtCreatormainFile = "./rob/jxzy.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatormainFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.knn_button.clicked.connect(self.knn_action_UI)
        self.rf_button.clicked.connect(self.rf_action_UI)
        self.dt_button.clicked.connect(self.dt_action_UI)
        self.svm_button.clicked.connect(self.svm_action_UI)
        self.by_button.clicked.connect(self.by_action_UI)
        self.feature_button.clicked.connect(self.feature_action_UI)
        self.ls_button.clicked.connect(self.ls_action_UI)
        self.lda_button.clicked.connect(self.lda_action_UI)
        self.pca_button.clicked.connect(self.pca_action_UI)
        self.rbm_button.clicked.connect(self.rbm_action_UI)

        # self.lassopls_button.clicked.connect.connect(self.lapls_action_UI)

    def knn_action_UI(self):
        self.knn = inputdata.MyApp()
        self.knn.sf = 1
        self.knn.show()
    def rf_action_UI(self):
        self.rf = inputdata.MyApp()
        self.rf.sf = 2
        self.rf.show()
    def dt_action_UI(self):
        self.dt = inputdata.MyApp()
        self.dt.sf = 3
        self.dt.show()
    def svm_action_UI(self):
        self.svm = inputdata.MyApp()
        self.svm.sf = 4
        self.svm.show()
    def by_action_UI(self):
        self.by = inputdata.MyApp()
        self.by.sf = 5
        self.by.show()
    def feature_action_UI(self):
        self.fe = inputdata.MyApp()
        self.fe.sf = 6
        self.fe.show()
    def ls_action_UI(self):
        self.ls = inputdata.MyApp()
        self.ls.sf = 7
        self.ls.show()
    def lda_action_UI(self):
        self.lda = inputdata.MyApp()
        self.lda.sf = 8
        self.lda.show()
    def pca_action_UI(self):
        self.pca = inputdata.MyApp()
        self.pca.sf = 9
        self.pca.show()
    def rbm_action_UI(self):
        self.rbm = inputdata.MyApp()
        self.rbm.sf = 10
        self.rbm.show()

    # def lapls_action_UI(self):
    #     self.lapls = inputdata.MyApp()
    #     self.lapls.sf = 11
    #     self.lapls.show()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())