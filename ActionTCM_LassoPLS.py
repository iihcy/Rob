# coding=utf-8

from numpy import *
import wx
import ModelTCM_LassoPLS

"""
    模型参数设置
"""
#coding=utf-8
import wx
import wx.grid
# from wx import *

'''
    Page1.数据信息--选项卡one
      输入：中医药数据_TCM.txt
      输出基本信息： 1)x与y;  2)标准化后的e0与f0;  3)均值mean_x与mean_y;  4)标准差std_x与std_y等
'''
class Page1(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent)
        # 定义TextCtrl文本
        self.txt_Contents = wx.TextCtrl(self, -1, u'样本基本信息:',style=wx.TE_MULTILINE | wx.HSCROLL, size=(400, 120), pos=(40, 20))
        self.txt_Contents.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.NORMAL))

        # 定义Button按钮--第一行
        sample_button = wx.Button(self, label=u" 数据信息 ", pos=(80, 160))
        XButton = wx.Button(self, label=u" 矩阵 X ", pos=(190, 160))
        YButton = wx.Button(self, label=u" 矩阵 Y ", pos=(300, 160))
        # 定义Button按钮--第二行
        eBbutton = wx.Button(self, label=u" 标准化 E ", pos=(80, 210))
        fBbutton = wx.Button(self, label=u" 标准化 F ", pos=(190, 210))
        mean_xbutton = wx.Button(self, label=u" 均值 X ", pos=(300, 210))
        # 定义Button按钮--第三行
        mean_ybutton = wx.Button(self, label=u" 均值 Y ", pos=(80, 260))
        std_xbutton = wx.Button(self, label=u" 标准差 X ", pos=(190, 260))
        std_ybutton = wx.Button(self, label=u" 标准差 Y ", pos=(300, 260))

        #定义事件
        self.Bind(wx.EVT_BUTTON, self.Onsample_button, sample_button)
        self.Bind(wx.EVT_BUTTON, self.On_XButton, XButton)
        self.Bind(wx.EVT_BUTTON, self.On_YButton, YButton)
        self.Bind(wx.EVT_BUTTON, self.On_eBbutton, eBbutton)
        self.Bind(wx.EVT_BUTTON, self.On_fBbutton, fBbutton)
        self.Bind(wx.EVT_BUTTON, self.On_meanxbutton, mean_xbutton)
        self.Bind(wx.EVT_BUTTON, self.On_meanybutton, mean_ybutton)
        self.Bind(wx.EVT_BUTTON, self.On_stdxbutton, std_xbutton)
        self.Bind(wx.EVT_BUTTON, self.On_stdybutton, std_ybutton)


    # 获取模型的样本信息
    def Onsample_button(self, event):
        self.txt_Contents.Clear()
        x, y, e0, f0, e0_row, e0_col, mean_x, mean_y, std_x, std_y = self.dataSourse()
        e0_row = str(e0_row);  e0_col = str(e0_col);  y_col = shape(y)[1];  y_col = str(y_col)
        assist = "========================"; Space="   "
        #数据基本信息
        self.txt_Contents.AppendText(assist + '\n' + u"☞☞☞数据信息☜☜☜" +Space + '\n'+ u"◆样本数量："+ e0_row + '; ' + Space
                                     + u"◆特征(自变量)数量："+ e0_col+ '; ' + Space + u"◆因变量数量：" + y_col+ '; ' + '\n' +assist + '\n')
        event.Skip()

    # 获取矩阵X
    def On_XButton(self,event):
        self.txt_Contents.Clear()
        x, y, e0, f0, e0_row, e0_col, mean_x, mean_y, std_x, std_y = self.dataSourse()
        x = str(x) # 转换为字符形式
        assist = "========================"
        self.txt_Contents.AppendText(assist + '\n' + u"☞☞☞矩阵X☜☜☜ " + '\n'  + x + '\n' + assist + '\n')
        event.Skip()

    # 获取矩阵Y
    def On_YButton(self, event):
        self.txt_Contents.Clear()
        x, y, e0, f0, e0_row, e0_col, mean_x, mean_y, std_x, std_y = self.dataSourse()
        y = str(y.T)  # 转换为字符形式
        assist = "========================"
        self.txt_Contents.AppendText(assist + '\n' + u"☞☞☞矩阵Y☜☜☜ " + '\n' + y + '\n' + assist + '\n')
        event.Skip()
    # 获取标准化后的矩阵X--E
    def On_eBbutton(self, event):
        self.txt_Contents.Clear()
        x, y, e0, f0, e0_row, e0_col, mean_x, mean_y, std_x, std_y = self.dataSourse()
        e0 = str(e0)  # 转换为字符形式
        assist = "========================"
        self.txt_Contents.AppendText(assist + '\n' + u"☞☞☞标准化E☜☜☜ " + '\n' + e0 + '\n' + assist + '\n')
        event.Skip()

    # 获取标准化后的矩阵Y--F
    def On_fBbutton(self, event):
        self.txt_Contents.Clear()
        x, y, e0, f0, e0_row, e0_col, mean_x, mean_y, std_x, std_y = self.dataSourse()
        f0 = str(f0.T)  # 转换为字符形式
        assist = "========================"
        self.txt_Contents.AppendText(assist + '\n' + u"☞☞☞标准化F☜☜☜ " + '\n' + f0 + '\n' + assist + '\n')
        event.Skip()

    # 获取均值X
    def On_meanxbutton(self, event):
        self.txt_Contents.Clear()
        x, y, e0, f0, e0_row, e0_col, mean_x, mean_y, std_x, std_y = self.dataSourse()
        mean_x = str(mean_x)  # 转换为字符形式
        assist = "========================"
        self.txt_Contents.AppendText(assist + '\n' + u"☞☞☞均值X☜☜☜ " + '\n' + mean_x + '\n' + assist + '\n')
        event.Skip()

    # 获取均值Y
    def On_meanybutton(self, event):
        self.txt_Contents.Clear()
        x, y, e0, f0, e0_row, e0_col, mean_x, mean_y, std_x, std_y = self.dataSourse()
        mean_y = str(mean_y)  # 转换为字符形式
        assist = "========================"
        self.txt_Contents.AppendText(assist + '\n' + u"☞☞☞均值Y☜☜☜ " + '\n' + mean_y + '\n' + assist + '\n')
        event.Skip()

    # 获取标准差X
    def On_stdxbutton(self, event):
        self.txt_Contents.Clear()
        x, y, e0, f0, e0_row, e0_col, mean_x, mean_y, std_x, std_y = self.dataSourse()
        std_x = str(std_x)  # 转换为字符形式
        assist = "========================"
        self.txt_Contents.AppendText(assist + '\n' + u"☞☞☞标准差X☜☜☜ " + '\n' + std_x + '\n' + assist + '\n')
        event.Skip()

    # 获取标准差Y
    def On_stdybutton(self, event):
        self.txt_Contents.Clear()
        x, y, e0, f0, e0_row, e0_col, mean_x, mean_y, std_x, std_y = self.dataSourse()
        std_y = str(std_y)  # 转换为字符形式
        assist = "========================"
        self.txt_Contents.AppendText(assist + '\n' + u"☞☞☞标准差Y☜☜☜ " + '\n' + std_y + '\n' + assist + '\n')
        event.Skip()

    #构造--获取数据源
    def dataSourse(filename):
       x, y = ModelTCM_LassoPLS.loadDataSet01("TCMdata.txt")
       e0, f0, e0_row, e0_col = ModelTCM_LassoPLS.stardantDataSet(x, y)
       mean_x, mean_y, std_x, std_y = ModelTCM_LassoPLS.data_Mean_Std(x, y)
       return x, y, e0, f0, e0_row, e0_col, mean_x, mean_y, std_x, std_y


