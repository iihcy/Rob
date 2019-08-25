#coding:utf-8
import wx
import wx.grid
import os
import ActionTCM_LassoPLS

"""
    Util工具：弹出窗口
"""
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u"警告",size=(350,200))
        self.pan = wx.Panel(self)
        content = u"Warning: Whether to import test data!"
        self.warn = wx.StaticText(self.pan, 0, content, style=wx.TE_CENTER, pos=(50,32))
        self.warn.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.NORMAL))
        button = wx.Button(self.pan, label='Yes', pos=(120,100))
        self.Bind(wx.EVT_BUTTON, self.onButton, button)

    #警告
    def onButton(self,event):
        #self.Close()
        #ActionTCM_LassoPLS.main()
        event.Skip()
        #self.Close()
        self.Destroy()


def main():
    app = wx.PySimpleApp()
    frame = MyFrame()
    frame.Show()
    frame.Center()
    app.MainLoop()

if __name__ == '__main__':
    main()