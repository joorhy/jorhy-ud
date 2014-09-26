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
from app.UI.printer_setting.CPopPrinterScheme import CPopPrinterScheme
from app.UI.printer_setting.CPopSchemeType import CPopSchemeType
from app.logic.printer_setting.CDataPrinterScheme import CDataPrinterSchemeInfo
from app.logic.printer_setting.CModelPrinterScheme import CModelPrinterScheme
from framework.core import EvtManager
from app.logic.CEnumEvent import CEnumEvent

###########################################################################
## Class CWgtPrinterScheme
###########################################################################

class CWgtPrinterScheme(wx.Panel):
    def _init_status_bar_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.SetMinSize(wx.Size(-1,50)) 
        # Add new button
        self.btnNew = wx.Button(self, wx.ID_ANY, u"新增", wx.DefaultPosition, wx.Size(50,50), 0)
        sizer.Add(self.btnNew, 0, 0, 5)
        # Add modify button
        self.btnModify = wx.Button(self, wx.ID_ANY, u"修改", wx.DefaultPosition, wx.Size(50,50), 0)
        sizer.Add(self.btnModify, 0, 0, 5)
        # Add delete button
        self.btnDelete = wx.Button(self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.Size(50,50), 0)
        sizer.Add(self.btnDelete, 0, 0, 5)
        # Add invoice type button
        self.btnSchemeType = wx.Button(self, wx.ID_ANY, u"单类", wx.DefaultPosition, wx.Size(50,50), 0)
        sizer.Add(self.btnSchemeType, 0, 0, 5)
        # Add refresh button
        self.btnRefresh = wx.Button(self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.Size(50,50), 0)
        sizer.Add(self.btnRefresh, 0, 0, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.Size(50,50), 0)
        sizer.Add(self.btnExit, 0, 0, 5)
        # Add fix space panel
        self.topPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL)
        self.topPanel.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
        self.topPanel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
        self.topPanel.SetMaxSize(wx.Size(-1,50))
        sizer.Add(self.topPanel, 1, wx.EXPAND, 5)
        
        # Layout status bar sizer
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_data_view_sizer(self, parent):
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.SetMinSize(wx.Size(800,600)) 
        # Create data view list
        self.dataViewList = wx.dataview.DataViewCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(800,600), 0)
        # Add items into data view list 
        self.dataViewList.AppendTextColumn(u"行号", 0) 
        self.dataViewList.AppendTextColumn(u"编号", 1) 
        self.dataViewList.AppendTextColumn(u"方案名称", 2) 
        self.dataViewList.AppendToggleColumn(u"生效", 3, width=50) 
        self.dataViewList.AppendTextColumn(u"单据类型", 4) 
        self.dataViewList.AppendTextColumn(u"厨打分数", 5) 
        self.dataViewList.AppendTextColumn(u"后备方案", 6)  
        sizer.Add(self.dataViewList, 0, 0, 5)
        
        # Layout data view list
        parent.Add(sizer, 1, 0, 5)

    def __init__( self, parent ):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(800,600), style=wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.Size(-1,-1), wx.DefaultSize)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_status_bar_sizer(sizer)
        self._init_data_view_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Create an instance of our model...
        self.model = CModelPrinterScheme(CDataPrinterSchemeInfo.GetData())
        CDataPrinterSchemeInfo.RefreshItems()
        
        # Tell the DVC to use the model
        self.dataViewList.AssociateModel(self.model)

        # Connect Events
        self.Bind( wx.EVT_SIZE, self.OnSize )
        
        self.btnNew.Bind(wx.EVT_BUTTON, self.OnBtnNew)
        self.btnModify.Bind(wx.EVT_BUTTON, self.OnBtnModify)
        self.btnDelete.Bind(wx.EVT_BUTTON, self.OnBtnDelete)
        self.btnSchemeType.Bind(wx.EVT_BUTTON, self.OnBtnSchemetype)
        self.btnRefresh.Bind(wx.EVT_BUTTON, self.OnBtnRefresh)
        self.btnExit.Bind(wx.EVT_BUTTON, self.OnBtnExit)
    
    def __del__( self ):
        pass
    
    def Initailize(self):
        # Add event listener
        EvtManager.AddListener(self, CEnumEvent.EVT_PRINTER_SCHEME_REFRESH, self.OnBtnRefresh)
        
        x, y = CDataDeskTop.GetFrameSize()       
        self.SetSize(wx.Size(x, y))

    def Uninitailize(self):
        # Add event listener
        EvtManager.RemoveListener(self, CEnumEvent.EVT_PRINTER_SCHEME_REFRESH, self.OnBtnRefresh)
    
    def RefreshUI(self):        
        # Refresh data view list
        CDataPrinterSchemeInfo.RefreshItems()
        result = CDataPrinterSchemeInfo.GetData()
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

        self.btnNew.SetMaxSize(wx.Size(50,50))
        self.btnModify.SetMaxSize(wx.Size(50,50))
        self.btnDelete.SetMaxSize(wx.Size(50,50))
        self.btnSchemeType.SetMaxSize(wx.Size(50,50))
        self.btnRefresh.SetMaxSize(wx.Size(50,50))
        self.btnExit.SetMaxSize(wx.Size(50,50))
        self.topPanel.SetMaxSize(wx.Size(x-300,50)) 
        self.dataViewList.SetMinSize(wx.Size(x,y-50))
        
    def OnBtnNew(self, event):
        event.Skip()
        self.popPrinterScheme = CPopPrinterScheme(self, "add")
        self.popPrinterScheme.ShowModal()
    
    def OnBtnModify(self, event):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        index = self.model.data.index(data)
        CDataPrinterSchemeInfo.SetCurItemIndex(index)
        self.popPrinterScheme = CPopPrinterScheme(self, "mod")
        self.popPrinterScheme.ShowModal()
    
    def OnBtnDelete( self, event ):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        self.model.data.remove(data)
        self.dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
        CDataPrinterSchemeInfo.DeleteItem(data)
        
    def OnBtnSchemetype( self, event ):
        event.Skip()  
        self.popSchemeType = CPopSchemeType(self)
        self.popSchemeType.ShowModal()  
    
    def OnBtnRefresh( self, event ):
        event.Skip()
        self.RefreshUI()
    
    def OnBtnExit( self, event ):
        event.Skip()
        CAppManager.SwitchToApplication('DeskTop')
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = CWgtPrinterScheme(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()
