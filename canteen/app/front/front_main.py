#_*_ encoding=utf-8 _*_
#!/usr/bin/env python
from app.app_manager import AppManager
from app.front.config import CONFIG
from service.http_json.http_service import HttpService

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

AppManager.get_instance().initialize()
AppManager.get_instance().switch_to_application('Login', 'front')
app.MainLoop()