# -*- coding: utf-8 -*- 
#!/usr/bin/env python

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from app.logic.login.CDataLogin import CDataLogin
from framework.core import EvtManager
from app.logic.CEnumEvent import CEnumEvent
from app.CAppManager import CAppManager

###########################################################################
## Class CWgtLogin
###########################################################################

class CWgtLogin(wx.Panel):
    def _init_keyboard_sizer(self, parent):
        sizer = wx.GridSizer(1, 1, 0, 0)

        keyboardSizer = wx.FlexGridSizer(4, 3, 0, 0)
        keyboardSizer.SetFlexibleDirection(wx.BOTH)
        keyboardSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        # Add key 1
        self.key_1 = wx.Button(self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0)
        self.key_1.SetMinSize(wx.Size(60,50))
        keyboardSizer.Add(self.key_1, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 5)
        # Add key 2
        self.key_2 = wx.Button(self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0)
        self.key_2.SetMinSize(wx.Size(60,50))
        keyboardSizer.Add(self.key_2, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.RIGHT|wx.LEFT|wx.EXPAND, 5)
        # Add key 3
        self.key_3 = wx.Button(self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0)
        self.key_3.SetMinSize(wx.Size(60,50))
        keyboardSizer.Add(self.key_3, 0, wx.TOP|wx.LEFT|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5)
        # Add key 4
        self.key_4 = wx.Button(self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0)
        self.key_4.SetMinSize(wx.Size(60,50))
        keyboardSizer.Add(self.key_4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.RIGHT|wx.LEFT, 5)
        # Add key 5
        self.key_5 = wx.Button(self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0)
        self.key_5.SetMinSize(wx.Size(60,50))
        keyboardSizer.Add(self.key_5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.RIGHT|wx.LEFT, 5)
        # Add key 6
        self.key_6 = wx.Button(self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0)
        self.key_6.SetMinSize(wx.Size(60,50))
        keyboardSizer.Add(self.key_6, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.LEFT, 5)
        # Add key 7
        self.key_7 = wx.Button(self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0)
        self.key_7.SetMinSize(wx.Size(60,50))
        keyboardSizer.Add(self.key_7, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.RIGHT|wx.LEFT, 5)
        # Add key 8
        self.key_8 = wx.Button(self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0)
        self.key_8.SetMinSize(wx.Size(60,50))
        keyboardSizer.Add(self.key_8, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.RIGHT|wx.LEFT, 5)
        # Add key 9
        self.key_9 = wx.Button(self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0)
        self.key_9.SetMinSize(wx.Size(60,50))
        keyboardSizer.Add(self.key_9, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.LEFT, 5)
        # Add key cancel
        self.key_cancel = wx.Button(self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0)
        self.key_cancel.SetMinSize(wx.Size(60,50))
        keyboardSizer.Add(self.key_cancel, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.RIGHT|wx.LEFT, 5)
        # Add key 0
        self.key_0 = wx.Button(self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.key_0.SetMinSize(wx.Size(60,50))
        keyboardSizer.Add(self.key_0, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.RIGHT|wx.LEFT, 5)
        # Add key back
        self.key_back = wx.Button(self, wx.ID_ANY, u"退格", wx.DefaultPosition, wx.DefaultSize, 0)
        self.key_back.SetMinSize(wx.Size(60,50))   
        keyboardSizer.Add(self.key_back, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.LEFT, 5)

        # Layout keyboard 
        sizer.Add(keyboardSizer, 1, wx.EXPAND, 5)
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_login_sizer(self, parent):
        gSizer = wx.GridSizer(3, 1, 0, 0)

        # Add spacer sizer
        spacer = wx.BoxSizer(wx.VERTICAL)
        gSizer.Add(spacer, 1, wx.EXPAND, 5)

        # Add login info sizer
        loginSizer = wx.FlexGridSizer(2, 2, 0, 0)
        loginSizer.SetFlexibleDirection(wx.BOTH)
        loginSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        # Add user name label
        sTxtUser = wx.StaticText(self, wx.ID_ANY, u"用户名：", wx.DefaultPosition, wx.DefaultSize, 0)
        sTxtUser.Wrap(-1)
        loginSizer.Add(sTxtUser, 0, wx.ALL, 5)
        # Add user name text control
        self.txtUser = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        loginSizer.Add(self.txtUser, 0, wx.ALL|wx.ALIGN_RIGHT, 5)
        # Add password label
        sTxtPassword = wx.StaticText(self, wx.ID_ANY, u"密码：", wx.DefaultPosition, wx.DefaultSize, 0)
        sTxtPassword.Wrap(-1)
        loginSizer.Add(sTxtPassword, 0, wx.ALL, 5)
        # Add password text control
        self.txtPassword = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD)
        loginSizer.Add(self.txtPassword, 0, wx.ALL, 5)
        # Layout login info sizer
        gSizer.Add(loginSizer, 1, wx.EXPAND, 5)

        # Add login buttons sizer
        btnSizer = wx.GridSizer(1, 3, 0, 0)
        # Add a spacer on left
        btnLeftSpacer = wx.BoxSizer(wx.VERTICAL)
        btnSizer.Add(btnLeftSpacer, 1, wx.EXPAND, 5)
        # Add login button 
        btnLoginSizer = wx.BoxSizer(wx.VERTICAL)
        self.btnLogin = wx.Button(self, wx.ID_ANY, u"登录", wx.DefaultPosition, wx.DefaultSize, 0)
        btnLoginSizer.Add(self.btnLogin, 0, wx.ALL, 5)
        btnSizer.Add(btnLoginSizer, 1, wx.EXPAND, 5)
        # Add a spacer on right
        btnRightSpacer = wx.GridSizer(0, 2, 0, 0)
        btnSizer.Add(btnRightSpacer, 1, wx.EXPAND, 5)
        
        # Layout login sizer
        gSizer.Add(btnSizer, 1, wx.EXPAND, 5)
        parent.Add(gSizer, 1, wx.EXPAND, 5)

    def __init__( self, parent ):
        wx.Panel.__init__ (self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(495,266), style=wx.TAB_TRAVERSAL)
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
        self.key_1.Bind(wx.EVT_LEFT_DOWN, self.OnKey_1)
        self.key_2.Bind(wx.EVT_LEFT_DOWN, self.OnKey_2)
        self.key_3.Bind(wx.EVT_LEFT_DOWN, self.OnKey_3)
        self.key_4.Bind(wx.EVT_LEFT_DOWN, self.OnKey_4)
        self.key_5.Bind(wx.EVT_LEFT_DOWN, self.OnKey_5)
        self.key_6.Bind(wx.EVT_LEFT_DOWN, self.OnKey_6)
        self.key_7.Bind(wx.EVT_LEFT_DOWN, self.OnKey_7)
        self.key_8.Bind(wx.EVT_LEFT_DOWN, self.OnKey_8)
        self.key_9.Bind(wx.EVT_LEFT_DOWN, self.OnKey_9)
        self.key_cancel.Bind(wx.EVT_LEFT_DOWN, self.OnKeyCancel)
        self.key_0.Bind(wx.EVT_LEFT_DOWN, self.OnKey_0)
        self.key_back.Bind(wx.EVT_LEFT_DOWN, self.OnKeyBack)
        self.btnLogin.Bind(wx.EVT_LEFT_DOWN, self.OnLogin)
        
        self.txtUser.Bind(wx.EVT_SET_FOCUS, self.OnSetUserFocus)
        self.txtPassword.Bind(wx.EVT_SET_FOCUS, self.OnSetPasswdFocus)
    
    def __del__(self):
        pass
    
    def Initailize(self):
        # Add event listener
        EvtManager.AddListener(self, CEnumEvent.EVT_LOGIN, self.OnEvtLogin)
        
        self.GetParent().SetTitle(u"登陆")

    def Uninitailize(self):
        # Remove event listener
        EvtManager.RemoveListener(self, CEnumEvent.EVT_LOGIN, self.OnEvtLogin)
    
        
    # Virtual event handlers, override them in your derived class
    def OnKey_1(self, event):
        event.Skip()
        if self.focus == 'User':
            self.txtUser.AppendText('1')
        elif self.focus == 'Passwd':
            self.txtPassword.AppendText('1')
    
    def OnKey_2(self, event):
        event.Skip()
        if self.focus == 'User':
            self.txtUser.AppendText('2')
        elif self.focus == 'Passwd':
            self.txtPassword.AppendText('2')
    
    def OnKey_3(self, event):
        event.Skip()
        if self.focus == 'User':
            self.txtUser.AppendText('3')
        elif self.focus == 'Passwd':
            self.txtPassword.AppendText('3')
    
    def OnKey_4(self, event):
        event.Skip()
        if self.focus == 'User':
            self.txtUser.AppendText('4')
        elif self.focus == 'Passwd':
            self.txtPassword.AppendText('4')
    
    def OnKey_5(self, event):
        event.Skip()
        if self.focus == 'User':
            self.txtUser.AppendText('5')
        elif self.focus == 'Passwd':
            self.txtPassword.AppendText('5')
    
    def OnKey_6(self, event):
        event.Skip()
        if self.focus == 'User':
            self.txtUser.AppendText('6')
        elif self.focus == 'Passwd':
            self.txtPassword.AppendText('6')
    
    def OnKey_7(self, event):
        event.Skip()
        if self.focus == 'User':
            self.txtUser.AppendText('7')
        elif self.focus == 'Passwd':
            self.txtPassword.AppendText('7')
    
    def OnKey_8(self, event):
        event.Skip()
        if self.focus == 'User':
            self.txtUser.AppendText('8')
        elif self.focus == 'Passwd':
            self.txtPassword.AppendText('8')
    
    def OnKey_9(self, event):
        event.Skip()
        if self.focus == 'User':
            self.txtUser.AppendText('9')
        elif self.focus == 'Passwd':
            self.txtPassword.AppendText('9')
    
    def OnKeyCancel(self, event):
        event.Skip()
        self.Destroy()
    
    def OnKey_0(self, event):
        event.Skip()
        if self.focus == 'User':
            self.txtUser.AppendText('0')
        elif self.focus == 'Passwd':
            self.txtPassword.AppendText('0')
    
    def OnKeyBack(self, event):
        event.Skip()
        if self.focus == 'User':
            self.txtUser.Remove(self.txtUser.GetInsertionPoint() - 1, self.txtUser.GetInsertionPoint())
        elif self.focus == 'Passwd':
            self.txtPassword.Remove(self.txtPassword.GetInsertionPoint() - 1, self.txtPassword.GetInsertionPoint())
        
    def OnLogin(self, event):
        event.Skip()
        CDataLogin().Login(self.txtUser.GetValue(), self.txtPassword.GetValue())
        
    def OnSetUserFocus(self, event):
        event.Skip()
        self.focus = 'User'
        
    def OnSetPasswdFocus(self, event):
        event.Skip()
        self.focus = 'Passwd'
        
    def OnEvtLogin(self, event):
        if CDataLogin().GetResult() == True:
            CAppManager.SwitchToApplication('DeskTop')
        else:
            dlg = wx.MessageDialog(self, u"用户名或密码错误", caption = u"登陆")
            dlg.ShowModal()
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = CWgtLogin(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()
    
