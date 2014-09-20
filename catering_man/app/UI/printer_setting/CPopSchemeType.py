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
from wx.dataview import DataViewColumn
from app.logic.printer_setting.CDataSchemeType import CDataSchemeType, CDataSchemeTypeInfo
from app.logic.printer_setting.CModelSchemeType import CModelSchemeType

###########################################################################
## Class CPopSchemeType
###########################################################################

class CPopSchemeType ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"厨打单类型", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.CAPTION|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.Size( -1,-1 ), wx.Size( -1,-1 ) )
        
        m_sizer = wx.BoxSizer( wx.VERTICAL )
        
        m_topSizer = wx.BoxSizer( wx.VERTICAL )
        
        self.m_dataViewList = wx.dataview.DataViewCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_dataViewList.SetMinSize( wx.Size( 600,300 ) )
        
        # Create an instance of our model...
        self.model = CModelSchemeType(CDataSchemeTypeInfo.GetData())
        
        # Tel the DVC to use the model
        self.m_dataViewList.AssociateModel(self.model)
        
        self.m_dataViewListLine = self.m_dataViewList.AppendTextColumn( u"行号", 0) 
        self.m_dataViewListCode = self.m_dataViewList.AppendTextColumn( u"编码", 1, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE ) 
        self.m_dataViewListName = self.m_dataViewList.AppendTextColumn( u"单类名称", 2, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE ) 
        m_topSizer.Add( self.m_dataViewList, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        m_sizer.Add( m_topSizer, 1, wx.EXPAND, 5 )
        
        m_bottomSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_btnNew = wx.Button( self, wx.ID_ANY, u"新增", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_bottomSizer.Add( self.m_btnNew, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.m_btnDelete = wx.Button( self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_bottomSizer.Add( self.m_btnDelete, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        
        m_bottomSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_btnRefresh = wx.Button( self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_bottomSizer.Add( self.m_btnRefresh, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.m_btnSave = wx.Button( self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_bottomSizer.Add( self.m_btnSave, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.m_btnExit = wx.Button( self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_bottomSizer.Add( self.m_btnExit, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        
        m_sizer.Add( m_bottomSizer, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( m_sizer )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_btnNew.Bind( wx.EVT_BUTTON, self.OnBtnNew )
        self.m_btnDelete.Bind( wx.EVT_BUTTON, self.OnBtnDelete )
        self.m_btnRefresh.Bind( wx.EVT_BUTTON, self.OnBtnRefresh )
        self.m_btnSave.Bind( wx.EVT_BUTTON, self.OnBtnSave )
        self.m_btnExit.Bind( wx.EVT_BUTTON, self.OnBtnExit )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def OnBtnNew( self, event ):
        event.Skip()
        CDataSchemeTypeInfo.AddItem(CDataSchemeType(0, 0, ""))
        
        data = CDataSchemeType(CDataSchemeTypeInfo.GetDataLen() + 1, CDataSchemeTypeInfo.GetId(), "")
        self.model.data.append(data)
        item = self.model.ObjectToItem(data)
        self.m_dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
    
    def OnBtnDelete( self, event ):
        event.Skip()
        item = self.m_dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        self.model.data.remove(data)
        self.m_dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
        CDataSchemeTypeInfo.DeleteItem(data)
    
    def OnBtnRefresh( self, event ):
        event.Skip()
        
        result = CDataSchemeTypeInfo.GetData()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.m_dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
                    
        self.model.Cleared()
    
    def OnBtnSave( self, event ):
        event.Skip()
        item = self.m_dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        CDataSchemeTypeInfo.UpdateItem(data)
    
    def OnBtnExit( self, event ):
        event.Skip()
        self.Close()


if __name__ == '__main__':
    app = wx.PySimpleApp()
    dlg = CPopSchemeType(None)
    dlg.Show()
    #dlg.Center()
    app.MainLoop()
