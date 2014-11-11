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
## Class PopWholeOrderDiscount
###########################################################################


class PopWholeOrderDiscount (wx.Dialog):
    def _init_ui(self, parent):
        # Add discount info
        discount_sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)
        discount_sizer.SetMinSize(wx.Size(-1, 120))
        # Add source discount sizer
        src_discount_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.s_txt_src_discount = wx.StaticText(self, wx.ID_ANY, u"原折扣：", wx.DefaultPosition,
                                                wx.Size(100, -1), wx.ALIGN_RIGHT)
        self.s_txt_src_discount.Wrap(-1)
        src_discount_sizer.Add(self.s_txt_src_discount, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtSrcDiscount = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        src_discount_sizer.Add(self.txtSrcDiscount, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        discount_sizer.Add(src_discount_sizer, 1, wx.EXPAND, 5)

        # Add special discount sizer
        special_discount_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.s_txt_spec_discount = wx.StaticText(self, wx.ID_ANY, u"特批折扣：", wx.DefaultPosition,
                                                 wx.Size(100, -1), wx.ALIGN_RIGHT)
        self.s_txt_spec_discount.Wrap(-1)
        special_discount_sizer.Add(self.s_txt_spec_discount, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtSpecDiscount = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        special_discount_sizer.Add(self.txtSpecDiscount, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        discount_sizer.Add(special_discount_sizer, 1, wx.EXPAND, 5)

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
        self.s_txt_src_discount = wx.StaticText(self, wx.ID_ANY, u"原折扣：", wx.DefaultPosition,
                                                wx.Size(100, -1), wx.ALIGN_RIGHT)
        self.s_txt_src_discount.Wrap(-1)
        src_discount_sizer.Add(self.s_txt_src_discount, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtSrcDiscount = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        src_discount_sizer.Add(self.txtSrcDiscount, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        discount_sizer.Add(src_discount_sizer, 1, wx.EXPAND, 5)

        # Add special discount sizer
        special_discount_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.s_txt_spec_discount = wx.StaticText(self, wx.ID_ANY, u"特批折扣：", wx.DefaultPosition,
                                                 wx.Size(100, -1), wx.ALIGN_RIGHT)
        self.s_txt_spec_discount.Wrap(-1)
        special_discount_sizer.Add(self.s_txt_spec_discount, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtSpecDiscount = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        special_discount_sizer.Add(self.txtSpecDiscount, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        discount_sizer.Add(special_discount_sizer, 1, wx.EXPAND, 5)

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

    def __del__(self):
        pass

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

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def on_btn_confirm(self, event):
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
        # Add spacer static text
        s_txt_spacer = wx.StaticLine(self.infoPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL)
        parent.Add(s_txt_spacer, 0, wx.ALL | wx.EXPAND, 5)

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
        # Add handout and service charge sizer
        handout_charge_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add handout
        s_txt_handout = wx.StaticText(container, wx.ID_ANY, u"赠送：", wx.DefaultPosition,
                                      wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_handout.Wrap(-1)
        handout_charge_sizer.Add(s_txt_handout, 0, wx.ALIGN_CENTER, 5)

        self.txtHandout = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(110, -1), 0)
        handout_charge_sizer.Add(self.txtHandout, 0, wx.ALIGN_CENTER, 5)
        # Add service charge
        s_txt_charge = wx.StaticText(container, wx.ID_ANY, u"服务费：", wx.DefaultPosition,
                                     wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_charge.Wrap(-1)
        handout_charge_sizer.Add(s_txt_charge, 0, wx.ALIGN_CENTER, 5)

        self.txtCharge = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(110, -1), 0)
        handout_charge_sizer.Add(self.txtCharge, 0, wx.ALIGN_CENTER, 5)

        sizer.Add(handout_charge_sizer, 1, wx.EXPAND, 5)
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

        sizer.Add(receivable_sizer, 1, wx.EXPAND, 5)

        # Layout
        parent.Add(sizer, 1, wx.EXPAND, 5)
        # Add spacer static text
        s_txt_spacer = wx.StaticLine(self.infoPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL)
        parent.Add(s_txt_spacer, 0, wx.ALL | wx.EXPAND, 5)

    def _init_checkout_info(self, parent):
        self.checkoutPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Add charged and free sizer
        charged_free_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add charged
        s_txt_charged = wx.StaticText(self.checkoutPanel, wx.ID_ANY, u"已收：", wx.DefaultPosition,
                                      wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_charged.Wrap(-1)
        charged_free_sizer.Add(s_txt_charged, 0, wx.ALIGN_CENTER, 5)

        self.txtCharged = wx.TextCtrl(self.checkoutPanel, wx.ID_ANY, wx.EmptyString,
                                      wx.DefaultPosition, wx.Size(120, -1), 0)
        charged_free_sizer.Add(self.txtCharged, 0, wx.ALIGN_CENTER, 5)
        # Add free
        s_txt_free = wx.StaticText(self.checkoutPanel, wx.ID_ANY, u"免单：", wx.DefaultPosition,
                                   wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_free.Wrap(-1)
        charged_free_sizer.Add(s_txt_free, 0, wx.ALIGN_CENTER, 5)

        self.txtFree = wx.TextCtrl(self.checkoutPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.Size(100, -1), 0)
        charged_free_sizer.Add(self.txtFree, 0, wx.ALIGN_CENTER, 5)
        # Add rounded
        s_txt_rounded = wx.StaticText(self.checkoutPanel, wx.ID_ANY, u"抹零：", wx.DefaultPosition,
                                      wx.Size(70, -1), wx.ALIGN_RIGHT)
        s_txt_rounded.Wrap(-1)
        charged_free_sizer.Add(s_txt_rounded, 0, wx.ALIGN_CENTER, 5)

        self.txtRounded = wx.TextCtrl(self.checkoutPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.Size(110, -1), 0)
        charged_free_sizer.Add(self.txtRounded, 0, wx.ALIGN_CENTER, 5)
        # Add deposit
        s_txt_deposit = wx.StaticText(self.checkoutPanel, wx.ID_ANY, u"押金：", wx.DefaultPosition,
                                      wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_deposit.Wrap(-1)
        charged_free_sizer.Add(s_txt_deposit, 0, wx.ALIGN_CENTER, 5)

        self.txtDeposit = wx.TextCtrl(self.checkoutPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.Size(110, -1), 0)
        charged_free_sizer.Add(self.txtDeposit, 0, wx.ALIGN_CENTER, 5)

        # Layout charged and free sizer
        sizer.Add(charged_free_sizer, 1, wx.EXPAND, 5)

        # Add balance sizer
        balance_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add balance
        s_txt_balance = wx.StaticText(self.checkoutPanel, wx.ID_ANY, u"余款：", wx.DefaultPosition,
                                      wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_balance.Wrap(-1)
        balance_sizer.Add(s_txt_balance, 0, wx.ALIGN_CENTER, 5)

        self.txtBalance = wx.TextCtrl(self.checkoutPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.Size(120, -1), 0)
        balance_sizer.Add(self.txtBalance, 0, wx.ALIGN_CENTER, 5)
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
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"埋单操作", pos=wx.DefaultPosition,
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
            CtrlOrderInfo.get_instance().check_out(self.table_item.table_id, self.table_item.order_id)
        self.Close()

    def on_btn_cancel(self, event):
        self.Close()

###########################################################################
## Class WgtCheckout
###########################################################################


class WgtCheckout (wx.Panel):
    def _init_status_bar(self, parent):
        self.statusBarPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 60), wx.TAB_TRAVERSAL)
        self.statusBarPanel.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.statusBarPanel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add all dishes discount button
        self.btnAllDiscount = wx.Button(self.statusBarPanel, wx.ID_ANY, u"全单折", wx.DefaultPosition,
                                        wx.Size(60, 60), 0)
        sizer.Add(self.btnAllDiscount, 0, 0, 5)
        # Add dishes discount button
        self.btnDishesDiscount = wx.Button(self.statusBarPanel, wx.ID_ANY, u"菜品折", wx.DefaultPosition,
                                           wx.Size(60, 60), 0)
        sizer.Add(self.btnDishesDiscount, 0, 0, 5)
        # Add free dishes button
        self.btnFree = wx.Button(self.statusBarPanel, wx.ID_ANY, u"免单", wx.DefaultPosition, wx.Size(60, 60), 0)
        sizer.Add(self.btnFree, 0, 0, 5)
        # Add vertical line
        s_vertical_line = wx.StaticLine(self.statusBarPanel, wx.ID_ANY, wx.DefaultPosition,
                                        wx.DefaultSize, wx.LI_VERTICAL)
        sizer.Add(s_vertical_line, 0, wx.EXPAND | wx.ALL, 5)
        # Add previous print button
        self.btnPrevPrint = wx.Button(self.statusBarPanel, wx.ID_ANY, u"预打", wx.DefaultPosition, wx.Size(60, 60), 0)
        sizer.Add(self.btnPrevPrint, 0, 0, 5)
        # Add checkout button
        self.btnCheckout = wx.Button(self.statusBarPanel, wx.ID_ANY, u"埋单", wx.DefaultPosition, wx.Size(60, 60), 0)
        sizer.Add(self.btnCheckout, 0, 0, 5)
        # Add exit button
        self.btnExit = wx.Button(self.statusBarPanel, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.Size(60, 60), 0)
        sizer.Add(self.btnExit, 0, 0, 5)

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
        self.dishesViewPanel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
        self.dishesViewPanel.SetMinSize(wx.Size(480, 300))
        # Add dishes list view sizer
        dishes_view_sizer = wx.BoxSizer(wx.VERTICAL)

        self.dataViewList = wx.dataview.DataViewCtrl(self.dishesViewPanel, wx.ID_ANY, wx.DefaultPosition,
                                                     wx.Size(480, 300), 0)
        self.dataViewList.AppendTextColumn(u"行号", 0)
        self.dataViewList.AppendTextColumn(u"菜品名称", 1)
        self.dataViewList.AppendTextColumn(u"规格", 2)
        self.dataViewList.AppendTextColumn(u"数量", 4)
        self.dataViewList.AppendTextColumn(u"退菜量", 9)
        self.dataViewList.AppendTextColumn(u"价格", 6)
        self.dataViewList.AppendTextColumn(u"加价", 8)
        dishes_view_sizer.Add(self.dataViewList, 0, wx.EXPAND, 5)

        # Layout dishes list view
        self.dishesViewPanel.SetSizer(dishes_view_sizer)
        self.dishesViewPanel.Layout()
        dishes_view_sizer.Fit(self.dishesViewPanel)
        sizer.Add(self.dishesViewPanel, 1, wx.EXPAND, 5)

        # Add checkout type list view sizer
        self.checkoutViewPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(480, 210), wx.TAB_TRAVERSAL)
        checkout_view_sizer = wx.BoxSizer(wx.VERTICAL)

        self.dataViewCheckout = wx.dataview.DataViewCtrl(self.checkoutViewPanel, wx.ID_ANY, wx.DefaultPosition,
                                                         wx.Size(480, 210), 0)
        self.dataViewCheckout.AppendTextColumn(u"行号", 0)
        self.dataViewCheckout.AppendTextColumn(u"收银方式", 1)
        self.dataViewCheckout.AppendTextColumn(u"实收金额", 2)
        self.dataViewCheckout.AppendTextColumn(u"付款金额", 3)
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
        self.tableInfoPanel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))

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
        s_txt_handout = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"赠送：", wx.DefaultPosition,
                                      wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_handout.Wrap(-1)
        handout_charge_sizer.Add(s_txt_handout, 0, wx.ALIGN_CENTER, 5)

        self.txtHandout = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                        wx.Size(100, -1), wx.ALIGN_CENTRE)
        self.txtHandout.Wrap(-1)
        handout_charge_sizer.Add(self.txtHandout, 0, wx.ALIGN_CENTER, 5)
        # Add service charge
        s_txt_charge = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"服务费：", wx.DefaultPosition,
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
        s_txt_offset = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"抵消差：", wx.DefaultPosition,
                                     wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_offset.Wrap(-1)
        offset_rounding_sizer.Add(s_txt_offset, 0, wx.ALIGN_CENTER, 5)

        self.txtOffset = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                       wx.Size(100, -1), wx.ALIGN_CENTRE)
        self.txtOffset.Wrap(-1)
        offset_rounding_sizer.Add(self.txtOffset, 0, wx.ALIGN_CENTER, 5)

        s_txt_rounding = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"抹零：", wx.DefaultPosition,
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
        s_txt_charged = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"已收：", wx.DefaultPosition,
                                      wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_charged.Wrap(-1)
        charged_deposit_sizer.Add(s_txt_charged, 0, wx.ALIGN_CENTER, 5)

        self.txtCharged = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                        wx.Size(100, -1), wx.ALIGN_CENTRE)
        self.txtCharged.Wrap(-1)
        charged_deposit_sizer.Add(self.txtCharged, 0, wx.ALIGN_CENTER, 5)
        # Add deposit
        s_txt_deposit = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"押金：", wx.DefaultPosition,
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

        s_txt_balance = wx.StaticText(self.tableInfoPanel, wx.ID_ANY, u"余额：", wx.DefaultPosition,
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
        self.cashierPanel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))

        sizer = wx.BoxSizer(wx.VERTICAL)

        # Add summary sizer
        summary_sizer = wx.BoxSizer(wx.HORIZONTAL)

        s_txt_cashier_type = wx.TextCtrl(self.cashierPanel, wx.ID_ANY, u"收银方式(非现金)", wx.DefaultPosition,
                                         wx.Size(143, -1), 0 | wx.RAISED_BORDER)
        s_txt_cashier_type.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        s_txt_cashier_type.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
        summary_sizer.Add(s_txt_cashier_type, 0, wx.ALIGN_CENTER, 5)

        self.txtMoney = wx.TextCtrl(self.cashierPanel, wx.ID_ANY, u"金额  0.0", wx.DefaultPosition,
                                    wx.Size(162, -1), 0 | wx.RAISED_BORDER)
        self.txtMoney.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        self.txtMoney.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
        summary_sizer.Add(self.txtMoney, 0, wx.ALIGN_CENTER, 5)

        sizer.Add(summary_sizer, 1, wx.EXPAND, 5)

        for i in range(1, 8):
            line_sizer = wx.BoxSizer(wx.HORIZONTAL)

            s_txt_type = wx.TextCtrl(self.cashierPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.Size(143, -1), 0 | wx.RAISED_BORDER)
            s_txt_type.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
            s_txt_type.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
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

        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_status_bar(sizer)
        self._init_data_view_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Create an instance of our model...
        table_num = CtrlTableInfo.get_instance().get_selected_item_id()
        order_num = CtrlTableInfo.get_instance().get_order_num(table_num)
        self.model = ModelOrderedDishes(CtrlOrderInfo.get_instance().get_order_dishes_items(order_num))
        # Tell the DVC to use the model
        self.dataViewList.AssociateModel(self.model)

        # Connect Events
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.btnAllDiscount.Bind(wx.EVT_BUTTON, self.on_btn_alldiscount)
        self.btnDishesDiscount.Bind(wx.EVT_BUTTON, self.on_btn_dishes_discount)
        self.btnFree.Bind(wx.EVT_BUTTON, self.on_btn_free_order)
        self.btnPrevPrint.Bind(wx.EVT_BUTTON, self.on_btn_prev_print)
        self.btnCheckout.Bind(wx.EVT_BUTTON, self.on_btn_checkout)
        self.btnExit.Bind(wx.EVT_BUTTON, self.on_btn_exit)

        # Initialize
        self._init_table_data()

    def __del__(self):
        pass

    def initialize(self):
        # Add event listener
        #EvtManager.add_listener(self, EnumEvent.EVT_DINING_ROOM_REFRESH, self.on_btn_refresh)

        x, y = CtrlHomePage.get_instance().get_screen_size()
        self.SetSize(wx.Size(x, y))

        self.GetParent().SetTitle(u"结算")

    def un_initialize(self):
        # Remove event listener
        #EvtManager.remove_listener(self, EnumEvent.EVT_DINING_ROOM_REFRESH, self.on_btn_refresh)
        pass

    def _init_table_data(self):
        table_num = CtrlTableInfo.get_instance().get_selected_item_id()
        table_item = CtrlTableInfo.get_instance().get_table_item(table_num)
        self.txtOrderNum.SetLabel(table_item.order_num if table_item.order_num is not None else "")
        self.txtTableNum.SetLabel(table_item.table_num)
        self.txtOpenTime.SetLabel(table_item.open_time)
        self.txtOpenMemo.SetLabel(table_item.memo)

    # Virtual event handlers, override them in your derived class
    def on_size(self, event):
        event.Skip()
        x, y = self.GetSize()

        self.btnAllDiscount.SetMaxSize(wx.Size(60, 60))
        self.btnDishesDiscount.SetMaxSize(wx.Size(60, 60))
        self.btnFree.SetMaxSize(wx.Size(60, 60))
        self.btnPrevPrint.SetMaxSize(wx.Size(60, 60))
        self.btnCheckout.SetMaxSize(wx.Size(60, 60))
        self.btnExit.SetMaxSize(wx.Size(60, 60))
        self.statusBarPanel.SetMaxSize(wx.Size(x, 60))
        self.dishesViewPanel.SetMinSize(wx.Size(x-300, y-60-220))
        self.dataViewList.SetMinSize(wx.Size(x-300, y-60-220))
        self.checkoutViewPanel.SetMinSize(wx.Size(x-300, 210))
        self.dataViewCheckout.SetMinSize(wx.Size(x-300, 210))

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
        pop_prev_print = PopPrevPrint(self)
        pop_prev_print.ShowModal()

    def on_btn_checkout(self, event):
        pop_checkout = PopCheckout(self)
        pop_checkout.ShowModal()

    def on_btn_exit(self, event):
        event.Skip()
        AppManager.get_instance().switch_to_application('FrontPage')


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = WgtCheckout(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()
