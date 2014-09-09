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
import wx.dataview
from app.CAppManager import CAppManager
from app.logic.desktop.CDataMainFrame import CDataMainFrame

###########################################################################
## Class CDiningTable
###########################################################################

class CDiningTable ( wx.Panel ):
    
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )
        
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
        
        self.m_btnBatAdd = wx.Button( self, wx.ID_ANY, u"批量增加", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnBatAdd.SetFont( wx.Font( 8, 70, 90, 90, False, wx.EmptyString ) )
        self.m_btnBatAdd.SetMinSize( wx.Size( 50,50 ) )
        
        m_topSizer.Add( self.m_btnBatAdd, 0, 0, 5 )
        
        self.m_btnTableType = wx.Button( self, wx.ID_ANY, u"桌类", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnTableType.SetMinSize( wx.Size( 50,50 ) )
        
        m_topSizer.Add( self.m_btnTableType, 0, 0, 5 )
        
        self.m_btnArea = wx.Button( self, wx.ID_ANY, u"区域", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnArea.SetMinSize( wx.Size( 50,50 ) )
        
        m_topSizer.Add( self.m_btnArea, 0, 0, 5 )
        
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
        
        self.m_dataViewColunmNum = self.m_dataViewListCtrl.AppendTextColumn( u"行号" ) 
        self.m_dataViewTableNum = self.m_dataViewListCtrl.AppendTextColumn( u"桌号" ) 
        self.m_dataViewTableName = self.m_dataViewListCtrl.AppendTextColumn( u"餐桌名" ) 
        self.m_dataViewType = self.m_dataViewListCtrl.AppendTextColumn( u"类型" ) 
        self.m_dataViewArea = self.m_dataViewListCtrl.AppendTextColumn( u"区域" ) 
        self.m_dataViewCustomerNum = self.m_dataViewListCtrl.AppendTextColumn( u"人数" ) 
        m_rightSizer.Add( self.m_dataViewListCtrl, 0, wx.EXPAND|wx.LEFT, 5 )
        
        
        m_bottomSizer.Add( m_rightSizer, 1, 0, 5 )
        
        
        m_sizer.Add( m_bottomSizer, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( m_sizer )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.Bind( wx.EVT_SIZE, self.OnSize )
        
        self.m_btnNew.Bind( wx.EVT_BUTTON, self.OnNew )
        self.m_btnModify.Bind( wx.EVT_BUTTON, self.OnModify )
        self.m_btnDelete.Bind( wx.EVT_BUTTON, self.OnDelete )
        self.m_btnBatAdd.Bind( wx.EVT_BUTTON, self.OnBatAdd )
        self.m_btnTableType.Bind( wx.EVT_BUTTON, self.OnTableType )
        self.m_btnArea.Bind( wx.EVT_BUTTON, self.OnAreaSetting )
        self.m_btnRefresh.Bind( wx.EVT_BUTTON, self.OnRefresh )
        self.m_btnExit.Bind( wx.EVT_BUTTON, self.OnExit )
    
    def __del__( self ):
        pass
    
    def Initailize(self):
        x, y = CDataMainFrame.GetFrameSize()
        self.SetSize(wx.Size(x, y))

    def Uninitailize(self):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def OnSize( self, event ):
        event.Skip()
        x, y = self.GetSize()

        self.m_btnNew.SetMaxSize(wx.Size( 50,50 ))
        self.m_btnModify.SetMaxSize(wx.Size( 50,50 ))
        self.m_btnDelete.SetMaxSize(wx.Size( 50,50 ))
        self.m_btnBatAdd.SetMaxSize(wx.Size( 50,50 ))
        self.m_btnTableType.SetMaxSize(wx.Size( 50,50 ))
        self.m_btnArea.SetMaxSize(wx.Size( 50,50 ))
        self.m_btnRefresh.SetMaxSize(wx.Size( 50,50 ))
        self.m_btnExit.SetMaxSize(wx.Size( 50,50 ))
        self.m_topPanel.SetMaxSize( wx.Size( x-400,50 ) ) 
        self.m_treeCtrl.SetMinSize( wx.Size( 200,y-50 ) )
        self.m_dataViewListCtrl.SetMinSize( wx.Size( x-200,y-50 ) )
        
    def OnNew( self, event ):
        event.Skip()
    
    def OnModify( self, event ):
        event.Skip()
    
    def OnDelete( self, event ):
        event.Skip()
    
    def OnBatAdd( self, event ):
        event.Skip()
    
    def OnTableType( self, event ):
        event.Skip()
    
    def OnAreaSetting( self, event ):
        event.Skip()
    
    def OnRefresh( self, event ):
        event.Skip()
    
    def OnExit( self, event ):
        event.Skip()
        CAppManager.SwitchToApplication('MainFrame')
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = CDiningTable(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()
