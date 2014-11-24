#!/usr/bin/env python
# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
from app.manager.UI.sys_setting import *
from app.app_manager import AppManager
from app.home_logic import CtrlHomePage
from framework.img_button import ImgButton
from framework.img_any_button import ImgAnyButton

import wx
import wx.xrc
import sys

###########################################################################
## Class PopPassword
###########################################################################


class PopPassword (wx.Dialog):
    def _init_ui(self, parent):
        parent.Add(wx.BoxSizer(wx.VERTICAL), 1, wx.EXPAND, 5)
        parent.Add(wx.BoxSizer(wx.VERTICAL), 1, wx.EXPAND, 5)

        # Add current password sizer
        cur_siser = wx.BoxSizer(wx.HORIZONTAL)

        self.sTxtCur = wx.StaticText(self, wx.ID_ANY, u"当前密码：", wx.DefaultPosition, wx.Size(200, -1), wx.ALIGN_RIGHT)
        self.sTxtCur.Wrap(-1)
        cur_siser.Add(self.sTxtCur, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtCurPassword = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
        cur_siser.Add(self.txtCurPassword, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        parent.Add(cur_siser, 1, wx.EXPAND, 5)
        # Add new password sizer
        new_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.sTxtNew = wx.StaticText(self, wx.ID_ANY, u"新密码：", wx.DefaultPosition, wx.Size(200, -1), wx.ALIGN_RIGHT)
        self.sTxtNew.Wrap(-1)
        new_sizer.Add(self.sTxtNew, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtNewPassword = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
        new_sizer.Add(self.txtNewPassword, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        parent.Add(new_sizer, 1, wx.EXPAND, 5)
        # Add new password verify sizer
        verify_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.sTxtVerify = wx.StaticText(self, wx.ID_ANY, u"确认新密码：", wx.DefaultPosition, wx.Size(200, -1), wx.ALIGN_RIGHT)
        self.sTxtVerify.Wrap(-1)
        verify_sizer.Add(self.sTxtVerify, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtVerifyPassword = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
        verify_sizer.Add(self.txtVerifyPassword, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        parent.Add(verify_sizer, 1, wx.EXPAND, 5)
        #Add control button
        ctrl_sizer = wx.BoxSizer(wx.HORIZONTAL)
        ctrl_sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        self.btnOk = wx.Button(self, wx.ID_ANY, u"确认", wx.DefaultPosition, wx.DefaultSize, 0)
        ctrl_sizer.Add(self.btnOk, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.btnCancel = wx.Button(self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0)
        ctrl_sizer.Add(self.btnCancel, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        ctrl_sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        parent.Add(ctrl_sizer, 1, wx.EXPAND, 5)

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"密码设置", pos=wx.DefaultPosition,
                           size=wx.Size(600, 400), style=wx.CAPTION)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        g_sizer = wx.GridSizer(8, 1, 0, 0)
        self._init_ui(g_sizer)

        self.SetSizer(g_sizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.btnOk.Bind(wx.EVT_BUTTON, self.on_btn_ok)
        self.btnCancel.Bind(wx.EVT_BUTTON, self.on_btn_cancel)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def on_btn_ok(self, event):
        event.Skip()

    def on_btn_cancel(self, event):
        event.Skip()
        self.Close()

###########################################################################
## Class WgtDeskTop
###########################################################################

li_func_widget_1 = ['DiningTable', 'DishesPublish', 'Employee', 'PrinterScheme', '', 'Company']
li_func_widget_2 = ['', '', 'UserPermission', 'SchemeRelated', '', 'Register']

li_title = [u"餐厅管理", u"菜品管理", u"员工管理", u"打印设置", u"报表中心", u"系统设置"]
li_func_img_1 = [(u"table.png", u"s_table.png"), (u"dishes_publish.png", u"s_dishes_publish.png"),
                 (u"employee_man.png", u"s_employee_man.png"), (u"print_scheme.png", u"s_print_scheme.png"),
                 (u"sale_info.png", u"s_sale_info.png"), (u"company.png", u"s_company.png")]
li_func_img_2 = [None, None, (u"role_man.png", u"s_role_man.png"), (u"dishes_relation.png", u"s_dishes_relation.png"),
                 (u"money_info.png", u"s_money_info.png"), (u"register.png", u"s_register.png")]
#li_func_title_3 = [(u"area_setting.png", u"s_area_setting.png"), (u"dishes_unit.png", u"s_dishes_unit.png"),
#                   (u"work_schedule.png", u"s_work_schedule.png"), None,
#                   (u"business_status.png", u"s_business_status.png"), (u"backup.png", u"s_backup.png")]
li_func_img_3 = [None, None, None, None,
                 (u"business_status.png", u"s_business_status.png"), None]
li_func_img_4 = [None, None, None, None, (u"consume.png", u"s_consume.png"), None]
li_func_img_5 = [None, None, None, None, (u"billboard.png", u"s_billboard.png"), None]
li_func_img_6 = [None, None, None, None, None, None]

li_func_images = [li_func_img_1, li_func_img_2, li_func_img_3,
                  li_func_img_4, li_func_img_5, li_func_img_6]

li_func_title_1 = [u'餐桌设置', u'菜品发布', u'员工管理', u'厨打方案', u'菜品销售查询', u'公司信息']
li_func_title_2 = [u'', u'', u'权限管理', u'菜品关联', u'收银情况查询', u'注册']
#li_func_title_3 = [u'区域设置', u'菜品单位设置', u'员工排班', u'', u'营业情况查询', u'数据备份']
li_func_title_3 = [u'', u'', u'', u'', u'营业情况查询', u'']
li_func_title_4 = [u'', u'', u'', u'', u'消费查询', u'']
li_func_title_5 = [u'', u'', u'', u'', u'菜品排行榜', u'']
li_func_title_6 = [u'', u'', u'', u'', u'', u'']
li_func_titles = [li_func_title_1, li_func_title_2, li_func_title_3,
                  li_func_title_4, li_func_title_5, li_func_title_6]


def get_func_number(index):
    func_num = 0
    for li_func_title in li_func_titles:
        if li_func_title[index] != u'':
            func_num += 1

    return func_num


class WgtHomePage (wx.Panel):
    def _init_status_bar_sizer(self, parent):
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Add status bar panel
        #sizer.SetMinSize(wx.Size(-1, 82))
        self.logoPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.logoPanel.SetMinSize(wx.Size(800, 82))

        sizer.Add(self.logoPanel, 1, wx.EXPAND, 5)
        parent.Add(sizer, 1, wx.EXPAND, 5)
        
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
        self.selectorPanel.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))

        # Add system setting button
        self.btnSysSetting = ImgButton(self.selectorPanel, u"sys_setting.png", u"s_sys_setting.png", "", None)
        # Add dining room setting button
        self.btnDiningRoomSetting = ImgButton(self.selectorPanel, u"dining.png", u"s_dining.png", "", None)
        # Add dishes publish button
        self.btnDishesPublishing = ImgButton(self.selectorPanel, u"dishes.png", u"s_dishes.png", "", None)
        # Add employee manager button
        self.btnStaffMan = ImgButton(self.selectorPanel, u"employee.png", u"s_employee.png", "", None)
        # Add printer setting button
        self.btnPrinter = ImgButton(self.selectorPanel, u"printing.png", u"s_printing.png", "", None)
        # Add report forms button
        self.btnReportForms = ImgButton(self.selectorPanel, u"report.png", u"s_report.png", "", None)
        # Add report forms button
        self.btnModifyPassword = ImgButton(self.selectorPanel, u"pwd_setting.png", u"s_pwd_setting.png", "", None)
        # Add exit button
        self.btnExit = ImgButton(self.selectorPanel, u"exit.png", u"s_exit.png", "", None)
        
        # Layout selector buttons
        self.selectorPanel.Layout()
        sizer.Add(self.selectorPanel, 1, wx.EXPAND | wx.RIGHT, 5)
        parent.Add(sizer, 1, 0, 5)
        
    def _init_func_widget_sizer(self, parent):
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.SetMinSize(wx.Size(600, 750)) 
        
        # Function widget panel initialize
        self.funcPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.funcPanel.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        self.funcPanel.SetMinSize(wx.Size(800, 600))
        
        func_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # Define function buttons dictionary
        self.di_funcButtons = dict()
        # Add function 1
        self.btnFunc_1 = ImgAnyButton(self.funcPanel)
        func_btn_item_1 = {0: self.btnFunc_1}
        self.di_funcButtons.update(func_btn_item_1)
        # Add function 2
        self.btnFunc_2 = ImgAnyButton(self.funcPanel)
        func_btn_item_2 = {1: self.btnFunc_2}
        self.di_funcButtons.update(func_btn_item_2)
        # Add function 3
        self.btnFunc_3 = ImgAnyButton(self.funcPanel)
        func_btn_item_3 = {2: self.btnFunc_3}
        self.di_funcButtons.update(func_btn_item_3)
        # Add function 4
        self.btnFunc_4 = ImgAnyButton(self.funcPanel)
        func_btn_item_4 = {3: self.btnFunc_4}
        self.di_funcButtons.update(func_btn_item_4)
        # Add function 5
        self.btnFunc_5 = ImgAnyButton(self.funcPanel)
        func_btn_item_5 = {4: self.btnFunc_5}
        self.di_funcButtons.update(func_btn_item_5)
        # Add function 6
        self.btnFunc_6 = ImgAnyButton(self.funcPanel)
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
        self.SetBackgroundColour(wx.Colour(0x51, 0x1c, 0x0a))

        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_status_bar_sizer(sizer)
        self._init_screen_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_PAINT, self.on_logo_paint)
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.btnDiningRoomSetting.Bind(wx.EVT_BUTTON, self.on_dining_room_setting)
        self.btnDishesPublishing.Bind(wx.EVT_BUTTON, self.on_dishes_publishing)
        self.btnStaffMan.Bind(wx.EVT_BUTTON, self.on_employee_manager)
        self.btnPrinter.Bind(wx.EVT_BUTTON, self.on_printer_setting)
        self.btnReportForms.Bind(wx.EVT_BUTTON, self.on_report_forms)
        self.btnSysSetting.Bind(wx.EVT_BUTTON, self.on_system_setting)
        self.btnModifyPassword.Bind(wx.EVT_BUTTON, self.on_modify_password)
        self.btnExit.Bind(wx.EVT_BUTTON, parent.on_exit)
        self.btnFunc_1.Bind(wx.EVT_BUTTON, self.on_func_1)
        self.btnFunc_2.Bind(wx.EVT_BUTTON, self.on_func_2)
        self.btnFunc_3.Bind(wx.EVT_BUTTON, self.on_func_3)
        self.btnFunc_4.Bind(wx.EVT_BUTTON, self.on_func_4)
        self.btnFunc_5.Bind(wx.EVT_BUTTON, self.on_func_5)
        self.btnFunc_6.Bind(wx.EVT_BUTTON, self.on_func_6)

        # Create function button list
        self.func_num = 0
        self.li_buttons = [self.btnDiningRoomSetting, self.btnDishesPublishing, self.btnStaffMan,
                           self.btnPrinter, self.btnReportForms, self.btnSysSetting]
        self.liFuncButtons = [self.btnFunc_1, self.btnFunc_2, self.btnFunc_3,
                              self.btnFunc_4, self.btnFunc_5, self.btnFunc_6]

    def __del__(self):
        pass

    # Override function, initialize user interface
    def initialize(self):
        x, y = CtrlHomePage.get_instance().get_screen_size()
        self.SetSize(wx.Size(x, y))

        select_item = CtrlHomePage.get_instance().get_selected_item()
        self._show_func_widget(select_item)

    # Override function un initialize user interface
    def un_initialize(self):
        pass

    # Virtual event handlers, override them in your derived class
    def on_logo_paint(self, event):
        dc = wx.ClientDC(self.logoPanel)
        dc.Clear()

        sz = self.logoPanel.GetClientSize()
        bg_img = wx.Image(sys.path[0] + "\\..\\image\\logo.png", wx.BITMAP_TYPE_PNG).Scale(sz.x, 82)
        bg_bmp = bg_img.ConvertToBitmap()

        mem_dc = wx.MemoryDC()
        mem_dc.SelectObject(bg_bmp)
        dc.Blit(0, 0,
                bg_bmp.GetWidth(), bg_bmp.GetHeight(),
                mem_dc, 0, 0, wx.COPY, True)

    def on_size(self, event):
        event.Skip()
        x, y = self.GetSize()

        self.logoPanel.SetSize(wx.Size(x, 82))
        self.selectorPanel.SetSize(wx.Size(200, y-82))
        self.funcPanel.SetMinSize(wx.Size(x-200, y-82))

        start_x = 15
        start_y = (y - 82 - (8 * 51)) / 2
        btn_w = 162
        btn_h = 46
        btn_size = wx.Size(btn_w, btn_h)
        self.btnSysSetting.SetPosition(wx.Point(start_x, start_y))
        self.btnSysSetting.SetSize(btn_size)

        self.btnDiningRoomSetting.SetPosition(wx.Point(start_x, start_y + btn_h + 5))
        self.btnDiningRoomSetting.SetSize(btn_size)

        self.btnDishesPublishing.SetPosition(wx.Point(start_x, start_y + ((btn_h + 5) * 2)))
        self.btnDishesPublishing.SetSize(btn_size)

        self.btnStaffMan.SetPosition(wx.Point(start_x, start_y + ((btn_h + 5) * 3)))
        self.btnStaffMan.SetSize(btn_size)

        self.btnPrinter.SetPosition(wx.Point(start_x, start_y + ((btn_h + 5) * 4)))
        self.btnPrinter.SetSize(btn_size)

        self.btnReportForms.SetPosition(wx.Point(start_x, start_y + ((btn_h + 5) * 5)))
        self.btnReportForms.SetSize(btn_size)

        self.btnModifyPassword.SetPosition(wx.Point(start_x, start_y + ((btn_h + 5) * 6)))
        self.btnModifyPassword.SetSize(btn_size)

        self.btnExit.SetPosition(wx.Point(start_x, start_y + ((btn_h + 5) * 7)))
        self.btnExit.SetSize(btn_size)

        self._show_func_buttons()

    def on_dining_room_setting(self, event):
        event.Skip()
        CtrlHomePage.get_instance().set_selected_item(0)
        self._show_func_widget(0)

    def on_dishes_publishing(self, event):
        event.Skip()
        CtrlHomePage.get_instance().set_selected_item(1)
        self._show_func_widget(1)

    def on_employee_manager(self, event):
        event.Skip()
        CtrlHomePage.get_instance().set_selected_item(2)
        self._show_func_widget(2)

    def on_printer_setting(self, event):
        event.Skip()
        CtrlHomePage.get_instance().set_selected_item(3)
        self._show_func_widget(3)

    def on_report_forms(self, event):
        event.Skip()
        CtrlHomePage.get_instance().set_selected_item(4)
        self._show_func_widget(4)

    def on_system_setting(self, event):
        event.Skip()
        CtrlHomePage.get_instance().set_selected_item(5)
        self._show_func_widget(5)

    def on_modify_password(self, event):
        event.Skip()
        pop_password = PopPassword(self)
        pop_password.ShowModal()

    def on_func_1(self, event):
        event.Skip()
        select_item = CtrlHomePage.get_instance().get_selected_item()
        AppManager.get_instance().set_app_title(li_func_title_1[select_item])
        self._set_screen_tile()
        if select_item == 1:
            pop_company = PopCompany(self)
            pop_company.ShowModal()
        elif select_item == 5:
            pop_company = PopCompany(self)
            pop_company.ShowModal()
        else:
            AppManager.get_instance().switch_to_application(li_func_widget_1[select_item])

    def on_func_2(self, event):
        event.Skip()
        select_item = CtrlHomePage.get_instance().get_selected_item()
        AppManager.get_instance().set_app_title(li_func_title_2[select_item])
        self._set_screen_tile()
        if select_item != 5:
            AppManager.get_instance().switch_to_application(li_func_widget_2[select_item])
        else:
            pop_register = PopRegister(self)
            pop_register.ShowModal()

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

    def _show_func_widget(self, index):
        self._enable_all_selector()
        self._hide_all_func_buttons()
        (self.li_buttons[index]).Enabled = False
        if get_func_number(index) == 1:
            AppManager.get_instance().set_app_title(li_func_title_1[index])
            AppManager.get_instance().switch_to_application(li_func_widget_1[index])
        else:
            AppManager.get_instance().set_app_title(li_title[index])
            self._show_function_buttons(index)

        self._set_screen_tile()
        self._show_func_buttons()

    def _show_function_buttons(self, index):
        func_button_index = 0
        for li_func_img in li_func_images:
            if li_func_img[index] is not None:
                (self.liFuncButtons[func_button_index]).Show()
                (self.liFuncButtons[func_button_index]).set_label(li_func_img[index][0], li_func_img[index][1])
                (self.liFuncButtons[func_button_index]).SetSize(wx.Size(142, 142))
            func_button_index += 1

    def _enable_all_selector(self):
        self.btnDiningRoomSetting.Enabled = True
        self.btnDishesPublishing.Enabled = True
        self.btnStaffMan.Enabled = True
        self.btnPrinter.Enabled = True
        self.btnReportForms.Enabled = False
        self.btnReportForms.SetBackgroundColour(wx.YELLOW)
        self.btnReportForms.SetForegroundColour(wx.YELLOW)
        self.btnSysSetting.Enabled = True
        self.btnModifyPassword.Enabled = True

    def _hide_all_func_buttons(self):
        self.btnFunc_1.Hide()
        self.btnFunc_2.Hide()
        self.btnFunc_3.Hide()
        self.btnFunc_4.Hide()
        self.btnFunc_5.Hide()
        self.btnFunc_6.Hide()    

    def _show_func_buttons(self):
        select_item = CtrlHomePage.get_instance().get_selected_item()
        self.func_num = get_func_number(select_item)
            
        x, y = self.GetSize()
        btn_y = ((y - 82) - 150) / 2
        btn_x = ((x - 200) - ((self.func_num * 150) + ((self.func_num - 1) * 10))) / 2
        for i in range(self.func_num):
            self.di_funcButtons[i].Move(wx.Point(btn_x + (i*150), btn_y))
            self.di_funcButtons[i].SetSize(wx.Size(142, 142))

    def _set_screen_tile(self):
        self.GetParent().SetTitle(AppManager.get_instance().get_app_title())

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = WgtHomePage(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()
