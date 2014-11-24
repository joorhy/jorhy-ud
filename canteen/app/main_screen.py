# -*- coding: utf-8 -*- 
#!/usr/bin/env python

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from app.home_logic import CtrlHomePage
    
###########################################################################
## Class MainScreen
###########################################################################


class MainScreen (wx.Frame):
    
    panel = None
    
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"采购管理", pos=wx.DefaultPosition,
                          size=wx.DefaultSize, style=wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX)
        
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.Centre(wx.BOTH)
        self.SetMinSize(wx.Size(800, 600))
        
        # Connect Events
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.Bind(wx.EVT_CLOSE, self.on_exit)
    
    def __del__(self):
        pass
    
    def set_panel(self, panel):
        self.panel = panel
    
    # Virtual event handlers, override them in your derived class
    def on_size(self, event):
        event.Skip()
        x, y = self.GetClientSize()
        CtrlHomePage.get_instance().set_screen_size(x, y)
        if self.panel is not None:
            self.panel.SetSize(wx.Size(x, y))
        
    def on_exit(self, event):
        event.Skip()
        self.Destroy()
