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

class CWgtDiningTable ( wx.Panel ):
    
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
        
        self.m_btnMinExpense = wx.Button( self, wx.ID_ANY, u"最低消费", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnMinExpense.SetFont( wx.Font( 8, 70, 90, 90, False, wx.EmptyString ) )
        self.m_btnMinExpense.SetMinSize( wx.Size( 50,50 ) )
        
        m_topSizer.Add( self.m_btnMinExpense, 0, 0, 5 )
        
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
        self.m_dataViewList = wx.dataview.DataViewCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_dataViewList.SetMinSize( wx.Size( -1,600 ) )
        
        # Create an instance of our model...
        self.model = CModelTable(CDataTableInfo.GetData())
        CDataTableInfo.RefreshItems()
        
        # Tel the DVC to use the model
        self.m_dataViewList.AssociateModel(self.model)
        
        self.m_dataViewColunmNum = self.m_dataViewList.AppendTextColumn( u"行号", 0 ) 
        self.m_dataViewTableNum = self.m_dataViewList.AppendTextColumn( u"桌号", 1 ) 
        self.m_dataViewTableName = self.m_dataViewList.AppendTextColumn( u"餐桌名", 2 ) 
        self.m_dataViewType = self.m_dataViewList.AppendTextColumn( u"类型", 3 ) 
        self.m_dataViewArea = self.m_dataViewList.AppendTextColumn( u"区域", 4 ) 
        self.m_dataViewCustomerNum = self.m_dataViewList.AppendTextColumn( u"人数", 5 ) 
        self.m_dataViewMinExpense = self.m_dataViewList.AppendTextColumn( u"最低消费类型", 6, width=100 )
        
        m_rightSizer.Add( self.m_dataViewList, 0, wx.EXPAND|wx.LEFT, 5 )
        
        
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
        self.m_btnMinExpense.Bind( wx.EVT_BUTTON, self.OnMinExpense )
        self.m_btnRefresh.Bind( wx.EVT_BUTTON, self.OnRefresh )
        self.m_btnExit.Bind( wx.EVT_BUTTON, self.OnExit )
        
        # Show tree ctrl
        self.ShowTreeCtrl()
    
    def __del__( self ):
        pass
    
    def Initailize(self):
        # Add event listenner
        CEvtManager.AddListenner(self, CEnumEvent.EVT_DINING_ROOM_REFRESH, self.OnRefresh)
        
        x, y = CDataDeskTop.GetFrameSize()
        self.SetSize(wx.Size(x, y))

    def Uninitailize(self):
        # Remove event listenner
        CEvtManager.RemoveListenner(self, CEnumEvent.EVT_DINING_ROOM_REFRESH, self.OnRefresh)
    
    def ShowTreeCtrl(self):
        isz = (16,16)
        il = wx.ImageList(isz[0], isz[1])
        fldridx     = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER,      wx.ART_OTHER, isz))
        fldropenidx = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER_OPEN, wx.ART_OTHER, isz))
        fileidx     = il.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, isz))
        
        self.m_treeCtrl.SetImageList(il)
        self.il = il

        self.root = self.m_treeCtrl.AddRoot(u"全部桌类")
        self.m_treeCtrl.SetPyData(self.root, None)
        self.m_treeCtrl.SetItemImage(self.root, fldridx, wx.TreeItemIcon_Normal)
        self.m_treeCtrl.SetItemImage(self.root, fldropenidx, wx.TreeItemIcon_Expanded)
        
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
                child = self.m_treeCtrl.AppendItem(self.root, title)
                self.m_treeCtrl.SetPyData(child, None)
                self.m_treeCtrl.SetItemImage(child, fldridx, wx.TreeItemIcon_Normal)
                self.m_treeCtrl.SetItemImage(child, fldropenidx, wx.TreeItemIcon_Expanded)
                for table_info in table_type_map[table_type.code]:
                    sub_clild = self.m_treeCtrl.AppendItem(child, table_info.name)
                    self.m_treeCtrl.SetPyData(sub_clild, None)
                    self.m_treeCtrl.SetItemImage(sub_clild, fileidx, wx.TreeItemIcon_Normal)
                    self.m_treeCtrl.SetItemImage(sub_clild, fileidx, wx.TreeItemIcon_Selected)
            else:
                title = "%s(0)" % table_type.name
                child = self.m_treeCtrl.AppendItem(self.root, title)
                self.m_treeCtrl.SetPyData(child, None)
                self.m_treeCtrl.SetItemImage(child, fldridx, wx.TreeItemIcon_Normal)
                self.m_treeCtrl.SetItemImage(child, fldropenidx, wx.TreeItemIcon_Expanded)
                
        self.m_treeCtrl.Expand(self.root)
                
    def RefreshUI(self):
        # Refresh treeCtrl
        CDataTableInfo.RefreshItems()
        self.m_treeCtrl.DeleteAllItems()
        self.ShowTreeCtrl()
        
        # Refresh dataviewlist
        result = CDataTableInfo.GetData()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.m_dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
                    
        self.model.Cleared()
    
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
        self.m_btnMinExpense.SetMaxSize(wx.Size( 50,50 ))
        self.m_btnRefresh.SetMaxSize(wx.Size( 50,50 ))
        self.m_btnExit.SetMaxSize(wx.Size( 50,50 ))
        self.m_topPanel.SetMaxSize( wx.Size( x-450,50 ) ) 
        self.m_treeCtrl.SetMinSize( wx.Size( 200,y-50 ) )
        self.m_dataViewList.SetMinSize( wx.Size( x-200,y-50 ) )
        
    def OnNew( self, event ):
        event.Skip()
        self.popTableInfo = CPopTableInfo(self, "add")
        self.popTableInfo.ShowModal()
    
    def OnModify( self, event ):
        event.Skip()
        item = self.m_dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        index = self.model.data.index(data)
        CDataTableInfo.SetCurItemIndex(index)
        self.popTableInfo = CPopTableInfo(self, "mod")
        self.popTableInfo.ShowModal()
    
    def OnDelete( self, event ):
        event.Skip()
        item = self.m_dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        self.model.data.remove(data)
        self.m_dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
        CDataTableInfo.DeleteItem(data)
    
    def OnBatAdd( self, event ):
        event.Skip()
        self.popBatAdd = CPopTableBatAdd(self)
        self.popBatAdd.ShowModal()
    
    def OnTableType( self, event ):
        event.Skip()
        self.popTableType = CPopTypeSetting(self)
        self.popTableType.ShowModal()
    
    def OnAreaSetting( self, event ):
        event.Skip()
        self.popArea = CPopAreaSetting(self)
        self.popArea.ShowModal()
        
    def OnMinExpense( self, event ):
        event.Skip()
        self.popMinExpense = CPopMinexpenseSetting(self)
        self.popMinExpense.ShowModal()
    
    def OnRefresh( self, event ):
        event.Skip()
        self.RefreshUI()
    
    def OnExit( self, event ):
        event.Skip()
        CAppManager.SwitchToApplication('DeskTop')
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = CWgtDiningTable(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()
