#!/usr/bin/env python
# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
from app.home_logic import CtrlHomePage
from app.manager.logic.ctrl import * 
from app.manager.logic.model import *
from app.manager.logic.data import *
from app.app_manager import AppManager

import wx
import wx.xrc
import wx.dataview
from wx.dataview import DataViewColumn

###########################################################################
## Class PopPrinterScheme
###########################################################################


class PopPrinterScheme(wx.Dialog):
    def _init_view_sizer(self, parent):
        panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        # Create a tow rows and 1 column grid sizer for scheme and printer
        g_sizer = wx.GridSizer(2, 1, 0, 0)
        g_sizer.SetMinSize(wx.Size(600, 300))
        
        # Create scheme panel
        top_panel = wx.Panel(panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        top_g_sizer = wx.GridSizer(1, 2, 0, 0)
        # Add column 1 of scheme
        self._init_scheme_column_1_sizer(top_panel, top_g_sizer)
        # Add column 2 of scheme
        self._init_scheme_column_2_sizer(top_panel, top_g_sizer)
        # Layout scheme panel
        top_panel.SetSizer(top_g_sizer)
        top_panel.Layout()
        top_g_sizer.Fit(top_panel)
        g_sizer.Add(top_panel, 1, wx.EXPAND, 5)
        
        # Create printer panel
        bottom_panel = wx.Panel(panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        bottom_g_sizer = wx.GridSizer(3, 1, 0, 0)
        # Add printer driver sizer
        self._init_printer_row_1_sizer(bottom_panel, bottom_g_sizer)
        # Layout printer panel
        bottom_panel.SetSizer(bottom_g_sizer)
        bottom_panel.Layout()
        bottom_g_sizer.Fit(bottom_panel)
        g_sizer.Add(bottom_panel, 1, wx.EXPAND, 5)
        
        # Layout view sizer
        panel.SetSizer(g_sizer)
        panel.Layout()
        g_sizer.Fit(panel)
        parent.Add(panel, 1, wx.EXPAND | wx.ALL, 5)
        
    def _init_scheme_column_1_sizer(self, container, parent):
        g_sizer = wx.GridSizer(3, 1, 0, 0)
        # Add scheme number sizer
        code_sizer = wx.BoxSizer(wx.HORIZONTAL)
        s_txt_code = wx.StaticText(container, wx.ID_ANY, u"方案编号：", wx.DefaultPosition, wx.Size(80, -1), 0)
        s_txt_code.Wrap(-1)
        code_sizer.Add(s_txt_code, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtCode = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        code_sizer.Add(self.txtCode, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.ckxValid = wx.CheckBox(container, wx.ID_ANY, u"生效：", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT)
        code_sizer.Add(self.ckxValid, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        g_sizer.Add(code_sizer, 1, wx.EXPAND, 5)
        # Add invoice type sizer
        type_sizer = wx.BoxSizer(wx.HORIZONTAL)
        s_txt_invoice = wx.StaticText(container, wx.ID_ANY, u"厨打单类：", wx.DefaultPosition, wx.Size(80, -1), 0)
        s_txt_invoice.Wrap(-1)
        type_sizer.Add(s_txt_invoice, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        cbx_type_choices = list()
        self.cbxType = wx.ComboBox(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.Size(110, -1), cbx_type_choices, 0)
        type_sizer.Add(self.cbxType, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        g_sizer.Add(type_sizer, 1, wx.EXPAND, 5)
        # Add reserve scheme sizer
        backup_sizer = wx.BoxSizer(wx.HORIZONTAL)
        s_txt_reserve = wx.StaticText(container, wx.ID_ANY, u"后备方案：", wx.DefaultPosition, wx.Size(80, -1), 0)
        s_txt_reserve.Wrap(-1)
        backup_sizer.Add(s_txt_reserve, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        cbx_type_backup = list()
        self.cbxBackup = wx.ComboBox(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.Size(110, -1), cbx_type_backup, 0)
        backup_sizer.Add(self.cbxBackup, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        g_sizer.Add(backup_sizer, 1, wx.EXPAND, 5)
        
        # Layout column 1 of scheme
        parent.Add(g_sizer, 1, wx.EXPAND, 5)

    def _init_scheme_column_2_sizer(self, container, parent):
        g_sizer = wx.GridSizer(3, 1, 0, 0)
        # Add scheme name sizer
        name_sizer = wx.BoxSizer(wx.HORIZONTAL)
        s_txt_name = wx.StaticText(container, wx.ID_ANY, u"方案名称：", wx.DefaultPosition, wx.Size(80, -1), 0)
        s_txt_name.Wrap(-1)
        name_sizer.Add(s_txt_name, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtName = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        name_sizer.Add(self.txtName, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        g_sizer.Add(name_sizer, 1, wx.EXPAND, 5)
        # Add print number sizer
        print_num_sizer = wx.BoxSizer(wx.HORIZONTAL)
        s_txt_number = wx.StaticText(container, wx.ID_ANY, u"厨打份数：", wx.DefaultPosition, wx.Size(80, -1), 0)
        s_txt_number.Wrap(-1)
        print_num_sizer.Add(s_txt_number, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        cbx_print_num_choices = list()
        self.cbxPrintNum = wx.ComboBox(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.Size(110, -1), cbx_print_num_choices, 0)
        print_num_sizer.Add(self.cbxPrintNum, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        g_sizer.Add(print_num_sizer, 1, wx.EXPAND, 5)
        
        # Layout column 2 of scheme
        parent.Add(g_sizer, 1, wx.EXPAND, 5)
        
    def _init_printer_row_1_sizer(self, container, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add printer driver label
        s_txt_driver = wx.StaticText(container, wx.ID_ANY, u"打印机：", wx.DefaultPosition, wx.Size(80, -1), 0)
        s_txt_driver.Wrap(-1)
        sizer.Add(s_txt_driver, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add printer driver combo box 
        cbx_print_driver_choices = list()
        self.cbxPrintDriver = wx.ComboBox(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.Size(400, -1), cbx_print_driver_choices, 0)
        sizer.Add(self.cbxPrintDriver, 0, wx.ALL, 5)
        # Layout printer driver 
        parent.Add(sizer, 1, wx.EXPAND, 5)
        
    def _init_ctrl_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Add track number
        self.txtTrack = wx.StaticText(self, wx.ID_ANY, u"1 / 1", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txtTrack.Wrap(-1)
        sizer.Add(self.txtTrack, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add previous record button
        self.btnPrev = wx.Button(self, wx.ID_ANY, u"上一记录", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnPrev, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add next record button
        self.btnNext = wx.Button(self, wx.ID_ANY, u"下一记录", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnNext, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add spacer
        sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        # Add save button
        self.btnSave = wx.Button(self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnSave, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnExit, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Layout control sizer
        parent.Add(sizer, 1, wx.EXPAND, 5)
        
    def __init__(self, parent, type_="add"):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"厨打基本方案设置", pos=wx.DefaultPosition,
                           size=wx.Size(600, 400), style=wx.CAPTION)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_view_sizer(sizer)
        self._init_ctrl_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.btnPrev.Bind(wx.EVT_BUTTON, self.on_btn_prev)
        self.btnNext.Bind(wx.EVT_BUTTON, self.on_btn_next)
        self.btnSave.Bind(wx.EVT_BUTTON, self.on_btn_save)
        self.btnExit.Bind(wx.EVT_BUTTON, self.on_btn_exit)

        # Initialize 
        self.index = 0
        self.type = type_
        self._initialize_view()

    def __del__(self):
        pass

    def _initialize_view(self):
        for index_ in range(4):
            self.cbxPrintNum.Append("%d" % (index_ + 1))

        if self.type == "add":
            self._init_add_view()
        elif self.type == "mod":
            self.index = CtrlPrinterScheme.get_instance().get_cur_item_index()
            self._init_mod_view()

    def _init_add_view(self):
        li_scheme_type = CtrlSchemeType.get_instance().get_data()
        for scheme_type in li_scheme_type:
            self.cbxType.Append(scheme_type.name, scheme_type)

        self.cbxType.SetSelection(0)

        li_print_scheme = CtrlPrinterScheme.get_instance().get_data()
        for print_scheme in li_print_scheme:
            self.cbxBackup.Append(print_scheme.name, print_scheme)
        #self.cbxBackup.SetSelection(0)

        self.cbxPrintNum.SetSelection(0)

        self.txtTrack.Enable(False)
        self.btnPrev.Enable(False)
        self.btnNext.Enable(False)

    def _init_mod_view(self):
        self.txtCode.Enable(False)
        if self.index < 0:
            self.index = 0
            return

        items = CtrlPrinterScheme.get_instance().get_items()
        if self.index >= len(items):
            self.index = len(items) - 1
            return

        data = items[self.index]
        self.txtCode.SetValue(str(data.key))
        self.txtName.SetValue(data.name)
        self.ckxValid.SetValue(data.valid)
        self.txtTrack.SetLabel(("%d / %d" % (self.index+1, len(items))))

        li_scheme_type = CtrlSchemeType.get_instance().get_data()
        for scheme_type in li_scheme_type:
            self.cbxType.Append(scheme_type.name, scheme_type)
            if scheme_type.key == data.scheme_type:
                self.cbxType.SetSelection(li_scheme_type.index(scheme_type))

        li_print_scheme = CtrlPrinterScheme.get_instance().get_data()
        for print_scheme in li_print_scheme:
            self.cbxBackup.Append(print_scheme.name, print_scheme)
            if print_scheme.key == data.backup:
                self.cbxBackup.SetSelection(li_print_scheme.index(print_scheme))

        self.cbxPrintNum.SetSelection(data.print_count - 1)

    # Virtual event handlers, override them in your derived class
    def on_btn_prev(self, event):
        event.Skip()
        self.index -= 1
        self._init_mod_view()

    def on_btn_next(self, event):
        event.Skip()
        self.index += 1
        self._init_mod_view()

    def on_btn_save(self, event):
        event.Skip()

        scheme_type = self.cbxType.GetClientData(self.cbxType.GetSelection())
        print_count = int(self.cbxPrintNum.GetValue())
        try:
            if not self.cbxBackup.IsEmpty():
                scheme_backup = self.cbxBackup.GetClientData(self.cbxBackup.GetSelection())
            else:
                scheme_backup = None
        except:
            scheme_backup = None
        data = DataPrinterScheme(0, int(self.txtCode.GetValue()),
                                 self.txtCode.GetValue(),
                                 self.txtName.GetValue(),
                                 self.ckxValid.GetValue(),
                                 scheme_type.key,
                                 print_count,
                                 scheme_backup.key if scheme_backup is not None else None)
        if self.type == "add":
            CtrlPrinterScheme.add_item(data)
        elif self.type == "mod":
            CtrlPrinterScheme.update_item(data)

    def on_btn_exit(self, event):
        event.Skip()
        self.Close()

###########################################################################
## Class PopSchemeRelated
###########################################################################


class PopSchemeRelated (wx.Dialog):
    def _init_view_sizer(self, parent):
        panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(500, 200), wx.STATIC_BORDER | wx.TAB_TRAVERSAL)
        # Create 3 rows and 1 column grid sizer
        g_sizer = wx.GridSizer(3, 1, 0, 0)
        g_sizer.SetMinSize(wx.Size(500, 200))
        # Add row 1 sizer 
        panel_top_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add product code 
        s_txt_code = wx.StaticText(panel, wx.ID_ANY, u"品码：", wx.DefaultPosition, wx.Size(80, -1), 0)
        s_txt_code.Wrap(-1)
        panel_top_sizer.Add(s_txt_code, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        
        self.txtCode = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        panel_top_sizer.Add(self.txtCode, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add product name
        s_txt_name = wx.StaticText(panel, wx.ID_ANY, u"菜品名称：", wx.DefaultPosition, wx.Size(80, -1), 0)
        s_txt_name.Wrap(-1)
        panel_top_sizer.Add(s_txt_name, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        
        self.txtName = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        panel_top_sizer.Add(self.txtName, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Layout row 1 sizer
        g_sizer.Add(panel_top_sizer, 1, wx.EXPAND, 5)

        # Add row 2 sizer
        panel_mid_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add kitchen print 
        self.radioBtnPrintOn = wx.RadioButton(panel, wx.ID_ANY, u"厨打", wx.DefaultPosition, wx.Size(100, -1), 0)
        panel_mid_sizer.Add(self.radioBtnPrintOn, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        
        self.radioBtnPrintOff = wx.RadioButton(panel, wx.ID_ANY, u"不厨打", wx.DefaultPosition, wx.Size(100, -1), 0)
        panel_mid_sizer.Add(self.radioBtnPrintOff, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Layout row 2 sizer
        g_sizer.Add(panel_mid_sizer, 1, wx.EXPAND, 5)

        # Add row 3 sizer
        panel_bottom_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add kitchen print scheme
        s_txt_scheme = wx.StaticText(panel, wx.ID_ANY, u"厨打方案：", wx.DefaultPosition, wx.Size(80, -1), 0)
        s_txt_scheme.Wrap(-1)
        panel_bottom_sizer.Add(s_txt_scheme, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        
        cbx_scheme_choices = list()
        self.cbxScheme = wx.ComboBox(panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.Size(110, -1), cbx_scheme_choices, 0)
        panel_bottom_sizer.Add(self.cbxScheme, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Layout row 3 sizer
        g_sizer.Add(panel_bottom_sizer, 1, wx.EXPAND, 5)

        # Layout view sizer
        panel.SetSizer(g_sizer)
        panel.Layout()
        parent.Add(panel, 1, wx.ALL, 5)

    def _init_ctrl_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add track number
        self.txtTrack = wx.StaticText(self, wx.ID_ANY, u"1 / 1", wx.DefaultPosition, wx.DefaultSize, 0)
        self.txtTrack.Wrap(-1)
        sizer.Add(self.txtTrack, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add previous record button
        self.btnPrev = wx.Button(self, wx.ID_ANY, u"上一记录", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnPrev, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add next record button
        self.btnNext = wx.Button(self, wx.ID_ANY, u"下一记录", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnNext, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add spacer
        sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        # Add save button
        self.btnSave = wx.Button(self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnSave, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnExit, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        
        # Layout control sizer
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"菜品厨打设置", pos=wx.DefaultPosition,
                           size=wx.Size(500, 300), style=wx.CAPTION | wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.SetMinSize(wx.Size(500, 300))
        self._init_view_sizer(sizer)
        self._init_ctrl_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)
        
        # Connect Events
        self.btnPrev.Bind(wx.EVT_BUTTON, self.on_btn_prev)
        self.btnNext.Bind(wx.EVT_BUTTON, self.on_btn_next)
        self.btnSave.Bind(wx.EVT_BUTTON, self.on_btn_save)
        self.btnExit.Bind(wx.EVT_BUTTON, self.on_btn_exit)
        
        # Initialize
        self.index = CtrlDishes.get_instance().get_cur_item_index()
        self._initialize_view()
    
    def __del__(self):
        pass
    
    def _initialize_view(self):
        self.txtCode.Enable(False)
        self.txtName.Enable(False)
        if self.index < 0:
            self.index = 0
            return
        
        items = CtrlDishes.get_instance().get_items()
        if self.index >= len(items):
            self.index = len(items) - 1
            return
        
        data = items[self.index]
        if data.is_print == '0':
            self.radioBtnPrintOn.SetValue(False)
            self.radioBtnPrintOff.SetValue(True)
        else:
            self.radioBtnPrintOn.SetValue(True)
            self.radioBtnPrintOff.SetValue(False)

        self.txtCode.SetValue(str(data.key))
        self.txtName.SetValue(data.name)
        li_scheme = CtrlPrinterScheme.get_instance().get_data()
        for scheme in li_scheme:
            self.cbxScheme.Append(scheme.name, scheme)
            if scheme.key == data.printer_scheme:
                self.cbxScheme.SetSelection(li_scheme.index(scheme))
            
    # Virtual event handlers, override them in your derived class
    def on_btn_prev(self, event):
        event.Skip()
        self.index -= 1
        self._initialize_view()
    
    def on_btn_next(self, event):
        event.Skip()
        self.index += 1
        self._initialize_view()
    
    def on_btn_save(self, event):
        event.Skip()
        scheme_type = self.cbxScheme.GetClientData(self.cbxScheme.GetSelection())
        items = CtrlDishes.get_instance().get_items()
        if self.index >= len(items):
            self.index = len(items) - 1
            return
        
        data = items[self.index]
        data.printer_scheme = scheme_type.key
        data.is_print = u'1' if self.radioBtnPrintOn.GetValue() else u'0'
        CtrlDishes.update_print_scheme(data)
    
    def on_btn_exit(self, event):
        event.Skip()
        self.Close()

###########################################################################
## Class PopSchemeRelatedBat
###########################################################################


class PopSchemeRelatedBat (wx.Dialog):
    def _init_view_sizer(self, parent):
        panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(500, 100), wx.STATIC_BORDER | wx.TAB_TRAVERSAL)
        # Create a 2 rows and 1 column grid sizer
        g_sizer = wx.GridSizer(2, 1, 0, 0)
        g_sizer.SetMinSize(wx.Size(500, 100))
        # Create kitchen print sizer
        print_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.radioBtnPrintOn = wx.RadioButton(panel, wx.ID_ANY, u"厨打", wx.DefaultPosition, wx.Size(100, -1), 0)
        print_sizer.Add(self.radioBtnPrintOn, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        
        self.radioBtnPrintOff = wx.RadioButton(panel, wx.ID_ANY, u"不厨打", wx.DefaultPosition, wx.Size(100, -1), 0)
        print_sizer.Add(self.radioBtnPrintOff, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Layout kitchen print sizer
        g_sizer.Add(print_sizer, 1, wx.EXPAND, 5)

        # Create kitchen print scheme sizer
        scheme_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        s_txt_scheme = wx.StaticText(panel, wx.ID_ANY, u"厨打方案：", wx.DefaultPosition, wx.Size(80, -1), 0)
        s_txt_scheme.Wrap(-1)
        scheme_sizer.Add(s_txt_scheme, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        
        cbx_scheme_name_choices = list()
        self.cbxSchemeName = wx.ComboBox(panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.Size(110, -1), cbx_scheme_name_choices, 0)
        scheme_sizer.Add(self.cbxSchemeName, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Layout kitchen print scheme sizer
        g_sizer.Add(scheme_sizer, 1, wx.EXPAND, 5)

        # Layout view sizer
        panel.SetSizer(g_sizer)
        panel.Layout()
        parent.Add(panel, 1, wx.ALL, 5)

    def _init_ctrl_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # Add spacer
        sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        # Add batch button
        self.btnBat = wx.Button(self, wx.ID_ANY, u"批处理", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnBat, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnExit, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        
        # Layout control sizer
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"菜品厨打批处理", pos=wx.DefaultPosition,
                           size=wx.Size(500, 200), style=wx.CAPTION)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.SetMinSize(wx.Size(500, 200))
        self._init_view_sizer(sizer)
        self._init_ctrl_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)
        
        # Connect Events
        self.btnBat.Bind(wx.EVT_BUTTON, self.on_btn_batch)
        self.btnExit.Bind(wx.EVT_BUTTON, self.on_btn_exit)
        
        # Initialize view data
        self.list_data = CtrlDishes.get_instance().get_cur_list_data()
        self._initialize_view()
    
    def __del__(self):
        pass    
    
    def _initialize_view(self):
        li_scheme = CtrlPrinterScheme.get_instance().get_data()
        for scheme in li_scheme:
            self.cbxSchemeName.Append(scheme.name, scheme) 
                
    # Virtual event handlers, override them in your derived class
    def on_btn_batch(self, event):
        event.Skip()
        if self.list_data is None:
            return
        
        scheme_type = self.cbxSchemeName.GetClientData(self.cbxSchemeName.GetSelection())
        for item in self.list_data:
            if isinstance(item, DataDishes):
                item.printer_scheme = scheme_type.key
                CtrlDishes.update_print_scheme(item)
                
    def on_btn_exit(self, event):
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
        self.dataViewList.SetMinSize(wx.Size(600, 300))
        # Add items into data view list
        self.dataViewList.AppendTextColumn(u"行号", 0) 
        self.dataViewList.AppendTextColumn(u"编码", 1, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE) 
        self.dataViewList.AppendTextColumn(u"单类名称", 2, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE) 
        sizer.Add(self.dataViewList, 0, wx.ALL | wx.EXPAND, 5)
        
        # Layout view sizer
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_ctrl_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add new button
        self.btnNew = wx.Button(self, wx.ID_ANY, u"新增", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnNew, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        # Add delete button
        self.btnDelete = wx.Button(self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnDelete, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        # Add spacer
        sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        # Add refresh button
        self.btnRefresh = wx.Button(self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnRefresh, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        # Add save button
        self.btnSave = wx.Button(self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnSave, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnExit, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        
        # Layout control sizer 
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"厨打单类型", pos=wx.DefaultPosition,
                           size=wx.Size(600, 400), style=wx.CAPTION | wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.Size(-1, -1), wx.Size(-1, -1))
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_view_sizer(sizer)
        self._init_ctrl_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Create an instance of our model...
        self.model = ModelSchemeType(CtrlSchemeType.get_instance().get_data())
        
        # Tell the DVC to use the model
        self.dataViewList.AssociateModel(self.model)

        # Connect Events
        self.btnNew.Bind(wx.EVT_BUTTON, self.on_btn_new)
        self.btnDelete.Bind(wx.EVT_BUTTON, self.on_btn_delete)
        self.btnRefresh.Bind(wx.EVT_BUTTON, self.on_btn_refresh)
        self.btnSave.Bind(wx.EVT_BUTTON, self.on_btn_save)
        self.btnExit.Bind(wx.EVT_BUTTON, self.on_btn_exit)
    
    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def on_btn_new(self, event):
        event.Skip()
        CtrlSchemeType.get_instance().add_item(DataSchemeType(0, 0, ""))
        
        data = DataSchemeType(CtrlSchemeType.get_instance().get_data_len() + 1, CtrlSchemeType.get_id(), "")
        self.model.data.append(data)
        item = self.model.ObjectToItem(data)
        self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
    
    def on_btn_delete(self, event):
        event.Skip()
        try:
            item = self.dataViewList.GetCurrentItem()
            data = self.model.ItemToObject(item)
            self.model.data.remove(data)
            self.dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
            CtrlSchemeType.delete_item(data)
        except:
            print 'PopSchemeType on_btn_delete error'
    
    def on_btn_refresh(self, event):
        event.Skip()
        result = CtrlSchemeType.get_instance().get_data()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
                    
        self.model.Cleared()
    
    def on_btn_save(self, event):
        event.Skip()
        for data in self.model.data:
            CtrlSchemeType.update_item(data)
    
    def on_btn_exit(self, event):
        event.Skip()
        self.Close()

###########################################################################
## Class WgtPrinterScheme
###########################################################################


class WgtPrinterScheme(wx.Panel):
    def _init_status_bar_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.SetMinSize(wx.Size(-1, 50))
        # Add new button
        self.btnNew = wx.Button(self, wx.ID_ANY, u"新增", wx.DefaultPosition, wx.Size(50, 50), 0)
        sizer.Add(self.btnNew, 0, 0, 5)
        # Add modify button
        self.btnModify = wx.Button(self, wx.ID_ANY, u"修改", wx.DefaultPosition, wx.Size(50, 50), 0)
        sizer.Add(self.btnModify, 0, 0, 5)
        # Add delete button
        self.btnDelete = wx.Button(self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.Size(50, 50), 0)
        sizer.Add(self.btnDelete, 0, 0, 5)
        # Add invoice type button
        self.btnSchemeType = wx.Button(self, wx.ID_ANY, u"单类", wx.DefaultPosition, wx.Size(50, 50), 0)
        sizer.Add(self.btnSchemeType, 0, 0, 5)
        # Add refresh button
        self.btnRefresh = wx.Button(self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.Size(50, 50), 0)
        sizer.Add(self.btnRefresh, 0, 0, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.Size(50, 50), 0)
        sizer.Add(self.btnExit, 0, 0, 5)
        # Add fix space panel
        self.topPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), wx.TAB_TRAVERSAL)
        self.topPanel.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
        self.topPanel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
        self.topPanel.SetMaxSize(wx.Size(-1, 50))
        sizer.Add(self.topPanel, 1, wx.EXPAND, 5)
        
        # Layout status bar sizer
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_data_view_sizer(self, parent):
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.SetMinSize(wx.Size(800, 600))
        # Create data view list
        self.dataViewList = wx.dataview.DataViewCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(800, 600), 0)
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

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition,
                          size=wx.Size(800, 600), style=wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.Size(-1, -1), wx.DefaultSize)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_status_bar_sizer(sizer)
        self._init_data_view_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Create an instance of our model...
        self.model = ModelPrinterScheme(CtrlPrinterScheme.get_instance().get_data())
        CtrlPrinterScheme.get_instance().refresh_items()
        
        # Tell the DVC to use the model
        self.dataViewList.AssociateModel(self.model)

        # Connect Events
        self.Bind(wx.EVT_SIZE, self.on_size)
        
        self.btnNew.Bind(wx.EVT_BUTTON, self.on_btn_new)
        self.btnModify.Bind(wx.EVT_BUTTON, self.on_btn_modify)
        self.btnDelete.Bind(wx.EVT_BUTTON, self.on_btn_delete)
        self.btnSchemeType.Bind(wx.EVT_BUTTON, self.pn_btn_scheme_type)
        self.btnRefresh.Bind(wx.EVT_BUTTON, self.on_btn_refresh)
        self.btnExit.Bind(wx.EVT_BUTTON, self.on_btn_exit)
    
    def __del__(self):
        pass
    
    def initialize(self):
        # Add event listener
        EvtManager.add_listener(self, EnumEvent.EVT_PRINTER_SCHEME_REFRESH, self.on_btn_refresh)
        
        x, y = CtrlHomePage.get_instance().get_screen_size()
        self.SetSize(wx.Size(x, y))

    def un_initialize(self):
        # Add event listener
        EvtManager.remove_listener(self, EnumEvent.EVT_PRINTER_SCHEME_REFRESH, self.on_btn_refresh)
    
    def _refresh_ui(self):
        # Refresh data view list
        CtrlPrinterScheme.get_instance().refresh_items()
        result = CtrlPrinterScheme.get_instance().get_data()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
                    
        self.model.Cleared()
    
    # Virtual event handlers, override them in your derived class
    def on_size(self, event):
        event.Skip()
        x, y = self.GetSize()

        self.btnNew.SetMaxSize(wx.Size(50, 50))
        self.btnModify.SetMaxSize(wx.Size(50, 50))
        self.btnDelete.SetMaxSize(wx.Size(50, 50))
        self.btnSchemeType.SetMaxSize(wx.Size(50, 50))
        self.btnRefresh.SetMaxSize(wx.Size(50, 50))
        self.btnExit.SetMaxSize(wx.Size(50, 50))
        self.topPanel.SetMaxSize(wx.Size(x-300, 50))
        self.dataViewList.SetMinSize(wx.Size(x, y-50))
        
    def on_btn_new(self, event):
        event.Skip()
        pop_printer_scheme = PopPrinterScheme(self, "add")
        pop_printer_scheme.ShowModal()
    
    def on_btn_modify(self, event):
        event.Skip()
        try:
            item = self.dataViewList.GetCurrentItem()
            data = self.model.ItemToObject(item)
            index = self.model.data.index(data)
            CtrlPrinterScheme.get_instance().set_cur_item_index(index)
            pop_printer_scheme = PopPrinterScheme(self, "mod")
            pop_printer_scheme.ShowModal()
        except:
            print 'WgtPrinterScheme on_btn_modify error'
    
    def on_btn_delete(self, event):
        event.Skip()
        try:
            item = self.dataViewList.GetCurrentItem()
            data = self.model.ItemToObject(item)
            self.model.data.remove(data)
            self.dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
            CtrlPrinterScheme.delete_item(data)
        except:
            print 'WgtPrinterScheme on_btn_delete error'
        
    def pn_btn_scheme_type(self, event):
        event.Skip()  
        pop_scheme_type = PopSchemeType(self)
        pop_scheme_type.ShowModal()
    
    def on_btn_refresh(self, event):
        event.Skip()
        self._refresh_ui()
    
    def on_btn_exit(self, event):
        event.Skip()
        self.Hide()
        AppManager.get_instance().switch_to_application('HomePage')
        
###########################################################################
## Class WgtSchemeRelated
###########################################################################


class WgtSchemeRelated (wx.Panel):
    def _init_status_bar_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.SetMinSize(wx.Size(800, 50))
        # Add kitchen print setting button
        self.btnSetting = wx.Button(self, wx.ID_ANY, u"厨打设置", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnSetting, 0, wx.EXPAND, 5)
        # Add batch kitchen print setting button
        self.btnBatSetting = wx.Button(self, wx.ID_ANY, u"批处理", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnBatSetting.SetMinSize(wx.Size(100, 50))
        sizer.Add(self.btnBatSetting, 0, 0, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnExit.SetMinSize(wx.Size(50, 50))
        sizer.Add(self.btnExit, 0, 0, 5)
        # Add fix space panel
        self.topPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.topPanel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
        sizer.Add(self.topPanel, 1, wx.EXPAND, 5)
        
        # Layout status bar sizer
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_data_view_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.SetMinSize(wx.Size(800, 550))
        # Add tree control
        left_sizer = wx.BoxSizer(wx.VERTICAL)
        left_sizer.SetMinSize(wx.Size(200, 550))
        self.treeCtrl = wx.TreeCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE)        
        left_sizer.Add(self.treeCtrl, 0, wx.EXPAND, 5)
        sizer.Add(left_sizer, 1, 0, 5)
        # Add data view list
        right_sizer = wx.BoxSizer(wx.VERTICAL)
        right_sizer.SetMinSize(wx.Size(600, 550))
        self.dataViewList = wx.dataview.DataViewCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.dataViewList.SetMinSize(wx.Size(-1, 600))
        # Add items into data view list
        self.dataViewList.AppendTextColumn(u"行号", 0) 
        self.dataViewList.AppendTextColumn(u"品码", 1) 
        self.dataViewList.AppendTextColumn(u"品名", 2) 
        self.dataViewList.AppendTextColumn(u"厨打方式", 10) 
        right_sizer.Add(self.dataViewList, 0, wx.EXPAND | wx.LEFT, 5)

        sizer.Add(right_sizer, 1, 0, 5)
        # Layout data view list
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition,
                          size=wx.Size(800, 600), style=wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_status_bar_sizer(sizer)
        self._init_data_view_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Create an instance of our model...
        self.model = ModelDishes(CtrlDishes.get_instance().get_data())
        CtrlDishes.get_instance().refresh_items()
        
        # Tell the DVC to use the model
        self.dataViewList.AssociateModel(self.model)

        # Connect Events
        self.Bind(wx.EVT_SIZE, self.on_size)
        
        self.btnSetting.Bind(wx.EVT_BUTTON, self.on_btn_setting)
        self.btnBatSetting.Bind(wx.EVT_BUTTON, self.on_btn_batch_setting)
        self.btnExit.Bind(wx.EVT_BUTTON, self.on_exit)
        
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.on_sel_changed, self.treeCtrl)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.on_activate, self.treeCtrl)
        
        # Show tree control
        self.tree_data = None
        self._show_tree_ctrl()
    
    def __del__(self):
        pass
    
    def initialize(self):
        # Add event listener
        EvtManager.add_listener(self, EnumEvent.EVT_DISHES_PUBLISH_REFRESH, self.on_refresh)
        
        x, y = CtrlHomePage.get_instance().get_screen_size()
        self.SetSize(wx.Size(x, y))

    def un_initialize(self):
        # Add event listener
        EvtManager.remove_listener(self, EnumEvent.EVT_DISHES_PUBLISH_REFRESH, self.on_refresh)
    
    def _show_tree_ctrl(self):
        isz = (16, 16)
        il = wx.ImageList(isz[0], isz[1])
        fl_idx = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, isz))
        fl_open_idx = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER_OPEN, wx.ART_OTHER, isz))
        file_idx = il.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, isz))
        
        self.treeCtrl.SetImageList(il)
        self.il = il

        self.root = self.treeCtrl.AddRoot(u"全部菜品")
        self.treeCtrl.SetPyData(self.root, None)
        self.treeCtrl.SetItemImage(self.root, fl_idx, wx.TreeItemIcon_Normal)
        self.treeCtrl.SetItemImage(self.root, fl_open_idx, wx.TreeItemIcon_Expanded)
        
        dishes_map = dict()
        CtrlDishes.get_instance().refresh_items()
        li_items = CtrlDishes.get_instance().get_items()
        for item in li_items:
            if item.category in dishes_map:
                dishes_map[item.category].append(item)
            else:
                list_tmp = list()
                list_tmp.append(item)
                dishes_map_tmp = {item.category: list_tmp}
                dishes_map.update(dishes_map_tmp)
        
        li_category = CtrlCategory.get_instance().get_data()
        for category in li_category:
            if category.key in dishes_map:
                title = "%s(%d)" % (category.name, len(dishes_map[category.key]))
                child = self.treeCtrl.AppendItem(self.root, title)
                self.treeCtrl.SetPyData(child, dishes_map[category.key])
                self.treeCtrl.SetItemImage(child, fl_idx, wx.TreeItemIcon_Normal)
                self.treeCtrl.SetItemImage(child, fl_open_idx, wx.TreeItemIcon_Expanded)
                for dishes in dishes_map[category.key]:
                    sub_child = self.treeCtrl.AppendItem(child, dishes.name)
                    self.treeCtrl.SetPyData(sub_child, dishes)
                    self.treeCtrl.SetItemImage(sub_child, file_idx, wx.TreeItemIcon_Normal)
                    self.treeCtrl.SetItemImage(sub_child, file_idx, wx.TreeItemIcon_Selected)
            else:
                title = "%s(0)" % category.name
                child = self.treeCtrl.AppendItem(self.root, title)
                self.treeCtrl.SetPyData(child, None)
                self.treeCtrl.SetItemImage(child, fl_idx, wx.TreeItemIcon_Normal)
                self.treeCtrl.SetItemImage(child, fl_open_idx, wx.TreeItemIcon_Expanded)
                
        self.treeCtrl.Expand(self.root)
    
    # Virtual event handlers, override them in your derived class
    def on_size(self, event):
        event.Skip()
        x, y = self.GetSize()

        self.btnSetting.SetMaxSize(wx.Size(100, 50))
        self.btnBatSetting.SetMaxSize(wx.Size(100, 50))
        self.btnExit.SetMaxSize(wx.Size(50, 50))
        self.topPanel.SetMaxSize(wx.Size(x-250, 50))
        self.treeCtrl.SetMinSize(wx.Size(200, y-50))
        self.dataViewList.SetMinSize(wx.Size(x-200, y-50))
        
    def on_btn_setting(self, event):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        try:
            data = self.model.ItemToObject(item)
        except:
            for item_ in self.model.data:
                if item_.key == self.tree_data.key:
                    data = item_
        index_ = self.model.data.index(data)
        CtrlDishes.get_instance().set_cur_item_index(index_)
        pop_related_setting = PopSchemeRelated(self)
        pop_related_setting.ShowModal()
    
    def on_btn_batch_setting(self, event):
        event.Skip()
        if isinstance(self.tree_data, list):
            CtrlDishes.get_instance().set_cur_list_data(self.tree_data)
            pop_related_bat_setting = PopSchemeRelatedBat(self)
            pop_related_bat_setting.ShowModal()
    
    def on_exit(self, event):
        event.Skip()
        self.Hide()
        AppManager.get_instance().switch_to_application('HomePage')
        
    def on_sel_changed(self, event):
        event.Skip()
        self.tree_data = self.treeCtrl.GetPyData(event.GetItem())

    def on_activate(self, event):
        event.Skip()
        self.tree_data = self.treeCtrl.GetPyData(event.GetItem())
        if isinstance(self.tree_data, DataDishes):
            self.on_btn_setting(event)
        
    def on_refresh(self, event):
        event.Skip()
        # Refresh treeCtrl
        CtrlDishes.get_instance().refresh_items()
        self.treeCtrl.DeleteAllItems()
        self._show_tree_ctrl()
        
        # Refresh data view list
        result = CtrlDishes.get_instance().get_data()
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