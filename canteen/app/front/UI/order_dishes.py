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
## Class WgtOrderDishes
###########################################################################


class WgtOrderDishes ( wx.Panel ):

    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition,
                            size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        m_sizer = wx.BoxSizer( wx.VERTICAL )

        self.m_topPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,60 ), wx.TAB_TRAVERSAL )
        self.m_topPanel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.m_topPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

        m_topSizer = wx.BoxSizer( wx.HORIZONTAL )

        self.btnDeleteDishes = wx.Button( self.m_topPanel, wx.ID_ANY, u"删菜", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
        m_topSizer.Add( self.btnDeleteDishes, 0, 0, 5 )

        self.btnSeat = wx.Button( self.m_topPanel, wx.ID_ANY, u"席位", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
        m_topSizer.Add( self.btnSeat, 0, 0, 5 )

        self.m_staticline12 = wx.StaticLine( self.m_topPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
        m_topSizer.Add( self.m_staticline12, 0, wx.EXPAND |wx.ALL, 5 )

        self.btnPrintOrder = wx.Button( self.m_topPanel, wx.ID_ANY, u"打印总单", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
        m_topSizer.Add( self.btnPrintOrder, 0, 0, 5 )

        self.btnCheck = wx.Button( self.m_topPanel, wx.ID_ANY, u"结算", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
        m_topSizer.Add( self.btnCheck, 0, 0, 5 )

        self.m_staticline13 = wx.StaticLine( self.m_topPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
        m_topSizer.Add( self.m_staticline13, 0, wx.EXPAND |wx.ALL, 5 )

        self.btnPlaceOrder = wx.Button( self.m_topPanel, wx.ID_ANY, u"落单", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
        m_topSizer.Add( self.btnPlaceOrder, 0, 0, 5 )

        self.btnExit = wx.Button( self.m_topPanel, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
        m_topSizer.Add( self.btnExit, 0, 0, 5 )


        self.m_topPanel.SetSizer( m_topSizer )
        self.m_topPanel.Layout()
        m_sizer.Add( self.m_topPanel, 1, wx.EXPAND, 5 )

        m_viewSizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_dataViewPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,520 ), wx.TAB_TRAVERSAL )
        self.m_dataViewPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

        m_dataViewSizer = wx.BoxSizer( wx.VERTICAL )

        self.m_dataViewCtrl = wx.dataview.DataViewListCtrl( self.m_dataViewPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,520 ), 0 )
        self.m_dataViewListColumn16 = self.m_dataViewCtrl.AppendTextColumn( u"行号" )
        self.m_dataViewListColumn17 = self.m_dataViewCtrl.AppendTextColumn( u"菜品名称" )
        self.m_dataViewListColumn18 = self.m_dataViewCtrl.AppendTextColumn( u"规格" )
        self.m_dataViewListColumn19 = self.m_dataViewCtrl.AppendTextColumn( u"单位" )
        self.m_dataViewListColumn21 = self.m_dataViewCtrl.AppendTextColumn( u"数量" )
        self.m_dataViewListColumn20 = self.m_dataViewCtrl.AppendTextColumn( u"退菜量" )
        self.m_dataViewListColumn22 = self.m_dataViewCtrl.AppendTextColumn( u"价格" )
        self.m_dataViewListColumn24 = self.m_dataViewCtrl.AppendTextColumn( u"实际金额" )
        m_dataViewSizer.Add( self.m_dataViewCtrl, 0, 0, 5 )


        self.m_dataViewPanel.SetSizer( m_dataViewSizer )
        self.m_dataViewPanel.Layout()
        m_viewSizer.Add( self.m_dataViewPanel, 1, wx.EXPAND|wx.TOP, 5 )

        self.m_orderPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,520 ), wx.TAB_TRAVERSAL )
        self.m_orderPanel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.m_orderPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

        m_orderSizer = wx.BoxSizer( wx.VERTICAL )

        self.m_ctrlPanel = wx.Panel( self.m_orderPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 380,180 ), wx.TAB_TRAVERSAL )
        m_ctrlSizer = wx.BoxSizer( wx.VERTICAL )

        m_ctrlInfoSizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText35 = wx.StaticText( self.m_ctrlPanel, wx.ID_ANY, u"品码或拼音简码录入：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText35.Wrap( -1 )
        m_ctrlInfoSizer.Add( self.m_staticText35, 0, wx.ALIGN_CENTER, 5 )


        m_ctrlSizer.Add( m_ctrlInfoSizer, 1, wx.EXPAND, 5 )

        m_ctrlTxtSizer = wx.BoxSizer( wx.HORIZONTAL )

        self.txtCode = wx.TextCtrl( self.m_ctrlPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 380,-1 ), 0 )
        m_ctrlTxtSizer.Add( self.txtCode, 0, wx.ALIGN_CENTER, 5 )


        m_ctrlSizer.Add( m_ctrlTxtSizer, 1, wx.EXPAND, 5 )

        m_ctrlBtnSizser = wx.BoxSizer( wx.HORIZONTAL )

        self.btnAddNun = wx.Button( self.m_ctrlPanel, wx.ID_ANY, u"数量加", wx.DefaultPosition, wx.Size( 95,-1 ), 0 )
        m_ctrlBtnSizser.Add( self.btnAddNun, 0, 0, 5 )

        self.btnDelNum = wx.Button( self.m_ctrlPanel, wx.ID_ANY, u"数量减", wx.DefaultPosition, wx.Size( 95,-1 ), 0 )
        m_ctrlBtnSizser.Add( self.btnDelNum, 0, 0, 5 )

        self.btnModNum = wx.Button( self.m_ctrlPanel, wx.ID_ANY, u"数量改", wx.DefaultPosition, wx.Size( 95,-1 ), 0 )
        m_ctrlBtnSizser.Add( self.btnModNum, 0, 0, 5 )

        self.btnDemand = wx.Button( self.m_ctrlPanel, wx.ID_ANY, u"特殊做法", wx.DefaultPosition, wx.Size( 95,-1 ), 0 )
        m_ctrlBtnSizser.Add( self.btnDemand, 0, 0, 5 )


        m_ctrlSizer.Add( m_ctrlBtnSizser, 1, wx.EXPAND, 5 )

        m_tableSizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText37 = wx.StaticText( self.m_ctrlPanel, wx.ID_ANY, u"餐桌：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText37.Wrap( -1 )
        m_tableSizer.Add( self.m_staticText37, 0, wx.ALIGN_CENTER, 5 )

        self.txtTableCode = wx.StaticText( self.m_ctrlPanel, wx.ID_ANY, u"01", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.txtTableCode.Wrap( -1 )
        m_tableSizer.Add( self.txtTableCode, 0, wx.ALIGN_CENTER, 5 )


        m_ctrlSizer.Add( m_tableSizer, 1, wx.EXPAND, 5 )

        m_peopleSizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText38 = wx.StaticText( self.m_ctrlPanel, wx.ID_ANY, u"人数：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText38.Wrap( -1 )
        m_peopleSizer.Add( self.m_staticText38, 0, wx.ALIGN_CENTER, 5 )

        self.txtPeopleNum = wx.StaticText( self.m_ctrlPanel, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.txtPeopleNum.Wrap( -1 )
        m_peopleSizer.Add( self.txtPeopleNum, 0, wx.ALIGN_CENTER, 5 )

        self.m_staticText40 = wx.StaticText( self.m_ctrlPanel, wx.ID_ANY, u"备注：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText40.Wrap( -1 )
        m_peopleSizer.Add( self.m_staticText40, 0, wx.ALIGN_CENTER, 5 )

        self.txtMemo = wx.StaticText( self.m_ctrlPanel, wx.ID_ANY, u"xxxxx", wx.DefaultPosition, wx.Size( 200,-1 ), wx.ALIGN_CENTRE )
        self.txtMemo.Wrap( -1 )
        m_peopleSizer.Add( self.txtMemo, 0, wx.ALIGN_CENTER, 5 )


        m_ctrlSizer.Add( m_peopleSizer, 1, wx.EXPAND, 5 )


        self.m_ctrlPanel.SetSizer( m_ctrlSizer )
        self.m_ctrlPanel.Layout()
        m_orderSizer.Add( self.m_ctrlPanel, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_dieshesPanel = wx.Panel( self.m_orderPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 380,370 ), wx.TAB_TRAVERSAL )
        m_dishesSizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_dishesListPanel = wx.Panel( self.m_dieshesPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 322,370 ), wx.STATIC_BORDER|wx.TAB_TRAVERSAL )
        m_dishesListSizer = wx.BoxSizer( wx.VERTICAL )

        bSizer45 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer45.SetMinSize( wx.Size( 230,-1 ) )
        self.m_button50 = wx.Button( self.m_dishesListPanel, wx.ID_ANY, u"肥肠煲", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
        bSizer45.Add( self.m_button50, 0, 0, 5 )

        self.m_button51 = wx.Button( self.m_dishesListPanel, wx.ID_ANY, u"话梅扣猪手", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
        bSizer45.Add( self.m_button51, 0, 0, 5 )

        self.m_button52 = wx.Button( self.m_dishesListPanel, wx.ID_ANY, u"酷辣馋嘴蛙", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
        bSizer45.Add( self.m_button52, 0, 0, 5 )

        self.m_button501 = wx.Button( self.m_dishesListPanel, wx.ID_ANY, u"清蒸小鸡", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
        bSizer45.Add( self.m_button501, 0, 0, 5 )


        m_dishesListSizer.Add( bSizer45, 1, wx.EXPAND, 5 )
        m_dishesListSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        m_dishesListSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        m_dishesListSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        m_dishesListSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        m_dishesListSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        m_dishesListSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        m_dishesListSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        m_dishesListSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        m_dishesListSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        m_dishesListSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer50 = wx.BoxSizer( wx.HORIZONTAL )

        self.btnDishesUp = wx.Button( self.m_dishesListPanel, wx.ID_ANY, u"上一页", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.btnDishesUp.SetMinSize( wx.Size( 150,-1 ) )

        bSizer50.Add( self.btnDishesUp, 0, wx.ALIGN_BOTTOM, 5 )


        bSizer50.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

        self.btnDishesDown = wx.Button( self.m_dishesListPanel, wx.ID_ANY, u"下一页", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.btnDishesDown.SetMinSize( wx.Size( 150,-1 ) )

        bSizer50.Add( self.btnDishesDown, 0, wx.ALIGN_BOTTOM, 5 )


        m_dishesListSizer.Add( bSizer50, 1, wx.EXPAND, 5 )


        self.m_dishesListPanel.SetSizer( m_dishesListSizer )
        self.m_dishesListPanel.Layout()
        m_dishesSizer.Add( self.m_dishesListPanel, 1, 0, 5 )

        self.m_dishesTypePanel = wx.Panel( self.m_dieshesPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 55,370 ), wx.STATIC_BORDER|wx.TAB_TRAVERSAL )
        m_dishesTypeSizer = wx.BoxSizer( wx.VERTICAL )

        self.m_button43 = wx.Button( self.m_dishesTypePanel, wx.ID_ANY, u"^", wx.DefaultPosition, wx.Size( 60,25 ), 0 )
        m_dishesTypeSizer.Add( self.m_button43, 0, 0, 5 )

        self.m_button44 = wx.Button( self.m_dishesTypePanel, wx.ID_ANY, u"荤菜", wx.DefaultPosition, wx.Size( 60,50 ), 0 )
        m_dishesTypeSizer.Add( self.m_button44, 0, 0, 5 )

        self.m_button45 = wx.Button( self.m_dishesTypePanel, wx.ID_ANY, u"素菜", wx.DefaultPosition, wx.Size( 60,50 ), 0 )
        m_dishesTypeSizer.Add( self.m_button45, 0, 0, 5 )

        self.m_button46 = wx.Button( self.m_dishesTypePanel, wx.ID_ANY, u"酒水", wx.DefaultPosition, wx.Size( 60,50 ), 0 )
        m_dishesTypeSizer.Add( self.m_button46, 0, 0, 5 )

        self.m_button47 = wx.Button( self.m_dishesTypePanel, wx.ID_ANY, u"点心", wx.DefaultPosition, wx.Size( 60,50 ), 0 )
        m_dishesTypeSizer.Add( self.m_button47, 0, 0, 5 )

        self.m_button48 = wx.Button( self.m_dishesTypePanel, wx.ID_ANY, u"文本菜类", wx.DefaultPosition, wx.Size( 60,50 ), 0 )
        m_dishesTypeSizer.Add( self.m_button48, 0, 0, 5 )


        m_dishesTypeSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button49 = wx.Button( self.m_dishesTypePanel, wx.ID_ANY, u"v", wx.DefaultPosition, wx.Size( 60,25 ), 0 )
        m_dishesTypeSizer.Add( self.m_button49, 0, 0, 5 )


        self.m_dishesTypePanel.SetSizer( m_dishesTypeSizer )
        self.m_dishesTypePanel.Layout()
        m_dishesSizer.Add( self.m_dishesTypePanel, 1, wx.EXPAND, 5 )


        self.m_dieshesPanel.SetSizer( m_dishesSizer )
        self.m_dieshesPanel.Layout()
        m_orderSizer.Add( self.m_dieshesPanel, 1, wx.EXPAND, 5 )


        self.m_orderPanel.SetSizer( m_orderSizer )
        self.m_orderPanel.Layout()
        m_viewSizer.Add( self.m_orderPanel, 1, wx.EXPAND|wx.LEFT|wx.TOP, 5 )


        m_sizer.Add( m_viewSizer, 1, wx.EXPAND, 5 )


        self.SetSizer( m_sizer )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.btnDeleteDishes.Bind( wx.EVT_BUTTON, self.on_btn_delete_dishes )
        self.btnSeat.Bind( wx.EVT_BUTTON, self.on_btn_seat )
        self.btnPrintOrder.Bind( wx.EVT_BUTTON, self.on_btn_print_order )
        self.btnCheck.Bind( wx.EVT_BUTTON, self.on_btn_check_order )
        self.btnPlaceOrder.Bind( wx.EVT_BUTTON, self.on_btn_place_order )
        self.btnExit.Bind( wx.EVT_BUTTON, self.on_btn_exit )
        self.btnAddNun.Bind( wx.EVT_BUTTON, self.on_btn_add_num )
        self.btnDelNum.Bind( wx.EVT_BUTTON, self.on_btn_del_num )
        self.btnModNum.Bind( wx.EVT_BUTTON, self.on_btn_mod_num )
        self.btnDemand.Bind( wx.EVT_BUTTON, self.on_btn_demand )
        self.m_button501.Bind( wx.EVT_BUTTON, self.on_btn_dishes )
        self.btnDishesUp.Bind( wx.EVT_BUTTON, self.on_btn_dishes_up )
        self.btnDishesDown.Bind( wx.EVT_BUTTON, self.on_btn_dishes_down )
        self.m_button43.Bind( wx.EVT_BUTTON, self.on_type_up )
        self.m_button44.Bind( wx.EVT_BUTTON, self.on_btn_type )
        self.m_button49.Bind( wx.EVT_BUTTON, self.on_type_down )

    def __del__(self):
        pass

    def initialize(self):
        # Add event listener
        #EvtManager.add_listener(self, EnumEvent.EVT_DINING_ROOM_REFRESH, self.on_btn_refresh)

        x, y = CtrlHomePage.get_screen_size()
        self.SetSize(wx.Size(x, y))

        self.GetParent().SetTitle(u"点菜")

    def un_initialize(self):
        # Remove event listener
        #EvtManager.remove_listener(self, EnumEvent.EVT_DINING_ROOM_REFRESH, self.on_btn_refresh)
        pass

    # Virtual event handlers, override them in your derived class
    def on_size(self, event):
        event.Skip()
        x, y = self.GetSize()

        self.btnDeleteDishes.SetMaxSize(wx.Size(60, 60))
        self.btnSeat.SetMaxSize(wx.Size(60, 60))
        self.btnPrintOrder.SetMaxSize(wx.Size(60, 60))
        self.btnCheck.SetMaxSize(wx.Size(60, 60))
        self.btnPlaceOrder.SetMaxSize(wx.Size(60, 60))
        self.btnExit.SetMaxSize(wx.Size(60, 60))
        self.m_topPanel.SetMaxSize(wx.Size(x, 60))
        self.m_dataViewPanel.SetMinSize(wx.Size(x-400, y-60))
        self.m_dataViewCtrl.SetMinSize(wx.Size(x-400, y-60))
        self.m_dieshesPanel.SetMinSize(wx.Size(380, y-180))
        self.m_dishesListPanel.SetMinSize(wx.Size(322, y-180))

    def on_btn_delete_dishes( self, event ):
        event.Skip()

    def on_btn_seat( self, event ):
        event.Skip()

    def on_btn_print_order( self, event ):
        event.Skip()

    def on_btn_check_order( self, event ):
        event.Skip()
        AppManager.switch_to_application('CheckOut')

    def on_btn_place_order( self, event ):
        event.Skip()

    def on_btn_exit( self, event ):
        event.Skip()
        AppManager.switch_to_application('FrontPage')

    def on_btn_add_num( self, event ):
        event.Skip()

    def on_btn_del_num( self, event ):
        event.Skip()

    def on_btn_mod_num( self, event ):
        event.Skip()

    def on_btn_demand( self, event ):
        event.Skip()

    def on_btn_dishes( self, event ):
        event.Skip()

    def on_btn_dishes_up( self, event ):
        event.Skip()

    def on_btn_dishes_down( self, event ):
        event.Skip()

    def on_type_up( self, event ):
        event.Skip()

    def on_btn_type( self, event ):
        event.Skip()

    def on_type_down( self, event ):
        event.Skip()


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = WgtOrderDishes(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()
