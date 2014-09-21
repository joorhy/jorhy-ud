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
from app.logic.dishes.CModelDishes import CModelDishes
from app.logic.dishes.CDataDishes import CDataDishes, CDataDishesInfo
from app.logic.dishes.CDataCategory import CDataCategory, CDataCategoryInfo
from app.UI.printer_setting.CPopSchemeRelated import CPopSchemeRelated
from app.UI.printer_setting.CPopSchemeRelatedBat import CPopSchemeRelatedBat
from framework.CEvtManager import CEvtManager
from app.logic.CEnumEvent import CEnumEvent

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
        self.m_dataViewList = wx.dataview.DataViewCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_dataViewList.SetMinSize( wx.Size( -1,600 ) )
        
        # Create an instance of our model...
        self.model = CModelDishes(CDataDishesInfo.GetData())
        CDataDishesInfo.RefreshItems()
        
        # Tel the DVC to use the model
        self.m_dataViewList.AssociateModel(self.model)
        
        self.m_dataViewLine = self.m_dataViewList.AppendTextColumn( u"行号", 0 ) 
        self.m_dataViewCode = self.m_dataViewList.AppendTextColumn( u"品码", 1 ) 
        self.m_dataViewName = self.m_dataViewList.AppendTextColumn( u"品名", 2 ) 
        self.m_dataViewType = self.m_dataViewList.AppendTextColumn( u"厨打方式", 10 ) 
        m_rightSizer.Add( self.m_dataViewList, 0, wx.EXPAND|wx.LEFT, 5 )
        
        
        m_bottomSizer.Add( m_rightSizer, 1, 0, 5 )
        
        
        m_sizer.Add( m_bottomSizer, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( m_sizer )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.Bind( wx.EVT_SIZE, self.OnSize )
        
        self.m_btnSetting.Bind( wx.EVT_BUTTON, self.OnBntSetting )
        self.m_btnBatSetting.Bind( wx.EVT_BUTTON, self.OnBntBatSetting )
        self.m_btnExit.Bind( wx.EVT_BUTTON, self.OnExit )
        
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged, self.m_treeCtrl)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.OnActivate, self.m_treeCtrl)
        
        # Show tree ctrl
        self.tree_data = None
        self.ShowTreeCtrl()
    
    def __del__( self ):
        pass
    
    def Initailize(self):
        # Add event listenner
        CEvtManager.AddListenner(self, CEnumEvent.EVT_DISHES_PUBLISH_REFRESH, self.OnRefresh)
        
        x, y = CDataDeskTop.GetFrameSize()       
        self.SetSize(wx.Size(x, y))

    def Uninitailize(self):
        # Add event listenner
        CEvtManager.RemoveListenner(self, CEnumEvent.EVT_DISHES_PUBLISH_REFRESH, self.OnRefresh)
    
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
        CDataDishesInfo.RefreshItems()
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
                self.m_treeCtrl.SetPyData(child, dishes_map[category.code])
                self.m_treeCtrl.SetItemImage(child, fldridx, wx.TreeItemIcon_Normal)
                self.m_treeCtrl.SetItemImage(child, fldropenidx, wx.TreeItemIcon_Expanded)
                for dishes in dishes_map[category.code]:
                    sub_clild = self.m_treeCtrl.AppendItem(child, dishes.name)
                    self.m_treeCtrl.SetPyData(sub_clild, dishes)
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
        
    def OnBntSetting( self, event ):
        event.Skip()
        if isinstance(self.tree_data, CDataDishes):
            CDataDishesInfo.SetCurItemIndex2(self.tree_data)
            self.popRelatedSetting = CPopSchemeRelated(self)
            self.popRelatedSetting.ShowModal()
    
    def OnBntBatSetting( self, event ):
        event.Skip()
        if isinstance(self.tree_data, list):
            CDataDishesInfo.SetCurListData(self.tree_data)
            self.popRelatedBatSetting = CPopSchemeRelatedBat(self)
            self.popRelatedBatSetting.ShowModal()
    
    def OnExit( self, event ):
        event.Skip()
        CAppManager.SwitchToApplication('DeskTop')
        
    def OnSelChanged(self, event):
        event.Skip()
        self.tree_data = self.m_treeCtrl.GetPyData(event.GetItem())

    def OnActivate(self, event):
        event.Skip()
        
    def OnRefresh(self, event ):
        event.Skip()
        # Refresh treeCtrl
        CDataDishesInfo.RefreshItems()
        self.m_treeCtrl.DeleteAllItems()
        self.ShowTreeCtrl()
        
        # Refresh dataviewlist
        result = CDataDishesInfo.GetData()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.m_dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
                    
        self.model.Cleared()
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = CWgtSchemeRelated(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()
