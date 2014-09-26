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
from framework.core import EvtManager
from app.logic.CEnumEvent import CEnumEvent

###########################################################################
## Class CWgtSchemeRelated
###########################################################################

class CWgtSchemeRelated (wx.Panel):
    def _init_status_bar_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.SetMinSize(wx.Size(800,50))
        # Add kitchen print setting button
        self.btnSetting = wx.Button(self, wx.ID_ANY, u"厨打设置", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnSetting, 0, wx.EXPAND, 5)
        # Add batch kitchen print setting button
        self.btnBatSetting = wx.Button(self, wx.ID_ANY, u"批处理", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnBatSetting.SetMinSize(wx.Size(100,50)) 
        sizer.Add(self.btnBatSetting, 0, 0, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnExit.SetMinSize(wx.Size(50,50))
        sizer.Add(self.btnExit, 0, 0, 5)
        # Add fix space panel
        self.topPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.topPanel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
        sizer.Add(self.topPanel, 1, wx.EXPAND, 5)
        
        # Layout status bar sizer
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_data_view_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.SetMinSize(wx.Size(800,550)) 
        # Add tree control
        leftSizer = wx.BoxSizer(wx.VERTICAL)
        leftSizer.SetMinSize(wx.Size(200,550)) 
        self.treeCtrl = wx.TreeCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE)        
        leftSizer.Add(self.treeCtrl, 0, wx.EXPAND, 5)
        sizer.Add(leftSizer, 1, 0, 5)
        # Add data view list
        rightSizer = wx.BoxSizer(wx.VERTICAL) 
        rightSizer.SetMinSize(wx.Size(600,550)) 
        self.dataViewList = wx.dataview.DataViewCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.dataViewList.SetMinSize(wx.Size(-1,600))
        # Add items into data view list
        self.dataViewList.AppendTextColumn(u"行号", 0) 
        self.dataViewList.AppendTextColumn(u"品码", 1) 
        self.dataViewList.AppendTextColumn(u"品名", 2) 
        self.dataViewList.AppendTextColumn(u"厨打方式", 10) 
        rightSizer.Add(self.dataViewList, 0, wx.EXPAND|wx.LEFT, 5)

        sizer.Add(rightSizer, 1, 0, 5)
        # Layout data view list
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(800,600), style=wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_status_bar_sizer(sizer)
        self._init_data_view_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre( wx.BOTH )

        # Create an instance of our model...
        self.model = CModelDishes(CDataDishesInfo.GetData())
        CDataDishesInfo.RefreshItems()
        
        # Tell the DVC to use the model
        self.dataViewList.AssociateModel(self.model)

        # Connect Events
        self.Bind( wx.EVT_SIZE, self.OnSize )
        
        self.btnSetting.Bind(wx.EVT_BUTTON, self.OnBntSetting)
        self.btnBatSetting.Bind(wx.EVT_BUTTON, self.OnBntBatSetting)
        self.btnExit.Bind(wx.EVT_BUTTON, self.OnExit)
        
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged, self.treeCtrl)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.OnActivate, self.treeCtrl)
        
        # Show tree control
        self.tree_data = None
        self.ShowTreeCtrl()
    
    def __del__( self ):
        pass
    
    def Initailize(self):
        # Add event listener
        EvtManager.AddListener(self, CEnumEvent.EVT_DISHES_PUBLISH_REFRESH, self.OnRefresh)
        
        x, y = CDataDeskTop.GetFrameSize()       
        self.SetSize(wx.Size(x, y))

    def Uninitailize(self):
        # Add event listener
        EvtManager.RemoveListener(self, CEnumEvent.EVT_DISHES_PUBLISH_REFRESH, self.OnRefresh)
    
    def ShowTreeCtrl(self):
        isz = (16,16)
        il = wx.ImageList(isz[0], isz[1])
        fldridx     = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER,      wx.ART_OTHER, isz))
        fldropenidx = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER_OPEN, wx.ART_OTHER, isz))
        fileidx     = il.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, isz))
        
        self.treeCtrl.SetImageList(il)
        self.il = il

        self.root = self.treeCtrl.AddRoot(u"全部菜品")
        self.treeCtrl.SetPyData(self.root, None)
        self.treeCtrl.SetItemImage(self.root, fldridx, wx.TreeItemIcon_Normal)
        self.treeCtrl.SetItemImage(self.root, fldropenidx, wx.TreeItemIcon_Expanded)
        
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
                child = self.treeCtrl.AppendItem(self.root, title)
                self.treeCtrl.SetPyData(child, dishes_map[category.code])
                self.treeCtrl.SetItemImage(child, fldridx, wx.TreeItemIcon_Normal)
                self.treeCtrl.SetItemImage(child, fldropenidx, wx.TreeItemIcon_Expanded)
                for dishes in dishes_map[category.code]:
                    sub_clild = self.treeCtrl.AppendItem(child, dishes.name)
                    self.treeCtrl.SetPyData(sub_clild, dishes)
                    self.treeCtrl.SetItemImage(sub_clild, fileidx, wx.TreeItemIcon_Normal)
                    self.treeCtrl.SetItemImage(sub_clild, fileidx, wx.TreeItemIcon_Selected)
            else:
                title = "%s(0)" % category.name
                child = self.treeCtrl.AppendItem(self.root, title)
                self.treeCtrl.SetPyData(child, None)
                self.treeCtrl.SetItemImage(child, fldridx, wx.TreeItemIcon_Normal)
                self.treeCtrl.SetItemImage(child, fldropenidx, wx.TreeItemIcon_Expanded)
                
        self.treeCtrl.Expand(self.root)
    
    # Virtual event handlers, override them in your derived class
    def OnSize( self, event ):
        event.Skip()
        x, y = self.GetSize()

        self.btnSetting.SetMaxSize(wx.Size( 100,50 ))
        self.btnBatSetting.SetMaxSize(wx.Size( 100,50 ))
        self.btnExit.SetMaxSize(wx.Size( 50,50 ))
        self.topPanel.SetMaxSize( wx.Size( x-250,50 ) ) 
        self.treeCtrl.SetMinSize( wx.Size( 200,y-50 ) )
        self.dataViewList.SetMinSize( wx.Size( x-200,y-50 ) )
        
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
        self.tree_data = self.treeCtrl.GetPyData(event.GetItem())

    def OnActivate(self, event):
        event.Skip()
        
    def OnRefresh(self, event ):
        event.Skip()
        # Refresh treeCtrl
        CDataDishesInfo.RefreshItems()
        self.treeCtrl.DeleteAllItems()
        self.ShowTreeCtrl()
        
        # Refresh data view list
        result = CDataDishesInfo.GetData()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
                    
        self.model.Cleared()
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = CWgtSchemeRelated(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()
