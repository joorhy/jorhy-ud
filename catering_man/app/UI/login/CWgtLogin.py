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
from framework.CEvtManager import CEvtManager
from app.logic.CEnumEvent import CEnumEvent
from app.CAppManager import CAppManager

###########################################################################
## Class CLogin
###########################################################################

class CWgtLogin ( wx.Panel ):
    
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 495,266 ), style = wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
        
        m_sizer = wx.GridSizer( 1, 2, 0, 0 )
        
        m_leftSizer = wx.GridSizer( 1, 1, 0, 0 )
        
        m_keyboxSizer = wx.FlexGridSizer( 4, 3, 0, 0 )
        m_keyboxSizer.SetFlexibleDirection( wx.BOTH )
        m_keyboxSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_key_1 = wx.Button( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_key_1.SetMinSize( wx.Size( 60,50 ) )
        
        m_keyboxSizer.Add( self.m_key_1, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
        
        self.m_key_2 = wx.Button( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_key_2.SetMinSize( wx.Size( 60,50 ) )
        
        m_keyboxSizer.Add( self.m_key_2, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
        
        self.m_key_3 = wx.Button( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_key_3.SetMinSize( wx.Size( 60,50 ) )
        
        m_keyboxSizer.Add( self.m_key_3, 0, wx.TOP|wx.LEFT|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_key_4 = wx.Button( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_key_4.SetMinSize( wx.Size( 60,50 ) )
        
        m_keyboxSizer.Add( self.m_key_4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
        
        self.m_key_5 = wx.Button( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_key_5.SetMinSize( wx.Size( 60,50 ) )
        
        m_keyboxSizer.Add( self.m_key_5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
        
        self.m_key_6 = wx.Button( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_key_6.SetMinSize( wx.Size( 60,50 ) )
        
        m_keyboxSizer.Add( self.m_key_6, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.LEFT, 5 )
        
        self.m_key_7 = wx.Button( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_key_7.SetMinSize( wx.Size( 60,50 ) )
        
        m_keyboxSizer.Add( self.m_key_7, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
        
        self.m_key_8 = wx.Button( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_key_8.SetMinSize( wx.Size( 60,50 ) )
        
        m_keyboxSizer.Add( self.m_key_8, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
        
        self.m_key_9 = wx.Button( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_key_9.SetMinSize( wx.Size( 60,50 ) )
        
        m_keyboxSizer.Add( self.m_key_9, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.LEFT, 5 )
        
        self.m_key_cancel = wx.Button( self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_key_cancel.SetMinSize( wx.Size( 60,50 ) )
        
        m_keyboxSizer.Add( self.m_key_cancel, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
        
        self.m_key_0 = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_key_0.SetMinSize( wx.Size( 60,50 ) )
        
        m_keyboxSizer.Add( self.m_key_0, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
        
        self.m_key_back = wx.Button( self, wx.ID_ANY, u"退格", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_key_back.SetMinSize( wx.Size( 60,50 ) )
        
        m_keyboxSizer.Add( self.m_key_back, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.LEFT, 5 )
        
        
        m_leftSizer.Add( m_keyboxSizer, 1, wx.EXPAND, 5 )
        
        
        m_sizer.Add( m_leftSizer, 1, wx.EXPAND, 5 )
        
        m_rightSizer = wx.GridSizer( 3, 1, 0, 0 )
        
        m_topSpaceSizer = wx.BoxSizer( wx.VERTICAL )
        
        
        m_rightSizer.Add( m_topSpaceSizer, 1, wx.EXPAND, 5 )
        
        m_loginSizer = wx.FlexGridSizer( 2, 2, 0, 0 )
        m_loginSizer.SetFlexibleDirection( wx.BOTH )
        m_loginSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_staticTxtUser = wx.StaticText( self, wx.ID_ANY, u"用户名：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTxtUser.Wrap( -1 )
        m_loginSizer.Add( self.m_staticTxtUser, 0, wx.ALL, 5 )
        
        self.m_txtUser = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        m_loginSizer.Add( self.m_txtUser, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
        
        self.m_staticTxtPassword = wx.StaticText( self, wx.ID_ANY, u"密码：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTxtPassword.Wrap( -1 )
        m_loginSizer.Add( self.m_staticTxtPassword, 0, wx.ALL, 5 )
        
        self.m_txtPassword = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
        m_loginSizer.Add( self.m_txtPassword, 0, wx.ALL, 5 )
        
        
        m_rightSizer.Add( m_loginSizer, 1, wx.EXPAND, 5 )
        
        m_btnSizer = wx.GridSizer( 1, 3, 0, 0 )
        
        m_leftSpaceSizer = wx.BoxSizer( wx.VERTICAL )
        
        
        m_btnSizer.Add( m_leftSpaceSizer, 1, wx.EXPAND, 5 )
        
        m_btnLoginSizer = wx.BoxSizer( wx.VERTICAL )
        
        self.m_btnLogin = wx.Button( self, wx.ID_ANY, u"登录", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_btnLoginSizer.Add( self.m_btnLogin, 0, wx.ALL, 5 )
        
        
        m_btnSizer.Add( m_btnLoginSizer, 1, wx.EXPAND, 5 )
        
        m_rightSpaceSizer = wx.GridSizer( 0, 2, 0, 0 )
        
        
        m_btnSizer.Add( m_rightSpaceSizer, 1, wx.EXPAND, 5 )
        
        
        m_rightSizer.Add( m_btnSizer, 1, wx.EXPAND, 5 )
        
        
        m_sizer.Add( m_rightSizer, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( m_sizer )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        self.m_focus = ''
        
        # Connect Events
        self.m_key_1.Bind( wx.EVT_LEFT_DOWN, self.OnKey_1 )
        self.m_key_2.Bind( wx.EVT_LEFT_DOWN, self.OnKey_2 )
        self.m_key_3.Bind( wx.EVT_LEFT_DOWN, self.OnKey_3 )
        self.m_key_4.Bind( wx.EVT_LEFT_DOWN, self.OnKey_4 )
        self.m_key_5.Bind( wx.EVT_LEFT_DOWN, self.OnKey_5 )
        self.m_key_6.Bind( wx.EVT_LEFT_DOWN, self.OnKey_6 )
        self.m_key_7.Bind( wx.EVT_LEFT_DOWN, self.OnKey_7 )
        self.m_key_8.Bind( wx.EVT_LEFT_DOWN, self.OnKey_8 )
        self.m_key_9.Bind( wx.EVT_LEFT_DOWN, self.OnKey_9 )
        self.m_key_cancel.Bind( wx.EVT_LEFT_DOWN, self.OnKeyCancel )
        self.m_key_0.Bind( wx.EVT_LEFT_DOWN, self.OnKey_0 )
        self.m_key_back.Bind( wx.EVT_LEFT_DOWN, self.OnKeyBack )
        self.m_btnLogin.Bind( wx.EVT_LEFT_DOWN, self.OnLogin )
        
        self.m_txtUser.Bind( wx.EVT_SET_FOCUS, self.OnSetUserFocus )
        self.m_txtPassword.Bind( wx.EVT_SET_FOCUS, self.OnSetPasswdFocus )
    
    def __del__( self ):
        pass
    
    def Initailize(self):
        # Add event listenner
        CEvtManager.AddListenner(self, CEnumEvent.EVT_LOGIN, self.OnEvtLogin)
        
        self.GetParent().SetTitle(u"登陆")

    def Uninitailize(self):
        # Remove event listenner
        CEvtManager.RemoveListenner(self, CEnumEvent.EVT_LOGIN, self.OnEvtLogin)
    
        
    # Virtual event handlers, overide them in your derived class
    def OnKey_1( self, event ):
        event.Skip()
        if self.m_focus == 'User':
            self.m_txtUser.AppendText('1')
        elif self.m_focus == 'Passwd':
            self.m_txtPassword.AppendText('1')
    
    def OnKey_2( self, event ):
        event.Skip()
        if self.m_focus == 'User':
            self.m_txtUser.AppendText('2')
        elif self.m_focus == 'Passwd':
            self.m_txtPassword.AppendText('2')
    
    def OnKey_3( self, event ):
        event.Skip()
        if self.m_focus == 'User':
            self.m_txtUser.AppendText('3')
        elif self.m_focus == 'Passwd':
            self.m_txtPassword.AppendText('3')
    
    def OnKey_4( self, event ):
        event.Skip()
        if self.m_focus == 'User':
            self.m_txtUser.AppendText('4')
        elif self.m_focus == 'Passwd':
            self.m_txtPassword.AppendText('4')
    
    def OnKey_5( self, event ):
        event.Skip()
        if self.m_focus == 'User':
            self.m_txtUser.AppendText('5')
        elif self.m_focus == 'Passwd':
            self.m_txtPassword.AppendText('5')
    
    def OnKey_6( self, event ):
        event.Skip()
        if self.m_focus == 'User':
            self.m_txtUser.AppendText('6')
        elif self.m_focus == 'Passwd':
            self.m_txtPassword.AppendText('6')
    
    def OnKey_7( self, event ):
        event.Skip()
        if self.m_focus == 'User':
            self.m_txtUser.AppendText('7')
        elif self.m_focus == 'Passwd':
            self.m_txtPassword.AppendText('7')
    
    def OnKey_8( self, event ):
        event.Skip()
        if self.m_focus == 'User':
            self.m_txtUser.AppendText('8')
        elif self.m_focus == 'Passwd':
            self.m_txtPassword.AppendText('8')
    
    def OnKey_9( self, event ):
        event.Skip()
        if self.m_focus == 'User':
            self.m_txtUser.AppendText('9')
        elif self.m_focus == 'Passwd':
            self.m_txtPassword.AppendText('9')
    
    def OnKeyCancel( self, event ):
        event.Skip()
        self.Destroy()
    
    def OnKey_0( self, event ):
        event.Skip()
        if self.m_focus == 'User':
            self.m_txtUser.AppendText('0')
        elif self.m_focus == 'Passwd':
            self.m_txtPassword.AppendText('0')
    
    def OnKeyBack( self, event ):
        event.Skip()
        if self.m_focus == 'User':
            self.m_txtUser.Remove(self.m_txtUser.GetInsertionPoint() - 1, self.m_txtUser.GetInsertionPoint())
        elif self.m_focus == 'Passwd':
            self.m_txtPassword.Remove(self.m_txtPassword.GetInsertionPoint() - 1, self.m_txtPassword.GetInsertionPoint())
        
    def OnLogin( self, event ):
        event.Skip()
        CDataLogin().Login(self.m_txtUser.GetValue(), self.m_txtPassword.GetValue())
        
    def OnSetUserFocus( self, event ):
        event.Skip()
        self.m_focus = 'User'
        
    def OnSetPasswdFocus( self, event ):
        event.Skip()
        self.m_focus = 'Passwd'
        
    def OnEvtLogin(self, event):
        if CDataLogin().GetResult() == True:
            CAppManager.SwitchToApplication('MainFrame')
        else:
            dlg = wx.MessageDialog(self, u"用户名或密码错误", caption = u"登陆")
            dlg.ShowModal()
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = CWgtLogin(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()
    
