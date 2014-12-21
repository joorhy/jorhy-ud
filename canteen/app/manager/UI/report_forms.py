#!/usr/bin/env python
# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
from app.home_logic import CtrlHomePage
from app.app_manager import AppManager
from app.manager.logic.model import *
from app.manager.logic.ctrl import *
from framework.img_button import ImgButton

import wx
import wx.xrc
import wx.dataview
import wx.lib.masked as masked

import sys
import os

###########################################################################
## Class WgtBusinessInfo
###########################################################################


class WgtBusinessInfo (wx.Panel):
    def _init_top_control(self, parent):
        self.topCtrlPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(800, 50), wx.TAB_TRAVERSAL)
        self.topCtrlPanel.SetMaxSize(wx.Size(800, 50))

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add from and to date
        s_txt_date = wx.StaticText(self.topCtrlPanel, wx.ID_ANY, u"日期：", wx.DefaultPosition, wx.Size(80, -1),
                                   wx.ALIGN_RIGHT)
        s_txt_date.SetBackgroundColour(wx.Colour(235, 107, 72))
        s_txt_date.Wrap(-1)
        s_txt_date.SetFont(wx.Font(16, 70, 90, 92, False, wx.EmptyString))
        sizer.Add(s_txt_date, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.dateFrom = wx.DatePickerCtrl(self.topCtrlPanel, size=(120, -1), style=wx.DP_DROPDOWN | wx.DP_SHOWCENTURY)
        sizer.Add(self.dateFrom, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        h = self.dateFrom.GetSize().height
        spin_from = wx.SpinButton(self.topCtrlPanel, -1, wx.DefaultPosition, (-1, h), wx.SP_VERTICAL)
        self.timeFrom = masked.TimeCtrl(self.topCtrlPanel, -1, size=(-1, h), style=wx.TE_PROCESS_TAB,
                                        name="24 hour control", fmt24hr=True, spinButton=spin_from)
        sizer.Add(self.timeFrom, 0, wx.ALIGN_CENTER, 5)
        sizer.Add(spin_from, 0, wx.ALIGN_CENTER | wx.RIGHT, 5)

        s_txt_line = wx.StaticText(self.topCtrlPanel, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize,
                                   wx.ALIGN_RIGHT)
        s_txt_line.SetBackgroundColour(wx.Colour(235, 107, 72))
        s_txt_line.Wrap(-1)
        s_txt_line.SetFont(wx.Font(16, 70, 90, 92, False, wx.EmptyString))
        sizer.Add(s_txt_line, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.dateTo = wx.DatePickerCtrl(self.topCtrlPanel, size=(120, -1), style=wx.DP_DROPDOWN | wx.DP_SHOWCENTURY)
        sizer.Add(self.dateTo, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        h = self.dateTo.GetSize().height
        spin_to = wx.SpinButton(self.topCtrlPanel, -1, wx.DefaultPosition, (-1, h), wx.SP_VERTICAL)
        self.timeTo = masked.TimeCtrl(self.topCtrlPanel, -1, size=(-1, h), style=wx.TE_PROCESS_TAB,
                                      name="24 hour control", fmt24hr=True, spinButton=spin_to)
        sizer.Add(self.timeTo, 0, wx.ALIGN_CENTER, 5)
        sizer.Add(spin_to, 0, wx.ALIGN_CENTER | wx.RIGHT, 5)

        # Add spacer
        sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        # Add query button
        self.btnQuery = ImgButton(self.topCtrlPanel, u"query.png", u"s_query.png")
        self.btnQuery.SetSize(wx.Size(82, 38))
        sizer.Add(self.btnQuery, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add export button
        self.btnExport = ImgButton(self.topCtrlPanel, u"export.png", u"s_export.png")
        self.btnExport.SetSize(wx.Size(82, 38))
        sizer.Add(self.btnExport, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add exit button
        self.btnExit = ImgButton(self.topCtrlPanel, u"back.png", u"s_back.png")
        self.btnExit.SetSize(wx.Size(82, 38))
        sizer.Add(self.btnExit, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.topCtrlPanel.SetSizer(sizer)
        self.topCtrlPanel.Layout()
        parent.Add(self.topCtrlPanel, 1, wx.EXPAND, 5)

    def _init_data_view(self, parent):
        self.dataViewPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.dataViewPanel.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.dataViewCtrl = wx.dataview.DataViewCtrl(self.dataViewPanel, wx.ID_ANY, wx.DefaultPosition,
                                                     wx.Size(800, 400), 0)
        self.dataViewCtrl.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        self.dataViewCtrl.AppendTextColumn(u"序号", 0)
        self.dataViewCtrl.AppendTextColumn(u"桌次", 1)
        self.dataViewCtrl.AppendTextColumn(u"消费人次", 2)
        self.dataViewCtrl.AppendTextColumn(u"消费金额", 3)
        self.dataViewCtrl.AppendTextColumn(u"优惠金额", 4)
        self.dataViewCtrl.AppendTextColumn(u"收款金额", 5)
        self.dataViewCtrl.AppendTextColumn(u"发票金额", 6)
        self.dataViewCtrl.AppendTextColumn(u"人均消费", 7)
        self.dataViewCtrl.AppendTextColumn(u"现金", 8)
        self.dataViewCtrl.AppendTextColumn(u"优惠券", 9)
        self.dataViewCtrl.AppendTextColumn(u"会员卡", 10)
        self.dataViewCtrl.AppendTextColumn(u"POS支付", 11)
        self.dataViewCtrl.AppendTextColumn(u"团购", 12)
        self.dataViewCtrl.AppendTextColumn(u"挂账", 13)
        self.dataViewCtrl.AppendTextColumn(u"老板签单", 14)
        self.dataViewCtrl.AppendTextColumn(u"时间", 15)
        sizer.Add(self.dataViewCtrl, 0, wx.EXPAND, 5)

        self.dataViewPanel.SetSizer(sizer)
        self.dataViewPanel.Layout()
        sizer.Fit(self.dataViewPanel)
        parent.Add(self.dataViewPanel, 1, wx.EXPAND, 5)

    def _init_bottom_line_1(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add total consume
        s_txt_total = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"消费总额：", wx.DefaultPosition,
                                    wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_total.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        s_txt_total.Wrap(-1)
        sizer.Add(s_txt_total, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtTotal = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                      wx.Size(60, -1), wx.ALIGN_LEFT)
        self.txtTotal.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        self.txtTotal.Wrap(-1)
        sizer.Add(self.txtTotal, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add favourable money
        s_txt_favourable = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"优惠金额：", wx.DefaultPosition,
                                         wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_favourable.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        s_txt_favourable.Wrap(-1)
        sizer.Add(s_txt_favourable, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtFavourable = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                           wx.Size(60, -1), wx.ALIGN_LEFT)
        self.txtFavourable.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        self.txtFavourable.Wrap(-1)
        sizer.Add(self.txtFavourable, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add real money
        s_txt_real = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"实际金额：", wx.DefaultPosition,
                                   wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_real.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        s_txt_real.Wrap(-1)
        sizer.Add(s_txt_real, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtReal = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                     wx.Size(60, -1), wx.ALIGN_LEFT)
        self.txtReal.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        self.txtReal.Wrap(-1)
        sizer.Add(self.txtReal, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add bill number
        s_txt_bill = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"发票金额：", wx.DefaultPosition,
                                   wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_bill.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        s_txt_bill.Wrap(-1)
        sizer.Add(s_txt_bill, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtBillNum = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                        wx.Size(60, -1), wx.ALIGN_LEFT)
        self.txtBillNum.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        self.txtBillNum.Wrap(-1)
        sizer.Add(self.txtBillNum, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add customer number
        s_txt_customers = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"消费人次：", wx.DefaultPosition,
                                        wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_customers.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        s_txt_customers.Wrap(-1)
        sizer.Add(s_txt_customers, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtCustomer = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                         wx.Size(60, -1), wx.ALIGN_LEFT)
        self.txtCustomer.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        self.txtCustomer.Wrap(-1)
        sizer.Add(self.txtCustomer, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add average money
        s_txt_average = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"人均：", wx.DefaultPosition,
                                      wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_average.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        s_txt_average.Wrap(-1)
        sizer.Add(s_txt_average, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtAverage = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                        wx.Size(60, -1), wx.ALIGN_LEFT)
        self.txtAverage.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        self.txtAverage.Wrap(-1)
        sizer.Add(self.txtAverage, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add cash money
        s_txt_cash = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"现金：", wx.DefaultPosition,
                                   wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_cash.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        s_txt_cash.Wrap(-1)
        sizer.Add(s_txt_cash, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtCash = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                     wx.Size(60, -1), wx.ALIGN_LEFT)
        self.txtCash.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        self.txtCash.Wrap(-1)
        sizer.Add(self.txtCash, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Layout
        parent.Add(sizer, 0, wx.ALIGN_CENTER | wx.ALL, 5)

    def _init_bottom_line_2(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add coupon money
        s_txt_coupon = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"优惠券：", wx.DefaultPosition,
                                     wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_coupon.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        s_txt_coupon.Wrap(-1)
        sizer.Add(s_txt_coupon, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtCoupon = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                       wx.Size(60, -1), wx.ALIGN_LEFT)
        self.txtCoupon.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        self.txtCoupon.Wrap(-1)
        sizer.Add(self.txtCoupon, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add membership money
        s_txt_membership = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"会员卡：", wx.DefaultPosition,
                                         wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_membership.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        s_txt_membership.Wrap(-1)
        sizer.Add(s_txt_membership, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtMembership = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                           wx.Size(60, -1), wx.ALIGN_LEFT)
        self.txtMembership.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        self.txtMembership.Wrap(-1)
        sizer.Add(self.txtMembership, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add pos money
        s_txt_pos = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"POS支付：", wx.DefaultPosition,
                                  wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_pos.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        s_txt_pos.Wrap(-1)
        sizer.Add(s_txt_pos, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtPos = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                    wx.Size(60, -1), wx.ALIGN_LEFT)
        self.txtPos.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        self.txtPos.Wrap(-1)
        sizer.Add(self.txtPos, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add group money
        s_txt_group = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"团购：", wx.DefaultPosition,
                                    wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_group.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        s_txt_group.Wrap(-1)
        sizer.Add(s_txt_group, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtGroup = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                      wx.Size(60, -1), wx.ALIGN_LEFT)
        self.txtGroup.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        self.txtGroup.Wrap(-1)
        sizer.Add(self.txtGroup, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add credit money
        s_txt_credit = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"挂账：", wx.DefaultPosition,
                                     wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_credit.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        s_txt_credit.Wrap(-1)
        sizer.Add(s_txt_credit, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtCredit = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                       wx.Size(60, -1), wx.ALIGN_LEFT)
        self.txtCredit.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        self.txtCredit.Wrap(-1)
        sizer.Add(self.txtCredit, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add boss sign money
        s_txt_boss_sign = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"老板签单：", wx.DefaultPosition,
                                        wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_boss_sign.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        s_txt_boss_sign.Wrap(-1)
        sizer.Add(s_txt_boss_sign, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtBossSign = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                         wx.Size(60, -1), wx.ALIGN_LEFT)
        self.txtBossSign.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        self.txtBossSign.Wrap(-1)
        sizer.Add(self.txtBossSign, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add reserve money
        s_txt_reserve = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                      wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_reserve.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        s_txt_reserve.Wrap(-1)
        sizer.Add(s_txt_reserve, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtReserve = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                        wx.Size(60, -1), wx.ALIGN_LEFT)
        self.txtReserve.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        self.txtReserve.Wrap(-1)
        sizer.Add(self.txtReserve, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Layout
        parent.Add(sizer, 0, wx.ALIGN_CENTER | wx.ALL, 5)

    def _init_bottom_control(self, parent):
        self.bottomCtrlPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.bottomCtrlPanel.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))

        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_bottom_line_1(sizer)
        self._init_bottom_line_2(sizer)
        # Layout
        self.bottomCtrlPanel.SetSizer(sizer)
        self.bottomCtrlPanel.Layout()
        sizer.Fit(self.bottomCtrlPanel)
        parent.Add(self.bottomCtrlPanel, 1, wx.EXPAND | wx.TOP, 5)

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(800, 600),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.SetBackgroundColour(wx.Colour(0x51, 0x1c, 0x0a))
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_top_control(sizer)
        self._init_data_view(sizer)
        self._init_bottom_control(sizer)
        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_SIZE, self.on_size)

        self.btnQuery.Bind(wx.EVT_BUTTON, self.on_btn_query)
        self.btnExport.Bind(wx.EVT_BUTTON, self.on_btn_export)
        self.btnExit.Bind(wx.EVT_BUTTON, self.on_btn_exit)

        # define variable
        self.model = None

    def __del__(self):
        pass

    def initialize(self):
        date_from, time_from, date_to, time_to = CtrlBusinessInfo.get_instance().get_query_time()
        if date_from is not None:
            self.dateFrom.SetValue(date_from)
        if time_from is not None:
            self.timeFrom.SetValue(time_from)
        if date_to is not None:
            self.dateTo.SetValue(date_to)
        if time_to is not None:
            self.timeTo.SetValue(time_to)

        # Create an instance of our model...
        self.model = ModelBusinessInfo(CtrlBusinessInfo.get_instance().get_business_items())
        # Tel the DVC to use the model
        self.dataViewCtrl.AssociateModel(self.model)

        # Add event listener
        EvtManager.add_listener(self, EnumEvent.EVT_BUSINESS_INFO_REFRESH, self.on_refresh)

        x, y = CtrlHomePage.get_instance().get_screen_size()
        self.SetSize(wx.Size(x, y))

    def un_initialize(self):
        # Remove event listener
        EvtManager.remove_listener(self, EnumEvent.EVT_BUSINESS_INFO_REFRESH, self.on_refresh)

    # Virtual event handlers, override them in your derived class
    def on_paint(self, event):
        dc = wx.ClientDC(self.topCtrlPanel)
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

        self.topCtrlPanel.SetMaxSize(wx.Size(x, 82))

        self.dataViewPanel.SetMinSize(wx.Size(x, y - 164))
        self.dataViewCtrl.SetMinSize(wx.Size(x, y - 164))

        self.bottomCtrlPanel.SetMaxSize(wx.Size(x, 82))

        self.Refresh()

    def on_btn_query(self, event):
        event.Skip()
        if (self.dateTo.GetValue() - self.dateFrom.GetValue()).days < 0:
            dlg = wx.MessageDialog(self, u"日期输入有误", caption=u"消费查询")
            dlg.ShowModal()
        else:
            CtrlBusinessInfo.get_instance().query_business(self.dateFrom.GetValue(), self.timeFrom.GetValue(),
                                                           self.dateTo.GetValue(), self.timeTo.GetValue())

    def on_btn_export(self, event):
        event.Skip()
        dlg = wx.FileDialog(
            self, message=u"选择保存路径",
            defaultDir=os.getcwd(),
            defaultFile="",
            wildcard="excel file (*.xlsx) |*.xlsx",
            style=wx.SAVE | wx.CHANGE_DIR)

        # Show the dialog and retrieve the user response. If it is the OK response,
        # process the data.
        if dlg.ShowModal() == wx.ID_OK:
            # This returns a Python list of files that were selected.
            file_name = dlg.GetPath()
            CtrlBusinessInfo.get_instance().export_business(file_name)

    def on_btn_exit(self, event):
        event.Skip()
        self.Hide()
        AppManager.get_instance().switch_to_application('HomePage')

    def on_refresh(self, event):
        # Refresh data view list
        consume_price, real_price, consumer_num, bill_total, cash_total, coupon_total, membership_total, pos_total,\
            group_total, credit_total, boss_sign_total = CtrlBusinessInfo.get_instance().get_summary_info()
        free_price = consume_price - real_price
        average_price = 0
        if consumer_num > 0:
            average_price = round((consume_price / consumer_num), 2)
        self.txtTotal.SetLabel(str(consume_price))
        self.txtFavourable.SetLabel(str(free_price))
        self.txtReal.SetLabel(str(real_price))
        self.txtCustomer.SetLabel(str(consumer_num))
        self.txtBillNum.SetLabel(str(bill_total))
        self.txtAverage.SetLabel(str(average_price))
        self.txtCash.SetLabel(str(cash_total))
        self.txtCoupon.SetLabel(str(coupon_total))
        self.txtMembership.SetLabel(str(membership_total))
        self.txtPos.SetLabel(str(pos_total))
        self.txtGroup.SetLabel(str(group_total))
        self.txtCredit.SetLabel(str(credit_total))
        self.txtBossSign.SetLabel(str(boss_sign_total))

        self.model.Cleared()


###########################################################################
## Class WgtSalesInfo
###########################################################################

class WgtSalesInfo (wx.Panel):
    def _init_top_control(self, parent):
        self.topCtrlPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(800, 50), wx.TAB_TRAVERSAL)
        self.topCtrlPanel.SetMaxSize(wx.Size(800, 50))

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add from and to date
        s_txt_date = wx.StaticText(self.topCtrlPanel, wx.ID_ANY, u"日期：", wx.DefaultPosition, wx.Size(80, -1),
                                   wx.ALIGN_RIGHT)
        s_txt_date.SetBackgroundColour(wx.Colour(235, 107, 72))
        s_txt_date.Wrap(-1)
        s_txt_date.SetFont(wx.Font(16, 70, 90, 92, False, wx.EmptyString))
        sizer.Add(s_txt_date, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.dateFrom = wx.DatePickerCtrl(self.topCtrlPanel, size=(120, -1), style=wx.DP_DROPDOWN | wx.DP_SHOWCENTURY)
        sizer.Add(self.dateFrom, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        h = self.dateFrom.GetSize().height
        spin_from = wx.SpinButton(self.topCtrlPanel, -1, wx.DefaultPosition, (-1, h), wx.SP_VERTICAL)
        self.timeFrom = masked.TimeCtrl(self.topCtrlPanel, -1, size=(-1, h), style=wx.TE_PROCESS_TAB,
                                        name="24 hour control", fmt24hr=True, spinButton=spin_from)
        sizer.Add(self.timeFrom, 0, wx.ALIGN_CENTER, 5)
        sizer.Add(spin_from, 0, wx.ALIGN_CENTER | wx.RIGHT, 5)

        s_txt_line = wx.StaticText(self.topCtrlPanel, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize,
                                   wx.ALIGN_RIGHT)
        s_txt_line.SetBackgroundColour(wx.Colour(235, 107, 72))
        s_txt_line.Wrap(-1)
        s_txt_line.SetFont(wx.Font(16, 70, 90, 92, False, wx.EmptyString))
        sizer.Add(s_txt_line, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.dateTo = wx.DatePickerCtrl(self.topCtrlPanel, size=(120, -1), style=wx.DP_DROPDOWN | wx.DP_SHOWCENTURY)
        sizer.Add(self.dateTo, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        h = self.dateTo.GetSize().height
        spin_to = wx.SpinButton(self.topCtrlPanel, -1, wx.DefaultPosition, (-1, h), wx.SP_VERTICAL)
        self.timeTo = masked.TimeCtrl(self.topCtrlPanel, -1, size=(-1, h), style=wx.TE_PROCESS_TAB,
                                      name="24 hour control", fmt24hr=True, spinButton=spin_to)
        sizer.Add(self.timeTo, 0, wx.ALIGN_CENTER, 5)
        sizer.Add(spin_to, 0, wx.ALIGN_CENTER | wx.RIGHT, 5)

        # Add spacer
        sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        # Add query button
        self.btnQuery = ImgButton(self.topCtrlPanel, u"query.png", u"s_query.png")
        self.btnQuery.SetSize(wx.Size(82, 38))
        sizer.Add(self.btnQuery, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add export button
        self.btnExport = ImgButton(self.topCtrlPanel, u"export.png", u"s_export.png")
        self.btnExport.SetSize(wx.Size(82, 38))
        sizer.Add(self.btnExport, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add exit button
        self.btnExit = ImgButton(self.topCtrlPanel, u"back.png", u"s_back.png")
        self.btnExit.SetSize(wx.Size(82, 38))
        sizer.Add(self.btnExit, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.topCtrlPanel.SetSizer(sizer)
        self.topCtrlPanel.Layout()
        parent.Add(self.topCtrlPanel, 1, wx.EXPAND, 5)

    def _init_data_view(self, parent):
        self.dataViewPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.dataViewPanel.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.dataViewCtrl = wx.dataview.DataViewCtrl(self.dataViewPanel, wx.ID_ANY, wx.DefaultPosition,
                                                     wx.Size(800, 400), 0)
        self.dataViewCtrl.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        self.dataViewCtrl.AppendTextColumn(u"序号", 0)
        self.dataViewCtrl.AppendTextColumn(u"桌台", 1)
        self.dataViewCtrl.AppendTextColumn(u"人次", 2)
        self.dataViewCtrl.AppendTextColumn(u"消费金额", 3)
        self.dataViewCtrl.AppendTextColumn(u"优惠金额", 4)
        self.dataViewCtrl.AppendTextColumn(u"实际金额", 5)
        self.dataViewCtrl.AppendTextColumn(u"发票金额", 6)
        self.dataViewCtrl.AppendTextColumn(u"现金", 7)
        self.dataViewCtrl.AppendTextColumn(u"优惠券", 8)
        self.dataViewCtrl.AppendTextColumn(u"会员卡", 9)
        self.dataViewCtrl.AppendTextColumn(u"POS支付", 10)
        self.dataViewCtrl.AppendTextColumn(u"团购", 11)
        self.dataViewCtrl.AppendTextColumn(u"挂账", 12)
        self.dataViewCtrl.AppendTextColumn(u"老板签单", 13)
        self.dataViewCtrl.AppendTextColumn(u"时间", 14, width=150)
        sizer.Add(self.dataViewCtrl, 0, wx.EXPAND, 5)

        self.dataViewPanel.SetSizer(sizer)
        self.dataViewPanel.Layout()
        sizer.Fit(self.dataViewPanel)
        parent.Add(self.dataViewPanel, 1, wx.EXPAND, 5)

    def _init_bottom_line_1(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add total consume
        s_txt_total = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"消费总额：", wx.DefaultPosition,
                                    wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_total.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        s_txt_total.Wrap(-1)
        sizer.Add(s_txt_total, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtTotal = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                      wx.Size(60, -1), wx.ALIGN_LEFT)
        self.txtTotal.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        self.txtTotal.Wrap(-1)
        sizer.Add(self.txtTotal, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add favourable money
        s_txt_favourable = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"优惠金额：", wx.DefaultPosition,
                                         wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_favourable.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        s_txt_favourable.Wrap(-1)
        sizer.Add(s_txt_favourable, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtFavourable = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                           wx.Size(60, -1), wx.ALIGN_LEFT)
        self.txtFavourable.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        self.txtFavourable.Wrap(-1)
        sizer.Add(self.txtFavourable, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add real money
        s_txt_real = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"实际收款额：", wx.DefaultPosition,
                                   wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_real.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        s_txt_real.Wrap(-1)
        sizer.Add(s_txt_real, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtReal = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                     wx.Size(60, -1), wx.ALIGN_LEFT)
        self.txtReal.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        self.txtReal.Wrap(-1)
        sizer.Add(self.txtReal, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add bill number
        s_txt_bill = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"发票金额：", wx.DefaultPosition,
                                   wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_bill.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        s_txt_bill.Wrap(-1)
        sizer.Add(s_txt_bill, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtBillNum = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                        wx.Size(60, -1), wx.ALIGN_LEFT)
        self.txtBillNum.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        self.txtBillNum.Wrap(-1)
        sizer.Add(self.txtBillNum, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add customer number
        s_txt_customers = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"消费人次：", wx.DefaultPosition,
                                        wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_customers.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        s_txt_customers.Wrap(-1)
        sizer.Add(s_txt_customers, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtCustomer = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                         wx.Size(60, -1), wx.ALIGN_LEFT)
        self.txtCustomer.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        self.txtCustomer.Wrap(-1)
        sizer.Add(self.txtCustomer, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add average money
        s_txt_average = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"人均：", wx.DefaultPosition,
                                      wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_average.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        s_txt_average.Wrap(-1)
        sizer.Add(s_txt_average, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtAverage = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                        wx.Size(60, -1), wx.ALIGN_LEFT)
        self.txtAverage.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        self.txtAverage.Wrap(-1)
        sizer.Add(self.txtAverage, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add cash money
        s_txt_cash = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"现金：", wx.DefaultPosition,
                                   wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_cash.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        s_txt_cash.Wrap(-1)
        sizer.Add(s_txt_cash, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtCash = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                     wx.Size(60, -1), wx.ALIGN_LEFT)
        self.txtCash.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        self.txtCash.Wrap(-1)
        sizer.Add(self.txtCash, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Layout
        parent.Add(sizer, 0, wx.ALIGN_CENTER | wx.ALL, 5)

    def _init_bottom_line_2(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add coupon money
        s_txt_coupon = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"优惠券：", wx.DefaultPosition,
                                     wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_coupon.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        s_txt_coupon.Wrap(-1)
        sizer.Add(s_txt_coupon, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtCoupon = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                       wx.Size(60, -1), wx.ALIGN_LEFT)
        self.txtCoupon.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        self.txtCoupon.Wrap(-1)
        sizer.Add(self.txtCoupon, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add membership money
        s_txt_membership = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"会员卡：", wx.DefaultPosition,
                                         wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_membership.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        s_txt_membership.Wrap(-1)
        sizer.Add(s_txt_membership, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtMembership = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                           wx.Size(60, -1), wx.ALIGN_LEFT)
        self.txtMembership.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        self.txtMembership.Wrap(-1)
        sizer.Add(self.txtMembership, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add pos money
        s_txt_pos = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"POS支付：", wx.DefaultPosition,
                                  wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_pos.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        s_txt_pos.Wrap(-1)
        sizer.Add(s_txt_pos, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtPos = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                    wx.Size(60, -1), wx.ALIGN_LEFT)
        self.txtPos.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        self.txtPos.Wrap(-1)
        sizer.Add(self.txtPos, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add group money
        s_txt_group = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"团购：", wx.DefaultPosition,
                                    wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_group.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        s_txt_group.Wrap(-1)
        sizer.Add(s_txt_group, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtGroup = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                      wx.Size(60, -1), wx.ALIGN_LEFT)
        self.txtGroup.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        self.txtGroup.Wrap(-1)
        sizer.Add(self.txtGroup, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add credit money
        s_txt_credit = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"挂账：", wx.DefaultPosition,
                                     wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_credit.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        s_txt_credit.Wrap(-1)
        sizer.Add(s_txt_credit, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtCredit = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                       wx.Size(60, -1), wx.ALIGN_LEFT)
        self.txtCredit.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        self.txtCredit.Wrap(-1)
        sizer.Add(self.txtCredit, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add boss sign money
        s_txt_boss_sign = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"老板签单：", wx.DefaultPosition,
                                        wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_boss_sign.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        s_txt_boss_sign.Wrap(-1)
        sizer.Add(s_txt_boss_sign, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtBossSign = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                         wx.Size(60, -1), wx.ALIGN_LEFT)
        self.txtBossSign.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        self.txtBossSign.Wrap(-1)
        sizer.Add(self.txtBossSign, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add reserve money
        s_txt_reserve = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                      wx.Size(60, -1), wx.ALIGN_RIGHT)
        s_txt_reserve.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        s_txt_reserve.Wrap(-1)
        sizer.Add(s_txt_reserve, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtReserve = wx.StaticText(self.bottomCtrlPanel, wx.ID_ANY, u"", wx.DefaultPosition,
                                        wx.Size(60, -1), wx.ALIGN_LEFT)
        self.txtReserve.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        self.txtReserve.Wrap(-1)
        sizer.Add(self.txtReserve, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Layout
        parent.Add(sizer, 0, wx.ALIGN_CENTER | wx.ALL, 5)

    def _init_bottom_control(self, parent):
        self.bottomCtrlPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.bottomCtrlPanel.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))

        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_bottom_line_1(sizer)
        self._init_bottom_line_2(sizer)

        # Layout
        self.bottomCtrlPanel.SetSizer(sizer)
        self.bottomCtrlPanel.Layout()
        sizer.Fit(self.bottomCtrlPanel)
        parent.Add(self.bottomCtrlPanel, 1, wx.EXPAND | wx.TOP, 5)

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(800, 600),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.SetBackgroundColour(wx.Colour(0x51, 0x1c, 0x0a))
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_top_control(sizer)
        self._init_data_view(sizer)
        self._init_bottom_control(sizer)
        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_SIZE, self.on_size)

        self.btnQuery.Bind(wx.EVT_BUTTON, self.on_btn_query)
        self.btnExport.Bind(wx.EVT_BUTTON, self.on_btn_export)
        self.btnExit.Bind(wx.EVT_BUTTON, self.on_btn_exit)

        # define variable
        self.model = None

    def __del__(self):
        pass

    def initialize(self):
        date_from, time_from, date_to, time_to = CtrlSalesInfo.get_instance().get_query_time()
        if date_from is not None:
            self.dateFrom.SetValue(date_from)
        if time_from is not None:
            self.timeFrom.SetValue(time_from)
        if date_to is not None:
            self.dateTo.SetValue(date_to)
        if time_to is not None:
            self.timeTo.SetValue(time_to)

        # Create an instance of our model...
        self.model = ModelSalesInfo(CtrlSalesInfo.get_instance().get_sales_items())
        # Tel the DVC to use the model
        self.dataViewCtrl.AssociateModel(self.model)

        # Add event listener
        EvtManager.add_listener(self, EnumEvent.EVT_SALES_INFO_REFRESH, self.on_refresh)

        x, y = CtrlHomePage.get_instance().get_screen_size()
        self.SetSize(wx.Size(x, y))

    def un_initialize(self):
        # Remove event listener
        EvtManager.remove_listener(self, EnumEvent.EVT_SALES_INFO_REFRESH, self.on_refresh)

    # Virtual event handlers, override them in your derived class
    def on_paint(self, event):
        dc = wx.ClientDC(self.topCtrlPanel)
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

        self.topCtrlPanel.SetMaxSize(wx.Size(x, 82))

        self.dataViewPanel.SetMinSize(wx.Size(x, y - 164))
        self.dataViewCtrl.SetMinSize(wx.Size(x, y - 164))

        self.bottomCtrlPanel.SetMaxSize(wx.Size(x, 82))

        self.Refresh()

    def on_btn_query(self, event):
        event.Skip()
        if (self.dateTo.GetValue() - self.dateFrom.GetValue()).days < 0:
            dlg = wx.MessageDialog(self, u"日期输入有误", caption=u"消费流水查询")
            dlg.ShowModal()
        else:
            CtrlSalesInfo.get_instance().query_sales(self.dateFrom.GetValue(), self.timeFrom.GetValue(),
                                                     self.dateTo.GetValue(), self.timeTo.GetValue())

    def on_btn_export(self, event):
        event.Skip()
        dlg = wx.FileDialog(
            self, message=u"选择保存路径",
            defaultDir=os.getcwd(),
            defaultFile="",
            wildcard="excel file (*.xlsx) |*.xlsx",
            style=wx.SAVE | wx.CHANGE_DIR)

        # Show the dialog and retrieve the user response. If it is the OK response,
        # process the data.
        if dlg.ShowModal() == wx.ID_OK:
            # This returns a Python list of files that were selected.
            file_name = dlg.GetPath()
            CtrlSalesInfo.get_instance().export_sales(file_name)

    def on_btn_exit(self, event):
        event.Skip()
        self.Hide()
        AppManager.get_instance().switch_to_application('HomePage')

    def on_refresh(self, event):
        # Refresh data view list
        consume_price, real_price, consumer_num, bill_total, cash_total, coupon_total, membership_total, pos_total,\
            group_total, credit_total, boss_sign_total = CtrlSalesInfo.get_instance().get_summary_info()
        free_price = consume_price - real_price
        average_price = 0
        if consumer_num > 0:
            average_price = round((consume_price / consumer_num), 2)
        self.txtTotal.SetLabel(str(consume_price))
        self.txtFavourable.SetLabel(str(free_price))
        self.txtReal.SetLabel(str(real_price))
        self.txtCustomer.SetLabel(str(consumer_num))
        self.txtAverage.SetLabel(str(average_price))
        self.txtBillNum.SetLabel(str(bill_total))
        self.txtAverage.SetLabel(str(average_price))
        self.txtCash.SetLabel(str(cash_total))
        self.txtCoupon.SetLabel(str(coupon_total))
        self.txtMembership.SetLabel(str(membership_total))
        self.txtPos.SetLabel(str(pos_total))
        self.txtGroup.SetLabel(str(group_total))
        self.txtCredit.SetLabel(str(credit_total))
        self.txtBossSign.SetLabel(str(boss_sign_total))

        self.model.Cleared()


###########################################################################
## Class WgtBillboardInfo
###########################################################################

class WgtBillboardInfo (wx.Panel):
    def _init_top_control(self, parent):
        self.topCtrlPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(800, 50), wx.TAB_TRAVERSAL)
        self.topCtrlPanel.SetMaxSize(wx.Size(800, 50))

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add from and to date
        s_txt_date = wx.StaticText(self.topCtrlPanel, wx.ID_ANY, u"日期：", wx.DefaultPosition, wx.Size(80, -1),
                                   wx.ALIGN_RIGHT)
        s_txt_date.SetBackgroundColour(wx.Colour(235, 107, 72))
        s_txt_date.Wrap(-1)
        s_txt_date.SetFont(wx.Font(16, 70, 90, 92, False, wx.EmptyString))
        sizer.Add(s_txt_date, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.dateFrom = wx.DatePickerCtrl(self.topCtrlPanel, size=(120, -1), style=wx.DP_DROPDOWN | wx.DP_SHOWCENTURY)
        sizer.Add(self.dateFrom, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        s_txt_line = wx.StaticText(self.topCtrlPanel, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize,
                                   wx.ALIGN_RIGHT)
        s_txt_line.SetBackgroundColour(wx.Colour(235, 107, 72))
        s_txt_line.Wrap(-1)
        s_txt_line.SetFont(wx.Font(16, 70, 90, 92, False, wx.EmptyString))
        sizer.Add(s_txt_line, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.dateTo = wx.DatePickerCtrl(self.topCtrlPanel, size=(120, -1), style=wx.DP_DROPDOWN | wx.DP_SHOWCENTURY)
        sizer.Add(self.dateTo, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add dishes category
        s_txt_category = wx.StaticText(self.topCtrlPanel, wx.ID_ANY, u"菜类：", wx.DefaultPosition,
                                       wx.Size(80, -1), wx.ALIGN_RIGHT)
        s_txt_category.SetBackgroundColour(wx.Colour(235, 107, 72))
        s_txt_category.Wrap(-1)
        s_txt_category.SetFont(wx.Font(16, 70, 90, 92, False, wx.EmptyString))

        sizer.Add(s_txt_category, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        cbx_category_choices = list()
        self.cbxCategory = wx.ComboBox(self.topCtrlPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, cbx_category_choices, 0)
        sizer.Add(self.cbxCategory, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add spacer
        sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        # Add query button
        self.btnQuery = ImgButton(self.topCtrlPanel, u"query.png", u"s_query.png")
        self.btnQuery.SetSize(wx.Size(82, 38))
        sizer.Add(self.btnQuery, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add export button
        self.btnExport = ImgButton(self.topCtrlPanel, u"export.png", u"s_export.png")
        self.btnExport.SetSize(wx.Size(82, 38))
        sizer.Add(self.btnExport, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add exit button
        self.btnExit = ImgButton(self.topCtrlPanel, u"back.png", u"s_back.png")
        self.btnExit.SetSize(wx.Size(82, 38))
        sizer.Add(self.btnExit, 0, wx.ALIGN_CENTER, 5)

        self.topCtrlPanel.SetSizer(sizer)
        self.topCtrlPanel.Layout()
        parent.Add(self.topCtrlPanel, 1, wx.EXPAND, 5)

    def _init_data_view(self, parent):
        self.dataViewPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.dataViewPanel.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.dataViewCtrl = wx.dataview.DataViewCtrl(self.dataViewPanel, wx.ID_ANY, wx.DefaultPosition,
                                                     wx.Size(800, 400), 0)
        self.dataViewCtrl.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        self.dataViewCtrl.AppendTextColumn(u"序号", 0)
        self.dataViewCtrl.AppendTextColumn(u"菜名", 1)
        self.dataViewCtrl.AppendTextColumn(u"编码缩写", 2)
        self.dataViewCtrl.AppendTextColumn(u"类别", 3)
        self.dataViewCtrl.AppendTextColumn(u"单位", 4)
        self.dataViewCtrl.AppendTextColumn(u"销售份数", 5)
        self.dataViewCtrl.AppendTextColumn(u"日均(份)", 6)
        self.dataViewCtrl.AppendTextColumn(u"销售总额", 7)
        self.dataViewCtrl.AppendTextColumn(u"退菜份数", 8)
        self.dataViewCtrl.AppendTextColumn(u"退菜总额", 9)
        sizer.Add(self.dataViewCtrl, 0, wx.EXPAND, 5)

        self.dataViewPanel.SetSizer(sizer)
        self.dataViewPanel.Layout()
        sizer.Fit(self.dataViewPanel)
        parent.Add(self.dataViewPanel, 1, wx.EXPAND, 5)

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(800, 600),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.SetBackgroundColour(wx.Colour(0x51, 0x1c, 0x0a))
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_top_control(sizer)
        self._init_data_view(sizer)
        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_SIZE, self.on_size)

        self.btnQuery.Bind(wx.EVT_BUTTON, self.on_btn_query)
        self.btnExport.Bind(wx.EVT_BUTTON, self.on_btn_export)
        self.btnExit.Bind(wx.EVT_BUTTON, self.on_btn_exit)

        # define variable
        self.model = None

    def __del__(self):
        pass

    def initialize(self):
        time_from, time_to = CtrlBillboardInfo.get_instance().get_query_time()
        if time_from is not None:
            self.dateFrom.SetValue(time_from)
        if time_to is not None:
            self.dateTo.SetValue(time_to)

        li_category = CtrlCategory.get_instance().get_data()
        for category in li_category:
            self.cbxCategory.Append(category.name, category)
        self.cbxCategory.SetSelection(0)

        # Create an instance of our model...
        self.model = ModelBillboardInfo(CtrlBillboardInfo.get_instance().get_billboard_items())
        # Tel the DVC to use the model
        self.dataViewCtrl.AssociateModel(self.model)

        # Add event listener
        EvtManager.add_listener(self, EnumEvent.EVT_BILLBOARD_INFO_REFRESH, self.on_refresh)

        x, y = CtrlHomePage.get_instance().get_screen_size()
        self.SetSize(wx.Size(x, y))

    def un_initialize(self):
        # Remove event listener
        EvtManager.remove_listener(self, EnumEvent.EVT_BILLBOARD_INFO_REFRESH, self.on_refresh)

    # Virtual event handlers, override them in your derived class
    def on_paint(self, event):
        dc = wx.ClientDC(self.topCtrlPanel)
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

        self.topCtrlPanel.SetMaxSize(wx.Size(x, 82))

        self.dataViewPanel.SetMinSize(wx.Size(x, y - 82))
        self.dataViewCtrl.SetMinSize(wx.Size(x, y - 82))

        self.Refresh()

    def on_btn_query(self, event):
        event.Skip()
        if (self.dateTo.GetValue() - self.dateFrom.GetValue()).days < 0:
            dlg = wx.MessageDialog(self, u"日期输入有误", caption=u"菜品排行榜查询")
            dlg.ShowModal()
        else:
            category = self.cbxCategory.GetClientData(self.cbxCategory.GetSelection())
            CtrlBillboardInfo.get_instance().query_billboard(self.dateFrom.GetValue(),
                                                             self.dateTo.GetValue(), category.key)

    def on_btn_export(self, event):
        event.Skip()
        dlg = wx.FileDialog(
            self, message=u"选择保存路径",
            defaultDir=os.getcwd(),
            defaultFile="",
            wildcard="excel file (*.xlsx) |*.xlsx",
            style=wx.SAVE | wx.CHANGE_DIR)

        # Show the dialog and retrieve the user response. If it is the OK response,
        # process the data.
        if dlg.ShowModal() == wx.ID_OK:
            # This returns a Python list of files that were selected.
            file_name = dlg.GetPath()
            CtrlBillboardInfo.get_instance().export_billboard(file_name)

    def on_btn_exit(self, event):
        event.Skip()
        self.Hide()
        AppManager.get_instance().switch_to_application('HomePage')

    def on_refresh(self, event):
        # Refresh data view list
        self.model.Cleared()