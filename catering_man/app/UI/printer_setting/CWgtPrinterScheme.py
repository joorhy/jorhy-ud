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
from framework.CEvtManager import CEvtManager
from app.logic.CEnumEvent import CEnumEvent

###########################################################################
## Class CWgtPrinterScheme
###########################################################################

class CWgtPrinterScheme ( wx.Panel ):
    
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.Size( -1,-1 ), wx.DefaultSize )
        
        m_sizer = wx.BoxSizer( wx.VERTICAL )
        
        m_topSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        m_topSizer.SetMinSize( wx.Size( -1,50 ) ) 
        self.m_btnNew = wx.Button( self, wx.ID_ANY, u"新增", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
        m_topSizer.Add( self.m_btnNew, 0, 0, 5 )
        
        self.m_btnModify = wx.Button( self, wx.ID_ANY, u"修改", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
        m_topSizer.Add( self.m_btnModify, 0, 0, 5 )
        
        self.m_btnDelete = wx.Button( self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
        m_topSizer.Add( self.m_btnDelete, 0, 0, 5 )
        
        self.m_btnSchemeType = wx.Button( self, wx.ID_ANY, u"单类", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
        m_topSizer.Add( self.m_btnSchemeType, 0, 0, 5 )
        
        self.m_btnRefresh = wx.Button( self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
        m_topSizer.Add( self.m_btnRefresh, 0, 0, 5 )
        
        self.m_btnExit = wx.Button( self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.Size( 50,50 ), 0 )
        m_topSizer.Add( self.m_btnExit, 0, 0, 5 )
        
        self.m_topPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
        self.m_topPanel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        self.m_topPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        self.m_topPanel.SetMaxSize( wx.Size( -1,50 ) )
        
        m_topSizer.Add( self.m_topPanel, 1, wx.EXPAND, 5 )
        
        
        m_sizer.Add( m_topSizer, 1, wx.EXPAND, 5 )
        
        m_bottomSizer = wx.BoxSizer( wx.VERTICAL )
        
        m_bottomSizer.SetMinSize( wx.Size( 800,600 ) ) 
        self.m_dataViewList = wx.dataview.DataViewCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 800,600 ), 0 )
        
        # Create an instance of our model...
        self.model = CModelPrinterScheme(CDataPrinterSchemeInfo.GetData())
        CDataPrinterSchemeInfo.RefreshItems()
        
        # Tel the DVC to use the model
        self.m_dataViewList.AssociateModel(self.model)
        
        self.m_dataViewListLine = self.m_dataViewList.AppendTextColumn( u"行号", 0 ) 
        self.m_dataViewListCode = self.m_dataViewList.AppendTextColumn( u"编号", 1 ) 
        self.m_dataViewListName = self.m_dataViewList.AppendTextColumn( u"方案名称", 2 ) 
        self.m_dataViewListValid = self.m_dataViewList.AppendToggleColumn( u"生效", 3, width=50 ) 
        self.m_dataViewListType = self.m_dataViewList.AppendTextColumn( u"单据类型", 4 ) 
        self.m_dataViewListPrintNum = self.m_dataViewList.AppendTextColumn( u"厨打分数", 5 ) 
        self.m_dataViewListPrintNum = self.m_dataViewList.AppendTextColumn( u"后备方案", 6 )  
        m_bottomSizer.Add( self.m_dataViewList, 0, 0, 5 )
        
        
        m_sizer.Add( m_bottomSizer, 1, 0, 5 )
        
        
        self.SetSizer( m_sizer )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.Bind( wx.EVT_SIZE, self.OnSize )
        
        self.m_btnNew.Bind( wx.EVT_BUTTON, self.OnBtnNew )
        self.m_btnModify.Bind( wx.EVT_BUTTON, self.OnBtnModify )
        self.m_btnDelete.Bind( wx.EVT_BUTTON, self.OnBtnDelete )
        self.m_btnSchemeType.Bind( wx.EVT_BUTTON, self.OnBtnSchemetype )
        self.m_btnRefresh.Bind( wx.EVT_BUTTON, self.OnBtnRefresh )
        self.m_btnExit.Bind( wx.EVT_BUTTON, self.OnBtnExit )
    
    def __del__( self ):
        pass
    
    def Initailize(self):
        # Add event listenner
        CEvtManager.AddListenner(self, CEnumEvent.EVT_PRINTER_SCHEME_REFRESH, self.OnBtnRefresh)
        
        x, y = CDataDeskTop.GetFrameSize()       
        self.SetSize(wx.Size(x, y))

    def Uninitailize(self):
        # Add event listenner
        CEvtManager.RemoveListenner(self, CEnumEvent.EVT_PRINTER_SCHEME_REFRESH, self.OnBtnRefresh)
    
    def RefreshUI(self):        
        # Refresh dataviewlist
        CDataPrinterSchemeInfo.RefreshItems()
        result = CDataPrinterSchemeInfo.GetData()
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
        self.m_btnSchemeType.SetMaxSize(wx.Size( 50,50 ))
        self.m_btnRefresh.SetMaxSize(wx.Size( 50,50 ))
        self.m_btnExit.SetMaxSize(wx.Size( 50,50 ))
        self.m_topPanel.SetMaxSize( wx.Size( x-300,50 ) ) 
        self.m_dataViewList.SetMinSize( wx.Size( x,y-50 ) )
        
    def OnBtnNew( self, event ):
        event.Skip()
        self.popPrinterScheme = CPopPrinterScheme(self, "add")
        self.popPrinterScheme.ShowModal()
    
    def OnBtnModify( self, event ):
        event.Skip()
        item = self.m_dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        index = self.model.data.index(data)
        CDataPrinterSchemeInfo.SetCurItemIndex(index)
        self.popPrinterScheme = CPopPrinterScheme(self, "mod")
        self.popPrinterScheme.ShowModal()
    
    def OnBtnDelete( self, event ):
        event.Skip()
        item = self.m_dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        self.model.data.remove(data)
        self.m_dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
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