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
from framework.img_button import ImgButton

import wx
import wx.xrc
import wx.dataview
import sys

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

        cbx_spec = list()
        self.cbxSpec = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(110, -1), cbx_spec, 0)
        self.cbxSpec.SetSelection(0)
        demand_sizer.Add(self.cbxSpec, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        s_txt_style = wx.StaticText(self, wx.ID_ANY, u"做法：", wx.DefaultPosition, wx.Size(80, -1), wx.ALIGN_RIGHT)
        s_txt_style.Wrap(-1)
        demand_sizer.Add(s_txt_style, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        cbx_style = list()
        self.cbxStyle = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(110, -1), cbx_style, 0)
        self.cbxStyle.SetSelection(0)
        demand_sizer.Add(self.cbxStyle, 0, wx.ALIGN_CENTER | wx.ALL, 5)

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

    def __init__(self, parent, opt_type, dishes_code):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"点菜操作", pos=wx.DefaultPosition,
                           size=wx.Size(500, 400), style=wx.CAPTION)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_ui(sizer)
        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.cbxSpec.Bind(wx.EVT_COMBOBOX, self.on_cbx_spec)
        self.cbxStyle.Bind(wx.EVT_COMBOBOX, self.on_cbx_style)

        self.btnConfirm.Bind(wx.EVT_BUTTON, self.on_btn_confirm)
        self.btnCancel.Bind(wx.EVT_BUTTON, self.on_btn_cancel)

        # Initialize
        self.type = opt_type
        self.dishes_code = dishes_code
        self._init_view()

    def __del__(self):
        pass

    def _init_view(self):
        self.txtDishesName.Enable(False)
        self.txtDishesCount.Enable(False)
        self.txtNormalPrice.Enable(False)
        self.txtAddPrice.Enable(False)
        if self.type == "add":
            self._init_add_view()
        else:
            self._init_mod_view()

    def _init_add_view(self):
        dishes_item = CtrlDishesInfo.get_instance().get_dishes_item(str(self.dishes_code))
        if dishes_item is not None:
            self.txtDishesName.SetValue(dishes_item.dishes_name)
            self.txtDishesCount.SetValue('1')

            di_spec = dishes_item.dishes_spec
            for spec in di_spec:
                self.cbxSpec.Append(spec["vch_name"], spec)
            self.cbxSpec.SetSelection(0)

            sel_spec = self.cbxSpec.GetClientData(self.cbxSpec.GetSelection())
            self.txtNormalPrice.SetValue(str(sel_spec["num_price"]))

            di_style = dishes_item.dishes_style
            if len(di_style) > 0:
                for style in di_style:
                    self.cbxStyle.Append(style["vch_name"], style)
                self.cbxStyle.SetSelection(0)

                sel_style = self.cbxStyle.GetClientData(self.cbxStyle.GetSelection())
                self.txtAddPrice.SetValue(str(sel_style["num_priceadd"]))
            else:
                self.txtAddPrice.SetValue("")

    def _init_mod_view(self):
        dishes_item = CtrlDishesInfo.get_instance().get_dishes_item(str(self.dishes_code))
        if dishes_item is not None:
            self.txtDishesName.SetValue(dishes_item.dishes_name)

            di_spec = dishes_item.dishes_spec
            for spec in di_spec:
                self.cbxSpec.Append(spec["vch_name"], spec)

            di_style = dishes_item.dishes_style
            for style in di_style:
                self.cbxStyle.Append(style["vch_name"], style)

            order_num = CtrlOrderInfo.get_instance().get_cur_order_id()
            if order_num is not None:
                order_dishes_item = CtrlOrderInfo.get_instance().get_order_dishes_item(order_num)
                if order_dishes_item is not None:
                    self.txtDishesCount.SetValue(str(order_dishes_item.dishes_count))

                    self.cbxSpec.SetSelection(di_spec.index(order_dishes_item.dishes_spec))
                    sel_spec = self.cbxSpec.GetClientData(self.cbxSpec.GetSelection())
                    self.txtNormalPrice.SetValue(str(sel_spec["num_price"]))

                    self.cbxStyle.SetSelection(di_style.index(order_dishes_item.dishes_style))
                    sel_style = self.cbxStyle.GetClientData(self.cbxStyle.GetSelection())
                    self.txtAddPrice.SetValue(str(sel_style["num_priceadd"]))

    # Virtual event handlers, override them in your derived class
    def on_cbx_spec(self, event):
        sel_spec = self.cbxSpec.GetClientData(self.cbxSpec.GetSelection())
        self.txtNormalPrice.SetValue(str(sel_spec["num_price"]))

    def on_cbx_style(self, event):
        sel_style = self.cbxStyle.GetClientData(self.cbxStyle.GetSelection())
        self.txtAddPrice.SetValue(str(sel_style["num_priceadd"]))

    def on_btn_confirm(self, event):
        style_sel = self.cbxStyle.GetSelection()
        style_data = None
        if style_sel != -1:
            style_data = self.cbxStyle.GetClientData(style_sel)

        CtrlOrderInfo.get_instance().order_dishes(int(self.dishes_code),
                                                  self.cbxSpec.GetClientData(self.cbxSpec.GetSelection()),
                                                  style_data,
                                                  self.txtSpecial.GetValue())
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
        ordered_dishes_item = CtrlOrderInfo.get_instance().get_select_dishes_item()
        if ordered_dishes_item is not None:
            self.txtDishesName.SetValue(ordered_dishes_item.dishes_name)
            self.txtDishesCount.SetValue(str(ordered_dishes_item.dishes_count))

    # Virtual event handlers, override them in your derived class
    def on_btn_confirm(self, event):
        CtrlOrderInfo.get_instance().mod_dishes(int(self.txtDishesCount.GetValue()))
        self.Close()

    def on_btn_cancel(self, event):
        self.Close()

