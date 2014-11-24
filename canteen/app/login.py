#!/usr/bin/env python
# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
from app.home_logic import CtrlHomePage
from framework.core import EvtManager
from app.enum_event import EnumEvent
from app.app_manager import AppManager

import wx
import wx.xrc
import sys

from framework.img_button import ImgButton

###########################################################################
## Class WgtLogin
###########################################################################


class WgtLogin(wx.Panel):
    def _init_keyboard_sizer(self):
        self.key_1 = ImgButton(self, u"key_1.png", u"s_key_1.png", "", wx.Colour(255, 163, 16))
        self.key_2 = ImgButton(self, u"key_2.png", u"s_key_2.png", "", wx.Colour(255, 163, 16))
        self.key_3 = ImgButton(self, u"key_3.png", u"s_key_3.png", "", wx.Colour(255, 163, 16))
        self.key_4 = ImgButton(self, u"key_4.png", u"s_key_4.png", "", wx.Colour(255, 163, 16))
        self.key_5 = ImgButton(self, u"key_5.png", u"s_key_5.png", "", wx.Colour(255, 163, 16))
        self.key_6 = ImgButton(self, u"key_6.png", u"s_key_6.png", "", wx.Colour(255, 163, 16))
        self.key_7 = ImgButton(self, u"key_7.png", u"s_key_7.png", "", wx.Colour(255, 163, 16))
        self.key_8 = ImgButton(self, u"key_8.png", u"s_key_8.png", "", wx.Colour(255, 163, 16))
        self.key_9 = ImgButton(self, u"key_9.png", u"s_key_9.png", "", wx.Colour(255, 163, 16))
        self.key_cancel = ImgButton(self, u"key_cancel.png", u"s_key_cancel.png", "", wx.Colour(255, 163, 16))
        self.key_0 = ImgButton(self, u"key_0.png", u"s_key_0.png", "", wx.Colour(255, 163, 16))
        self.key_back = ImgButton(self, u"key_back.png", u"s_key_back.png", "", wx.Colour(255, 163, 16))

    def _init_login_sizer(self):
        # Add user name label
        self.userLabel = ImgButton(self, u"user.png", u"user.png")
        self.userLabel.Enable(False)
        # Add user name text control
        self.txtUser = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        # Add password label
        self.passwordLabel = ImgButton(self, u"password.png", u"password.png")
        self.passwordLabel.Enable(False)
        # Add password text control
        self.txtPassword = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, wx.TE_PASSWORD)
        # Add login button
        self.btnLogin = ImgButton(self, u"btn_login.png", u"s_btn_login.png", "", wx.Colour(255, 163, 16))

    def __init__(self, parent, app_):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition,
                          size=wx.Size(495, 266), style=wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        self._init_keyboard_sizer()
        self._init_login_sizer()

        self.Layout()
        self.Centre(wx.BOTH) 
        self.focus = ''
        
        # Connect Events
        self.Bind(wx.EVT_SIZE, self.on_size)
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

        self.Bind(wx.EVT_PAINT, self.on_paint)
        #self.Bind(wx.EVT_ERASE_BACKGROUND, self.on_erase_background)

        # application type
        self.app = app_
    
    def __del__(self):
        pass
    
    def initialize(self):
        # Add event listener
        EvtManager.add_listener(self, EnumEvent.EVT_LOGIN, self.on_evt_login)
        
        self.GetParent().SetTitle(u"登陆")
        x, y = CtrlHomePage.get_instance().get_screen_size()
        self.SetSize(wx.Size(x, y))

    def un_initialize(self):
        # Remove event listener
        EvtManager.remove_listener(self, EnumEvent.EVT_LOGIN, self.on_evt_login)

    # Virtual event handlers, override them in your derived class
    def on_paint(self, event):
        dc = wx.ClientDC(self)
        dc.Clear()

        sz = self.GetClientSize()
        bg_img = wx.Image(sys.path[0] + "\\..\\image\\login_bg.jpg", wx.BITMAP_TYPE_JPEG).Scale(sz.x, sz.y)
        bg_bmp = bg_img.ConvertToBitmap()

        mem_dc = wx.MemoryDC()
        mem_dc.SelectObject(bg_bmp)
        dc.Blit(0, 0,
                bg_bmp.GetWidth(), bg_bmp.GetHeight(),
                mem_dc, 0, 0, wx.COPY, True)

    def on_erase_background(self, event):
        #dc = event.GetDC()
        #if not dc:
        dc = wx.ClientDC(self)
        #rect = self.GetUpdateRegion().GetBox()
        #dc.SetClippingRect(rect)
        dc.Clear()

        sz = self.GetClientSize()
        bg_img = wx.Image(sys.path[0] + "\\..\\image\\login_bg.jpg", wx.BITMAP_TYPE_JPEG).Scale(sz.x, sz.y)
        bg_bmp = bg_img.ConvertToBitmap()
        #dc.DrawBitmap(bg_bmp, 0, 0)

        #bmp = wx.Bitmap(sys.path[0] + "\\..\\image\\login_bg.jpg").
        mem_dc = wx.MemoryDC()
        mem_dc.SelectObject(bg_bmp)
        dc.Blit(0, 0,
                bg_bmp.GetWidth(), bg_bmp.GetHeight(),
                mem_dc, 0, 0, wx.COPY, True)

    def on_size(self, event):
        event.Skip()
        x, y = self.GetClientSize()
        start_x = x / 2 - 190
        start_y = y * 4 / 9

        btn_w = 62
        btn_h = 48
        btn_size = wx.Size(btn_w, btn_h)
        self.key_1.SetPosition(wx.Point(start_x, start_y))
        self.key_1.SetSize(btn_size)

        self.key_2.SetPosition(wx.Point(start_x + btn_w, start_y))
        self.key_2.SetSize(btn_size)

        self.key_3.SetPosition(wx.Point(start_x + (btn_w * 2), start_y))
        self.key_3.SetSize(btn_size)

        self.key_4.SetPosition(wx.Point(start_x, start_y + btn_h))
        self.key_4.SetSize(btn_size)

        self.key_5.SetPosition(wx.Point(start_x + btn_w, start_y + btn_h))
        self.key_5.SetSize(btn_size)

        self.key_6.SetPosition(wx.Point(start_x + (btn_w * 2), start_y + btn_h))
        self.key_6.SetSize(btn_size)

        self.key_7.SetPosition(wx.Point(start_x, start_y + (btn_h * 2)))
        self.key_7.SetSize(btn_size)

        self.key_8.SetPosition(wx.Point(start_x + btn_w, start_y + (btn_h * 2)))
        self.key_8.SetSize(btn_size)

        self.key_9.SetPosition(wx.Point(start_x + (btn_w * 2), start_y + (btn_h * 2)))
        self.key_9.SetSize(btn_size)

        self.key_cancel.SetPosition(wx.Point(start_x, start_y + (btn_h * 3)))
        self.key_cancel.SetSize(btn_size)

        self.key_0.SetPosition(wx.Point(start_x + btn_w, start_y + (btn_h * 3)))
        self.key_0.SetSize(btn_size)

        self.key_back.SetPosition(wx.Point(start_x + (btn_w * 2), start_y + (btn_h * 3)))
        self.key_back.SetSize(btn_size)

        self.userLabel.SetSize(wx.Size(80, 25))
        self.userLabel.SetPosition(wx.Point(start_x + 200, start_y + 60))

        self.txtUser.SetPosition(wx.Point(start_x + 280, start_y + 60))
        self.txtPassword.SetTransparent(0)

        self.passwordLabel.SetSize(wx.Size(80, 25))
        self.passwordLabel.SetPosition(wx.Point(start_x + 200, start_y + 100))

        self.txtPassword.SetPosition(wx.Point(start_x + 280, start_y + 100))
        self.txtPassword.SetTransparent(255)

        self.btnLogin.SetSize(wx.Size(102, 32))
        self.btnLogin.SetPosition(wx.Point(start_x + 245, start_y + 140))

        self.Refresh()

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
        self.GetParent().Destroy()
    
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
        if self.app == 'manager':
            from app.manager.logic.ctrl import CtrlManagerLogin
            CtrlManagerLogin.get_instance().login(self.txtUser.GetValue(), self.txtPassword.GetValue())
        elif self.app == 'front':
            from app.front.logic.ctrl import CtrlFrontLogin
            CtrlFrontLogin.get_instance().login(self.txtUser.GetValue(), self.txtPassword.GetValue())
        
    def on_set_user_focus(self, event):
        event.Skip()
        self.focus = 'User'
        
    def on_set_password_focus(self, event):
        event.Skip()
        self.focus = 'Password'
        
    def on_evt_login(self, event):
        event.Skip()
        if self.app == 'manager':
            from app.manager.logic.ctrl import CtrlManagerLogin
            if CtrlManagerLogin.get_instance().get_result():
                AppManager.get_instance().switch_to_application('HomePage')
            else:
                dlg = wx.MessageDialog(self, u"用户名或密码错误", caption=u"登陆")
                dlg.ShowModal()
        elif self.app == 'front':
            from app.front.logic.ctrl import CtrlFrontLogin
            if CtrlFrontLogin.get_instance().get_result():
                AppManager.get_instance().switch_to_application('FrontPage')
            else:
                dlg = wx.MessageDialog(self, u"用户名或密码错误", caption=u"登陆")
                dlg.ShowModal()

    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = WgtLogin(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()
