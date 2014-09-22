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
## Class CWgtPermission
###########################################################################

class CWgtPermission ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"权限管理", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        m_sizer = wx.BoxSizer( wx.VERTICAL )
        
        m_topSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        m_topSizer.SetMinSize( wx.Size( 800,50 ) ) 
        self.m_btnNew = wx.Button( self, wx.ID_ANY, u"新增", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnNew.SetMinSize( wx.Size( 50,50 ) )
        
        m_topSizer.Add( self.m_btnNew, 0, wx.EXPAND, 5 )
        
        self.m_btnModify = wx.Button( self, wx.ID_ANY, u"修改", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnModify.SetMinSize( wx.Size( 50,50 ) )
        
        m_topSizer.Add( self.m_btnModify, 0, 0, 5 )
        
        self.m_btnDelete = wx.Button( self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnDelete.SetMinSize( wx.Size( 50,50 ) )
        
        m_topSizer.Add( self.m_btnDelete, 0, 0, 5 )
        
        self.m_btnRefresh = wx.Button( self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnRefresh.SetMinSize( wx.Size( 50,50 ) )
        
        m_topSizer.Add( self.m_btnRefresh, 0, 0, 5 )
        
        self.m_btnExit = wx.Button( self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnExit.SetMinSize( wx.Size( 50,50 ) )
        
        m_topSizer.Add( self.m_btnExit, 0, 0, 5 )
        
        self.m_topPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_topPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        m_topSizer.Add( self.m_topPanel, 1, wx.EXPAND, 5 )
        
        
        m_sizer.Add( m_topSizer, 1, wx.EXPAND, 5 )
        
        m_bottomSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        m_bottomSizer.SetMinSize( wx.Size( 800,550 ) ) 
        m_leftSizer = wx.BoxSizer( wx.VERTICAL )
        
        m_leftSizer.SetMinSize( wx.Size( 200,550 ) ) 
        self.m_treeCtrl = wx.TreeCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
        self.m_treeCtrl.SetMinSize( wx.Size( -1,600 ) )
        
        m_leftSizer.Add( self.m_treeCtrl, 0, wx.EXPAND, 5 )
        
        
        m_bottomSizer.Add( m_leftSizer, 1, 0, 5 )
        
        m_rightSizer = wx.BoxSizer( wx.VERTICAL )
        
        m_rightSizer.SetMinSize( wx.Size( 600,550 ) ) 
        self.m_dataViewListCtrl = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_dataViewListCtrl.SetMinSize( wx.Size( -1,600 ) )
        
        self.m_dataViewLine = self.m_dataViewListCtrl.AppendTextColumn( u"行号" ) 
        self.m_dataViewType = self.m_dataViewListCtrl.AppendTextColumn( u"类型" ) 
        self.m_dataViewCode = self.m_dataViewListCtrl.AppendTextColumn( u"编码" ) 
        self.m_dataViewName = self.m_dataViewListCtrl.AppendTextColumn( u"名称" ) 
        self.m_dataViewNote = self.m_dataViewListCtrl.AppendTextColumn( u"备注" ) 
        m_rightSizer.Add( self.m_dataViewListCtrl, 0, wx.EXPAND|wx.LEFT, 5 )
        
        
        m_bottomSizer.Add( m_rightSizer, 1, 0, 5 )
        
        
        m_sizer.Add( m_bottomSizer, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( m_sizer )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_btnNew.Bind( wx.EVT_BUTTON, self.OnBtnNew )
        self.m_btnModify.Bind( wx.EVT_BUTTON, self.OnBtnModify )
        self.m_btnDelete.Bind( wx.EVT_BUTTON, self.OnBtnDelete )
        self.m_btnRefresh.Bind( wx.EVT_BUTTON, self.OnBtnRefresh )
        self.m_btnExit.Bind( wx.EVT_BUTTON, self.OnBtnExit )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def OnBtnNew( self, event ):
        event.Skip()
    
    def OnBtnModify( self, event ):
        event.Skip()
    
    def OnBtnDelete( self, event ):
        event.Skip()
    
    def OnBtnRefresh( self, event ):
        event.Skip()
    
    def OnBtnExit( self, event ):
        event.Skip()
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = CWgtPermission(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()