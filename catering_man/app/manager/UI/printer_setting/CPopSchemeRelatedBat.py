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

class CPopSchemeRelatedBat (wx.Dialog):
    def _init_view_sizer(self, parent):
        panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(500,100), wx.STATIC_BORDER|wx.TAB_TRAVERSAL)
        # Create a 2 rows and 1 column grid sizer
        gSizer = wx.GridSizer(2, 1, 0, 0)
        gSizer.SetMinSize(wx.Size(500,100))
        # Create kitchen print sizer
        printSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.rbtnPrintOn = wx.RadioButton(panel, wx.ID_ANY, u"厨打", wx.DefaultPosition, wx.Size(100,-1), 0)
        printSizer.Add(self.rbtnPrintOn, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        
        self.rbtnPrintOff = wx.RadioButton(panel, wx.ID_ANY, u"不厨打", wx.DefaultPosition, wx.Size(100,-1), 0)
        printSizer.Add(self.rbtnPrintOff, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Layout kitchen print sizer
        gSizer.Add(printSizer, 1, wx.EXPAND, 5)

        # Create kitchen print scheme sizer
        schemeSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        sTxtScheme = wx.StaticText(panel, wx.ID_ANY, u"厨打方案：", wx.DefaultPosition, wx.Size(80,-1), 0)
        sTxtScheme.Wrap(-1)
        schemeSizer.Add(sTxtScheme, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        
        cbxSchemeNameChoices = list()
        self.cbxSchemeName = wx.ComboBox(panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(110,-1), cbxSchemeNameChoices, 0)
        schemeSizer.Add(self.cbxSchemeName, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Layout kitchen print scheme sizer
        gSizer.Add(schemeSizer, 1, wx.EXPAND, 5)

        # Layout view sizer
        panel.SetSizer(gSizer)
        panel.Layout()
        parent.Add(panel, 1, wx.ALL, 5)

    def _init_ctrl_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # Add spacer
        sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        # Add batch button
        self.btnBat = wx.Button(self, wx.ID_ANY, u"批处理", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnBat, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnExit, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        
        # Layout control sizer
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"菜品厨打批处理", pos=wx.DefaultPosition, size=wx.Size(500,200), style=wx.CAPTION)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.SetMinSize(wx.Size(500,200)) 
        self._init_view_sizer(sizer)
        self._init_ctrl_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)
        
        # Connect Events
        self.btnBat.Bind(wx.EVT_BUTTON, self.OnBtnBat)
        self.btnExit.Bind(wx.EVT_BUTTON, self.OnBtnExit)
        
        # Initialize view data
        self.list_data = CDataDishesInfo.GetCurListData()
        self.InitailzeView()
    
    def __del__( self ):
        pass    
    
    def InitailzeView(self):
        li_scheme = CDataPrinterSchemeInfo.GetData()
        for scheme in li_scheme:
            self.cbxSchemeName.Append(scheme.name, scheme) 
                
    # Virtual event handlers, override them in your derived class
    def OnBtnBat( self, event ):
        event.Skip()
        if self.list_data == None:
            return
        
        scheme_type = self.cbxSchemeName.GetClientData(self.cbxSchemeName.GetSelection())
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
