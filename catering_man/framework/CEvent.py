# -*- coding: utf-8 -*- 
#!/usr/bin/env python
import wx
    
class CEvent(wx.PyEvent):
    def __init__(self, evt_id, evt_data):
        wx.PyEvent.__init__(self)
        self.SetEventType(evt_id)
        self.data = evt_data
