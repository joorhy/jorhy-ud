#_*_ encoding=utf-8 _*_
#!/usr/bin/env python
import wx
from app.app_manager import AppManager

app = wx.App()
AppManager.initialize()
AppManager.switch_to_application('Login', 'manager')
app.MainLoop()