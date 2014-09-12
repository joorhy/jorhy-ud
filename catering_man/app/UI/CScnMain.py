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
from app.logic.desktop.CDataDeskTop import CDataDeskTop
    
###########################################################################
## Class CProcure
###########################################################################

class CScnMain ( wx.Frame ):
    
    panel = None
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"采购管理", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        
        self.Centre( wx.BOTH )
        
        self.SetMinSize( wx.Size(800,600) )
        
        # Connect Events
        self.Bind( wx.EVT_SIZE, self.OnSize )   
        self.Bind( wx.EVT_CLOSE, self.OnExit )
    
    def __del__( self ):
        pass
    
    def SetPanel(self, panel):
        self.panel = panel
    
    # Virtual event handlers, overide them in your derived class
    def OnSize( self, event ):
        event.Skip()
        x, y = self.GetClientSize()
        CDataDeskTop.SetFrameSize(x, y)
        if self.panel != None:
            self.panel.SetSize(wx.Size(x, y))
        
    def OnExit( self, event ):
        event.Skip()
        self.Destroy();
