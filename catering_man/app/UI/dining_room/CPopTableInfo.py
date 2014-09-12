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
from app.logic.dining_room.CDataArea import CDataArea
from app.logic.dining_room.CDataArea import CDataAreaInfo
from app.logic.dining_room.CDataType import CDataType
from app.logic.dining_room.CDataType import CDataTypeInfo
from app.logic.dining_room.CDataTable import CDataTable, CDataTableInfo
from app.logic.dining_room.CDataMinexpense import CDataMinexpenseInfo

###########################################################################
## Class CPopTableInfo
###########################################################################

class CPopTableInfo ( wx.Dialog ):
    
    def __init__( self, parent, type ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"餐桌资料设置", pos = wx.DefaultPosition, size = wx.Size( 600,300 ), style = wx.CAPTION|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        m_sizer = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 600,200 ), wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
        m_gSizer = wx.GridSizer( 1, 2, 0, 0 )
        
        m_gSizer.SetMinSize( wx.Size( 600,200 ) ) 
        m_gSizerLeft = wx.GridSizer( 3, 2, 0, 0 )
        
        self.m_staticText1 = wx.StaticText( self.m_panel, wx.ID_ANY, u"餐桌编码：", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        m_gSizerLeft.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        if type == "mod":
            self.m_txtCode = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(120,-1), wx.TE_READONLY )
        else:
            self.m_txtCode = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(120,-1), 0 )
        
        m_gSizerLeft.Add( self.m_txtCode, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_staticText2 = wx.StaticText( self.m_panel, wx.ID_ANY, u"所属类型：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        m_gSizerLeft.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        m_cbxTypeChoices = []
        self.m_cbxType = wx.ComboBox( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(120,-1), m_cbxTypeChoices, 0 )
        m_gSizerLeft.Add( self.m_cbxType, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_staticText3 = wx.StaticText( self.m_panel, wx.ID_ANY, u"人数：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        m_gSizerLeft.Add( self.m_staticText3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_txtPeple = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(120,-1), 0 )
        m_gSizerLeft.Add( self.m_txtPeple, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_gSizer.Add( m_gSizerLeft, 1, wx.EXPAND, 5 )
        
        m_gSizerRight = wx.GridSizer( 3, 2, 0, 0 )
        
        self.m_staticText4 = wx.StaticText( self.m_panel, wx.ID_ANY, u"餐桌名称：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        m_gSizerRight.Add( self.m_staticText4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_txtName = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(120,-1), 0 )
        m_gSizerRight.Add( self.m_txtName, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_staticText5 = wx.StaticText( self.m_panel, wx.ID_ANY, u"所属区域：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        m_gSizerRight.Add( self.m_staticText5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        m_cbxAreaChoices = []
        self.m_cbxArea = wx.ComboBox( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(120,-1), m_cbxAreaChoices, 0 )
        m_gSizerRight.Add( self.m_cbxArea, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_staticText6 = wx.StaticText( self.m_panel, wx.ID_ANY, u"消费类型：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        m_gSizerRight.Add( self.m_staticText6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        m_cbxMinExpenseChoices = []
        self.m_cbxMinExpense = wx.ComboBox( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(120,-1), m_cbxAreaChoices, 0 )
        m_gSizerRight.Add( self.m_cbxMinExpense, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_gSizer.Add( m_gSizerRight, 1, wx.EXPAND, 5 )
        
        
        self.m_panel.SetSizer( m_gSizer )
        self.m_panel.Layout()
        m_sizer.Add( self.m_panel, 1, wx.EXPAND |wx.ALL, 5 )
        
        m_bottomSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticTxtNum = wx.StaticText( self, wx.ID_ANY, u"1 / 1 ", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTRE )
        self.m_staticTxtNum.Wrap( -1 )
        m_bottomSizer.Add( self.m_staticTxtNum, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_btnPrev = wx.Button( self, wx.ID_ANY, u"上一记录", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_bottomSizer.Add( self.m_btnPrev, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_btnNext = wx.Button( self, wx.ID_ANY, u"下一记录", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_bottomSizer.Add( self.m_btnNext, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_bottomSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_btnSave = wx.Button( self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_bottomSizer.Add( self.m_btnSave, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_btnExit = wx.Button( self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_bottomSizer.Add( self.m_btnExit, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_sizer.Add( m_bottomSizer, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( m_sizer )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_btnPrev.Bind( wx.EVT_BUTTON, self.OnBtnPrev )
        self.m_btnNext.Bind( wx.EVT_BUTTON, self.OnBtnNext )
        self.m_btnSave.Bind( wx.EVT_BUTTON, self.OnBtnSave )
        self.m_btnExit.Bind( wx.EVT_BUTTON, self.OnBtnExit )
        
        # Initailize 
        self.index = 0
        self.type = type
        self.Initailize()
    
    def __del__( self ):
        pass
    
    
    def Initailize(self):
        if self.type == "add":
            self.InitAddInfo()
        elif self.type == "mod":
            self.index = CDataTableInfo.GetCurItemIndex()
            self.InitModInfo()
        
    def InitAddInfo(self):
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
        
        self.m_staticTxtNum.Enable(False)
        self.m_btnPrev.Enable(False)
        self.m_btnNext.Enable(False)
        
    def InitModInfo(self):
        if self.index < 0:
            self.index = 0
            return
        
        items = CDataTableInfo.GetItems()
        if self.index >= len(items):
            self.index = len(items) - 1
            return
        
        data = items[self.index]
        self.m_txtCode.SetValue(str(data.code))
        self.m_txtName.SetValue(data.name)
        self.m_txtPeple.SetValue(str(data.peple_num))
        self.m_staticTxtNum.SetLabel(("%d / %d" % (self.index+1, len(items))))

        li_area = CDataAreaInfo.GetData()
        area_selection = 0
        for area in li_area:
            self.m_cbxArea.Append(area.name, area)
            if area.code == data.area:
                self.m_cbxArea.SetSelection(area_selection)
            area_selection += 1
            
        li_table_type = CDataTypeInfo.GetData()
        table_type_selection = 0
        for table_type in li_table_type:
            self.m_cbxType.Append(table_type.name, table_type)
            if table_type.code == data.table_type:
                self.m_cbxType.SetSelection(table_type_selection)
            table_type_selection += 1
        
        li_min_expense = CDataMinexpenseInfo.GetData()
        min_expense_selection = 0
        for min_expense in li_min_expense:
            self.m_cbxMinExpense.Append(min_expense.name, min_expense)
            if min_expense.code == data.min_type:
                self.m_cbxMinExpense.SetSelection(min_expense_selection)
            min_expense_selection += 1
    
    # Virtual event handlers, overide them in your derived class        
    def OnBtnPrev( self, event ):
        event.Skip()
        self.index -= 1
        self.InitModInfo()
    
    def OnBtnNext( self, event ):
        event.Skip()
        self.index += 1
        self.InitModInfo()
    
    def OnBtnSave( self, event ):
        event.Skip()
        
        area = self.m_cbxArea.GetClientData(self.m_cbxArea.GetSelection())
        type = self.m_cbxType.GetClientData(self.m_cbxType.GetSelection())
        min_expense = self.m_cbxMinExpense.GetClientData(self.m_cbxMinExpense.GetSelection())
        data = CDataTable(0, 
                          int(self.m_txtCode.GetValue()), 
                          self.m_txtName.GetValue(), 
                          type.code, 
                          area.code, 
                          int(self.m_txtPeple.GetValue()), 
                          min_expense.code)
        if self.type == "add":
            CDataTableInfo.AddItem(data)
        elif self.type == "mod":
            CDataTableInfo.UpdateItem(data)
    
    def OnBtnExit( self, event ):
        event.Skip()
        self.Close()
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    dlg = CPopTableInfo(None, "add")
    dlg.Show()
    #dlg.Center()
    app.MainLoop()

