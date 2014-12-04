#_*_ encoding=utf-8 _*_
#!/usr/bin/env python
from app.front.logic.ctrl import *
from app.app_manager import AppManager
from app.front.config import CONFIG
from service.http_json.http_service import HttpService
from framework.core import Log

import wx
import sys
import json

CONFIG.useTemp = False

app = wx.App()

if not CONFIG.useTemp:
    config = open(sys.path[0] + "\\..\\front_config.json", "r")
    content = config.read()
    config_json = json.loads(content)
    HttpService.get_instance().initialize(config_json['svr_address'], config_json['svr_port'])

try:
    CtrlTableInfo.get_instance().get_table_items()
    CtrlDishesInfo.get_instance().get_dishes_items()
except Exception, ex:
    print Exception, ":", ex

Log.initialize("manager.log")

AppManager.get_instance().initialize('front')
AppManager.get_instance().switch_to_application('Login', 'front')
app.MainLoop()