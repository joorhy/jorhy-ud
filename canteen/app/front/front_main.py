#_*_ encoding=utf-8 _*_
#!/usr/bin/env python
from app.app_manager import AppManager
from app.front.config import CONFIG

import wx

CONFIG.useTemp = True

app = wx.App()
AppManager.initialize()
AppManager.switch_to_application('Login', 'front')
app.MainLoop()