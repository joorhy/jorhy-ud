# -*- coding: utf-8 -*-
#!/usr/bin/env python

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
from app.home_logic import CtrlHomePage
from app.app_manager import AppManager
from app.front.logic.ctrl import *
from app.front.logic.model import *
from framework.img_button import ImgButton

import wx
import wx.xrc
import wx.dataview
import time
import sys


###########################################################################
## Class PopOpenTable
###########################################################################

class PopOpenTable(wx.Dialog):
    def _init_data_view(self, parent):
        self.dataPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        sb_sizer = wx.StaticBoxSizer(wx.StaticBox(self.dataPanel, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)
        # Add table number and table name sizer
        table_number_name_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add table number
        s_txt_table_num = wx.StaticText(self.dataPanel, wx.ID_ANY, u"餐桌号：", wx.DefaultPosition,
                                        wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_table_num.Wrap(-1)
        table_number_name_sizer.Add(s_txt_table_num, 0, wx.ALL, 5)

        self.txtTableNum = wx.TextCtrl(self.dataPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        table_number_name_sizer.Add(self.txtTableNum, 0, wx.ALL, 5)
        # Add table name
        s_txt_table_name = wx.StaticText(self.dataPanel, wx.ID_ANY, u"餐桌名：", wx.DefaultPosition,
                                         wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_table_name.Wrap(-1)
        table_number_name_sizer.Add(s_txt_table_name, 0, wx.ALL, 5)

        self.txtTableName = wx.TextCtrl(self.dataPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        table_number_name_sizer.Add(self.txtTableName, 0, wx.ALL, 5)

        sb_sizer.Add(table_number_name_sizer, 1, wx.EXPAND, 5)

        # Add people number and waiter info sizer
        people_number_waiter_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add people number
        s_txt_people_num = wx.StaticText(self.dataPanel, wx.ID_ANY, u"人数：", wx.DefaultPosition,
                                         wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_people_num.Wrap(-1)
        people_number_waiter_sizer.Add(s_txt_people_num, 0, wx.ALL, 5)

        self.txtPeopleNum = wx.TextCtrl(self.dataPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        people_number_waiter_sizer.Add(self.txtPeopleNum, 0, wx.ALL, 5)
        # Add waiter info
        s_txt_waiter = wx.StaticText(self.dataPanel, wx.ID_ANY, u"服务员：", wx.DefaultPosition,
                                     wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_waiter.Wrap(-1)
        people_number_waiter_sizer.Add(s_txt_waiter, 0, wx.ALL, 5)

        cbx_waiter_choices = list()
        self.cbxWaiter = wx.ComboBox(self.dataPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.Size(110, -1), cbx_waiter_choices, 0)
        people_number_waiter_sizer.Add(self.cbxWaiter, 0, wx.ALL, 5)

        sb_sizer.Add(people_number_waiter_sizer, 1, wx.EXPAND, 5)

        # Add memo sizer
        memo_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add memo
        s_txt_memo = wx.StaticText(self.dataPanel, wx.ID_ANY, u"备注：", wx.DefaultPosition,
                                   wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_memo.Wrap(-1)
        memo_sizer.Add(s_txt_memo, 0, wx.ALL, 5)

        self.txtMemo = wx.TextCtrl(self.dataPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(300, -1), 0)
        memo_sizer.Add(self.txtMemo, 0, wx.ALL, 5)

        sb_sizer.Add(memo_sizer, 1, wx.EXPAND, 5)

        # Add open table person and time sizer
        open_person_deposit_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add open table person
        s_txt_open_person = wx.StaticText(self.dataPanel, wx.ID_ANY, u"开台人：", wx.DefaultPosition,
                                          wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_open_person.Wrap(-1)
        open_person_deposit_sizer.Add(s_txt_open_person, 0, wx.ALL, 5)

        self.txtOpenPerson = wx.TextCtrl(self.dataPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        open_person_deposit_sizer.Add(self.txtOpenPerson, 0, wx.ALL, 5)
        # Add deposit
        s_txt_deposit = wx.StaticText(self.dataPanel, wx.ID_ANY, u"押金：", wx.DefaultPosition,
                                      wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_deposit.Wrap(-1)
        open_person_deposit_sizer.Add(s_txt_deposit, 0, wx.ALL, 5)

        self.txtDeposit = wx.TextCtrl(self.dataPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        open_person_deposit_sizer.Add(self.txtDeposit, 0, wx.ALL, 5)

        sb_sizer.Add(open_person_deposit_sizer, 1, wx.EXPAND, 5)

        # Add open table person and time sizer
        open_time_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add open table time
        s_txt_open_time = wx.StaticText(self.dataPanel, wx.ID_ANY, u"开台时间：", wx.DefaultPosition,
                                        wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_open_time.Wrap(-1)
        open_time_sizer.Add(s_txt_open_time, 0, wx.ALL, 5)

        self.txtOpenTime = wx.TextCtrl(self.dataPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.Size(300, -1), 0)
        open_time_sizer.Add(self.txtOpenTime, 0, wx.ALL, 5)

        sb_sizer.Add(open_time_sizer, 1, wx.EXPAND, 5)

        # Layout data view
        self.dataPanel.SetSizer(sb_sizer)
        self.dataPanel.Layout()
        sb_sizer.Fit(self.dataPanel)
        parent.Add(self.dataPanel, 1, wx.EXPAND | wx.ALL, 5)

    def _init_ctrl(self, parent):
        self.ctrlPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), wx.TAB_TRAVERSAL)
        sizer = wx.BoxSizer(wx.VERTICAL)
        # Add spacer
        sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        # Add open table button
        self.btnOpen = wx.Button(self.ctrlPanel, wx.ID_ANY, u"开台", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnOpen, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add cancel button
        self.btnCancel = wx.Button(self.ctrlPanel, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnCancel, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Layout ctrl panel
        self.ctrlPanel.SetSizer(sizer)
        self.ctrlPanel.Layout()
        sizer.Fit(self.ctrlPanel)
        parent.Add(self.ctrlPanel, 1, wx.EXPAND | wx.ALL, 5)

    def __init__(self, parent, table_num):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"开台操作", pos=wx.DefaultPosition,
                           size=wx.Size(600, 300), style=wx.CAPTION)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        self._init_data_view(sizer)
        self._init_ctrl(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.btnOpen.Bind(wx.EVT_BUTTON, self.on_btn_open)
        self.btnCancel.Bind(wx.EVT_BUTTON, self.on_btn_cancel)

        # Initialize
        self.table_num = table_num
        self._init_table_info()

    def __del__(self):
        pass

    def _init_table_info(self):
        item = CtrlTableInfo.get_instance().get_table_item(self.table_num)
        if item is not None:
            self.txtTableNum.SetValue(str(item.table_num))
            self.txtTableNum.Enable(False)
            self.txtTableName.SetValue(item.table_name)
            self.txtTableName.Enable(False)
            self.txtPeopleNum.SetValue(str(item.people_num))
            self.txtOpenPerson.SetValue(CtrlFrontLogin.get_instance().get_user())
            self.txtOpenPerson.Enable(False)
            self.txtOpenTime.SetValue(time.strftime('%Y-%m-%d %H:%M:%S'))
            self.txtOpenTime.Enable(False)

            waiter_items = CtrlTableInfo.get_instance().get_waiter_items()
            for item in waiter_items:
                self.cbxWaiter.Append(item.waiter_name, item)

            self.cbxWaiter.SetSelection(0)

    # Virtual event handlers, override them in your derived class
    def on_btn_open(self, event):
        event.Skip()
        table_info = DataTableItem()
        table_info.table_id = self.table_num
        table_info.open_time = time.strftime('%Y-%m-%d %H:%M:%S')
        table_info.waiter = self.cbxWaiter.GetValue()
        table_info.customer_num = int(self.txtPeopleNum.GetValue())
        CtrlTableInfo.get_instance().open_table(table_info)
        self.Close()

    def on_btn_cancel(self, event):
        event.Skip()
        self.Close()

###########################################################################
## Class PopChangeTable
###########################################################################


class PopChangeTable (wx.Dialog):
    def _init_title_info(self, parent):
        self.titlePanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.titlePanel.SetMaxSize(wx.Size(-1, 30))

        sizer = wx.BoxSizer(wx.HORIZONTAL)

        s_txt_title = wx.StaticText(self.titlePanel, wx.ID_ANY, u"可转入餐台列表:", wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        s_txt_title.Wrap(-1)
        sizer.Add(s_txt_title, 0, wx.ALL, 5)

        # Layout title
        self.titlePanel.SetSizer(sizer)
        self.titlePanel.Layout()
        sizer.Fit(self.titlePanel)
        parent.Add(self.titlePanel, 1, wx.EXPAND | wx.ALL, 5)

    def _init_data_view(self, parent):
        self.dataViewPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition,
                                      wx.DefaultSize, wx.STATIC_BORDER | wx.TAB_TRAVERSAL)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Add data view ctrl list
        self.dataViewCtrl = wx.dataview.DataViewCtrl(self.dataViewPanel, wx.ID_ANY,
                                                     wx.DefaultPosition, wx.Size(600, 300), 0)
        self.dataViewCtrl.AppendTextColumn(u"行号", 0)
        self.dataViewCtrl.AppendTextColumn(u"餐桌号", 1)
        self.dataViewCtrl.AppendTextColumn(u"餐桌名", 2)
        self.dataViewCtrl.AppendTextColumn(u"餐桌类型", 3)
        self.dataViewCtrl.AppendTextColumn(u"餐桌区域", 4)
        self.dataViewCtrl.AppendTextColumn(u"人数", 5)
        sizer.Add(self.dataViewCtrl, 0, wx.EXPAND, 5)

        # Layout data view ctrl list
        self.dataViewPanel.SetSizer(sizer)
        self.dataViewPanel.Layout()
        sizer.Fit(self.dataViewPanel)
        parent.Add(self.dataViewPanel, 1, wx.EXPAND, 5)

    def _init_ctrl_view(self, parent):
        self.ctrlPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Add table number
        s_txt_table_code = wx.StaticText(self.ctrlPanel, wx.ID_ANY, u"转入台号：", wx.DefaultPosition,
                                         wx.Size(80, -1), wx.ALIGN_RIGHT)
        s_txt_table_code.Wrap(-1)
        sizer.Add(s_txt_table_code, 0, wx.ALIGN_CENTER, 5)

        self.txtTableCode = wx.TextCtrl(self.ctrlPanel, wx.ID_ANY, wx.EmptyString,
                                        wx.DefaultPosition, wx.Size(200, -1), 0)
        sizer.Add(self.txtTableCode, 0, wx.ALIGN_CENTER, 5)

        # Add spacer
        sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        # Add ok button
        self.btnOk = wx.Button(self.ctrlPanel, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnOk, 0, wx.ALIGN_CENTER, 5)
        # Add cancel button
        self.btnCancel = wx.Button(self.ctrlPanel, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnCancel, 0, 0, 5)

        # Layout control
        self.ctrlPanel.SetSizer(sizer)
        self.ctrlPanel.Layout()
        sizer.Fit(self.ctrlPanel)
        parent.Add(self.ctrlPanel, 1, wx.EXPAND, 5)

    def __init__(self, parent, src_table_num):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"转台操作", pos=wx.DefaultPosition,
                           size=wx.Size(600, 400), style=wx.CAPTION)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        sizer = wx.BoxSizer(wx.VERTICAL)

        self._init_title_info(sizer)
        self._init_data_view(sizer)
        self._init_ctrl_view(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.btnOk.Bind(wx.EVT_BUTTON, self.on_btn_ok)
        self.btnCancel.Bind(wx.EVT_BUTTON, self.on_btn_cancel)

        self.Bind(wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.on_item_activated, self.dataViewCtrl)
        self.Bind(wx.dataview.EVT_DATAVIEW_SELECTION_CHANGED, self.on_item_changed, self.dataViewCtrl)

        # Create an instance of our model...
        self.model = ModelFreeTable(CtrlTableInfo.get_instance().get_free_tables())
        # Tell the DVC to use the model
        self.dataViewCtrl.AssociateModel(self.model)

        # Initialize
        self.src_table_num = src_table_num
        self.txtTableCode.Enable(False)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def on_btn_ok(self, event):
        event.Skip()
        try:
            CtrlTableInfo.get_instance().change_table(self.src_table_num, str(self.txtTableCode.GetValue()))
        except:
            pass
        self.Close()

    def on_btn_cancel(self, event):
        event.Skip()
        self.Close()

    def on_item_activated(self, event):
        event.Skip()
        print self.model.GetValue(event.GetItem(), 1)

    def on_item_changed(self, event):
        event.Skip()
        try:
            self.txtTableCode.SetValue(str(self.model.GetValue(event.GetItem(), 1)))
        except:
            self.txtTableCode.SetValue('')

###########################################################################
## Class PopCloseTable
###########################################################################


class PopCloseTable (wx.Dialog):
    def _init_ui(self, parent):
        # Add table info sizer
        table_info_sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)
        table_info_sizer.SetMinSize(wx.Size(-1, 120))
        # Add table number sizer
        table_number_sizer = wx.BoxSizer(wx.HORIZONTAL)
        s_txt_table_num = wx.StaticText(self, wx.ID_ANY, u"餐桌号：", wx.DefaultPosition,
                                        wx.Size(100, -1), wx.ALIGN_RIGHT)
        s_txt_table_num.Wrap(-1)
        table_number_sizer.Add(s_txt_table_num, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtTableNum = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        table_number_sizer.Add(self.txtTableNum, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        table_info_sizer.Add(table_number_sizer, 1, wx.EXPAND, 5)

        # Add table_name sizer
        table_name_sizer = wx.BoxSizer(wx.HORIZONTAL)

        s_txt_table_name = wx.StaticText(self, wx.ID_ANY, u"餐桌名：", wx.DefaultPosition,
                                         wx.Size(100, -1), wx.ALIGN_RIGHT)
        s_txt_table_name.Wrap(-1)
        table_name_sizer.Add(s_txt_table_name, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtTableName = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        table_name_sizer.Add(self.txtTableName, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        table_info_sizer.Add(table_name_sizer, 1, wx.EXPAND, 5)

        parent.Add(table_info_sizer, 1, wx.EXPAND, 5)

        # Add discount control
        ctrl_sizer = wx.BoxSizer(wx.HORIZONTAL)
        ctrl_sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        # Add confirm button
        self.btnConfirm = wx.Button(self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0)
        ctrl_sizer.Add(self.btnConfirm, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add cancel button
        self.btnCancel = wx.Button(self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0)
        ctrl_sizer.Add(self.btnCancel, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        ctrl_sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        parent.Add(ctrl_sizer, 1, wx.EXPAND, 5)

    def __init__(self, parent, table_num):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"撤台", pos=wx.DefaultPosition,
                           size=wx.Size(300, 200), style=wx.CAPTION)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_ui(sizer)
        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.btnConfirm.Bind(wx.EVT_BUTTON, self.on_btn_confirm)
        self.btnCancel.Bind(wx.EVT_BUTTON, self.on_btn_cancel)

        # Initialize
        self.table_num = table_num
        self._init_data_view()

    def __del__(self):
        pass

    def _init_data_view(self):
        self.txtTableNum.Enable(False)
        self.txtTableName.Enable(False)
        table_item = CtrlTableInfo.get_instance().get_table_item(self.table_num)
        if table_item is not None:
            self.txtTableNum.SetValue(table_item.table_num)
            self.txtTableName.SetValue(table_item.table_name)

    # Virtual event handlers, override them in your derived class
    def on_btn_confirm(self, event):
        CtrlTableInfo.get_instance().close_table(self.table_num)
        self.Close()

    def on_btn_cancel(self, event):
        self.Close()

###########################################################################
## Class WgtFrontPage
###########################################################################


class WgtFrontPage (wx.Panel):
    def _init_status_bar(self, parent):
        self.statusBarPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition,
                                       wx.Size(-1, 82), wx.TAB_TRAVERSAL)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add open table button
        self.btnOpenTable = ImgButton(self.statusBarPanel, u"open_table.png", u"s_open_table.png")
        # Add order dishes button
        self.btnOrderDishes = ImgButton(self.statusBarPanel, u"order_dishes.png", u"s_order_dishes.png")
        # Add checkout button
        self.btnCheckout = ImgButton(self.statusBarPanel, u"checkout.png", u"s_checkout.png")
        # Add change table button
        self.btnChangeTable = ImgButton(self.statusBarPanel, u"change_table.png", u"s_change_table.png")
        # Add status button
        self.btnCloseTable = ImgButton(self.statusBarPanel, u"close_table.png", u"s_close_table.png")
        # Add refresh button
        self.btnRefresh = ImgButton(self.statusBarPanel, u"refresh_table.png", u"s_refresh_table.png")
        # Add exit button
        self.btnExit = ImgButton(self.statusBarPanel, u"cancel.png", u"s_cancel.png")

        # Layout
        self.statusBarPanel.SetSizer(sizer)
        self.statusBarPanel.Layout()
        parent.Add(self.statusBarPanel, 1, wx.EXPAND, 5)

    def _init_data_info(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.dishesSelectorPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(560, 520), wx.TAB_TRAVERSAL)
        self.dishesSelectorPanel.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        sizer.Add(self.dishesSelectorPanel, 1, wx.EXPAND | wx.RIGHT, 5)

        self.tableInfoPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(300, 520), wx.TAB_TRAVERSAL)
        self.tableInfoPanel.SetBackgroundColour(wx.Colour(0xea, 0xd4, 0x99))

        table_info_sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_table_info(self.tableInfoPanel, table_info_sizer)
        self._init_data_view(self.tableInfoPanel, table_info_sizer)
        self._init_ctrl(self.tableInfoPanel, table_info_sizer)

        self.tableInfoPanel.SetSizer(table_info_sizer)
        self.tableInfoPanel.Layout()
        sizer.Add(self.tableInfoPanel, 1, wx.EXPAND, 5)
        # Add horizontal line
        s_horizontal_line = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        sizer.Add(s_horizontal_line, 0, wx.EXPAND | wx.ALL, 5)

        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_table_info(self, container, parent):
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.infoPanel = wx.Panel(container, wx.ID_ANY, wx.DefaultPosition, wx.Size(300, 230), wx.TAB_TRAVERSAL)
        info_sizer = wx.BoxSizer(wx.VERTICAL)

        # Add table number and table name sizer
        table_number_name_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add table number
        s_txt_table_num = wx.StaticText(self.infoPanel, wx.ID_ANY, u"餐桌号：", wx.DefaultPosition,
                                        wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_table_num.Wrap(-1)
        s_txt_table_num.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        table_number_name_sizer.Add(s_txt_table_num, 0, wx.ALIGN_CENTER, 5)

        self.txtTableNum = wx.StaticText(self.infoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                         wx.Size(100, -1), wx.ALIGN_CENTER)
        self.txtTableNum.Wrap(-1)
        self.txtTableNum.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        table_number_name_sizer.Add(self.txtTableNum, 0, wx.ALIGN_CENTER, 5)
        # Add table name
        s_txt_table_name = wx.StaticText(self.infoPanel, wx.ID_ANY, u"桌名：", wx.DefaultPosition,
                                         wx.Size(50, -1), wx.ALIGN_RIGHT)
        s_txt_table_name.Wrap(-1)
        s_txt_table_name.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        table_number_name_sizer.Add(s_txt_table_name, 0, wx.ALIGN_CENTER, 5)

        self.txtTableName = wx.StaticText(self.infoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                          wx.Size(60, -1), wx.ALIGN_CENTER)
        self.txtTableName.Wrap(-1)
        self.txtTableName.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        table_number_name_sizer.Add(self.txtTableName, 0, wx.ALIGN_CENTER, 5)

        info_sizer.Add(table_number_name_sizer, 1, wx.EXPAND, 5)
        # Add table type and table area sizer
        type_area_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add table type
        s_txt_table_type = wx.StaticText(self.infoPanel, wx.ID_ANY, u"桌类：", wx.DefaultPosition,
                                         wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_table_type.Wrap(-1)
        s_txt_table_type.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        type_area_sizer.Add(s_txt_table_type, 0, wx.ALIGN_CENTER, 5)

        self.txtTableType = wx.StaticText(self.infoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                          wx.Size(100, -1), wx.ALIGN_CENTER)
        self.txtTableType.Wrap(-1)
        self.txtTableType.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        type_area_sizer.Add(self.txtTableType, 0, wx.ALIGN_CENTER, 5)
        # Add table area
        s_txt_table_area = wx.StaticText(self.infoPanel, wx.ID_ANY, u"区域：", wx.DefaultPosition,
                                         wx.Size(50, -1), wx.ALIGN_RIGHT)
        s_txt_table_area.Wrap(-1)
        s_txt_table_area.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        type_area_sizer.Add(s_txt_table_area, 0, wx.ALIGN_CENTER, 5)

        self.txtTableArea = wx.StaticText(self.infoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                          wx.Size(60, -1), wx.ALIGN_CENTER)
        self.txtTableArea.Wrap(-1)
        self.txtTableArea.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        type_area_sizer.Add(self.txtTableArea, 0, wx.ALIGN_CENTER, 5)

        info_sizer.Add(type_area_sizer, 1, wx.EXPAND, 5)
        # Add horizontal line
        s_horizontal_line = wx.StaticLine(self.infoPanel, wx.ID_ANY, wx.DefaultPosition,
                                          wx.DefaultSize, wx.LI_HORIZONTAL)
        info_sizer.Add(s_horizontal_line, 0, wx.EXPAND | wx.ALL, 5)
        # Add order number and money sizer
        order_number_money_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add order number
        s_txt_order_num = wx.StaticText(self.infoPanel, wx.ID_ANY, u"单号：", wx.DefaultPosition,
                                        wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_order_num.Wrap(-1)
        s_txt_order_num.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        order_number_money_sizer.Add(s_txt_order_num, 0, wx.ALIGN_CENTER, 5)

        self.txtOrderNum = wx.StaticText(self.infoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                         wx.Size(100, -1), wx.ALIGN_CENTRE)
        self.txtOrderNum.Wrap(-1)
        self.txtOrderNum.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        order_number_money_sizer.Add(self.txtOrderNum, 0, wx.ALIGN_CENTER, 5)
        # Add waiter
        s_txt_waiter = wx.StaticText(self.infoPanel, wx.ID_ANY, u"服务员：", wx.DefaultPosition,
                                     wx.Size(50, -1), wx.ALIGN_RIGHT)
        s_txt_waiter.Wrap(-1)
        s_txt_waiter.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        order_number_money_sizer.Add(s_txt_waiter, 0, wx.ALIGN_CENTER, 5)

        self.txtWaiter = wx.StaticText(self.infoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                       wx.Size(60, -1), wx.ALIGN_CENTER)
        self.txtWaiter.Wrap(-1)
        self.txtWaiter.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        order_number_money_sizer.Add(self.txtWaiter, 0, wx.ALIGN_CENTER, 5)

        info_sizer.Add(order_number_money_sizer, 1, wx.EXPAND, 5)
        # Add person number and deposit
        person_number_deposit_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add customer
        s_txt_customer = wx.StaticText(self.infoPanel, wx.ID_ANY, u"人数：", wx.DefaultPosition,
                                       wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_customer.Wrap(-1)
        s_txt_customer.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        person_number_deposit_sizer.Add(s_txt_customer, 0, wx.ALIGN_CENTER, 5)

        self.txtPersonNum = wx.StaticText(self.infoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                          wx.Size(100, -1), wx.ALIGN_CENTER)
        self.txtPersonNum.Wrap(-1)
        self.txtPersonNum.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        person_number_deposit_sizer.Add(self.txtPersonNum, 0, wx.ALIGN_CENTER, 5)

        # Add deposit
        s_txt_deposit = wx.StaticText(self.infoPanel, wx.ID_ANY, u"押金：", wx.DefaultPosition,
                                      wx.Size(50, -1), wx.ALIGN_RIGHT)
        s_txt_deposit.Wrap(-1)
        s_txt_deposit.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        person_number_deposit_sizer.Add(s_txt_deposit, 0, wx.ALIGN_CENTER, 5)

        self.txtDeposit = wx.StaticText(self.infoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                        wx.Size(60, -1), wx.ALIGN_CENTER)
        self.txtDeposit.Wrap(-1)
        self.txtDeposit.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        person_number_deposit_sizer.Add(self.txtDeposit, 0, wx.ALIGN_CENTER, 5)

        info_sizer.Add(person_number_deposit_sizer, 1, wx.EXPAND, 5)

        # Add open table time sizer
        open_time_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add open table time
        s_txt_open_time = wx.StaticText(self.infoPanel, wx.ID_ANY, u"开台时间：", wx.DefaultPosition,
                                        wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_open_time.Wrap(-1)
        s_txt_open_time.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        open_time_sizer.Add(s_txt_open_time, 0, wx.ALIGN_CENTER, 5)

        self.txtOpenTime = wx.StaticText(self.infoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                         wx.Size(200, -1), wx.ALIGN_CENTER)
        self.txtOpenTime.Wrap(-1)
        self.txtOpenTime.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        open_time_sizer.Add(self.txtOpenTime, 0, wx.ALIGN_CENTER, 5)

        info_sizer.Add(open_time_sizer, 1, wx.EXPAND, 5)

        # Add memo sizer
        memo_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add memo
        s_txt_memo = wx.StaticText(self.infoPanel, wx.ID_ANY, u"备注：", wx.DefaultPosition,
                                   wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_memo.Wrap(-1)
        s_txt_memo.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        memo_sizer.Add(s_txt_memo, 0, wx.ALIGN_CENTER, 5)

        self.txtMemo = wx.StaticText(self.infoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                     wx.Size(200, -1), wx.ALIGN_CENTRE)
        self.txtMemo.Wrap(-1)
        self.txtMemo.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        memo_sizer.Add(self.txtMemo, 0, wx.ALIGN_CENTER, 5)

        info_sizer.Add(memo_sizer, 1, wx.EXPAND, 5)

        # Layout
        self.infoPanel.SetSizer(info_sizer)
        self.infoPanel.Layout()
        sizer.Add(self.infoPanel, 1, 0, 5)

        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_data_view(self, container, parent):
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.dataViewDishes = wx.dataview.DataViewCtrl(container, wx.ID_ANY, wx.DefaultPosition,
                                                       wx.Size(300, 220), 0)

        self.dataViewDishes.AppendTextColumn(u"行号", 0)
        self.dataViewDishes.AppendTextColumn(u"菜品名称", 1)
        self.dataViewDishes.AppendTextColumn(u"规格", 2)
        self.dataViewDishes.AppendTextColumn(u"单位", 3)
        self.dataViewDishes.AppendTextColumn(u"数量", 4)
        self.dataViewDishes.AppendTextColumn(u"退菜量", 5)
        self.dataViewDishes.AppendTextColumn(u"价格", 6)
        self.dataViewDishes.AppendTextColumn(u"实际金额", 7)
        self.dataViewDishes.SetBackgroundColour(wx.Colour(0xea, 0xd4, 0x99))
        sizer.Add(self.dataViewDishes, 0, 0, 5)

        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_ctrl(self, container, parent):
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.ctrlPanel = wx.Panel(container, wx.ID_ANY, wx.DefaultPosition, wx.Size(300, 100), wx.TAB_TRAVERSAL)
        ctrl_sizer = wx.BoxSizer(wx.VERTICAL)
        # Add customer number sizer
        customer_number_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add customer number
        s_txt_customer_num = wx.StaticText(self.ctrlPanel, wx.ID_ANY, u"当前消费人数：", wx.DefaultPosition,
                                           wx.Size(100, -1), wx.ALIGN_RIGHT)
        s_txt_customer_num.Wrap(-1)
        customer_number_sizer.Add(s_txt_customer_num, 0, wx.ALIGN_CENTER, 5)

        self.txtCustomerNum = wx.StaticText(self.ctrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                            wx.Size(60, -1), wx.ALIGN_CENTRE)
        self.txtCustomerNum.Wrap(-1)
        customer_number_sizer.Add(self.txtCustomerNum, 0, wx.ALIGN_CENTER, 5)

        ctrl_sizer.Add(customer_number_sizer, 1, wx.EXPAND, 5)
        # Add amount of consumption sizer
        amount_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add amount of consumption
        s_txt_amount = wx.StaticText(self.ctrlPanel, wx.ID_ANY, u"当前消费金额：", wx.DefaultPosition,
                                     wx.Size(100, -1), wx.ALIGN_RIGHT)
        s_txt_amount.Wrap(-1)
        amount_sizer.Add(s_txt_amount, 0, wx.ALIGN_CENTER, 5)

        self.txtAmount = wx.StaticText(self.ctrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                       wx.Size(60, -1), wx.ALIGN_CENTRE)
        self.txtAmount.Wrap(-1)
        amount_sizer.Add(self.txtAmount, 0, wx.ALIGN_CENTER, 5)

        ctrl_sizer.Add(amount_sizer, 1, wx.EXPAND, 5)

        # Layout
        self.ctrlPanel.SetSizer(ctrl_sizer)
        self.ctrlPanel.Layout()
        sizer.Add(self.ctrlPanel, 1, wx.ALL, 5)
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition,
                          size=wx.Size(800, 600), style=wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(0x51, 0x1c, 0x0a))

        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_status_bar(sizer)
        self._init_data_info(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.btnOpenTable.Bind(wx.EVT_BUTTON, self.on_btn_open_table)
        self.btnOrderDishes.Bind(wx.EVT_BUTTON, self.on_btn_order_dishes)
        self.btnCheckout.Bind(wx.EVT_BUTTON, self.on_btn_checkout)
        self.btnChangeTable.Bind(wx.EVT_BUTTON, self.on_btn_change_table)
        self.btnRefresh.Bind(wx.EVT_BUTTON, self.on_btn_refresh)
        self.btnCloseTable.Bind(wx.EVT_BUTTON, self.on_btn_close_table)
        self.btnExit.Bind(wx.EVT_BUTTON, parent.on_exit)

        # Create an instance of our model...
        table_num = CtrlTableInfo.get_instance().get_selected_item_id()
        order_num = CtrlTableInfo.get_instance().get_order_num(table_num)
        self.model = ModelOrderedDishes(CtrlOrderInfo.get_instance().get_order_dishes_items(order_num))
        # Tell the DVC to use the model
        self.dataViewDishes.AssociateModel(self.model)

        # initialize
        self.tableBtnMap = dict()

    def __del__(self):
        pass

    def initialize(self):
        # Add event listener
        EvtManager.add_listener(self, EnumEvent.EVT_FRONT_PAGE_REFRESH, self.on_refresh)

        x, y = CtrlHomePage.get_instance().get_screen_size()
        self.SetSize(wx.Size(x, y))

        self.GetParent().SetTitle(u"收银")

    def un_initialize(self):
        # Remove event listener
        EvtManager.remove_listener(self, EnumEvent.EVT_FRONT_PAGE_REFRESH, self.on_refresh)
        pass

    # Virtual event handlers, override them in your derived class
    def on_paint(self, event):
        dc = wx.ClientDC(self.statusBarPanel)
        dc.Clear()

        sz = self.GetClientSize()
        bg_img = wx.Image(sys.path[0] + "\\..\\image\\top_bg.png", wx.BITMAP_TYPE_PNG).Scale(sz.x, 82)
        bg_bmp = bg_img.ConvertToBitmap()

        mem_dc = wx.MemoryDC()
        mem_dc.SelectObject(bg_bmp)
        dc.Blit(0, 0,
                bg_bmp.GetWidth(), bg_bmp.GetHeight(),
                mem_dc, 0, 0, wx.COPY, True)

    def on_size(self, event):
        event.Skip()
        x, y = self.GetSize()

        self.btnOpenTable.SetSize(wx.Size(63, 70))
        self.btnOpenTable.SetPosition(wx.Point(0, 6))

        self.btnOrderDishes.SetSize(wx.Size(65, 70))
        self.btnOrderDishes.SetPosition(wx.Point(65, 6))

        self.btnCheckout.SetSize(wx.Size(63, 70))
        self.btnCheckout.SetPosition(wx.Point(130, 6))

        self.btnChangeTable.SetSize(wx.Size(63, 70))
        self.btnChangeTable.SetPosition(wx.Point(195, 6))

        self.btnRefresh.SetSize(wx.Size(103, 70))
        self.btnRefresh.SetPosition(wx.Point(260, 6))

        self.btnCloseTable.SetSize(wx.Size(63, 70))
        self.btnCloseTable.SetPosition(wx.Point(365, 6))

        self.btnExit.SetSize(wx.Size(63, 70))
        self.btnExit.SetPosition(wx.Point(430, 6))

        self.statusBarPanel.SetSize(wx.Size(x, 82))
        self.dishesSelectorPanel.SetMinSize(wx.Size(x-300, y-82))
        self.tableInfoPanel.SetMinSize(wx.Size(290, y-82))
        self.dataViewDishes.SetMinSize(wx.Size(290, y-372))

        self.Refresh()

        self._show_table_buttons(x-300, y-82)

    def on_btn_open_table(self, event):
        event.Skip()
        selected_table_num = CtrlTableInfo.get_instance().get_selected_item_id()
        if selected_table_num is None:
            dlg = wx.MessageDialog(self, u"请选择餐桌", caption=u"开台")
            dlg.ShowModal()
        else:
            item = CtrlTableInfo.get_instance().get_table_item(selected_table_num)
            if item is not None and item.table_status == 0:
                pop_open_table = PopOpenTable(self, selected_table_num)
                pop_open_table.ShowModal()
            else:
                dlg = wx.MessageDialog(self, u"此桌已经开台", caption=u"开台")
                dlg.ShowModal()

    def on_btn_order_dishes(self, event):
        event.Skip()
        selected_table_num = CtrlTableInfo.get_instance().get_selected_item_id()
        if selected_table_num is None:
            dlg = wx.MessageDialog(self, u"请选择餐桌", caption=u"点菜")
            dlg.ShowModal()
        else:
            item = CtrlTableInfo.get_instance().get_table_item(selected_table_num)
            if item is not None and item.table_status != 0:
                order_num = CtrlTableInfo.get_instance().get_order_num(selected_table_num)
                if order_num is not None:
                    CtrlOrderInfo.get_instance().create_order(order_num, item.table_status)
                    AppManager.get_instance().switch_to_application('OrderDishes')
            else:
                dlg = wx.MessageDialog(self, u"此桌未开台", caption=u"点菜")
                dlg.ShowModal()

    def on_btn_checkout(self, event):
        event.Skip()
        selected_table_num = CtrlTableInfo.get_instance().get_selected_item_id()
        if selected_table_num is None:
            dlg = wx.MessageDialog(self, u"请选择餐桌", caption=u"结算")
            dlg.ShowModal()
        else:
            item = CtrlTableInfo.get_instance().get_table_item(selected_table_num)
            if item is not None and item.table_status == 2:
                order_num = CtrlTableInfo.get_instance().get_order_num(selected_table_num)
                CtrlOrderInfo.get_instance().create_order(order_num, item.table_status)
                AppManager.get_instance().switch_to_application('CheckOut')
            else:
                dlg = wx.MessageDialog(self, u"此桌未点菜", caption=u"结算")
                dlg.ShowModal()

    def on_btn_change_table(self, event):
        event.Skip()
        selected_table_num = CtrlTableInfo.get_instance().get_selected_item_id()
        if selected_table_num is None:
            dlg = wx.MessageDialog(self, u"请选择餐桌", caption=u"转台")
            dlg.ShowModal()
        else:
            item = CtrlTableInfo.get_instance().get_table_item(selected_table_num)
            if item is not None and item.table_status != 0:
                pop_change_table = PopChangeTable(self, item.table_num)
                pop_change_table.ShowModal()
            else:
                dlg = wx.MessageDialog(self, u"此桌未开台", caption=u"转台")
                dlg.ShowModal()

    def on_btn_refresh(self, event):
        CtrlTableInfo.get_instance().refresh_table_items()

    def on_refresh(self, event):
        self._refresh_table_info()
        self._refresh_dishes_view()
        self._set_focus_table()

    def on_btn_close_table(self, event):
        selected_table_num = CtrlTableInfo.get_instance().get_selected_item_id()
        if selected_table_num is None:
            dlg = wx.MessageDialog(self, u"请选择餐桌", caption=u"撤台")
            dlg.ShowModal()
        else:
            item = CtrlTableInfo.get_instance().get_table_item(selected_table_num)
            if item is not None and (item.table_status == 1 or item.table_status == 3):
                pop_close_table = PopCloseTable(self, selected_table_num)
                pop_close_table.ShowModal()
            else:
                dlg = wx.MessageDialog(self, u"此桌未开台或未结账", caption=u"撤台")
                dlg.ShowModal()

    def on_btn_table(self, event):
        event.Skip()
        selected_table_num = event.GetId()
        win_id = CtrlTableInfo.get_instance().get_selected_item_id()
        if win_id is not None:
            btn_label = self.tableBtnMap[win_id].GetLabel()
            index_ = btn_label.index(u'√        ' + '\r\n')
            if index_ == 0:
                self.tableBtnMap[win_id].SetLabel(btn_label[9:])
        CtrlTableInfo.get_instance().set_selected_item_id(selected_table_num)
        self.tableBtnMap[selected_table_num].SetLabel(u'√        ' + self.tableBtnMap[selected_table_num].GetLabel())
        self.tableBtnMap[selected_table_num].Refresh()

        self._show_table_info()
        self._refresh_dishes_view()

    def _set_focus_table(self):
        selected_table_num = CtrlTableInfo.get_instance().get_selected_table_num()
        if selected_table_num is not None:
            if self.tableBtnMap[selected_table_num].GetLabel().find(u'√') == -1:
                CtrlTableInfo.get_instance().set_selected_item_id(selected_table_num)
                self.tableBtnMap[selected_table_num].SetLabel(u'√        ' +
                                                              self.tableBtnMap[selected_table_num].GetLabel())
                self.tableBtnMap[selected_table_num].Refresh()

    def _show_table_info(self):
        self.txtOrderNum.SetLabel('')
        self.txtTableNum.SetLabel('')
        self.txtTableName.SetLabel('')
        self.txtTableType.SetLabel('')
        self.txtTableArea.SetLabel('')
        self.txtOpenTime.SetLabel('')
        self.txtWaiter.SetLabel('')
        self.txtPersonNum.SetLabel('')
        self.txtDeposit.SetLabel('')
        self.txtMemo.SetLabel('')
        self.txtCustomerNum.SetLabel('')

        table_num = CtrlTableInfo.get_instance().get_selected_item_id()
        if table_num is None:
            return

        try:
            # Show table info
            table_item = CtrlTableInfo.get_instance().get_table_item(table_num)
            self.txtTableNum.SetLabel(table_item.table_num)
            self.txtTableName.SetLabel(table_item.table_name)
            self.txtTableType.SetLabel(table_item.table_type)
            self.txtTableArea.SetLabel(table_item.table_area)
            if table_item.table_status != 0:
                self.txtOrderNum.SetLabel(table_item.order_num)
                self.txtOpenTime.SetLabel(table_item.open_time)
                self.txtWaiter.SetLabel(table_item.waiter)
                self.txtPersonNum.SetLabel(str(table_item.people_num))
                self.txtDeposit.SetLabel(table_item.deposit)
                self.txtMemo.SetLabel(table_item.memo)
                self.txtCustomerNum.SetLabel(str(table_item.customer_num))

            # Show dishes order info
            order_num = CtrlTableInfo.get_instance().get_order_num(table_num)
            if order_num is not None:
                order_item = CtrlOrderInfo.get_instance().get_order_item(order_num)
                if order_item is not None:
                    self.txtAmount.SetLabel(str(order_item.order_money))
        except:
            pass

    @staticmethod
    def _get_table_title(table_code, people_num, amount, selected=False):
        selected_flag = u''
        if selected:
            selected_flag = u'√        '
        if amount is not None:
            return selected_flag + '\r\n' + table_code + '\r\n' + str(people_num) + u'人桌' \
                                 + '\r\n' + u'￥ ' + str(amount)
        else:
            return selected_flag + '\r\n' + table_code + '\r\n' + str(people_num) + u'人桌' + '\r\n'

    def _show_table_buttons(self, x, y):
        column = x / 82
        row = y / 82
        for (k, v) in self.tableBtnMap.items():
            self.Unbind(wx.EVT_BUTTON, v, handler=self.on_btn_table)
            v.Destroy()
        self.tableBtnMap.clear()

        table_items = CtrlTableInfo.get_instance().get_table_items()
        for i in range(0, row):
            for j in range(0, column):
                index_ = i*column+j
                if index_ >= len(table_items):
                    break
                item = table_items[index_]
                win_id = int(item.table_num)
                btn_title = self._get_table_title(item.table_name,
                                                  item.customer_num if item.table_status != 0 else item.people_num,
                                                  item.amount, item.is_selected)
                self.tableBtnMap[win_id] = wx.Button(self.dishesSelectorPanel, win_id, btn_title,
                                                     (2+j*82, 2+i*82), wx.Size(80, 80), wx.STATIC_BORDER)
                if item.table_status == 0:
                    self.tableBtnMap[win_id].SetBackgroundColour(wx.Colour(198, 220, 147))
                elif item.table_status == 1:
                    self.tableBtnMap[win_id].SetBackgroundColour(wx.Colour(237, 113, 79))
                elif item.table_status == 2:
                    self.tableBtnMap[win_id].SetBackgroundColour(wx.Colour(72, 173, 253))
                elif item.table_status == 3:
                    self.tableBtnMap[win_id].SetBackgroundColour(wx.Colour(252, 219, 52))

                self.Bind(wx.EVT_BUTTON, self.on_btn_table, self.tableBtnMap[win_id])

        self._show_table_info()
        self._refresh_dishes_view()

    def _refresh_table_info(self):
        x, y = self.GetSize()
        self._show_table_buttons(x-300, y-82)

    def _refresh_dishes_view(self):
        # Refresh data view list
        table_num = CtrlTableInfo.get_instance().get_selected_item_id()
        order_num = CtrlTableInfo.get_instance().get_order_num(table_num)
        table_item = CtrlTableInfo.get_instance().get_table_item(table_num)
        if table_item is not None and table_item.table_status == 2:
            CtrlOrderInfo.get_instance().create_order(order_num, 2)

        result = CtrlOrderInfo.get_instance().get_order_dishes_items(order_num)
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.dataViewDishes.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)

        self.model.Cleared()

        self.txtAmount.SetLabel('')
        order_item = CtrlOrderInfo.get_instance().get_order_item(order_num)
        if order_item is not None:
            self.txtAmount.SetLabel(str((order_item.place_money * order_item.all_discount) - order_item.free_price))

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = WgtFrontPage(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()
