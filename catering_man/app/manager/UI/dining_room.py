#!/usr/bin/env python
# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
from app.manager.logic.data import * 
from app.manager.logic.ctrl import * 
from app.manager.logic.model import *
from app.manager.AppManager import AppManager

import wx
import wx.xrc
import wx.dataview
from wx.dataview import DataViewColumn

###########################################################################
## Class CPopAreaSetting
###########################################################################

class PopAreaSetting (wx.Dialog):
    def _init_view_sizer(self, parent):
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Create data view list
        self.dataViewList = wx.dataview.DataViewCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.dataViewList.SetMinSize(wx.Size(600, 300))  
        # Add data view items
        self.dataViewList.AppendTextColumn(u"行号", 0) 
        self.dataViewList.AppendTextColumn(u"编码", 1, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE) 
        self.dataViewList.AppendTextColumn(u"区域名称", 2, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE) 
        sizer.Add(self.dataViewList, 0, wx.ALL|wx.EXPAND, 5)

        # Layout data view 
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_ctrl_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # Add new button
        self.btnNew = wx.Button(self, wx.ID_ANY, u"新增", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnNew, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        # Add delete button
        self.btnDelete = wx.Button(self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnDelete, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        # Add spacer
        sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        # Add refresh button
        self.btnRefresh = wx.Button(self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnRefresh, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        # Add save button
        self.btnSave = wx.Button(self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnSave, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnExit, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        # Layout control buttons
        parent.Add(sizer, 1, wx.EXPAND, 5)
        
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"区域设置", pos=wx.DefaultPosition, size=wx.Size(600, 400), style=wx.CAPTION|wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.Size(-1, -1), wx.Size(-1, -1))

        sizer = wx.BoxSizer(wx.VERTICAL)

        self._init_view_sizer(sizer)
        self._init_ctrl_sizer(sizer)

        # Create an instance of our model...
        self.model = ModelArea(CtrlArea.GetData())

        # Tell the DVC to use the model
        self.dataViewList.AssociateModel(self.model)

        # Layout user interface
        self.SetSizer(sizer)
        self.Layout()
        self.Centre( wx.BOTH )

        # Connect Events
        self.btnNew.Bind(wx.EVT_BUTTON, self.OnBtnNew)
        self.btnDelete.Bind(wx.EVT_BUTTON, self.OnBtnDelete)
        self.btnRefresh.Bind(wx.EVT_BUTTON, self.OnBtnRefresh)
        self.btnSave.Bind(wx.EVT_BUTTON, self.OnBtnSave)
        self.btnExit.Bind(wx.EVT_BUTTON, self.OnBtnExit)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def OnBtnNew(self, event):
        event.Skip()
        CtrlArea.AddItem(DataArea(0, 0, ""))

        data = DataArea(CtrlArea.GetDataLen() + 1, CtrlArea.GetId(), "")
        self.model.data.append(data)
        item = self.model.ObjectToItem(data)
        self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)

    def OnBtnDelete(self, event):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        self.model.data.remove(data)
        self.dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
        CtrlArea.DeleteItem(data)

    def OnBtnRefresh(self, event):
        event.Skip()
        result = CtrlArea.GetData()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)

        self.model.Cleared()

    def OnBtnSave(self, event):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        CtrlArea.UpdateItem(data)

    def OnBtnExit(self, event):
        event.Skip()
        self.Close()

###########################################################################
## Class CPopMinexpenseSetting
###########################################################################

class PopMinexpenseSetting(wx.Dialog):
    def _init_view_sizer(self, parent):
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Create data view list
        self.dataViewList = wx.dataview.DataViewCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.dataViewList.SetMinSize(wx.Size(600, 300))

        # Add data view items
        self.dataViewList.AppendTextColumn(u"行号", 0) 
        self.dataViewList.AppendTextColumn(u"编码", 1, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE) 
        self.dataViewList.AppendTextColumn(u"消费名称", 2, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE) 
        self.dataViewList.AppendTextColumn(u"消费金额", 3, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE) 
        sizer.Add(self.dataViewList, 0, wx.ALL|wx.EXPAND, 5)

        # Layout data view
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_ctrl_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Add new button
        self.btnNew = wx.Button(self, wx.ID_ANY, u"新增", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnNew, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        # Add delete button
        self.btnDelete = wx.Button(self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnDelete, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        # Add spacer
        sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        # Add refresh button
        self.btnRefresh = wx.Button(self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnRefresh, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        # Add save button
        self.btnSave = wx.Button(self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnSave, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add( self.btnExit, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        # Layout control 
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"最低消费类型设置", pos=wx.DefaultPosition, size=wx.Size(600, 400), style=wx.CAPTION|wx.TAB_TRAVERSAL)
        
        self.SetSizeHintsSz(wx.Size(-1, -1), wx.Size(-1, -1))
        sizer = wx.BoxSizer(wx.VERTICAL)

        self._init_view_sizer(sizer)
        self._init_ctrl_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Create an instance of our model...
        self.model = ModelMinexpense(CtrlMinexpense.GetData())
        
        # Tell the DVC to use the model
        self.dataViewList.AssociateModel(self.model)
        
        # Connect Events
        self.btnNew.Bind(wx.EVT_BUTTON, self.OnBtnNew)
        self.btnDelete.Bind(wx.EVT_BUTTON, self.OnBtnDelete)
        self.btnRefresh.Bind(wx.EVT_BUTTON, self.OnBtnRefresh)
        self.btnSave.Bind(wx.EVT_BUTTON, self.OnBtnSave)
        self.btnExit.Bind(wx.EVT_BUTTON, self.OnBtnExit)
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, override them in your derived class
    def OnBtnNew( self, event ):
        event.Skip()
        CtrlMinexpense.AddItem(DataMinexpense(0, 0, "", 0))
        
        data = DataMinexpense(CtrlMinexpense.GetDataLen() + 1, CtrlMinexpense.GetId(), "", 0)
        self.model.data.append(data)
        item = self.model.ObjectToItem(data)
        self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
    
    def OnBtnDelete( self, event ):
        event.Skip()
        item = self.m_dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        self.model.data.remove(data)
        self.dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
        CtrlMinexpense.DeleteItem(data)
    
    def OnBtnRefresh( self, event ):
        event.Skip()
        result = CtrlMinexpense.GetData()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
                    
        self.model.Cleared()
    
    def OnBtnSave( self, event ):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        CtrlMinexpense.UpdateItem(data)
    
    def OnBtnExit( self, event ):
        event.Skip()
        self.Close()

###########################################################################
## Class CPopTableBatAdd
###########################################################################

class PopTableBatAdd (wx.Dialog):
    def _init_view_sizer(self, parent):
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Create grid sizer for 1 row and 2 column
        gSizer = wx.GridSizer(1, 2, 0, 0)
        
        # Column 1 is another grid sizer for 4 rows and 2 column
        gSizerLeft = wx.GridSizer(4, 2, 0, 0)
        # Add label for code prefix
        sTxtCodePre = wx.StaticText(self, wx.ID_ANY, u"编号前缀：", wx.DefaultPosition, wx.DefaultSize, 0)
        sTxtCodePre.Wrap(-1)
        gSizerLeft.Add(sTxtCodePre, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add text for code prefix
        self.txtCodePre = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizerLeft.Add(self.txtCodePre, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add label for from
        sTxtFrom = wx.StaticText(self, wx.ID_ANY, u"从：", wx.DefaultPosition, wx.DefaultSize, 0)
        sTxtFrom.Wrap(-1)
        gSizerLeft.Add(sTxtFrom, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add text for from
        self.txtFrom = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizerLeft.Add(self.txtFrom, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add label for area
        sTxtArea = wx.StaticText(self, wx.ID_ANY, u"区域：", wx.DefaultPosition, wx.DefaultSize, 0)
        sTxtArea.Wrap(-1)
        gSizerLeft.Add(sTxtArea, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add combo box for area
        cbxAreaChoices = list()
        self.cbxArea = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, cbxAreaChoices, 0)
        gSizerLeft.Add(self.cbxArea, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add label for consumer type 
        sTxtContype = wx.StaticText(self, wx.ID_ANY, u"消费类型：", wx.DefaultPosition, wx.DefaultSize, 0)
        sTxtContype.Wrap(-1)
        gSizerLeft.Add(sTxtContype, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add combo box for consumer type 
        cbxMinExpenseChoices = list()
        self.cbxMinExpense = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, cbxMinExpenseChoices, 0)
        gSizerLeft.Add(self.cbxMinExpense, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Layout column 1
        gSizer.Add(gSizerLeft, 1, wx.EXPAND, 5)
        
        # Column 2 is another grid sizer for 4 rows and 2 columns
        gSizerRight = wx.GridSizer(4, 2, 0, 0)
        # Add spacer
        gSizerRight.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        gSizerRight.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        # Add label for to
        sTxtTo = wx.StaticText(self, wx.ID_ANY, u"到：", wx.DefaultPosition, wx.DefaultSize, 0)
        sTxtTo.Wrap(-1)
        gSizerRight.Add(sTxtTo, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add text control for to
        self.txtTo = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizerRight.Add(self.txtTo, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add label for dining table type
        sTxtTableType = wx.StaticText(self, wx.ID_ANY, u"餐桌类型：", wx.DefaultPosition, wx.DefaultSize, 0)
        sTxtTableType.Wrap(-1)
        gSizerRight.Add(sTxtTableType, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add combo box for dining table type
        cbxTypeChoices = list()
        self.cbxType = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, cbxTypeChoices, 0)
        gSizerRight.Add(self.cbxType, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add label for people number
        sTxtPepleNum = wx.StaticText(self, wx.ID_ANY, u"人数：", wx.DefaultPosition, wx.DefaultSize, 0)
        sTxtPepleNum.Wrap( -1 )
        gSizerRight.Add(sTxtPepleNum, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add text control for people number
        self.txtPepleNum = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizerRight.Add(self.txtPepleNum, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Layout column 2
        gSizer.Add(gSizerRight, 1, wx.EXPAND, 5)
        
        # Layout data view
        sizer.Add(gSizer, 1, wx.EXPAND, 5)
        parent.Add(sizer, 1, wx.EXPAND, 5)
        
    def _init_ctrl_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add spacer
        sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        # Add create button
        self.btnCreate = wx.Button(self, wx.ID_ANY, u"生成", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnCreate, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnExit, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Layout control 
        parent.Add(sizer, 1, wx.EXPAND, 5)
        
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"批量生成餐桌", pos=wx.DefaultPosition, size=wx.Size(480, 220), style=wx.CAPTION)
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        sizer = wx.BoxSizer( wx.VERTICAL )
        
        self._init_view_sizer(sizer)
        self._init_ctrl_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.btnCreate.Bind(wx.EVT_BUTTON, self.OnBtnCreate)
        self.btnExit.Bind(wx.EVT_BUTTON, self.OnBtnExit)

        # Initialize data on view list
        self.InitailizeView()

    def __del__( self ):
        pass

    def InitailizeView(self):
        li_area = CtrlArea.GetData()
        for area in li_area:
            self.cbxArea.Append(area.name, area)
        self.cbxArea.SetSelection(0)

        li_table_type = CtrlType.GetData()
        for table_type in li_table_type:
            self.cbxType.Append(table_type.name, table_type)
        self.cbxType.SetSelection(0)

        li_min_expense = CtrlTable.GetData()
        for min_expense in li_min_expense:
            self.cbxMinExpense.Append(min_expense.name, min_expense)
        self.cbxMinExpense.SetSelection(0)

    # Virtual event handlers, override them in your derived class
    def OnBtnCreate( self, event ):
        event.Skip()
        area = self.cbxArea.GetClientData(self.cbxArea.GetSelection())
        table_type = self.cbxType.GetClientData(self.cbxType.GetSelection())
        min_expense = self.cbxMinExpense.GetClientData(self.cbxMinExpense.GetSelection())
        i_from = int(self.txtFrom.GetValue())
        i_to = int(self.txtTo.GetValue())
        i_peple_num = int(self.txtPepleNum.GetValue())
        table_items = list()
        for index in range(i_from, i_to + 1):
            table_items.append(DataTable(0, 0, ("餐桌%d" % index), table_type.code, area.code, i_peple_num, min_expense.code))

        CtrlTable.AddItems(table_items)

    def OnBtnExit( self, event ):
        event.Skip()
        self.Close()

###########################################################################
## Class CPopTableInfo
###########################################################################

class PopTableInfo (wx.Dialog):
    def _init_view_sizer(self, parent):
        panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(600, 200), wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL)
        # Create a grid sizer with 1 row and 2 columns
        gSizer = wx.GridSizer(1, 2, 0, 0)
        gSizer.SetMinSize(wx.Size(600, 200)) 

        # Column 1 also is a grid sizer with 3 rows and 2 columns
        gSizerLeft = wx.GridSizer(3, 2, 0, 0)
        # Add label for dining table code 
        sTxtTableCode = wx.StaticText(panel, wx.ID_ANY, u"餐桌编码：", wx.Point( -1,-1 ), wx.DefaultSize, 0)
        sTxtTableCode.Wrap(-1)
        gSizerLeft.Add(sTxtTableCode, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add text control for dining table code 
        self.txtCode = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(120, -1), 0)
        gSizerLeft.Add(self.txtCode, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add label for dining table type
        sTxtTableType = wx.StaticText(panel, wx.ID_ANY, u"所属类型：", wx.DefaultPosition, wx.DefaultSize, 0)
        sTxtTableType.Wrap(-1)
        gSizerLeft.Add(sTxtTableType, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add combo box for dining table type
        cbxTypeChoices = list()
        self.cbxType = wx.ComboBox(panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(120, -1), cbxTypeChoices, 0)
        gSizerLeft.Add(self.cbxType, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add label for people number
        sTxtPepleNum = wx.StaticText(panel, wx.ID_ANY, u"人数：", wx.DefaultPosition, wx.DefaultSize, 0)
        sTxtPepleNum.Wrap( -1 )
        gSizerLeft.Add(sTxtPepleNum, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add text control for people number
        self.txtPeple = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(120, -1), 0)
        gSizerLeft.Add(self.txtPeple, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Layout column 1
        gSizer.Add(gSizerLeft, 1, wx.EXPAND, 5)
        
        # Column 2 also is a grid sizer with 3 rows and 2 columns
        gSizerRight = wx.GridSizer(3, 2, 0, 0)
        # Add label for dining table name 
        sTxtTalbeName = wx.StaticText(panel, wx.ID_ANY, u"餐桌名称：", wx.DefaultPosition, wx.DefaultSize, 0)
        sTxtTalbeName.Wrap(-1)
        gSizerRight.Add(sTxtTalbeName, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add text control for dining table name 
        self.txtName = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(120,-1), 0)
        gSizerRight.Add(self.txtName, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add label for dining table area 
        sTxtTableArea = wx.StaticText(panel, wx.ID_ANY, u"所属区域：", wx.DefaultPosition, wx.DefaultSize, 0)
        sTxtTableArea.Wrap(-1)
        gSizerRight.Add(sTxtTableArea, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add combo box for dining table area 
        cbxAreaChoices = list()
        self.cbxArea = wx.ComboBox(panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(120,-1), cbxAreaChoices, 0)
        gSizerRight.Add(self.cbxArea, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add label for consumer type 
        sTxtContype = wx.StaticText(panel, wx.ID_ANY, u"消费类型：", wx.DefaultPosition, wx.DefaultSize, 0)
        sTxtContype.Wrap(-1)
        gSizerRight.Add(sTxtContype, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add combo box for consumer type 
        cbxMinExpenseChoices = list()
        self.cbxMinExpense = wx.ComboBox(panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(120,-1), cbxMinExpenseChoices, 0)
        gSizerRight.Add(self.cbxMinExpense, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Layout column 2
        gSizer.Add(gSizerRight, 1, wx.EXPAND, 5)
        
        # Layout data view
        panel.SetSizer(gSizer)
        panel.Layout()
        parent.Add(panel, 1, wx.EXPAND |wx.ALL, 5)
        
    def _init_ctrl_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # Add static text for track
        self.txtTrack = wx.StaticText(self, wx.ID_ANY, u"1 / 1 ", wx.DefaultPosition, wx.Size(80,-1), wx.ALIGN_CENTRE)
        self.txtTrack.Wrap(-1)
        sizer.Add(self.txtTrack, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add previous record button
        self.btnPrev = wx.Button(self, wx.ID_ANY, u"上一记录", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnPrev, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add next record button
        self.btnNext = wx.Button(self, wx.ID_ANY, u"下一记录", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnNext, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add spacer
        sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        # Add save button
        self.btnSave = wx.Button(self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnSave, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnExit, 0, wx.ALIGN_CENTER|wx.ALL, 5)

        # Layout control buttons
        parent.Add(sizer, 1, wx.EXPAND, 5)
        
    def __init__(self, parent, type_):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"餐桌资料设置", pos=wx.DefaultPosition, size=wx.Size(600, 300), style=wx.CAPTION|wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        sizer = wx.BoxSizer(wx.VERTICAL)

        self._init_view_sizer(sizer)
        self._init_ctrl_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.btnPrev.Bind(wx.EVT_BUTTON, self.OnBtnPrev)
        self.btnNext.Bind(wx.EVT_BUTTON, self.OnBtnNext)
        self.btnSave.Bind(wx.EVT_BUTTON, self.OnBtnSave)
        self.btnExit.Bind(wx.EVT_BUTTON, self.OnBtnExit)

        # Initialize data view
        self.index = 0
        self.type = type_
        self.InitailizeView()

    def __del__( self ):
        pass

    def InitailizeView(self):
        if self.type == "add":
            self.InitAddView()
        elif self.type == "mod":
            self.index = CtrlTable.GetCurItemIndex()
            self.InitModView()

    def InitAddView(self):
        li_area = CtrlArea.GetData()
        for area in li_area:
            self.cbxArea.Append(area.name, area)
        self.cbxArea.SetSelection(0)

        li_table_type = CtrlType.GetData()
        for table_type in li_table_type:
            self.cbxType.Append(table_type.name, table_type)
        self.cbxType.SetSelection(0)

        li_min_expense = CtrlMinexpense.GetData()
        for min_expense in li_min_expense:
            self.cbxMinExpense.Append(min_expense.name, min_expense)
        self.cbxMinExpense.SetSelection(0)

        self.txtTrack.Enable(False)
        self.btnPrev.Enable(False)
        self.btnNext.Enable(False)

    def InitModView(self):
        self.txtCode.Enable(False) 
        if self.index < 0:
            self.index = 0
            return

        items = CtrlTable.GetItems()
        if self.index >= len(items):
            self.index = len(items) - 1
            return

        data = items[self.index]
        self.txtCode.SetValue(str(data.code))
        self.txtName.SetValue(data.name)
        self.txtPeple.SetValue(str(data.peple_num))
        self.txtTrack.SetLabel(("%d / %d" % (self.index+1, len(items))))

        li_area = CtrlArea.GetData()
        area_selection = 0
        for area in li_area:
            self.cbxArea.Append(area.name, area)
            if area.code == data.area:
                self.cbxArea.SetSelection(area_selection)
            area_selection += 1

        li_table_type = CtrlType.GetData()
        table_type_selection = 0
        for table_type in li_table_type:
            self.cbxType.Append(table_type.name, table_type)
            if table_type.code == data.table_type:
                self.cbxType.SetSelection(table_type_selection)
            table_type_selection += 1

        li_min_expense = CtrlMinexpense.GetData()
        min_expense_selection = 0
        for min_expense in li_min_expense:
            self.cbxMinExpense.Append(min_expense.name, min_expense)
            if min_expense.code == data.min_type:
                self.cbxMinExpense.SetSelection(min_expense_selection)
            min_expense_selection += 1

    # Virtual event handlers, override them in your derived class        
    def OnBtnPrev( self, event ):
        event.Skip()
        self.index -= 1
        self.InitModView()

    def OnBtnNext( self, event ):
        event.Skip()
        self.index += 1
        self.InitModView()

    def OnBtnSave( self, event ):
        event.Skip()
        area = self.cbxArea.GetClientData(self.cbxArea.GetSelection())
        type_ = self.cbxType.GetClientData(self.cbxType.GetSelection())
        min_expense = self.cbxMinExpense.GetClientData(self.cbxMinExpense.GetSelection())
        data = DataTable(0, 
                        int(self.txtCode.GetValue()), 
                        self.txtName.GetValue(), 
                        type_.code, 
                        area.code, 
                        int(self.txtPeple.GetValue()), 
                        min_expense.code)
        if self.type == "add":
            CtrlTable.AddItem(data)
        elif self.type == "mod":
            CtrlTable.UpdateItem(data)

    def OnBtnExit( self, event ):
        event.Skip()
        self.Close()

###########################################################################
## Class CPopTypeSetting
###########################################################################

class PopTypeSetting (wx.Dialog):
    def _init_view_sizer(self, parent):
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Create data view list 
        self.dataViewList = wx.dataview.DataViewCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.dataViewList.SetMinSize(wx.Size(600, 300))
        # Add items into data view list
        self.dataViewList.AppendTextColumn(u"行号", 0) 
        self.dataViewList.AppendTextColumn(u"编码", 1, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE) 
        self.dataViewList.AppendTextColumn(u"桌类名称", 2, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE) 
        sizer.Add(self.dataViewList, 0, wx.ALL|wx.EXPAND, 5)
        
        # Layout data view 
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_ctrl_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Add new button
        self.btnNew = wx.Button(self, wx.ID_ANY, u"新增", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnNew, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        # Add delete button
        self.btnDelete = wx.Button(self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnDelete, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        # Add spacer
        sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        # Add refresh button
        self.btnRefresh = wx.Button(self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnRefresh, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        # Add save button
        self.btnSave = wx.Button(self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnSave, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnExit, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        
        # Layout control buttons
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"桌类设置", pos=wx.DefaultPosition, size=wx.Size(600,400), style=wx.CAPTION|wx.TAB_TRAVERSAL) 
        self.SetSizeHintsSz(wx.Size(-1,-1), wx.Size(-1,-1))
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        self._init_view_sizer(sizer)
        self._init_ctrl_sizer(sizer)
        
        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Create an instance of our model...
        self.model = ModelType(CtrlType.GetData())
        # Tell the DVC to use the model
        self.dataViewList.AssociateModel(self.model)

        # Connect Events
        self.btnNew.Bind(wx.EVT_BUTTON, self.OnBtnNew)
        self.btnDelete.Bind(wx.EVT_BUTTON, self.OnBtnDelete)
        self.btnRefresh.Bind(wx.EVT_BUTTON, self.OnBtnRefresh)
        self.btnSave.Bind(wx.EVT_BUTTON, self.OnBtnSave)
        self.btnExit.Bind(wx.EVT_BUTTON, self.OnBtnExit)
    
    def __del__( self ):
        pass
       
    # Virtual event handlers, override them in your derived class
    def OnBtnNew( self, event ):
        event.Skip()
        CtrlType.AddItem(DataType(0, 0, ""))
        
        data = DataType(CtrlType.GetDataLen() + 1, CtrlType.GetId(), "")
        self.model.data.append(data)
        item = self.model.ObjectToItem(data)
        self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
    
    def OnBtnDelete( self, event ):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        self.model.data.remove(data)
        self.dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
        CtrlType.DeleteItem(data)
    
    def OnBtnRefresh( self, event ):
        event.Skip()
        result = CtrlType.GetData()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
                    
        self.model.Cleared()
    
    def OnBtnSave( self, event ):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        CtrlType.UpdateItem(data)
    
    def OnBtnExit( self, event ):
        event.Skip()
        self.Close()

###########################################################################
## Class CDiningTable
###########################################################################

class WgtDiningTable (wx.Panel):
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
        self.model = ModelTable(CtrlTable.GetData())
        CtrlTable.RefreshItems()
        
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
        EvtManager.AddListener(self, EnumEvent.EVT_DINING_ROOM_REFRESH, self.OnBtnRefresh)
        
        x, y = CtrlHomePage.GetFrameSize()
        self.SetSize(wx.Size(x, y))

    def Uninitailize(self):
        # Remove event listener
        EvtManager.RemoveListener(self, EnumEvent.EVT_DINING_ROOM_REFRESH, self.OnBtnRefresh)
    
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
        li_items = CtrlTable.GetItems()
        for item in li_items:
            if table_type_map.has_key(item.table_type):
                table_type_map[item.table_type].append(item)
            else:
                list_tmp = []
                list_tmp.append(item)
                table_type_map_tmp = {item.table_type:list_tmp}
                table_type_map.update(table_type_map_tmp)
        
        li_table_type = CtrlTable.GetData()
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
        CtrlTable.RefreshItems()
        self.treeCtrl.DeleteAllItems()
        self.ShowTreeCtrl()
        
        # Refresh data view list
        result = CtrlTable.GetData()
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
        self.popTableInfo = PopTableInfo(self, "add")
        self.popTableInfo.ShowModal()
    
    def OnBtnModify(self, event):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        index = self.model.data.index(data)
        CtrlTable.SetCurItemIndex(index)
        self.popTableInfo = PopTableInfo(self, "mod")
        self.popTableInfo.ShowModal()
    
    def OnBtnDelete(self, event):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        self.model.data.remove(data)
        self.dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
        CtrlTable.DeleteItem(data)
    
    def OnBtnBatAdd(self, event):
        event.Skip()
        self.popBatAdd = PopTableBatAdd(self)
        self.popBatAdd.ShowModal()
    
    def OnBtnTableType(self, event):
        event.Skip()
        self.popTableType = PopTypeSetting(self)
        self.popTableType.ShowModal()
    
    def OnBtnAreaSetting(self, event):
        event.Skip()
        self.popArea = PopAreaSetting(self)
        self.popArea.ShowModal()
        
    def OnBtnMinExpense(self, event):
        event.Skip()
        self.popMinExpense = PopMinexpenseSetting(self)
        self.popMinExpense.ShowModal()
    
    def OnBtnRefresh(self, event):
        event.Skip()
        self.RefreshUI()
    
    def OnBtnExit(self, event):
        event.Skip()
        CtrlHomePage.SetSelectedItem()
        AppManager.SwitchToApplication('HomePage')
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = WgtDiningTable(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()


