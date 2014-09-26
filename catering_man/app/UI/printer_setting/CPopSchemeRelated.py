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
from app.logic.dishes.CDataDishes import CDataDishesInfo
from app.logic.printer_setting.CDataPrinterScheme import CDataPrinterSchemeInfo

###########################################################################
## Class CPopSchemeRelated
###########################################################################

class CPopSchemeRelated (wx.Dialog):
    def _init_view_sizer(self, parent):
        panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(500,200), wx.STATIC_BORDER|wx.TAB_TRAVERSAL)
        # Create 3 rows and 1 column grid sizer
        gSizer = wx.GridSizer(3, 1, 0, 0)
        gSizer.SetMinSize(wx.Size(500,200)) 
        # Add row 1 sizer 
        panelTopSizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add product code 
        sTxtCode = wx.StaticText(panel, wx.ID_ANY, u"品码：", wx.DefaultPosition, wx.Size(80,-1), 0)
        sTxtCode.Wrap(-1)
        panelTopSizer.Add(sTxtCode, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        
        self.txtCode = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        panelTopSizer.Add(self.txtCode, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add product name
        sTxtName = wx.StaticText(panel, wx.ID_ANY, u"菜品名称：", wx.DefaultPosition, wx.Size(80,-1), 0)
        sTxtName.Wrap(-1)
        panelTopSizer.Add(sTxtName, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        
        self.txtName = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        panelTopSizer.Add(self.txtName, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Layout row 1 sizer
        gSizer.Add(panelTopSizer, 1, wx.EXPAND, 5)

        # Add row 2 sizer
        panelMidSizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add kitchen print 
        self.rbtnPrintOn = wx.RadioButton(panel, wx.ID_ANY, u"厨打", wx.DefaultPosition, wx.Size(100,-1), 0)
        panelMidSizer.Add(self.rbtnPrintOn, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        
        self.rbtnPrintOff = wx.RadioButton(panel, wx.ID_ANY, u"不厨打", wx.DefaultPosition, wx.Size(100,-1), 0)
        panelMidSizer.Add(self.rbtnPrintOff, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Layout row 2 sizer
        gSizer.Add(panelMidSizer, 1, wx.EXPAND, 5)

        # Add row 3 sizer
        panelBtmSizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add kitchen print scheme
        sTxtScheme = wx.StaticText(panel, wx.ID_ANY, u"厨打方案：", wx.DefaultPosition, wx.Size(80,-1), 0)
        sTxtScheme.Wrap(-1)
        panelBtmSizer.Add(sTxtScheme, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        
        cbxSchemeChoices = list()
        self.cbxScheme = wx.ComboBox(panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(110,-1), cbxSchemeChoices, 0)
        panelBtmSizer.Add(self.cbxScheme, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Layout row 3 sizer
        gSizer.Add(panelBtmSizer, 1, wx.EXPAND, 5)

        # Layout view sizer
        panel.SetSizer(gSizer)
        panel.Layout()
        parent.Add(panel, 1, wx.ALL, 5)

    def _init_ctrl_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add track number
        self.txtTrack = wx.StaticText(self, wx.ID_ANY, u"1 / 1", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txtTrack.Wrap( -1 )
        sizer.Add(self.txtTrack, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add previous record button
        self.btnPrev = wx.Button(self, wx.ID_ANY, u"上一记录", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnPrev, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add next record button
        self.btnNext = wx.Button(self, wx.ID_ANY, u"下一记录", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnNext, 0, wx.ALIGN_CENTER|wx.ALL, 5) 
        # Add spacer
        sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        # Add save button
        self.btnSave = wx.Button(self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnSave, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnExit, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        
        # Layout control sizer
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"菜品厨打设置", pos=wx.DefaultPosition, size=wx.Size(500,300), style=wx.CAPTION|wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.SetMinSize(wx.Size(500,300)) 
        self._init_view_sizer(sizer)
        self._init_ctrl_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)
        
        # Connect Events
        self.btnPrev.Bind(wx.EVT_BUTTON, self.OnBtnPrev)
        self.btnNext.Bind(wx.EVT_BUTTON, self.OnBtnNext)
        self.btnSave.Bind(wx.EVT_BUTTON, self.OnBtnSave)
        self.btnExit.Bind(wx.EVT_BUTTON, self.OnBtnExit)
        
        # Initialize
        self.index = CDataDishesInfo.GetCurItemIndex()
        self.InitailzeView()
    
    def __del__( self ):
        pass
    
    def InitailzeView(self):
        self.txtCode.Enable(False)
        self.txtName.Enable(False)
        self.rbtnPrintOn.SetValue(False)
        self.rbtnPrintOff.SetValue(True)
        if self.index < 0:
            self.index = 0
            return
        
        items = CDataDishesInfo.GetItems()
        if self.index >= len(items):
            self.index = len(items) - 1
            return
        
        data = items[self.index]
        self.txtCode.SetValue(str(data.code))
        self.txtName.SetValue(data.name)
        li_scheme = CDataPrinterSchemeInfo.GetData()
        scheme_selection = 0
        for scheme in li_scheme:
            self.cbxScheme.Append(scheme.name, scheme)
            if scheme.code == data.printer_scheme:
                self.cbxScheme.SetSelection(scheme_selection)
            scheme_selection += 1    
            
    # Virtual event handlers, overide them in your derived class
    def OnBtnPrev(self, event):
        event.Skip()
        self.index -= 1
        self.Initailze()
    
    def OnBtnNext(self, event):
        event.Skip()
        self.index += 1
        self.Initailze()
    
    def OnBtnSave(self, event):
        event.Skip()
        scheme_type = self.cbxScheme.GetClientData(self.cbxScheme.GetSelection())
        items = CDataDishesInfo.GetItems()
        if self.index >= len(items):
            self.index = len(items) - 1
            return
        
        data = items[self.index]
        data.printer_scheme = scheme_type.code
        CDataDishesInfo.UpdatePrinterScheme(data)
    
    def OnBtnExit(self, event):
        event.Skip()
        self.Close()
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    dlg = CPopSchemeRelated(None)
    dlg.Show()
    app.MainLoop()
