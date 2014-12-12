#!/usr/bin/env python
# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
from app.home_logic import CtrlHomePage
from app.manager.logic.ctrl import * 
from app.manager.logic.model import *
from app.manager.logic.data import *
from app.app_manager import AppManager
from framework.core import TreeImage
from framework.img_button import ImgButton

import wx
import wx.xrc
import wx.dataview
from wx.dataview import DataViewColumn
import sys

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
        self.model = ModelArea(CtrlArea.get_instance().get_data())

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
        CtrlArea.get_instance().add_item(DataArea())

        data = DataArea(CtrlArea.get_instance().get_data_len() + 1, CtrlArea.get_instance().get_id())
        self.model.data.append(data)
        item = self.model.ObjectToItem(data)
        self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)

    def on_btn_delete(self, event):
        event.Skip()
        try:
            item = self.dataViewList.GetCurrentItem()
            data = self.model.ItemToObject(item)
            self.model.data.remove(data)
            self.dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
            CtrlArea.get_instance().delete_item(data)
        except:
            print 'PopAreaSetting on_btn_delete error'

    def on_btn_refresh(self, event):
        event.Skip()
        result = CtrlArea.get_instance().get_data()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)

        self.model.Cleared()

    def on_btn_save(self, event):
        event.Skip()
        for data in self.model.data:
            CtrlArea.get_instance().update_item(data)

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
        self.model = ModelMinExpense(CtrlMinExpense.get_instance().get_data())
        
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
        CtrlMinExpense.get_instance().add_item(DataMinExpense())
        
        data = DataMinExpense(CtrlMinExpense.get_instance().get_data_len() + 1, CtrlMinExpense.get_instance().get_id())
        self.model.data.append(data)
        item = self.model.ObjectToItem(data)
        self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
    
    def on_btn_delete(self, event):
        event.Skip()
        try:
            item = self.dataViewList.GetCurrentItem()
            data = self.model.ItemToObject(item)
            self.model.data.remove(data)
            self.dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
            CtrlMinExpense.get_instance().delete_item(data)
        except:
            print 'PopMinExpenseSetting on_btn_delete error'
    
    def on_btn_refresh(self, event):
        event.Skip()
        result = CtrlMinExpense.get_instance().get_data()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
                    
        self.model.Cleared()
    
    def on_btn_save(self, event):
        event.Skip()
        for data in self.model.data:
            CtrlMinExpense.get_instance().update_item(data)
    
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
                                   wx.Size(110, -1), cbx_area_choices, 0)
        g_sizer_left.Add(self.cbxArea, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add label for consumer type 
        s_txt_type = wx.StaticText(self, wx.ID_ANY, u"消费类型：", wx.DefaultPosition, wx.DefaultSize, 0)
        s_txt_type.Wrap(-1)
        g_sizer_left.Add(s_txt_type, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add combo box for consumer type 
        cbx_min_expense_choices = list()
        self.cbxMinExpense = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.Size(110, -1), cbx_min_expense_choices, 0)
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
                                   wx.Size(110, -1), cbx_type_choices, 0)
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
        self._initialize_view()

    def __del__(self):
        pass

    def _initialize_view(self):
        li_area = CtrlArea.get_instance().get_data()
        for area in li_area:
            self.cbxArea.Append(area.name, area)
        self.cbxArea.SetSelection(0)

        li_table_type = CtrlType.get_instance().get_data()
        for table_type in li_table_type:
            self.cbxType.Append(table_type.name, table_type)
        self.cbxType.SetSelection(0)

        li_min_expense = CtrlMinExpense.get_instance().get_data()
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
        for index_ in range(i_from, i_to + 1):
            CtrlTable.get_instance().add_item(DataTable(0, 0, ("餐桌%d" % index_), table_type.key, area.key,
                                         i_people_num, min_expense.key))

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
            self.index = CtrlTable.get_instance().get_cur_item_index()
            self._init_mod_view()

    def _init_add_view(self):
        li_area = CtrlArea.get_instance().get_data()
        for area in li_area:
            self.cbxArea.Append(area.name, area)
        self.cbxArea.SetSelection(0)

        li_table_type = CtrlType.get_instance().get_data()
        for table_type in li_table_type:
            self.cbxType.Append(table_type.name, table_type)
        self.cbxType.SetSelection(0)

        li_min_expense = CtrlMinExpense.get_instance().get_data()
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

        items = CtrlTable.get_instance().get_items()
        if self.index >= len(items):
            self.index = len(items) - 1
            return

        data = items[self.index]
        self.txtCode.SetValue(str(data.key))
        self.txtName.SetValue(data.name)
        self.txtPeople.SetValue(str(data.people_num))
        self.txtTrack.SetLabel(("%d / %d" % (self.index+1, len(items))))

        li_area = CtrlArea.get_instance().get_data()
        for area in li_area:
            self.cbxArea.Append(area.name, area)
            if area.key == data.area:
                self.cbxArea.SetSelection(li_area.index(area))

        li_table_type = CtrlType.get_instance().get_data()
        for table_type in li_table_type:
            self.cbxType.Append(table_type.name, table_type)
            if table_type.key == data.table_type:
                self.cbxType.SetSelection(li_table_type.index(table_type))

        li_min_expense = CtrlMinExpense.get_instance().get_data()
        for min_expense in li_min_expense:
            self.cbxMinExpense.Append(min_expense.name, min_expense)
            if min_expense.key == data.min_type:
                self.cbxMinExpense.SetSelection(li_min_expense.index(min_expense))

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
                         type_.key,
                         area.key,
                         int(self.txtPeople.GetValue()),
                         min_expense.key)
        if self.type == "add":
            CtrlTable.get_instance().add_item(data)
        elif self.type == "mod":
            CtrlTable.get_instance().update_item(data)

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
        self.model = ModelType(CtrlType.get_instance().get_data())
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
        CtrlType.get_instance().add_item(DataType())
        
        data = DataType(CtrlType.get_instance().get_data_len() + 1, CtrlType.get_instance().get_id())
        self.model.data.append(data)
        item = self.model.ObjectToItem(data)
        self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
    
    def on_btn_delete(self, event):
        event.Skip()
        try:
            item = self.dataViewList.GetCurrentItem()
            data = self.model.ItemToObject(item)
            self.model.data.remove(data)
            self.dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
            CtrlType.get_instance().delete_item(data)
        except:
            print 'PopTypeSetting on_btn_delete error'
    
    def on_btn_refresh(self, event):
        event.Skip()
        result = CtrlType.get_instance().get_data()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
                    
        self.model.Cleared()
    
    def on_btn_save(self, event):
        event.Skip()
        for data in self.model.data:
            CtrlType.get_instance().update_item(data)
    
    def on_btn_exit(self, event):
        event.Skip()
        self.Close()

