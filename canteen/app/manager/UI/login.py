#!/usr/bin/env python
# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
from app.manager.logic.ctrl import CtrlLogin
from framework.core import EvtManager
from app.manager.EnumEvent import EnumEvent
from app.manager.AppManager import AppManager

import wx
import wx.xrc

###########################################################################
## Class WgtLogin
###########################################################################


class WgtLogin(wx.Panel):
    def _init_keyboard_sizer(self, parent):
        sizer = wx.GridSizer(1, 1, 0, 0)

        keyboard_sizer = wx.FlexGridSizer(4, 3, 0, 0)
        keyboard_sizer.SetFlexibleDirection(wx.BOTH)
        keyboard_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        # Add key 1
        self.key_1 = wx.Button(self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0)
        self.key_1.SetMinSize(wx.Size(60, 50))
        keyboard_sizer.Add(self.key_1, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND | wx.TOP | wx.RIGHT | wx.LEFT, 5)
        # Add key 2
        self.key_2 = wx.Button(self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0)
        self.key_2.SetMinSize(wx.Size(60, 50))
        keyboard_sizer.Add(self.key_2, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.TOP |
                           wx.RIGHT | wx.LEFT | wx.EXPAND, 5)
        # Add key 3
        self.key_3 = wx.Button(self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0)
        self.key_3.SetMinSize(wx.Size(60, 50))
        keyboard_sizer.Add(self.key_3, 0, wx.TOP | wx.LEFT | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        # Add key 4
        self.key_4 = wx.Button(self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0)
        self.key_4.SetMinSize(wx.Size(60, 50))
        keyboard_sizer.Add(self.key_4, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP | wx.RIGHT | wx.LEFT, 5)
        # Add key 5
        self.key_5 = wx.Button(self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0)
        self.key_5.SetMinSize(wx.Size(60, 50))
        keyboard_sizer.Add(self.key_5, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP | wx.RIGHT | wx.LEFT, 5)
        # Add key 6
        self.key_6 = wx.Button(self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0)
        self.key_6.SetMinSize(wx.Size(60, 50))
        keyboard_sizer.Add(self.key_6, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP | wx.LEFT, 5)
        # Add key 7
        self.key_7 = wx.Button(self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0)
        self.key_7.SetMinSize(wx.Size(60, 50))
        keyboard_sizer.Add(self.key_7, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL |
                           wx.TOP | wx.RIGHT | wx.LEFT, 5)
        # Add key 8
        self.key_8 = wx.Button(self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0)
        self.key_8.SetMinSize(wx.Size(60, 50))
        keyboard_sizer.Add(self.key_8, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL |
                           wx.TOP | wx.RIGHT | wx.LEFT, 5)
        # Add key 9
        self.key_9 = wx.Button(self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0)
        self.key_9.SetMinSize(wx.Size(60, 50))
        keyboard_sizer.Add(self.key_9, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP | wx.LEFT, 5)
        # Add key cancel
        self.key_cancel = wx.Button(self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0)
        self.key_cancel.SetMinSize(wx.Size(60, 50))
        keyboard_sizer.Add(self.key_cancel, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP | wx.RIGHT | wx.LEFT, 5)
        # Add key 0
        self.key_0 = wx.Button(self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.key_0.SetMinSize(wx.Size(60, 50))
        keyboard_sizer.Add(self.key_0, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP | wx.RIGHT | wx.LEFT, 5)
        # Add key back
        self.key_back = wx.Button(self, wx.ID_ANY, u"退格", wx.DefaultPosition, wx.DefaultSize, 0)
        self.key_back.SetMinSize(wx.Size(60, 50))
        keyboard_sizer.Add(self.key_back, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP | wx.LEFT, 5)

        # Layout keyboard 
        sizer.Add(keyboard_sizer, 1, wx.EXPAND, 5)
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_login_sizer(self, parent):
        g_sizer = wx.GridSizer(3, 1, 0, 0)

        # Add spacer sizer
        spacer = wx.BoxSizer(wx.VERTICAL)
        g_sizer.Add(spacer, 1, wx.EXPAND, 5)

        # Add login info sizer
        login_sizer = wx.FlexGridSizer(2, 2, 0, 0)
        login_sizer.SetFlexibleDirection(wx.BOTH)
        login_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        # Add user name label
        s_txt_user = wx.StaticText(self, wx.ID_ANY, u"用户名：", wx.DefaultPosition, wx.DefaultSize, 0)
        s_txt_user.Wrap(-1)
        login_sizer.Add(s_txt_user, 0, wx.ALL, 5)
        # Add user name text control
        self.txtUser = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        login_sizer.Add(self.txtUser, 0, wx.ALL | wx.ALIGN_RIGHT, 5)
        # Add password label
        s_txt_password = wx.StaticText(self, wx.ID_ANY, u"密码：", wx.DefaultPosition, wx.DefaultSize, 0)
        s_txt_password.Wrap(-1)
        login_sizer.Add(s_txt_password, 0, wx.ALL, 5)
        # Add password text control
        self.txtPassword = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, wx.TE_PASSWORD)
        login_sizer.Add(self.txtPassword, 0, wx.ALL, 5)
        # Layout login info sizer
        g_sizer.Add(login_sizer, 1, wx.EXPAND, 5)

        # Add login buttons sizer
        btn_sizer = wx.GridSizer(1, 3, 0, 0)
        # Add a spacer on left
        btn_left_spacer = wx.BoxSizer(wx.VERTICAL)
        btn_sizer.Add(btn_left_spacer, 1, wx.EXPAND, 5)
        # Add login button 
        btn_login_sizer = wx.BoxSizer(wx.VERTICAL)
        self.btnLogin = wx.Button(self, wx.ID_ANY, u"登录", wx.DefaultPosition, wx.DefaultSize, 0)
        btn_login_sizer.Add(self.btnLogin, 0, wx.ALL, 5)
        btn_sizer.Add(btn_login_sizer, 1, wx.EXPAND, 5)
        # Add a spacer on right
        btn_right_spacer = wx.GridSizer(0, 2, 0, 0)
        btn_sizer.Add(btn_right_spacer, 1, wx.EXPAND, 5)

        # Layout login sizer
        g_sizer.Add(btn_sizer, 1, wx.EXPAND, 5)
        parent.Add(g_sizer, 1, wx.EXPAND, 5)

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition,
                          size=wx.Size(495, 266), style=wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DLIGHT))
        
        sizer = wx.GridSizer(1, 2, 0, 0)
        self._init_keyboard_sizer(sizer)
        self._init_login_sizer(sizer)
        
        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH) 
        self.focus = ''
        
        # Connect Events
        self.key_1.Bind(wx.EVT_LEFT_DOWN, self.on_key_1)
        self.key_2.Bind(wx.EVT_LEFT_DOWN, self.on_key_2)
        self.key_3.Bind(wx.EVT_LEFT_DOWN, self.on_key_3)
        self.key_4.Bind(wx.EVT_LEFT_DOWN, self.on_key_4)
        self.key_5.Bind(wx.EVT_LEFT_DOWN, self.on_key_5)
        self.key_6.Bind(wx.EVT_LEFT_DOWN, self.on_key_6)
        self.key_7.Bind(wx.EVT_LEFT_DOWN, self.on_key_7)
        self.key_8.Bind(wx.EVT_LEFT_DOWN, self.on_key_8)
        self.key_9.Bind(wx.EVT_LEFT_DOWN, self.on_key_9)
        self.key_cancel.Bind(wx.EVT_LEFT_DOWN, self.on_key_cancel)
        self.key_0.Bind(wx.EVT_LEFT_DOWN, self.on_key_0)
        self.key_back.Bind(wx.EVT_LEFT_DOWN, self.on_key_back)
        self.btnLogin.Bind(wx.EVT_LEFT_DOWN, self.on_login)
        
        self.txtUser.Bind(wx.EVT_SET_FOCUS, self.on_set_user_focus)
        self.txtPassword.Bind(wx.EVT_SET_FOCUS, self.on_set_password_focus)
    
    def __del__(self):
        pass
    
    def initialize(self):
        # Add event listener
        EvtManager.add_listener(self, EnumEvent.EVT_LOGIN, self.on_evt_login)
        
        self.GetParent().SetTitle(u"登陆")

    def un_initialize(self):
        # Remove event listener
        EvtManager.remove_listener(self, EnumEvent.EVT_LOGIN, self.on_evt_login)

    # Virtual event handlers, override them in your derived class
    def on_key_1(self, event):
        event.Skip()
        if self.focus == 'User':
            self.txtUser.AppendText('1')
        elif self.focus == 'Password':
            self.txtPassword.AppendText('1')
    
    def on_key_2(self, event):
        event.Skip()
        if self.focus == 'User':
            self.txtUser.AppendText('2')
        elif self.focus == 'Password':
            self.txtPassword.AppendText('2')
    
    def on_key_3(self, event):
        event.Skip()
        if self.focus == 'User':
            self.txtUser.AppendText('3')
        elif self.focus == 'Password':
            self.txtPassword.AppendText('3')
    
    def on_key_4(self, event):
        event.Skip()
        if self.focus == 'User':
            self.txtUser.AppendText('4')
        elif self.focus == 'Password':
            self.txtPassword.AppendText('4')
    
    def on_key_5(self, event):
        event.Skip()
        if self.focus == 'User':
            self.txtUser.AppendText('5')
        elif self.focus == 'Password':
            self.txtPassword.AppendText('5')
    
    def on_key_6(self, event):
        event.Skip()
        if self.focus == 'User':
            self.txtUser.AppendText('6')
        elif self.focus == 'Password':
            self.txtPassword.AppendText('6')
    
    def on_key_7(self, event):
        event.Skip()
        if self.focus == 'User':
            self.txtUser.AppendText('7')
        elif self.focus == 'Password':
            self.txtPassword.AppendText('7')
    
    def on_key_8(self, event):
        event.Skip()
        if self.focus == 'User':
            self.txtUser.AppendText('8')
        elif self.focus == 'Password':
            self.txtPassword.AppendText('8')
    
    def on_key_9(self, event):
        event.Skip()
        if self.focus == 'User':
            self.txtUser.AppendText('9')
        elif self.focus == 'Password':
            self.txtPassword.AppendText('9')
    
    def on_key_cancel(self, event):
        event.Skip()
        self.Destroy()
    
    def on_key_0(self, event):
        event.Skip()
        if self.focus == 'User':
            self.txtUser.AppendText('0')
        elif self.focus == 'Password':
            self.txtPassword.AppendText('0')
    
    def on_key_back(self, event):
        event.Skip()
        if self.focus == 'User':
            self.txtUser.Remove(self.txtUser.GetInsertionPoint() - 1, self.txtUser.GetInsertionPoint())
        elif self.focus == 'Password':
            self.txtPassword.Remove(self.txtPassword.GetInsertionPoint() - 1, self.txtPassword.GetInsertionPoint())
        
    def on_login(self, event):
        event.Skip()
        CtrlLogin().login(self.txtUser.GetValue(), self.txtPassword.GetValue())
        
    def on_set_user_focus(self, event):
        event.Skip()
        self.focus = 'User'
        
    def on_set_password_focus(self, event):
        event.Skip()
        self.focus = 'Password'
        
    def on_evt_login(self, event):
        event.Skip()
        if CtrlLogin().get_result():
            AppManager.switch_to_application('HomePage')
        else:
            dlg = wx.MessageDialog(self, u"用户名或密码错误", caption=u"登陆")
            dlg.ShowModal()
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = WgtLogin(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()
