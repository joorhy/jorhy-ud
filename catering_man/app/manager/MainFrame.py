#_*_ encoding=utf-8 _*_
#!/usr/bin/env python
import wx
from app.manager.AppManager import AppManager


if __name__ == '__main__':
    app = wx.PySimpleApp()
    AppManager.Initailize()
    AppManager.SwitchToApplication('Login')
    app.MainLoop()