###########################################################################
## Class WgtDiningTable
###########################################################################


class WgtDiningTable (wx.Panel):
    def _init_status_bar_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.SetMinSize(wx.Size(800, 82))

        # Add fix panel
        self.topPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.topPanel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
        sizer.Add(self.topPanel, 1, wx.EXPAND, 5)

        # Add new button
        self.btnNew = ImgButton(self.topPanel, u"new.png", u"s_new.png")
        # Add modify button
        self.btnModify = ImgButton(self.topPanel, u"modify.png", u"s_modify.png")
        # Add delete button
        self.btnDelete = ImgButton(self.topPanel, u"delete.png", u"s_delete.png")
        # Add batch add button
        self.btnBatAdd = ImgButton(self.topPanel, u"bat_add.png", u"s_bat_add.png")
        # Add table type setting button
        self.btnTableType = ImgButton(self.topPanel, u"table_type.png", u"s_table_type.png")
        # Add area setting button
        self.btnArea = ImgButton(self.topPanel, u"table_area.png", u"s_table_area.png")
        # Add consumer type setting button
        self.btnMinExpense = ImgButton(self.topPanel, u"min_expense.png", u"s_min_expense.png")
        # Add refresh button
        self.btnRefresh = ImgButton(self.topPanel, u"refresh.png", u"s_refresh.png")
        # Add exit button
        self.btnExit = ImgButton(self.topPanel, u"tool_exit.png", u"s_tool_exit.png")
        
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
        self.treeCtrl.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
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
        self.dataViewList.AppendTextColumn(u"行号", 0, align=wx.ALIGN_CENTER)
        self.dataViewList.AppendTextColumn(u"桌号", 1, align=wx.ALIGN_CENTER)
        self.dataViewList.AppendTextColumn(u"餐桌名", 2, align=wx.ALIGN_CENTER)
        self.dataViewList.AppendTextColumn(u"类型", 3, align=wx.ALIGN_CENTER)
        self.dataViewList.AppendTextColumn(u"区域", 4, align=wx.ALIGN_CENTER)
        self.dataViewList.AppendTextColumn(u"人数", 5, align=wx.ALIGN_CENTER)
        self.dataViewList.AppendTextColumn(u"最低消费类型", 6, width=100, align=wx.ALIGN_CENTER)
        #self.dataViewList.
        self.dataViewList.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        sizer.Add(self.dataViewList, 0, wx.EXPAND | wx.LEFT, 5)
        
        # Layout data view list
        parent.Add(sizer, 1, 0, 5)

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition,
                          size=wx.Size(800, 600), style=wx.TAB_TRAVERSAL)
        
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(0x51, 0x1c, 0x0a))
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        self._init_status_bar_sizer(sizer)
        self._init_screen_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_PAINT, self.on_paint)
        #self.Bind(wx.EVT_ERASE_BACKGROUND, self.on_paint)
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

        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.on_sel_changed, self.treeCtrl)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.on_activate, self.treeCtrl)

        # define variable
        self.model = None
        self.tree_data = None

    def __del__(self):
        pass
    
    def initialize(self):
        # Create an instance of our model...
        self.model = ModelTable(CtrlTable.get_instance().get_data())
        CtrlTable.get_instance().refresh_items()
        # Tell the DVC to use the model
        self.dataViewList.AssociateModel(self.model)
        # Show tree control
        self._show_tree_ctrl()

        # Add event listener
        EvtManager.add_listener(self, EnumEvent.EVT_DINING_ROOM_REFRESH, self.on_btn_refresh)
        
        x, y = CtrlHomePage.get_instance().get_screen_size()
        self.SetSize(wx.Size(x, y))

    def un_initialize(self):
        # Remove event listener
        EvtManager.remove_listener(self, EnumEvent.EVT_DINING_ROOM_REFRESH, self.on_btn_refresh)
    
    def _show_tree_ctrl(self):
        self.treeCtrl.DeleteAllItems()
        tree_image = TreeImage()
        self.treeCtrl.SetImageList(tree_image.image_list)
        self.il = tree_image.image_list

        self.root = self.treeCtrl.AddRoot(u"全部桌类")
        self.treeCtrl.SetPyData(self.root, None)
        self.treeCtrl.SetItemImage(self.root, tree_image.folder_idx, wx.TreeItemIcon_Normal)
        self.treeCtrl.SetItemImage(self.root, tree_image.folder_open_idx, wx.TreeItemIcon_Expanded)
        
        table_type_map = dict()
        li_items = CtrlTable.get_instance().get_items()
        for item in li_items:
            if item.table_type in table_type_map:
                table_type_map[item.table_type].append(item)
            else:
                list_tmp = list()
                list_tmp.append(item)
                table_type_map_tmp = {item.table_type: list_tmp}
                table_type_map.update(table_type_map_tmp)
        
        li_table_type = CtrlType.get_instance().get_data()
        for table_type in li_table_type:
            if table_type.key in table_type_map:
                title = "%s(%d)" % (table_type.name, len(table_type_map[table_type.key]))
                child = self.treeCtrl.AppendItem(self.root, title)
                self.treeCtrl.SetPyData(child, table_type)
                self.treeCtrl.SetItemImage(child, tree_image.folder_idx, wx.TreeItemIcon_Normal)
                self.treeCtrl.SetItemImage(child, tree_image.folder_open_idx, wx.TreeItemIcon_Expanded)
                for table_info in table_type_map[table_type.key]:
                    sub_child = self.treeCtrl.AppendItem(child, table_info.name)
                    self.treeCtrl.SetPyData(sub_child, table_info)
                    self.treeCtrl.SetItemImage(sub_child, tree_image.file_idx, wx.TreeItemIcon_Normal)
                    self.treeCtrl.SetItemImage(sub_child, tree_image.file_idx, wx.TreeItemIcon_Selected)
            else:
                title = "%s(0)" % table_type.name
                child = self.treeCtrl.AppendItem(self.root, title)
                self.treeCtrl.SetPyData(child, None)
                self.treeCtrl.SetItemImage(child, tree_image.folder_idx, wx.TreeItemIcon_Normal)
                self.treeCtrl.SetItemImage(child, tree_image.folder_open_idx, wx.TreeItemIcon_Expanded)
                
        self.treeCtrl.Expand(self.root)
                
    def _refresh_ui(self):
        # Refresh treeCtrl
        CtrlTable.get_instance().refresh_items()
        self.treeCtrl.DeleteAllItems()
        self._show_tree_ctrl()
        
        # Refresh data view list
        result = CtrlTable.get_instance().get_data()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
                    
        self.model.Cleared()
    
    # Virtual event handlers, override them in your derived class
    def on_paint(self, event):
        dc = wx.ClientDC(self.topPanel)
        dc.Clear()

        sz = self.GetClientSize()
        bg_img = wx.Image(sys.path[0] + "\\..\\image\\top_bg.png", wx.BITMAP_TYPE_PNG).Scale(sz.x, 82)
        bg_bmp = bg_img.ConvertToBitmap()

        #self.topPanel.Refresh()

        mem_dc = wx.MemoryDC()
        mem_dc.SelectObject(bg_bmp)
        dc.Blit(0, 0,
                bg_bmp.GetWidth(), bg_bmp.GetHeight(),
                mem_dc, 0, 0, wx.COPY, True)

        #self.btnExit.Show()

    def on_size(self, event):
        event.Skip()
        x, y = self.GetSize()

        self.btnNew.SetSize(wx.Size(63, 70))
        self.btnNew.SetPosition(wx.Point(0, 6))

        self.btnModify.SetSize(wx.Size(63, 70))
        self.btnModify.SetPosition(wx.Point(65, 6))

        self.btnDelete.SetSize(wx.Size(63, 70))
        self.btnDelete.SetPosition(wx.Point(130, 6))

        self.btnBatAdd.SetSize(wx.Size(103, 70))
        self.btnBatAdd.SetPosition(wx.Point(195, 6))

        self.btnTableType.SetSize(wx.Size(63, 70))
        self.btnTableType.SetPosition(wx.Point(300, 6))

        self.btnArea.SetSize(wx.Size(63, 70))
        self.btnArea.SetPosition(wx.Point(365, 6))

        self.btnMinExpense.SetSize(wx.Size(103, 70))
        self.btnMinExpense.SetPosition(wx.Point(430, 6))

        self.btnRefresh.SetSize(wx.Size(63, 70))
        self.btnRefresh.SetPosition(wx.Point(535, 6))

        self.btnExit.SetSize(wx.Size(63, 70))
        self.btnExit.SetPosition(wx.Point(600, 6))

        self.topPanel.SetMaxSize(wx.Size(x, 82))
        self.treeCtrl.SetMinSize(wx.Size(200, y-82))
        self.dataViewList.SetMinSize(wx.Size(x-200, y-82))

        self.Refresh()
        
    def on_btn_new(self, event):
        event.Skip()
        pop_table_info = PopTableInfo(self, "add")
        pop_table_info.ShowModal()
    
    def on_btn_modify(self, event):
        event.Skip()
        try:
            item = self.dataViewList.GetCurrentItem()
            try:
                    data = self.model.ItemToObject(item)
            except:
                for item_ in self.model.data:
                    if item_.key == self.tree_data.key:
                        data = item_
            index_ = self.model.data.index(data)
            CtrlTable.get_instance().set_cur_item_index(index_)
            pop_table_info = PopTableInfo(self, "mod")
            pop_table_info.ShowModal()
        except Exception, ex:
            print Exception, ":", ex
            print 'WgtDiningTable: on_btn_modify error'
    
    def on_btn_delete(self, event):
        event.Skip()
        try:
            item = self.dataViewList.GetCurrentItem()
            try:
                data = self.model.ItemToObject(item)
            except Exception, ex:
                print Exception, ":", ex
                for item_ in self.model.data:
                    if item_.key == self.tree_data.key:
                        data = item_

            self.model.data.remove(data)
            self.dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
            CtrlTable.get_instance().delete_item(data)
        except Exception, ex:
            print Exception, ":", ex
            print 'WgtDiningTable: on_btn_delete error'
    
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
        CtrlHomePage.get_instance().set_selected_item()
        AppManager.get_instance().switch_to_application('HomePage')

    def on_sel_changed(self, event):
        event.Skip()
        self.tree_data = self.treeCtrl.GetPyData(event.GetItem())

    def on_activate(self, event):
        event.Skip()
        self.tree_data = self.treeCtrl.GetPyData(event.GetItem())
        if isinstance(self.tree_data, DataTable):
            self.on_btn_modify(event)
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = WgtDiningTable(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()
