#!/usr/bin/env python
# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
from app.manager.UI.sys_setting import *
from app.manager.AppManager import AppManager
from app.manager.logic.ctrl import CtrlHomePage

import wx
import wx.xrc

###########################################################################
## Class CWgtDeskTop
###########################################################################

li_func_widget_1 = ['DiningTable', 'DishesPublish', 'Employee', 'PrinterScheme', '', 'Company']
li_func_widget_2 = ['', '', 'DutyTable', 'SchemeRelated', '', 'Register']

li_title = [u"餐厅设置", u"菜品发布", u"员工管理", u"打印设置", u"报表中心", u"系统设置"]


class WgtHomePage (wx.Panel):
    def _init_status_bar_sizer(self, parent):
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Add status bar panel
        sizer.SetMinSize(wx.Size(800, 50)) 
        self.logoPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.logoPanel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.logoPanel.SetMinSize(wx.Size(50, 50))
        sizer.Add(self.logoPanel, 1, wx.EXPAND | wx.BOTTOM, 5)
        parent.Add(sizer, 1, 0, 5)
        
    def _init_screen_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.SetMinSize(wx.Size(800, 750))
        
        self._init_selector_sizer(sizer)
        self._init_func_widget_sizer(sizer)
        
        parent.Add(sizer, 1, 0, 5)
        
    def _init_selector_sizer(self, parent):
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.SetMinSize(wx.Size(200, 750))
        
        # Selector panel initialize
        self.selectorPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.selectorPanel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))
        
        selector_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Add enough space on top 
        selector_top_sizer = wx.BoxSizer(wx.VERTICAL)
        selector_top_sizer.SetMinSize(wx.Size(200, 50))
        selector_top_sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        selector_sizer.Add(selector_top_sizer, 1, 0, 5)
        
        # Set the selector buttons
        selector_bottom_sizer = wx.BoxSizer(wx.VERTICAL)
        selector_bottom_sizer.SetMinSize(wx.Size(200, 550))
        # Add dining room setting button
        self.btnDiningRoomSetting = wx.Button(self.selectorPanel, wx.ID_ANY, u"餐厅设置",
                                              wx.Point(50, 50), wx.DefaultSize, 0)
        selector_bottom_sizer.Add(self.btnDiningRoomSetting, 0, wx.ALIGN_CENTER, 5)
        # Add dishes publish button
        self.btnDishesPublishing = wx.Button(self.selectorPanel, wx.ID_ANY, u"菜品发布", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        selector_bottom_sizer.Add(self.btnDishesPublishing, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add employee manager button
        self.btnStaffMan = wx.Button(self.selectorPanel, wx.ID_ANY, u"员工管理", wx.DefaultPosition, wx.DefaultSize, 0)
        selector_bottom_sizer.Add(self.btnStaffMan, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add printer setting button
        self.btnPrinter = wx.Button(self.selectorPanel, wx.ID_ANY, u"打印设置", wx.DefaultPosition, wx.DefaultSize, 0)
        selector_bottom_sizer.Add(self.btnPrinter, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add report forms button
        self.btnReportForms = wx.Button(self.selectorPanel, wx.ID_ANY, u"报表中心", wx.DefaultPosition, wx.DefaultSize, 0)
        selector_bottom_sizer.Add(self.btnReportForms, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add system setting button
        self.btnSysSetting = wx.Button(self.selectorPanel, wx.ID_ANY, u"系统设置", wx.DefaultPosition, wx.DefaultSize, 0)
        selector_bottom_sizer.Add(self.btnSysSetting, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add exit button
        self.btnExit = wx.Button(self.selectorPanel, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        selector_bottom_sizer.Add(self.btnExit, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        
        # Layout selector buttons
        selector_sizer.Add(selector_bottom_sizer, 1, 0, 5)
        self.selectorPanel.SetSizer(selector_sizer)
        self.selectorPanel.Layout()
        selector_sizer.Fit(self.selectorPanel)
        sizer.Add(self.selectorPanel, 1, wx.EXPAND | wx.RIGHT, 5)
        parent.Add(sizer, 1, 0, 5)
        
    def _init_func_widget_sizer(self, parent):
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.SetMinSize(wx.Size(600, 750)) 
        
        # Function widget panel initialize
        self.funcPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.funcPanel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))
        self.funcPanel.SetMinSize(wx.Size(800, 600))
        
        func_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # Define function buttons dictionary
        self.di_funcButtons = dict()
        # Add function 1
        self.btnFunc_1 = wx.Button(self.funcPanel, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0)  
        func_btn_item_1 = {0: self.btnFunc_1}
        self.di_funcButtons.update(func_btn_item_1)
        # Add function 2
        self.btnFunc_2 = wx.Button(self.funcPanel, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0)
        func_btn_item_2 = {1: self.btnFunc_2}
        self.di_funcButtons.update(func_btn_item_2)
        # Add function 3
        self.btnFunc_3 = wx.Button(self.funcPanel, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0)
        func_btn_item_3 = {2: self.btnFunc_3}
        self.di_funcButtons.update(func_btn_item_3)
        # Add function 4
        self.btnFunc_4 = wx.Button(self.funcPanel, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0)
        func_btn_item_4 = {3: self.btnFunc_4}
        self.di_funcButtons.update(func_btn_item_4)
        # Add function 5
        self.btnFunc_5 = wx.Button(self.funcPanel, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0)
        func_btn_item_5 = {4: self.btnFunc_5}
        self.di_funcButtons.update(func_btn_item_5)
        # Add function 6
        self.btnFunc_6 = wx.Button(self.funcPanel, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0) 
        func_btn_item_6 = {5: self.btnFunc_6}
        self.di_funcButtons.update(func_btn_item_6)
        
        # Layout function widget items
        self.funcPanel.SetSizer(func_sizer)
        self.funcPanel.Layout()
        func_sizer.Fit(self.funcPanel)
        sizer.Add(self.funcPanel, 1, wx.EXPAND, 5)
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition,
                          size=wx.Size(800, 600), style=wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.Size(800, 600), wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWFRAME))

        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_status_bar_sizer(sizer)
        self._init_screen_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.btnDiningRoomSetting.Bind(wx.EVT_LEFT_DOWN, self.on_dining_room_setting)
        self.btnDishesPublishing.Bind(wx.EVT_LEFT_DOWN, self.on_dishes_publishing)
        self.btnStaffMan.Bind(wx.EVT_LEFT_DOWN, self.on_employee_manager)
        self.btnPrinter.Bind(wx.EVT_LEFT_DOWN, self.on_printer_setting)
        self.btnReportForms.Bind(wx.EVT_LEFT_DOWN, self.on_report_forms)
        self.btnSysSetting.Bind(wx.EVT_LEFT_DOWN, self.on_system_setting)
        self.btnExit.Bind(wx.EVT_LEFT_DOWN, parent.on_exit)
        self.btnFunc_1.Bind(wx.EVT_LEFT_DOWN, self.on_func_1)
        self.btnFunc_2.Bind(wx.EVT_LEFT_DOWN, self.on_func_2)
        self.btnFunc_3.Bind(wx.EVT_LEFT_DOWN, self.on_func_3)
        self.btnFunc_4.Bind(wx.EVT_LEFT_DOWN, self.on_func_4)
        self.btnFunc_5.Bind(wx.EVT_LEFT_DOWN, self.on_func_5)
        self.btnFunc_6.Bind(wx.EVT_LEFT_DOWN, self.on_func_6)

    def __del__(self):
        pass

    # Override function, initialize user interface
    def initialize(self):
        x, y = CtrlHomePage.get_screen_size()
        self.SetSize(wx.Size(x, y))

        select_item = CtrlHomePage.get_selected_item()
        if select_item == 0:
            self._show_dining_room_setting()
        elif select_item == 1:
            self._show_dishes_publishing()
        elif select_item == 2:
            self._show_employee_manager()
        elif select_item == 3:
            self._show_kitchen_printer()
        elif select_item == 4:
            self._show_report_forms()
        elif select_item == 5:
            self._show_system_setting()

    # Override function un initialize user interface
    def un_initialize(self):
        pass

    # Virtual event handlers, override them in your derived class
    def on_size(self, event):
        event.Skip()
        x, y = self.GetSize()

        self.logoPanel.SetMinSize(wx.Size(x, 50))
        self.selectorPanel.SetMaxSize(wx.Size(200, y-50))
        self.funcPanel.SetMinSize(wx.Size(x-200, y-50))

        self._show_func_buttons()

    def on_dining_room_setting(self, event):
        event.Skip()
        CtrlHomePage.set_selected_item(0)
        self._show_dining_room_setting()

    def on_dishes_publishing(self, event):
        event.Skip()
        CtrlHomePage.set_selected_item(1)
        self._show_dishes_publishing()

    def on_employee_manager(self, event):
        event.Skip()
        CtrlHomePage.set_selected_item(2)
        self._show_employee_manager()

    def on_printer_setting(self, event):
        event.Skip()
        CtrlHomePage.set_selected_item(3)
        self._show_kitchen_printer()

    def on_report_forms(self, event):
        event.Skip()
        CtrlHomePage.set_selected_item(4)
        self._show_report_forms()

    def on_system_setting(self, event):
        event.Skip()
        CtrlHomePage.set_selected_item(5)
        self._show_system_setting()

    def on_func_1(self, event):
        event.Skip()
        select_item = CtrlHomePage.get_selected_item()
        if select_item != 5:
            AppManager.switch_to_application(li_func_widget_1[select_item])
        else:
            pop_company = PopCompany(self)
            pop_company.ShowModal()
            self.Refresh()

    def on_func_2(self, event):
        event.Skip()
        select_item = CtrlHomePage.get_selected_item()
        if select_item != 5:
            AppManager.switch_to_application(li_func_widget_2[select_item])
        else:
            pop_register = PopRegister(self)
            pop_register.ShowModal()
            self.Refresh()

    def on_func_3(self, event):
        event.Skip()
        self.Refresh()

    def on_func_4(self, event):
        event.Skip()
        self.Refresh()

    def on_func_5(self, event):
        event.Skip()
        self.Refresh()

    def on_func_6(self, event):
        event.Skip()
        self.Refresh()

    def _show_dining_room_setting(self):
        self._enable_all_selector()
        self._hide_all_func_buttons()
        self.btnDiningRoomSetting.Enabled = False
        #self.btnFunc_1.Show()
        #self.btnFunc_1.Label = u"餐桌设置"
        AppManager.switch_to_application(li_func_widget_1[0])
        self._set_screen_tile()

    def _show_dishes_publishing(self):
        self._enable_all_selector()
        self._hide_all_func_buttons()
        self.btnDishesPublishing.Enabled = False
        #self.btnFunc_1.Show()
        #self.btnFunc_1.Label = u"菜品发布"
        AppManager.switch_to_application(li_func_widget_1[1])
        self._set_screen_tile()
        self._show_func_buttons()

    def _show_employee_manager(self):
        self._enable_all_selector()
        self._hide_all_func_buttons()
        self.btnStaffMan.Enabled = False
        self.btnFunc_1.Show()
        self.btnFunc_1.Label = u"员工管理"
        self.btnFunc_2.Show()
        self.btnFunc_2.Label = u"权限管理"
        self.btnFunc_3.Show()
        self.btnFunc_3.Label = u"员工排班"
        self._set_screen_tile()
        self._show_func_buttons()

    def _show_kitchen_printer(self):
        self._enable_all_selector()
        self._hide_all_func_buttons()
        self.btnPrinter.Enabled = False
        self.btnFunc_1.Show()
        self.btnFunc_1.Label = u"厨打方案"
        self.btnFunc_2.Show()
        self.btnFunc_2.Label = u"菜品关联"
        self._set_screen_tile()
        self._show_func_buttons()

    def _show_report_forms(self):
        self._enable_all_selector()
        self._hide_all_func_buttons()
        self.btnReportForms.Enabled = False
        self.btnFunc_1.Show()
        self.btnFunc_1.Label = u"菜品销售查询"
        self.btnFunc_2.Show()
        self.btnFunc_2.Label = u"收银情况查询"
        self.btnFunc_3.Show()
        self.btnFunc_3.Label = u"营业情况查询"
        self.btnFunc_4.Show()
        self.btnFunc_4.Label = u"消费查询"
        self.btnFunc_5.Show()
        self.btnFunc_5.Label = u"菜品排行榜"
        self._set_screen_tile()
        self._show_func_buttons()

    def _show_system_setting(self):
        self._enable_all_selector()
        self._hide_all_func_buttons()
        self.btnSysSetting.Enabled = False
        self.btnFunc_1.Show()
        self.btnFunc_1.Label = u"公司信息"
        self.btnFunc_2.Show()
        self.btnFunc_2.Label = u"注册"
        self.btnFunc_3.Show()
        self.btnFunc_3.Label = u"数据备份"
        self._set_screen_tile()
        self._show_func_buttons()

    def _enable_all_selector(self):
        self.btnDiningRoomSetting.Enabled = True
        self.btnDishesPublishing.Enabled = True
        self.btnStaffMan.Enabled = True
        self.btnPrinter.Enabled = True
        self.btnReportForms.Enabled = True
        self.btnSysSetting.Enabled = True

    def _hide_all_func_buttons(self):
        self.btnFunc_1.Hide()
        self.btnFunc_2.Hide()
        self.btnFunc_3.Hide()
        self.btnFunc_4.Hide()
        self.btnFunc_5.Hide()
        self.btnFunc_6.Hide()    

    def _show_func_buttons(self):
        select_item = CtrlHomePage.get_selected_item()  
        self.func_num = 1
        if select_item == 0:
            self.func_num = 1
        elif select_item == 1:
            self.func_num = 1
        elif select_item == 2:
            self.func_num = 3
        elif select_item == 3:
            self.func_num = 2
        elif select_item == 4:
            self.func_num = 5
        elif select_item == 5:
            self.func_num = 3 
            
        x, y = self.GetSize()
        btn_y = ((y - 50) - 100) / 2
        btn_x = ((x - 200) - ((self.func_num * 100) + ((self.func_num - 1) * 10))) / 2
        for i in range(self.func_num):
            self.di_funcButtons[i].Move(wx.Point(btn_x + (i*110), btn_y))
            self.di_funcButtons[i].SetSize(wx.Size(100, 100))

    def _set_screen_tile(self):
        select_item = CtrlHomePage.get_selected_item()  
        self.GetParent().SetTitle(li_title[select_item])

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = WgtHomePage(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()
