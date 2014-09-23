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
from app.UI.dining_room.CPopAreaSetting import CPopAreaSetting
from app.UI.dining_room.CPopTypeSetting import CPopTypeSetting
from app.UI.dining_room.CPopTableInfo import CPopTableInfo
from app.logic.dining_room.CModelTable import CModelTable
from app.logic.dining_room.CDataTable import CDataTableInfo
from app.UI.dining_room.CPopMinexpenseSetting import CPopMinexpenseSetting
from app.logic.dining_room.CDataType import CDataTypeInfo
from framework.CEvtManager import CEvtManager
from app.logic.CEnumEvent import CEnumEvent
from app.UI.dining_room.CPopTableBatAdd import CPopTableBatAdd

###########################################################################
## Class CDiningTable
###########################################################################

class CWgtDiningTable (wx.Panel):
    def _init_status_bar_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.SetMinSize(wx.Size(800,50)) 

        # Add new button
        self.btnNew = wx.Button(self, wx.ID_ANY, u"新增", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnNew.SetMinSize(wx.Size(50,50))
        sizer.Add(self.btnNew, 0, wx.EXPAND, 5)
        # Add modify button
        self.btnModify = wx.Button(self, wx.ID_ANY, u"修改", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnModify.SetMinSize(wx.Size(50,50)) 
        sizer.Add(self.btnModify, 0, 0, 5)
        # Add delete button
        self.btnDelete = wx.Button(self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnDelete.SetMinSize(wx.Size(50,50))
        sizer.Add(self.btnDelete, 0, 0, 5)
        # Add batch add button
        self.btnBatAdd = wx.Button(self, wx.ID_ANY, u"批量增加", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnBatAdd.SetFont(wx.Font(8, 70, 90, 90, False, wx.EmptyString))
        self.btnBatAdd.SetMinSize(wx.Size(50, 50))
        sizer.Add(self.btnBatAdd, 0, 0, 5)
        # Add table type setting button
        self.btnTableType = wx.Button(self, wx.ID_ANY, u"桌类", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnTableType.SetMinSize(wx.Size(50,50)) 
        sizer.Add(self.btnTableType, 0, 0, 5)
        # Add area setting button
        self.btnArea = wx.Button(self, wx.ID_ANY, u"区域", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnArea.SetMinSize(wx.Size(50,50))
        sizer.Add(self.btnArea, 0, 0, 5)
        # Add consumer type setting button
        self.btnMinExpense = wx.Button(self, wx.ID_ANY, u"最低消费", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnMinExpense.SetFont(wx.Font(8, 70, 90, 90, False, wx.EmptyString))
        self.btnMinExpense.SetMinSize(wx.Size(50,50))
        sizer.Add(self.btnMinExpense, 0, 0, 5)
        # Add refresh button
        self.btnRefresh = wx.Button(self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnRefresh.SetMinSize(wx.Size(50,50))
        sizer.Add(self.btnRefresh, 0, 0, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnExit.SetMinSize(wx.Size(50,50))
        sizer.Add(self.btnExit, 0, 0, 5)
        # Add fix panel
        self.topPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.topPanel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
        sizer.Add(self.topPanel, 1, wx.EXPAND, 5)
        
        # Layout status bar
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_screen_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.SetMinSize(wx.Size(800, 550)) 

        self._init_tree_sizer(sizer)
        self._init_view_sizer(sizer)

        # Layout screen
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_tree_sizer(self, parent):
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.SetMinSize(wx.Size(200, 550)) 

        # Create tree control
        self.treeCtrl = wx.TreeCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE)
        self.treeCtrl.SetMinSize(wx.Size(-1, 600))
        sizer.Add(self.treeCtrl, 0, wx.EXPAND, 5)
        
        # Layout tree control
        parent.Add(sizer, 1, 0, 5)

    def _init_view_sizer(self, parent):
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.SetMinSize(wx.Size(600, 550)) 

        # Create data view list
        self.dataViewList = wx.dataview.DataViewCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.dataViewList.SetMinSize(wx.Size(-1, 600))
        # Add items into data view list
        self.dataViewList.AppendTextColumn(u"行号", 0) 
        self.dataViewList.AppendTextColumn(u"桌号", 1) 
        self.dataViewList.AppendTextColumn(u"餐桌名", 2) 
        self.dataViewList.AppendTextColumn(u"类型", 3) 
        self.dataViewList.AppendTextColumn(u"区域", 4) 
        self.dataViewList.AppendTextColumn(u"人数", 5) 
        self.dataViewList.AppendTextColumn(u"最低消费类型", 6, width=100)
        sizer.Add(self.dataViewList, 0, wx.EXPAND|wx.LEFT, 5)
        
        # Layout data view list
        parent.Add(sizer, 1, 0, 5)

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size= wx.Size(800,600), style=wx.TAB_TRAVERSAL)
        
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DDKSHADOW))
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        self._init_status_bar_sizer(sizer)
        self._init_screen_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)
        
        # Create an instance of our model...
        self.model = CModelTable(CDataTableInfo.GetData())
        CDataTableInfo.RefreshItems()
        
        # Tell the DVC to use the model
        self.dataViewList.AssociateModel(self.model)

        # Connect Events
        self.Bind(wx.EVT_SIZE, self.OnSize) 
        self.btnNew.Bind(wx.EVT_BUTTON, self.OnBtnNew)
        self.btnModify.Bind(wx.EVT_BUTTON, self.OnBtnModify)
        self.btnDelete.Bind(wx.EVT_BUTTON, self.OnBtnDelete)
        self.btnBatAdd.Bind(wx.EVT_BUTTON, self.OnBtnBatAdd)
        self.btnTableType.Bind(wx.EVT_BUTTON, self.OnBtnTableType)
        self.btnArea.Bind(wx.EVT_BUTTON, self.OnBtnAreaSetting)
        self.btnMinExpense.Bind(wx.EVT_BUTTON, self.OnBtnMinExpense)
        self.btnRefresh.Bind(wx.EVT_BUTTON, self.OnBtnRefresh)
        self.btnExit.Bind(wx.EVT_BUTTON, self.OnBtnExit)
        
        # Show tree control
        self.ShowTreeCtrl()
    
    def __del__( self ):
        pass
    
    def Initailize(self):
        # Add event listener
        CEvtManager.AddListenner(self, CEnumEvent.EVT_DINING_ROOM_REFRESH, self.OnBtnRefresh)
        
        x, y = CDataDeskTop.GetFrameSize()
        self.SetSize(wx.Size(x, y))

    def Uninitailize(self):
        # Remove event listener
        CEvtManager.RemoveListenner(self, CEnumEvent.EVT_DINING_ROOM_REFRESH, self.OnBtnRefresh)
    
    def ShowTreeCtrl(self):
        isz = (16,16)
        il = wx.ImageList(isz[0], isz[1])
        fldridx     = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER,      wx.ART_OTHER, isz))
        fldropenidx = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER_OPEN, wx.ART_OTHER, isz))
        fileidx     = il.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, isz))
        
        self.treeCtrl.SetImageList(il)
        self.il = il

        self.root = self.treeCtrl.AddRoot(u"全部桌类")
        self.treeCtrl.SetPyData(self.root, None)
        self.treeCtrl.SetItemImage(self.root, fldridx, wx.TreeItemIcon_Normal)
        self.treeCtrl.SetItemImage(self.root, fldropenidx, wx.TreeItemIcon_Expanded)
        
        table_type_map = dict()
        li_items = CDataTableInfo.GetItems()
        for item in li_items:
            if table_type_map.has_key(item.table_type):
                table_type_map[item.table_type].append(item)
            else:
                list_tmp = []
                list_tmp.append(item)
                table_type_map_tmp = {item.table_type:list_tmp}
                table_type_map.update(table_type_map_tmp)
        
        li_table_type = CDataTypeInfo.GetData()
        for table_type in li_table_type:
            if table_type_map.has_key(table_type.code):
                title = "%s(%d)" % (table_type.name, len(table_type_map[table_type.code]))
                child = self.treeCtrl.AppendItem(self.root, title)
                self.treeCtrl.SetPyData(child, None)
                self.treeCtrl.SetItemImage(child, fldridx, wx.TreeItemIcon_Normal)
                self.treeCtrl.SetItemImage(child, fldropenidx, wx.TreeItemIcon_Expanded)
                for table_info in table_type_map[table_type.code]:
                    sub_clild = self.treeCtrl.AppendItem(child, table_info.name)
                    self.treeCtrl.SetPyData(sub_clild, None)
                    self.treeCtrl.SetItemImage(sub_clild, fileidx, wx.TreeItemIcon_Normal)
                    self.treeCtrl.SetItemImage(sub_clild, fileidx, wx.TreeItemIcon_Selected)
            else:
                title = "%s(0)" % table_type.name
                child = self.treeCtrl.AppendItem(self.root, title)
                self.treeCtrl.SetPyData(child, None)
                self.treeCtrl.SetItemImage(child, fldridx, wx.TreeItemIcon_Normal)
                self.treeCtrl.SetItemImage(child, fldropenidx, wx.TreeItemIcon_Expanded)
                
        self.treeCtrl.Expand(self.root)
                
    def RefreshUI(self):
        # Refresh treeCtrl
        CDataTableInfo.RefreshItems()
        self.treeCtrl.DeleteAllItems()
        self.ShowTreeCtrl()
        
        # Refresh data view list
        result = CDataTableInfo.GetData()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
                    
        self.model.Cleared()
    
    # Virtual event handlers, override them in your derived class
    def OnSize( self, event ):
        event.Skip()
        x, y = self.GetSize()

        self.btnNew.SetMaxSize(wx.Size( 50,50 ))
        self.btnModify.SetMaxSize(wx.Size( 50,50 ))
        self.btnDelete.SetMaxSize(wx.Size( 50,50 ))
        self.btnBatAdd.SetMaxSize(wx.Size( 50,50 ))
        self.btnTableType.SetMaxSize(wx.Size( 50,50 ))
        self.btnArea.SetMaxSize(wx.Size( 50,50 ))
        self.btnMinExpense.SetMaxSize(wx.Size( 50,50 ))
        self.btnRefresh.SetMaxSize(wx.Size( 50,50 ))
        self.btnExit.SetMaxSize(wx.Size( 50,50 ))
        self.topPanel.SetMaxSize( wx.Size( x-450,50 ) ) 
        self.treeCtrl.SetMinSize( wx.Size( 200,y-50 ) )
        self.dataViewList.SetMinSize( wx.Size( x-200,y-50 ) )
        
    def OnBtnNew(self, event):
        event.Skip()
        self.popTableInfo = CPopTableInfo(self, "add")
        self.popTableInfo.ShowModal()
    
    def OnBtnModify(self, event):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        index = self.model.data.index(data)
        CDataTableInfo.SetCurItemIndex(index)
        self.popTableInfo = CPopTableInfo(self, "mod")
        self.popTableInfo.ShowModal()
    
    def OnBtnDelete(self, event):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        self.model.data.remove(data)
        self.dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
        CDataTableInfo.DeleteItem(data)
    
    def OnBtnBatAdd(self, event):
        event.Skip()
        self.popBatAdd = CPopTableBatAdd(self)
        self.popBatAdd.ShowModal()
    
    def OnBtnTableType(self, event):
        event.Skip()
        self.popTableType = CPopTypeSetting(self)
        self.popTableType.ShowModal()
    
    def OnBtnAreaSetting(self, event):
        event.Skip()
        self.popArea = CPopAreaSetting(self)
        self.popArea.ShowModal()
        
    def OnBtnMinExpense(self, event):
        event.Skip()
        self.popMinExpense = CPopMinexpenseSetting(self)
        self.popMinExpense.ShowModal()
    
    def OnBtnRefresh(self, event):
        event.Skip()
        self.RefreshUI()
    
    def OnBtnExit(self, event):
        event.Skip()
        CAppManager.SwitchToApplication('DeskTop')
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = CWgtDiningTable(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()
