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
from app.logic.dishes.CDataDishes import CDataDishes, CDataDishesInfo
from app.logic.printer_setting.CDataSchemeType import CDataSchemeTypeInfo

###########################################################################
## Class CPopSchemeRelated
###########################################################################

class CPopSchemeRelated ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"菜品厨打设置", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.CAPTION|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        m_sizer = wx.BoxSizer( wx.VERTICAL )
        
        m_sizer.SetMinSize( wx.Size( 500,300 ) ) 
        self.m_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,200 ), wx.STATIC_BORDER|wx.TAB_TRAVERSAL )
        m_panelGSizer = wx.GridSizer( 3, 1, 0, 0 )
        
        m_panelGSizer.SetMinSize( wx.Size( 500,200 ) ) 
        m_panelTopSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self.m_panel, wx.ID_ANY, u"品码：", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        self.m_staticText1.Wrap( -1 )
        m_panelTopSizer.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_txtCode = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        m_panelTopSizer.Add( self.m_txtCode, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_staticText2 = wx.StaticText( self.m_panel, wx.ID_ANY, u"菜品名称：", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        self.m_staticText2.Wrap( -1 )
        m_panelTopSizer.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_txtName = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        m_panelTopSizer.Add( self.m_txtName, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_panelGSizer.Add( m_panelTopSizer, 1, wx.EXPAND, 5 )
        
        m_panelMidSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_rbtnPrintOn = wx.RadioButton( self.m_panel, wx.ID_ANY, u"厨打", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
        m_panelMidSizer.Add( self.m_rbtnPrintOn, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_rbtnPrintOff = wx.RadioButton( self.m_panel, wx.ID_ANY, u"不厨打", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_rbtnPrintOff.SetMinSize( wx.Size( 100,-1 ) )
        
        m_panelMidSizer.Add( self.m_rbtnPrintOff, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_panelGSizer.Add( m_panelMidSizer, 1, wx.EXPAND, 5 )
        
        m_panelBtmSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText3 = wx.StaticText( self.m_panel, wx.ID_ANY, u"厨打方案：", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        self.m_staticText3.Wrap( -1 )
        m_panelBtmSizer.Add( self.m_staticText3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        m_cbxSchemeChoices = []
        self.m_cbxScheme = wx.ComboBox( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_cbxSchemeChoices, 0 )
        m_panelBtmSizer.Add( self.m_cbxScheme, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_panelGSizer.Add( m_panelBtmSizer, 1, wx.EXPAND, 5 )
        
        
        self.m_panel.SetSizer( m_panelGSizer )
        self.m_panel.Layout()
        m_sizer.Add( self.m_panel, 1, wx.ALL, 5 )
        
        m_ctrlSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticTxtNum = wx.StaticText( self, wx.ID_ANY, u"1 / 1", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTxtNum.Wrap( -1 )
        m_ctrlSizer.Add( self.m_staticTxtNum, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_btnPrev = wx.Button( self, wx.ID_ANY, u"上一记录", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_ctrlSizer.Add( self.m_btnPrev, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_btnNext = wx.Button( self, wx.ID_ANY, u"下一记录", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_ctrlSizer.Add( self.m_btnNext, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_ctrlSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_btnSave = wx.Button( self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_ctrlSizer.Add( self.m_btnSave, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_btnExit = wx.Button( self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_ctrlSizer.Add( self.m_btnExit, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_sizer.Add( m_ctrlSizer, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( m_sizer )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_btnPrev.Bind( wx.EVT_BUTTON, self.OnBtnPrev )
        self.m_btnNext.Bind( wx.EVT_BUTTON, self.OnBtnNext )
        self.m_btnSave.Bind( wx.EVT_BUTTON, self.OnBtnSave )
        self.m_btnExit.Bind( wx.EVT_BUTTON, self.OnBtnExit )
        
        # Initailize
        self.index = CDataDishesInfo.GetCurItemIndex()
        self.Initailze()
    
    def __del__( self ):
        pass
    
    def Initailze(self):
        self.m_txtCode.Enable(False)
        self.m_txtName.Enable(False)
        self.m_rbtnPrintOn.SetValue(False)
        self.m_rbtnPrintOff.SetValue(True)
        if self.index < 0:
            self.index = 0
            return
        
        items = CDataDishesInfo.GetItems()
        if self.index >= len(items):
            self.index = len(items) - 1
            return
        
        data = items[self.index]
        self.m_txtCode.SetValue(str(data.code))
        self.m_txtName.SetValue(data.name)
        li_scheme = CDataSchemeTypeInfo.GetData()
        scheme_selection = 0
        for scheme in li_scheme:
            self.m_cbxScheme.Append(scheme.name, scheme)
            if scheme.code == data.printer_scheme:
                self.m_cbxUnit.SetSelection(scheme_selection)
            scheme_selection += 1    
            
    # Virtual event handlers, overide them in your derived class
    def OnBtnPrev( self, event ):
        event.Skip()
        self.index -= 1
        self.Initailze()
    
    def OnBtnNext( self, event ):
        event.Skip()
        self.index += 1
        self.Initailze()
    
    def OnBtnSave( self, event ):
        event.Skip()
        scheme_type = self.m_cbxScheme.GetClientData(self.m_cbxScheme.GetSelection())
        items = CDataDishesInfo.GetItems()
        if self.index >= len(items):
            self.index = len(items) - 1
            return
        
        data = items[self.index]
        data.printer_scheme = scheme_type.code
        CDataDishesInfo.UpdatePrinterScheme(data)
    
    def OnBtnExit( self, event ):
        event.Skip()
        self.Close()
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    dlg = CPopSchemeRelated(None)
    dlg.Show()
    app.MainLoop()
