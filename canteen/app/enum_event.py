# -*- coding: utf-8 -*- 
#!/usr/bin/env python

import wx
from framework.core import Singleton


class EnumEvent(Singleton):
    # Login event  
    EVT_LOGIN = wx.NewId()
    # Dining room refresh event
    EVT_DINING_ROOM_REFRESH = wx.NewId()
    # Dishes publish refresh event
    EVT_DISHES_PUBLISH_REFRESH = wx.NewId()
    # Employee manager refresh event
    EVT_EMPLOYEE_REFRESH = wx.NewId()
    # Employee permission refresh event
    EVT_PERMISSION_REFRESH = wx.NewId()
    # Printer scheme refresh event
    EVT_PRINTER_SCHEME_REFRESH = wx.NewId()
    # Business info refresh event
    EVT_BUSINESS_INFO_REFRESH = wx.NewId()
    # Sales info refresh event
    EVT_SALES_INFO_REFRESH = wx.NewId()
    # Billboard info refresh event
    EVT_BILLBOARD_INFO_REFRESH = wx.NewId()
    # Front page refresh event
    EVT_FRONT_PAGE_REFRESH = wx.NewId()
    # Order dishes items refresh event
    EVT_ORDER_DISHES_ITEMS_REFRESH = wx.NewId()
    # checkout info refresh event
    EVT_CHECKOUT_INFO_REFRESH = wx.NewId()