'''
    Page2.特征分析--选项卡two
        1)获取原始回归系数；
        2）获取改进算法的回归系数，即特征系数；
        3）返回选择出的特征（自变量）系数；
'''
class Page2(wx.Panel):
    xishu = ''
    def __init__(self,parent):
        wx.Panel.__init__(self, parent)
        # 界面布局
        self.text_top01 = wx.StaticText(self, 0, u"特征选择后的自变量:", style=wx.TE_LEFT, pos=(20, 12))
        self.text_top02 = wx.StaticText(self, 0, u"PLS原始的回归系数:", style=wx.TE_LEFT, pos=(20, 75))
        self.text_top03 = wx.StaticText(self, 0, u"Lasso_PLS的回归系数:", style=wx.TE_LEFT, pos=(300, 75))

        self.textContents01 = wx.TextCtrl(self, style=wx.TE_CENTER, pos=(20, 35), size=(430, 30))
        self.textContents02 = wx.TextCtrl(self, style=wx.TE_MULTILINE|wx.HSCROLL, pos=(20, 95),size=(150, 200))
        self.textContents03 = wx.TextCtrl(self, style=wx.TE_MULTILINE|wx.HSCROLL, pos=(300, 95), size=(150, 200))
        xishu01 = wx.Button(self, label="原始系数", pos=(190, 120))
        xishu02 = wx.Button(self, label="特征系数", pos=(190, 170))
        xishu03 = wx.Button(self, label="特征选择", pos=(190, 220))

        # 定义按钮事件
        self.Bind(wx.EVT_BUTTON, self.On_xishu01, xishu01)
        self.Bind(wx.EVT_BUTTON, self.On_xishu02, xishu02)
        self.Bind(wx.EVT_BUTTON, self.On_xishu03, xishu03)

    # 事件
    def On_xishu01(self, event):
        self.textContents02.Clear()
        RR, RMSE, SSE, SSR, xish01, xish, m = ModelTCM_LassoPLS.model_Result()
        xish = str(xish)
        assist = "=========="
        self.textContents02.AppendText(assist + '\n' + u"★原始回归系数： " + '\n' + xish + '\n' + assist + '\n')
        event.Skip()

    def On_xishu02(self, event):
        self.textContents03.Clear()
        RR, RMSE, SSE, SSR, xish01, xish, m = ModelTCM_LassoPLS.model_Result()
        xish01 = str(xish01)
        assist = "=========="
        self.textContents03.AppendText(assist + '\n' + u"★特征回归系数： " + '\n' + xish01 + '\n' + assist + '\n')
        event.Skip()

    def On_xishu03(self, event):
        self.textContents01.Clear()
        RR, RMSE, SSE, SSR, xish01, xish, m = ModelTCM_LassoPLS.model_Result() # xish01,sish = 9*1
        # xish01 = str(xish01)
        # index = mat(zeros((m))).T
        for i in range(m):
            if xish01[i] != 0:
                # index[i] = i
                i = str(i+1)
                self.textContents01.AppendText(u"自变量： " + 'x' + i + u'；')
        event.Skip()

