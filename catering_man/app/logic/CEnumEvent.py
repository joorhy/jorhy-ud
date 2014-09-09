# -*- coding: utf-8 -*- 
#!/usr/bin/env python

import wx
from framework.CSingleton import CSingleton

class CEnumEvent(CSingleton):  
    EVT_LOGIN = wx.NewId()

    