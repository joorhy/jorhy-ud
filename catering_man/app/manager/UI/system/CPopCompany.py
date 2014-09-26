# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from app.logic.desktop.CDataDeskTop import CDataDeskTop
from app.CAppManager import CAppManager

###########################################################################
## Class CPopCompany
###########################################################################

class CPopCompany ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"公司信息", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.CAPTION )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        m_sizer = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.STATIC_BORDER|wx.TAB_TRAVERSAL )
        self.m_panel.SetMinSize( wx.Size( -1,300 ) )
        
        m_gSizer = wx.GridSizer( 6, 1, 0, 0 )
        
        m_gSizer.SetMinSize( wx.Size( -1,300 ) ) 
        m_bSizer_1 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self.m_panel, wx.ID_ANY, u"名称：", wx.DefaultPosition, wx.Size( 120,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText1.Wrap( -1 )
        self.m_staticText1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
        
        m_bSizer_1.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_txtName = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 360,-1 ), 0 )
        m_bSizer_1.Add( self.m_txtName, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_gSizer.Add( m_bSizer_1, 1, wx.EXPAND, 5 )
        
        m_bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2 = wx.StaticText( self.m_panel, wx.ID_ANY, u"负责人：", wx.DefaultPosition, wx.Size( 120,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText2.Wrap( -1 )
        m_bSizer2.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_txtPersion = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
        m_bSizer2.Add( self.m_txtPersion, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_gSizer.Add( m_bSizer2, 1, wx.EXPAND, 5 )
        
        m_bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText3 = wx.StaticText( self.m_panel, wx.ID_ANY, u"联系电话：", wx.DefaultPosition, wx.Size( 120,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText3.Wrap( -1 )
        m_bSizer3.Add( self.m_staticText3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_txtPhone = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
        m_bSizer3.Add( self.m_txtPhone, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_gSizer.Add( m_bSizer3, 1, wx.EXPAND, 5 )
        
        m_bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText4 = wx.StaticText( self.m_panel, wx.ID_ANY, u"电子邮箱：", wx.DefaultPosition, wx.Size( 120,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText4.Wrap( -1 )
        m_bSizer4.Add( self.m_staticText4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_txtEmail = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 360,-1 ), 0 )
        m_bSizer4.Add( self.m_txtEmail, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_gSizer.Add( m_bSizer4, 1, wx.EXPAND, 5 )
        
        m_bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText5 = wx.StaticText( self.m_panel, wx.ID_ANY, u"地址：", wx.DefaultPosition, wx.Size( 120,-1 ), wx.ALIGN_RIGHT )
        self.m_staticText5.Wrap( -1 )
        m_bSizer5.Add( self.m_staticText5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_txtAddr = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 360,-1 ), 0 )
        m_bSizer5.Add( self.m_txtAddr, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_gSizer.Add( m_bSizer5, 1, wx.EXPAND, 5 )
        
        
        self.m_panel.SetSizer( m_gSizer )
        self.m_panel.Layout()
        m_gSizer.Fit( self.m_panel )
        m_sizer.Add( self.m_panel, 1, wx.EXPAND |wx.ALL, 5 )
        
        m_bottomSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        
        m_bottomSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_btnSave = wx.Button( self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_bottomSizer.Add( self.m_btnSave, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_btnExit = wx.Button( self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_bottomSizer.Add( self.m_btnExit, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_sizer.Add( m_bottomSizer, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( m_sizer )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_btnSave.Bind( wx.EVT_BUTTON, self.OnBtnSave )
        self.m_btnExit.Bind( wx.EVT_BUTTON, self.OnBtnExit )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, override them in your derived class
    def OnBtnSave( self, event ):
        event.Skip()
    
    def OnBtnExit( self, event ):
        event.Skip()
        self.Close()
        #CDataDeskTop.SetSelectedItem()
        #CAppManager.SwitchToApplication('DeskTop')
     
if __name__ == '__main__':
    app = wx.PySimpleApp()
    dlg = CPopCompany(None)
    dlg.Show()
    app.MainLoop()
