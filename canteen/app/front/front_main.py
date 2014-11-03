#_*_ encoding=utf-8 _*_
#!/usr/bin/env python
from app.app_manager import AppManager
from app.front.config import CONFIG

import wx

CONFIG.useTemp = True

app = wx.App()
AppManager.get_instance().initialize()
AppManager.get_instance().switch_to_application('Login', 'front')
app.MainLoop()