'''
    Page3.实验结果--选项卡three
        1)获取改进算法的R^2；
        2）获取改进算法的RMSE--均方根误差；
        3）画图，即图形可视化
'''
class Page3(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent)
        # 界面布局
        self.text_top01 = wx.StaticText(self, 0, u"Lasso_PLS：", style=wx.TE_LEFT, pos=(20, 12))
        # self.text_top02 = wx.StaticText(self, 0, u"可视化图行：", style=wx.TE_LEFT, pos=(200, 12))
        self.textContents001 = wx.TextCtrl(self, style=wx.TE_LEFT|wx.TE_MULTILINE, pos=(20, 35), size=(435, 220))
        # self.textContents002 = wx.TextCtrl(self, style=wx.TE_CENTER, pos=(200, 35), size=(250, 220))
        modelResult = wx.Button(self, label="模型结果", pos=(120, 270))
        imageResult = wx.Button(self, label="生成图", pos=(260, 270))
        # 添加事件
        self.Bind(wx.EVT_BUTTON, self.On_modelResult, modelResult)
        self.Bind(wx.EVT_BUTTON, self.On_imageResult, imageResult)

    # 事件
    def On_modelResult(self, event):
        self.textContents001.Clear()
        RR, RMSE, SSE, SSR, xish01, xish, m = ModelTCM_LassoPLS.model_Result()
        RR = str(RR); RMSE = str(RMSE); SSE = str(SSE); SSR = str(SSR)
        assist = "======================="

        self.textContents001.AppendText(u"=========结果摘要=========" + '\n' + u"1.R的平方： " + RR + '\n'+ '*******************' +
                                        '\n' + u"2.均方根误差RMSE： "+ RMSE + '\n'+'*******************' + '\n'
                                        + u"3.残差平方和SSE： "  + SSE +'\n' + '*******************' +'\n'
                                        + u"4.回归平方和SSR： "  + SSR + '\n' + '*******************' +'\n')
        # 剔除的自变量（或特征）
        self.textContents001.AppendText('*******************' + '\n' +u'☆☆剔除的自变量（特征）为：' + '\n')
        for i in range(m):
            if xish01[i] == 0:
                # index[i] = i
                i = str(i+1)
                self.textContents001.AppendText(u"    自变量： " + 'x' + i + u'；')
        self.textContents001.AppendText('\n' + assist)
        event.Skip()

    def On_imageResult(self, event):
        # self.textContents001.Clear()
        ModelTCM_LassoPLS.Image_lassoPLS()
        event.Skip()



class Page4(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent)

def main():
    app = wx.App(False)
    frame = wx.Frame(None, title="参数设置", size=(500, 400))
    frame.SetBackgroundColour('#F8F8FF')
    frameText = frame.CreateStatusBar()
    frameText.SetStatusText(u"☛中医药数据分析：@Aliked(2018-07-09)")
    #固定窗口大小
    frame.SetMinSize((500, 400))
    frame.SetMaxSize((500, 400))
    nbook = wx.Notebook(frame)
    #选项卡
    nbook.AddPage(Page1(nbook), u" 基本信息 ")
    nbook.AddPage(Page2(nbook), u" 特征分析 ")
    nbook.AddPage(Page3(nbook), u" 实验结果 ")
    nbook.AddPage(Page4(nbook), u" 其它信息 ")
    frame.Show()
    frame.Center()
    app.MainLoop()

#主窗口
if __name__ == '__main__':
    main()