#_*_ encoding=utf-8 _*_
#!/usr/bin/env python
import wx
from app.CAppManager import CAppManager


if __name__ == '__main__':
    app = wx.PySimpleApp()
    CAppManager.Initailize()
    CAppManager.SwitchToApplication('Login')
    app.MainLoop()
