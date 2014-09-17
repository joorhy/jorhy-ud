# -*- coding: utf-8 -*- 
#!/usr/bin/env python

import wx
from framework.CSingleton import CSingleton

class CEnumEvent(CSingleton):
    # Login event  
    EVT_LOGIN = wx.NewId()
    # Dining room refresh event
    EVT_DINING_ROOM_REFRESH = wx.NewId()
    # Dishes publish refresh event
    EVT_DISHES_PUBLISH_REFRESH = wx.NewId()

    