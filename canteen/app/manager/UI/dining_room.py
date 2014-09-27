#!/usr/bin/env python
# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

from app.manager.logic.ctrl import * 
from app.manager.logic.model import *
from app.manager.logic.data import *
from app.manager.AppManager import AppManager

import wx
import wx.xrc
import wx.dataview
from wx.dataview import DataViewColumn

###########################################################################
## Class PopAreaSetting
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
        sizer.Add(self.dataViewList, 0, wx.ALL | wx.EXPAND, 5)

        # Layout data view 
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_ctrl_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # Add new button
        self.btnNew = wx.Button(self, wx.ID_ANY, u"新增", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnNew, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        # Add delete button
        self.btnDelete = wx.Button(self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnDelete, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        # Add spacer
        sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        # Add refresh button
        self.btnRefresh = wx.Button(self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnRefresh, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        # Add save button
        self.btnSave = wx.Button(self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnSave, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnExit, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        # Layout control buttons
        parent.Add(sizer, 1, wx.EXPAND, 5)
        
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"区域设置", pos=wx.DefaultPosition,
                           size=wx.Size(600, 400), style=wx.CAPTION | wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.Size(-1, -1), wx.Size(-1, -1))

        sizer = wx.BoxSizer(wx.VERTICAL)

        self._init_view_sizer(sizer)
        self._init_ctrl_sizer(sizer)

        # Create an instance of our model...
        self.model = ModelArea(CtrlArea.get_data())

        # Tell the DVC to use the model
        self.dataViewList.AssociateModel(self.model)

        # Layout user interface
        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.btnNew.Bind(wx.EVT_BUTTON, self.on_btn_new)
        self.btnDelete.Bind(wx.EVT_BUTTON, self.on_btn_delete)
        self.btnRefresh.Bind(wx.EVT_BUTTON, self.on_btn_refresh)
        self.btnSave.Bind(wx.EVT_BUTTON, self.on_btn_save)
        self.btnExit.Bind(wx.EVT_BUTTON, self.on_btn_exit)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def on_btn_new(self, event):
        event.Skip()
        CtrlArea.add_item(DataArea(0, 0, ""))

        data = DataArea(CtrlArea.get_data_len() + 1, CtrlArea.get_id(), "")
        self.model.data.append(data)
        item = self.model.ObjectToItem(data)
        self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)

    def on_btn_delete(self, event):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        self.model.data.remove(data)
        self.dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
        CtrlArea.delete_item(data)

    def on_btn_refresh(self, event):
        event.Skip()
        result = CtrlArea.get_data()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)

        self.model.Cleared()

    def on_btn_save(self, event):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        CtrlArea.update_item(data)

    def on_btn_exit(self, event):
        event.Skip()
        self.Close()

###########################################################################
## Class PopMinExpenseSetting
###########################################################################


class PopMinExpenseSetting(wx.Dialog):
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
        sizer.Add(self.dataViewList, 0, wx.ALL | wx.EXPAND, 5)

        # Layout data view
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_ctrl_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Add new button
        self.btnNew = wx.Button(self, wx.ID_ANY, u"新增", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnNew, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        # Add delete button
        self.btnDelete = wx.Button(self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnDelete, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        # Add spacer
        sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        # Add refresh button
        self.btnRefresh = wx.Button(self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnRefresh, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        # Add save button
        self.btnSave = wx.Button(self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnSave, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnExit, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        # Layout control 
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"最低消费类型设置", pos=wx.DefaultPosition,
                           size=wx.Size(600, 400), style=wx.CAPTION | wx.TAB_TRAVERSAL)
        
        self.SetSizeHintsSz(wx.Size(-1, -1), wx.Size(-1, -1))
        sizer = wx.BoxSizer(wx.VERTICAL)

        self._init_view_sizer(sizer)
        self._init_ctrl_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Create an instance of our model...
        self.model = ModelMinExpense(CtrlMinExpense.get_data())
        
        # Tell the DVC to use the model
        self.dataViewList.AssociateModel(self.model)
        
        # Connect Events
        self.btnNew.Bind(wx.EVT_BUTTON, self.on_btn_new)
        self.btnDelete.Bind(wx.EVT_BUTTON, self.on_btn_delete)
        self.btnRefresh.Bind(wx.EVT_BUTTON, self.on_btn_refresh)
        self.btnSave.Bind(wx.EVT_BUTTON, self.on_btn_save)
        self.btnExit.Bind(wx.EVT_BUTTON, self.on_btn_exit)
    
    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def on_btn_new(self, event):
        event.Skip()
        CtrlMinExpense.add_item(DataMinExpense(0, 0, "", 0))
        
        data = DataMinExpense(CtrlMinExpense.get_data_len() + 1, CtrlMinExpense.get_id(), "", 0)
        self.model.data.append(data)
        item = self.model.ObjectToItem(data)
        self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
    
    def on_btn_delete(self, event):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        self.model.data.remove(data)
        self.dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
        CtrlMinExpense.delete_item(data)
    
    def on_btn_refresh(self, event):
        event.Skip()
        result = CtrlMinExpense.get_data()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
                    
        self.model.Cleared()
    
    def on_btn_save(self, event):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        CtrlMinExpense.update_item(data)
    
    def on_btn_exit(self, event):
        event.Skip()
        self.Close()

###########################################################################
## Class PopTableBatAdd
###########################################################################


class PopTableBatAdd (wx.Dialog):
    def _init_view_sizer(self, parent):
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Create grid sizer for 1 row and 2 column
        g_sizer = wx.GridSizer(1, 2, 0, 0)
        
        # Column 1 is another grid sizer for 4 rows and 2 column
        g_sizer_left = wx.GridSizer(4, 2, 0, 0)
        # Add label for code prefix
        s_txt_code_pre = wx.StaticText(self, wx.ID_ANY, u"编号前缀：", wx.DefaultPosition, wx.DefaultSize, 0)
        s_txt_code_pre.Wrap(-1)
        g_sizer_left.Add(s_txt_code_pre, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add text for code prefix
        self.txtCodePre = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        g_sizer_left.Add(self.txtCodePre, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add label for from
        s_txt_from = wx.StaticText(self, wx.ID_ANY, u"从：", wx.DefaultPosition, wx.DefaultSize, 0)
        s_txt_from.Wrap(-1)
        g_sizer_left.Add(s_txt_from, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add text for from
        self.txtFrom = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        g_sizer_left.Add(self.txtFrom, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add label for area
        s_txt_area = wx.StaticText(self, wx.ID_ANY, u"区域：", wx.DefaultPosition, wx.DefaultSize, 0)
        s_txt_area.Wrap(-1)
        g_sizer_left.Add(s_txt_area, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add combo box for area
        cbx_area_choices = list()
        self.cbxArea = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.DefaultSize, cbx_area_choices, 0)
        g_sizer_left.Add(self.cbxArea, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add label for consumer type 
        s_txt_type = wx.StaticText(self, wx.ID_ANY, u"消费类型：", wx.DefaultPosition, wx.DefaultSize, 0)
        s_txt_type.Wrap(-1)
        g_sizer_left.Add(s_txt_type, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add combo box for consumer type 
        cbx_min_expense_choices = list()
        self.cbxMinExpense = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize, cbx_min_expense_choices, 0)
        g_sizer_left.Add(self.cbxMinExpense, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Layout column 1
        g_sizer.Add(g_sizer_left, 1, wx.EXPAND, 5)
        
        # Column 2 is another grid sizer for 4 rows and 2 columns
        g_sizer_right = wx.GridSizer(4, 2, 0, 0)
        # Add spacer
        g_sizer_right.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        g_sizer_right.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        # Add label for to
        s_txt_to = wx.StaticText(self, wx.ID_ANY, u"到：", wx.DefaultPosition, wx.DefaultSize, 0)
        s_txt_to.Wrap(-1)
        g_sizer_right.Add(s_txt_to, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add text control for to
        self.txtTo = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        g_sizer_right.Add(self.txtTo, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add label for dining table type
        s_txt_table_type = wx.StaticText(self, wx.ID_ANY, u"餐桌类型：", wx.DefaultPosition, wx.DefaultSize, 0)
        s_txt_table_type.Wrap(-1)
        g_sizer_right.Add(s_txt_table_type, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add combo box for dining table type
        cbx_type_choices = list()
        self.cbxType = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.DefaultSize, cbx_type_choices, 0)
        g_sizer_right.Add(self.cbxType, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add label for people number
        s_txt_people_number = wx.StaticText(self, wx.ID_ANY, u"人数：", wx.DefaultPosition, wx.DefaultSize, 0)
        s_txt_people_number.Wrap(-1)
        g_sizer_right.Add(s_txt_people_number, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add text control for people number
        self.txtPeopleNum = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        g_sizer_right.Add(self.txtPeopleNum, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Layout column 2
        g_sizer.Add(g_sizer_right, 1, wx.EXPAND, 5)
        
        # Layout data view
        sizer.Add(g_sizer, 1, wx.EXPAND, 5)
        parent.Add(sizer, 1, wx.EXPAND, 5)
        
    def _init_ctrl_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add spacer
        sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        # Add create button
        self.btnCreate = wx.Button(self, wx.ID_ANY, u"生成", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnCreate, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnExit, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Layout control 
        parent.Add(sizer, 1, wx.EXPAND, 5)
        
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"批量生成餐桌", pos=wx.DefaultPosition,
                           size=wx.Size(480, 220), style=wx.CAPTION)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        self._init_view_sizer(sizer)
        self._init_ctrl_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.btnCreate.Bind(wx.EVT_BUTTON, self.on_btn_create)
        self.btnExit.Bind(wx.EVT_BUTTON, self.on_btn_exit)

        # Initialize data on view list
        self._initailize_view()

    def __del__(self):
        pass

    def _initailize_view(self):
        li_area = CtrlArea.get_data()
        for area in li_area:
            self.cbxArea.Append(area.name, area)
        self.cbxArea.SetSelection(0)

        li_table_type = CtrlType.get_data()
        for table_type in li_table_type:
            self.cbxType.Append(table_type.name, table_type)
        self.cbxType.SetSelection(0)

        li_min_expense = CtrlTable.get_data()
        for min_expense in li_min_expense:
            self.cbxMinExpense.Append(min_expense.name, min_expense)
        self.cbxMinExpense.SetSelection(0)

    # Virtual event handlers, override them in your derived class
    def on_btn_create(self, event):
        event.Skip()
        area = self.cbxArea.GetClientData(self.cbxArea.GetSelection())
        table_type = self.cbxType.GetClientData(self.cbxType.GetSelection())
        min_expense = self.cbxMinExpense.GetClientData(self.cbxMinExpense.GetSelection())
        i_from = int(self.txtFrom.GetValue())
        i_to = int(self.txtTo.GetValue())
        i_people_num = int(self.txtPeopleNum.GetValue())
        table_items = list()
        for index in range(i_from, i_to + 1):
            table_items.append(DataTable(0, 0, ("餐桌%d" % index), table_type.code, area.code,
                                         i_people_num, min_expense.code))

        CtrlTable.add_items(table_items)

    def on_btn_exit(self, event):
        event.Skip()
        self.Close()

###########################################################################
## Class PopTableInfo
###########################################################################


class PopTableInfo (wx.Dialog):
    def _init_view_sizer(self, parent):
        panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(600, 200), wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        # Create a grid sizer with 1 row and 2 columns
        g_sizer = wx.GridSizer(1, 2, 0, 0)
        g_sizer.SetMinSize(wx.Size(600, 200))

        # Column 1 also is a grid sizer with 3 rows and 2 columns
        g_sizer_left = wx.GridSizer(3, 2, 0, 0)
        # Add label for dining table code 
        s_txt_table_code = wx.StaticText(panel, wx.ID_ANY, u"餐桌编码：", wx.Point(-1, -1), wx.DefaultSize, 0)
        s_txt_table_code.Wrap(-1)
        g_sizer_left.Add(s_txt_table_code, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add text control for dining table code 
        self.txtCode = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(120, -1), 0)
        g_sizer_left.Add(self.txtCode, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add label for dining table type
        s_txt_table_type = wx.StaticText(panel, wx.ID_ANY, u"所属类型：", wx.DefaultPosition, wx.DefaultSize, 0)
        s_txt_table_type.Wrap(-1)
        g_sizer_left.Add(s_txt_table_type, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add combo box for dining table type
        cbx_type_choices = list()
        self.cbxType = wx.ComboBox(panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.Size(120, -1), cbx_type_choices, 0)
        g_sizer_left.Add(self.cbxType, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add label for people number
        s_txt_people_num = wx.StaticText(panel, wx.ID_ANY, u"人数：", wx.DefaultPosition, wx.DefaultSize, 0)
        s_txt_people_num.Wrap(-1)
        g_sizer_left.Add(s_txt_people_num, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add text control for people number
        self.txtPeople = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(120, -1), 0)
        g_sizer_left.Add(self.txtPeople, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Layout column 1
        g_sizer.Add(g_sizer_left, 1, wx.EXPAND, 5)
        
        # Column 2 also is a grid sizer with 3 rows and 2 columns
        g_sizer_right = wx.GridSizer(3, 2, 0, 0)
        # Add label for dining table name 
        s_txt_table_name = wx.StaticText(panel, wx.ID_ANY, u"餐桌名称：", wx.DefaultPosition, wx.DefaultSize, 0)
        s_txt_table_name.Wrap(-1)
        g_sizer_right.Add(s_txt_table_name, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add text control for dining table name 
        self.txtName = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(120, -1), 0)
        g_sizer_right.Add(self.txtName, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add label for dining table area 
        s_txt_table_area = wx.StaticText(panel, wx.ID_ANY, u"所属区域：", wx.DefaultPosition, wx.DefaultSize, 0)
        s_txt_table_area.Wrap(-1)
        g_sizer_right.Add(s_txt_table_area, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add combo box for dining table area 
        cbx_area_choices = list()
        self.cbxArea = wx.ComboBox(panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.Size(120, -1), cbx_area_choices, 0)
        g_sizer_right.Add(self.cbxArea, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add label for consumer type 
        s_txt_type = wx.StaticText(panel, wx.ID_ANY, u"消费类型：", wx.DefaultPosition, wx.DefaultSize, 0)
        s_txt_type.Wrap(-1)
        g_sizer_right.Add(s_txt_type, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add combo box for consumer type 
        cbx_min_expense_choices = list()
        self.cbxMinExpense = wx.ComboBox(panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.Size(120, -1), cbx_min_expense_choices, 0)
        g_sizer_right.Add(self.cbxMinExpense, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Layout column 2
        g_sizer.Add(g_sizer_right, 1, wx.EXPAND, 5)
        
        # Layout data view
        panel.SetSizer(g_sizer)
        panel.Layout()
        parent.Add(panel, 1, wx.EXPAND | wx.ALL, 5)
        
    def _init_ctrl_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # Add static text for track
        self.txtTrack = wx.StaticText(self, wx.ID_ANY, u"1 / 1 ", wx.DefaultPosition, wx.Size(80, -1), wx.ALIGN_CENTRE)
        self.txtTrack.Wrap(-1)
        sizer.Add(self.txtTrack, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add previous record button
        self.btnPrev = wx.Button(self, wx.ID_ANY, u"上一记录", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnPrev, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add next record button
        self.btnNext = wx.Button(self, wx.ID_ANY, u"下一记录", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnNext, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add spacer
        sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        # Add save button
        self.btnSave = wx.Button(self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnSave, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnExit, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Layout control buttons
        parent.Add(sizer, 1, wx.EXPAND, 5)
        
    def __init__(self, parent, type_):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"餐桌资料设置", pos=wx.DefaultPosition,
                           size=wx.Size(600, 300), style=wx.CAPTION | wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        sizer = wx.BoxSizer(wx.VERTICAL)

        self._init_view_sizer(sizer)
        self._init_ctrl_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.btnPrev.Bind(wx.EVT_BUTTON, self.on_btn_prev)
        self.btnNext.Bind(wx.EVT_BUTTON, self.on_btn_next)
        self.btnSave.Bind(wx.EVT_BUTTON, self.on_btn_save)
        self.btnExit.Bind(wx.EVT_BUTTON, self.on_btn_exit)

        # Initialize data view
        self.index = 0
        self.type = type_
        self._initialize_view()

    def __del__(self):
        pass

    def _initialize_view(self):
        if self.type == "add":
            self._init_add_view()
        elif self.type == "mod":
            self.index = CtrlTable.get_cur_item_index()
            self._init_mod_view()

    def _init_add_view(self):
        li_area = CtrlArea.get_data()
        for area in li_area:
            self.cbxArea.Append(area.name, area)
        self.cbxArea.SetSelection(0)

        li_table_type = CtrlType.get_data()
        for table_type in li_table_type:
            self.cbxType.Append(table_type.name, table_type)
        self.cbxType.SetSelection(0)

        li_min_expense = CtrlMinExpense.get_data()
        for min_expense in li_min_expense:
            self.cbxMinExpense.Append(min_expense.name, min_expense)
        self.cbxMinExpense.SetSelection(0)

        self.txtTrack.Enable(False)
        self.btnPrev.Enable(False)
        self.btnNext.Enable(False)

    def _init_mod_view(self):
        self.txtCode.Enable(False) 
        if self.index < 0:
            self.index = 0
            return

        items = CtrlTable.get_items()
        if self.index >= len(items):
            self.index = len(items) - 1
            return

        data = items[self.index]
        self.txtCode.SetValue(str(data.code))
        self.txtName.SetValue(data.name)
        self.txtPeople.SetValue(str(data.people_num))
        self.txtTrack.SetLabel(("%d / %d" % (self.index+1, len(items))))

        li_area = CtrlArea.get_data()
        area_selection = 0
        for area in li_area:
            self.cbxArea.Append(area.name, area)
            if area.code == data.area:
                self.cbxArea.SetSelection(area_selection)
            area_selection += 1

        li_table_type = CtrlType.get_data()
        table_type_selection = 0
        for table_type in li_table_type:
            self.cbxType.Append(table_type.name, table_type)
            if table_type.code == data.table_type:
                self.cbxType.SetSelection(table_type_selection)
            table_type_selection += 1

        li_min_expense = CtrlMinExpense.get_data()
        min_expense_selection = 0
        for min_expense in li_min_expense:
            self.cbxMinExpense.Append(min_expense.name, min_expense)
            if min_expense.code == data.min_type:
                self.cbxMinExpense.SetSelection(min_expense_selection)
            min_expense_selection += 1

    # Virtual event handlers, override them in your derived class        
    def on_btn_prev(self, event):
        event.Skip()
        self.index -= 1
        self._init_mod_view()

    def on_btn_next(self, event):
        event.Skip()
        self.index += 1
        self._init_mod_view()

    def on_btn_save(self, event):
        event.Skip()
        area = self.cbxArea.GetClientData(self.cbxArea.GetSelection())
        type_ = self.cbxType.GetClientData(self.cbxType.GetSelection())
        min_expense = self.cbxMinExpense.GetClientData(self.cbxMinExpense.GetSelection())
        data = DataTable(0,
                         int(self.txtCode.GetValue()),
                         self.txtName.GetValue(),
                         type_.code,
                         area.code,
                         int(self.txtPeople.GetValue()),
                         min_expense.code)
        if self.type == "add":
            CtrlTable.add_item(data)
        elif self.type == "mod":
            CtrlTable.update_item(data)

    def on_btn_exit(self, event):
        event.Skip()
        self.Close()

###########################################################################
## Class PopTypeSetting
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
        sizer.Add(self.dataViewList, 0, wx.ALL | wx.EXPAND, 5)
        
        # Layout data view 
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_ctrl_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Add new button
        self.btnNew = wx.Button(self, wx.ID_ANY, u"新增", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnNew, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        # Add delete button
        self.btnDelete = wx.Button(self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnDelete, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        # Add spacer
        sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        # Add refresh button
        self.btnRefresh = wx.Button(self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnRefresh, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        # Add save button
        self.btnSave = wx.Button(self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnSave, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnExit, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        
        # Layout control buttons
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"桌类设置", pos=wx.DefaultPosition,
                           size=wx.Size(600, 400), style=wx.CAPTION | wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.Size(-1, -1), wx.Size(-1, -1))
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        self._init_view_sizer(sizer)
        self._init_ctrl_sizer(sizer)
        
        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Create an instance of our model...
        self.model = ModelType(CtrlType.get_data())
        # Tell the DVC to use the model
        self.dataViewList.AssociateModel(self.model)

        # Connect Events
        self.btnNew.Bind(wx.EVT_BUTTON, self.on_btn_new)
        self.btnDelete.Bind(wx.EVT_BUTTON, self.on_btn_delete)
        self.btnRefresh.Bind(wx.EVT_BUTTON, self.on_btn_refresh)
        self.btnSave.Bind(wx.EVT_BUTTON, self.on_btn_save)
        self.btnExit.Bind(wx.EVT_BUTTON, self.on_btn_exit)
    
    def __del__(self):
        pass
       
    # Virtual event handlers, override them in your derived class
    def on_btn_new(self, event):
        event.Skip()
        CtrlType.add_item(DataType(0, 0, ""))
        
        data = DataType(CtrlType.get_data_len() + 1, CtrlType.get_id(), "")
        self.model.data.append(data)
        item = self.model.ObjectToItem(data)
        self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
    
    def on_btn_delete(self, event):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        self.model.data.remove(data)
        self.dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
        CtrlType.delete_item(data)
    
    def on_btn_refresh(self, event):
        event.Skip()
        result = CtrlType.get_data()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
                    
        self.model.Cleared()
    
    def on_btn_save(self, event):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        CtrlType.update_item(data)
    
    def on_btn_exit(self, event):
        event.Skip()
        self.Close()

###########################################################################
## Class DiningTable
###########################################################################


class WgtDiningTable (wx.Panel):
    def _init_status_bar_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.SetMinSize(wx.Size(800, 50))

        # Add new button
        self.btnNew = wx.Button(self, wx.ID_ANY, u"新增", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnNew.SetMinSize(wx.Size(50, 50))
        sizer.Add(self.btnNew, 0, wx.EXPAND, 5)
        # Add modify button
        self.btnModify = wx.Button(self, wx.ID_ANY, u"修改", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnModify.SetMinSize(wx.Size(50, 50))
        sizer.Add(self.btnModify, 0, 0, 5)
        # Add delete button
        self.btnDelete = wx.Button(self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnDelete.SetMinSize(wx.Size(50, 50))
        sizer.Add(self.btnDelete, 0, 0, 5)
        # Add batch add button
        self.btnBatAdd = wx.Button(self, wx.ID_ANY, u"批量增加", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnBatAdd.SetFont(wx.Font(8, 70, 90, 90, False, wx.EmptyString))
        self.btnBatAdd.SetMinSize(wx.Size(50, 50))
        sizer.Add(self.btnBatAdd, 0, 0, 5)
        # Add table type setting button
        self.btnTableType = wx.Button(self, wx.ID_ANY, u"桌类", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnTableType.SetMinSize(wx.Size(50, 50))
        sizer.Add(self.btnTableType, 0, 0, 5)
        # Add area setting button
        self.btnArea = wx.Button(self, wx.ID_ANY, u"区域", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnArea.SetMinSize(wx.Size(50, 50))
        sizer.Add(self.btnArea, 0, 0, 5)
        # Add consumer type setting button
        self.btnMinExpense = wx.Button(self, wx.ID_ANY, u"最低消费", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnMinExpense.SetFont(wx.Font(8, 70, 90, 90, False, wx.EmptyString))
        self.btnMinExpense.SetMinSize(wx.Size(50, 50))
        sizer.Add(self.btnMinExpense, 0, 0, 5)
        # Add refresh button
        self.btnRefresh = wx.Button(self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnRefresh.SetMinSize(wx.Size(50, 50))
        sizer.Add(self.btnRefresh, 0, 0, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnExit.SetMinSize(wx.Size(50, 50))
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
        sizer.Add(self.dataViewList, 0, wx.EXPAND | wx.LEFT, 5)
        
        # Layout data view list
        parent.Add(sizer, 1, 0, 5)

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition,
                          size=wx.Size(800, 600), style=wx.TAB_TRAVERSAL)
        
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DDKSHADOW))
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        self._init_status_bar_sizer(sizer)
        self._init_screen_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)
        
        # Create an instance of our model...
        self.model = ModelTable(CtrlTable.get_data())
        CtrlTable.refresh_items()
        
        # Tell the DVC to use the model
        self.dataViewList.AssociateModel(self.model)

        # Connect Events
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.btnNew.Bind(wx.EVT_BUTTON, self.on_btn_new)
        self.btnModify.Bind(wx.EVT_BUTTON, self.on_btn_modify)
        self.btnDelete.Bind(wx.EVT_BUTTON, self.on_btn_delete)
        self.btnBatAdd.Bind(wx.EVT_BUTTON, self.on_btn_bat_add)
        self.btnTableType.Bind(wx.EVT_BUTTON, self.on_btn_table_type)
        self.btnArea.Bind(wx.EVT_BUTTON, self.on_btn_area_setting)
        self.btnMinExpense.Bind(wx.EVT_BUTTON, self.on_btn_min_expense)
        self.btnRefresh.Bind(wx.EVT_BUTTON, self.on_btn_refresh)
        self.btnExit.Bind(wx.EVT_BUTTON, self.on_btn_exit)
        
        # Show tree control
        self._show_tree_ctrl()
    
    def __del__(self):
        pass
    
    def initialize(self):
        # Add event listener
        EvtManager.add_listener(self, EnumEvent.EVT_DINING_ROOM_REFRESH, self.on_btn_refresh)
        
        x, y = CtrlHomePage.get_screen_size()
        self.SetSize(wx.Size(x, y))

    def un_initialize(self):
        # Remove event listener
        EvtManager.remove_listener(self, EnumEvent.EVT_DINING_ROOM_REFRESH, self.on_btn_refresh)
    
    def _show_tree_ctrl(self):
        isz = (16, 16)
        il = wx.ImageList(isz[0], isz[1])
        fl_idx = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, isz))
        fl_open_idx = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER_OPEN, wx.ART_OTHER, isz))
        file_idx = il.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, isz))
        
        self.treeCtrl.SetImageList(il)
        self.il = il

        self.root = self.treeCtrl.AddRoot(u"全部桌类")
        self.treeCtrl.SetPyData(self.root, None)
        self.treeCtrl.SetItemImage(self.root, fl_idx, wx.TreeItemIcon_Normal)
        self.treeCtrl.SetItemImage(self.root, fl_open_idx, wx.TreeItemIcon_Expanded)
        
        table_type_map = dict()
        li_items = CtrlTable.get_items()
        for item in li_items:
            if item.table_type in table_type_map:
                table_type_map[item.table_type].append(item)
            else:
                list_tmp = list()
                list_tmp.append(item)
                table_type_map_tmp = {item.table_type: list_tmp}
                table_type_map.update(table_type_map_tmp)
        
        li_table_type = CtrlTable.get_data()
        for table_type in li_table_type:
            if table_type.code in table_type_map:
                title = "%s(%d)" % (table_type.name, len(table_type_map[table_type.code]))
                child = self.treeCtrl.AppendItem(self.root, title)
                self.treeCtrl.SetPyData(child, None)
                self.treeCtrl.SetItemImage(child, fl_idx, wx.TreeItemIcon_Normal)
                self.treeCtrl.SetItemImage(child, fl_open_idx, wx.TreeItemIcon_Expanded)
                for table_info in table_type_map[table_type.code]:
                    sub_child = self.treeCtrl.AppendItem(child, table_info.name)
                    self.treeCtrl.SetPyData(sub_child, None)
                    self.treeCtrl.SetItemImage(sub_child, file_idx, wx.TreeItemIcon_Normal)
                    self.treeCtrl.SetItemImage(sub_child, file_idx, wx.TreeItemIcon_Selected)
            else:
                title = "%s(0)" % table_type.name
                child = self.treeCtrl.AppendItem(self.root, title)
                self.treeCtrl.SetPyData(child, None)
                self.treeCtrl.SetItemImage(child, fl_idx, wx.TreeItemIcon_Normal)
                self.treeCtrl.SetItemImage(child, fl_open_idx, wx.TreeItemIcon_Expanded)
                
        self.treeCtrl.Expand(self.root)
                
    def _refresh_ui(self):
        # Refresh treeCtrl
        CtrlTable.refresh_items()
        self.treeCtrl.DeleteAllItems()
        self._show_tree_ctrl()
        
        # Refresh data view list
        result = CtrlTable.get_data()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
                    
        self.model.Cleared()
    
    # Virtual event handlers, override them in your derived class
    def on_size(self, event):
        event.Skip()
        x, y = self.GetSize()

        self.btnNew.SetMaxSize(wx.Size(50, 50))
        self.btnModify.SetMaxSize(wx.Size(50, 50))
        self.btnDelete.SetMaxSize(wx.Size(50, 50))
        self.btnBatAdd.SetMaxSize(wx.Size(50, 50))
        self.btnTableType.SetMaxSize(wx.Size(50, 50))
        self.btnArea.SetMaxSize(wx.Size(50, 50))
        self.btnMinExpense.SetMaxSize(wx.Size(50, 50))
        self.btnRefresh.SetMaxSize(wx.Size(50, 50))
        self.btnExit.SetMaxSize(wx.Size(50, 50))
        self.topPanel.SetMaxSize(wx.Size(x-450, 50))
        self.treeCtrl.SetMinSize(wx.Size(200, y-50))
        self.dataViewList.SetMinSize(wx.Size(x-200, y-50))
        
    def on_btn_new(self, event):
        event.Skip()
        pop_table_info = PopTableInfo(self, "add")
        pop_table_info.ShowModal()
    
    def on_btn_modify(self, event):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        index = self.model.data.index(data)
        CtrlTable.set_cur_item_index(index)
        pop_table_info = PopTableInfo(self, "mod")
        pop_table_info.ShowModal()
    
    def on_btn_delete(self, event):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        self.model.data.remove(data)
        self.dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
        CtrlTable.delete_item(data)
    
    def on_btn_bat_add(self, event):
        event.Skip()
        pop_bat_add = PopTableBatAdd(self)
        pop_bat_add.ShowModal()
    
    def on_btn_table_type(self, event):
        event.Skip()
        pop_table_type = PopTypeSetting(self)
        pop_table_type.ShowModal()
    
    def on_btn_area_setting(self, event):
        event.Skip()
        pop_area = PopAreaSetting(self)
        pop_area.ShowModal()
        
    def on_btn_min_expense(self, event):
        event.Skip()
        pop_min_expense = PopMinExpenseSetting(self)
        pop_min_expense.ShowModal()
    
    def on_btn_refresh(self, event):
        event.Skip()
        self._refresh_ui()
    
    def on_btn_exit(self, event):
        event.Skip()
        self.Hide()
        CtrlHomePage.set_selected_item()
        AppManager.switch_to_application('HomePage')
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = WgtDiningTable(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()