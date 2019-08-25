# coding=utf-8
import wx
import os
from numpy import *
# import wx.grid
import ActionTCM_LassoPLS
import warn_onModel

"""
    模型主窗口
"""
class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        self.dirname = ''
        wx.Frame.__init__(self, parent, id, u'中医药数据分析', size=(600, 500))

        # 创建状态栏
        self.status = self.CreateStatusBar()
        self.statusMess = self.status.SetStatusText("@Aliked(2018-07-09)")
        #self.Bind(wx.EVT_HELP, self.OnOpen, self.statusMess)

        # 创建菜单
        menuBar = wx.MenuBar()
        # 创建菜单-File
        filemenu = wx.Menu()
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open")
        filemenu.AppendSeparator() # 菜单下划线
        menuSave = filemenu.Append(wx.ID_SAVE, "&Save")
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT, "&Exit")
        filemenu.AppendSeparator()
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About")
        menuBar.Append(filemenu, " &File ")

        #创建菜单-Edit(未完待续)
        editmenu = wx.Menu()
        editmenu.Append(wx.NewId(), "&Copy")
        editmenu.AppendSeparator()
        editmenu.Append(wx.NewId(), "&Cut")
        editmenu.AppendSeparator()
        editmenu.Append(wx.NewId(), "&Paste")
        editmenu.AppendSeparator()
        editmenu.Append(wx.NewId(), "&Reset")
        menuBar.Append(editmenu, " &Edit ")

        # 创建菜单-Model
        modelmenu = wx.Menu()
        menuModel = modelmenu.Append(wx.NewId(), "&PLS") #待续
        modelmenu.AppendSeparator()
        menuModel = modelmenu.Append(wx.NewId(), "&Lasso_PLS")
        menuBar.Append(modelmenu, " &Model ")

        # 创建菜单-Help
        helpmenu = wx.Menu()
        #menuHelp = helpmenu.Append(wx.NewId(), "")  # 待续
        Helpmenu = menuBar.Append(helpmenu, " &Help ")
        # 菜单下划线
        # helpmenu.AppendSeparator()

        # 事件：Events.
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnSave, menuSave)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        #self.Bind(wx.Menu, self.on_Help, Helpmenu)
        self.SetMenuBar(menuBar)

        # 创建面板
        panel = wx.Panel(self)
        # 创建浏览，重置，建模按钮
        self.bt_Browse = wx.Button(panel, label='浏览')
        self.bt_Reset = wx.Button(panel, label='重置')
        self.bt_Model = wx.Button(panel , label ='建模')

        # 创建文本，左对齐，注意这里style=wx.TE_LEFT，不是wx.ALIGN_LEFT ，表示控件中的输入光标是靠左对齐。
        #self.st_tips = wx.StaticText(panel, 0, u"请输入文件路径", style=wx.TE_LEFT)
        self.st_tips = wx.StaticText(panel, 0, u"文件路径:", style=wx.TE_LEFT)
        self.text_filename = wx.TextCtrl(panel, style=wx.TE_LEFT)
        #self.st_tips2.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        #self.st_tips2.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL))

        # 创建文本内容框，多行，垂直滚动条
        self.text_contents = wx.TextCtrl(panel, -1, u"请导入实验数据(仅支持txt文件)", style=wx.TE_MULTILINE | wx.HSCROLL)

        # 添加容器，容器中控件按横向并排排列
        bsizer_top = wx.BoxSizer(wx.VERTICAL)
        # 添加容器，容器中控件按纵向并排排列
        bsizer_File = wx.BoxSizer(wx.HORIZONTAL)
        bsizer_bottom = wx.BoxSizer(wx.HORIZONTAL)

        #bsizer_message = wx.BoxSizer(wx.HORIZONTAL)
        # 在容器中添加st_tips控件，proportion=0 代表当容器大小变化时，st_tips控件的大小不变
        # flag = wx.EXPAND|wx.ALL中，wx.ALL代表在st_tips控件四周都增加宽度为x的空白，x取border参数的值，本例是border=5
        # wx.EXPAND代表st_tips控件占满可用空间。
        #bsizer_top.Add(self.st_tips, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
        # proportion=1 代表当容器大小变化时，st_tips2控件的大小变化，变化速度为1
        bsizer_File.Add(self.st_tips, proportion=0, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, border=5)
        # proportion=2 代表当容器大小变化时，text_filename控件的大小变化，变化速度为2
        bsizer_File.Add(self.text_filename, proportion=4, flag=wx.EXPAND | wx.ALL, border=5)
        bsizer_File.Add(self.bt_Browse, proportion=1, flag=wx.ALL, border=5)
        bsizer_File.Add(self.bt_Reset, proportion=1, flag=wx.ALL, border=5)
        bsizer_File.Add(self.bt_Model, proportion=1, flag=wx.ALL, border=5)
        bsizer_bottom.Add(self.text_contents, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
        #bsizer_message.Add(self.text_Message, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)

        # wx.VERTICAL 横向分割
        bsizer_all = wx.BoxSizer(wx.VERTICAL)

        # 添加顶部sizer，proportion=0 代表bsizer_top大小不可变化
        bsizer_all.Add(bsizer_top, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
        bsizer_all.Add(bsizer_File, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)

       # 添加顶部sizer，proportion=1 代表bsizer_bottom大小变化
        bsizer_all.Add(bsizer_bottom, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
        self.Bind(wx.EVT_BUTTON, self.OnOpen, self.bt_Browse)
        self.Bind(wx.EVT_BUTTON, self.on_Reset, self.bt_Reset)
        self.Bind(wx.EVT_BUTTON, self.on_Model, self.bt_Model)
        # self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)
        panel.SetSizer(bsizer_all)

    # 事件
    def on_Reset(self, event):
        self.text_filename.Clear()
        self.text_contents.Clear()
        event.Skip()

    #未完待补充
    def OnSave(self, event):
        filesFilter = "文本文档(*.txt)|*.txt"
        fileDialog = wx.FileDialog(self, message="保存文件", wildcard=filesFilter, style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        dialogResult = fileDialog.ShowModal()
        if dialogResult != wx.ID_OK:
            return
        path = fileDialog.GetPath()
        # fileDialog.GetFilename()  # 获得默认的文件名字
        self.assist = "==================================="
        self.text_contents.AppendText(self.assist + '\n' + u"★★★Successful Save: " + path + '\n' + self.assist)
        fileDialog.GetDirectory()  # 返回默认的文件夹
        #fr = write()
        # filesFilter = "文本文档(*.txt)|*.txt"
        # fileDialog = wx.FileDialog(self, message="选择单个文件", wildcard=filesFilter, style=wx.FD_OPEN)
        # self.filename = fileDialog.GetFilename()
        #file = open(self.filename.GetValue(), 'w')
        # file.write(self.text_contents.GetValue().encode('utf-8'))
        # fileDialog.ShowModal()
        # file.close()
        event.Skip()
        fileDialog.Destroy()

    def OnExit(self,event):
        ''' 退出平台 '''
        self.Close(True)

    def OnAbout(self, event):
        ''' 相关信息 '''
        dlg = wx.MessageDialog(self, u" Author:黄灿奕", "About Sample Editor", wx.OK)
        dlg.ShowModal()
        event.Skip()
        dlg.Destroy()  # 销毁

    def OnOpen(self, event):
        ''' 打开文件 '''
        filesFilter = "文本文档(*.txt)|*.txt"
        fileDialog = wx.FileDialog(self, message="打开文件", wildcard=filesFilter, style=wx.FD_OPEN)
        if fileDialog.ShowModal() != wx.ID_OK:
            return
        path = fileDialog.GetPath() # 返回选择的文件的全路径
        self.text_filename.SetLabel(path)
        self.filename = fileDialog.GetFilename() # 获得默认的文件名字
        self.dirname = fileDialog.GetDirectory() # 返回默认的文件夹
        f = open(os.path.join(self.dirname, self.filename), 'r')
        self.assist =  "========================================"
        self.contents = self.text_contents.SetValue(self.assist + '\n' + f.read() + '\n')
        self.text_contents.AppendText(self.assist + '\n' +u"★★★Successful Input: " + path + '\n' + self.assist)
        f.close()
        event.Skip()
        fileDialog.Destroy()

    def on_Model(self, event):
        ''' 模型建立 '''
        #判断是否可以建模--IsSingleLine()
        # if self.text_contents:
        #     return warn_onModel.main()
        #     #return ActionTCM_LassoPLS.main()
        #warn_onModel.main()
        # if self.contents =='':
        #     return warn_onModel.main()
        ActionTCM_LassoPLS.main()
        #warn_onModel.main()
        event.Skip()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MyFrame(parent=None, id=-1)
    frame.SetBackgroundColour('#F8F8FF')
    frame.Show()
    frame.Center()
    app.MainLoop()