# -*- coding: utf-8 -*-
"""
决策树参数设置模块
    1.每一个算法模块的参数设置都是独立的，因此，对独立模块的修改不影响其他的
    2.
"""

import sys 
import math
from PyQt4 import QtGui, uic
#导入决策树模块
from sklearn import tree 
#导入标准化模块
from sklearn import preprocessing
#导入混合矩阵模块
import mm_matrix
#导入Roc模块
import proc_s
#导入混淆矩阵计算模块
from sklearn.metrics import confusion_matrix
#导入字符流模块
from sklearn.externals.six import StringIO 
#导入保存模型的模块
from sklearn.externals import joblib
#导入树结构显示模块 
import dt_views

qtCreatormainFile = "./rob/dt.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatormainFile)
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        self.x_data = list()
        self.y_data = list()
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.dt_action.clicked.connect(self.ss)
        self.mm_Button01.clicked.connect(self.ptu01)
        self.mm_Button02.clicked.connect(self.ptu02)
        self.roc_Button.clicked.connect(self.pro)
        self.dtp_Button.clicked.connect(self.pshu)
        self.save_button.clicked.connect(self.out_model)
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
    
    #计算各种分类评估指标    
    def cmm(self,cm):
        ls = dict()
        for i in range(len(cm)):
            tmp = list()
            tp = cm[i][i]
            fp = sum(cm.T[i])-tp
            fn = sum(cm[i])-tp
            tn = sum(sum(cm))-tp-fp-fn
            #求每个类别对应的评估值
            if tp != 0 :
                TPR = float(tp)/(tp+fn)    #真正率   
            else:
                TPR = 0
            if fn != 0 :
                FNR = float(fn)/(fp+tn)    #假负率
            else:
                FNR = 0
            if fp != 0 :
                FPR = float(fp)/(fp+tn)    #假正率
            else:
                FPR = 0
            if tn !=0 :
                TNR = float(tn)/(tn+fp)    #真负率
            else:
                TNR = 0
    
            tmp.append(TPR)
            tmp.append(FNR)
            tmp.append(FPR)
            tmp.append(TNR)
            if tp != 0:
                P = float(tp)/(tp+fp)      #精确度
                R = float(tp)/(tp+fn)      #召回率
                F_score = 2*P*R/(P+R)   #查准率和查全率的的调和平均值
            else:
                P = 0
                R = 0
                F_score = 0
            tmp.append(P)
            tmp.append(R)
            tmp.append(F_score)
            
            ls[self.labels[i]] = tmp
        return ls
    
    '''
    对每个参数的值判断是否为空
    '''
    def para(self):
        # 对每个参数的值判断是否为空
        # splitter参数的设置
        if not self.sp_box.itemText(self.sp_box.currentIndex()).strip():
            self.splitter = 'best'
        else:
            self.splitter = self.sp_box.itemText(self.sp_box.currentIndex())
        # criterion参数的设置
        if not self.cr_box.itemText(self.cr_box.currentIndex()).strip():
            self.criterion = 'gini'
        else:
            self.criterion = self.cr_box.itemText(self.cr_box.currentIndex())
        # max_depth参数的设置
        if not self.md_edit.text().strip():
            self.max_depth = None
        else:
            self.max_depth = int(self.md_edit.text())
        # random_state参数的设置
        if not self.rs_edit.text().strip():
            self.random_state = None
        else:
            self.random_state = int(self.rs_edit.text())
        # class_w参数的设置
        if self.cw_box.itemText(self.cw_box.currentIndex()) == 'None':
            self.class_w = None
        else:
            self.class_w = self.cw_box.itemText(self.cw_box.currentIndex())
        # min_sl参数的设置
        if not self.msl_edit.text().strip():
            self.min_sl = 1
        else:
            self.min_sl = int(self.msl_edit.text())
        # max_f参数的设置
        if self.mf_box.itemText(self.mf_box.currentIndex()) == 'None':
            self.max_f = None
        else:
            self.max_f = self.mf_box.itemText(self.mf_box.currentIndex())
        # max_ln参数的设置
        if not self.mln_edit.text().strip():
            self.max_ln = None
        else:
            self.max_ln = int(self.mln_edit.text())
        # min_ss参数的设置
        if not self.mss_edit.text().strip():
            self.min_ss = 2
        else:
            self.min_ss = int(self.mss_edit.text())
        # min_wfl参数的设置
        if not self.wfl_edit.text().strip():
            self.min_wfl = 0.0
        else:
            self.min_wfl = float(self.wfl_edit.text())
        # presort参数的设置
        if self.pre_box.itemText(self.pre_box.currentIndex()) == 'False':
            self.presort = False
        else:
            self.presort = self.pre_box.itemText(self.pre_box.currentIndex())
    
    '''
    主函数
    '''
    def dtc(self):
        self.para()  #获取所有参数
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
        
        #knn算法实现
        self.clf = tree.DecisionTreeClassifier(
                 criterion = self.criterion,
                 splitter = self.splitter,
                 max_depth = self.max_depth,
                 min_samples_split = self.min_ss,
                 min_samples_leaf = self.min_sl,
                 min_weight_fraction_leaf = self.min_wfl,
                 max_features = self.max_f,
                 random_state = self.random_state,
                 max_leaf_nodes = self.max_ln,
                 class_weight = self.class_w,
                 presort = self.presort)
        
        
        self.clf.fit(self.x_train, self.y01_train)
        
        self.y_pred = self.clf.predict(self.x_test)
        self.x_pred = self.clf.predict(self.x_train)
        
        
        '''
        该模块是对dtable01模块进行设置，即显示训练集的训练结果
        '''
        #设置单元格的行数和列数
        self.dtable01.setRowCount(3*len(self.labels))
        self.dtable01.setColumnCount(8)
        lab = ['真正率(TPR)','假负率(FNR)'
        ,'假正率(FPR)','真负率(TNR)','精确度(PRE)','召回率(REC)','F-SCORE']
        
        #训练数据
        xcm = confusion_matrix(self.y01_train, self.x_pred)
        self.train_precision = 0.0
        for i in range(len(xcm)): 
            self.train_precision += xcm[i][i]
        self.train_precision = self.train_precision/sum(sum(xcm))
        print (xcm)
        
        #测试数据
        tcm = confusion_matrix(self.y01_test, self.y_pred)
        self.test_precision = 0.0
        for i in range(len(tcm)): 
            self.test_precision += tcm[i][i]
        self.test_precision = self.test_precision/sum(sum(tcm))
        print (tcm)
        #求出每个类别labels作为正样本的TP,FP,FN,TN,以字典的形式存储
        xls = self.cmm(xcm)
        tls = self.cmm(tcm)
        #计算训练 每个类别labels对应的评估值
        num=0
        for key in xls:
            
            tmp01 = xls[key]
            tmp02 = tls[key]
            mlan = "类别："+str(key)
            self.dtable01.setItem(num,0, QtGui.QTableWidgetItem(mlan.decode('utf-8')))
            self.dtable01.setItem(num+1,0, QtGui.QTableWidgetItem('train'))
            self.dtable01.setItem(num+2,0, QtGui.QTableWidgetItem('test'))
            for j in range(len(tmp01)):
                
                self.dtable01.setItem(num,j+1, QtGui.QTableWidgetItem(lab[j].decode('utf-8')))
                self.dtable01.setItem(num+1,j+1, QtGui.QTableWidgetItem(str(round(tmp01[j],2))))
                self.dtable01.setItem(num+2,j+1, QtGui.QTableWidgetItem(str(round(tmp02[j],2))))
            num =num + 3
             
        '''
        该模块是对dtable02模块进行设置，即显示训练集的训练结果
        '''
        #设置单元格的行数和列数
        self.dtable02.setRowCount(len(self.x_pred))
        self.dtable02.setColumnCount(2)
        self.dtable02.setHorizontalHeaderLabels(['real','pred'])
        
        for s in range(len(self.x_pred)):
            if self.y01_train[s] == self.x_pred[s]:
                self.dtable02.setItem(s,0, QtGui.QTableWidgetItem(str(self.y01_train[s])))
                self.dtable02.setItem(s,1, QtGui.QTableWidgetItem(str(self.x_pred[s])))
                self.dtable02.item(s,0).setBackgroundColor(QtGui.QColor(214, 71, 0))
                self.dtable02.item(s,1).setBackgroundColor(QtGui.QColor(214, 71, 0))
            else: 
                self.dtable02.setItem(s,0, QtGui.QTableWidgetItem(str(self.y01_train[s])))
                self.dtable02.setItem(s,1, QtGui.QTableWidgetItem(str(self.x_pred[s])))
        
        '''
        该模块是对dtable03模块进行设置，显示测试集的测试结果
        '''
        #设置单元格的行数和列数
        self.dtable03.setRowCount(len(self.y_pred))
        self.dtable03.setColumnCount(2)
        self.dtable03.setHorizontalHeaderLabels(['real','pred'])
        
        for s in range(len(self.y_pred)):
            if self.y01_test[s] == self.y_pred[s]:
                self.dtable03.setItem(s,0, QtGui.QTableWidgetItem(str(self.y01_test[s])))
                self.dtable03.setItem(s,1, QtGui.QTableWidgetItem(str(self.y_pred[s])))
                self.dtable03.item(s,0).setBackgroundColor(QtGui.QColor(214, 71, 0))
                self.dtable03.item(s,1).setBackgroundColor(QtGui.QColor(214, 71, 0))
            else: 
                self.dtable03.setItem(s,0, QtGui.QTableWidgetItem(str(self.y01_test[s])))
                self.dtable03.setItem(s,1, QtGui.QTableWidgetItem(str(self.y_pred[s])))
        
        '''
        该模块是对train_e模块进行设置，显示测试集的测试结果
        ''' 
        self.train_e.setText(str(round(self.train_precision,3)))
        self.test_e.setText(str(round(self.test_precision,3)))
    
    #保存模型
    def out_model(self):
        self.filepath=str(QtGui.QFileDialog.getSaveFileName(self,"文件保存","F:/","Model Files (*.model)"))
        joblib.dump(self.clf, self.filepath.decode('GB2312'))    

    #画出树结构
    def pshu(self):
        dot_data = StringIO()
        tree.export_graphviz(self.clf, out_file=dot_data)
        graph = dot_data.getvalue()
        self.dt = dt_views.MyApp(graph)
        self.dt.show()
        print (graph)
    #对应mm_Button01的函数     
    def ptu01(self):
        #画图train混淆矩阵窗口
        mm = mm_matrix.c_matrix()
        mm.labels = self.labels
        mm.y_true = self.y01_train
        mm.y_pred = self.x_pred
        mm.p_tu()
    
    #对应mm_Button02的函数
    def ptu02(self):
        #画图train混淆矩阵窗口
        mm = mm_matrix.c_matrix()
        mm.labels = self.labels
        mm.y_true = self.y01_test
        mm.y_pred = self.y_pred
        mm.p_tu()
    #对应roc_Button的函数
    def pro(self):
        
        p_roc = proc_s.proc()
        p_roc.y_true =self.y01_test
        p_roc.y_pred = self.y_pred
        p_roc.labels = self.labels
        p_roc.mroc()
         



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())  
