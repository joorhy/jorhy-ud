#!/usr/bin/env python
# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from app.logic.dining_room.CDataTable import CDataTable, CDataTableInfo
from app.logic.dining_room.CDataArea import CDataAreaInfo
from app.logic.dining_room.CDataType import CDataTypeInfo
from app.logic.dining_room.CDataMinexpense import CDataMinexpenseInfo

###########################################################################
## Class CPopTableBatAdd
###########################################################################

class CPopTableBatAdd ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"批量生成餐桌", pos = wx.DefaultPosition, size = wx.Size( 480,220 ), style = wx.CAPTION )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        m_sizer = wx.BoxSizer( wx.VERTICAL )
        
        m_topSizer = wx.BoxSizer( wx.VERTICAL )
        
        m_gSizer = wx.GridSizer( 1, 2, 0, 0 )
        
        m_gSizerLeft = wx.GridSizer( 4, 2, 0, 0 )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"编号前缀：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        m_gSizerLeft.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_txtCodePrev = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        m_gSizerLeft.Add( self.m_txtCodePrev, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"从：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        m_gSizerLeft.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_txtFrom = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        m_gSizerLeft.Add( self.m_txtFrom, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"区域：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        m_gSizerLeft.Add( self.m_staticText3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        m_cbxAreaChoices = []
        self.m_cbxArea = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_cbxAreaChoices, 0 )
        m_gSizerLeft.Add( self.m_cbxArea, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"消费类型：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        m_gSizerLeft.Add( self.m_staticText4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        m_cbxMinExpenseChoices = []
        self.m_cbxMinExpense = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_cbxMinExpenseChoices, 0 )
        m_gSizerLeft.Add( self.m_cbxMinExpense, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_gSizer.Add( m_gSizerLeft, 1, wx.EXPAND, 5 )
        
        m_gSizerRight = wx.GridSizer( 4, 2, 0, 0 )
        
        
        m_gSizerRight.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        m_gSizerRight.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"到：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        m_gSizerRight.Add( self.m_staticText5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_txtTo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        m_gSizerRight.Add( self.m_txtTo, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"餐桌类型：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        m_gSizerRight.Add( self.m_staticText6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        m_cbxTypeChoices = []
        self.m_cbxType = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_cbxTypeChoices, 0 )
        m_gSizerRight.Add( self.m_cbxType, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"人数：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        m_gSizerRight.Add( self.m_staticText7, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_txtPepleNum = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        m_gSizerRight.Add( self.m_txtPepleNum, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_gSizer.Add( m_gSizerRight, 1, wx.EXPAND, 5 )
        
        
        m_topSizer.Add( m_gSizer, 1, wx.EXPAND, 5 )
        
        
        m_sizer.Add( m_topSizer, 1, wx.EXPAND, 5 )
        
        m_bottomSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        
        m_bottomSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_btnCreate = wx.Button( self, wx.ID_ANY, u"生成", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_bottomSizer.Add( self.m_btnCreate, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_btnExit = wx.Button( self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_bottomSizer.Add( self.m_btnExit, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_sizer.Add( m_bottomSizer, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( m_sizer )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_btnCreate.Bind( wx.EVT_BUTTON, self.OnBtnCreate )
        self.m_btnExit.Bind( wx.EVT_BUTTON, self.OnBtnExit )
        
        # Initailze 
        self.Initailize()
    
    def __del__( self ):
        pass
    
    def Initailize(self):
        li_area = CDataAreaInfo.GetData()
        for area in li_area:
            self.m_cbxArea.Append(area.name, area)
        self.m_cbxArea.SetSelection(0)
            
        li_table_type = CDataTypeInfo.GetData()
        for table_type in li_table_type:
            self.m_cbxType.Append(table_type.name, table_type)
        self.m_cbxType.SetSelection(0)
        
        li_min_expense = CDataMinexpenseInfo.GetData()
        for min_expense in li_min_expense:
            self.m_cbxMinExpense.Append(min_expense.name, min_expense)
        self.m_cbxMinExpense.SetSelection(0)
    
    # Virtual event handlers, overide them in your derived class
    def OnBtnCreate( self, event ):
        event.Skip()
        area = self.m_cbxArea.GetClientData(self.m_cbxArea.GetSelection())
        table_type = self.m_cbxType.GetClientData(self.m_cbxType.GetSelection())
        min_expense = self.m_cbxMinExpense.GetClientData(self.m_cbxMinExpense.GetSelection())
        i_from = int(self.m_txtFrom.GetValue())
        i_to = int(self.m_txtTo.GetValue())
        i_peple_num = int(self.m_txtPepleNum.GetValue())
        table_items = list()
        for index in range(i_from, i_to + 1):
            table_items.append( CDataTable(0, 0, ("餐桌%d" % index), table_type.code, area.code, i_peple_num, min_expense.code) )
        
        CDataTableInfo.AddItems(table_items)
    
    def OnBtnExit( self, event ):
        event.Skip()
        self.Close()
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    dlg = CPopTableBatAdd(None)
    dlg.Show()
    #dlg.Center()
    app.MainLoop()

