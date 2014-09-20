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
from app.logic.printer_setting.CDataPrinterScheme import CDataPrinterSchemeInfo,\
    CDataPrinterScheme
from app.logic.printer_setting.CDataSchemeType import CDataSchemeTypeInfo

###########################################################################
## Class CPopPrinterScheme
###########################################################################

class CPopPrinterScheme ( wx.Dialog ):
    
    def __init__( self, parent, type="add" ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"厨打基本方案设置", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.CAPTION )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        m_sizer = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        m_gSizer = wx.GridSizer( 2, 1, 0, 0 )
        
        m_gSizer.SetMinSize( wx.Size( 600,300 ) ) 
        self.m_topPanel = wx.Panel( self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
        m_topGSizezr = wx.GridSizer( 1, 2, 0, 0 )
        
        m_leftGSizer = wx.GridSizer( 3, 1, 0, 0 )
        
        m_codeSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self.m_topPanel, wx.ID_ANY, u"方案编号：", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        self.m_staticText1.Wrap( -1 )
        m_codeSizer.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_txtCode = wx.TextCtrl( self.m_topPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        m_codeSizer.Add( self.m_txtCode, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_ckxValid = wx.CheckBox( self.m_topPanel, wx.ID_ANY, u"生效：", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
        m_codeSizer.Add( self.m_ckxValid, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_leftGSizer.Add( m_codeSizer, 1, wx.EXPAND, 5 )
        
        m_typeSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2 = wx.StaticText( self.m_topPanel, wx.ID_ANY, u"厨打单类：", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        self.m_staticText2.Wrap( -1 )
        m_typeSizer.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        m_cbxTypeChoices = []
        self.m_cbxType = wx.ComboBox( self.m_topPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 110,-1 ), m_cbxTypeChoices, 0 )
        m_typeSizer.Add( self.m_cbxType, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_leftGSizer.Add( m_typeSizer, 1, wx.EXPAND, 5 )
        
        m_backupSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText3 = wx.StaticText( self.m_topPanel, wx.ID_ANY, u"后备方案：", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        self.m_staticText3.Wrap( -1 )
        m_backupSizer.Add( self.m_staticText3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_txtBackup = wx.TextCtrl( self.m_topPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        m_backupSizer.Add( self.m_txtBackup, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_leftGSizer.Add( m_backupSizer, 1, wx.EXPAND, 5 )
        
        
        m_topGSizezr.Add( m_leftGSizer, 1, wx.EXPAND, 5 )
        
        m_rightGSizer = wx.GridSizer( 3, 1, 0, 0 )
        
        m_nameSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText4 = wx.StaticText( self.m_topPanel, wx.ID_ANY, u"方案名称：", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        self.m_staticText4.Wrap( -1 )
        m_nameSizer.Add( self.m_staticText4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_txtName = wx.TextCtrl( self.m_topPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        m_nameSizer.Add( self.m_txtName, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_rightGSizer.Add( m_nameSizer, 1, wx.EXPAND, 5 )
        
        m_printNumSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText5 = wx.StaticText( self.m_topPanel, wx.ID_ANY, u"厨打份数：", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        self.m_staticText5.Wrap( -1 )
        m_printNumSizer.Add( self.m_staticText5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        m_cbxPrintNumChoices = []
        self.m_cbxPrintNum = wx.ComboBox( self.m_topPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 110,-1 ), m_cbxPrintNumChoices, 0 )
        m_printNumSizer.Add( self.m_cbxPrintNum, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_rightGSizer.Add( m_printNumSizer, 1, wx.EXPAND, 5 )
        
        
        m_topGSizezr.Add( m_rightGSizer, 1, wx.EXPAND, 5 )
        
        
        self.m_topPanel.SetSizer( m_topGSizezr )
        self.m_topPanel.Layout()
        m_topGSizezr.Fit( self.m_topPanel )
        m_gSizer.Add( self.m_topPanel, 1, wx.EXPAND, 5 )
        
        self.m_bottomPanel = wx.Panel( self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
        m_bottomGSizer = wx.GridSizer( 3, 1, 0, 0 )
        
        m_bottomTopSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText6 = wx.StaticText( self.m_bottomPanel, wx.ID_ANY, u"打印机：", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        self.m_staticText6.Wrap( -1 )
        m_bottomTopSizer.Add( self.m_staticText6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        m_cbxPrintDriverChoices = []
        self.m_cbxPrintDriver = wx.ComboBox( self.m_bottomPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), m_cbxPrintDriverChoices, 0 )
        m_bottomTopSizer.Add( self.m_cbxPrintDriver, 0, wx.ALL, 5 )
        
        
        m_bottomGSizer.Add( m_bottomTopSizer, 1, wx.EXPAND, 5 )
        
        
        self.m_bottomPanel.SetSizer( m_bottomGSizer )
        self.m_bottomPanel.Layout()
        m_bottomGSizer.Fit( self.m_bottomPanel )
        m_gSizer.Add( self.m_bottomPanel, 1, wx.EXPAND, 5 )
        
        
        self.m_panel.SetSizer( m_gSizer )
        self.m_panel.Layout()
        m_gSizer.Fit( self.m_panel )
        m_sizer.Add( self.m_panel, 1, wx.EXPAND |wx.ALL, 5 )
        
        m_bottomSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticTxtNum = wx.StaticText( self, wx.ID_ANY, u"1 / 1", wx.DefaultPosition, wx.DefaultSize, 0 )
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
        for index in range(4):
            self.m_cbxPrintNum.Append("%d" % (index + 1))
            
        if self.type == "add":
            self.InitAddInfo()
        elif self.type == "mod":
            self.index = CDataPrinterSchemeInfo.GetCurItemIndex()
            self.InitModInfo()
        
    def InitAddInfo(self):
        li_scheme_type = CDataSchemeTypeInfo.GetData()
        for scheme_type in li_scheme_type:
            self.m_cbxType.Append(scheme_type.name, scheme_type)
        self.m_cbxType.SetSelection(0)
        
        self.m_cbxPrintNum.SetSelection(0)
    
        self.m_staticTxtNum.Enable(False)
        self.m_btnPrev.Enable(False)
        self.m_btnNext.Enable(False)
        
    def InitModInfo(self):
        self.m_txtCode.Enable(False)
        if self.index < 0:
            self.index = 0
            return
        
        items = CDataPrinterSchemeInfo.GetItems()
        if self.index >= len(items):
            self.index = len(items) - 1
            return
        
        data = items[self.index]
        self.m_txtCode.SetValue(str(data.code))
        self.m_txtName.SetValue(data.name)
        self.m_ckxValid.SetValue(data.valid)
        self.m_txtBackup.SetValue(data.backup)
        self.m_staticTxtNum.SetLabel(("%d / %d" % (self.index+1, len(items))))

        li_scheme_type = CDataSchemeTypeInfo.GetData()
        scheme_type_selection = 0
        for scheme_type in li_scheme_type:
            self.m_cbxType.Append(scheme_type.name, scheme_type)
            if scheme_type.code == data.scheme_type:
                self.m_cbxType.SetSelection(scheme_type_selection)
            scheme_type_selection += 1
            
        self.m_cbxPrintNum.SetSelection(data.print_count - 1)
            
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
        scheme_type = self.m_cbxType.GetClientData(self.m_cbxType.GetSelection())
        print_count = int(self.m_cbxPrintNum.GetValue())
        data = CDataPrinterScheme(0, 
                          int(self.m_txtCode.GetValue()), 
                          self.m_txtName.GetValue(), 
                          self.m_ckxValid.GetValue(), 
                          scheme_type.code, 
                          print_count, 
                          self.m_txtBackup.GetValue())
        if self.type == "add":
            CDataPrinterSchemeInfo.AddItem(data)
        elif self.type == "mod":
            CDataPrinterSchemeInfo.UpdateItem(data)
    
    def OnBtnExit( self, event ):
        event.Skip()
        self.Close()
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    dlg = CPopPrinterScheme(None)
    dlg.Show()
    app.MainLoop()