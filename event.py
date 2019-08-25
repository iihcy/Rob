#coding:utf-8

import wx, os
import warn_onModel
import ActionTCM_LassoPLS

def on_Reset(self, event):
    self.text_filename.Clear()
    self.text_contents.Clear()

# 未完待补充
def OnSave(self, event):
    filesFilter = "文本文档(*.txt)|*.txt"
    fileDialog = wx.FileDialog(self, message="保存文件", wildcard=filesFilter, style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
    dialogResult = fileDialog.ShowModal()
    if dialogResult != wx.ID_OK:
        return
    path = fileDialog.GetPath()
    # fileDialog.GetFilename()  # 获得默认的文件名字
    self.text_contents.SetLabel(path)
    fileDialog.GetDirectory()  # 返回默认的文件夹
    # fr = write()
    # filesFilter = "文本文档(*.txt)|*.txt"
    # fileDialog = wx.FileDialog(self, message="选择单个文件", wildcard=filesFilter, style=wx.FD_OPEN)
    # self.filename = fileDialog.GetFilename()
    file = open(self.filename.GetValue(), 'w')
    file.write(self.text_contents.GetValue().encode('utf-8'))
    fileDialog.ShowModal()
    file.close()
    fileDialog.Destroy()


def OnExit(self, event):
    ''' 退出平台 '''
    self.Close(True)


def OnAbout(self, event):
    ''' 相关信息 '''
    dlg = wx.MessageDialog(self, u" Author:黄灿奕", "About Sample Editor", wx.OK)
    dlg.ShowModal()
    dlg.Destroy()  # 销毁


def OnOpen(self, event):
    ''' 打开文件 '''
    filesFilter = "文本文档(*.txt)|*.txt"
    fileDialog = wx.FileDialog(self, message="打开文件", wildcard=filesFilter, style=wx.FD_OPEN)
    if fileDialog.ShowModal() != wx.ID_OK:
        return
    path = fileDialog.GetPath()  # 返回选择的文件的全路径
    self.name = self.text_filename.SetLabel(path)
    self.filename = fileDialog.GetFilename()  # 获得默认的文件名字
    self.dirname = fileDialog.GetDirectory()  # 返回默认的文件夹
    f = open(os.path.join(self.dirname, self.filename), 'r')
    self.assist = "========================================"
    self.contents = self.text_contents.SetValue(self.assist + '\n' + f.read() + '\n')
    self.text_contents.AppendText(self.assist + '\n' + u"★★★Successful Input: " + path + '\n' + self.assist)
    f.close()
    fileDialog.Destroy()


def on_Model(self, event):
    ''' 模型建立 '''
    # dlg = wx.MessageDialog(None, u"提示：是否继续操作！", u"警告提示", wx.YES_NO | wx.ICON_QUESTION)
    # if dlg.ShowModal() != wx.ID_YES:
    #     self.Close(False)
    # dialog = wx.Dialog(self)
    # self.rec = dialog.ShowModal()
    # dlg.Destroy()
    if self.name == "" or self.contents == "":
        warn_onModel.main()
    ActionTCM_LassoPLS.main()

