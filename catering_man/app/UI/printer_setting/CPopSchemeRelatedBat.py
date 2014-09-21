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
from app.logic.dishes.CDataDishes import CDataDishesInfo, CDataDishes
from app.logic.printer_setting.CDataPrinterScheme import CDataPrinterSchemeInfo

###########################################################################
## Class CPopSchemeRelatedBat
###########################################################################

class CPopSchemeRelatedBat ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"菜品厨打批处理", pos = wx.DefaultPosition, size = wx.Size( 500,200 ), style = wx.CAPTION )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        m_sizer = wx.BoxSizer( wx.VERTICAL )
        
        m_sizer.SetMinSize( wx.Size( 500,200 ) ) 
        self.m_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,100 ), wx.STATIC_BORDER|wx.TAB_TRAVERSAL )
        m_panelGSizer = wx.GridSizer( 2, 1, 0, 0 )
        
        m_panelGSizer.SetMinSize( wx.Size( 500,100 ) ) 
        m_printSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_rbtnPrintOn = wx.RadioButton( self.m_panel, wx.ID_ANY, u"厨打", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
        m_printSizer.Add( self.m_rbtnPrintOn, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_rbtnPrintOff = wx.RadioButton( self.m_panel, wx.ID_ANY, u"不厨打", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_rbtnPrintOff.SetMinSize( wx.Size( 100,-1 ) )
        
        m_printSizer.Add( self.m_rbtnPrintOff, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_panelGSizer.Add( m_printSizer, 1, wx.EXPAND, 5 )
        
        m_schemeSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText = wx.StaticText( self.m_panel, wx.ID_ANY, u"厨打方案：", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        self.m_staticText.Wrap( -1 )
        m_schemeSizer.Add( self.m_staticText, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        m_cbxSchemeNameChoices = []
        self.m_cbxSchemeName = wx.ComboBox( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 110,-1 ), m_cbxSchemeNameChoices, 0 )
        m_schemeSizer.Add( self.m_cbxSchemeName, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_panelGSizer.Add( m_schemeSizer, 1, wx.EXPAND, 5 )
        
        
        self.m_panel.SetSizer( m_panelGSizer )
        self.m_panel.Layout()
        m_sizer.Add( self.m_panel, 1, wx.ALL, 5 )
        
        m_ctrlSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        
        m_ctrlSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_btnBat = wx.Button( self, wx.ID_ANY, u"批处理", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_ctrlSizer.Add( self.m_btnBat, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_btnExit = wx.Button( self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_ctrlSizer.Add( self.m_btnExit, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_sizer.Add( m_ctrlSizer, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( m_sizer )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_btnBat.Bind( wx.EVT_BUTTON, self.OnBtnBat )
        self.m_btnExit.Bind( wx.EVT_BUTTON, self.OnBtnExit )
        
        # Initailize
        self.list_data = CDataDishesInfo.GetCurListData()
        self.Initailze()
    
    def __del__( self ):
        pass    
    
    def Initailze(self):
        li_scheme = CDataPrinterSchemeInfo.GetData()
        for scheme in li_scheme:
            self.m_cbxSchemeName.Append(scheme.name, scheme) 
                
    # Virtual event handlers, overide them in your derived class
    def OnBtnBat( self, event ):
        event.Skip()
        if self.list_data == None:
            return
        
        scheme_type = self.m_cbxSchemeName.GetClientData(self.m_cbxSchemeName.GetSelection())
        for item in self.list_data:
            if isinstance(item, CDataDishes):
                item.printer_scheme = scheme_type.code
                CDataDishesInfo.UpdatePrinterScheme(item)
                
    def OnBtnExit( self, event ):
        event.Skip()
        self.Close()
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    dlg = CPopSchemeRelatedBat(None)
    dlg.Show()
    app.MainLoop()
