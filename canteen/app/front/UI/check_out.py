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
## Class PopWholeOrderDiscount
###########################################################################


class PopWholeOrderDiscount (wx.Dialog):
    def _init_ui(self, parent):
        # Add discount info
        discount_sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)
        discount_sizer.SetMinSize(wx.Size(-1, 120))
        # Add source discount sizer
        src_discount_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.s_txt_src_discount = wx.StaticText(self, wx.ID_ANY, u"全单折扣：", wx.DefaultPosition,
                                                wx.Size(100, -1), wx.ALIGN_RIGHT)
        self.s_txt_src_discount.Wrap(-1)
        src_discount_sizer.Add(self.s_txt_src_discount, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtSrcDiscount = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        src_discount_sizer.Add(self.txtSrcDiscount, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        discount_sizer.Add(src_discount_sizer, 1, wx.EXPAND, 5)

        # Add special discount sizer
        '''special_discount_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.s_txt_spec_discount = wx.StaticText(self, wx.ID_ANY, u"特批折扣：", wx.DefaultPosition,
                                                 wx.Size(100, -1), wx.ALIGN_RIGHT)
        self.s_txt_spec_discount.Wrap(-1)
        special_discount_sizer.Add(self.s_txt_spec_discount, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtSpecDiscount = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        special_discount_sizer.Add(self.txtSpecDiscount, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        discount_sizer.Add(special_discount_sizer, 1, wx.EXPAND, 5)'''

        parent.Add(discount_sizer, 1, wx.EXPAND, 5)

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
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"全单折扣", pos=wx.DefaultPosition,
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
        order_id = CtrlOrderInfo.get_instance().get_cur_order_id()
        if order_id is not None:
            order_item = CtrlOrderInfo.get_instance().get_order_item(order_id)
            if order_item is not None:
                order_item.all_discount = float(self.txtSrcDiscount.GetValue())
                CtrlOrderInfo.get_instance().update_checkout_info()

        self.Close()

    def on_btn_cancel(self, event):
        self.Close()

###########################################################################
## Class PopDishesDiscount
###########################################################################


class PopDishesDiscount (wx.Dialog):
    def _init_ui(self, parent):
        # Add discount info
        discount_sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)
        discount_sizer.SetMinSize(wx.Size(-1, 120))
        # Add source discount sizer
        src_discount_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.s_txt_src_discount = wx.StaticText(self, wx.ID_ANY, u"菜品折扣：", wx.DefaultPosition,
                                                wx.Size(100, -1), wx.ALIGN_RIGHT)
        self.s_txt_src_discount.Wrap(-1)
        src_discount_sizer.Add(self.s_txt_src_discount, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtSrcDiscount = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        src_discount_sizer.Add(self.txtSrcDiscount, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        discount_sizer.Add(src_discount_sizer, 1, wx.EXPAND, 5)

        # Add special discount sizer
        '''special_discount_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.s_txt_spec_discount = wx.StaticText(self, wx.ID_ANY, u"特批折扣：", wx.DefaultPosition,
                                                 wx.Size(100, -1), wx.ALIGN_RIGHT)
        self.s_txt_spec_discount.Wrap(-1)
        special_discount_sizer.Add(self.s_txt_spec_discount, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtSpecDiscount = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        special_discount_sizer.Add(self.txtSpecDiscount, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        discount_sizer.Add(special_discount_sizer, 1, wx.EXPAND, 5)'''

        parent.Add(discount_sizer, 1, wx.EXPAND, 5)

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
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"单品折扣", pos=wx.DefaultPosition,
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
        self.txtSrcDiscount.Enable(False)
        dishes_code = CtrlOrderInfo.get_instance().get_select_dishes_code()
        if dishes_code is not None:
            dishes_item = CtrlDishesInfo.get_instance().get_dishes_item(dishes_code)
            if dishes_item is not None:
                self.txtSrcDiscount.SetValue(str(dishes_item.dishes_discount))

    # Virtual event handlers, override them in your derived class
    def on_btn_confirm(self, event):
        self.Close()

    def on_btn_cancel(self, event):
        self.Close()

###########################################################################
## Class PopCheckoutDiscount
###########################################################################


class PopCheckoutDiscount (wx.Dialog):
    def _init_ui(self, parent):
        # Add consume info
        consume_sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)
        consume_sizer.SetMinSize(wx.Size(-1, 120))
        # Add source discount sizer
        consume_sum_sizer = wx.BoxSizer(wx.HORIZONTAL)
        s_txt_consume = wx.StaticText(self, wx.ID_ANY, u"消费总价：", wx.DefaultPosition,
                                      wx.Size(100, -1), wx.ALIGN_RIGHT)
        s_txt_consume.Wrap(-1)
        consume_sum_sizer.Add(s_txt_consume, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtConsumeSum = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        consume_sum_sizer.Add(self.txtConsumeSum, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        consume_sizer.Add(consume_sum_sizer, 1, wx.EXPAND, 5)

        # Add free sizer
        free_sizer = wx.BoxSizer(wx.HORIZONTAL)

        s_txt_free = wx.StaticText(self, wx.ID_ANY, u"减免金额：", wx.DefaultPosition,
                                   wx.Size(100, -1), wx.ALIGN_RIGHT)
        s_txt_free.Wrap(-1)
        free_sizer.Add(s_txt_free, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtFree = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        free_sizer.Add(self.txtFree, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        consume_sizer.Add(free_sizer, 1, wx.EXPAND, 5)

        parent.Add(consume_sizer, 1, wx.EXPAND, 5)

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
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"收银免单", pos=wx.DefaultPosition,
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
        self.real_price = 0.0
        self._init_data_view()

    def __del__(self):
        pass

    def _init_data_view(self):
        self.txtConsumeSum.Enable(False)
        order_id = CtrlOrderInfo.get_instance().get_cur_order_id()
        if order_id is not None:
            order_item = CtrlOrderInfo.get_instance().get_order_item(order_id)
            if order_item is not None:
                self.real_price = order_item.place_money * order_item.all_discount
                self.txtConsumeSum.SetValue(str(self.real_price))

    # Virtual event handlers, override them in your derived class
    def on_btn_confirm(self, event):
        if float(self.txtFree.GetValue()) > self.real_price:
            dlg = wx.MessageDialog(self, u"减免金额不能大于总金额", caption=u"收银免单")
            dlg.ShowModal()
        else:
            order_id = CtrlOrderInfo.get_instance().get_cur_order_id()
            if order_id is not None:
                order_item = CtrlOrderInfo.get_instance().get_order_item(order_id)
                if order_item is not None:
                    order_item.free_price = float(self.txtFree.GetValue())
                    CtrlOrderInfo.get_instance().update_checkout_info()

            self.Close()

    def on_btn_cancel(self, event):
        self.Close()

###########################################################################
## Class PopPrevPrint
###########################################################################


class PopPrevPrint (wx.Dialog):
    def _init_order_info(self, parent):
        self.infoPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        self._init_order_left_info(self.infoPanel, sizer)
        self._init_order_right_info(self.infoPanel, sizer)

        # Layout
        self.infoPanel.SetSizer(sizer)
        self.infoPanel.Layout()
        sizer.Fit(self.infoPanel)
        parent.Add(self.infoPanel, 1, wx.EXPAND, 5)

    def _init_order_left_info(self, container, parent):
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Add order number and table name sizer
        order_table_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add order number
        s_txt_order_num = wx.StaticText(container, wx.ID_ANY, u"开台单号：", wx.DefaultPosition,
                                        wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_order_num.Wrap(-1)
        order_table_sizer.Add(s_txt_order_num, 0, wx.ALIGN_CENTER, 5)

        self.txtOrderNum = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(120, -1), 0)
        order_table_sizer.Add(self.txtOrderNum, 0, wx.ALIGN_CENTER, 5)
        # Add table number
        s_txt_table_num = wx.StaticText(container, wx.ID_ANY, u"餐桌：", wx.DefaultPosition,
                                        wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_table_num.Wrap(-1)
        order_table_sizer.Add(s_txt_table_num, 0, wx.ALIGN_CENTER, 5)

        self.txtTableNum = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, -1), 0)
        order_table_sizer.Add(self.txtTableNum, 0, wx.ALIGN_CENTER, 5)

        sizer.Add(order_table_sizer, 1, wx.EXPAND, 5)

        # Add open table time
        open_time_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add open table time
        s_txt_open_time = wx.StaticText(container, wx.ID_ANY, u"开台时间：", wx.DefaultPosition,
                                        wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_open_time.Wrap(-1)
        open_time_sizer.Add(s_txt_open_time, 0, wx.ALIGN_CENTER, 5)

        self.txtOpenTime = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(280, -1), 0)
        open_time_sizer.Add(self.txtOpenTime, 0, wx.ALIGN_CENTER, 5)

        sizer.Add(open_time_sizer, 1, wx.EXPAND, 5)
        # Add open table memo sizer
        open_table_memo_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add open table memo
        s_txt_memo = wx.StaticText(container, wx.ID_ANY, u"开台备注：", wx.DefaultPosition,
                                   wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_memo.Wrap(-1)
        open_table_memo_sizer.Add(s_txt_memo, 0, wx.ALIGN_CENTER, 5)

        self.txtMemo = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(280, -1), 0)
        open_table_memo_sizer.Add(self.txtMemo, 0, wx.ALIGN_CENTER, 5)

        sizer.Add(open_table_memo_sizer, 1, wx.EXPAND, 5)

        # Layout
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_order_right_info(self, container, parent):
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Add consumption and discount sizer
        consume_discount_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add consumption
        s_txt_consume = wx.StaticText(container, wx.ID_ANY, u"消费：", wx.DefaultPosition,
                                      wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_consume.Wrap(-1)
        consume_discount_sizer.Add(s_txt_consume, 0, wx.ALIGN_CENTER, 5)

        self.txtConsume = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(110, -1), 0)
        consume_discount_sizer.Add(self.txtConsume, 0, wx.ALIGN_CENTER, 5)
        # Add discount
        s_txt_discount = wx.StaticText(container, wx.ID_ANY, u"折扣：", wx.DefaultPosition,
                                       wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_discount.Wrap(-1)
        consume_discount_sizer.Add(s_txt_discount, 0, wx.ALIGN_CENTER, 5)

        self.txtDiscount = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(110, -1), 0)
        consume_discount_sizer.Add(self.txtDiscount, 0, wx.ALIGN_CENTER, 5)

        sizer.Add(consume_discount_sizer, 1, wx.EXPAND, 5)
        # Add fees receivable sizer
        receivable_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add receivable
        s_txt_receivable = wx.StaticText(container, wx.ID_ANY, u"应收：", wx.DefaultPosition,
                                         wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_receivable.Wrap(-1)
        receivable_sizer.Add(s_txt_receivable, 0, wx.ALIGN_CENTER, 5)

        self.txtReceivable = wx.TextCtrl(self.infoPanel, wx.ID_ANY, wx.EmptyString,
                                         wx.DefaultPosition, wx.Size(110, -1), 0)
        receivable_sizer.Add(self.txtReceivable, 0, wx.ALIGN_CENTER, 5)
        # Add free
        s_txt_free = wx.StaticText(container, wx.ID_ANY, u"免单：", wx.DefaultPosition,
                                   wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_free.Wrap(-1)
        receivable_sizer.Add(s_txt_free, 0, wx.ALIGN_CENTER, 5)

        self.txtFree = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.Size(110, -1), 0)
        receivable_sizer.Add(self.txtFree, 0, wx.ALIGN_CENTER, 5)
        sizer.Add(receivable_sizer, 1, wx.EXPAND, 5)
         # Add real price sizer
        real_price_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add real price
        s_txt_real_price = wx.StaticText(container, wx.ID_ANY, u"实收：", wx.DefaultPosition,
                                         wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_real_price.Wrap(-1)
        real_price_sizer.Add(s_txt_real_price, 0, wx.ALIGN_CENTER, 5)

        self.txtRealPrice = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(110, -1), 0)
        real_price_sizer.Add(self.txtRealPrice, 0, wx.ALIGN_CENTER, 5)
        # Add cash
        s_txt_cash = wx.StaticText(container, wx.ID_ANY, u"现金：", wx.DefaultPosition,
                                   wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_cash.Wrap(-1)
        real_price_sizer.Add(s_txt_cash, 0, wx.ALIGN_CENTER, 5)

        self.txtCash = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(110, -1), 0)
        real_price_sizer.Add(self.txtCash, 0, wx.ALIGN_CENTER, 5)
        sizer.Add(real_price_sizer, 1, wx.EXPAND, 5)

        # Layout
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_checkout_info(self, parent):
        self.checkoutPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Add charged and free sizer
        charged_free_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add coupon
        s_txt_coupon = wx.StaticText(self.checkoutPanel, wx.ID_ANY, u"优惠券：", wx.DefaultPosition,
                                      wx.Size(80, -1), wx.ALIGN_RIGHT)
        s_txt_coupon.Wrap(-1)
        charged_free_sizer.Add(s_txt_coupon, 0, wx.ALIGN_CENTER, 5)

        self.txtCoupon = wx.TextCtrl(self.checkoutPanel, wx.ID_ANY, wx.EmptyString,
                                     wx.DefaultPosition, wx.Size(120, -1), 0)
        charged_free_sizer.Add(self.txtCoupon, 0, wx.ALIGN_CENTER, 5)
        # Add membership
        s_txt_membership = wx.StaticText(self.checkoutPanel, wx.ID_ANY, u"会员卡：", wx.DefaultPosition,
                                         wx.Size(80, -1), wx.ALIGN_RIGHT)
        s_txt_membership.Wrap(-1)
        charged_free_sizer.Add(s_txt_membership, 0, wx.ALIGN_CENTER, 5)

        self.txtMembership = wx.TextCtrl(self.checkoutPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.Size(120, -1), 0)
        charged_free_sizer.Add(self.txtMembership, 0, wx.ALIGN_CENTER, 5)
        # Add pos
        s_txt_pos = wx.StaticText(self.checkoutPanel, wx.ID_ANY, u"Pos支付：", wx.DefaultPosition,
                                  wx.Size(80, -1), wx.ALIGN_RIGHT)
        s_txt_pos.Wrap(-1)
        charged_free_sizer.Add(s_txt_pos, 0, wx.ALIGN_CENTER, 5)

        self.txtPos = wx.TextCtrl(self.checkoutPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                  wx.Size(120, -1), 0)
        charged_free_sizer.Add(self.txtPos, 0, wx.ALIGN_CENTER, 5)

        # Layout charged and free sizer
        sizer.Add(charged_free_sizer, 1, wx.EXPAND, 5)

        # Add balance sizer
        balance_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add group
        s_txt_group = wx.StaticText(self.checkoutPanel, wx.ID_ANY, u"团购：", wx.DefaultPosition,
                                    wx.Size(80, -1), wx.ALIGN_RIGHT)
        s_txt_group.Wrap(-1)
        balance_sizer.Add(s_txt_group, 0, wx.ALIGN_CENTER, 5)

        self.txtGroup = wx.TextCtrl(self.checkoutPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.Size(120, -1), 0)
        balance_sizer.Add(self.txtGroup, 0, wx.ALIGN_CENTER, 5)

        # Add credit
        s_txt_credit = wx.StaticText(self.checkoutPanel, wx.ID_ANY, u"挂账：", wx.DefaultPosition,
                                     wx.Size(80, -1), wx.ALIGN_RIGHT)
        s_txt_credit.Wrap(-1)
        balance_sizer.Add(s_txt_credit, 0, wx.ALIGN_CENTER, 5)

        self.txtCredit = wx.TextCtrl(self.checkoutPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.Size(120, -1), 0)
        balance_sizer.Add(self.txtCredit, 0, wx.ALIGN_CENTER, 5)
        # Add boss sign
        s_txt_boss_sign = wx.StaticText(self.checkoutPanel, wx.ID_ANY, u"老板签单：", wx.DefaultPosition,
                                        wx.Size(80, -1), wx.ALIGN_RIGHT)
        s_txt_boss_sign.Wrap(-1)
        balance_sizer.Add(s_txt_boss_sign, 0, wx.ALIGN_CENTER, 5)

        self.txtBosssign = wx.TextCtrl(self.checkoutPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.Size(120, -1), 0)
        balance_sizer.Add(self.txtBosssign, 0, wx.ALIGN_CENTER, 5)
        # Layout balance sizer
        sizer.Add(balance_sizer, 1, wx.EXPAND, 5)

        # Layout
        self.checkoutPanel.SetSizer(sizer)
        self.checkoutPanel.Layout()
        sizer.Fit(self.checkoutPanel)
        parent.Add(self.checkoutPanel, 1, wx.EXPAND, 5)

    def _init_data_view(self, parent):
        self.dataViewPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition,
                                      wx.DefaultSize, wx.STATIC_BORDER | wx.TAB_TRAVERSAL)
        self.dataViewPanel.SetMinSize(wx.Size(-1, 200))

        sizer = wx.BoxSizer(wx.VERTICAL)
        # Add data view list
        self.dataViewCtrl = wx.dataview.DataViewCtrl(self.dataViewPanel, wx.ID_ANY, wx.DefaultPosition,
                                                     wx.DefaultSize, 0)
        self.dataViewCtrl.SetMinSize(wx.Size(-1, 200))

        self.dataViewCtrl.AppendTextColumn(u"行号", 0)
        self.dataViewCtrl.AppendTextColumn(u"菜品名称", 1)
        self.dataViewCtrl.AppendTextColumn(u"规格", 2)
        self.dataViewCtrl.AppendTextColumn(u"单位", 3)
        self.dataViewCtrl.AppendTextColumn(u"数量", 4)
        self.dataViewCtrl.AppendTextColumn(u"退菜量", 5)
        self.dataViewCtrl.AppendTextColumn(u"价格", 6)
        self.dataViewCtrl.AppendTextColumn(u"实际金额", 7)
        sizer.Add(self.dataViewCtrl, 0, wx.EXPAND, 5)

        # Layout
        self.dataViewPanel.SetSizer(sizer)
        self.dataViewPanel.Layout()
        sizer.Fit(self.dataViewPanel)
        parent.Add(self.dataViewPanel, 1, wx.EXPAND, 5)

    def _init_ctrl(self, parent):
        self.ctrlPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Add spacer
        sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        # Add previous print button
        self.btnPrevPrint = wx.Button(self.ctrlPanel, wx.ID_ANY, u"预打", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnPrevPrint, 0, wx.ALIGN_CENTER, 5)
        # Add exit button
        self.btnExit = wx.Button(self.ctrlPanel, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnExit, 0, wx.ALIGN_CENTER, 5)

        # Layout
        self.ctrlPanel.SetSizer(sizer)
        self.ctrlPanel.Layout()
        sizer.Fit(self.ctrlPanel)
        parent.Add(self.ctrlPanel, 1, wx.EXPAND | wx.ALL, 5)

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"预打账单", pos=wx.DefaultPosition,
                           size=wx.Size(700, 480), style=wx.CAPTION)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_order_info(sizer)
        self._init_checkout_info(sizer)
        self._init_data_view(sizer)
        self._init_ctrl(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.btnPrevPrint.Bind(wx.EVT_BUTTON, self.on_btn_prev_print)
        self.btnExit.Bind(wx.EVT_BUTTON, self.on_btn_exit)

        # Initialize
        self._init_view_data()
        self._init_consume_data()

    def __del__(self):
        pass

    def _init_view_data(self):
        self.txtTableNum.Enable(False)
        self.txtOpenTime.Enable(False)
        self.txtMemo.Enable(False)
        self.txtOrderNum.Enable(False)
        select_table_num = CtrlTableInfo.get_instance().get_selected_item_id()
        if select_table_num is not None:
            # Initialize table info
            table_item = CtrlTableInfo.get_instance().get_table_item(select_table_num)
            self.txtTableNum.SetValue(str(table_item.table_num))
            self.txtOpenTime.SetValue(table_item.open_time)
            self.txtMemo.SetValue(table_item.memo)
            # Initialize order info
            order_num = CtrlTableInfo.get_instance().get_order_num(select_table_num)
            if order_num is not None:
                self.txtOrderNum.SetValue(order_num)
                # Create an instance of our model...
                self.model = ModelOrderedDishes(CtrlOrderInfo.get_instance().get_order_dishes_items(order_num))
                # Tell the DVC to use the model
                self.dataViewCtrl.AssociateModel(self.model)

    def _init_consume_data(self):
        self.txtConsume.Enable(False)
        self.txtDiscount.Enable(False)
        self.txtFree.Enable(False)
        self.txtReceivable.Enable(False)
        self.txtRealPrice.Enable(False)
        self.txtCoupon.Enable(False)
        self.txtMembership.Enable(False)
        self.txtPos.Enable(False)
        self.txtGroup.Enable(False)
        self.txtCredit.Enable(False)
        self.txtBosssign.Enable(False)
        self.txtCash.Enable(False)
        order_id = CtrlOrderInfo.get_instance().get_cur_order_id()
        if order_id is not None:
            order_item = CtrlOrderInfo.get_instance().get_order_item(order_id)
            if order_item is not None:
                self.txtConsume.SetLabel(str(order_item.place_money))
                self.txtDiscount.SetLabel(str(order_item.all_discount))
                self.txtFree.SetLabel(str(order_item.free_price))
                self.txtReceivable.SetLabel(str(order_item.place_money * order_item.all_discount))
                self.txtRealPrice.SetLabel(str(order_item.place_money * order_item.all_discount -
                                               order_item.free_price))
                self.txtCoupon.SetValue(str(order_item.cashier_coupon))
                self.txtMembership.SetValue(str(order_item.cashier_membership))
                self.txtPos.SetValue(str(order_item.cashier_pos))
                self.txtGroup.SetValue(str(order_item.cashier_group))
                self.txtCredit.SetValue(str(order_item.cashier_credit))
                self.txtBosssign.SetValue(str(order_item.cashier_boss_sign))
                self.txtCash.SetValue(str(order_item.cashier_cash))

    # Virtual event handlers, override them in your derived class
    def on_btn_prev_print(self, event):
        event.Skip()
        self.Close()

    def on_btn_exit(self, event):
        event.Skip()
        self.Close()

###########################################################################
## Class PopCheckout
###########################################################################


class PopCheckout (wx.Dialog):
    def _init_ui(self, parent):
        # Add order info
        order_info_sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)
        order_info_sizer.SetMinSize(wx.Size(-1, 120))
        # Add order number sizer
        order_num_sizer = wx.BoxSizer(wx.HORIZONTAL)
        s_txt_order_num = wx.StaticText(self, wx.ID_ANY, u"单号：", wx.DefaultPosition,
                                        wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_order_num.Wrap(-1)
        order_num_sizer.Add(s_txt_order_num, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtOrderNum = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(120, -1), 0)
        order_num_sizer.Add(self.txtOrderNum, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        s_txt_money = wx.StaticText(self, wx.ID_ANY, u"金额：", wx.DefaultPosition,
                                    wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_money.Wrap(-1)
        order_num_sizer.Add(s_txt_money, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtMoney = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(120, -1), 0)
        order_num_sizer.Add(self.txtMoney, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        order_info_sizer.Add(order_num_sizer, 1, wx.EXPAND, 5)

        # Add money sizer
        money_sizer = wx.BoxSizer(wx.HORIZONTAL)
        s_txt_bill_num = wx.StaticText(self, wx.ID_ANY, u"发票金额：", wx.DefaultPosition,
                                       wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_bill_num.Wrap(-1)
        money_sizer.Add(s_txt_bill_num, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtBillNum = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(120, -1), 0)
        money_sizer.Add(self.txtBillNum, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        s_txt_need_bill = wx.StaticText(self, wx.ID_ANY, u"有发票：", wx.DefaultPosition,
                                        wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_need_bill.Wrap(-1)
        money_sizer.Add(s_txt_need_bill, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.cbxNeedBill = wx.CheckBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(120, -1), 0)
        money_sizer.Add(self.cbxNeedBill, 0, wx.ALIGN_CENTER | wx.ALL, 5)

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
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"埋单操作", pos=wx.DefaultPosition,
                           size=wx.Size(400, 200), style=wx.CAPTION)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_ui(sizer)
        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.btnConfirm.Bind(wx.EVT_BUTTON, self.on_btn_confirm)
        self.btnCancel.Bind(wx.EVT_BUTTON, self.on_btn_cancel)
        self.cbxNeedBill.Bind(wx.EVT_CHECKBOX, self.on_cbx_need_bill)

        # Initialize
        self.table_item = None
        self._init_data_view()
        self.cbxNeedBill.SetValue(False)
        self.txtBillNum.Enable(False)

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
                self.txtMoney.SetValue(str((order_item.place_money * order_item.all_discount) - order_item.free_price))

    # Virtual event handlers, override them in your derived class
    def on_btn_confirm(self, event):
        if self.table_item is not None:
            bill_num = 0.0
            if self.cbxNeedBill.GetValue():
                bill_num = float(self.txtBillNum.GetValue())
            CtrlOrderInfo.get_instance().check_out(self.table_item.table_id, self.table_item.order_id,
                                                   self.table_item.order_num, bill_num)
        self.Close()

    def on_btn_cancel(self, event):
        self.Close()

    def on_cbx_need_bill(self, event):
        if self.cbxNeedBill.GetValue():
            self.txtBillNum.Enable(True)
        else:
            self.txtBillNum.SetValue("")
            self.txtBillNum.Enable(False)

###########################################################################
## Class WgtCheckout
###########################################################################


class WgtCheckout (wx.Panel):
    def _init_status_bar(self, parent):
        self.statusBarPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 82), wx.TAB_TRAVERSAL)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add all dishes discount button
        self.btnAllDiscount = ImgButton(self.statusBarPanel, u"all_discount.png", u"s_all_discount.png")
        # Add dishes discount button
        self.btnDishesDiscount = ImgButton(self.statusBarPanel, u"dishes_discount.png", u"s_dishes_discount.png")
        # Add free dishes button
        self.btnFree = ImgButton(self.statusBarPanel, u"free.png", u"s_free.png")
        # Add previous print button
        self.btnPrevPrint = ImgButton(self.statusBarPanel, u"print.png", u"s_print.png")
        # Add checkout button
        self.btnCheckout = ImgButton(self.statusBarPanel, u"check_order.png", u"s_check_order.png")
        # Add exit button
        self.btnExit = ImgButton(self.statusBarPanel, u"front_exit.png", u"s_front_exit.png")

        # Layout
        self.statusBarPanel.SetSizer(sizer)
        self.statusBarPanel.Layout()
        parent.Add(self.statusBarPanel, 1, wx.EXPAND, 5)

    def _init_data_view_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        self._init_data_view_list(sizer)
        self._init_checkout_info(sizer)

        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_data_view_list(self, parent):
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.dishesViewPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition,
                                        wx.DefaultSize, wx.STATIC_BORDER | wx.TAB_TRAVERSAL)
        self.dishesViewPanel.SetBackgroundColour(wx.Colour(0xea, 0xd4, 0x99))
        # Add dishes list view sizer
        dishes_view_sizer = wx.BoxSizer(wx.VERTICAL)

        self.dataViewList = wx.dataview.DataViewCtrl(self.dishesViewPanel, wx.ID_ANY, wx.DefaultPosition,
                                                     wx.DefaultSize, 0)
        self.dataViewList.AppendTextColumn(u"行号", 0)
        self.dataViewList.AppendTextColumn(u"菜品名称", 1)
        self.dataViewList.AppendTextColumn(u"规格", 2)
        self.dataViewList.AppendTextColumn(u"数量", 4)
        self.dataViewList.AppendTextColumn(u"退菜量", 9)
        self.dataViewList.AppendTextColumn(u"价格", 6)
        self.dataViewList.AppendTextColumn(u"加价", 8)
        self.dataViewList.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        dishes_view_sizer.Add(self.dataViewList, 0, wx.EXPAND, 5)

        # Layout dishes list view
        self.dishesViewPanel.SetSizer(dishes_view_sizer)
        self.dishesViewPanel.Layout()
        dishes_view_sizer.Fit(self.dishesViewPanel)
        sizer.Add(self.dishesViewPanel, 1, wx.EXPAND, 5)

        # Add checkout type list view sizer
        self.checkoutViewPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(480, 210), wx.TAB_TRAVERSAL)
        self.checkoutViewPanel.SetBackgroundColour(wx.Colour(0xea, 0xd4, 0x99))
        checkout_view_sizer = wx.BoxSizer(wx.VERTICAL)

        self.dataViewCheckout = wx.dataview.DataViewCtrl(self.checkoutViewPanel, wx.ID_ANY, wx.DefaultPosition,
                                                         wx.Size(480, 210), 0)
        self.dataViewCheckout.AppendTextColumn(u"行号", 0)
        self.dataViewCheckout.AppendTextColumn(u"收银方式", 1)
        self.dataViewCheckout.AppendTextColumn(u"实收金额", 2)
        self.dataViewCheckout.AppendTextColumn(u"付款金额", 3)
        self.dataViewCheckout.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        checkout_view_sizer.Add(self.dataViewCheckout, 0, wx.EXPAND, 5)

        # Layout checkout type list view
        self.checkoutViewPanel.SetSizer(checkout_view_sizer)
        self.checkoutViewPanel.Layout()
        sizer.Add(self.checkoutViewPanel, 1, wx.EXPAND, 5)

        # Layout
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_checkout_info(self, parent):
        sizer = wx.BoxSizer(wx.VERTICAL)

        self._init_table_info(sizer)
        self._init_cashier_info(sizer)

        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_table_info(self, parent):
        self.tableInfoPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(300, 300),
                                       wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL)
        self.tableInfoPanel.SetBackgroundColour(wx.Colour(0xea, 0xd4, 0x99))

        sizer = wx.BoxSizer(wx.VERTICAL)
        # Add order number and table number sizer
        order_table_number_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add open table order number
        s_txt_order_num = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"开台单号：", wx.DefaultPosition,
                                        wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_order_num.Wrap(-1)
        order_table_number_sizer.Add(s_txt_order_num, 0, wx.ALIGN_CENTER, 5)

        self.txtOrderNum = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                         wx.Size(100, -1), wx.ALIGN_CENTRE)
        self.txtOrderNum.Wrap(-1)
        order_table_number_sizer.Add(self.txtOrderNum, 0, wx.ALIGN_CENTER, 5)
        # Add table number
        s_txt_table_num = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"餐桌：", wx.DefaultPosition,
                                        wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_table_num.Wrap(-1)
        order_table_number_sizer.Add(s_txt_table_num, 0, wx.ALIGN_CENTER, 5)

        self.txtTableNum = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                         wx.Size(80, -1), wx.ALIGN_CENTRE)
        self.txtTableNum.Wrap(-1)
        order_table_number_sizer.Add(self.txtTableNum, 0, wx.ALIGN_CENTER, 5)

        sizer.Add(order_table_number_sizer, 1, wx.EXPAND, 5)

        # Add operator and waiter sizer
        operator_waiter_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add operator
        s_txt_operator = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"开台人：", wx.DefaultPosition,
                                       wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_operator.Wrap(-1)
        operator_waiter_sizer.Add(s_txt_operator, 0, wx.ALIGN_CENTER, 5)

        self.txtOpenPerson = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                           wx.Size(100, -1), wx.ALIGN_CENTRE)
        self.txtOpenPerson.Wrap(-1)
        operator_waiter_sizer.Add(self.txtOpenPerson, 0, wx.ALIGN_CENTER, 5)
        # Add memo
        s_txt_waiter = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"服务员：", wx.DefaultPosition,
                                     wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_waiter.Wrap(-1)
        operator_waiter_sizer.Add(s_txt_waiter, 0, wx.ALIGN_CENTER, 5)

        self.txtOpenWaiter = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                           wx.Size(80, -1), wx.ALIGN_CENTRE)
        self.txtOpenWaiter.Wrap(-1)
        operator_waiter_sizer.Add(self.txtOpenWaiter, 0, wx.ALIGN_CENTER, 5)

        sizer.Add(operator_waiter_sizer, 1, wx.EXPAND, 5)

        # Add open table time sizer
        open_time_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add open table time
        s_txt_open_time = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"开台时间：", wx.DefaultPosition,
                                        wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_open_time.Wrap(-1)
        open_time_sizer.Add(s_txt_open_time, 0, wx.ALIGN_CENTER, 5)

        self.txtOpenTime = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                         wx.Size(280, -1), wx.ALIGN_CENTRE)
        self.txtOpenTime.Wrap(-1)
        open_time_sizer.Add(self.txtOpenTime, 0, wx.ALIGN_CENTER, 5)

        sizer.Add(open_time_sizer, 1, wx.EXPAND, 5)

        # Add open table memo sizer
        open_memo_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add open table time
        s_txt_open_memo = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"开台备注：", wx.DefaultPosition,
                                        wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_open_memo.Wrap(-1)
        open_memo_sizer.Add(s_txt_open_memo, 0, wx.ALIGN_CENTER, 5)

        self.txtOpenMemo = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                         wx.Size(280, -1), wx.ALIGN_CENTRE)
        self.txtOpenMemo.Wrap(-1)
        open_memo_sizer.Add(self.txtOpenMemo, 0, wx.ALIGN_CENTER, 5)

        sizer.Add(open_memo_sizer, 1, wx.EXPAND, 5)

        # Add horizontal line
        s_horizontal_line = wx.StaticLine(self.tableInfoPanel, wx.ID_ANY, wx.DefaultPosition,
                                          wx.DefaultSize, wx.LI_HORIZONTAL)
        sizer.Add(s_horizontal_line, 0, wx.EXPAND, 5)

        # Add consume and discount sizer
        consume_discount_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add consume
        s_txt_consume = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"消费：", wx.DefaultPosition,
                                      wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_consume.Wrap(-1)
        consume_discount_sizer.Add(s_txt_consume, 0, wx.ALIGN_CENTER, 5)

        self.txtConsume = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                        wx.Size(100, -1), wx.ALIGN_CENTRE)
        self.txtConsume.Wrap(-1)
        consume_discount_sizer.Add(self.txtConsume, 0, wx.ALIGN_CENTER, 5)
        # Add discount
        s_txt_discount = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"折扣：", wx.DefaultPosition,
                                       wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_discount.Wrap(-1)
        consume_discount_sizer.Add(s_txt_discount, 0, wx.ALIGN_CENTER, 5)

        self.txtDiscount = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                         wx.Size(80, -1), wx.ALIGN_CENTRE)
        self.txtDiscount.Wrap(-1)
        consume_discount_sizer.Add(self.txtDiscount, 0, wx.ALIGN_CENTER, 5)

        sizer.Add(consume_discount_sizer, 1, wx.EXPAND, 5)

        # Add handout and service charge
        handout_charge_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add handout
        s_txt_handout = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                      wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_handout.Wrap(-1)
        handout_charge_sizer.Add(s_txt_handout, 0, wx.ALIGN_CENTER, 5)

        self.txtHandout = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                        wx.Size(100, -1), wx.ALIGN_CENTRE)
        self.txtHandout.Wrap(-1)
        handout_charge_sizer.Add(self.txtHandout, 0, wx.ALIGN_CENTER, 5)
        # Add service charge
        s_txt_charge = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                     wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_charge.Wrap(-1)
        handout_charge_sizer.Add(s_txt_charge, 0, wx.ALIGN_CENTER, 5)

        self.txtCharge = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                       wx.Size(80, -1), wx.ALIGN_CENTRE)
        self.txtCharge.Wrap(-1)
        handout_charge_sizer.Add(self.txtCharge, 0, wx.ALIGN_CENTER, 5)

        sizer.Add(handout_charge_sizer, 1, wx.EXPAND, 5)

        # Add offset the different and rounding sizer
        offset_rounding_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add offset the different
        s_txt_offset = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                     wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_offset.Wrap(-1)
        offset_rounding_sizer.Add(s_txt_offset, 0, wx.ALIGN_CENTER, 5)

        self.txtOffset = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                       wx.Size(100, -1), wx.ALIGN_CENTRE)
        self.txtOffset.Wrap(-1)
        offset_rounding_sizer.Add(self.txtOffset, 0, wx.ALIGN_CENTER, 5)

        s_txt_rounding = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                       wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_rounding.Wrap(-1)
        offset_rounding_sizer.Add(s_txt_rounding, 0, wx.ALIGN_CENTER, 5)

        self.txtRounding = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                         wx.Size(80, -1), wx.ALIGN_CENTRE)
        self.txtRounding.Wrap(-1)
        offset_rounding_sizer.Add(self.txtRounding, 0, wx.ALIGN_CENTER, 5)

        sizer.Add(offset_rounding_sizer, 1, wx.EXPAND, 5)

        # Add horizontal line
        s_horizontal_line = wx.StaticLine(self.tableInfoPanel, wx.ID_ANY, wx.DefaultPosition,
                                          wx.DefaultSize, wx.LI_HORIZONTAL)
        sizer.Add(s_horizontal_line, 0, wx.EXPAND, 5)

        # Add fees receivable and free of charge
        receivable_free_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add fees receivable
        s_txt_receivable = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"应收：", wx.DefaultPosition,
                                         wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_receivable.Wrap(-1)
        receivable_free_sizer.Add(s_txt_receivable, 0, wx.ALIGN_CENTER, 5)

        self.txtReceivable = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                           wx.Size(100, -1), wx.ALIGN_CENTRE)
        self.txtReceivable.Wrap(-1)
        receivable_free_sizer.Add(self.txtReceivable, 0, wx.ALIGN_CENTER, 5)
        # Add free of charge
        s_txt_free = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"免单：", wx.DefaultPosition,
                                   wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_free.Wrap(-1)
        receivable_free_sizer.Add(s_txt_free, 0, wx.ALIGN_CENTER, 5)

        self.txtFree = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                     wx.Size(80, -1), wx.ALIGN_CENTRE)
        self.txtFree.Wrap(-1)
        receivable_free_sizer.Add(self.txtFree, 0, wx.ALIGN_CENTER, 5)

        sizer.Add(receivable_free_sizer, 1, wx.EXPAND, 5)

        # Add has been charged and deposit sizer
        charged_deposit_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add has been charged
        s_txt_charged = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"实收：", wx.DefaultPosition,
                                      wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_charged.Wrap(-1)
        charged_deposit_sizer.Add(s_txt_charged, 0, wx.ALIGN_CENTER, 5)

        self.txtCharged = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                        wx.Size(100, -1), wx.ALIGN_CENTRE)
        self.txtCharged.Wrap(-1)
        charged_deposit_sizer.Add(self.txtCharged, 0, wx.ALIGN_CENTER, 5)
        # Add deposit
        s_txt_deposit = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                      wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_deposit.Wrap(-1)
        charged_deposit_sizer.Add(s_txt_deposit, 0, wx.ALIGN_CENTER, 5)

        self.txtDeposit = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                        wx.Size(80, -1), wx.ALIGN_CENTRE)
        self.txtDeposit.Wrap(-1)
        charged_deposit_sizer.Add(self.txtDeposit, 0, wx.ALIGN_CENTER, 5)

        sizer.Add(charged_deposit_sizer, 1, wx.EXPAND, 5)

        # Add balance sizer
        balance_sizer = wx.BoxSizer(wx.HORIZONTAL)

        s_txt_balance = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                      wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_balance.Wrap(-1)
        balance_sizer.Add(s_txt_balance, 0, wx.ALIGN_CENTER, 5)

        self.txtBalance = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                        wx.Size(100, -1), wx.ALIGN_CENTRE)
        self.txtBalance.Wrap(-1)
        balance_sizer.Add(self.txtBalance, 0, wx.ALIGN_CENTER, 5)

        sizer.Add(balance_sizer, 1, wx.EXPAND, 5)

        # Add horizontal line
        s_horizontal_line = wx.StaticLine(self.tableInfoPanel, wx.ID_ANY, wx.DefaultPosition,
                                          wx.DefaultSize, wx.LI_HORIZONTAL)
        sizer.Add(s_horizontal_line, 0, wx.EXPAND, 5)

        # Add cash and keep the change
        cash_change_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add cash
        s_txt_cash = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"现金：", wx.DefaultPosition,
                                   wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_cash.Wrap(-1)
        cash_change_sizer.Add(s_txt_cash, 0, wx.ALIGN_CENTER, 5)

        self.txtCash = wx.TextCtrl(self.tableInfoPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.Size(100, 20), 0)
        cash_change_sizer.Add(self.txtCash, 0, wx.ALIGN_CENTER, 5)
        # Add keep the change
        s_txt_change = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"找零：", wx.DefaultPosition,
                                     wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_change.Wrap(-1)
        cash_change_sizer.Add(s_txt_change, 0, wx.ALIGN_CENTER, 5)

        self.txtChange = wx.TextCtrl(self.tableInfoPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.Size(80, 20), 0)
        cash_change_sizer.Add(self.txtChange, 0, wx.ALIGN_CENTER, 5)

        sizer.Add(cash_change_sizer, 1, wx.EXPAND, 5)

        # Layout
        self.tableInfoPanel.SetSizer(sizer)
        self.tableInfoPanel.Layout()
        parent.Add(self.tableInfoPanel, 1, wx.EXPAND, 5)

    def _init_cashier_info(self, parent):
        self.cashierPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(300, 210),
                                     wx.STATIC_BORDER | wx.TAB_TRAVERSAL)
        self.cashierPanel.SetBackgroundColour(wx.Colour(0xea, 0xd4, 0x99))

        sizer = wx.BoxSizer(wx.VERTICAL)

        # Add summary sizer
        summary_sizer = wx.BoxSizer(wx.HORIZONTAL)

        s_txt_cashier_type = wx.TextCtrl(self.cashierPanel, wx.ID_ANY, u"收银方式(非现金)", wx.DefaultPosition,
                                         wx.Size(143, -1), 0 | wx.RAISED_BORDER)
        s_txt_cashier_type.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        s_txt_cashier_type.SetBackgroundColour(wx.Colour(241, 197, 102))
        summary_sizer.Add(s_txt_cashier_type, 0, wx.ALIGN_CENTER, 5)

        self.txtMoney = wx.TextCtrl(self.cashierPanel, wx.ID_ANY, u"金额  0.0", wx.DefaultPosition,
                                    wx.Size(162, -1), 0 | wx.RAISED_BORDER)
        self.txtMoney.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        self.txtMoney.SetBackgroundColour(wx.Colour(241, 197, 102))
        summary_sizer.Add(self.txtMoney, 0, wx.ALIGN_CENTER, 5)

        sizer.Add(summary_sizer, 1, wx.EXPAND, 5)
        # Add coupon sizer
        coupon_sizer = wx.BoxSizer(wx.HORIZONTAL)
        s_txt_coupon = wx.TextCtrl(self.cashierPanel, wx.ID_ANY, u"优惠券", wx.DefaultPosition,
                                   wx.Size(143, -1), 0 | wx.RAISED_BORDER)
        s_txt_coupon.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        s_txt_coupon.SetBackgroundColour(wx.Colour(241, 197, 102))
        coupon_sizer.Add(s_txt_coupon, 0, wx.ALIGN_CENTER, 5)

        self.txtCoupon = wx.TextCtrl(self.cashierPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.Size(163, -1), 0 | wx.RAISED_BORDER)
        self.txtCoupon.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        self.txtCoupon.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        coupon_sizer.Add(self.txtCoupon, 0, wx.ALIGN_CENTER, 5)

        sizer.Add(coupon_sizer, 1, wx.EXPAND, 5)
        # Add membership card sizer
        membership_sizer = wx.BoxSizer(wx.HORIZONTAL)

        s_txt_membership = wx.TextCtrl(self.cashierPanel, wx.ID_ANY, u"会员卡", wx.DefaultPosition,
                                       wx.Size(143, -1), 0 | wx.RAISED_BORDER)
        s_txt_membership.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        s_txt_membership.SetBackgroundColour(wx.Colour(241, 197, 102))
        membership_sizer.Add(s_txt_membership, 0, wx.ALIGN_CENTER, 5)

        self.txtMembership = wx.TextCtrl(self.cashierPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.Size(163, -1), 0 | wx.RAISED_BORDER)
        self.txtMembership.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        self.txtMembership.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        membership_sizer.Add(self.txtMembership, 0, wx.ALIGN_CENTER, 5)

        sizer.Add(membership_sizer, 1, wx.EXPAND, 5)
        # Add pos sizer
        pos_sizer = wx.BoxSizer(wx.HORIZONTAL)

        s_txt_pos = wx.TextCtrl(self.cashierPanel, wx.ID_ANY, u"Pos支付 ", wx.DefaultPosition,
                                wx.Size(143, -1), 0 | wx.RAISED_BORDER)
        s_txt_pos.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        s_txt_pos.SetBackgroundColour(wx.Colour(241, 197, 102))
        pos_sizer.Add(s_txt_pos, 0, wx.ALIGN_CENTER, 5)

        self.txtPos = wx.TextCtrl(self.cashierPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                  wx.Size(163, -1), 0 | wx.RAISED_BORDER)
        self.txtPos.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        self.txtPos.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        pos_sizer.Add(self.txtPos, 0, wx.ALIGN_CENTER, 5)

        sizer.Add(pos_sizer, 1, wx.EXPAND, 5)
        # Add group sizer
        group_sizer = wx.BoxSizer(wx.HORIZONTAL)

        s_txt_group = wx.TextCtrl(self.cashierPanel, wx.ID_ANY, u"团购", wx.DefaultPosition,
                                  wx.Size(143, -1), 0 | wx.RAISED_BORDER)
        s_txt_group.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        s_txt_group.SetBackgroundColour(wx.Colour(241, 197, 102))
        group_sizer.Add(s_txt_group, 0, wx.ALIGN_CENTER, 5)

        self.txtGroup = wx.TextCtrl(self.cashierPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.Size(163, -1), 0 | wx.RAISED_BORDER)
        self.txtGroup.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        self.txtGroup.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        group_sizer.Add(self.txtGroup, 0, wx.ALIGN_CENTER, 5)

        sizer.Add(group_sizer, 1, wx.EXPAND, 5)
        # Add on credit sizer
        credit_sizer = wx.BoxSizer(wx.HORIZONTAL)

        s_txt_credit = wx.TextCtrl(self.cashierPanel, wx.ID_ANY, u"挂账", wx.DefaultPosition,
                                   wx.Size(143, -1), 0 | wx.RAISED_BORDER)
        s_txt_credit.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        s_txt_credit.SetBackgroundColour(wx.Colour(241, 197, 102))
        credit_sizer.Add(s_txt_credit, 0, wx.ALIGN_CENTER, 5)

        self.txtCredit = wx.TextCtrl(self.cashierPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.Size(163, -1), 0 | wx.RAISED_BORDER)
        self.txtCredit.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        self.txtCredit.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        credit_sizer.Add(self.txtCredit, 0, wx.ALIGN_CENTER, 5)

        sizer.Add(credit_sizer, 1, wx.EXPAND, 5)
        # Add boss sign sizer
        boss_sign_sizer = wx.BoxSizer(wx.HORIZONTAL)

        s_txt_boss_sign = wx.TextCtrl(self.cashierPanel, wx.ID_ANY, u"老板签单", wx.DefaultPosition,
                                      wx.Size(143, -1), 0 | wx.RAISED_BORDER)
        s_txt_boss_sign.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        s_txt_boss_sign.SetBackgroundColour(wx.Colour(241, 197, 102))
        boss_sign_sizer.Add(s_txt_boss_sign, 0, wx.ALIGN_CENTER, 5)

        self.txtBossSign = wx.TextCtrl(self.cashierPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.Size(163, -1), 0 | wx.RAISED_BORDER)
        self.txtBossSign.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        self.txtBossSign.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        boss_sign_sizer.Add(self.txtBossSign, 0, wx.ALIGN_CENTER, 5)

        sizer.Add(boss_sign_sizer, 1, wx.EXPAND, 5)
        # Add reserve sizer
        for i in range(1, 3):
            line_sizer = wx.BoxSizer(wx.HORIZONTAL)

            s_txt_type = wx.TextCtrl(self.cashierPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.Size(143, -1), 0 | wx.RAISED_BORDER)
            s_txt_type.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
            s_txt_type.SetBackgroundColour(wx.Colour(241, 197, 102))
            line_sizer.Add(s_txt_type, 0, wx.ALIGN_CENTER, 5)

            self.txtReserveMoney = wx.TextCtrl(self.cashierPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                               wx.Size(163, -1), 0 | wx.RAISED_BORDER)
            self.txtReserveMoney.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
            self.txtReserveMoney.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
            line_sizer.Add(self.txtReserveMoney, 0, wx.ALIGN_CENTER, 5)

            sizer.Add(line_sizer, 1, wx.EXPAND, 5)

        self.cashierPanel.SetSizer(sizer)
        self.cashierPanel.Layout()
        parent.Add(self.cashierPanel, 1, wx.EXPAND, 5)

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition,
                          size=wx.Size(800, 600), style=wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(0x51, 0x1c, 0x0a))

        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_status_bar(sizer)
        self._init_data_view_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.btnAllDiscount.Bind(wx.EVT_BUTTON, self.on_btn_alldiscount)
        self.btnDishesDiscount.Bind(wx.EVT_BUTTON, self.on_btn_dishes_discount)
        self.btnFree.Bind(wx.EVT_BUTTON, self.on_btn_free_order)
        self.btnPrevPrint.Bind(wx.EVT_BUTTON, self.on_btn_prev_print)
        self.btnCheckout.Bind(wx.EVT_BUTTON, self.on_btn_checkout)
        self.btnExit.Bind(wx.EVT_BUTTON, self.on_btn_exit)

        self.txtCoupon.Bind(wx.EVT_TEXT, self.on_txt_coupon)
        self.txtMembership.Bind(wx.EVT_TEXT, self.on_txt_membership)
        self.txtPos.Bind(wx.EVT_TEXT, self.on_txt_pos)
        self.txtGroup.Bind(wx.EVT_TEXT, self.on_txt_group)
        self.txtCredit.Bind(wx.EVT_TEXT, self.on_txt_credit)
        self.txtBossSign.Bind(wx.EVT_TEXT, self.on_txt_boss_sign)

        self.txtCash.Bind(wx.EVT_TEXT, self.on_txt_cash)

        self.Bind(wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.on_item_activated, self.dataViewCheckout)
        self.Bind(wx.dataview.EVT_DATAVIEW_SELECTION_CHANGED, self.on_item_changed, self.dataViewList)

        # define variable
        self.real_price = 0.0
        self.model = None
        self.cashier_total = 0.0
        self.cashier_coupon = 0.0
        self.cashier_membership = 0.0
        self.cashier_pos = 0.0
        self.cashier_group = 0.0
        self.cashier_credit = 0.0
        self.cashier_boss_sign = 0.0

        self.cash = 0.0

    def __del__(self):
        pass

    def initialize(self):
        # Create an instance of our model...
        table_num = CtrlTableInfo.get_instance().get_selected_item_id()
        order_num = CtrlTableInfo.get_instance().get_order_num(table_num)
        self.model = ModelOrderedDishes(CtrlOrderInfo.get_instance().get_order_dishes_items(order_num))
        # Tell the DVC to use the model
        self.dataViewList.AssociateModel(self.model)

        # Initialize
        self._init_table_data()
        self._init_consume_data()

        # Add event listener
        EvtManager.add_listener(self, EnumEvent.EVT_CHECKOUT_INFO_REFRESH, self.on_refresh)

        x, y = CtrlHomePage.get_instance().get_screen_size()
        self.SetSize(wx.Size(x, y))

        self.GetParent().SetTitle(u"结算")

    def un_initialize(self):
        # Remove event listener
        EvtManager.remove_listener(self, EnumEvent.EVT_CHECKOUT_INFO_REFRESH, self.on_refresh)

    def _init_table_data(self):
        table_num = CtrlTableInfo.get_instance().get_selected_item_id()
        table_item = CtrlTableInfo.get_instance().get_table_item(table_num)
        self.txtOrderNum.SetLabel(table_item.order_num if table_item.order_num is not None else "")
        self.txtTableNum.SetLabel(table_item.table_num)
        self.txtOpenTime.SetLabel(table_item.open_time)
        self.txtOpenMemo.SetLabel(table_item.memo)

        self.cashier_total = 0.0
        self.cashier_coupon = 0.0
        self.cashier_membership = 0.0
        self.cashier_pos = 0.0
        self.cashier_group = 0.0
        self.cashier_credit = 0.0
        self.cashier_boss_sign = 0.0

    def _init_consume_data(self):
        self.txtChange.Enable(False)
        self.txtConsume.SetLabel('')
        self.txtDiscount.SetLabel('')
        self.txtFree.SetLabel('')
        self.txtReceivable.SetLabel('')
        self.txtCharged.SetLabel('')
        self.txtCoupon.SetLabel('')
        self.txtMembership.SetLabel('')
        self.txtPos.SetLabel('')
        self.txtGroup.SetLabel('')
        self.txtCredit.SetLabel('')
        self.txtBossSign.SetLabel('')

        order_id = CtrlOrderInfo.get_instance().get_cur_order_id()
        if order_id is not None:
            order_item = CtrlOrderInfo.get_instance().get_order_item(order_id)
            if order_item is not None:
                order_item.cashier_coupon = 0.0
                order_item.cashier_membership = 0.0
                order_item.cashier_pos = 0.0
                order_item.cashier_group = 0.0
                order_item.cashier_credit = 0.0
                order_item.cashier_boss_sign = 0.0
                order_item.cashier_cash = 0.0
                self.txtConsume.SetLabel(str(order_item.place_money))
                self.txtDiscount.SetLabel(str(order_item.all_discount))
                self.txtFree.SetLabel(str(order_item.free_price))
                self.txtReceivable.SetLabel(str(order_item.place_money * order_item.all_discount))
                self.real_price = order_item.place_money * order_item.all_discount - order_item.free_price
                self.txtCharged.SetLabel(str(self.real_price))

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

        self.btnAllDiscount.SetSize(wx.Size(83, 70))
        self.btnAllDiscount.SetPosition(wx.Point(0, 6))

        self.btnDishesDiscount.SetSize(wx.Size(83, 70))
        self.btnDishesDiscount.SetPosition(wx.Point(85, 6))

        self.btnFree.SetSize(wx.Size(63, 70))
        self.btnFree.SetPosition(wx.Point(170, 6))

        self.btnPrevPrint.SetSize(wx.Size(63, 70))
        self.btnPrevPrint.SetPosition(wx.Point(235, 6))

        self.btnCheckout.SetSize(wx.Size(63, 70))
        self.btnCheckout.SetPosition(wx.Point(300, 6))

        self.btnExit.SetSize(wx.Size(63, 70))
        self.btnExit.SetPosition(wx.Point(365, 6))

        self.statusBarPanel.SetSize(wx.Size(x, 82))
        self.dishesViewPanel.SetMinSize(wx.Size(x-300, y-82-220))
        self.dataViewList.SetMinSize(wx.Size(x-300, y-82-220))
        self.checkoutViewPanel.SetMinSize(wx.Size(x-300, 210))
        self.dataViewCheckout.SetMinSize(wx.Size(x-300, 210))

        self.Refresh()

    def on_btn_alldiscount(self, event):
        pop_whole_discount = PopWholeOrderDiscount(self)
        pop_whole_discount.ShowModal()

    def on_btn_dishes_discount(self, event):
        pop_dishes_discount = PopDishesDiscount(self)
        pop_dishes_discount.ShowModal()

    def on_btn_free_order(self, event):
        pop_checkout_discount = PopCheckoutDiscount(self)
        pop_checkout_discount.ShowModal()

    def on_btn_prev_print(self, event):
        if self.cash + self.cashier_total - self.real_price < 0:
            dlg = wx.MessageDialog(self, u"余额不足", caption=u"结账")
            dlg.ShowModal()
        else:
            pop_prev_print = PopPrevPrint(self)
            pop_prev_print.ShowModal()

    def on_btn_checkout(self, event):
        if self.cash + self.cashier_total - self.real_price < 0:
            dlg = wx.MessageDialog(self, u"余额不足", caption=u"结账")
            dlg.ShowModal()
        else:
            pop_checkout = PopCheckout(self)
            pop_checkout.ShowModal()

    def on_btn_exit(self, event):
        event.Skip()
        AppManager.get_instance().switch_to_application('FrontPage')

    def on_txt_coupon(self, enent):
        if self.txtCoupon.GetValue() == '':
            self.cashier_coupon = 0.0
            self.refresh_cashier_info()
            return

        try:
            self.cashier_coupon = float(self.txtCoupon.GetValue())
            #self.txtCoupon.SetValue(str(self.cashier_coupon))
            self.refresh_cashier_info()
        except ValueError:
            self.txtCoupon.Remove(self.txtCoupon.GetInsertionPoint() - 1, self.txtCoupon.GetInsertionPoint())
            dlg = wx.MessageDialog(self, u"金额输入错误", caption=u"结账")
            dlg.ShowModal()

    def on_txt_membership(self, enent):
        if self.txtMembership.GetValue() == '':
            self.cashier_membership = 0.0
            self.refresh_cashier_info()
            return

        try:
            self.cashier_membership = float(self.txtMembership.GetValue())
            #self.txtMembership.SetValue(str(self.cashier_membership))
            self.refresh_cashier_info()
        except ValueError:
            self.txtMembership.Remove(self.txtMembership.GetInsertionPoint() - 1,
                                      self.txtMembership.GetInsertionPoint())
            dlg = wx.MessageDialog(self, u"金额输入错误", caption=u"结账")
            dlg.ShowModal()

    def on_txt_pos(self, enent):
        if self.txtPos.GetValue() == '':
            self.cashier_pos = 0.0
            self.refresh_cashier_info()
            return

        try:
            self.cashier_pos = float(self.txtPos.GetValue())
            #self.txtPos.SetValue(str(self.cashier_pos))
            self.refresh_cashier_info()
        except ValueError:
            self.txtPos.Remove(self.txtPos.GetInsertionPoint() - 1, self.txtPos.GetInsertionPoint())
            dlg = wx.MessageDialog(self, u"金额输入错误", caption=u"结账")
            dlg.ShowModal()

    def on_txt_group(self, enent):
        if self.txtGroup.GetValue() == '':
            self.cashier_group = 0.0
            self.refresh_cashier_info()
            return

        try:
            self.cashier_group = float(self.txtGroup.GetValue())
            #self.txtGroup.SetValue(str(self.cashier_group))
            self.refresh_cashier_info()
        except ValueError:
            self.txtGroup.Remove(self.txtGroup.GetInsertionPoint() - 1, self.txtGroup.GetInsertionPoint())
            dlg = wx.MessageDialog(self, u"金额输入错误", caption=u"结账")
            dlg.ShowModal()

    def on_txt_credit(self, enent):
        if self.txtCredit.GetValue() == '':
            self.cashier_credit = 0.0
            self.refresh_cashier_info()
            return

        try:
            self.cashier_credit = float(self.txtCredit.GetValue())
            #self.txtCredit.SetValue(str(self.cashier_credit))
            self.refresh_cashier_info()
        except ValueError:
            self.txtCredit.Remove(self.txtCredit.GetInsertionPoint() - 1, self.txtCredit.GetInsertionPoint())
            dlg = wx.MessageDialog(self, u"金额输入错误", caption=u"结账")
            dlg.ShowModal()

    def on_txt_boss_sign(self, enent):
        if self.txtBossSign.GetValue() == '':
            self.cashier_boss_sign = 0.0
            self.refresh_cashier_info()
            return

        try:
            self.cashier_boss_sign = float(self.txtBossSign.GetValue())
            #self.txtBossSign.SetValue(str(self.cashier_boss_sign))
            self.refresh_cashier_info()
        except ValueError:
            self.txtBossSign.Remove(self.txtBossSign.GetInsertionPoint() - 1, self.txtBossSign.GetInsertionPoint())
            dlg = wx.MessageDialog(self, u"金额输入错误", caption=u"结账")
            dlg.ShowModal()

    def on_txt_cash(self, enent):
        if self.txtCash.GetValue() == '':
            self.cash = 0.0
            self.refresh_cashier_info()
            return

        try:
            self.cash = float(self.txtCash.GetValue())
            self.refresh_cashier_info()
        except ValueError:
            self.txtCash.Remove(self.txtCash.GetInsertionPoint() - 1, self.txtCash.GetInsertionPoint())
            dlg = wx.MessageDialog(self, u"金额输入错误", caption=u"结账")
            dlg.ShowModal()

    def refresh_cashier_info(self):
        self.cashier_total = self.cashier_coupon + self.cashier_membership + self.cashier_pos + self.cashier_group + \
            self.cashier_credit + self.cashier_boss_sign

        if self.cashier_total > self.real_price:
            raise ValueError
        else:
            self.txtMoney.SetLabel(str(self.cashier_total))

        order_id = CtrlOrderInfo.get_instance().get_cur_order_id()
        if order_id is not None:
            order_item = CtrlOrderInfo.get_instance().get_order_item(order_id)
            if order_item is not None:
                order_item.cashier_coupon = self.cashier_coupon
                order_item.cashier_membership = self.cashier_membership
                order_item.cashier_pos = self.cashier_pos
                order_item.cashier_group = self.cashier_group
                order_item.cashier_credit = self.cashier_credit
                order_item.cashier_boss_sign = self.cashier_boss_sign
                order_item.cashier_cash = self.real_price - self.cashier_total

        #self.txtCash.SetValue(str(self.cash))
        if self.txtCash.GetValue() != '':
            self.txtChange.SetValue(str(self.cash - self.real_price + self.cashier_total))

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
            CtrlOrderInfo.get_instance().set_select_dishes_code(None)

    def on_refresh(self, event):
        self._init_consume_data()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = WgtCheckout(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()
