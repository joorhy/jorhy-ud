# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class CPopRegister
###########################################################################

class CPopRegister ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"注册", pos = wx.DefaultPosition, size = wx.Size( 600,300 ), style = wx.DEFAULT_DIALOG_STYLE )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        m_gSizer = wx.GridSizer( 2, 1, 0, 0 )
        
        m_sbSizerTop = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"申请授权" ), wx.VERTICAL )
        
        m_topSizer = wx.BoxSizer( wx.VERTICAL )
        
        m_topSizerApply = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"终端数：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        m_topSizerApply.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_txtTerminalNum = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        m_topSizerApply.Add( self.m_txtTerminalNum, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_topSizer.Add( m_topSizerApply, 1, wx.ALIGN_CENTER, 5 )
        
        
        m_sbSizerTop.Add( m_topSizer, 1, wx.EXPAND, 5 )
        
        m_bottonSizer = wx.BoxSizer( wx.VERTICAL )
        
        self.m_btnApply = wx.Button( self, wx.ID_ANY, u"申请", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_bottonSizer.Add( self.m_btnApply, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_sbSizerTop.Add( m_bottonSizer, 1, wx.EXPAND, 5 )
        
        
        m_gSizer.Add( m_sbSizerTop, 1, wx.EXPAND, 5 )
        
        m_sbSizerBottom = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"验证码校验" ), wx.VERTICAL )
        
        m_topSizerVerify = wx.BoxSizer( wx.VERTICAL )
        
        m_innerVerifySizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"验证码：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        m_innerVerifySizer.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_txtKey = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
        m_innerVerifySizer.Add( self.m_txtKey, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_topSizerVerify.Add( m_innerVerifySizer, 1, wx.ALIGN_CENTER, 5 )
        
        
        m_sbSizerBottom.Add( m_topSizerVerify, 1, wx.EXPAND, 5 )
        
        m_bottomSizerVerify = wx.BoxSizer( wx.VERTICAL )
        
        self.m_btnVerify = wx.Button( self, wx.ID_ANY, u"确认", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_bottomSizerVerify.Add( self.m_btnVerify, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_sbSizerBottom.Add( m_bottomSizerVerify, 1, wx.EXPAND, 5 )
        
        
        m_gSizer.Add( m_sbSizerBottom, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( m_gSizer )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_btnApply.Bind( wx.EVT_BUTTON, self.OnBtnApply )
        self.m_btnVerify.Bind( wx.EVT_BUTTON, self.OnBtnVerify )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def OnBtnApply( self, event ):
        event.Skip()
    
    def OnBtnVerify( self, event ):
        event.Skip()
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    dlg = CPopRegister(None)
    dlg.Show()
    app.MainLoop()
