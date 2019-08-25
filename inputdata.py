# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 19:24:16 2016

@author: Administrator
"""

import sys 
from PyQt4 import QtGui, uic
import xlrd as xl
import knn_action
import rf_action
import dt_action
import svm_action
import by_action
import feature_action
import ls_action
import lda_action
import pca_action
import rbm_action
#窗口调用模块
qtCreatorFile = "./rob/inputdata.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

#定义窗口方法
class MyApp(QtGui.QDialog,Ui_MainWindow):
    #依据模块定义界面
    def __init__(self):
        self.sf = int()
        #初始Window框架
        QtGui.QMainWindow.__init__(self)
        #初始UI界面
        Ui_MainWindow.__init__(self)
        #依据QT设置UI
        self.setupUi(self)
        #对ridio加入组bg中
        self.bg = QtGui.QButtonGroup()
        self.bg.addButton(self.s_radio_1,1)
        self.bg.addButton(self.s_radio_2,2)
        #默认定义s_radio_2这个控件被选中
        self.s_radio_2.setChecked(True)
        #对Data_In_Button按钮的响应，即打开文件按钮
        self.Data_In_Button.clicked.connect(self.data_In)
        #对p_iv按钮的响应，即选择自变量部分
        self.p_iv.clicked.connect(self.data_iv)
        #对p_dv按钮的响应，即选择因变量部分
        self.p_dv.clicked.connect(self.data_dv)
        #对pmButton按钮的响应，即进入模块设置模块部分
        self.pmButton.clicked.connect(self.dataspilt)
    
    #Data_In_Button按钮的响应函数，数据导入显示界面
    def data_In(self):
        #打开文件的框架
        self.filepath=str(QtGui.QFileDialog.getOpenFileName(self))
        # self.filepath = json.dumps(self.filepath)
        self.filename.setText(self.filepath)
        #转化文件格式
        path = self.filepath.replace('\\',"/")
        #取出文件尾缀
        t_datas = self.filepath.split('.')
        #依据不同的为尾缀对文件进行不同的读入
        if len(t_datas) == 2:
            #如果尾缀是xlsx
            if t_datas[1] == 'xlsx' or t_datas[1] == 'xls':
                #导入xlsx文件，即所有数据在框中显示
                self.input_xlsx(path)
                #取出数据中的特征，并为其独立命名，以s_x的形式，显示在框中
                self.spitdata()
    
    #对p_iv按钮的响应函数，放入的是自变量         
    def data_iv(self):
        #定义一个list用于存储选中特征的列值
        self.iv_list = list()
        #获取单元格被选中的值，该items是特定的object
        items = self.charatable.selectedItems()
        #设置单元格的行数和列数
        ml = len(items)
        self.ivtable.setRowCount(ml)
        self.ivtable.setColumnCount(1)
        #遍历出items中的值，并让其在自变量框中显示
        for i in range(ml):
            str01 = str(items[i].text()).split('_')
            if len(str01)==2:
                #存入自变量的列标
                self.iv_list.append(int(str01[1])-1)
            #显示选中的自变量
            self.ivtable.setItem(i,0, QtGui.QTableWidgetItem(str(items[i].text())))
    
    #对p_dv按钮的响应，放入的是因变量
    def data_dv(self):
        #定义一个list用于存储选中特征的列值
        self.dv_list = list()
        #获取单元格被选中的值，该items是特定的object
        items = self.charatable.selectedItems()
        #设置单元格的行数和列数
        ml = len(items)
        self.dvtable.setRowCount(ml)
        self.dvtable.setColumnCount(1)
        #遍历出items中的值，并让其在因变量框中显示
        for i in range(ml):
            str01 = str(items[i].text()).split('_')
            if len(str01)==2:
                #存入因变量的列标
                self.dv_list.append(int(str01[1])-1)
            #显示选中的因变量    
            self.dvtable.setItem(i,0, QtGui.QTableWidgetItem(str(items[i].text())))
        
    #对xlsx文件的读取
    def input_xlsx(self,path):
        #读取xlsx文件的数据进入self.fcontent
        filelist = xl.open_workbook(path,'r')
        #读xlsx中的sheet0页面中的数据
        table = filelist.sheet_by_index(0)
        #读取xlsx文件的行数和列数        
        nrow = table.nrows
        ncol = table.ncols
        #设置单元格的行数和列数
        self.datatable.setRowCount(nrow)
        self.datatable.setColumnCount(ncol)
        #定义一个fcontent用于存储数据
        self.fcontent = list()       
        for i in range(nrow) :
            fco = list()
            for j in range(ncol) :
                fco.append(table.cell(i,j).value)
            self.fcontent.append(fco)
        #显示数据
        for j in range(nrow):
            for i in range(ncol):
                self.datatable.setItem(j,i, QtGui.QTableWidgetItem(str(self.fcontent[j][i])))
    
    #抽出特征
    def spitdata(self):
        ncol = len(self.fcontent[0])
        #设置单元格的行数和列数
        self.charatable.setRowCount(ncol)
        self.charatable.setColumnCount(1)
        #显示特征值，此值为自己重定义的值
        for s in range(ncol):
            st01 = 's_'+str(s+1)
            self.charatable.setItem(s,0, QtGui.QTableWidgetItem(str(st01)))
        
    #数据处理，按选择的要求进行划分
    def dataspilt(self):
        #定义自变量和因变量
        self.x_data=list()
        self.y_data=list()
        #定义一个数据存储首行处理后的数据
        data = list()
        #对首行进行处理
        ml = len(self.fcontent)
        mh = len(self.fcontent[0])
        #如果redio选项框中选择第一个就返回一个1，若选择第二个就返回2
        if self.bg.checkedId() == 2:#返回2就是首行去除
            for i in range(ml):
                tmp03 =list()
                if i != 0 :#去除首行
                    for j in range(mh):
                        tmp03.append(self.fcontent[i][j])
                    data.append(tmp03)
        else:#保留首行
            data=self.fcontent
        #对数据的划分按你选择的特征标准
        for a in range(len(data)):
            tmp01 = list()
            tmp02 = list()
            #提取数据中的自变量部分
            for b in self.iv_list :
                tmp01.append(data[a][b])
            self.x_data.append(tmp01)
            #提取数据中的因变量部分
            for z in self.dv_list:
                tmp02.append(data[a][z])
            self.y_data.append(tmp02)
        #打开下一个窗口
        if self.sf == 1 :
            self.knn_window01 = knn_action.MyApp()
            self.knn_window01.x_data=self.x_data
            self.knn_window01.y_data=self.y_data
            self.knn_window01.show()
        elif self.sf == 2 :
            self.rf_window01 = rf_action.MyApp()
            self.rf_window01.x_data=self.x_data
            self.rf_window01.y_data=self.y_data
            self.rf_window01.show()
        elif self.sf == 3 :
            self.dt_window01 = dt_action.MyApp()
            self.dt_window01.x_data=self.x_data
            self.dt_window01.y_data=self.y_data
            self.dt_window01.show()
        elif self.sf == 4 :
            self.svm_window01 = svm_action.MyApp()
            self.svm_window01.x_data=self.x_data
            self.svm_window01.y_data=self.y_data
            self.svm_window01.show()
        elif self.sf == 5 :
            self.by_window01 = by_action.MyApp()
            self.by_window01.x_data=self.x_data
            self.by_window01.y_data=self.y_data
            self.by_window01.show()
        elif self.sf == 6 :
            self.fe_window01 = feature_action.MyApp()
            self.fe_window01.x_data=self.x_data
            self.fe_window01.y_data=self.y_data
            self.fe_window01.show()
        elif self.sf == 7 :
            self.ls_window01 = ls_action.MyApp()
            self.ls_window01.x_data=self.x_data
            self.ls_window01.y_data=self.y_data
            self.ls_window01.show()
        elif self.sf == 8 :
            self.lda_window01 = lda_action.MyApp()
            self.lda_window01.x_data=self.x_data
            self.lda_window01.y_data=self.y_data
            self.lda_window01.show()
        elif self.sf == 9 :
            self.pca_window01 = pca_action.MyApp()
            self.pca_window01.x_data=self.x_data
            self.pca_window01.y_data=self.y_data
            self.pca_window01.show()
        elif self.sf == 10 :
            self.rbm_window01 = rbm_action.MyApp()
            self.rbm_window01.x_data=self.x_data
            self.rbm_window01.y_data=self.y_data
            self.rbm_window01.show()
        #print self.y_data

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())