# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 16:15:18 2016

@author: Administrator
"""
import sys 
import math
from PyQt4 import QtGui, uic
#导入标准化模块
from sklearn import preprocessing
#导入VarianceThreshold模块
from sklearn.feature_selection import VarianceThreshold 
#导入SelectKBest , f_classif模块
from sklearn.feature_selection import SelectKBest , f_classif
#导入SelectPercentile模块
from sklearn.feature_selection import SelectPercentile
#导入GenericUnivariateSelect 模块
from sklearn.feature_selection import GenericUnivariateSelect  
#导入RFECV模块
from sklearn.feature_selection import RFECV
from sklearn.svm import SVR
#导入保存模型的模块
from sklearn.externals import joblib

qtCreatormainFile = "./rob/feature.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatormainFile)
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        self.x_data = list()
        self.y_data = list()
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.rfwlv_action.clicked.connect(self.rfwlv)
        self.ufs_action.clicked.connect(self.ufs)
        self.rfe_action.clicked.connect(self.rfe)
        #对标准化radio加入组bg中
        self.bg01 = QtGui.QButtonGroup()
        self.bg01.addButton(self.s_radio_1,1)
        self.bg01.addButton(self.s_radio_2,2)
        #默认定义s_radio_1这个控件被选中
        self.s_radio_1.setChecked(True)
        #对数据集划分radio加入组bg中
        self.bg02 = QtGui.QButtonGroup()
        self.bg02.addButton(self.d_radio_1,1)
        self.bg02.addButton(self.d_radio_2,2)
        #默认定义s_radio_1这个控件被选中
        self.d_radio_1.setChecked(True)
        
    def rfwlv(self):
        self.bz()    #标准化
        self.stt()   #划分数据集
        self.dtc01()   #
    
    def ufs(self):
        self.bz()    #标准化
        self.stt()   #划分数据集
        self.dtc03()   #    
    
    def rfe(self):
        self.bz()    #标准化
        self.stt()   #划分数据集
        self.dtc04()   #    
    
    #数据标准化
    def bz(self):
        if self.bg01.checkedId() == 1:
            self.x = preprocessing.scale(self.x_data)
        else:
            min_max_scaler = preprocessing.MinMaxScaler()
            self.x = min_max_scaler.fit_transform(self.x_data)
    
    #训练数据和测试数据的划分
    def stt(self):
        #对数据进行划分，其中自变量和因变量都进行
        #这样就产生四个数据集：x_train,x_test,y_train,y_test
        self.x_train = list()
        self.x_test = list()
        self.y_train = list()
        self.y_test = list()
        if self.bg02.checkedId() == 1:
            strte = self.tt_box.itemText(self.tt_box.currentIndex())
            s01 = str(strte).split(':')
            if len(s01) == 2:
                xnum = math.ceil((int(s01[0])*1.0/10)*len(self.x_data))
                
                for i in range(len(self.x_data)):
                    if i <= xnum:
                        self.x_train.append(self.x_data[i])
                        self.y_train.append(self.y_data[i])
                    else:
                        self.x_test.append(self.x_data[i])
                        self.y_test.append(self.y_data[i])
        else:
            ts01 = int(self.train.text())
            ts02 = int(self.test.text())
            for i in range(ts01+ts02):
                if i < ts01:
                    self.x_train.append(self.x_data[i])
                    self.y_train.append(self.y_data[i])
                else:
                    self.x_test.append(self.x_data[i])
                    self.y_test.append(self.y_data[i])
    
    '''
    主函数
    '''
    def dtc01(self):
        #将y转化为一维形式：self.y_train，self.y_test
        self.y01_train = list()
        self.y01_test = list()
        for a in range(len(self.y_train)):
            self.y01_train.append(self.y_train[a][0])
        for b in range(len(self.y_test)):
            self.y01_test.append(self.y_test[b][0])
            
        #取出其中labels
        self.labels = list()
        for c in range(len(self.y_test)):
            if self.labels.count(self.y_test[c][0]) == 0:
                self.labels.append(self.y_test[c][0])
        print (self.labels)
        
        # VarianceThreshold算法的实现
        # 参数的获取
        if not self.th_edit.text().strip():
            self.max_depth = 0.0
        else:
            self.max_depth = float(self.md_edit.text())
        
        # 定义模型
        self.clf = VarianceThreshold(threshold=self.max_depth) 
        self.clf.fit_transform(self.x_train)
        self.f_c = self.clf.get_support()
        '''
        该模块是对dtable01模块进行设置，即显示训练集的训练结果
        '''
        # VarianceThreshold算法的结果显示
        self.rfwlv_dtable.setRowCount(2)
        self.rfwlv_dtable.setColumnCount(len(self.x_train[0]))
        mlan = "是否保留该特征(T/F)"
        self.rfwlv_dtable.setSpan(0, 0, 1, len(self.x_train[0]))
        self.rfwlv_dtable.setItem(0,0, QtGui.QTableWidgetItem(mlan.decode('utf-8')))
        for j in range(len(self.f_c)):
            self.rfwlv_dtable.setItem(1,j, QtGui.QTableWidgetItem(str(self.f_c[j])))
    
    
    def dtc03(self):
        #将y转化为一维形式：self.y_train，self.y_test
        self.y01_train = list()
        self.y01_test = list()
        for a in range(len(self.y_train)):
            self.y01_train.append(self.y_train[a][0])
        for b in range(len(self.y_test)):
            self.y01_test.append(self.y_test[b][0])
            
        #取出其中labels
        self.labels = list()
        for c in range(len(self.y_test)):
            if self.labels.count(self.y_test[c][0]) == 0:
                self.labels.append(self.y_test[c][0])
        print (self.labels)

        # SelectKBest算法的实现
        # 参数的获取
        if not self.kedit.text().strip():
            self.k = 10
        else:
            self.k = int(self.kedit.text())
        
        if not self.pedit.text().strip():
            self.param = 1e-05
        else:
            self.param = float(self.pedit.text())
        
        self.mode = self.mo_box.itemText(self.mo_box.currentIndex())
        
        # 定义模型
        if self.sp_box.itemText(self.sp_box.currentIndex()) == 'SelectKBest':
            self.clf = SelectKBest(score_func= f_classif,  k=self.k) 
            self.clf.fit_transform(self.x_train,self.y01_train)
            self.f_c = self.clf.get_support()
        elif self.sp_box.itemText(self.sp_box.currentIndex()) == 'SelectPercentile':
            self.clf = SelectPercentile(score_func= f_classif,  percentile= self.k) 
            self.clf.fit_transform(self.x_train,self.y01_train)
            self.f_c = self.clf.get_support()
        else:
            self.clf = GenericUnivariateSelect(score_func= f_classif, mode= self.mode, param=self.param) 
            self.clf.fit_transform(self.x_train,self.y01_train)
            self.f_c = self.clf.get_support()
        # 
        '''
        该模块是对dtable01模块进行设置，即显示训练集的训练结果
        '''
        # VarianceThreshold算法的结果显示
        self.ufs_dtable.setRowCount(2)
        self.ufs_dtable.setColumnCount(len(self.x_train[0]))
        mlan = "是否保留该特征(T/F)"
        self.ufs_dtable.setSpan(0, 0, 1, len(self.x_train[0]))
        self.ufs_dtable.setItem(0,0, QtGui.QTableWidgetItem(mlan.decode('utf-8')))
        for j in range(len(self.f_c)):
            self.ufs_dtable.setItem(1,j, QtGui.QTableWidgetItem(str(self.f_c[j])))
        
    def dtc04(self):
        #将y转化为一维形式：self.y_train，self.y_test
        self.y01_train = list()
        self.y01_test = list()
        for a in range(len(self.y_train)):
            self.y01_train.append(self.y_train[a][0])
        for b in range(len(self.y_test)):
            self.y01_test.append(self.y_test[b][0])
            
        #取出其中labels
        self.labels = list()
        for c in range(len(self.y_test)):
            if self.labels.count(self.y_test[c][0]) == 0:
                self.labels.append(self.y_test[c][0])
        print (self.labels)
        
        # VarianceThreshold算法的实现
        # 参数的获取
        if not self.stepedit.text().strip():
            self.step = 1
        else:
            self.step = int(self.stepedit.text())
        
        if not self.cvedit.text().strip():
            self.cv = 5
        else:
            self.cv = int(self.cvedit.text())
        # 定义模型
        estimator = SVR(kernel="linear")
        self.clf = RFECV(estimator, step=self.step, cv=self.cv)
        self.clf.fit(self.x_train,self.y01_train)
        
        self.f_c = self.clf.get_support()
        '''
        该模块是对dtable01模块进行设置，即显示训练集的训练结果
        '''
        # VarianceThreshold算法的结果显示
        self.rfe_dtable.setRowCount(2)
        self.rfe_dtable.setColumnCount(len(self.x_train[0]))
        mlan = "是否保留该特征(T/F)"
        self.rfe_dtable.setSpan(0, 0, 1, len(self.x_train[0]))
        self.rfe_dtable.setItem(0,0, QtGui.QTableWidgetItem(mlan.decode('utf-8')))
        for j in range(len(self.f_c)):
            self.rfe_dtable.setItem(1,j, QtGui.QTableWidgetItem(str(self.f_c[j])))
        
    #保存模型
    def out_model(self):
        self.filepath=str(QtGui.QFileDialog.getSaveFileName(self,"文件保存","F:/","Model Files (*.model)"))
        joblib.dump(self.clf, self.filepath.decode('GB2312'))
        


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())  
