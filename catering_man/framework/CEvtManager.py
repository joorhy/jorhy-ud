# -*- coding: utf-8 -*- 
#!/usr/bin/env python

import wx
from framework.CSingleton import CSingleton
from framework.CEvent import CEvent

evt_map = {}

class CEvtManager(CSingleton):
    @staticmethod
    def AddListenner(win, evt_id, func):
        win.Connect(-1, -1, evt_id, func)    
        if evt_map.has_key(evt_id):
            evt_map[evt_id].append(win)
        else:
            list_tmp = []
            list_tmp.append(win)
            evt_map_tmp = {evt_id:list_tmp}
            evt_map.update(evt_map_tmp)
            
    @staticmethod
    def RemoveListenner(win, evt_id, func):
        pass
    
    @staticmethod
    def DispatchEvent(evt_id, evt_data = ""):
        if evt_map.has_key(evt_id):
            for item in evt_map[evt_id]:
                wx.PostEvent(item, CEvent(evt_id, evt_data))
        
