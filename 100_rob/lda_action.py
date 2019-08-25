# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 16:15:18 2016

@author: Administrator
"""
import sys 
import math
from PyQt4 import QtGui, uic
#导入的是线性判别分析LDA算法
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
#导入标准化模块
from sklearn import preprocessing

#导入保存模型的模块
from sklearn.externals import joblib

qtCreatormainFile = "./rob/lda.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatormainFile)
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        self.x_data = list()
        self.y_data = list()
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.svm_action.clicked.connect(self.ss)
        self.dtp_Button.clicked.connect(self.out_model)
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
        
    def ss(self):
        self.bz()    #标准化
        self.stt()   #划分数据集
        self.dtc()   #决策树
        
    
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
    def dtc(self):
        
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
        
        if self.nc_edit.text().strip():
            k = int(self.nc_edit.text())
        else:
            k= None
        #LDA算法实现
        self.clf = LinearDiscriminantAnalysis(n_components=k) 
        #训练模型
        self.clf.fit(self.x_train, self.y01_train)
        #对训练集中x进行转换
        self.train_x = self.clf.transform(self.x_train)
        #对测试集中x进行转换
        self.test_x = self.clf.transform(self.x_test)
        '''
        该模块是对dtable_train模块进行设置，即显示训练集的训练结果
        '''
        #设置单元格的行数和列数
        self.dtable_train.setRowCount(len(self.train_x))
        self.dtable_train.setColumnCount(len(self.train_x[0]))

        for s in range(len(self.train_x)):
            if s/2.0==0:
                for s01 in range(len(self.train_x[0])):
                    self.dtable_train.setItem(s,s01, QtGui.QTableWidgetItem(str(self.train_x[s][s01])))
                    self.dtable_train.item(s,s01).setBackgroundColor(QtGui.QColor(214, 71, 0))
            else:
                for s01 in range(len(self.train_x[0])):
                    self.dtable_train.setItem(s,s01, QtGui.QTableWidgetItem(str(self.train_x[s][s01])))
        
        '''
        该模块是对dtable_test模块进行设置，显示测试集的测试结果
        '''
        #设置单元格的行数和列数
        self.dtable_test.setRowCount(len(self.test_x))
        self.dtable_test.setColumnCount(len(self.test_x[0]))

        for s in range(len(self.test_x)):
            if s/2.0==0:
                for s01 in range(len(self.test_x[0])):
                    self.dtable_test.setItem(s,s01, QtGui.QTableWidgetItem(str(self.test_x[s][s01])))
                    self.dtable_test.item(s,s01).setBackgroundColor(QtGui.QColor(214, 71, 0))
            else:
                for s01 in range(len(self.test_x[0])):
                    self.dtable_test.setItem(s,s01, QtGui.QTableWidgetItem(str(self.test_x[s][s01])))
        
        
    #保存模型
    def out_model(self):
        self.filepath=str(QtGui.QFileDialog.getSaveFileName(self,"文件保存","F:/","Model Files (*.model)"))
        joblib.dump(self.clf, self.filepath.decode('GB2312'))
        
   
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())  
