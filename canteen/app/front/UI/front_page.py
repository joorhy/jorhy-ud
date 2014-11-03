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
from app.front.logic.model import ModelFreeTable

import wx
import wx.xrc
import wx.dataview
import time


###########################################################################
## Class PopOpenTable
###########################################################################

class PopOpenTable (wx.Dialog):
    def __init__(self, parent, table_num):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"开台操作", pos=wx.DefaultPosition,
                           size=wx.Size(600, 200), style=wx.CAPTION)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        m_sizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_dataPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        m_dataSBSizer = wx.StaticBoxSizer( wx.StaticBox( self.m_dataPanel, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

        line_1_sizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText28 = wx.StaticText( self.m_dataPanel, wx.ID_ANY, u"餐桌号：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText28.Wrap( -1 )
        line_1_sizer.Add( self.m_staticText28, 0, wx.ALL, 5 )

        self.txtTableNum = wx.TextCtrl( self.m_dataPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        line_1_sizer.Add( self.txtTableNum, 0, wx.ALL, 5 )

        self.m_staticText29 = wx.StaticText( self.m_dataPanel, wx.ID_ANY, u"餐桌名：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText29.Wrap( -1 )
        line_1_sizer.Add( self.m_staticText29, 0, wx.ALL, 5 )

        self.txtTableName = wx.TextCtrl( self.m_dataPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        line_1_sizer.Add( self.txtTableName, 0, wx.ALL, 5 )


        m_dataSBSizer.Add( line_1_sizer, 1, wx.EXPAND, 5 )

        line_2_sizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText30 = wx.StaticText( self.m_dataPanel, wx.ID_ANY, u"人数：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText30.Wrap( -1 )
        line_2_sizer.Add( self.m_staticText30, 0, wx.ALL, 5 )

        self.txtPeopleNum = wx.TextCtrl( self.m_dataPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        line_2_sizer.Add( self.txtPeopleNum, 0, wx.ALL, 5 )

        self.m_staticText31 = wx.StaticText( self.m_dataPanel, wx.ID_ANY, u"服务员：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText31.Wrap( -1 )
        line_2_sizer.Add( self.m_staticText31, 0, wx.ALL, 5 )

        cbxWaiterChoices = []
        self.cbxWaiter = wx.ComboBox( self.m_dataPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 110,-1 ), cbxWaiterChoices, 0 )
        line_2_sizer.Add( self.cbxWaiter, 0, wx.ALL, 5 )


        m_dataSBSizer.Add( line_2_sizer, 1, wx.EXPAND, 5 )

        line_3_sizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText32 = wx.StaticText( self.m_dataPanel, wx.ID_ANY, u"备注：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText32.Wrap( -1 )
        line_3_sizer.Add( self.m_staticText32, 0, wx.ALL, 5 )

        self.txtMemo = wx.TextCtrl( self.m_dataPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
        line_3_sizer.Add( self.txtMemo, 0, wx.ALL, 5 )


        m_dataSBSizer.Add( line_3_sizer, 1, wx.EXPAND, 5 )

        line_4_sizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText34 = wx.StaticText( self.m_dataPanel, wx.ID_ANY, u"开台人：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText34.Wrap( -1 )
        line_4_sizer.Add( self.m_staticText34, 0, wx.ALL, 5 )

        self.txtOprator = wx.TextCtrl( self.m_dataPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        line_4_sizer.Add( self.txtOprator, 0, wx.ALL, 5 )

        self.m_staticText35 = wx.StaticText( self.m_dataPanel, wx.ID_ANY, u"开台时间：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText35.Wrap( -1 )
        line_4_sizer.Add( self.m_staticText35, 0, wx.ALL, 5 )

        self.txtOpenTime = wx.TextCtrl( self.m_dataPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        line_4_sizer.Add( self.txtOpenTime, 0, wx.ALL, 5 )


        m_dataSBSizer.Add( line_4_sizer, 1, wx.EXPAND, 5 )


        self.m_dataPanel.SetSizer( m_dataSBSizer )
        self.m_dataPanel.Layout()
        m_dataSBSizer.Fit( self.m_dataPanel )
        m_sizer.Add( self.m_dataPanel, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_ctrlPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
        m_ctrlSizer = wx.BoxSizer( wx.VERTICAL )


        m_ctrlSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

        self.btnOpen = wx.Button( self.m_ctrlPanel, wx.ID_ANY, u"开台", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_ctrlSizer.Add( self.btnOpen, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.btnCancel = wx.Button( self.m_ctrlPanel, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_ctrlSizer.Add( self.btnCancel, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        self.m_ctrlPanel.SetSizer( m_ctrlSizer )
        self.m_ctrlPanel.Layout()
        m_ctrlSizer.Fit( self.m_ctrlPanel )
        m_sizer.Add( self.m_ctrlPanel, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( m_sizer )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.btnOpen.Bind( wx.EVT_BUTTON, self.on_btn_open )
        self.btnCancel.Bind( wx.EVT_BUTTON, self.on_btn_cancel )

        # initialize
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
            self.txtOprator.SetValue(u"system")
            self.txtOprator.Enable(False)
            self.txtOpenTime.SetValue(time.strftime('%Y/%m/%d %H:%M:%S'))
            self.txtOpenTime.Enable(False)

            waiter_items = CtrlTableInfo.get_instance().get_waiter_items()
            for item in waiter_items:
                self.cbxWaiter.Append(item.waiter_name, item)

            self.cbxWaiter.SetSelection(0)

    # Virtual event handlers, override them in your derived class
    def on_btn_open(self, event):
        event.Skip()
        table_info = DataTableItem()
        CtrlTableInfo.get_instance().open_table(self.table_num, table_info)
        self.Close()

    def on_btn_cancel(self, event):
        event.Skip()
        self.Close()

###########################################################################
## Class PopChangeTable
###########################################################################


class PopChangeTable (wx.Dialog):

    def __init__(self, parent, src_table_num):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"转台操作", pos=wx.DefaultPosition,
                           size=wx.Size(600, 400), style=wx.CAPTION)

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        m_sizer = wx.BoxSizer( wx.VERTICAL )

        self.m_topPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_topPanel.SetMaxSize( wx.Size( -1,30 ) )

        m_topSizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText78 = wx.StaticText( self.m_topPanel, wx.ID_ANY, u"可转入餐台列表：  ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText78.Wrap( -1 )
        m_topSizer.Add( self.m_staticText78, 0, wx.ALL, 5 )


        self.m_topPanel.SetSizer( m_topSizer )
        self.m_topPanel.Layout()
        m_topSizer.Fit( self.m_topPanel )
        m_sizer.Add( self.m_topPanel, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_dataViewPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.STATIC_BORDER|wx.TAB_TRAVERSAL )
        m_dataViewSizer = wx.BoxSizer( wx.VERTICAL )

        self.dataViewList = wx.dataview.DataViewListCtrl( self.m_dataViewPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 600,300 ), 0 )
        self.m_dataViewListColumn28 = self.dataViewList.AppendTextColumn( u"行号" )
        self.m_dataViewListColumn29 = self.dataViewList.AppendTextColumn( u"餐桌号" )
        self.m_dataViewListColumn30 = self.dataViewList.AppendTextColumn( u"餐桌名" )
        self.m_dataViewListColumn31 = self.dataViewList.AppendTextColumn( u"餐桌类型" )
        self.m_dataViewListColumn32 = self.dataViewList.AppendTextColumn( u"餐桌区域" )
        self.m_dataViewListColumn33 = self.dataViewList.AppendTextColumn( u"人数" )
        m_dataViewSizer.Add( self.dataViewList, 0, wx.EXPAND, 5 )


        self.m_dataViewPanel.SetSizer( m_dataViewSizer )
        self.m_dataViewPanel.Layout()
        m_dataViewSizer.Fit( self.m_dataViewPanel )
        m_sizer.Add( self.m_dataViewPanel, 1, wx.EXPAND, 5 )

        self.m_ctrlPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        m_ctrlSizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText79 = wx.StaticText( self.m_ctrlPanel, wx.ID_ANY, u"转入台号：", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText79.Wrap( -1 )
        m_ctrlSizer.Add( self.m_staticText79, 0, wx.ALIGN_CENTER, 5 )

        self.txtTableCode = wx.TextCtrl( self.m_ctrlPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        m_ctrlSizer.Add( self.txtTableCode, 0, wx.ALIGN_CENTER, 5 )


        m_ctrlSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

        self.btnOk = wx.Button( self.m_ctrlPanel, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_ctrlSizer.Add( self.btnOk, 0, wx.ALIGN_CENTER, 5 )

        self.btnCancel = wx.Button( self.m_ctrlPanel, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_ctrlSizer.Add( self.btnCancel, 0, 0, 5 )


        self.m_ctrlPanel.SetSizer( m_ctrlSizer )
        self.m_ctrlPanel.Layout()
        m_ctrlSizer.Fit( self.m_ctrlPanel )
        m_sizer.Add( self.m_ctrlPanel, 1, wx.EXPAND, 5 )


        self.SetSizer( m_sizer )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.btnOk.Bind( wx.EVT_BUTTON, self.on_btn_ok )
        self.btnCancel.Bind( wx.EVT_BUTTON, self.on_btn_cancel )

        # initialize
        # Create an instance of our model...
        self.model = ModelFreeTable(CtrlTableInfo.get_instance().get_free_tables())

        # Tell the DVC to use the model
        self.dataViewList.AssociateModel(self.model)

        self.src_table_num = src_table_num

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def on_btn_ok(self, event):
        event.Skip()
        CtrlTableInfo.get_instance().change_table(self.src_table_num, str(self.txtTableCode.GetValue()))
        self.Close()

    def on_btn_cancel(self, event):
        event.Skip()
        self.Close()

###########################################################################
## Class PopPrevPrint
###########################################################################


class PopPrevPrint ( wx.Dialog ):
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"预打账单", pos = wx.DefaultPosition, size = wx.Size( 700,480 ), style = wx.CAPTION )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        m_sizer = wx.BoxSizer( wx.VERTICAL )

        self.m_infoPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        m_infoSizer = wx.BoxSizer( wx.HORIZONTAL )

        m_leftInfoSizer = wx.BoxSizer( wx.VERTICAL )

        line_1_sizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText80 = wx.StaticText( self.m_infoPanel, wx.ID_ANY, u"开台单号：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText80.Wrap( -1 )
        line_1_sizer.Add( self.m_staticText80, 0, wx.ALIGN_CENTER, 5 )

        self.txtOrderNum = wx.TextCtrl( self.m_infoPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
        line_1_sizer.Add( self.txtOrderNum, 0, wx.ALIGN_CENTER, 5 )

        self.m_staticText81 = wx.StaticText( self.m_infoPanel, wx.ID_ANY, u"餐桌：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText81.Wrap( -1 )
        line_1_sizer.Add( self.m_staticText81, 0, wx.ALIGN_CENTER, 5 )

        self.txtTableNum = wx.TextCtrl( self.m_infoPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
        line_1_sizer.Add( self.txtTableNum, 0, wx.ALIGN_CENTER, 5 )


        m_leftInfoSizer.Add( line_1_sizer, 1, wx.EXPAND, 5 )

        line_2_sizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText82 = wx.StaticText( self.m_infoPanel, wx.ID_ANY, u"开台时间：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText82.Wrap( -1 )
        line_2_sizer.Add( self.m_staticText82, 0, wx.ALIGN_CENTER, 5 )

        self.txtOpenTime = wx.TextCtrl( self.m_infoPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
        line_2_sizer.Add( self.txtOpenTime, 0, wx.ALIGN_CENTER, 5 )


        m_leftInfoSizer.Add( line_2_sizer, 1, wx.EXPAND, 5 )

        line_3_sizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText83 = wx.StaticText( self.m_infoPanel, wx.ID_ANY, u"开台备注：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText83.Wrap( -1 )
        line_3_sizer.Add( self.m_staticText83, 0, wx.ALIGN_CENTER, 5 )

        self.m_textCtrl33 = wx.TextCtrl( self.m_infoPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
        line_3_sizer.Add( self.m_textCtrl33, 0, wx.ALIGN_CENTER, 5 )


        m_leftInfoSizer.Add( line_3_sizer, 1, wx.EXPAND, 5 )


        m_infoSizer.Add( m_leftInfoSizer, 1, wx.EXPAND, 5 )

        self.m_staticline7 = wx.StaticLine( self.m_infoPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
        m_infoSizer.Add( self.m_staticline7, 0, wx.ALL|wx.EXPAND, 5 )

        m_rightInfoSizer = wx.BoxSizer( wx.VERTICAL )

        line_4_sizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText84 = wx.StaticText( self.m_infoPanel, wx.ID_ANY, u"消费：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText84.Wrap( -1 )
        line_4_sizer.Add( self.m_staticText84, 0, wx.ALIGN_CENTER, 5 )

        self.txtXiaofei = wx.TextCtrl( self.m_infoPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 110,-1 ), 0 )
        line_4_sizer.Add( self.txtXiaofei, 0, wx.ALIGN_CENTER, 5 )

        self.m_staticText85 = wx.StaticText( self.m_infoPanel, wx.ID_ANY, u"折扣：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText85.Wrap( -1 )
        line_4_sizer.Add( self.m_staticText85, 0, wx.ALIGN_CENTER, 5 )

        self.txtZhekou = wx.TextCtrl( self.m_infoPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 110,-1 ), 0 )
        line_4_sizer.Add( self.txtZhekou, 0, wx.ALIGN_CENTER, 5 )


        m_rightInfoSizer.Add( line_4_sizer, 1, wx.EXPAND, 5 )

        line_5_sizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText86 = wx.StaticText( self.m_infoPanel, wx.ID_ANY, u"赠送：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText86.Wrap( -1 )
        line_5_sizer.Add( self.m_staticText86, 0, wx.ALIGN_CENTER, 5 )

        self.txtZengsong = wx.TextCtrl( self.m_infoPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 110,-1 ), 0 )
        line_5_sizer.Add( self.txtZengsong, 0, wx.ALIGN_CENTER, 5 )

        self.m_staticText87 = wx.StaticText( self.m_infoPanel, wx.ID_ANY, u"服务费：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText87.Wrap( -1 )
        line_5_sizer.Add( self.m_staticText87, 0, wx.ALIGN_CENTER, 5 )

        self.txtFuwufei = wx.TextCtrl( self.m_infoPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 110,-1 ), 0 )
        line_5_sizer.Add( self.txtFuwufei, 0, wx.ALIGN_CENTER, 5 )


        m_rightInfoSizer.Add( line_5_sizer, 1, wx.EXPAND, 5 )

        line_6_sizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText88 = wx.StaticText( self.m_infoPanel, wx.ID_ANY, u"应收：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText88.Wrap( -1 )
        line_6_sizer.Add( self.m_staticText88, 0, wx.ALIGN_CENTER, 5 )

        self.txtYingshou = wx.TextCtrl( self.m_infoPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 110,-1 ), 0 )
        line_6_sizer.Add( self.txtYingshou, 0, wx.ALIGN_CENTER, 5 )


        m_rightInfoSizer.Add( line_6_sizer, 1, wx.EXPAND, 5 )


        m_infoSizer.Add( m_rightInfoSizer, 1, wx.EXPAND, 5 )


        self.m_infoPanel.SetSizer( m_infoSizer )
        self.m_infoPanel.Layout()
        m_infoSizer.Fit( self.m_infoPanel )
        m_sizer.Add( self.m_infoPanel, 1, wx.EXPAND, 5 )

        self.m_staticline8 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        m_sizer.Add( self.m_staticline8, 0, wx.EXPAND, 5 )

        self.m_checkPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        m_checkSizer = wx.BoxSizer( wx.VERTICAL )

        line_7_sizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText89 = wx.StaticText( self.m_checkPanel, wx.ID_ANY, u"已收：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText89.Wrap( -1 )
        line_7_sizer.Add( self.m_staticText89, 0, wx.ALIGN_CENTER, 5 )

        self.txtYishou = wx.TextCtrl( self.m_checkPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
        line_7_sizer.Add( self.txtYishou, 0, wx.ALIGN_CENTER, 5 )

        self.m_staticText90 = wx.StaticText( self.m_checkPanel, wx.ID_ANY, u"免单：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText90.Wrap( -1 )
        line_7_sizer.Add( self.m_staticText90, 0, wx.ALIGN_CENTER, 5 )

        self.txtMiandan = wx.TextCtrl( self.m_checkPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
        line_7_sizer.Add( self.txtMiandan, 0, wx.ALIGN_CENTER, 5 )

        self.m_staticText91 = wx.StaticText( self.m_checkPanel, wx.ID_ANY, u"抹零：", wx.DefaultPosition, wx.Size( 70,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText91.Wrap( -1 )
        line_7_sizer.Add( self.m_staticText91, 0, wx.ALIGN_CENTER, 5 )

        self.txtMoling = wx.TextCtrl( self.m_checkPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 110,-1 ), 0 )
        line_7_sizer.Add( self.txtMoling, 0, wx.ALIGN_CENTER, 5 )

        self.m_staticText92 = wx.StaticText( self.m_checkPanel, wx.ID_ANY, u"押金：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText92.Wrap( -1 )
        line_7_sizer.Add( self.m_staticText92, 0, wx.ALIGN_CENTER, 5 )

        self.txtYajin = wx.TextCtrl( self.m_checkPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 110,-1 ), 0 )
        line_7_sizer.Add( self.txtYajin, 0, wx.ALIGN_CENTER, 5 )


        m_checkSizer.Add( line_7_sizer, 1, wx.EXPAND, 5 )

        line_8_sizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText93 = wx.StaticText( self.m_checkPanel, wx.ID_ANY, u"余款：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText93.Wrap( -1 )
        line_8_sizer.Add( self.m_staticText93, 0, wx.ALIGN_CENTER, 5 )

        self.txtYukuan = wx.TextCtrl( self.m_checkPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
        line_8_sizer.Add( self.txtYukuan, 0, wx.ALIGN_CENTER, 5 )


        m_checkSizer.Add( line_8_sizer, 1, wx.EXPAND, 5 )


        self.m_checkPanel.SetSizer( m_checkSizer )
        self.m_checkPanel.Layout()
        m_checkSizer.Fit( self.m_checkPanel )
        m_sizer.Add( self.m_checkPanel, 1, wx.EXPAND, 5 )

        self.m_dataViewPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.STATIC_BORDER|wx.TAB_TRAVERSAL )
        self.m_dataViewPanel.SetMinSize( wx.Size( -1,200 ) )

        m_dataViewSizer = wx.BoxSizer( wx.VERTICAL )

        self.m_dataView = wx.dataview.DataViewListCtrl( self.m_dataViewPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_dataView.SetMinSize( wx.Size( -1,200 ) )

        self.m_dataViewListColumn31 = self.m_dataView.AppendTextColumn( u"行号" )
        self.m_dataViewListColumn32 = self.m_dataView.AppendTextColumn( u"餐桌" )
        self.m_dataViewListColumn33 = self.m_dataView.AppendTextColumn( u"菜品名称" )
        self.m_dataViewListColumn34 = self.m_dataView.AppendTextColumn( u"规格" )
        self.m_dataViewListColumn35 = self.m_dataView.AppendTextColumn( u"数量" )
        self.m_dataViewListColumn36 = self.m_dataView.AppendTextColumn( u"退菜量" )
        m_dataViewSizer.Add( self.m_dataView, 0, wx.EXPAND, 5 )


        self.m_dataViewPanel.SetSizer( m_dataViewSizer )
        self.m_dataViewPanel.Layout()
        m_dataViewSizer.Fit( self.m_dataViewPanel )
        m_sizer.Add( self.m_dataViewPanel, 1, wx.EXPAND, 5 )

        self.m_ctrlPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        m_ctrlSizer = wx.BoxSizer( wx.HORIZONTAL )


        m_ctrlSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

        self.btnPrevPrint = wx.Button( self.m_ctrlPanel, wx.ID_ANY, u"预打", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_ctrlSizer.Add( self.btnPrevPrint, 0, wx.ALIGN_CENTER, 5 )

        self.btnExit = wx.Button( self.m_ctrlPanel, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_ctrlSizer.Add( self.btnExit, 0, wx.ALIGN_CENTER, 5 )


        self.m_ctrlPanel.SetSizer( m_ctrlSizer )
        self.m_ctrlPanel.Layout()
        m_ctrlSizer.Fit( self.m_ctrlPanel )
        m_sizer.Add( self.m_ctrlPanel, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( m_sizer )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.btnPrevPrint.Bind( wx.EVT_BUTTON, self.on_btn_prev_print )
        self.btnExit.Bind( wx.EVT_BUTTON, self.on_btn_exit )

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def on_btn_prev_print( self, event ):
        event.Skip()

    def on_btn_exit( self, event ):
        event.Skip()
        self.Close()

###########################################################################
## Class WgtFrontPage
###########################################################################


class WgtFrontPage (wx.Panel):
    def _init_ui(self):
        m_sizer = wx.BoxSizer(wx.VERTICAL)

        self.m_topPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition,
                                   wx.Size(-1, 60), wx.RAISED_BORDER | wx.TAB_TRAVERSAL)
        self.m_topPanel.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_topPanel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
        self.m_topPanel.SetMaxSize(wx.Size(-1, 60))

        m_topSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.btnOpenTable = wx.Button(self.m_topPanel, wx.ID_ANY, u"开台", wx.DefaultPosition, wx.Size(60, 60), 0)
        m_topSizer.Add(self.btnOpenTable, 0, 0, 5)

        self.btnOrderDishes = wx.Button( self.m_topPanel, wx.ID_ANY, u"点菜", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
        m_topSizer.Add( self.btnOrderDishes, 0, 0, 5 )

        self.btnCheck = wx.Button( self.m_topPanel, wx.ID_ANY, u"结算", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
        m_topSizer.Add( self.btnCheck, 0, 0, 5 )

        self.m_staticline9 = wx.StaticLine( self.m_topPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
        m_topSizer.Add( self.m_staticline9, 0, wx.EXPAND |wx.ALL, 5 )

        self.btnChangeTable = wx.Button( self.m_topPanel, wx.ID_ANY, u"转台", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
        m_topSizer.Add( self.btnChangeTable, 0, 0, 5 )

        self.btnPrePrint = wx.Button( self.m_topPanel, wx.ID_ANY, u"预打账单", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
        m_topSizer.Add( self.btnPrePrint, 0, 0, 5 )

        self.btnRefresh = wx.Button( self.m_topPanel, wx.ID_ANY, u"数据刷新", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
        m_topSizer.Add( self.btnRefresh, 0, 0, 5 )

        self.m_staticline10 = wx.StaticLine( self.m_topPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
        m_topSizer.Add( self.m_staticline10, 0, wx.EXPAND |wx.ALL, 5 )

        self.btnState = wx.Button( self.m_topPanel, wx.ID_ANY, u"状态", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
        m_topSizer.Add( self.btnState, 0, 0, 5 )

        self.m_staticline11 = wx.StaticLine( self.m_topPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
        m_topSizer.Add( self.m_staticline11, 0, wx.EXPAND |wx.ALL, 5 )

        self.btnExit = wx.Button( self.m_topPanel, wx.ID_ANY, u"注销", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
        m_topSizer.Add( self.btnExit, 0, 0, 5 )


        self.m_topPanel.SetSizer( m_topSizer )
        self.m_topPanel.Layout()
        m_sizer.Add( self.m_topPanel, 1, wx.EXPAND, 5 )

        m_bottomSizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_leftPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 560,520 ), wx.TAB_TRAVERSAL )
        self.m_leftPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
        m_bottomSizer.Add( self.m_leftPanel, 1, wx.EXPAND|wx.RIGHT|wx.TOP, 5 )

        self.m_rightPannel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,520 ), wx.TAB_TRAVERSAL )
        self.m_rightPannel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.m_rightPannel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

        m_rightSizer = wx.BoxSizer( wx.VERTICAL )

        m_infoSizer = wx.BoxSizer( wx.VERTICAL )

        self.m_infoPannel = wx.Panel( self.m_rightPannel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,200 ), wx.TAB_TRAVERSAL)
        m_listSizer = wx.BoxSizer( wx.VERTICAL )

        m_sizer_1 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText1 = wx.StaticText( self.m_infoPannel, wx.ID_ANY, u"餐桌号：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText1.Wrap( -1 )
        self.m_staticText1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

        m_sizer_1.Add( self.m_staticText1, 0, wx.ALIGN_CENTER, 5 )

        self.txtCode = wx.TextCtrl( self.m_infoPannel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        m_sizer_1.Add( self.txtCode, 0, wx.ALIGN_CENTER, 5 )


        m_listSizer.Add( m_sizer_1, 1, wx.EXPAND|wx.TOP, 5 )

        self.m_staticline2 = wx.StaticLine( self.m_infoPannel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        self.m_staticline2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        self.m_staticline2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        m_listSizer.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

        m_sizer_2 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText2 = wx.StaticText( self.m_infoPannel, wx.ID_ANY, u"桌号：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText2.Wrap( -1 )
        self.m_staticText2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        m_sizer_2.Add( self.m_staticText2, 0, wx.ALIGN_CENTER, 5 )

        self.txtTableNum = wx.StaticText( self.m_infoPannel, wx.ID_ANY, u"0101", wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTER )
        self.txtTableNum.Wrap( -1 )
        self.txtTableNum.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        m_sizer_2.Add( self.txtTableNum, 0, wx.ALIGN_CENTER, 5 )

        self.m_staticText4 = wx.StaticText( self.m_infoPannel, wx.ID_ANY, u"桌名：", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText4.Wrap( -1 )
        self.m_staticText4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        m_sizer_2.Add( self.m_staticText4, 0, wx.ALIGN_CENTER, 5 )

        self.txtTableName = wx.StaticText( self.m_infoPannel, wx.ID_ANY, u"01", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_CENTER )
        self.txtTableName.Wrap( -1 )
        self.txtTableName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        m_sizer_2.Add( self.txtTableName, 0, wx.ALIGN_CENTER, 5 )


        m_listSizer.Add( m_sizer_2, 1, wx.EXPAND, 5 )

        m_sizer_3 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText6 = wx.StaticText( self.m_infoPannel, wx.ID_ANY, u"桌类：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText6.Wrap( -1 )
        self.m_staticText6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        m_sizer_3.Add( self.m_staticText6, 0, wx.ALIGN_CENTER, 5 )

        self.txtType = wx.StaticText( self.m_infoPannel, wx.ID_ANY, u"餐桌", wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTER )
        self.txtType.Wrap( -1 )
        self.txtType.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        m_sizer_3.Add( self.txtType, 0, wx.ALIGN_CENTER, 5 )

        self.m_staticText8 = wx.StaticText( self.m_infoPannel, wx.ID_ANY, u"区域：", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText8.Wrap( -1 )
        self.m_staticText8.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        m_sizer_3.Add( self.m_staticText8, 0, wx.ALIGN_CENTER, 5 )

        self.txtArea = wx.StaticText( self.m_infoPannel, wx.ID_ANY, u"首层", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_CENTER )
        self.txtArea.Wrap( -1 )
        self.txtArea.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        m_sizer_3.Add( self.txtArea, 0, wx.ALIGN_CENTER, 5 )


        m_listSizer.Add( m_sizer_3, 1, wx.EXPAND, 5 )

        self.m_staticline3 = wx.StaticLine( self.m_infoPannel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        m_listSizer.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

        m_sizer_4 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText10 = wx.StaticText( self.m_infoPannel, wx.ID_ANY, u"单号：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText10.Wrap( -1 )
        self.m_staticText10.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        m_sizer_4.Add( self.m_staticText10, 0, wx.ALIGN_CENTER, 5 )

        self.txtOrderNum = wx.StaticText( self.m_infoPannel, wx.ID_ANY, u"14000001", wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTRE )
        self.txtOrderNum.Wrap( -1 )
        self.txtOrderNum.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        m_sizer_4.Add( self.txtOrderNum, 0, wx.ALIGN_CENTER, 5 )

        self.m_staticText16 = wx.StaticText( self.m_infoPannel, wx.ID_ANY, u"金额：", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText16.Wrap( -1 )
        self.m_staticText16.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        m_sizer_4.Add( self.m_staticText16, 0, wx.ALIGN_CENTER, 5 )

        self.txtPrice = wx.StaticText( self.m_infoPannel, wx.ID_ANY, u"100.00", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_CENTRE )
        self.txtPrice.Wrap( -1 )
        self.txtPrice.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        m_sizer_4.Add( self.txtPrice, 0, wx.ALIGN_CENTER, 5 )

        m_listSizer.Add( m_sizer_4, 1, wx.EXPAND, 5 )

        m_sizer_6 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText18 = wx.StaticText( self.m_infoPannel, wx.ID_ANY, u"开台时间：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText18.Wrap( -1 )
        self.m_staticText18.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        m_sizer_6.Add( self.m_staticText18, 0, wx.ALIGN_CENTER, 5 )

        self.txtOpenTime = wx.StaticText( self.m_infoPannel, wx.ID_ANY, u"8:00", wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTER)
        self.txtOpenTime.Wrap( -1 )
        self.txtOpenTime.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        m_sizer_6.Add( self.txtOpenTime, 0, wx.ALIGN_CENTER, 5 )

        self.m_staticText20 = wx.StaticText( self.m_infoPannel, wx.ID_ANY, u"押金：", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText20.Wrap( -1 )
        self.m_staticText20.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        m_sizer_6.Add( self.m_staticText20, 0, wx.ALIGN_CENTER, 5 )

        self.txtDispost = wx.StaticText( self.m_infoPannel, wx.ID_ANY, u"200.00", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_CENTER)
        self.txtDispost.Wrap( -1 )
        self.txtDispost.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        m_sizer_6.Add( self.txtDispost, 0, wx.ALIGN_CENTER, 5 )


        m_listSizer.Add( m_sizer_6, 1, wx.EXPAND, 5 )

        m_sizer_7 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText14 = wx.StaticText( self.m_infoPannel, wx.ID_ANY, u"服务员：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText14.Wrap( -1 )
        self.m_staticText14.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        m_sizer_7.Add( self.m_staticText14, 0, wx.ALIGN_CENTER, 5 )

        self.txtWaiter = wx.StaticText( self.m_infoPannel, wx.ID_ANY, u"xxx", wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTER)
        self.txtWaiter.Wrap( -1 )
        self.txtWaiter.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        m_sizer_7.Add( self.txtWaiter, 0, wx.ALIGN_CENTER, 5 )

        self.m_staticText12 = wx.StaticText( self.m_infoPannel, wx.ID_ANY, u"人数：", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText12.Wrap( -1 )
        self.m_staticText12.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        m_sizer_7.Add( self.m_staticText12, 0, wx.ALIGN_CENTER, 5 )

        self.txtPeopleNum = wx.StaticText( self.m_infoPannel, wx.ID_ANY, u"10", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_CENTER )
        self.txtPeopleNum.Wrap( -1 )
        self.txtPeopleNum.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        m_sizer_7.Add( self.txtPeopleNum, 0, wx.ALIGN_CENTER, 5 )


        m_listSizer.Add( m_sizer_7, 1, wx.EXPAND, 5 )

        m_sizer_8 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText22 = wx.StaticText( self.m_infoPannel, wx.ID_ANY, u"备注：", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText22.Wrap( -1 )
        self.m_staticText22.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        m_sizer_8.Add( self.m_staticText22, 0, wx.ALIGN_CENTER, 5 )

        self.txtMemo = wx.StaticText( self.m_infoPannel, wx.ID_ANY, u"xxxxxx", wx.DefaultPosition, wx.Size( 200,-1 ), wx.ALIGN_CENTRE )
        self.txtMemo.Wrap( -1 )
        self.txtMemo.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        m_sizer_8.Add( self.txtMemo, 0, wx.ALIGN_CENTER, 5 )


        m_listSizer.Add( m_sizer_8, 1, wx.EXPAND, 5 )


        self.m_infoPannel.SetSizer( m_listSizer )
        self.m_infoPannel.Layout()
        m_infoSizer.Add( self.m_infoPannel, 1, 0, 5 )


        m_rightSizer.Add( m_infoSizer, 1, wx.EXPAND, 5 )

        m_dishesSizer = wx.BoxSizer( wx.VERTICAL )

        self.m_dataViewListDishes = wx.dataview.DataViewListCtrl( self.m_rightPannel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,220 ), wx.RIGHT )
        self.m_dataViewListColumn1 = self.m_dataViewListDishes.AppendTextColumn( u"行号" )
        self.m_dataViewListColumn2 = self.m_dataViewListDishes.AppendTextColumn( u"品名" )
        self.m_dataViewListColumn3 = self.m_dataViewListDishes.AppendTextColumn( u"单位" )
        self.m_dataViewListColumn4 = self.m_dataViewListDishes.AppendTextColumn( u"数量" )
        self.m_dataViewListColumn5 = self.m_dataViewListDishes.AppendTextColumn( u"价格" )
        m_dishesSizer.Add( self.m_dataViewListDishes, 0, 0, 5 )


        m_rightSizer.Add( m_dishesSizer, 1, wx.EXPAND, 5 )

        m_ctrlSizer = wx.BoxSizer( wx.VERTICAL )

        self.m_ctrlPannel = wx.Panel( self.m_rightPannel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,100 ), wx.TAB_TRAVERSAL )
        m_ctrlListSizer = wx.BoxSizer( wx.VERTICAL )

        m_ctrlSizer_1 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText24 = wx.StaticText( self.m_ctrlPannel, wx.ID_ANY, u"当前消费人数：", wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText24.Wrap( -1 )
        m_ctrlSizer_1.Add( self.m_staticText24, 0, wx.ALIGN_CENTER, 5 )

        self.txtCustomer = wx.StaticText( self.m_ctrlPannel, wx.ID_ANY, u"20", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_CENTRE )
        self.txtCustomer.Wrap( -1 )
        m_ctrlSizer_1.Add( self.txtCustomer, 0, wx.ALIGN_CENTER, 5 )


        m_ctrlListSizer.Add( m_ctrlSizer_1, 1, wx.EXPAND, 5 )

        m_ctrlSizer_2 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText26 = wx.StaticText( self.m_ctrlPannel, wx.ID_ANY, u"当前消费金额：", wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText26.Wrap( -1 )
        m_ctrlSizer_2.Add( self.m_staticText26, 0, wx.ALIGN_CENTER, 5 )

        self.txtAmount = wx.StaticText( self.m_ctrlPannel, wx.ID_ANY, u"200.00", wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_CENTRE )
        self.txtAmount.Wrap( -1 )
        m_ctrlSizer_2.Add( self.txtAmount, 0, wx.ALIGN_CENTER, 5 )


        m_ctrlListSizer.Add( m_ctrlSizer_2, 1, wx.EXPAND, 5 )


        self.m_ctrlPannel.SetSizer( m_ctrlListSizer )
        self.m_ctrlPannel.Layout()
        m_ctrlSizer.Add( self.m_ctrlPannel, 1, wx.ALL, 5 )


        m_rightSizer.Add( m_ctrlSizer, 1, wx.EXPAND, 5 )


        self.m_rightPannel.SetSizer( m_rightSizer )
        self.m_rightPannel.Layout()
        m_bottomSizer.Add( self.m_rightPannel, 1, wx.TOP, 5 )

        self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        m_bottomSizer.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )


        m_sizer.Add(m_bottomSizer, 1, wx.EXPAND, 5 )

        self.SetSizer(m_sizer)
        self.Layout()

        self.Centre( wx.BOTH )

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition,
                          size=wx.Size(800, 600), style=wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self._init_ui()
        self.tableBtnMap = dict()

        # Connect Events
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.btnOpenTable.Bind(wx.EVT_BUTTON, self.on_btn_open_table)
        self.btnOrderDishes.Bind(wx.EVT_BUTTON, self.on_btn_order_dishes)
        self.btnCheck.Bind(wx.EVT_BUTTON, self.on_btn_checkout)
        self.btnChangeTable.Bind(wx.EVT_BUTTON, self.on_btn_change_table)
        self.btnPrePrint.Bind(wx.EVT_BUTTON, self.on_btn_prev_print)
        self.btnRefresh.Bind(wx.EVT_BUTTON, self.on_btn_refresh)
        self.btnState.Bind(wx.EVT_BUTTON, self.on_btn_state)
        self.btnExit.Bind(wx.EVT_BUTTON, parent.on_exit)

        # initialize
        self.selected_table_num = -1

    def __del__(self):
        pass

    def initialize(self):
        # Add event listener
        EvtManager.add_listener(self, EnumEvent.EVT_FRONT_PAGE_REFRESH, self.on_btn_refresh)

        x, y = CtrlHomePage.get_instance().get_screen_size()
        self.SetSize(wx.Size(x, y))

        self.GetParent().SetTitle(u"收银")

    def un_initialize(self):
        # Remove event listener
        EvtManager.remove_listener(self, EnumEvent.EVT_FRONT_PAGE_REFRESH, self.on_btn_refresh)
        pass

    # Virtual event handlers, override them in your derived class
    def on_size(self, event):
        event.Skip()
        x, y = self.GetSize()

        self.btnOpenTable.SetMaxSize(wx.Size(60, 60))
        self.btnOrderDishes.SetMaxSize(wx.Size(60, 60))
        self.btnCheck.SetMaxSize(wx.Size(60, 60))
        self.btnChangeTable.SetMaxSize(wx.Size(60, 60))
        self.btnPrePrint.SetMaxSize(wx.Size(60, 60))
        self.btnRefresh.SetMaxSize(wx.Size(60, 60))
        self.btnState.SetMaxSize(wx.Size(60, 60))
        self.btnExit.SetMaxSize(wx.Size(60, 60))
        self.m_topPanel.SetMaxSize(wx.Size(x, 60))
        self.m_leftPanel.SetMinSize(wx.Size(x-300, y-60))
        self.m_rightPannel.SetMinSize(wx.Size(290, y-60))
        self.m_dataViewListDishes.SetMinSize(wx.Size(290, y-340))

        self._show_table_buttons(x-300, y-60)

    def on_btn_open_table(self, event):
        event.Skip()
        if self.selected_table_num == -1:
            dlg = wx.MessageDialog(self, u"请选择餐桌", caption=u"开台")
            dlg.ShowModal()
        else:
            item = CtrlTableInfo.get_instance().get_table_item(self.selected_table_num)
            if item is not None and not item.is_open:
                pop_open_table = PopOpenTable(self, self.selected_table_num)
                pop_open_table.ShowModal()
            else:
                dlg = wx.MessageDialog(self, u"此桌已经开台", caption=u"开台")
                dlg.ShowModal()

    def on_btn_order_dishes(self, event):
        event.Skip()
        if self.selected_table_num == -1:
            dlg = wx.MessageDialog(self, u"请选择餐桌", caption=u"点菜")
            dlg.ShowModal()
        else:
            item = CtrlTableInfo.get_instance().get_table_item(self.selected_table_num)
            if item is not None and item.is_open:
                order_num = CtrlTableInfo.get_instance().order_dishes(self.selected_table_num)
                CtrlOrderInfo.get_instance().create_order(order_num)
                AppManager.get_instance().switch_to_application('OrderDishes')
            else:
                dlg = wx.MessageDialog(self, u"此桌未开台", caption=u"点菜")
                dlg.ShowModal()

    def on_btn_checkout(self, event):
        event.Skip()
        if self.selected_table_num == -1:
            dlg = wx.MessageDialog(self, u"请选择餐桌", caption=u"点菜")
            dlg.ShowModal()
        else:
            item = CtrlTableInfo.get_instance().get_table_item(self.selected_table_num)
            if item is not None and item.is_open:
                order_num = CtrlTableInfo.get_instance().order_dishes(self.selected_table_num)
                CtrlOrderInfo.get_instance().create_order(order_num)
                AppManager.get_instance().switch_to_application('CheckOut')
            else:
                dlg = wx.MessageDialog(self, u"此桌未开台", caption=u"点菜")
                dlg.ShowModal()

    def on_btn_change_table(self, event):
        event.Skip()
        if self.selected_table_num == -1:
            dlg = wx.MessageDialog(self, u"请选择餐桌", caption=u"转台")
            dlg.ShowModal()
        else:
            item = CtrlTableInfo.get_instance().get_table_item(self.selected_table_num)
            if item is not None and item.is_open:
                pop_change_table = PopChangeTable(self, item.table_num)
                pop_change_table.ShowModal()
            else:
                dlg = wx.MessageDialog(self, u"此桌未开台", caption=u"转台")
                dlg.ShowModal()

    def on_btn_prev_print(self, event):
        event.Skip()
        pop_prev_print = PopPrevPrint(self)
        pop_prev_print.ShowModal()

    def on_btn_refresh(self, event):
        event.Skip()
        self._refresh_table_info()

    def on_btn_state(self, event):
        event.Skip()

    def on_btn_table(self, event):
        event.Skip()
        self.selected_table_num = event.GetId()

    @staticmethod
    def _get_table_title(table_code, people_num, amount):
        if amount is not None:
            return table_code + '\r\n' + str(people_num) + u'人桌' + '\r\n' + u'￥ ' + str(amount)
        else:
            return table_code + '\r\n' + str(people_num) + u'人桌'

    def _show_table_buttons(self, x, y):
        column = x / 80
        row = y / 80
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
                self.tableBtnMap[win_id] = wx.Button(self.m_leftPanel, win_id,
                                                     self._get_table_title(item.table_num,
                                                                           item.people_num, item.amount),
                                                     (j*80, i*80), wx.Size(80, 80), wx.STATIC_BORDER)
                if item.is_open:
                    self.tableBtnMap[win_id].SetBackgroundColour(wx.GREEN)
                else:
                    self.tableBtnMap[win_id].SetBackgroundColour(wx.RED)

                self.Bind(wx.EVT_BUTTON, self.on_btn_table, self.tableBtnMap[win_id])

    def _refresh_table_info(self):
        x, y = self.GetSize()
        self._show_table_buttons(x-300, y-60)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = WgtFrontPage(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()

