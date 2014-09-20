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
## Class CDishesPublish
###########################################################################

class CWgtDishesPublish ( wx.Panel ):
    
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        m_sizer = wx.BoxSizer( wx.VERTICAL )
        
        m_topSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        m_topSizer.SetMinSize( wx.Size( -1,50 ) ) 
        self.m_btnNew = wx.Button( self, wx.ID_ANY, u"新增", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnNew.SetMinSize( wx.Size( 50,50 ) )
        
        m_topSizer.Add( self.m_btnNew, 0, 0, 5 )
        
        self.m_btnModify = wx.Button( self, wx.ID_ANY, u"修改", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnModify.SetMinSize( wx.Size( 50,50 ) )
        
        m_topSizer.Add( self.m_btnModify, 0, 0, 5 )
        
        self.m_btnDelete = wx.Button( self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnDelete.SetMinSize( wx.Size( 50,50 ) )
        
        m_topSizer.Add( self.m_btnDelete, 0, 0, 5 )
        
        self.m_btnType = wx.Button( self, wx.ID_ANY, u"类型", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnType.SetMinSize( wx.Size( 50,50 ) )
        
        m_topSizer.Add( self.m_btnType, 0, 0, 5 )
        
        self.m_btnUnit = wx.Button( self, wx.ID_ANY, u"单位", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnUnit.SetMinSize( wx.Size( 50,50 ) )
        
        m_topSizer.Add( self.m_btnUnit, 0, 0, 5 )
        
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
        
        m_bottonSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        m_leftSizer = wx.BoxSizer( wx.VERTICAL )
        
        m_leftSizer.SetMinSize( wx.Size( 200,600 ) ) 
        self.m_treeCtrl = wx.TreeCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
        self.m_treeCtrl.SetMinSize( wx.Size( -1,600 ) )
        
        m_leftSizer.Add( self.m_treeCtrl, 0, wx.EXPAND, 5 )
        
        
        m_bottonSizer.Add( m_leftSizer, 1, 0, 5 )
        
        m_rightSizer = wx.BoxSizer( wx.VERTICAL )
        
        m_rightSizer.SetMinSize( wx.Size( 600,600 ) ) 
        self.m_dataViewList = wx.dataview.DataViewCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,600 ), 0 )
        
        # Create an instance of our model...
        self.model = CModelDishes(CDataDishesInfo.GetData())
        CDataDishesInfo.RefreshItems()
        
        # Tel the DVC to use the model
        self.m_dataViewList.AssociateModel(self.model)
        
        self.m_dataViewColumn = self.m_dataViewList.AppendTextColumn( u"行号", 0 ) 
        self.m_dataViewCode = self.m_dataViewList.AppendTextColumn( u"品码", 1 ) 
        self.m_dataViewName = self.m_dataViewList.AppendTextColumn( u"品名", 2 ) 
        self.m_dataViewBrevityCode = self.m_dataViewList.AppendTextColumn( u"拼音简码", 3 ) 
        self.m_dataViewSpec = self.m_dataViewList.AppendTextColumn( u"规格", 4 ) 
        self.m_dataViewSpec = self.m_dataViewList.AppendTextColumn( u"做法", 5 ) 
        self.m_dataViewType = self.m_dataViewList.AppendTextColumn( u"所属类", 6 ) 
        self.m_dataViewUnit = self.m_dataViewList.AppendTextColumn( u"单位", 7 ) 
        self.m_dataViewPrice = self.m_dataViewList.AppendTextColumn( u"售价", 8 ) 
        self.m_dataViewPrice = self.m_dataViewList.AppendToggleColumn( u"停用", 9 ) 
        m_rightSizer.Add( self.m_dataViewList, 0, wx.EXPAND|wx.LEFT, 5 )
        
        
        m_bottonSizer.Add( m_rightSizer, 1, 0, 5 )
        
        
        m_sizer.Add( m_bottonSizer, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( m_sizer )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.Bind( wx.EVT_SIZE, self.OnSize )
        
        self.m_btnNew.Bind( wx.EVT_BUTTON, self.OnNew )
        self.m_btnModify.Bind( wx.EVT_BUTTON, self.OnModify )
        self.m_btnDelete.Bind( wx.EVT_BUTTON, self.OnDelete )
        self.m_btnType.Bind( wx.EVT_BUTTON, self.OnType )
        self.m_btnUnit.Bind( wx.EVT_BUTTON, self.OnUnit )
        self.m_btnRefresh.Bind( wx.EVT_BUTTON, self.OnRefresh )
        self.m_btnExit.Bind( wx.EVT_BUTTON, self.OnExit )
        
        # Show tree ctrl
        self.ShowTreeCtrl()
    
    def __del__( self ):
        pass
    
    def Initailize(self):
        # Add event listenner
        CEvtManager.AddListenner(self, CEnumEvent.EVT_DISHES_PUBLISH_REFRESH, self.OnRefresh)
        
        x, y = CDataDeskTop.GetFrameSize()        
        self.SetSize(wx.Size(x, y))

    def Uninitailize(self):
        # Remove event listenner
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
    
    def RefreshUI(self):
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
    
    # Virtual event handlers, overide them in your derived class
    def OnSize( self, event ):
        event.Skip()
        x, y = self.GetSize()
        
        self.m_btnNew.SetMaxSize(wx.Size( 50,50 ))
        self.m_btnModify.SetMaxSize(wx.Size( 50,50 ))
        self.m_btnDelete.SetMaxSize(wx.Size( 50,50 ))
        self.m_btnType.SetMaxSize(wx.Size( 50,50 ))
        self.m_btnUnit.SetMaxSize(wx.Size( 50,50 ))
        self.m_btnRefresh.SetMaxSize(wx.Size( 50,50 ))
        self.m_btnExit.SetMaxSize(wx.Size( 50,50 ))
        self.m_topPanel.SetMaxSize( wx.Size( x-350,50 ) ) 
        self.m_treeCtrl.SetMinSize( wx.Size( 200,y-50 ) )
        self.m_dataViewList.SetMinSize( wx.Size( x-200,y-50 ) )
        
    def OnNew( self, event ):
        event.Skip()
        self.popDishesInfo = CPopDishesInfo(self, "add")
        self.popDishesInfo.ShowModal()
    
    def OnModify( self, event ):
        event.Skip()
        item = self.m_dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        index = self.model.data.index(data)
        CDataDishesInfo.SetCurItemIndex(index)
        self.popDishesInfo = CPopDishesInfo(self, "mod")
        self.popDishesInfo.ShowModal()
    
    def OnDelete( self, event ):
        event.Skip()
        item = self.m_dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        self.model.data.remove(data)
        self.m_dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
        CDataDishesInfo.DeleteItem(data)
    
    def OnType( self, event ):
        event.Skip()
        self.popCategory = CPopCategorySetting(self)
        self.popCategory.ShowModal()
    
    def OnUnit( self, event ):
        event.Skip()
        self.popUnit = CPopUnitSetting(self)
        self.popUnit.ShowModal()
    
    def OnRefresh( self, event ):
        event.Skip()
        self.RefreshUI()
    
    def OnExit( self, event ):
        event.Skip()
        CAppManager.SwitchToApplication('DeskTop')
    
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = CWgtDishesPublish(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()