###########################################################################
## Class WgtOrderDishes
###########################################################################


class WgtOrderDishes (wx.Panel):
    def _init_status_bar(self, parent):
        self.statusBarPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition,
                                       wx.Size(-1, 82), wx.TAB_TRAVERSAL)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add delete dishes button
        self.btnDeleteDishes = ImgButton(self.statusBarPanel, u"delete_dishes.png", u"s_delete_dishes.png")
        # Add seat button
        self.btnSeat = ImgButton(self.statusBarPanel, u"seat.png", u"s_seat.png")
        # Add place order button
        self.btnPlaceOrder = ImgButton(self.statusBarPanel, u"place_order.png", u"s_place_order.png")
        # Add exit button
        self.btnExit = ImgButton(self.statusBarPanel, u"front_exit.png", u"s_front_exit.png")

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

        sizer = wx.BoxSizer(wx.VERTICAL)
        # Add data view list control
        self.dataViewCtrl = wx.dataview.DataViewCtrl(self.dataViewPanel, wx.ID_ANY, wx.DefaultPosition,
                                                     wx.Size(400, 520), 0)
        self.dataViewCtrl.AppendTextColumn(u"行号", 0)
        self.dataViewCtrl.AppendTextColumn(u"菜品名称", 1)
        self.dataViewCtrl.AppendTextColumn(u"规格", 2)
        self.dataViewCtrl.AppendTextColumn(u"单位", 3)
        self.dataViewCtrl.AppendTextColumn(u"数量", 4)
        #self.dataViewCtrl.AppendTextColumn(u"退菜量", 5)
        self.dataViewCtrl.AppendTextColumn(u"单价", 6)
        self.dataViewCtrl.AppendTextColumn(u"实际金额", 7)
        self.dataViewCtrl.AppendTextColumn(u"落单状态", 11)
        self.dataViewCtrl.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        sizer.Add(self.dataViewCtrl, 0, 0, 5)

        # Layout
        self.dataViewPanel.SetSizer(sizer)
        self.dataViewPanel.Layout()
        parent.Add(self.dataViewPanel, 1, wx.EXPAND, 5)

    def _init_order_info(self, parent):
        self.orderPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(400, 520), wx.TAB_TRAVERSAL)
        self.orderPanel.SetBackgroundColour(wx.Colour(0xea, 0xd4, 0x99))

        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_dishes_search_ctrl(self.orderPanel, sizer)
        self._init_dishes_info_ctrl(self.orderPanel, sizer)

        self.orderPanel.SetSizer(sizer)
        self.orderPanel.Layout()
        parent.Add(self.orderPanel, 1, wx.EXPAND | wx.LEFT, 5)

    def _init_dishes_search_ctrl(self, container, parent):
        self.ctrlPanel = wx.Panel(container, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.ctrlPanel.SetBackgroundColour(wx.Colour(0xea, 0xd4, 0x99))
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
        self.dishesPanel = wx.Panel(container, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add dishes list panel
        self.dishesListPanel = wx.Panel(self.dishesPanel, wx.ID_ANY, wx.DefaultPosition,
                                        wx.DefaultSize, wx.STATIC_BORDER | wx.TAB_TRAVERSAL)
        self.dishesListPanel.SetBackgroundColour(wx.Colour(0xea, 0xd4, 0x99))
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
        self.SetBackgroundColour(wx.Colour(0x51, 0x1c, 0x0a))

        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_status_bar(sizer)
        self._init_view_info(sizer)

        self.SetSizer(sizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_PAINT, self.on_paint)
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

        # initialize
        self.dishes_page = 0
        self.dishesBtnMap = dict()
        self.type_page = 0
        self.typeBtnMap = dict()

        # define variable
        self.model = None

    def __del__(self):
        pass

    def initialize(self):
        # Create an instance of our model...
        table_num = CtrlTableInfo.get_instance().get_selected_item_id()
        order_num = CtrlTableInfo.get_instance().get_order_num(table_num)
        self.model = ModelOrderedDishes(CtrlOrderInfo.get_instance().get_order_dishes_items(order_num))
        # Tell the DVC to use the model
        self.dataViewCtrl.AssociateModel(self.model)

        self._show_table_data()

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

        self._refresh_btns()

    def _refresh_btns(self):
        self.btnDeleteDishes.Refresh()
        self.btnSeat.Refresh()
        self.btnPlaceOrder.Refresh()
        self.btnExit.Refresh()

    def on_size(self, event):
        event.Skip()
        x, y = self.GetClientSize()

        self.btnDeleteDishes.SetSize(wx.Size(63, 70))
        self.btnDeleteDishes.SetPosition(wx.Point(0, 6))

        self.btnSeat.SetSize(wx.Size(63, 70))
        self.btnSeat.SetPosition(wx.Point(65, 6))

        self.btnPlaceOrder.SetSize(wx.Size(63, 70))
        self.btnPlaceOrder.SetPosition(wx.Point(130, 6))

        self.btnExit.SetSize(wx.Size(63, 70))
        self.btnExit.SetPosition(wx.Point(195, 6))

        self.statusBarPanel.SetSize(wx.Size(x, 82))
        self.dataViewPanel.SetMinSize(wx.Size(x-400, y-82))
        self.dataViewCtrl.SetMinSize(wx.Size(x-400, y-82))
        self.ctrlPanel.SetSize(wx.Size(380, 180))
        self.dishesPanel.SetMinSize(wx.Size(380, y-262))
        self.dishesListPanel.SetMinSize(wx.Size(325, y-262))
        self.dishesTypePanel.SetMinSize(wx.Size(55, y-262))

        self.Refresh()

        self._show_dishes_buttons(320, y-262)
        self._show_type_buttons(y-262)
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

    def on_btn_demand(self, event):
        pop_order_dishes = PopOrderDishes(self, "mod", CtrlOrderInfo.get_instance().get_select_dishes_id())
        pop_order_dishes.ShowModal()

    def on_btn_dishes(self, event):
        event.Skip()
        pop_order_dishes = PopOrderDishes(self, "add", event.GetId())
        pop_order_dishes.ShowModal()

    def on_btn_dishes_up(self, event):
        if self.dishes_page > 0:
            self.dishes_page -= 1
            x, y = self.GetSize()
            self._show_dishes_buttons(320, y-262)

    def on_btn_dishes_down(self, event):
        self.dishes_page += 1
        x, y = self.GetSize()
        self._show_dishes_buttons(320, y-262)

    def on_btn_type(self, event):
        CtrlDishesInfo.get_instance().set_cur_dishes_type(event.GetId())
        self.dishes_page = 0
        x, y = self.GetSize()
        self._show_dishes_buttons(320, y-262)

    def on_btn_type_up(self, event):
        if self.type_page > 0:
            self.type_page -= 1
            x, y = self.GetSize()
            self._show_type_buttons(y-262)

    def on_btn_type_down(self, event):
        self.type_page += 1
        x, y = self.GetSize()
        self._show_type_buttons(y-262)

    def _show_dishes_buttons(self, x, y):
        column = x / 80
        row = (y - 32) / 80
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
                    self.dishesBtnMap[win_id].SetBackgroundColour(wx.Colour(234, 210, 140))

                    self.Bind(wx.EVT_BUTTON, self.on_btn_dishes, self.dishesBtnMap[win_id])
        except Exception, ex:
            print Exception, ":", ex

        if self.btnDishesUp is not None:
            self.btnDishesUp.Destroy()
        self.btnDishesUp = ImgButton(self.dishesListPanel, u"prev_page.png", u"s_prev_page.png",
                                     "", wx.Colour(0xea, 0xd4, 0x99))
        self.btnDishesUp.SetPosition(wx.Point(0, y-32))
        self.btnDishesUp.SetSize(wx.Size(152, 32))

        if self.btnDishesDown is not None:
            self.btnDishesDown.Destroy()
        self.btnDishesDown = ImgButton(self.dishesListPanel, u"next_page.png", u"s_next_page.png",
                                       "", wx.Colour(0xea, 0xd4, 0x99))
        self.btnDishesDown.SetPosition(wx.Point(x-152, y-32))
        self.btnDishesDown.SetSize(wx.Size(152, 32))

        self.btnDishesUp.Bind(wx.EVT_BUTTON, self.on_btn_dishes_up)
        self.btnDishesDown.Bind(wx.EVT_BUTTON, self.on_btn_dishes_down)

    def _show_type_buttons(self, y):
        row = (y - 64) / 50
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
            self.typeBtnMap[10000] = wx.Button(self.dishesTypePanel, 10000, u"全部类型",
                                              (0, 25), wx.Size(70, 50))
            self.typeBtnMap[10000].SetBackgroundColour(wx.Colour(241, 197, 102))

            self.Bind(wx.EVT_BUTTON, self.on_btn_type, self.typeBtnMap[10000])
            for i in range(0, row):
                if i >= len(type_items):
                    break

                item = type_items[i + start_item_index]
                win_id = item.type_id
                self.typeBtnMap[win_id] = wx.Button(self.dishesTypePanel, win_id, item.type_name,
                                                    (0, (i+1)*50+25), wx.Size(70, 50))
                self.typeBtnMap[win_id].SetBackgroundColour(wx.Colour(241, 197, 102))

                self.Bind(wx.EVT_BUTTON, self.on_btn_type, self.typeBtnMap[win_id])
        except Exception, ex:
            print Exception, ":", ex

        if self.btnTypeUp is not None:
            self.btnTypeUp.Destroy()
        self.btnTypeUp = ImgButton(self.dishesTypePanel, u"up.png", u"s_up.png", "", wx.Colour(0xea, 0xd4, 0x99))
        self.btnTypeUp.SetPosition(wx.Point(0, 0))
        self.btnTypeUp.SetSize(wx.Size(72, 32))

        if self.btnTypeDown is not None:
            self.btnTypeDown.Destroy()
        self.btnTypeDown = ImgButton(self.dishesTypePanel, u"down.png", u"s_down.png", "", wx.Colour(0xea, 0xd4, 0x99))
        self.btnTypeDown.SetPosition(wx.Point(0, y-32))
        self.btnTypeDown.SetSize(wx.Size(72, 32))

        self.btnTypeUp.Bind(wx.EVT_BUTTON, self.on_btn_type_up)
        self.btnTypeDown.Bind(wx.EVT_BUTTON, self.on_btn_type_down)

    def _show_dishes_data(self):
        self.txtDishesCode.Enable(False)
        dishes_code = CtrlOrderInfo.get_instance().get_select_dishes_code()
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
            dishes_code = self.model.GetValue(event.GetItem(), 10)
            dishes_spec_id = self.model.GetValue(event.GetItem(), 12)
            dishes_style_id = self.model.GetValue(event.GetItem(), 13)
            CtrlOrderInfo.get_instance().set_select_dishes_id(dishes_code, dishes_spec_id, dishes_style_id)
            CtrlOrderInfo.get_instance().set_select_dishes_code(dishes_code)
        except Exception, ex:
            print Exception, ":", ex
            CtrlOrderInfo.get_instance().set_select_dishes_id(None, None, None)

        self._show_dishes_data()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = WgtOrderDishes(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()
