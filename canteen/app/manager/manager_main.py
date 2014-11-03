#_*_ encoding=utf-8 _*_
#!/usr/bin/env python
from app.app_manager import AppManager
from service.data_base.sql_manager import SqlManager


import wx
import sys
import json

app = wx.App()

config = open(sys.path[0] + "\\..\\config.json", "r")
content = config.read()
config_json = json.loads(content)
SqlManager.get_instance().initialize(config_json['db_address'], config_json['db_user'], config_json["db_password"])

from app.manager.logic.ctrl import CtrlManagerLogin
CtrlManagerLogin.get_instance().initialize(config_json['user'], config_json["password"])

AppManager.get_instance().initialize()
AppManager.get_instance().switch_to_application('Login', 'manager')
app.MainLoop()