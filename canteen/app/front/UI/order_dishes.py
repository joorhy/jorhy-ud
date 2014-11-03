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

        self.dataViewList = wx.dataview.DataViewCtrl(self.m_dataViewPanel, wx.ID_ANY, wx.DefaultPosition,
                                                     wx.Size(400, 520), 0)
        self.m_dataViewListColumn16 = self.dataViewList.AppendTextColumn(u"行号", 0)
        self.m_dataViewListColumn17 = self.dataViewList.AppendTextColumn(u"菜品名称", 1)
        self.m_dataViewListColumn18 = self.dataViewList.AppendTextColumn(u"规格", 2)
        self.m_dataViewListColumn19 = self.dataViewList.AppendTextColumn(u"单位", 3)
        self.m_dataViewListColumn21 = self.dataViewList.AppendTextColumn(u"数量", 4)
        self.m_dataViewListColumn20 = self.dataViewList.AppendTextColumn(u"退菜量", 5)
        self.m_dataViewListColumn22 = self.dataViewList.AppendTextColumn(u"价格", 6)
        self.m_dataViewListColumn24 = self.dataViewList.AppendTextColumn(u"实际金额", 7)
        m_dataViewSizer.Add(self.dataViewList, 0, 0, 5)


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

        self.btnDishesUp = None
        self.btnDishesDown = None

        self.m_dishesListPanel.Layout()
        m_dishesSizer.Add(self.m_dishesListPanel, 1, 0, 5)

        self.m_dishesTypePanel = wx.Panel(self.m_dieshesPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size(55, 370),
                                          wx.STATIC_BORDER | wx.TAB_TRAVERSAL)

        self.btnTypeUp = None
        self.btnTypeDown = None

        self.m_dishesTypePanel.Layout()
        m_dishesSizer.Add(self.m_dishesTypePanel, 1, wx.EXPAND, 5)


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
        self.btnDeleteDishes.Bind(wx.EVT_BUTTON, self.on_btn_delete_dishes)
        self.btnSeat.Bind(wx.EVT_BUTTON, self.on_btn_seat)
        self.btnPrintOrder.Bind(wx.EVT_BUTTON, self.on_btn_print_order)
        self.btnCheck.Bind(wx.EVT_BUTTON, self.on_btn_check_order)
        self.btnPlaceOrder.Bind(wx.EVT_BUTTON, self.on_btn_place_order)
        self.btnExit.Bind(wx.EVT_BUTTON, self.on_btn_exit)
        self.btnAddNun.Bind(wx.EVT_BUTTON, self.on_btn_add_num)
        self.btnDelNum.Bind(wx.EVT_BUTTON, self.on_btn_del_num)
        self.btnModNum.Bind(wx.EVT_BUTTON, self.on_btn_mod_num)
        self.btnDemand.Bind(wx.EVT_BUTTON, self.on_btn_demand)

        self.Bind(wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.on_item_activated, self.dataViewList)
        self.Bind(wx.dataview.EVT_DATAVIEW_SELECTION_CHANGED, self.on_item_changed, self.dataViewList)

        # Create an instance of our model...
        self.model = ModelOrderedDishes(CtrlOrderInfo.get_instance().get_dishes_items())
        # Tell the DVC to use the model
        self.dataViewList.AssociateModel(self.model)

        # initialize
        self.dishes_page = 0
        self.dishesBtnMap = dict()
        self.type_page = 0
        self.typeBtnMap = dict()
        self.cur_sel_id = 0

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
        self.btnPrintOrder.SetMaxSize(wx.Size(60, 60))
        self.btnCheck.SetMaxSize(wx.Size(60, 60))
        self.btnPlaceOrder.SetMaxSize(wx.Size(60, 60))
        self.btnExit.SetMaxSize(wx.Size(60, 60))
        self.m_topPanel.SetMaxSize(wx.Size(x, 60))
        self.m_dataViewPanel.SetMinSize(wx.Size(x-400, y-60))
        self.dataViewList.SetMinSize(wx.Size(x-400, y-60))
        self.m_dieshesPanel.SetMinSize(wx.Size(380, y-240))
        self.m_dishesListPanel.SetMinSize(wx.Size(325, y-240))
        self.m_dishesTypePanel.SetMinSize(wx.Size(55, y-240))

        self._show_dishes_buttons(325, y-60-200)
        self._show_type_buttons(y-60-200)

    def on_btn_delete_dishes(self, event):
        event.Skip()
        if self.cur_sel_id > 0:
            CtrlOrderInfo.get_instance().del_dishes(self.cur_sel_id)

    def on_btn_seat(self, event):
        event.Skip()

    def on_btn_print_order(self, event):
        event.Skip()

    def on_btn_check_order(self, event):
        event.Skip()
        AppManager.get_instance().switch_to_application('CheckOut')

    def on_btn_place_order(self, event):
        event.Skip()

    def on_btn_exit(self, event):
        event.Skip()
        AppManager.get_instance().switch_to_application('FrontPage')

    def on_btn_add_num(self, event):
        event.Skip()

    def on_btn_del_num(self, event):
        event.Skip()

    def on_btn_mod_num(self, event):
        event.Skip()

    def on_btn_demand(self, event):
        event.Skip()

    def on_btn_dishes(self, event):
        event.Skip()
        CtrlOrderInfo.get_instance().add_dishes(event.GetId())

    def on_btn_dishes_up(self, event):
        event.Skip()
        if self.dishes_page > 0:
            self.dishes_page -= 1
            x, y = self.GetSize()
            self._show_dishes_buttons(320, y-60-200)

    def on_btn_dishes_down(self, event):
        event.Skip()
        self.dishes_page += 1
        x, y = self.GetSize()
        self._show_dishes_buttons(320, y-60-200)

    def on_btn_type(self, event):
        event.Skip()

    def on_type_up(self, event):
        event.Skip()
        if self.type_page > 0:
            self.type_page -= 1
            x, y = self.GetSize()
            self._show_type_buttons(y-60-200)

    def on_type_down(self, event):
        event.Skip()
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
            for i in range(0, row):
                for j in range(0, column):
                    index_ = i*column+j
                    if index_ >= len(dishes_items):
                        break
                    item = dishes_items[index_ + start_item_index]
                    win_id = int(item.dishes_code)
                    self.dishesBtnMap[win_id] = wx.Button(self.m_dishesListPanel, win_id, item.dishes_name,
                                                          (j*80, i*80), wx.Size(80, 80))
                    self.dishesBtnMap[win_id].SetBackgroundColour(wx.CYAN)

                    self.Bind(wx.EVT_BUTTON, self.on_btn_dishes, self.dishesBtnMap[win_id])
        except:
            pass

        if self.btnDishesUp is not None:
            self.btnDishesUp.Destroy()
        self.btnDishesUp = wx.Button(self.m_dishesListPanel, -1, u"上一页", (0, y-30), wx.Size(150, 30))

        if self.btnDishesDown is not None:
            self.btnDishesDown.Destroy()
        self.btnDishesDown = wx.Button(self.m_dishesListPanel, -1, u"下一页", (x-150, y-30), wx.Size(150, 30))

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
                self.typeBtnMap[win_id] = wx.Button(self.m_dishesTypePanel, win_id, item.type_name,
                                                    (0, i*50+25), wx.Size(70, 50))
                self.typeBtnMap[win_id].SetBackgroundColour(wx.YELLOW)

                self.Bind(wx.EVT_BUTTON, self.on_btn_type, self.typeBtnMap[win_id])
        except:
            pass

        if self.btnTypeUp is not None:
            self.btnTypeUp.Destroy()
        self.btnTypeUp = wx.Button(self.m_dishesTypePanel, -1, u"^", (0, 0), wx.Size(70, 30))

        if self.btnTypeDown is not None:
            self.btnTypeDown.Destroy()
        self.btnTypeDown = wx.Button(self.m_dishesTypePanel, -1, u"v", (0, y-30), wx.Size(70, 30))

        self.btnTypeUp.Bind(wx.EVT_BUTTON, self.on_type_up)
        self.btnTypeDown.Bind(wx.EVT_BUTTON, self.on_type_down)

    def on_dishes_items_refresh(self, event):
        event.Skip()
        # Refresh data view list
        result = CtrlOrderInfo.get_instance().get_dishes_items()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)

        self.model.Cleared()

    def on_item_activated(self, event):
        event.Skip()
        print self.model.GetValue(event.GetItem(), 0)

    def on_item_changed(self, event):
        event.Skip()
        self.cur_sel_id = self.model.GetValue(event.GetItem(), 0)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = WgtOrderDishes(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()
