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
from app.logic.desktop.CDataDeskTop import CDataDeskTop
from app.CAppManager import CAppManager
from app.UI.dishes.CPopUnitSetting import CPopUnitSetting
from app.UI.dishes.CPopCategorySetting import CPopCategorySetting
from app.UI.dishes.CPopDishesInfo import CPopDishesInfo
from app.logic.dishes.CModelDishes import CModelDishes
from app.logic.dishes.CDataDishes import CDataDishesInfo
from app.logic.dishes.CDataCategory import CDataCategoryInfo
from framework.CEvtManager import CEvtManager
from app.logic.CEnumEvent import CEnumEvent

###########################################################################
## Class CWgtDishesPublish
###########################################################################

class CWgtDishesPublish (wx.Panel):
    def _init_status_bar_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.SetMinSize(wx.Size(-1,50)) 

        # Add new button
        self.btnNew = wx.Button(self, wx.ID_ANY, u"新增", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnNew.SetMinSize(wx.Size(50,50))
        sizer.Add(self.btnNew, 0, 0, 5)
        # Add modify button
        self.btnModify = wx.Button(self, wx.ID_ANY, u"修改", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnModify.SetMinSize(wx.Size(50,50))
        sizer.Add(self.btnModify, 0, 0, 5)
        # Add delete button
        self.btnDelete = wx.Button(self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnDelete.SetMinSize(wx.Size(50,50))
        sizer.Add(self.btnDelete, 0, 0, 5)
        # Add dishes type button
        self.btnType = wx.Button(self, wx.ID_ANY, u"类型", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnType.SetMinSize(wx.Size(50,50))
        sizer.Add(self.btnType, 0, 0, 5)
        # Add dishes unit button
        self.btnUnit = wx.Button(self, wx.ID_ANY, u"单位", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnUnit.SetMinSize(wx.Size(50,50))
        sizer.Add(self.btnUnit, 0, 0, 5)
        # Add refresh button
        self.btnRefresh = wx.Button(self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnRefresh.SetMinSize(wx.Size(50,50))
        sizer.Add(self.btnRefresh, 0, 0, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnExit.SetMinSize(wx.Size(50,50))
        sizer.Add(self.btnExit, 0, 0, 5)
        # Add space fix panel 
        self.topPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.topPanel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
        sizer.Add(self.topPanel, 1, wx.EXPAND, 5)
        
        # Layout status bar
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_view_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # This sizer for tree control
        leftSizer = wx.BoxSizer(wx.VERTICAL) 
        leftSizer.SetMinSize(wx.Size(200,600)) 
        # Create a tree control
        self.treeCtrl = wx.TreeCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE)
        self.treeCtrl.SetMinSize(wx.Size(-1,600))
        leftSizer.Add(self.treeCtrl, 0, wx.EXPAND, 5)
        # Layout tree control
        sizer.Add(leftSizer, 1, 0, 5)
        
        # This sizer for data view list
        rightSizer = wx.BoxSizer(wx.VERTICAL)
        rightSizer.SetMinSize(wx.Size(600,600)) 
        # Create a data view list
        self.dataViewList = wx.dataview.DataViewCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1,600), 0)
        # Add items into data view list
        self.dataViewList.AppendTextColumn(u"行号", 0) 
        self.dataViewList.AppendTextColumn(u"品码", 1) 
        self.dataViewList.AppendTextColumn(u"品名", 2) 
        self.dataViewList.AppendTextColumn(u"拼音简码", 3) 
        self.dataViewList.AppendTextColumn(u"规格", 4) 
        self.dataViewList.AppendTextColumn(u"做法", 5) 
        self.dataViewList.AppendTextColumn(u"所属类", 6) 
        self.dataViewList.AppendTextColumn(u"单位", 7) 
        self.dataViewList.AppendTextColumn(u"售价", 8) 
        self.dataViewList.AppendToggleColumn(u"停用", 9) 
        rightSizer.Add(self.dataViewList, 0, wx.EXPAND|wx.LEFT, 5)
        # Layout data view list
        sizer.Add(rightSizer, 1, 0, 5)
        
        # Layout view sizer
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(800,600), style=wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_status_bar_sizer(sizer)
        self._init_view_sizer(sizer)
        
        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)
        
        # Create an instance of our model...
        self.model = CModelDishes(CDataDishesInfo.GetData())
        CDataDishesInfo.RefreshItems()
        
        # Tel the DVC to use the model
        self.dataViewList.AssociateModel(self.model)

        # Connect Events
        self.Bind(wx.EVT_SIZE, self.OnSize)
        
        self.btnNew.Bind(wx.EVT_BUTTON, self.OnBtnNew)
        self.btnModify.Bind(wx.EVT_BUTTON, self.OnBtnModify)
        self.btnDelete.Bind(wx.EVT_BUTTON, self.OnBtnDelete)
        self.btnType.Bind(wx.EVT_BUTTON, self.OnBtnType)
        self.btnUnit.Bind(wx.EVT_BUTTON, self.OnBtnUnit)
        self.btnRefresh.Bind(wx.EVT_BUTTON, self.OnBtnRefresh)
        self.btnExit.Bind(wx.EVT_BUTTON, self.OnBtnExit)
        
        # Show tree control
        self.ShowTreeCtrl()
    
    def __del__( self ):
        pass
    
    def Initailize(self):
        # Add event listener
        CEvtManager.AddListener(self, CEnumEvent.EVT_DISHES_PUBLISH_REFRESH, self.OnBtnRefresh)
        
        x, y = CDataDeskTop.GetFrameSize()        
        self.SetSize(wx.Size(x, y))

    def Uninitailize(self):
        # Remove event listener
        CEvtManager.RemoveListener(self, CEnumEvent.EVT_DISHES_PUBLISH_REFRESH, self.OnBtnRefresh)
    
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
                self.treeCtrl.SetPyData(child, None)
                self.treeCtrl.SetItemImage(child, fldridx, wx.TreeItemIcon_Normal)
                self.treeCtrl.SetItemImage(child, fldropenidx, wx.TreeItemIcon_Expanded)
                for dishes in dishes_map[category.code]:
                    sub_clild = self.treeCtrl.AppendItem(child, dishes.name)
                    self.treeCtrl.SetPyData(sub_clild, None)
                    self.treeCtrl.SetItemImage(sub_clild, fileidx, wx.TreeItemIcon_Normal)
                    self.treeCtrl.SetItemImage(sub_clild, fileidx, wx.TreeItemIcon_Selected)
            else:
                title = "%s(0)" % category.name
                child = self.treeCtrl.AppendItem(self.root, title)
                self.treeCtrl.SetPyData(child, None)
                self.treeCtrl.SetItemImage(child, fldridx, wx.TreeItemIcon_Normal)
                self.treeCtrl.SetItemImage(child, fldropenidx, wx.TreeItemIcon_Expanded)
                
        self.treeCtrl.Expand(self.root)
    
    def RefreshUI(self):
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
    
    # Virtual event handlers, override them in your derived class
    def OnSize(self, event):
        event.Skip()
        x, y = self.GetSize()
        
        self.btnNew.SetMaxSize(wx.Size(50,50))
        self.btnModify.SetMaxSize(wx.Size(50,50))
        self.btnDelete.SetMaxSize(wx.Size(50,50))
        self.btnType.SetMaxSize(wx.Size(50,50))
        self.btnUnit.SetMaxSize(wx.Size(50,50))
        self.btnRefresh.SetMaxSize(wx.Size(50,50))
        self.btnExit.SetMaxSize(wx.Size(50,50))
        self.topPanel.SetMaxSize(wx.Size(x-350,50)) 
        self.treeCtrl.SetMinSize(wx.Size(200,y-50))
        self.dataViewList.SetMinSize(wx.Size(x-200,y-50))
        
    def OnBtnNew(self, event):
        event.Skip()
        self.popDishesInfo = CPopDishesInfo(self, "add")
        self.popDishesInfo.ShowModal()
    
    def OnBtnModify(self, event):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        index = self.model.data.index(data)
        CDataDishesInfo.SetCurItemIndex(index)
        self.popDishesInfo = CPopDishesInfo(self, "mod")
        self.popDishesInfo.ShowModal()
    
    def OnBtnDelete(self, event):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        self.model.data.remove(data)
        self.dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
        CDataDishesInfo.DeleteItem(data)
    
    def OnBtnType(self, event):
        event.Skip()
        self.popCategory = CPopCategorySetting(self)
        self.popCategory.ShowModal()
    
    def OnBtnUnit(self, event):
        event.Skip()
        self.popUnit = CPopUnitSetting(self)
        self.popUnit.ShowModal()
    
    def OnBtnRefresh(self, event):
        event.Skip()
        self.RefreshUI()
    
    def OnBtnExit(self, event):
        event.Skip()
        CDataDeskTop.SetSelectedItem()
        CAppManager.SwitchToApplication('DeskTop')
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = CWgtDishesPublish(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()
