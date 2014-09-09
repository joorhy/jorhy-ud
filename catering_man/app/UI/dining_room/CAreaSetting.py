#!/usr/bin/env python
# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview
from wx.dataview import DataViewColumn

###########################################################################
## Class CAreaSetting
###########################################################################

class CAreaSetting ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"区域设置", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.CAPTION|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.Size( -1,-1 ), wx.Size( -1,-1 ) )
        
        m_sizer = wx.BoxSizer( wx.VERTICAL )
        
        m_topSizer = wx.BoxSizer( wx.VERTICAL )
        
        self.m_dataViewList = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_dataViewList.SetMinSize( wx.Size( 600,300 ) )
        
        self.m_dataViewListLine = self.m_dataViewList.AppendTextColumn( u"行号" ) 
        self.m_dataViewListCode = self.m_dataViewList.AppendTextColumn( u"编码" ) 
        self.m_dataViewListName = self.m_dataViewList.AppendTextColumn( u"区域名称" ) 
        m_topSizer.Add( self.m_dataViewList, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        m_sizer.Add( m_topSizer, 1, wx.EXPAND, 5 )
        
        m_bottomSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_btnNew = wx.Button( self, wx.ID_ANY, u"新增", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_bottomSizer.Add( self.m_btnNew, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.m_btnDelete = wx.Button( self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_bottomSizer.Add( self.m_btnDelete, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        
        m_bottomSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_btnRefresh = wx.Button( self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_bottomSizer.Add( self.m_btnRefresh, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.m_btnSave = wx.Button( self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_bottomSizer.Add( self.m_btnSave, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.m_btnExit = wx.Button( self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_bottomSizer.Add( self.m_btnExit, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        
        m_sizer.Add( m_bottomSizer, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( m_sizer )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_btnNew.Bind( wx.EVT_BUTTON, self.OnBtnNew )
        self.m_btnDelete.Bind( wx.EVT_BUTTON, self.OnBtnDelete )
        self.m_btnRefresh.Bind( wx.EVT_BUTTON, self.OnBtnRefresh )
        self.m_btnSave.Bind( wx.EVT_BUTTON, self.OnBtnSave )
        self.m_btnExit.Bind( wx.EVT_BUTTON, self.OnBtnExit )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def OnBtnNew( self, event ):
        event.Skip()
        valuse = [1, "", ""]
        self.m_dataViewList.InsertItem(0, valuse)
    
    def OnBtnDelete( self, event ):
        event.Skip()
    
    def OnBtnRefresh( self, event ):
        event.Skip()
    
    def OnBtnSave( self, event ):
        event.Skip()
    
    def OnBtnExit( self, event ):
        event.Skip()
        self.Close()


if __name__ == '__main__':
    app = wx.PySimpleApp()
    dlg = CAreaSetting(None)
    dlg.Show()
    #dlg.Center()
    app.MainLoop()
