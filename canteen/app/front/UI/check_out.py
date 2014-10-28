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

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class WgtCheckout
###########################################################################


class WgtCheckout ( wx.Panel ):

    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition,
                            size = wx.Size( 800,600 ), style =wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        m_sizer = wx.BoxSizer( wx.VERTICAL )

        self.m_topPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,60 ), wx.TAB_TRAVERSAL )
        self.m_topPanel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.m_topPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

        m_topSizer = wx.BoxSizer( wx.HORIZONTAL )

        self.btnAllDiscount = wx.Button( self.m_topPanel, wx.ID_ANY, u"全单折", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
        m_topSizer.Add( self.btnAllDiscount, 0, 0, 5 )

        self.m_staticline14 = wx.StaticLine( self.m_topPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
        m_topSizer.Add( self.m_staticline14, 0, wx.EXPAND |wx.ALL, 5 )

        self.btnDishesDiscount = wx.Button( self.m_topPanel, wx.ID_ANY, u"菜品折", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
        m_topSizer.Add( self.btnDishesDiscount, 0, 0, 5 )

        self.m_staticline15 = wx.StaticLine( self.m_topPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
        m_topSizer.Add( self.m_staticline15, 0, wx.EXPAND |wx.ALL, 5 )

        self.btnFree = wx.Button( self.m_topPanel, wx.ID_ANY, u"免单", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
        m_topSizer.Add( self.btnFree, 0, 0, 5 )

        self.m_staticline16 = wx.StaticLine( self.m_topPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
        m_topSizer.Add( self.m_staticline16, 0, wx.EXPAND |wx.ALL, 5 )

        self.btnPrevPrint = wx.Button( self.m_topPanel, wx.ID_ANY, u"预打", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
        m_topSizer.Add( self.btnPrevPrint, 0, 0, 5 )

        self.m_staticline17 = wx.StaticLine( self.m_topPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
        m_topSizer.Add( self.m_staticline17, 0, wx.EXPAND |wx.ALL, 5 )

        self.btnCheck = wx.Button( self.m_topPanel, wx.ID_ANY, u"埋单", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
        m_topSizer.Add( self.btnCheck, 0, 0, 5 )

        self.btnExit = wx.Button( self.m_topPanel, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
        m_topSizer.Add( self.btnExit, 0, 0, 5 )


        self.m_topPanel.SetSizer( m_topSizer )
        self.m_topPanel.Layout()
        m_sizer.Add( self.m_topPanel, 1, wx.EXPAND, 5 )

        m_viewSiezr = wx.BoxSizer( wx.HORIZONTAL )

        m_leftSizer = wx.BoxSizer( wx.VERTICAL )

        self.m_dishesViewPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.STATIC_BORDER|wx.TAB_TRAVERSAL )
        self.m_dishesViewPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        self.m_dishesViewPanel.SetMinSize( wx.Size( 480,300 ) )

        m_dishesViewSizser = wx.BoxSizer( wx.VERTICAL )

        self.m_dataViewDishes = wx.dataview.DataViewListCtrl( self.m_dishesViewPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 480,300 ), 0 )
        self.m_dataViewListColumn14 = self.m_dataViewDishes.AppendTextColumn( u"行号" )
        self.m_dataViewListColumn15 = self.m_dataViewDishes.AppendTextColumn( u"菜品名称" )
        self.m_dataViewListColumn16 = self.m_dataViewDishes.AppendTextColumn( u"规格" )
        self.m_dataViewListColumn17 = self.m_dataViewDishes.AppendTextColumn( u"数量" )
        self.m_dataViewListColumn18 = self.m_dataViewDishes.AppendTextColumn( u"退菜量" )
        self.m_dataViewListColumn19 = self.m_dataViewDishes.AppendTextColumn( u"价格" )
        self.m_dataViewListColumn20 = self.m_dataViewDishes.AppendTextColumn( u"加价" )
        m_dishesViewSizser.Add( self.m_dataViewDishes, 0, wx.EXPAND, 5 )


        self.m_dishesViewPanel.SetSizer( m_dishesViewSizser )
        self.m_dishesViewPanel.Layout()
        m_dishesViewSizser.Fit( self.m_dishesViewPanel )
        m_leftSizer.Add( self.m_dishesViewPanel, 1, wx.EXPAND, 5 )

        self.m_checkViewPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 480,210 ), wx.TAB_TRAVERSAL )
        m_checkViewSizer = wx.BoxSizer( wx.VERTICAL )

        self.m_dataViewCheckout = wx.dataview.DataViewListCtrl( self.m_checkViewPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 480,210 ), 0 )
        self.m_dataViewListColumn21 = self.m_dataViewCheckout.AppendTextColumn( u"行号" )
        self.m_dataViewListColumn22 = self.m_dataViewCheckout.AppendTextColumn( u"收银方式" )
        self.m_dataViewListColumn23 = self.m_dataViewCheckout.AppendTextColumn( u"实收金额" )
        self.m_dataViewListColumn24 = self.m_dataViewCheckout.AppendTextColumn( u"付款金额" )
        m_checkViewSizer.Add( self.m_dataViewCheckout, 0, wx.EXPAND, 5 )


        self.m_checkViewPanel.SetSizer( m_checkViewSizer )
        self.m_checkViewPanel.Layout()
        m_leftSizer.Add( self.m_checkViewPanel, 1, wx.EXPAND, 5 )


        m_viewSiezr.Add( m_leftSizer, 1, wx.EXPAND, 5 )

        m_rightSizer = wx.BoxSizer( wx.VERTICAL )

        self.m_talbeInfoPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,300 ), wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
        self.m_talbeInfoPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

        m_tableInfoSizer = wx.BoxSizer( wx.VERTICAL )

        line_1_sizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText42 = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"开台单号：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText42.Wrap( -1 )
        line_1_sizer.Add( self.m_staticText42, 0, wx.ALIGN_CENTER, 5 )

        self.txtOrderNum = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"B14092100001", wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTRE )
        self.txtOrderNum.Wrap( -1 )
        line_1_sizer.Add( self.txtOrderNum, 0, wx.ALIGN_CENTER, 5 )

        self.m_staticText44 = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"餐桌：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText44.Wrap( -1 )
        line_1_sizer.Add( self.m_staticText44, 0, wx.ALIGN_CENTER, 5 )

        self.txtTableNum = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"04", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTRE )
        self.txtTableNum.Wrap( -1 )
        line_1_sizer.Add( self.txtTableNum, 0, wx.ALIGN_CENTER, 5 )


        m_tableInfoSizer.Add( line_1_sizer, 1, wx.EXPAND, 5 )

        line_2_sizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText46 = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"开台时间：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText46.Wrap( -1 )
        line_2_sizer.Add( self.m_staticText46, 0, wx.ALIGN_CENTER, 5 )

        self.txtOpenTime = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"16:35-16:45", wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTRE )
        self.txtOpenTime.Wrap( -1 )
        line_2_sizer.Add( self.txtOpenTime, 0, wx.ALIGN_CENTER, 5 )

        self.m_staticText48 = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"时长：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText48.Wrap( -1 )
        line_2_sizer.Add( self.m_staticText48, 0, wx.ALIGN_CENTER, 5 )

        self.txtTimeInterval = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"5分", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTRE )
        self.txtTimeInterval.Wrap( -1 )
        line_2_sizer.Add( self.txtTimeInterval, 0, wx.ALIGN_CENTER, 5 )


        m_tableInfoSizer.Add( line_2_sizer, 1, wx.EXPAND, 5 )

        line_3_sizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText50 = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"开台人：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText50.Wrap( -1 )
        line_3_sizer.Add( self.m_staticText50, 0, wx.ALIGN_CENTER, 5 )

        self.txtOpenPerson = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"system", wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTRE )
        self.txtOpenPerson.Wrap( -1 )
        line_3_sizer.Add( self.txtOpenPerson, 0, wx.ALIGN_CENTER, 5 )

        self.m_staticText52 = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"开台备注：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText52.Wrap( -1 )
        line_3_sizer.Add( self.m_staticText52, 0, wx.ALIGN_CENTER, 5 )

        self.txtOpenMemo = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"xxx", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTRE )
        self.txtOpenMemo.Wrap( -1 )
        line_3_sizer.Add( self.txtOpenMemo, 0, wx.ALIGN_CENTER, 5 )


        m_tableInfoSizer.Add( line_3_sizer, 1, wx.EXPAND, 5 )

        self.m_staticline4 = wx.StaticLine( self.m_talbeInfoPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        m_tableInfoSizer.Add( self.m_staticline4, 0, wx.EXPAND, 5 )

        line_4_sizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText54 = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"消费：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText54.Wrap( -1 )
        line_4_sizer.Add( self.m_staticText54, 0, wx.ALIGN_CENTER, 5 )

        self.txtAmount = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"163.00", wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTRE )
        self.txtAmount.Wrap( -1 )
        line_4_sizer.Add( self.txtAmount, 0, wx.ALIGN_CENTER, 5 )

        self.m_staticText56 = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"折扣：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText56.Wrap( -1 )
        line_4_sizer.Add( self.m_staticText56, 0, wx.ALIGN_CENTER, 5 )

        self.txtDiscount = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTRE )
        self.txtDiscount.Wrap( -1 )
        line_4_sizer.Add( self.txtDiscount, 0, wx.ALIGN_CENTER, 5 )


        m_tableInfoSizer.Add( line_4_sizer, 1, wx.EXPAND, 5 )

        line_5_sizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText58 = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"赠送：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText58.Wrap( -1 )
        line_5_sizer.Add( self.m_staticText58, 0, wx.ALIGN_CENTER, 5 )

        self.txtFree = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTRE )
        self.txtFree.Wrap( -1 )
        line_5_sizer.Add( self.txtFree, 0, wx.ALIGN_CENTER, 5 )

        self.m_staticText60 = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"服务费：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText60.Wrap( -1 )
        line_5_sizer.Add( self.m_staticText60, 0, wx.ALIGN_CENTER, 5 )

        self.txtServiceCust = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTRE )
        self.txtServiceCust.Wrap( -1 )
        line_5_sizer.Add( self.txtServiceCust, 0, wx.ALIGN_CENTER, 5 )


        m_tableInfoSizer.Add( line_5_sizer, 1, wx.EXPAND, 5 )

        line_6_sizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText62 = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"抵消差：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText62.Wrap( -1 )
        line_6_sizer.Add( self.m_staticText62, 0, wx.ALIGN_CENTER, 5 )

        self.txtSub = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTRE )
        self.txtSub.Wrap( -1 )
        line_6_sizer.Add( self.txtSub, 0, wx.ALIGN_CENTER, 5 )

        self.m_staticText64 = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"抹零：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText64.Wrap( -1 )
        line_6_sizer.Add( self.m_staticText64, 0, wx.ALIGN_CENTER, 5 )

        self.txtUpercase = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTRE )
        self.txtUpercase.Wrap( -1 )
        line_6_sizer.Add( self.txtUpercase, 0, wx.ALIGN_CENTER, 5 )


        m_tableInfoSizer.Add( line_6_sizer, 1, wx.EXPAND, 5 )

        self.m_staticline5 = wx.StaticLine( self.m_talbeInfoPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        m_tableInfoSizer.Add( self.m_staticline5, 0, wx.EXPAND, 5 )

        line_7_sizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText66 = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"应收：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText66.Wrap( -1 )
        line_7_sizer.Add( self.m_staticText66, 0, wx.ALIGN_CENTER, 5 )

        self.txtCollect = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"163.00", wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTRE )
        self.txtCollect.Wrap( -1 )
        line_7_sizer.Add( self.txtCollect, 0, wx.ALIGN_CENTER, 5 )

        self.m_staticText68 = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"免单：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText68.Wrap( -1 )
        line_7_sizer.Add( self.m_staticText68, 0, wx.ALIGN_CENTER, 5 )

        self.txtFreeOrder = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTRE )
        self.txtFreeOrder.Wrap( -1 )
        line_7_sizer.Add( self.txtFreeOrder, 0, wx.ALIGN_CENTER, 5 )


        m_tableInfoSizer.Add( line_7_sizer, 1, wx.EXPAND, 5 )

        bSizer69 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText70 = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"已收：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText70.Wrap( -1 )
        bSizer69.Add( self.m_staticText70, 0, wx.ALIGN_CENTER, 5 )

        self.txtHaveCollect = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTRE )
        self.txtHaveCollect.Wrap( -1 )
        bSizer69.Add( self.txtHaveCollect, 0, wx.ALIGN_CENTER, 5 )

        self.m_staticText72 = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"押金：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText72.Wrap( -1 )
        bSizer69.Add( self.m_staticText72, 0, wx.ALIGN_CENTER, 5 )

        self.txtYajin = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTRE )
        self.txtYajin.Wrap( -1 )
        bSizer69.Add( self.txtYajin, 0, wx.ALIGN_CENTER, 5 )


        m_tableInfoSizer.Add( bSizer69, 1, wx.EXPAND, 5 )

        bSizer70 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText74 = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"余额：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText74.Wrap( -1 )
        bSizer70.Add( self.m_staticText74, 0, wx.ALIGN_CENTER, 5 )

        self.txtYue = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTRE )
        self.txtYue.Wrap( -1 )
        bSizer70.Add( self.txtYue, 0, wx.ALIGN_CENTER, 5 )


        m_tableInfoSizer.Add( bSizer70, 1, wx.EXPAND, 5 )

        self.m_staticline6 = wx.StaticLine( self.m_talbeInfoPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        m_tableInfoSizer.Add( self.m_staticline6, 0, wx.EXPAND, 5 )

        bSizer71 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText76 = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"现金：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText76.Wrap( -1 )
        bSizer71.Add( self.m_staticText76, 0, wx.ALIGN_CENTER, 5 )

        self.txtXianjin = wx.TextCtrl( self.m_talbeInfoPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,20 ), 0 )
        bSizer71.Add( self.txtXianjin, 0, wx.ALIGN_CENTER, 5 )

        self.m_staticText77 = wx.StaticText( self.m_talbeInfoPanel, wx.ID_ANY, u"找零：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText77.Wrap( -1 )
        bSizer71.Add( self.m_staticText77, 0, wx.ALIGN_CENTER, 5 )

        self.txtZhaoling = wx.TextCtrl( self.m_talbeInfoPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,20 ), 0 )
        bSizer71.Add( self.txtZhaoling, 0, wx.ALIGN_CENTER, 5 )


        m_tableInfoSizer.Add( bSizer71, 1, wx.EXPAND, 5 )


        self.m_talbeInfoPanel.SetSizer( m_tableInfoSizer )
        self.m_talbeInfoPanel.Layout()
        m_rightSizer.Add( self.m_talbeInfoPanel, 1, wx.EXPAND, 5 )

        self.m_panel24 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,210 ), wx.STATIC_BORDER|wx.TAB_TRAVERSAL )
        self.m_panel24.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

        bSizer61 = wx.BoxSizer( wx.VERTICAL )

        bSizer72 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_textCtrl11 = wx.TextCtrl( self.m_panel24, wx.ID_ANY, u"收银方式(非现金)", wx.DefaultPosition, wx.Size( 143,-1 ), 0|wx.RAISED_BORDER )
        self.m_textCtrl11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        self.m_textCtrl11.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

        bSizer72.Add( self.m_textCtrl11, 0, wx.ALIGN_CENTER, 5 )

        self.m_textCtrl111 = wx.TextCtrl( self.m_panel24, wx.ID_ANY, u"金额  0.0", wx.DefaultPosition, wx.Size( 162,-1 ), 0|wx.RAISED_BORDER )
        self.m_textCtrl111.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        self.m_textCtrl111.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

        bSizer72.Add( self.m_textCtrl111, 0, wx.ALIGN_CENTER, 5 )


        bSizer61.Add( bSizer72, 1, wx.EXPAND, 5 )

        bSizer721 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_textCtrl112 = wx.TextCtrl( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 143,-1 ), 0|wx.RAISED_BORDER )
        self.m_textCtrl112.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        self.m_textCtrl112.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

        bSizer721.Add( self.m_textCtrl112, 0, wx.ALIGN_CENTER, 5 )

        self.m_textCtrl1111 = wx.TextCtrl( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 163,-1 ), 0|wx.RAISED_BORDER )
        self.m_textCtrl1111.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        self.m_textCtrl1111.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        bSizer721.Add( self.m_textCtrl1111, 0, wx.ALIGN_CENTER, 5 )


        bSizer61.Add( bSizer721, 1, wx.EXPAND, 5 )

        bSizer722 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_textCtrl113 = wx.TextCtrl( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 143,-1 ), 0|wx.RAISED_BORDER )
        self.m_textCtrl113.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        self.m_textCtrl113.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

        bSizer722.Add( self.m_textCtrl113, 0, wx.ALIGN_CENTER, 5 )

        self.m_textCtrl1112 = wx.TextCtrl( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 162,-1 ), 0|wx.RAISED_BORDER )
        self.m_textCtrl1112.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        self.m_textCtrl1112.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        bSizer722.Add( self.m_textCtrl1112, 0, wx.ALIGN_CENTER, 5 )


        bSizer61.Add( bSizer722, 1, wx.EXPAND, 5 )

        bSizer723 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_textCtrl114 = wx.TextCtrl( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 143,-1 ), 0|wx.RAISED_BORDER )
        self.m_textCtrl114.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        self.m_textCtrl114.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

        bSizer723.Add( self.m_textCtrl114, 0, wx.ALIGN_CENTER, 5 )

        self.m_textCtrl1113 = wx.TextCtrl( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 162,-1 ), 0|wx.RAISED_BORDER )
        self.m_textCtrl1113.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        self.m_textCtrl1113.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        bSizer723.Add( self.m_textCtrl1113, 0, wx.ALIGN_CENTER, 5 )


        bSizer61.Add( bSizer723, 1, wx.EXPAND, 5 )

        bSizer724 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_textCtrl115 = wx.TextCtrl( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 143,-1 ), 0|wx.RAISED_BORDER )
        self.m_textCtrl115.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        self.m_textCtrl115.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

        bSizer724.Add( self.m_textCtrl115, 0, wx.ALIGN_CENTER, 5 )

        self.m_textCtrl1114 = wx.TextCtrl( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 162,-1 ), 0|wx.RAISED_BORDER )
        self.m_textCtrl1114.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        self.m_textCtrl1114.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        bSizer724.Add( self.m_textCtrl1114, 0, wx.ALIGN_CENTER, 5 )


        bSizer61.Add( bSizer724, 1, wx.EXPAND, 5 )

        bSizer725 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_textCtrl116 = wx.TextCtrl( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 143,-1 ), 0|wx.RAISED_BORDER )
        self.m_textCtrl116.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        self.m_textCtrl116.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

        bSizer725.Add( self.m_textCtrl116, 0, wx.ALIGN_CENTER, 5 )

        self.m_textCtrl1115 = wx.TextCtrl( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 162,-1 ), 0|wx.RAISED_BORDER )
        self.m_textCtrl1115.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        self.m_textCtrl1115.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        bSizer725.Add( self.m_textCtrl1115, 0, wx.ALIGN_CENTER, 5 )


        bSizer61.Add( bSizer725, 1, wx.EXPAND, 5 )

        bSizer726 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_textCtrl117 = wx.TextCtrl( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 143,-1 ), 0|wx.RAISED_BORDER )
        self.m_textCtrl117.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        self.m_textCtrl117.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

        bSizer726.Add( self.m_textCtrl117, 0, wx.ALIGN_CENTER, 5 )

        self.m_textCtrl1116 = wx.TextCtrl( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 162,-1 ), 0|wx.RAISED_BORDER )
        self.m_textCtrl1116.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        self.m_textCtrl1116.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        bSizer726.Add( self.m_textCtrl1116, 0, wx.ALIGN_CENTER, 5 )


        bSizer61.Add( bSizer726, 1, wx.EXPAND, 5 )

        bSizer7261 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_textCtrl1171 = wx.TextCtrl( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 143,-1 ), 0|wx.RAISED_BORDER )
        self.m_textCtrl1171.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        self.m_textCtrl1171.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

        bSizer7261.Add( self.m_textCtrl1171, 0, wx.ALIGN_CENTER, 5 )

        self.m_textCtrl11161 = wx.TextCtrl( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 162,-1 ), 0|wx.RAISED_BORDER )
        self.m_textCtrl11161.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        self.m_textCtrl11161.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        bSizer7261.Add( self.m_textCtrl11161, 0, wx.ALIGN_CENTER, 5 )


        bSizer61.Add( bSizer7261, 1, wx.EXPAND, 5 )

        bSizer7262 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_textCtrl1172 = wx.TextCtrl( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 143,-1 ), 0|wx.RAISED_BORDER )
        self.m_textCtrl1172.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        self.m_textCtrl1172.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

        bSizer7262.Add( self.m_textCtrl1172, 0, wx.ALIGN_CENTER, 5 )

        self.m_textCtrl11162 = wx.TextCtrl( self.m_panel24, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 162,-1 ), 0|wx.RAISED_BORDER )
        self.m_textCtrl11162.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        self.m_textCtrl11162.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        bSizer7262.Add( self.m_textCtrl11162, 0, wx.ALIGN_CENTER, 5 )


        bSizer61.Add( bSizer7262, 1, wx.EXPAND, 5 )


        self.m_panel24.SetSizer( bSizer61 )
        self.m_panel24.Layout()
        m_rightSizer.Add( self.m_panel24, 1, wx.EXPAND, 5 )


        m_viewSiezr.Add( m_rightSizer, 1, wx.EXPAND, 5 )


        m_sizer.Add( m_viewSiezr, 1, wx.EXPAND, 5 )


        self.SetSizer( m_sizer )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.btnAllDiscount.Bind( wx.EVT_BUTTON, self.on_btn_alldiscount )
        self.btnDishesDiscount.Bind( wx.EVT_BUTTON, self.on_btn_dishes_discount )
        self.btnFree.Bind( wx.EVT_BUTTON, self.on_btn_free_order )
        self.btnPrevPrint.Bind( wx.EVT_BUTTON, self.on_btn_prev_print )
        self.btnCheck.Bind( wx.EVT_BUTTON, self.on_btn_checkout )
        self.btnExit.Bind( wx.EVT_BUTTON, self.on_btn_exit )

    def __del__(self):
        pass

    def initialize(self):
        # Add event listener
        #EvtManager.add_listener(self, EnumEvent.EVT_DINING_ROOM_REFRESH, self.on_btn_refresh)

        x, y = CtrlHomePage.get_screen_size()
        self.SetSize(wx.Size(x, y))

        self.GetParent().SetTitle(u"结算")

    def un_initialize(self):
        # Remove event listener
        #EvtManager.remove_listener(self, EnumEvent.EVT_DINING_ROOM_REFRESH, self.on_btn_refresh)
        pass


    # Virtual event handlers, override them in your derived class
    def on_size(self, event):
        event.Skip()
        x, y = self.GetSize()

        self.btnAllDiscount.SetMaxSize(wx.Size(60, 60))
        self.btnDishesDiscount.SetMaxSize(wx.Size(60, 60))
        self.btnFree.SetMaxSize(wx.Size(60, 60))
        self.btnPrevPrint.SetMaxSize(wx.Size(60, 60))
        self.btnCheck.SetMaxSize(wx.Size(60, 60))
        self.btnExit.SetMaxSize(wx.Size(60, 60))
        self.m_topPanel.SetMaxSize(wx.Size(x, 60))
        self.m_dishesViewPanel.SetMinSize(wx.Size(x-300, y-60-220))
        self.m_dataViewDishes.SetMinSize(wx.Size(x-300, y-60-220))
        self.m_checkViewPanel.SetMinSize(wx.Size(x-300, 210))
        self.m_dataViewCheckout.SetMinSize(wx.Size(x-300, 210))

    def on_btn_alldiscount( self, event ):
        event.Skip()

    def on_btn_dishes_discount( self, event ):
        event.Skip()

    def on_btn_free_order( self, event ):
        event.Skip()

    def on_btn_prev_print( self, event ):
        event.Skip()

    def on_btn_checkout( self, event ):
        event.Skip()

    def on_btn_exit( self, event ):
        event.Skip()
        AppManager.switch_to_application('FrontPage')


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = WgtCheckout(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()
