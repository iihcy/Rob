# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 16:15:18 2016

@author: Administrator
"""


import sys 
import math
import numpy as np
from PyQt4 import QtGui, uic
# 导入的是ls算法
from sklearn import linear_model
# 导入标准化模块
from sklearn import preprocessing
# 导入保存模型的模块
from sklearn.externals import joblib
# 画图工具
import matplotlib.pyplot as plt 

qtCreatormainFile = "./rob/ls.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatormainFile)
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        self.x_data = list()
        self.y_data = list()
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
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
        
        #LinearRegression模型的所有按钮
        self.lr_action.clicked.connect(self.ss01)
        self.hz_lr_tr.clicked.connect(self.huizhi01)
        self.hz_lr_te.clicked.connect(self.huizhi02)
        self.hz_lr_tr_2.clicked.connect(self.huizhi03)
        self.hz_lr_te_2.clicked.connect(self.huizhi04)
        self.save_lr_button.clicked.connect(self.out_model_lr)
        # Ridge模型
        self.ri_action.clicked.connect(self.ss02)
        self.hz_ri_tr.clicked.connect(self.huizhi01)
        self.hz_ri_te.clicked.connect(self.huizhi02)
        self.hz_ri_tr_2.clicked.connect(self.huizhi03)
        self.hz_ri_te_2.clicked.connect(self.huizhi04)
        self.save_ri_button.clicked.connect(self.out_model_ri)
        # Lasso模型
        self.la_action.clicked.connect(self.ss03)
        self.hz_la_tr.clicked.connect(self.huizhi01)
        self.hz_la_te.clicked.connect(self.huizhi02)
        self.hz_la_tr_2.clicked.connect(self.huizhi03)
        self.hz_la_te_2.clicked.connect(self.huizhi04)
        self.save_la_button.clicked.connect(self.out_model_la)
        # Elastic Net模型
        self.el_action.clicked.connect(self.ss04)
        self.hz_el_tr.clicked.connect(self.huizhi01)
        self.hz_el_te.clicked.connect(self.huizhi02)
        self.hz_el_tr_2.clicked.connect(self.huizhi03)
        self.hz_el_te_2.clicked.connect(self.huizhi04)
        self.save_el_button.clicked.connect(self.out_model_el)
        # Multi-task Lasso模型
        self.mu_action.clicked.connect(self.ss05)
        self.hz_mu_tr.clicked.connect(self.huizhi01)
        self.hz_mu_te.clicked.connect(self.huizhi02)
        self.hz_mu_tr_2.clicked.connect(self.huizhi03)
        self.hz_mu_te_2.clicked.connect(self.huizhi04)
        self.save_mu_button.clicked.connect(self.out_model_mu)
        # Least Angle Regression 模型
        self.le_action.clicked.connect(self.ss06)
        self.hz_le_tr.clicked.connect(self.huizhi01)
        self.hz_le_te.clicked.connect(self.huizhi02)
        self.hz_le_tr_2.clicked.connect(self.huizhi03)
        self.hz_le_te_2.clicked.connect(self.huizhi04)
        self.save_le_button.clicked.connect(self.out_model_le)
        # LARS Lasso 模型
        self.lar_action.clicked.connect(self.ss07)
        self.hz_lar_tr.clicked.connect(self.huizhi01)
        self.hz_lar_te.clicked.connect(self.huizhi02)
        self.hz_lar_tr_2.clicked.connect(self.huizhi03)
        self.hz_lar_te_2.clicked.connect(self.huizhi04)
        self.save_lar_button.clicked.connect(self.out_model_lar)
        # OMP 模型
        self.om_action.clicked.connect(self.ss08)
        self.hz_om_tr.clicked.connect(self.huizhi01)
        self.hz_om_te.clicked.connect(self.huizhi02)
        self.hz_om_tr_2.clicked.connect(self.huizhi03)
        self.hz_om_te_2.clicked.connect(self.huizhi04)
        self.save_om_button.clicked.connect(self.out_model_om)
    
    def ss01(self):
        self.bz()    # 标准化
        self.stt()   # 划分数据集
        self.dtc01()   # LinearRegression模型  
    def ss02(self):
        self.bz()    # 标准化
        self.stt()   # 划分数据集
        self.dtc02()   # Ridge模型
    def ss03(self):
        self.bz()    # 标准化
        self.stt()   # 划分数据集
        self.dtc03()   # Lasso模型
    def ss04(self):
        self.bz()    # 标准化
        self.stt()   # 划分数据集
        self.dtc04()   # Elastic Net模型
    def ss05(self):
        self.bz()    # 标准化
        self.stt()   # 划分数据集
        self.dtc05()   # Multi-task Lasso模型
    def ss06(self):
        self.bz()    # 标准化
        self.stt()   # 划分数据集
        self.dtc06()   # Multi-task Lasso模型
    def ss07(self):
        self.bz()    # 标准化
        self.stt()   # 划分数据集
        self.dtc07()   # Multi-task Lasso模型
    def ss08(self):
        self.bz()    # 标准化
        self.stt()   # 划分数据集
        self.dtc08()   # Multi-task Lasso模型
    
    '''
    数据标准化
    '''
    def bz(self):
        if self.bg01.checkedId() == 1:
            self.x = preprocessing.scale(self.x_data)
        else:
            min_max_scaler = preprocessing.MinMaxScaler()
            self.x = min_max_scaler.fit_transform(self.x_data) 
    '''
    训练数据和测试数据的划分
    '''
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
    # LinearRegression()回归
    def dtc01(self):
        #将y转化为一维形式：self.y_train，self.y_test
        self.y01_train = list()
        self.y01_test = list()
        for a in range(len(self.y_train)):
            self.y01_train.append(self.y_train[a][0])
        for b in range(len(self.y_test)):
            self.y01_test.append(self.y_test[b][0])
            
        #LR算法实现
        self.clf_lr = linear_model.LinearRegression()
        self.clf_lr.fit(self.x_train, self.y01_train)
        self.y_pred = self.clf_lr.predict(self.x_test)
        self.x_pred = self.clf_lr.predict(self.x_train)
        #设置值
        self.stab(self.lr_table02, self.lr_table03)
        self.eetab(self.lr_table01)
    # Ridge回归
    def dtc02(self):
        #将y转化为一维形式：self.y_train，self.y_test
        self.y01_train = list()
        self.y01_test = list()
        for a in range(len(self.y_train)):
            self.y01_train.append(self.y_train[a][0])
        for b in range(len(self.y_test)):
            self.y01_test.append(self.y_test[b][0])
        
        if not self.a_edit.text().strip():
            self.alpha = 1.0
        else:
            self.alpha = float(self.a_edit.text())
        #LR算法实现
        self.clf_ri = linear_model.Ridge(alpha = self.alpha) 
        self.clf_ri.fit(self.x_train, self.y01_train)
        self.y_pred = self.clf_ri.predict(self.x_test)
        self.x_pred = self.clf_ri.predict(self.x_train)
        #设置值
        self.stab(self.ri_table02, self.ri_table03)
        self.eetab(self.ri_table01)
    
    # Lasso回归
    def dtc03(self):
        #将y转化为一维形式：self.y_train，self.y_test
        self.y01_train = list()
        self.y01_test = list()
        for a in range(len(self.y_train)):
            self.y01_train.append(self.y_train[a][0])
        for b in range(len(self.y_test)):
            self.y01_test.append(self.y_test[b][0])
        
        if not self.la_edit.text().strip():
            self.la_alpha = 1.0
        else:
            self.la_alpha = float(self.la_edit.text())
        #LR算法实现
        self.clf_la = linear_model.Lasso(alpha = self.la_alpha) 
        self.clf_la.fit(self.x_train, self.y01_train)
        self.y_pred = self.clf_la.predict(self.x_test)
        self.x_pred = self.clf_la.predict(self.x_train)
        #设置值
        self.stab(self.la_table02, self.la_table03)
        self.eetab(self.la_table01)
    
    # Elastic Net回归
    def dtc04(self):
        #将y转化为一维形式：self.y_train，self.y_test
        self.y01_train = list()
        self.y01_test = list()
        for a in range(len(self.y_train)):
            self.y01_train.append(self.y_train[a][0])
        for b in range(len(self.y_test)):
            self.y01_test.append(self.y_test[b][0])
        
        if not self.el_edit.text().strip():
            self.el_alpha = 1.0
        else:
            self.el_alpha = float(self.la_edit.text())
        if not self.el1_edit.text().strip():
            self.el1_alpha = 0.5
        else:
            self.el1_alpha = float(self.la_edit.text())
        #LR算法实现
        self.clf_el = linear_model.ElasticNet(alpha = self.la_alpha, l1_ratio =self.el1_alpha) 
        self.clf_el.fit(self.x_train, self.y01_train)
        self.y_pred = self.clf_el.predict(self.x_test)
        self.x_pred = self.clf_el.predict(self.x_train)
        #设置值
        self.stab(self.el_table02, self.el_table03)
        self.eetab(self.el_table01)
    
    # Multi-task Lasso 回归
    def dtc05(self):
        #将y转化为一维形式：self.y_train，self.y_test
        self.y01_train = list()
        self.y01_test = list()
        for a in range(len(self.y_train)):
            self.y01_train.append(self.y_train[a][0])
        for b in range(len(self.y_test)):
            self.y01_test.append(self.y_test[b][0])
        
        if not self.mu_edit.text().strip():
            self.mu_alpha = 1.0
        else:
            self.mu_alpha = float(self.mu_edit.text())
        #LR算法实现
        self.clf_mu = linear_model.MultiTaskLasso(alpha = self.mu_alpha) 
        self.clf_mu.fit(self.x_train, self.y01_train)
        self.y_pred = self.clf_mu.predict(self.x_test)
        self.x_pred = self.clf_mu.predict(self.x_train)
        #设置值
        self.stab(self.mu_table02, self.mu_table03)
        self.eetab(self.mu_table01)
    
    # Least Angle Regression回归
    def dtc06(self):
        #将y转化为一维形式：self.y_train，self.y_test
        self.y01_train = list()
        self.y01_test = list()
        for a in range(len(self.y_train)):
            self.y01_train.append(self.y_train[a][0])
        for b in range(len(self.y_test)):
            self.y01_test.append(self.y_test[b][0])
        
        if not self.le_edit.text().strip():
            self.le_alpha = 500
        else:
            self.le_alpha = float(self.le_edit.text())
        #LR算法实现
        self.clf_le = linear_model.Lars(n_nonzero_coefs = self.le_alpha) 
        self.clf_le.fit(self.x_train, self.y01_train)
        self.y_pred = self.clf_le.predict(self.x_test)
        self.x_pred = self.clf_le.predict(self.x_train)
        #设置值
        self.stab(self.le_table02, self.le_table03)
        self.eetab(self.le_table01)
    
    # LARS Lasso 回归
    def dtc07(self):
        #将y转化为一维形式：self.y_train，self.y_test
        self.y01_train = list()
        self.y01_test = list()
        for a in range(len(self.y_train)):
            self.y01_train.append(self.y_train[a][0])
        for b in range(len(self.y_test)):
            self.y01_test.append(self.y_test[b][0])
        
        if not self.lar_edit.text().strip():
            self.lar_alpha = 1.0
        else:
            self.lar_alpha = float(self.lar_edit.text())
        #LR算法实现
        self.clf_lar = linear_model.LassoLars(alpha = self.lar_alpha) 
        self.clf_lar.fit(self.x_train, self.y01_train)
        self.y_pred = self.clf_lar.predict(self.x_test)
        self.x_pred = self.clf_lar.predict(self.x_train)
        #设置值
        self.stab(self.lar_table02, self.lar_table03)
        self.eetab(self.lar_table01)
    
    # OMP 回归
    def dtc08(self):
        #将y转化为一维形式：self.y_train，self.y_test
        self.y01_train = list()
        self.y01_test = list()
        for a in range(len(self.y_train)):
            self.y01_train.append(self.y_train[a][0])
        for b in range(len(self.y_test)):
            self.y01_test.append(self.y_test[b][0])
        
        if not self.om_edit.text().strip():
            self.om_alpha = None
        else:
            self.om_alpha = float(self.om_edit.text())
        #LR算法实现
        self.clf_om = linear_model.OrthogonalMatchingPursuit(n_nonzero_coefs = self.om_alpha) 
        self.clf_om.fit(self.x_train, self.y01_train)
        self.y_pred = self.clf_om.predict(self.x_test)
        self.x_pred = self.clf_om.predict(self.x_train)
        #设置值
        self.stab(self.om_table02, self.om_table03)
        self.eetab(self.om_table01)
    '''
    该模块是对dtable01模块进行设置，即显示训练集的训练结果
    '''
    def eetab(self, mtable01):
        
        #求模型评估指标
        #Mean-dependent-var 和 S.D dependent var
        meanset = list()
        sdset = list()
        self.y01_t = np.array(self.y01_train) # 训练集的真实值
        self.y01_t_mean = np.mean(self.y01_t) # 训练集的真实值的均值
        meanset.append(self.y01_t_mean)
        self.y01_t_var = np.var(self.y01_t) # 训练集的真实值的方差
        sdset.append(self.y01_t_var)
        self.y01_p = np.array(self.x_pred) # 训练集的预测值
        self.y01_p_mean = np.mean(self.y01_p) # 训练集的预测值的均值
        meanset.append(self.y01_p_mean)
        self.y01_p_var = np.var(self.y01_p) # 训练集的预测值的方差
        sdset.append(self.y01_p_var)
        self.y02_t = np.array(self.y01_test) # 测试集的真实值
        self.y02_t_mean = np.mean(self.y02_t) # 测试集的真实值的均值
        meanset.append(self.y02_t_mean)
        self.y02_t_var = np.var(self.y02_t) # 测试集的真实值的方差
        sdset.append(self.y02_t_var)
        self.y02_p = np.array(self.y_pred) # 测试集的预测值
        self.y02_p_mean = np.mean(self.y02_p) # 测试集的预测值的均值
        meanset.append(self.y02_p_mean)
        self.y02_p_var = np.var(self.y02_p) # 测试集的预测值的方差
        sdset.append(self.y02_p_var)
        
        # SST, SSR 和 SSE
        s_s_s = list()
        train_SST = 0 #训练集
        train_SSR = 0
        train_SSE = 0
        for a1 in range(len(self.x_pred)):
            train_SST += (self.y01_train[a1] - self.y01_t_mean)*(self.y01_train[a1] - self.y01_t_mean)
            train_SSR += (self.x_pred[a1] - self.y01_p_mean)*(self.x_pred[a1] - self.y01_p_mean)
            train_SSE += (self.y01_train[a1] - self.x_pred[a1])*(self.y01_train[a1] - self.x_pred[a1])
        print (train_SST, train_SSR, train_SSE)
        s_s_s.append(train_SST)
        s_s_s.append(train_SSR)
        s_s_s.append(train_SSE)
        test_SST = 0 #测试集
        test_SSR = 0
        test_SSE = 0
        for a2 in range(len(self.y_pred)):
            test_SST += (self.y01_test[a2] - self.y02_t_mean)*(self.y01_test[a2] - self.y02_t_mean)
            test_SSR += (self.y_pred[a2] - self.y02_p_mean)*(self.y_pred[a2] - self.y02_p_mean)
            test_SSE += (self.y01_test[a2] - self.y_pred[a2])*(self.y01_test[a2] - self.y_pred[a2])
        print (test_SST, test_SSR, test_SSE)
        s_s_s.append(test_SST)
        s_s_s.append(test_SSR)
        s_s_s.append(test_SSE)
        
        #S.E regression，F-statistic 和 R-squared
        ser = list()
        train_SER = 0
        test_SER = 0
        train_F = 0
        test_F = 0
        train_R = 0
        test_R = 0
        #求训练集和测试集的 S.E regression
        train_SER = math.sqrt(train_SSE/(len(self.x_train)-len(self.x_train[0])))
        test_SER = math.sqrt(test_SSE/(len(self.x_test)-len(self.x_test[0])))
        #求训练集和测试集的 F-statistic
        train_F = (train_SSE/len(self.x_train[0]))/(train_SSR/(len(self.x_train)-len(self.x_train[0])-1))
        test_F = (test_SSE/len(self.x_train[0]))/(test_SSR/(len(self.x_train)-len(self.x_train[0])-1))
        #求训练集和测试集的R-squared
        train_R =1-(train_SSR/train_SST)
        test_R =1-(test_SSR/test_SST)
        ser.append(train_SER)
        ser.append(test_SER)
        ser.append(train_F)
        ser.append(test_F)
        ser.append(train_R)
        ser.append(test_R)
        
        #设置单元格的行数和列数
        mtable01.setRowCount(9)
        mtable01.setColumnCount(6)
        labels01 = ['训练集真实值y1','训练集预测值y1_pred','测试集真实值y2','测试集预测值y2_pred']
        for i in range(len(labels01)): # 添加Mean-dependent-var 和 S.D dependent var
            mtable01.setItem(0,i, QtGui.QTableWidgetItem(labels01[i].decode('utf8')))
            mtable01.setItem(1,i, QtGui.QTableWidgetItem(str(meanset[i])))
            mtable01.setItem(2,i, QtGui.QTableWidgetItem(str(sdset[i])))
        
        labels02 = ['训练集SST','训练集SSR','训练集SSE','测试集SST','测试集SSR','测试集SSE']
        for j in range(len(labels02)): # SST, SSR 和 SSE
            mtable01.setItem(4,j, QtGui.QTableWidgetItem(labels02[j].decode('utf8')))
            mtable01.setItem(5,j, QtGui.QTableWidgetItem(str(s_s_s[j])))
        labels03 = ['训练集SER','测试集SER','训练集F-statistic','测试集F-statistic','训练集R-squared','测试集R-squared']
        for k in range(len(labels03)): # S.E regression
            mtable01.setItem(7,k, QtGui.QTableWidgetItem(labels03[k].decode('utf8')))
            mtable01.setItem(8,k, QtGui.QTableWidgetItem(str(ser[k])))
        
    def stab(self, mtable02, mtable03):
        '''
        该模块是对dtable02模块进行设置，即显示训练集的训练结果
        '''
        #设置单元格的行数和列数
        mtable02.setRowCount(len(self.x_pred))
        mtable02.setColumnCount(2)
        mtable02.setHorizontalHeaderLabels(['real','pred'])
        for s in range(len(self.x_pred)):
            if self.y01_train[s] == self.x_pred[s]:
                mtable02.setItem(s,0, QtGui.QTableWidgetItem(str(self.y01_train[s])))
                mtable02.setItem(s,1, QtGui.QTableWidgetItem(str(self.x_pred[s])))
                mtable02.item(s,0).setBackgroundColor(QtGui.QColor(214, 71, 0))
                mtable02.item(s,1).setBackgroundColor(QtGui.QColor(214, 71, 0))
            else: 
                mtable02.setItem(s,0, QtGui.QTableWidgetItem(str(self.y01_train[s])))
                mtable02.setItem(s,1, QtGui.QTableWidgetItem(str(self.x_pred[s])))
        '''
        该模块是对dtable03模块进行设置，显示测试集的测试结果
        '''
        #设置单元格的行数和列数
        mtable03.setRowCount(len(self.y_pred))
        mtable03.setColumnCount(2)
        mtable03.setHorizontalHeaderLabels(['real','pred'])
        for s in range(len(self.y_pred)):
            if self.y01_test[s] == self.y_pred[s]:
                mtable03.setItem(s,0, QtGui.QTableWidgetItem(str(self.y01_test[s])))
                mtable03.setItem(s,1, QtGui.QTableWidgetItem(str(self.y_pred[s])))
                mtable03.item(s,0).setBackgroundColor(QtGui.QColor(214, 71, 0))
                mtable03.item(s,1).setBackgroundColor(QtGui.QColor(214, 71, 0))
            else: 
                mtable03.setItem(s,0, QtGui.QTableWidgetItem(str(self.y01_test[s])))
                mtable03.setItem(s,1, QtGui.QTableWidgetItem(str(self.y_pred[s])))
    
    '''
    绘制图
    '''
    def huizhi01(self):
        y_train = np.array(self.y01_train)
        y_train_pred = np.array(self.x_pred)
        x_train = range(len(y_train))
        plt.figure(1,figsize=(8,6))
        plt.plot(x_train, y_train,label = "$true$",color='blue',linewidth=2)
        plt.plot(x_train, y_train_pred,'r--',label="$pred$")
        plt.xlabel("Sample number")
        plt.ylabel("Value of Y")
        plt.title("Comparison of the real value and the predictive value of TrainSet")
        plt.show()
    
    def huizhi02(self):
        y_test = np.array(self.y01_test)
        y_test_pred = np.array(self.y_pred)
        x_test = range(len(y_test))
        plt.figure(2,figsize=(8,6))
        plt.plot(x_test, y_test,label = "$true$",color='blue',linewidth=2)
        plt.plot(x_test, y_test_pred,'r--',label="$pred$")
        plt.xlabel("Sample number")
        plt.ylabel("Value of Y")
        plt.title("Comparison of the real value and the predictive value of TestSet")
        plt.show()
    
    def huizhi03(self):
        y_train = np.array(self.y01_train)
        y_train_pred = np.array(self.x_pred)
        plt.figure(3,figsize=(8,6))
        plt.plot(y_train, y_train_pred,'r.')
        plt.xlabel("True value of Y")
        plt.ylabel("Predictive value of Y")
        plt.title("Comparison of real value and predictive value of TrainSet (YY map)")
        plt.show()
    
    def huizhi04(self):
        y_test = np.array(self.y01_test)
        y_test_pred = np.array(self.y_pred)
        plt.figure(4,figsize=(8,6))
        plt.plot(y_test, y_test_pred,'r.')
        plt.xlabel("True value of Y")
        plt.ylabel("Predictive value of Y")
        plt.title("Comparison of real value and predictive value of TestSet (YY map)")
        plt.show()
    '''
    保存模型
    '''
    def out_model_lr(self):
        self.filepath=str(QtGui.QFileDialog.getSaveFileName(self,"文件保存","F:/","Model Files (*.model)"))
        joblib.dump(self.clf_lr, self.filepath.decode('GB2312'))    
    
    def out_model_ri(self):
        self.filepath=str(QtGui.QFileDialog.getSaveFileName(self,"文件保存","F:/","Model Files (*.model)"))
        joblib.dump(self.clf_ri, self.filepath.decode('GB2312'))    
    
    def out_model_la(self):
        self.filepath=str(QtGui.QFileDialog.getSaveFileName(self,"文件保存","F:/","Model Files (*.model)"))
        joblib.dump(self.clf_la, self.filepath.decode('GB2312'))    
    def out_model_el(self):
        self.filepath=str(QtGui.QFileDialog.getSaveFileName(self,"文件保存","F:/","Model Files (*.model)"))
        joblib.dump(self.clf_el, self.filepath.decode('GB2312'))
    def out_model_mu(self):
        self.filepath=str(QtGui.QFileDialog.getSaveFileName(self,"文件保存","F:/","Model Files (*.model)"))
        joblib.dump(self.clf_mu, self.filepath.decode('GB2312'))   
    def out_model_le(self):
        self.filepath=str(QtGui.QFileDialog.getSaveFileName(self,"文件保存","F:/","Model Files (*.model)"))
        joblib.dump(self.clf_le, self.filepath.decode('GB2312'))    
    def out_model_lar(self):
        self.filepath=str(QtGui.QFileDialog.getSaveFileName(self,"文件保存","F:/","Model Files (*.model)"))
        joblib.dump(self.clf_lar, self.filepath.decode('GB2312'))
    def out_model_om(self):
        self.filepath=str(QtGui.QFileDialog.getSaveFileName(self,"文件保存","F:/","Model Files (*.model)"))
        joblib.dump(self.clf_om, self.filepath.decode('GB2312'))    


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())  
    