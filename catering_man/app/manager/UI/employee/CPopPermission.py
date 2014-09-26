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

###########################################################################
## Class CPopPermission
###########################################################################

class CPopPermission ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"权限设置", pos = wx.DefaultPosition, size = wx.Size( 600,470 ), style = wx.CAPTION )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        m_sizer = wx.BoxSizer( wx.VERTICAL )
        
        m_topSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        m_topSizer.SetMinSize( wx.Size( 600,400 ) ) 
        m_leftSizer = wx.BoxSizer( wx.VERTICAL )
        
        m_leftSizer.SetMinSize( wx.Size( 200,400 ) ) 
        self.m_treeCtrl = wx.TreeCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
        self.m_treeCtrl.SetMinSize( wx.Size( -1,400 ) )
        
        m_leftSizer.Add( self.m_treeCtrl, 0, wx.EXPAND, 5 )
        
        
        m_topSizer.Add( m_leftSizer, 1, 0, 5 )
        
        m_rightSizer = wx.BoxSizer( wx.VERTICAL )
        
        m_rightSizer.SetMinSize( wx.Size( 400,400 ) ) 
        self.m_dataViewListCtrl = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_dataViewListCtrl.SetMinSize( wx.Size( -1,400 ) )
        
        self.m_dataViewLine = self.m_dataViewListCtrl.AppendTextColumn( u"行号" ) 
        self.m_dataViewType = self.m_dataViewListCtrl.AppendTextColumn( u"类别" ) 
        self.m_dataViewPermission = self.m_dataViewListCtrl.AppendTextColumn( u"权限" ) 
        self.m_dataViewState = self.m_dataViewListCtrl.AppendToggleColumn( u"状态" ) 
        m_rightSizer.Add( self.m_dataViewListCtrl, 0, wx.EXPAND|wx.LEFT, 5 )
        
        
        m_topSizer.Add( m_rightSizer, 1, 0, 5 )
        
        
        m_sizer.Add( m_topSizer, 1, wx.EXPAND, 5 )
        
        m_bottomSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        m_bottomSizer.SetMinSize( wx.Size( 600,50 ) ) 
        self.m_topPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_topPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        m_bottomSizer.Add( self.m_topPanel, 1, wx.EXPAND, 5 )
        
        self.m_btnSave = wx.Button( self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_bottomSizer.Add( self.m_btnSave, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_btnExit = wx.Button( self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_bottomSizer.Add( self.m_btnExit, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_sizer.Add( m_bottomSizer, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( m_sizer )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_btnSave.Bind( wx.EVT_BUTTON, self.OnBtnSave )
        self.m_btnExit.Bind( wx.EVT_BUTTON, self.OnBtnExit )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def OnBtnSave( self, event ):
        event.Skip()
    
    def OnBtnExit( self, event ):
        event.Skip()
        self.Close()
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    dlg = CPopPermission(None)
    dlg.Show()
    app.MainLoop()
