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
from app.CAppManager import CAppManager
from app.logic.desktop.CDataDeskTop import CDataDeskTop
from app.logic.dishes.CDataDishes import CDataDishesInfo
from app.logic.dishes.CDataCategory import CDataCategoryInfo

###########################################################################
## Class CWgtSchemeRelated
###########################################################################

class CWgtSchemeRelated ( wx.Panel ):
    
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        m_sizer = wx.BoxSizer( wx.VERTICAL )
        
        m_topSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        m_topSizer.SetMinSize( wx.Size( 800,50 ) ) 
        self.m_btnSetting = wx.Button( self, wx.ID_ANY, u"厨打设置", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnSetting.SetMinSize( wx.Size( 100,50 ) )
        
        m_topSizer.Add( self.m_btnSetting, 0, wx.EXPAND, 5 )
        
        self.m_btnBatSetting = wx.Button( self, wx.ID_ANY, u"批处理", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnBatSetting.SetMinSize( wx.Size( 100,50 ) )
        
        m_topSizer.Add( self.m_btnBatSetting, 0, 0, 5 )
        
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
        m_leftSizer.Add( self.m_treeCtrl, 0, wx.EXPAND, 5 )
        
        
        m_bottomSizer.Add( m_leftSizer, 1, 0, 5 )
        
        m_rightSizer = wx.BoxSizer( wx.VERTICAL )
        
        m_rightSizer.SetMinSize( wx.Size( 600,550 ) ) 
        self.m_dataViewList = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_dataViewList.SetMinSize( wx.Size( -1,600 ) )
        
        self.m_dataViewLine = self.m_dataViewList.AppendTextColumn( u"行号" ) 
        self.m_dataViewCode = self.m_dataViewList.AppendTextColumn( u"品码" ) 
        self.m_dataViewName = self.m_dataViewList.AppendTextColumn( u"品名" ) 
        self.m_dataViewType = self.m_dataViewList.AppendTextColumn( u"厨打方式" ) 
        m_rightSizer.Add( self.m_dataViewList, 0, wx.EXPAND|wx.LEFT, 5 )
        
        
        m_bottomSizer.Add( m_rightSizer, 1, 0, 5 )
        
        
        m_sizer.Add( m_bottomSizer, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( m_sizer )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.Bind( wx.EVT_SIZE, self.OnSize )
        
        self.m_btnSetting.Bind( wx.EVT_BUTTON, self.OnNew )
        self.m_btnBatSetting.Bind( wx.EVT_BUTTON, self.OnModify )
        self.m_btnExit.Bind( wx.EVT_BUTTON, self.OnExit )
        
        # Show tree ctrl
        self.ShowTreeCtrl()
    
    def __del__( self ):
        pass
    
    def Initailize(self):
        x, y = CDataDeskTop.GetFrameSize()       
        self.SetSize(wx.Size(x, y))

    def Uninitailize(self):
        pass
    
    def ShowTreeCtrl(self):
        isz = (16,16)
        il = wx.ImageList(isz[0], isz[1])
        fldridx     = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER,      wx.ART_OTHER, isz))
        fldropenidx = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER_OPEN, wx.ART_OTHER, isz))
        fileidx     = il.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, isz))
        
        self.m_treeCtrl.SetImageList(il)
        self.il = il

        self.root = self.m_treeCtrl.AddRoot(u"全部菜品")
        self.m_treeCtrl.SetPyData(self.root, None)
        self.m_treeCtrl.SetItemImage(self.root, fldridx, wx.TreeItemIcon_Normal)
        self.m_treeCtrl.SetItemImage(self.root, fldropenidx, wx.TreeItemIcon_Expanded)
        
        dishes_map = dict()
        li_items = CDataDishesInfo.GetItems()
        for item in li_items:
            if dishes_map.has_key(item.category):
                dishes_map[item.category].append(item)
            else:
                list_tmp = []
                list_tmp.append(item)
                dishes_map_tmp = {item.category:list_tmp}
                dishes_map.update(dishes_map_tmp)
        
        li_category = CDataCategoryInfo.GetData()
        for category in li_category:
            if dishes_map.has_key(category.code):
                title = "%s(%d)" % (category.name, len(dishes_map[category.code]))
                child = self.m_treeCtrl.AppendItem(self.root, title)
                self.m_treeCtrl.SetPyData(child, None)
                self.m_treeCtrl.SetItemImage(child, fldridx, wx.TreeItemIcon_Normal)
                self.m_treeCtrl.SetItemImage(child, fldropenidx, wx.TreeItemIcon_Expanded)
                for dishes in dishes_map[category.code]:
                    sub_clild = self.m_treeCtrl.AppendItem(child, dishes.name)
                    self.m_treeCtrl.SetPyData(sub_clild, None)
                    self.m_treeCtrl.SetItemImage(sub_clild, fileidx, wx.TreeItemIcon_Normal)
                    self.m_treeCtrl.SetItemImage(sub_clild, fileidx, wx.TreeItemIcon_Selected)
            else:
                title = "%s(0)" % category.name
                child = self.m_treeCtrl.AppendItem(self.root, title)
                self.m_treeCtrl.SetPyData(child, None)
                self.m_treeCtrl.SetItemImage(child, fldridx, wx.TreeItemIcon_Normal)
                self.m_treeCtrl.SetItemImage(child, fldropenidx, wx.TreeItemIcon_Expanded)
                
        self.m_treeCtrl.Expand(self.root)
    
    # Virtual event handlers, overide them in your derived class
    def OnSize( self, event ):
        event.Skip()
        x, y = self.GetSize()

        self.m_btnSetting.SetMaxSize(wx.Size( 100,50 ))
        self.m_btnBatSetting.SetMaxSize(wx.Size( 100,50 ))
        self.m_btnExit.SetMaxSize(wx.Size( 50,50 ))
        self.m_topPanel.SetMaxSize( wx.Size( x-250,50 ) ) 
        self.m_treeCtrl.SetMinSize( wx.Size( 200,y-50 ) )
        self.m_dataViewList.SetMinSize( wx.Size( x-200,y-50 ) )
        
    def OnNew( self, event ):
        event.Skip()
    
    def OnModify( self, event ):
        event.Skip()
    
    def OnExit( self, event ):
        event.Skip()
        CAppManager.SwitchToApplication('DeskTop')
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = CWgtSchemeRelated(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()
