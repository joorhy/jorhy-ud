#!/usr/bin/env python
# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
from app.manager.logic.data import * 
from app.manager.logic.ctrl import * 
from app.manager.logic.model import *
from app.manager.AppManager import AppManager

import wx
import wx.xrc
import wx.dataview
from wx.dataview import DataViewColumn

###########################################################################
## Class CPopPrinterScheme
###########################################################################

class PopPrinterScheme(wx.Dialog):
    def _init_view_sizer(self, parent):
        panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        # Create a tow rows and 1 column grid sizer for scheme and printer
        gSizer = wx.GridSizer(2, 1, 0, 0)
        gSizer.SetMinSize(wx.Size(600,300))
        
        # Create scheme panel
        topPanel = wx.Panel(panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL)
        topGSizer = wx.GridSizer(1, 2, 0, 0)
        # Add column 1 of scheme
        self._init_scheme_colume_1_sizer(topPanel, topGSizer)
        # Add column 2 of scheme
        self._init_scheme_colume_2_sizer(topPanel, topGSizer)
        # Layout scheme panel
        topPanel.SetSizer(topGSizer)
        topPanel.Layout()
        topGSizer.Fit(topPanel)
        gSizer.Add(topPanel, 1, wx.EXPAND, 5)
        
        # Create printer panel
        bottomPanel = wx.Panel(panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL)
        bottomGSizer = wx.GridSizer(3, 1, 0, 0)
        # Add printer driver sizer
        self._init_priner_row_1_sizer(bottomPanel, bottomGSizer)
        # Layout printer panel
        bottomPanel.SetSizer(bottomGSizer)
        bottomPanel.Layout()
        bottomGSizer.Fit(bottomPanel)
        gSizer.Add(bottomPanel, 1, wx.EXPAND, 5)
        
        # Layout view sizer
        panel.SetSizer(gSizer)
        panel.Layout()
        gSizer.Fit(panel)
        parent.Add(panel, 1, wx.EXPAND |wx.ALL, 5)
        
    def _init_scheme_colume_1_sizer(self, container, parent):
        gSizer = wx.GridSizer(3, 1, 0, 0)
        # Add scheme number sizer
        codeSizer = wx.BoxSizer(wx.HORIZONTAL)
        sTxtCode = wx.StaticText(container, wx.ID_ANY, u"方案编号：", wx.DefaultPosition, wx.Size(80,-1), 0)
        sTxtCode.Wrap(-1)
        codeSizer.Add(sTxtCode, 0, wx.ALIGN_CENTER|wx.ALL, 5)

        self.txtCode = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        codeSizer.Add(self.txtCode, 0, wx.ALIGN_CENTER|wx.ALL, 5)

        self.ckxValid = wx.CheckBox(container, wx.ID_ANY, u"生效：", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT)
        codeSizer.Add(self.ckxValid, 0, wx.ALIGN_CENTER|wx.ALL, 5)

        gSizer.Add(codeSizer, 1, wx.EXPAND, 5)
        # Add invoice type sizer
        typeSizer = wx.BoxSizer(wx.HORIZONTAL)
        sTxtInvoice = wx.StaticText(container, wx.ID_ANY, u"厨打单类：", wx.DefaultPosition, wx.Size(80,-1), 0)
        sTxtInvoice.Wrap(-1)
        typeSizer.Add(sTxtInvoice, 0, wx.ALIGN_CENTER|wx.ALL, 5)

        cbxTypeChoices = list()
        self.cbxType = wx.ComboBox(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(110,-1), cbxTypeChoices, 0)
        typeSizer.Add(self.cbxType, 0, wx.ALIGN_CENTER|wx.ALL, 5)

        gSizer.Add(typeSizer, 1, wx.EXPAND, 5)
        # Add reserve scheme sizer
        backupSizer = wx.BoxSizer(wx.HORIZONTAL)
        sTxtReserve = wx.StaticText(container, wx.ID_ANY, u"后备方案：", wx.DefaultPosition, wx.Size(80,-1), 0)
        sTxtReserve.Wrap(-1)
        backupSizer.Add(sTxtReserve, 0, wx.ALIGN_CENTER|wx.ALL, 5)

        self.txtBackup = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        backupSizer.Add(self.txtBackup, 0, wx.ALIGN_CENTER|wx.ALL, 5)

        gSizer.Add(backupSizer, 1, wx.EXPAND, 5)
        
        # Layout column 1 of scheme
        parent.Add(gSizer, 1, wx.EXPAND, 5)

    def _init_scheme_colume_2_sizer(self, container, parent):
        gSizer = wx.GridSizer(3, 1, 0, 0)
        # Add scheme name sizer
        nameSizer = wx.BoxSizer(wx.HORIZONTAL)
        sTxtName = wx.StaticText(container, wx.ID_ANY, u"方案名称：", wx.DefaultPosition, wx.Size(80,-1), 0)
        sTxtName.Wrap(-1)
        nameSizer.Add(sTxtName, 0, wx.ALIGN_CENTER|wx.ALL, 5)

        self.txtName = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        nameSizer.Add(self.txtName, 0, wx.ALIGN_CENTER|wx.ALL, 5)

        gSizer.Add(nameSizer, 1, wx.EXPAND, 5)
        # Add print number sizer
        printNumSizer = wx.BoxSizer(wx.HORIZONTAL)
        sTxtNum = wx.StaticText(container, wx.ID_ANY, u"厨打份数：", wx.DefaultPosition, wx.Size(80,-1), 0)
        sTxtNum.Wrap(-1)
        printNumSizer.Add(sTxtNum, 0, wx.ALIGN_CENTER|wx.ALL, 5)

        cbxPrintNumChoices = list()
        self.cbxPrintNum = wx.ComboBox(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(110,-1), cbxPrintNumChoices, 0)
        printNumSizer.Add(self.cbxPrintNum, 0, wx.ALIGN_CENTER|wx.ALL, 5)

        gSizer.Add(printNumSizer, 1, wx.EXPAND, 5)
        
        # Layout column 2 of scheme
        parent.Add(gSizer, 1, wx.EXPAND, 5)
        
    def _init_priner_row_1_sizer(self, container, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add printer driver label
        sTxtDriver = wx.StaticText(container, wx.ID_ANY, u"打印机：", wx.DefaultPosition, wx.Size(80,-1), 0)
        sTxtDriver.Wrap(-1)
        sizer.Add(sTxtDriver, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        # Add printer driver combo box 
        cbxPrintDriverChoices = list()
        self.cbxPrintDriver = wx.ComboBox(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400,-1), cbxPrintDriverChoices, 0)
        sizer.Add(self.cbxPrintDriver, 0, wx.ALL, 5)
        # Layout printer driver 
        parent.Add(sizer, 1, wx.EXPAND, 5)
        
    def _init_ctrl_sizer(self, parent):
        sizer = wx.BoxSizer( wx.HORIZONTAL )

        # Add track number
        self.txtTrack = wx.StaticText(self, wx.ID_ANY, u"1 / 1", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txtTrack.Wrap(-1)
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
        
    def __init__(self, parent, type_="add"):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"厨打基本方案设置", pos=wx.DefaultPosition, size=wx.Size(600,400), style=wx.CAPTION)
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        sizer = wx.BoxSizer(wx.VERTICAL)
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
        self.index = 0
        self.type = type_
        self.InitializeView()

    def __del__( self ):
        pass

    def InitializeView(self):
        for index in range(4):
            self.cbxPrintNum.Append("%d" % (index + 1))

        if self.type == "add":
            self.InitAddView()
        elif self.type == "mod":
            self.index = CtrlPrinterScheme.GetCurItemIndex()
            self.InitModView()

    def InitAddView(self):
        li_scheme_type = CtrlSchemeType.GetData()
        for scheme_type in li_scheme_type:
            self.cbxType.Append(scheme_type.name, scheme_type)
        self.cbxType.SetSelection(0)

        self.cbxPrintNum.SetSelection(0)

        self.txtTrack.Enable(False)
        self.btnPrev.Enable(False)
        self.btnNext.Enable(False)

    def InitModView(self):
        self.txtCode.Enable(False)
        if self.index < 0:
            self.index = 0
            return

        items = CtrlPrinterScheme.GetItems()
        if self.index >= len(items):
            self.index = len(items) - 1
            return

        data = items[self.index]
        self.txtCode.SetValue(str(data.code))
        self.txtName.SetValue(data.name)
        self.ckxValid.SetValue(data.valid)
        self.txtBackup.SetValue(data.backup)
        self.staticTxtNum.SetLabel(("%d / %d" % (self.index+1, len(items))))

        li_scheme_type = CtrlSchemeType.GetData()
        scheme_type_selection = 0
        for scheme_type in li_scheme_type:
            self.cbxType.Append(scheme_type.name, scheme_type)
            if scheme_type.code == data.scheme_type:
                self.cbxType.SetSelection(scheme_type_selection)
            scheme_type_selection += 1

        self.cbxPrintNum.SetSelection(data.print_count - 1)

    # Virtual event handlers, override them in your derived class
    def OnBtnPrev(self, event):
        event.Skip()
        self.index -= 1
        self.InitModInfo()

    def OnBtnNext(self, event):
        event.Skip()
        self.index += 1
        self.InitModView()

    def OnBtnSave(self, event):
        event.Skip()
        scheme_type = self.cbxType.GetClientData(self.cbxType.GetSelection())
        print_count = int(self.cbxPrintNum.GetValue())
        data = DataPrinterScheme(0, 
                            int(self.txtCode.GetValue()), 
                            self.txtName.GetValue(), 
                            self.ckxValid.GetValue(), 
                            scheme_type.code, 
                            print_count, 
                            self.txtBackup.GetValue())
        if self.type == "add":
            CtrlPrinterScheme.AddItem(data)
        elif self.type == "mod":
            CtrlPrinterScheme.UpdateItem(data)

    def OnBtnExit(self, event):
        event.Skip()
        self.Close()

###########################################################################
## Class CPopSchemeRelated
###########################################################################

class PopSchemeRelated (wx.Dialog):
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
        self.index = CtrlDishes.GetCurItemIndex()
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
        
        items = CtrlDishes.GetItems()
        if self.index >= len(items):
            self.index = len(items) - 1
            return
        
        data = items[self.index]
        self.txtCode.SetValue(str(data.code))
        self.txtName.SetValue(data.name)
        li_scheme = CtrlPrinterScheme.GetData()
        scheme_selection = 0
        for scheme in li_scheme:
            self.cbxScheme.Append(scheme.name, scheme)
            if scheme.code == data.printer_scheme:
                self.cbxScheme.SetSelection(scheme_selection)
            scheme_selection += 1    
            
    # Virtual event handlers, override them in your derived class
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
        items = CtrlDishes.GetItems()
        if self.index >= len(items):
            self.index = len(items) - 1
            return
        
        data = items[self.index]
        data.printer_scheme = scheme_type.code
        CtrlDishes.UpdatePrinterScheme(data)
    
    def OnBtnExit(self, event):
        event.Skip()
        self.Close()

###########################################################################
## Class PopSchemeRelatedBat
###########################################################################

class PopSchemeRelatedBat (wx.Dialog):
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
        self.list_data = CtrlDishes.GetCurListData()
        self.InitailzeView()
    
    def __del__( self ):
        pass    
    
    def InitailzeView(self):
        li_scheme = CtrlPrinterScheme.GetData()
        for scheme in li_scheme:
            self.cbxSchemeName.Append(scheme.name, scheme) 
                
    # Virtual event handlers, override them in your derived class
    def OnBtnBat( self, event ):
        event.Skip()
        if self.list_data == None:
            return
        
        scheme_type = self.cbxSchemeName.GetClientData(self.cbxSchemeName.GetSelection())
        for item in self.list_data:
            if isinstance(item, DataDishes):
                item.printer_scheme = scheme_type.code
                CtrlDishes.UpdatePrinterScheme(item)
                
    def OnBtnExit( self, event ):
        event.Skip()
        self.Close()
        
###########################################################################
## Class PopSchemeType
###########################################################################

class PopSchemeType (wx.Dialog):
    def _init_view_sizer(self, parent):
        sizer = wx.BoxSizer(wx.VERTICAL)
        # Create data view list
        self.dataViewList = wx.dataview.DataViewCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.dataViewList.SetMinSize(wx.Size(600,300))
        # Add items into data view list
        self.dataViewList.AppendTextColumn(u"行号", 0) 
        self.dataViewList.AppendTextColumn(u"编码", 1, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE) 
        self.dataViewList.AppendTextColumn(u"单类名称", 2, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE) 
        sizer.Add(self.dataViewList, 0, wx.ALL|wx.EXPAND, 5)
        
        # Layout view sizer
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_ctrl_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add new button
        self.btnNew = wx.Button(self, wx.ID_ANY, u"新增", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnNew, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        # Add delete button
        self.btnDelete = wx.Button(self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnDelete, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        # Add spacer
        sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        # Add refresh button
        self.btnRefresh = wx.Button(self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnRefresh, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        # Add save button
        self.btnSave = wx.Button(self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnSave, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnExit, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        
        # Layout control sizer 
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"厨打单类型", pos=wx.DefaultPosition, size=wx.Size(600,400), style=wx.CAPTION|wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.Size(-1,-1), wx.Size(-1,-1))
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_view_sizer(sizer)
        self._init_ctrl_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Create an instance of our model...
        self.model = ModelSchemeType(CtrlSchemeType.GetData())
        
        # Tell the DVC to use the model
        self.dataViewList.AssociateModel(self.model)

        # Connect Events
        self.btnNew.Bind(wx.EVT_BUTTON, self.OnBtnNew)
        self.btnDelete.Bind(wx.EVT_BUTTON, self.OnBtnDelete)
        self.btnRefresh.Bind(wx.EVT_BUTTON, self.OnBtnRefresh)
        self.btnSave.Bind(wx.EVT_BUTTON, self.OnBtnSave)
        self.btnExit.Bind(wx.EVT_BUTTON, self.OnBtnExit)
    
    def __del__(self):
        pass
    
    
    # Virtual event handlers, override them in your derived class
    def OnBtnNew(self, event):
        event.Skip()
        CtrlSchemeType.AddItem(DataSchemeType(0, 0, ""))
        
        data = DataSchemeType(CtrlSchemeType.GetDataLen() + 1, CtrlSchemeType.GetId(), "")
        self.model.data.append(data)
        item = self.model.ObjectToItem(data)
        self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
    
    def OnBtnDelete(self, event):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        self.model.data.remove(data)
        self.dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
        CtrlSchemeType.DeleteItem(data)
    
    def OnBtnRefresh(self, event):
        event.Skip()
        result = CtrlSchemeType.GetData()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
                    
        self.model.Cleared()
    
    def OnBtnSave(self, event):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        CtrlSchemeType.UpdateItem(data)
    
    def OnBtnExit(self, event):
        event.Skip()
        self.Close()

###########################################################################
## Class WgtPrinterScheme
###########################################################################

class WgtPrinterScheme(wx.Panel):
    def _init_status_bar_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.SetMinSize(wx.Size(-1,50)) 
        # Add new button
        self.btnNew = wx.Button(self, wx.ID_ANY, u"新增", wx.DefaultPosition, wx.Size(50,50), 0)
        sizer.Add(self.btnNew, 0, 0, 5)
        # Add modify button
        self.btnModify = wx.Button(self, wx.ID_ANY, u"修改", wx.DefaultPosition, wx.Size(50,50), 0)
        sizer.Add(self.btnModify, 0, 0, 5)
        # Add delete button
        self.btnDelete = wx.Button(self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.Size(50,50), 0)
        sizer.Add(self.btnDelete, 0, 0, 5)
        # Add invoice type button
        self.btnSchemeType = wx.Button(self, wx.ID_ANY, u"单类", wx.DefaultPosition, wx.Size(50,50), 0)
        sizer.Add(self.btnSchemeType, 0, 0, 5)
        # Add refresh button
        self.btnRefresh = wx.Button(self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.Size(50,50), 0)
        sizer.Add(self.btnRefresh, 0, 0, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.Size(50,50), 0)
        sizer.Add(self.btnExit, 0, 0, 5)
        # Add fix space panel
        self.topPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL)
        self.topPanel.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
        self.topPanel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
        self.topPanel.SetMaxSize(wx.Size(-1,50))
        sizer.Add(self.topPanel, 1, wx.EXPAND, 5)
        
        # Layout status bar sizer
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_data_view_sizer(self, parent):
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.SetMinSize(wx.Size(800,600)) 
        # Create data view list
        self.dataViewList = wx.dataview.DataViewCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(800,600), 0)
        # Add items into data view list 
        self.dataViewList.AppendTextColumn(u"行号", 0) 
        self.dataViewList.AppendTextColumn(u"编号", 1) 
        self.dataViewList.AppendTextColumn(u"方案名称", 2) 
        self.dataViewList.AppendToggleColumn(u"生效", 3, width=50) 
        self.dataViewList.AppendTextColumn(u"单据类型", 4) 
        self.dataViewList.AppendTextColumn(u"厨打分数", 5) 
        self.dataViewList.AppendTextColumn(u"后备方案", 6)  
        sizer.Add(self.dataViewList, 0, 0, 5)
        
        # Layout data view list
        parent.Add(sizer, 1, 0, 5)

    def __init__( self, parent ):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(800,600), style=wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.Size(-1,-1), wx.DefaultSize)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_status_bar_sizer(sizer)
        self._init_data_view_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Create an instance of our model...
        self.model = ModelPrinterScheme(CtrlPrinterScheme.GetData())
        CtrlPrinterScheme.RefreshItems()
        
        # Tell the DVC to use the model
        self.dataViewList.AssociateModel(self.model)

        # Connect Events
        self.Bind( wx.EVT_SIZE, self.OnSize )
        
        self.btnNew.Bind(wx.EVT_BUTTON, self.OnBtnNew)
        self.btnModify.Bind(wx.EVT_BUTTON, self.OnBtnModify)
        self.btnDelete.Bind(wx.EVT_BUTTON, self.OnBtnDelete)
        self.btnSchemeType.Bind(wx.EVT_BUTTON, self.OnBtnSchemetype)
        self.btnRefresh.Bind(wx.EVT_BUTTON, self.OnBtnRefresh)
        self.btnExit.Bind(wx.EVT_BUTTON, self.OnBtnExit)
    
    def __del__( self ):
        pass
    
    def Initailize(self):
        # Add event listener
        EvtManager.AddListener(self, EnumEvent.EVT_PRINTER_SCHEME_REFRESH, self.OnBtnRefresh)
        
        x, y = CtrlHomePage.GetFrameSize()       
        self.SetSize(wx.Size(x, y))

    def Uninitailize(self):
        # Add event listener
        EvtManager.RemoveListener(self, EnumEvent.EVT_PRINTER_SCHEME_REFRESH, self.OnBtnRefresh)
    
    def RefreshUI(self):        
        # Refresh data view list
        CtrlPrinterScheme.RefreshItems()
        result = CtrlPrinterScheme.GetData()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
                    
        self.model.Cleared()
    
    # Virtual event handlers, override them in your derived class
    def OnSize( self, event ):
        event.Skip()
        x, y = self.GetSize()

        self.btnNew.SetMaxSize(wx.Size(50,50))
        self.btnModify.SetMaxSize(wx.Size(50,50))
        self.btnDelete.SetMaxSize(wx.Size(50,50))
        self.btnSchemeType.SetMaxSize(wx.Size(50,50))
        self.btnRefresh.SetMaxSize(wx.Size(50,50))
        self.btnExit.SetMaxSize(wx.Size(50,50))
        self.topPanel.SetMaxSize(wx.Size(x-300,50)) 
        self.dataViewList.SetMinSize(wx.Size(x,y-50))
        
    def OnBtnNew(self, event):
        event.Skip()
        self.popPrinterScheme = PopPrinterScheme(self, "add")
        self.popPrinterScheme.ShowModal()
    
    def OnBtnModify(self, event):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        index = self.model.data.index(data)
        CtrlPrinterScheme.SetCurItemIndex(index)
        self.popPrinterScheme = PopPrinterScheme(self, "mod")
        self.popPrinterScheme.ShowModal()
    
    def OnBtnDelete( self, event ):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        self.model.data.remove(data)
        self.dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
        CtrlPrinterScheme.DeleteItem(data)
        
    def OnBtnSchemetype( self, event ):
        event.Skip()  
        self.popSchemeType = PopSchemeType(self)
        self.popSchemeType.ShowModal()  
    
    def OnBtnRefresh( self, event ):
        event.Skip()
        self.RefreshUI()
    
    def OnBtnExit( self, event ):
        event.Skip()
        AppManager.SwitchToApplication('HomePage')
        
###########################################################################
## Class WgtSchemeRelated
###########################################################################

class WgtSchemeRelated (wx.Panel):
    def _init_status_bar_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.SetMinSize(wx.Size(800,50))
        # Add kitchen print setting button
        self.btnSetting = wx.Button(self, wx.ID_ANY, u"厨打设置", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnSetting, 0, wx.EXPAND, 5)
        # Add batch kitchen print setting button
        self.btnBatSetting = wx.Button(self, wx.ID_ANY, u"批处理", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnBatSetting.SetMinSize(wx.Size(100,50)) 
        sizer.Add(self.btnBatSetting, 0, 0, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnExit.SetMinSize(wx.Size(50,50))
        sizer.Add(self.btnExit, 0, 0, 5)
        # Add fix space panel
        self.topPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.topPanel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
        sizer.Add(self.topPanel, 1, wx.EXPAND, 5)
        
        # Layout status bar sizer
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_data_view_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.SetMinSize(wx.Size(800,550)) 
        # Add tree control
        leftSizer = wx.BoxSizer(wx.VERTICAL)
        leftSizer.SetMinSize(wx.Size(200,550)) 
        self.treeCtrl = wx.TreeCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE)        
        leftSizer.Add(self.treeCtrl, 0, wx.EXPAND, 5)
        sizer.Add(leftSizer, 1, 0, 5)
        # Add data view list
        rightSizer = wx.BoxSizer(wx.VERTICAL) 
        rightSizer.SetMinSize(wx.Size(600,550)) 
        self.dataViewList = wx.dataview.DataViewCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.dataViewList.SetMinSize(wx.Size(-1,600))
        # Add items into data view list
        self.dataViewList.AppendTextColumn(u"行号", 0) 
        self.dataViewList.AppendTextColumn(u"品码", 1) 
        self.dataViewList.AppendTextColumn(u"品名", 2) 
        self.dataViewList.AppendTextColumn(u"厨打方式", 10) 
        rightSizer.Add(self.dataViewList, 0, wx.EXPAND|wx.LEFT, 5)

        sizer.Add(rightSizer, 1, 0, 5)
        # Layout data view list
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(800,600), style=wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_status_bar_sizer(sizer)
        self._init_data_view_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre( wx.BOTH )

        # Create an instance of our model...
        self.model = ModelDishes(CtrlDishes.GetData())
        CtrlDishes.RefreshItems()
        
        # Tell the DVC to use the model
        self.dataViewList.AssociateModel(self.model)

        # Connect Events
        self.Bind( wx.EVT_SIZE, self.OnSize )
        
        self.btnSetting.Bind(wx.EVT_BUTTON, self.OnBntSetting)
        self.btnBatSetting.Bind(wx.EVT_BUTTON, self.OnBntBatSetting)
        self.btnExit.Bind(wx.EVT_BUTTON, self.OnExit)
        
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged, self.treeCtrl)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.OnActivate, self.treeCtrl)
        
        # Show tree control
        self.tree_data = None
        self.ShowTreeCtrl()
    
    def __del__( self ):
        pass
    
    def Initailize(self):
        # Add event listener
        EvtManager.AddListener(self, EnumEvent.EVT_DISHES_PUBLISH_REFRESH, self.OnRefresh)
        
        x, y = CtrlHomePage.GetFrameSize()       
        self.SetSize(wx.Size(x, y))

    def Uninitailize(self):
        # Add event listener
        EvtManager.RemoveListener(self, EnumEvent.EVT_DISHES_PUBLISH_REFRESH, self.OnRefresh)
    
    def ShowTreeCtrl(self):
        isz = (16,16)
        il = wx.ImageList(isz[0], isz[1])
        fldridx     = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER,      wx.ART_OTHER, isz))
        fldropenidx = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER_OPEN, wx.ART_OTHER, isz))
        fileidx     = il.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, isz))
        
        self.treeCtrl.SetImageList(il)
        self.il = il

        self.root = self.treeCtrl.AddRoot(u"全部菜品")
        self.treeCtrl.SetPyData(self.root, None)
        self.treeCtrl.SetItemImage(self.root, fldridx, wx.TreeItemIcon_Normal)
        self.treeCtrl.SetItemImage(self.root, fldropenidx, wx.TreeItemIcon_Expanded)
        
        dishes_map = dict()
        CtrlDishes.RefreshItems()
        li_items = CtrlDishes.GetItems()
        for item in li_items:
            if dishes_map.has_key(item.category):
                dishes_map[item.category].append(item)
            else:
                list_tmp = []
                list_tmp.append(item)
                dishes_map_tmp = {item.category:list_tmp}
                dishes_map.update(dishes_map_tmp)
        
        li_category = CtrlCategory.GetData()
        for category in li_category:
            if dishes_map.has_key(category.code):
                title = "%s(%d)" % (category.name, len(dishes_map[category.code]))
                child = self.treeCtrl.AppendItem(self.root, title)
                self.treeCtrl.SetPyData(child, dishes_map[category.code])
                self.treeCtrl.SetItemImage(child, fldridx, wx.TreeItemIcon_Normal)
                self.treeCtrl.SetItemImage(child, fldropenidx, wx.TreeItemIcon_Expanded)
                for dishes in dishes_map[category.code]:
                    sub_clild = self.treeCtrl.AppendItem(child, dishes.name)
                    self.treeCtrl.SetPyData(sub_clild, dishes)
                    self.treeCtrl.SetItemImage(sub_clild, fileidx, wx.TreeItemIcon_Normal)
                    self.treeCtrl.SetItemImage(sub_clild, fileidx, wx.TreeItemIcon_Selected)
            else:
                title = "%s(0)" % category.name
                child = self.treeCtrl.AppendItem(self.root, title)
                self.treeCtrl.SetPyData(child, None)
                self.treeCtrl.SetItemImage(child, fldridx, wx.TreeItemIcon_Normal)
                self.treeCtrl.SetItemImage(child, fldropenidx, wx.TreeItemIcon_Expanded)
                
        self.treeCtrl.Expand(self.root)
    
    # Virtual event handlers, override them in your derived class
    def OnSize( self, event ):
        event.Skip()
        x, y = self.GetSize()

        self.btnSetting.SetMaxSize(wx.Size( 100,50 ))
        self.btnBatSetting.SetMaxSize(wx.Size( 100,50 ))
        self.btnExit.SetMaxSize(wx.Size( 50,50 ))
        self.topPanel.SetMaxSize( wx.Size( x-250,50 ) ) 
        self.treeCtrl.SetMinSize( wx.Size( 200,y-50 ) )
        self.dataViewList.SetMinSize( wx.Size( x-200,y-50 ) )
        
    def OnBntSetting( self, event ):
        event.Skip()
        if isinstance(self.tree_data, DataDishes):
            CtrlDishes.SetCurItemIndex2(self.tree_data)
            self.popRelatedSetting = PopSchemeRelated(self)
            self.popRelatedSetting.ShowModal()
    
    def OnBntBatSetting( self, event ):
        event.Skip()
        if isinstance(self.tree_data, list):
            CtrlDishes.SetCurListData(self.tree_data)
            self.popRelatedBatSetting = PopSchemeRelatedBat(self)
            self.popRelatedBatSetting.ShowModal()
    
    def OnExit( self, event ):
        event.Skip()
        AppManager.SwitchToApplication('HomePage')
        
    def OnSelChanged(self, event):
        event.Skip()
        self.tree_data = self.treeCtrl.GetPyData(event.GetItem())

    def OnActivate(self, event):
        event.Skip()
        
    def OnRefresh(self, event ):
        event.Skip()
        # Refresh treeCtrl
        CtrlDishes.RefreshItems()
        self.treeCtrl.DeleteAllItems()
        self.ShowTreeCtrl()
        
        # Refresh data view list
        result = CtrlDishes.GetData()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
                    
        self.model.Cleared()
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = WgtSchemeRelated(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()