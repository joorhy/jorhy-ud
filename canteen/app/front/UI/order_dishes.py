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
from app.front.logic.model import ModelOrderedDishes

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class PopDeleteDishes
###########################################################################


class PopDeleteDishes (wx.Dialog):
    def _init_ui(self, parent):
        # Add dishes info
        dishes_info_sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)
        dishes_info_sizer.SetMinSize(wx.Size(-1, 120))
        # Add dishes name sizer
        dishes_name_sizer = wx.BoxSizer(wx.HORIZONTAL)
        s_txt_dishes_name = wx.StaticText(self, wx.ID_ANY, u"菜品名称：", wx.DefaultPosition,
                                          wx.Size(100, -1), wx.ALIGN_RIGHT)
        s_txt_dishes_name.Wrap(-1)
        dishes_name_sizer.Add(s_txt_dishes_name, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtDishesName = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        dishes_name_sizer.Add(self.txtDishesName, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        dishes_info_sizer.Add(dishes_name_sizer, 1, wx.EXPAND, 5)

        # Add dishes count sizer
        dishes_count_sizer = wx.BoxSizer(wx.HORIZONTAL)

        s_txt_dishes_count = wx.StaticText(self, wx.ID_ANY, u"菜品数量：", wx.DefaultPosition,
                                           wx.Size(100, -1), wx.ALIGN_RIGHT)
        s_txt_dishes_count.Wrap(-1)
        dishes_count_sizer.Add(s_txt_dishes_count, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtDishesCount = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        dishes_count_sizer.Add(self.txtDishesCount, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        dishes_info_sizer.Add(dishes_count_sizer, 1, wx.EXPAND, 5)

        parent.Add(dishes_info_sizer, 1, wx.EXPAND, 5)

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

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"删菜操作", pos=wx.DefaultPosition,
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
        self._init_data_view()

    def __del__(self):
        pass

    def _init_data_view(self):
        self.txtDishesName.Enable(False)
        self.txtDishesCount.Enable(False)
        ordered_dishes_item = CtrlOrderInfo.get_instance().get_select_dishes_item()
        if ordered_dishes_item is not None:
            self.txtDishesName.SetValue(ordered_dishes_item.dishes_name)
            self.txtDishesCount.SetValue(str(ordered_dishes_item.dishes_count))

    # Virtual event handlers, override them in your derived class
    def on_btn_confirm(self, event):
        CtrlOrderInfo.get_instance().delete_dishes()
        self.Close()

    def on_btn_cancel(self, event):
        self.Close()

###########################################################################
## Class PopSeatSetting
###########################################################################


class PopSeatSetting (wx.Dialog):
    def _init_ui(self, parent):
        # Add seat number info
        seat_num_sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.HORIZONTAL)
        seat_num_sizer.SetMinSize(wx.Size(-1, 120))

        s_txt_seat_num = wx.StaticText(self, wx.ID_ANY, u"席位数量：", wx.DefaultPosition,
                                       wx.Size(100, -1), wx.ALIGN_RIGHT)
        s_txt_seat_num.Wrap(-1)
        seat_num_sizer.Add(s_txt_seat_num, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtSeatNum = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        seat_num_sizer.Add(self.txtSeatNum, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        parent.Add(seat_num_sizer, 1, wx.EXPAND, 5)

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

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"删菜操作", pos=wx.DefaultPosition,
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

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def on_btn_confirm(self, event):
        self.Close()

    def on_btn_cancel(self, event):
        self.Close()

###########################################################################
## Class PopPlaceOrder
###########################################################################


class PopPlaceOrder (wx.Dialog):
    def _init_ui(self, parent):
        # Add order info
        order_info_sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)
        order_info_sizer.SetMinSize(wx.Size(-1, 120))
        # Add order number sizer
        order_num_sizer = wx.BoxSizer(wx.HORIZONTAL)
        s_txt_order_num = wx.StaticText(self, wx.ID_ANY, u"单号：", wx.DefaultPosition,
                                        wx.Size(100, -1), wx.ALIGN_RIGHT)
        s_txt_order_num.Wrap(-1)
        order_num_sizer.Add(s_txt_order_num, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtOrderNum = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        order_num_sizer.Add(self.txtOrderNum, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        order_info_sizer.Add(order_num_sizer, 1, wx.EXPAND, 5)

        # Add money sizer
        money_sizer = wx.BoxSizer(wx.HORIZONTAL)

        s_txt_money = wx.StaticText(self, wx.ID_ANY, u"金额：", wx.DefaultPosition,
                                                 wx.Size(100, -1), wx.ALIGN_RIGHT)
        s_txt_money.Wrap(-1)
        money_sizer.Add(s_txt_money, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtMoney = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        money_sizer.Add(self.txtMoney, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        order_info_sizer.Add(money_sizer, 1, wx.EXPAND, 5)

        parent.Add(order_info_sizer, 1, wx.EXPAND, 5)

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

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"落单操作", pos=wx.DefaultPosition,
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
        self.table_item = None
        self._init_data_view()

    def __del__(self):
        pass

    def _init_data_view(self):
        self.txtOrderNum.Enable(False)
        self.txtMoney.Enable(False)
        table_num = CtrlTableInfo.get_instance().get_selected_item_id()
        if table_num is not None:
            self.table_item = CtrlTableInfo.get_instance().get_table_item(table_num)
            if self.table_item is not None:
                self.txtOrderNum.SetValue(self.table_item.order_num if self.table_item.order_num is not None else "")

        order_id = CtrlOrderInfo.get_instance().get_cur_order_id()
        if order_id is not None:
            order_item = CtrlOrderInfo.get_instance().get_order_item(order_id)
            if order_item is not None:
                self.txtMoney.SetValue(str(order_item.order_money))

    # Virtual event handlers, override them in your derived class
    def on_btn_confirm(self, event):
        if self.table_item is not None:
            CtrlOrderInfo.get_instance().place_order(self.table_item.table_id, self.table_item.order_id)
        self.Close()

    def on_btn_cancel(self, event):
        self.Close()

###########################################################################
## Class PopOrderDishes
###########################################################################


class PopOrderDishes (wx.Dialog):
    def _init_ui(self, parent):
        # Add data view sizer
        view_sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)
        view_sizer.SetMinSize(wx.Size(-1, 300))
        # Add dishes info sizer
        dishes_info_sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        # Add dishes sizer
        dishes_sizer = wx.BoxSizer(wx.HORIZONTAL)
        s_txt_name = wx.StaticText(self, wx.ID_ANY, u"菜品名称：", wx.DefaultPosition,
                                   wx.Size(80, -1), wx.ALIGN_RIGHT)
        s_txt_name.Wrap(-1)
        dishes_sizer.Add(s_txt_name, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtDishesName = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        dishes_sizer.Add(self.txtDishesName, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        s_txt_count = wx.StaticText(self, wx.ID_ANY, u"菜品数量：", wx.DefaultPosition,
                                    wx.Size(80, -1), wx.ALIGN_RIGHT)
        s_txt_count.Wrap(-1)
        dishes_sizer.Add(s_txt_count, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtDishesCount = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        dishes_sizer.Add(self.txtDishesCount, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        dishes_info_sizer.Add(dishes_sizer, 1, wx.EXPAND, 5)

        # Add price info sizer
        price_sizer = wx.BoxSizer(wx.HORIZONTAL)

        s_txt_price = wx.StaticText(self, wx.ID_ANY, u"价格：", wx.DefaultPosition,
                                         wx.Size(80, -1), wx.ALIGN_RIGHT)
        s_txt_price.Wrap(-1)
        price_sizer.Add(s_txt_price, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtNormalPrice = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        price_sizer.Add(self.txtNormalPrice, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        s_txt_add = wx.StaticText(self, wx.ID_ANY, u"加价：", wx.DefaultPosition, wx.Size(80, -1), wx.ALIGN_RIGHT)
        s_txt_add.Wrap(-1)
        price_sizer.Add(s_txt_add, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtAddPrice = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        price_sizer.Add(self.txtAddPrice, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        dishes_info_sizer.Add(price_sizer, 1, wx.EXPAND, 5)

        # Add demand sizer
        demand_sizer = wx.BoxSizer(wx.HORIZONTAL)

        s_txt_spec = wx.StaticText(self, wx.ID_ANY, u"规格：", wx.DefaultPosition, wx.Size(80, -1), wx.ALIGN_RIGHT)
        s_txt_spec.Wrap(-1)
        demand_sizer.Add(s_txt_spec, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        choice_spec = list()
        self.choiceSpec = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_spec, 0)
        self.choiceSpec.SetSelection(0)
        demand_sizer.Add(self.choiceSpec, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        s_txt_style = wx.StaticText(self, wx.ID_ANY, u"做法：", wx.DefaultPosition, wx.Size(80, -1), wx.ALIGN_RIGHT)
        s_txt_style.Wrap(-1)
        demand_sizer.Add(s_txt_style, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        choice_style = list()
        self.choiceStyle = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_style, 0)
        self.choiceStyle.SetSelection(0)
        demand_sizer.Add(self.choiceStyle, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        dishes_info_sizer.Add(demand_sizer, 1, wx.EXPAND, 5)

        view_sizer.Add(dishes_info_sizer, 1, wx.EXPAND, 5)

        # Add special info sizer
        special_info_sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"特殊做法：" ), wx.VERTICAL)

        self.txtSpecial = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.Size(-1, 120), wx.TE_MULTILINE)
        special_info_sizer.Add(self.txtSpecial, 0, wx.ALL | wx.EXPAND, 5)

        view_sizer.Add(special_info_sizer, 1, wx.EXPAND, 5)

        # Layout view sizer
        parent.Add(view_sizer, 1, wx.EXPAND, 5)

        # Add control sizer
        ctrl_sizer = wx.BoxSizer(wx.HORIZONTAL)

        ctrl_sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        self.btnConfirm = wx.Button(self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0)
        ctrl_sizer.Add(self.btnConfirm, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.btnCancel = wx.Button(self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0)
        ctrl_sizer.Add(self.btnCancel, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        parent.Add(ctrl_sizer, 1, wx.EXPAND, 5)

    def __init__(self, parent, type):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"点菜操作", pos=wx.DefaultPosition,
                           size=wx.Size(500, 400), style=wx.CAPTION)

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
        self.type = type

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def on_btn_confirm(self, event):
        self.Close()

    def on_btn_cancel(self, event):
        self.Close()

###########################################################################
## Class PopDeleteDishes
###########################################################################


class PopModDishesNum (wx.Dialog):
    def _init_ui(self, parent):
        # Add dishes info
        dishes_info_sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)
        dishes_info_sizer.SetMinSize(wx.Size(-1, 120))
        # Add dishes name sizer
        dishes_name_sizer = wx.BoxSizer(wx.HORIZONTAL)
        s_txt_dishes_name = wx.StaticText(self, wx.ID_ANY, u"菜品名称：", wx.DefaultPosition,
                                          wx.Size(100, -1), wx.ALIGN_RIGHT)
        s_txt_dishes_name.Wrap(-1)
        dishes_name_sizer.Add(s_txt_dishes_name, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtDishesName = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        dishes_name_sizer.Add(self.txtDishesName, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        dishes_info_sizer.Add(dishes_name_sizer, 1, wx.EXPAND, 5)

        # Add dishes count sizer
        dishes_count_sizer = wx.BoxSizer(wx.HORIZONTAL)

        s_txt_dishes_count = wx.StaticText(self, wx.ID_ANY, u"菜品数量：", wx.DefaultPosition,
                                           wx.Size(100, -1), wx.ALIGN_RIGHT)
        s_txt_dishes_count.Wrap(-1)
        dishes_count_sizer.Add(s_txt_dishes_count, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtDishesCount = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        dishes_count_sizer.Add(self.txtDishesCount, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        dishes_info_sizer.Add(dishes_count_sizer, 1, wx.EXPAND, 5)

        parent.Add(dishes_info_sizer, 1, wx.EXPAND, 5)

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

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"修改数量", pos=wx.DefaultPosition,
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
        self._init_data_view()

    def __del__(self):
        pass

    def _init_data_view(self):
        self.txtDishesName.Enable(False)
        self.txtDishesCount.Enable(False)
        ordered_dishes_item = CtrlOrderInfo.get_instance().get_select_dishes_item()
        if ordered_dishes_item is not None:
            self.txtDishesName.SetValue(ordered_dishes_item.dishes_name)
            self.txtDishesCount.SetValue(str(ordered_dishes_item.dishes_count))

    # Virtual event handlers, override them in your derived class
    def on_btn_confirm(self, event):
        CtrlOrderInfo.get_instance().delete_dishes()
        self.Close()

    def on_btn_cancel(self, event):
        self.Close()

###########################################################################
## Class WgtOrderDishes
###########################################################################


class WgtOrderDishes (wx.Panel):
    def _init_status_bar(self, parent):
        self.statusBarPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition,
                                       wx.Size(-1, 60), wx.RAISED_BORDER | wx.TAB_TRAVERSAL)
        self.statusBarPanel.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.statusBarPanel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add delete dishes button
        self.btnDeleteDishes = wx.Button(self.statusBarPanel, wx.ID_ANY, u"删菜", wx.DefaultPosition, wx.Size(60, 60), 0)
        sizer.Add(self.btnDeleteDishes, 0, 0, 5)
        # Add seat button
        self.btnSeat = wx.Button(self.statusBarPanel, wx.ID_ANY, u"席位", wx.DefaultPosition, wx.Size(60, 60), 0)
        sizer.Add(self.btnSeat, 0, 0, 5)
        # Add place order button
        self.btnPlaceOrder = wx.Button(self.statusBarPanel, wx.ID_ANY, u"落单", wx.DefaultPosition, wx.Size(60, 60), 0)
        sizer.Add(self.btnPlaceOrder, 0, 0, 5)
        # Add vertical line
        s_vertical_line = wx.StaticLine(self.statusBarPanel, wx.ID_ANY, wx.DefaultPosition,
                                        wx.DefaultSize, wx.LI_VERTICAL)
        sizer.Add(s_vertical_line, 0, wx.EXPAND | wx.ALL, 5)
        # Add exit button
        self.btnExit = wx.Button(self.statusBarPanel, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.Size(60, 60), 0)
        sizer.Add(self.btnExit, 0, 0, 5)

        # Layout
        self.statusBarPanel.SetSizer(sizer)
        self.statusBarPanel.Layout()
        parent.Add(self.statusBarPanel, 1, wx.EXPAND, 5)

    def _init_view_info(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self._init_data_view_list(sizer)
        self._init_order_info(sizer)

        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_data_view_list(self, parent):
        self.dataViewPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(400, 520), wx.TAB_TRAVERSAL)
        self.dataViewPanel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOBK))

        sizer = wx.BoxSizer(wx.VERTICAL)
        # Add data view list control
        self.dataViewCtrl = wx.dataview.DataViewCtrl(self.dataViewPanel, wx.ID_ANY, wx.DefaultPosition,
                                                     wx.Size(400, 520), 0)
        self.dataViewCtrl.AppendTextColumn(u"行号", 0)
        self.dataViewCtrl.AppendTextColumn(u"菜品名称", 1)
        self.dataViewCtrl.AppendTextColumn(u"规格", 2)
        self.dataViewCtrl.AppendTextColumn(u"单位", 3)
        self.dataViewCtrl.AppendTextColumn(u"数量", 4)
        self.dataViewCtrl.AppendTextColumn(u"退菜量", 5)
        self.dataViewCtrl.AppendTextColumn(u"价格", 6)
        self.dataViewCtrl.AppendTextColumn(u"实际金额", 7)
        sizer.Add(self.dataViewCtrl, 0, 0, 5)

        # Layout
        self.dataViewPanel.SetSizer(sizer)
        self.dataViewPanel.Layout()
        parent.Add(self.dataViewPanel, 1, wx.EXPAND | wx.TOP, 5)

    def _init_order_info(self, parent):
        self.orderPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(400, 520), wx.TAB_TRAVERSAL)
        self.orderPanel.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.orderPanel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))

        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_dishes_search_ctrl(self.orderPanel, sizer)
        self._init_dishes_info_ctrl(self.orderPanel, sizer)

        self.orderPanel.SetSizer(sizer)
        self.orderPanel.Layout()
        parent.Add(self.orderPanel, 1, wx.EXPAND | wx.LEFT | wx.TOP, 5)

    def _init_dishes_search_ctrl(self, container, parent):
        self.ctrlPanel = wx.Panel(container, wx.ID_ANY, wx.DefaultPosition, wx.Size(380, 180), wx.TAB_TRAVERSAL)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Add search title sizer
        search_title_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add search title
        s_txt_search_title = wx.StaticText(self.ctrlPanel, wx.ID_ANY, u"菜品名称：", wx.DefaultPosition,
                                           wx.Size(80, -1), 0)
        s_txt_search_title.Wrap(-1)
        search_title_sizer.Add(s_txt_search_title, 0, wx.ALIGN_CENTER, 5)
        # Add search content
        self.txtDishesCode = wx.TextCtrl(self.ctrlPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.Size(300, -1), 0)
        search_title_sizer.Add(self.txtDishesCode, 0, wx.ALIGN_CENTER, 5)
        sizer.Add(search_title_sizer, 1, wx.EXPAND, 5)

        # Add control sizer
        ctrl_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add add ordered dishes number button
        self.btnAddDishes = wx.Button(self.ctrlPanel, wx.ID_ANY, u"数量加", wx.DefaultPosition, wx.Size(95, -1), 0)
        ctrl_sizer.Add(self.btnAddDishes, 0, 0, 5)
        # Add del ordered dishes number button
        self.btnDelDishes = wx.Button(self.ctrlPanel, wx.ID_ANY, u"数量减", wx.DefaultPosition, wx.Size(95, -1), 0)
        ctrl_sizer.Add(self.btnDelDishes, 0, 0, 5)
        # Add mod ordered dishes number button
        self.btnModDishes = wx.Button(self.ctrlPanel, wx.ID_ANY, u"数量改", wx.DefaultPosition, wx.Size(95, -1), 0)
        ctrl_sizer.Add(self.btnModDishes, 0, 0, 5)
        # Add special demand button
        self.btnSpecialDemand = wx.Button(self.ctrlPanel, wx.ID_ANY, u"特殊做法", wx.DefaultPosition,
                                          wx.Size(95, -1), 0)
        ctrl_sizer.Add(self.btnSpecialDemand, 0, 0, 5)
        sizer.Add(ctrl_sizer, 1, wx.EXPAND, 5)

        # Add table info sizer
        table_info_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add dishes table code
        s_txt_table_code = wx.StaticText(self.ctrlPanel, wx.ID_ANY, u"餐桌：", wx.DefaultPosition,
                                         wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_table_code.Wrap(-1)
        table_info_sizer.Add(s_txt_table_code, 0, wx.ALIGN_CENTER, 5)

        self.txtTableCode = wx.StaticText(self.ctrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                          wx.Size(100, -1), wx.ALIGN_CENTER)
        self.txtTableCode.Wrap(-1)
        table_info_sizer.Add(self.txtTableCode, 0, wx.ALIGN_CENTER, 5)

        # Add customer number
        s_txt_customer_num = wx.StaticText(self.ctrlPanel, wx.ID_ANY, u"人数：", wx.DefaultPosition,
                                           wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_customer_num.Wrap(-1)
        table_info_sizer.Add(s_txt_customer_num, 0, wx.ALIGN_CENTER, 5)

        self.txtCustomerNum = wx.StaticText(self.ctrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                            wx.Size(60, -1), wx.ALIGN_RIGHT)
        self.txtCustomerNum.Wrap(-1)
        table_info_sizer.Add(self.txtCustomerNum, 0, wx.ALIGN_CENTER, 5)

        sizer.Add(table_info_sizer, 1, wx.EXPAND, 5)
        # Add customer info sizer
        customer_info_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Add memo
        s_txt_memo = wx.StaticText(self.ctrlPanel, wx.ID_ANY, u"备注：", wx.DefaultPosition,
                                   wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_memo.Wrap(-1)
        customer_info_sizer.Add(s_txt_memo, 0, wx.ALIGN_CENTER, 5)

        self.txtMemo = wx.StaticText(self.ctrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                     wx.Size(200, -1), wx.ALIGN_CENTRE)
        self.txtMemo.Wrap(-1)
        customer_info_sizer.Add(self.txtMemo, 0, wx.ALIGN_CENTER, 5)
        sizer.Add(customer_info_sizer, 1, wx.EXPAND, 5)

        # Layout
        self.ctrlPanel.SetSizer(sizer)
        self.ctrlPanel.Layout()
        parent.Add(self.ctrlPanel, 1, wx.EXPAND | wx.ALL, 5)

    def _init_dishes_info_ctrl(self, container, parent):
        self.dishesPanel = wx.Panel(container, wx.ID_ANY, wx.DefaultPosition, wx.Size(380, 370), wx.TAB_TRAVERSAL)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add dishes list panel
        self.dishesListPanel = wx.Panel(self.dishesPanel, wx.ID_ANY, wx.DefaultPosition,
                                        wx.Size(322, 370), wx.STATIC_BORDER | wx.TAB_TRAVERSAL)
        # Add dishes control button
        self.btnDishesUp = None
        self.btnDishesDown = None
        # Layout dishes list control
        self.dishesListPanel.Layout()
        sizer.Add(self.dishesListPanel, 1, 0, 5)
        # Add dishes type panel
        self.dishesTypePanel = wx.Panel(self.dishesPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size(55, 370),
                                        wx.STATIC_BORDER | wx.TAB_TRAVERSAL)
        # Add dishes type control button
        self.btnTypeUp = None
        self.btnTypeDown = None
        # Layout dishes type control
        self.dishesTypePanel.Layout()
        sizer.Add(self.dishesTypePanel, 1, wx.EXPAND, 5)

        # Layout
        self.dishesPanel.SetSizer(sizer)
        self.dishesPanel.Layout()
        parent.Add(self.dishesPanel, 1, wx.EXPAND, 5)

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition,
                          size=wx.Size(800, 600), style=wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_status_bar(sizer)
        self._init_view_info(sizer)

        self.SetSizer(sizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.btnDeleteDishes.Bind(wx.EVT_BUTTON, self.on_btn_delete_dishes)
        self.btnSeat.Bind(wx.EVT_BUTTON, self.on_btn_seat)
        self.btnPlaceOrder.Bind(wx.EVT_BUTTON, self.on_btn_place_order)
        self.btnExit.Bind(wx.EVT_BUTTON, self.on_btn_exit)
        self.btnAddDishes.Bind(wx.EVT_BUTTON, self.on_btn_add_num)
        self.btnDelDishes.Bind(wx.EVT_BUTTON, self.on_btn_del_num)
        self.btnModDishes.Bind(wx.EVT_BUTTON, self.on_btn_mod_num)
        self.btnSpecialDemand.Bind(wx.EVT_BUTTON, self.on_btn_demand)

        self.Bind(wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.on_item_activated, self.dataViewCtrl)
        self.Bind(wx.dataview.EVT_DATAVIEW_SELECTION_CHANGED, self.on_item_changed, self.dataViewCtrl)

        # Create an instance of our model...
        table_num = CtrlTableInfo.get_instance().get_selected_item_id()
        order_num = CtrlTableInfo.get_instance().get_order_num(table_num)
        self.model = ModelOrderedDishes(CtrlOrderInfo.get_instance().get_order_dishes_items(order_num))
        # Tell the DVC to use the model
        self.dataViewCtrl.AssociateModel(self.model)

        # initialize
        self.dishes_page = 0
        self.dishesBtnMap = dict()
        self.type_page = 0
        self.typeBtnMap = dict()

    def __del__(self):
        pass

    def initialize(self):
        # Add event listener
        EvtManager.add_listener(self, EnumEvent.EVT_ORDER_DISHES_ITEMS_REFRESH, self.on_dishes_items_refresh)

        x, y = CtrlHomePage.get_instance().get_screen_size()
        self.SetSize(wx.Size(x, y))

        self.GetParent().SetTitle(u"点菜")

    def un_initialize(self):
        # Remove event listener
        EvtManager.remove_listener(self, EnumEvent.EVT_ORDER_DISHES_ITEMS_REFRESH, self.on_dishes_items_refresh)
        pass

    # Virtual event handlers, override them in your derived class
    def on_size(self, event):
        event.Skip()
        x, y = self.GetSize()

        self.btnDeleteDishes.SetMaxSize(wx.Size(60, 60))
        self.btnSeat.SetMaxSize(wx.Size(60, 60))
        self.btnPlaceOrder.SetMaxSize(wx.Size(60, 60))
        self.btnExit.SetMaxSize(wx.Size(60, 60))
        self.statusBarPanel.SetMaxSize(wx.Size(x, 60))
        self.dataViewPanel.SetMinSize(wx.Size(x-400, y-60))
        self.dataViewCtrl.SetMinSize(wx.Size(x-400, y-60))
        self.dishesPanel.SetMinSize(wx.Size(380, y-240))
        self.dishesListPanel.SetMinSize(wx.Size(325, y-240))
        self.dishesTypePanel.SetMinSize(wx.Size(55, y-240))

        self._show_dishes_buttons(320, y-60-200)
        self._show_type_buttons(y-60-200)
        self._show_dishes_data()
        self._show_table_data()

    def on_btn_delete_dishes(self, event):
        if CtrlOrderInfo.get_instance().get_select_dishes_id() is None:
            dlg = wx.MessageDialog(self, u"没有可删除菜品", caption=u"删菜")
            dlg.ShowModal()
        else:
            pop_delete_dishes = PopDeleteDishes(self)
            pop_delete_dishes.ShowModal()

    def on_btn_seat(self, event):
        pop_seat_setting = PopSeatSetting(self)
        pop_seat_setting.ShowModal()

    def on_btn_place_order(self, event):
        pop_place_order = PopPlaceOrder(self)
        pop_place_order.ShowModal()

    def on_btn_exit(self, event):
        AppManager.get_instance().switch_to_application('FrontPage')

    def on_btn_add_num(self, event):
        CtrlOrderInfo.get_instance().plus_dishes()

    def on_btn_del_num(self, event):
        CtrlOrderInfo.get_instance().minus_dishes()

    def on_btn_mod_num(self, event):
        pop_mod_num = PopModDishesNum(self)
        pop_mod_num.ShowModal()
        CtrlOrderInfo.get_instance().mod_dishes(8)

    def on_btn_demand(self, event):
        pop_order_dishes = PopOrderDishes(self, "mod")
        pop_order_dishes.ShowModal()

    def on_btn_dishes(self, event):
        event.Skip()
        pop_order_dishes = PopOrderDishes(self, "add")
        pop_order_dishes.ShowModal()
        CtrlOrderInfo.get_instance().order_dishes(event.GetId())

    def on_btn_dishes_up(self, event):
        if self.dishes_page > 0:
            self.dishes_page -= 1
            x, y = self.GetSize()
            self._show_dishes_buttons(320, y-60-200)

    def on_btn_dishes_down(self, event):
        self.dishes_page += 1
        x, y = self.GetSize()
        self._show_dishes_buttons(320, y-60-200)

    def on_btn_type(self, event):
        CtrlDishesInfo.get_instance().set_cur_dishes_type(event.GetId())
        self.dishes_page = 0
        x, y = self.GetSize()
        self._show_dishes_buttons(320, y-60-200)

    def on_btn_type_up(self, event):
        if self.type_page > 0:
            self.type_page -= 1
            x, y = self.GetSize()
            self._show_type_buttons(y-60-200)

    def on_btn_type_down(self, event):
        self.type_page += 1
        x, y = self.GetSize()
        self._show_type_buttons(y-60-200)

    def _show_dishes_buttons(self, x, y):
        column = x / 80
        row = (y - 30) / 80
        start_item_index = column * row * self.dishes_page
        dishes_items = CtrlDishesInfo.get_instance().get_dishes_items()
        if start_item_index >= len(dishes_items):
            self.dishes_page -= 1
            return

        for (k, v) in self.dishesBtnMap.items():
            self.Unbind(wx.EVT_BUTTON, v, handler=self.on_btn_dishes)
            v.Destroy()
        self.dishesBtnMap.clear()

        try:
            index_ = 0
            for i in range(0, row):
                for j in range(0, column):
                    if index_ >= len(dishes_items):
                        break
                    item = dishes_items[index_ + start_item_index]
                    index_ += 1
                    win_id = int(item.dishes_code)
                    self.dishesBtnMap[win_id] = wx.Button(self.dishesListPanel, win_id, item.dishes_name,
                                                          (j*80, i*80), wx.Size(80, 80))
                    self.dishesBtnMap[win_id].SetBackgroundColour(wx.CYAN)

                    self.Bind(wx.EVT_BUTTON, self.on_btn_dishes, self.dishesBtnMap[win_id])
        except:
            pass

        if self.btnDishesUp is not None:
            self.btnDishesUp.Destroy()
        self.btnDishesUp = wx.Button(self.dishesListPanel, -1, u"上一页", (0, y-30), wx.Size(150, 30))

        if self.btnDishesDown is not None:
            self.btnDishesDown.Destroy()
        self.btnDishesDown = wx.Button(self.dishesListPanel, -1, u"下一页", (x-150, y-30), wx.Size(150, 30))

        self.btnDishesUp.Bind(wx.EVT_BUTTON, self.on_btn_dishes_up)
        self.btnDishesDown.Bind(wx.EVT_BUTTON, self.on_btn_dishes_down)

    def _show_type_buttons(self, y):
        row = (y - 60) / 50
        type_items = CtrlDishesInfo.get_instance().get_type_items()

        start_item_index = row * self.type_page
        if start_item_index >= len(type_items):
            self.type_page -= 1
            return

        for (k, v) in self.typeBtnMap.items():
            self.Unbind(wx.EVT_BUTTON, v, handler=self.on_btn_type)
            v.Destroy()
        self.typeBtnMap.clear()

        try:
            for i in range(0, row):
                if i >= len(type_items):
                    break

                item = type_items[i + start_item_index]
                win_id = item.type_id
                self.typeBtnMap[win_id] = wx.Button(self.dishesTypePanel, win_id, item.type_name,
                                                    (0, i*50+25), wx.Size(70, 50))
                self.typeBtnMap[win_id].SetBackgroundColour(wx.YELLOW)

                self.Bind(wx.EVT_BUTTON, self.on_btn_type, self.typeBtnMap[win_id])
        except:
            pass

        if self.btnTypeUp is not None:
            self.btnTypeUp.Destroy()
        self.btnTypeUp = wx.Button(self.dishesTypePanel, -1, u"^", (0, 0), wx.Size(70, 30))

        if self.btnTypeDown is not None:
            self.btnTypeDown.Destroy()
        self.btnTypeDown = wx.Button(self.dishesTypePanel, -1, u"v", (0, y-30), wx.Size(70, 30))

        self.btnTypeUp.Bind(wx.EVT_BUTTON, self.on_btn_type_up)
        self.btnTypeDown.Bind(wx.EVT_BUTTON, self.on_btn_type_down)

    def _show_dishes_data(self):
        self.txtDishesCode.Enable(False)
        dishes_code = CtrlOrderInfo.get_instance().get_select_dishes_id()
        if dishes_code is not None:
            dishes_item = CtrlDishesInfo.get_instance().get_dishes_item(dishes_code)
            if dishes_item is not None:
                self.txtDishesCode.SetValue(dishes_item.dishes_name)

    def _show_table_data(self):
        table_num = CtrlTableInfo.get_instance().get_selected_item_id()
        if table_num is None:
            return

        # Show table info
        table_item = CtrlTableInfo.get_instance().get_table_item(table_num)
        self.txtTableCode.SetLabel(table_item.table_name)
        self.txtCustomerNum.SetLabel(str(table_item.people_num))
        self.txtMemo.SetLabel(table_item.memo)

    def on_dishes_items_refresh(self, event):
        # Refresh data view list
        table_num = CtrlTableInfo.get_instance().get_selected_item_id()
        order_num = CtrlTableInfo.get_instance().get_order_num(table_num)
        result = CtrlOrderInfo.get_instance().get_order_dishes_items(order_num)
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.dataViewCtrl.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)

        self.model.Cleared()
        self._show_dishes_data()

    def on_item_activated(self, event):
        print self.model.GetValue(event.GetItem(), 0)

    def on_item_changed(self, event):
        try:
            dishes_id = self.model.GetValue(event.GetItem(), 0)
            dishes_code = CtrlDishesInfo.get_instance().get_code_by_di(dishes_id)
            CtrlOrderInfo.get_instance().set_select_dishes_id(dishes_code)
        except:
            CtrlOrderInfo.get_instance().set_select_dishes_id(None)

        self._show_dishes_data()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = WgtOrderDishes(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()
