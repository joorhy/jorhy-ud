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
from app.CAppManager import CAppManager
from app.logic.desktop.CDataMainFrame import CDataMainFrame

###########################################################################
## Class CMainFrame
###########################################################################

class CMainFrame ( wx.Panel ):
    
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.Size( 800,600 ), wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
        
        m_sizer = wx.BoxSizer( wx.VERTICAL )
        
        m_topSizer = wx.BoxSizer( wx.VERTICAL )
        
        m_topSizer.SetMinSize( wx.Size( 800,50 ) ) 
        self.m_logoPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_logoPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
        self.m_logoPanel.SetMinSize( wx.Size( 50,50 ) )
        
        m_topSizer.Add( self.m_logoPanel, 1, wx.EXPAND|wx.BOTTOM, 5 )
        
        
        m_sizer.Add( m_topSizer, 1, 0, 5 )
        
        m_bottomSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        m_bottomSizer.SetMinSize( wx.Size( 800,750 ) ) 
        m_leftSizer = wx.BoxSizer( wx.VERTICAL )
        
        m_leftSizer.SetMinSize( wx.Size( 200,750 ) ) 
        self.m_selectorPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_selectorPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
        
        m_selectorSizer = wx.BoxSizer( wx.VERTICAL )
        
        m_selectorTopSizer = wx.BoxSizer( wx.VERTICAL )
        
        m_selectorTopSizer.SetMinSize( wx.Size( 200,50 ) ) 
        
        m_selectorTopSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        m_selectorSizer.Add( m_selectorTopSizer, 1, 0, 5 )
        
        m_selectorBottomSizer = wx.BoxSizer( wx.VERTICAL )
        
        m_selectorBottomSizer.SetMinSize( wx.Size( 200,550 ) ) 
        self.m_btnDiningRoomSetting = wx.Button( self.m_selectorPanel, wx.ID_ANY, u"餐厅设置", wx.Point( 50,50 ), wx.DefaultSize, 0 )
        m_selectorBottomSizer.Add( self.m_btnDiningRoomSetting, 0, wx.ALIGN_CENTER, 5 )
        
        self.m_btnDishesPublishing = wx.Button( self.m_selectorPanel, wx.ID_ANY, u"菜品发布", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_selectorBottomSizer.Add( self.m_btnDishesPublishing, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_btnStaffMan = wx.Button( self.m_selectorPanel, wx.ID_ANY, u"员工管理", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_selectorBottomSizer.Add( self.m_btnStaffMan, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_btnReportForms = wx.Button( self.m_selectorPanel, wx.ID_ANY, u"报表中心", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_selectorBottomSizer.Add( self.m_btnReportForms, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_btnSysSetting = wx.Button( self.m_selectorPanel, wx.ID_ANY, u"系统设置", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_selectorBottomSizer.Add( self.m_btnSysSetting, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_btnStockMan = wx.Button( self.m_selectorPanel, wx.ID_ANY, u"库存管理", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_selectorBottomSizer.Add( self.m_btnStockMan, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_btnExit = wx.Button( self.m_selectorPanel, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_selectorBottomSizer.Add( self.m_btnExit, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_selectorSizer.Add( m_selectorBottomSizer, 1, 0, 5 )
        
        
        self.m_selectorPanel.SetSizer( m_selectorSizer )
        self.m_selectorPanel.Layout()
        m_selectorSizer.Fit( self.m_selectorPanel )
        m_leftSizer.Add( self.m_selectorPanel, 1, wx.EXPAND|wx.RIGHT, 5 )
        
        
        m_bottomSizer.Add( m_leftSizer, 1, 0, 5 )
        
        m_rightSizer = wx.BoxSizer( wx.VERTICAL )
        
        m_rightSizer.SetMinSize( wx.Size( 600,750 ) ) 
        self.m_funcPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_funcPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
        self.m_funcPanel.SetMinSize( wx.Size( 800,600 ) )
        
        m_btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_funcBtnMan = {}
        self.m_btnFunc_1 = wx.Button( self.m_funcPanel, wx.ID_ANY, u"Func1", wx.DefaultPosition, wx.DefaultSize, 0 )  
        funcBtnMan_1 = {0:self.m_btnFunc_1}
        self.m_funcBtnMan.update(funcBtnMan_1 )
        
        self.m_btnFunc_2 = wx.Button( self.m_funcPanel, wx.ID_ANY, u"Func2", wx.DefaultPosition, wx.DefaultSize, 0 )
        funcBtnMan_2 = {1:self.m_btnFunc_2}
        self.m_funcBtnMan.update(funcBtnMan_2 )
        
        self.m_btnFunc_3 = wx.Button( self.m_funcPanel, wx.ID_ANY, u"Func3", wx.DefaultPosition, wx.DefaultSize, 0 )
        funcBtnMan_3 = {2:self.m_btnFunc_3}
        self.m_funcBtnMan.update(funcBtnMan_3 )
        
        self.m_btnFunc_4 = wx.Button( self.m_funcPanel, wx.ID_ANY, u"Func4", wx.DefaultPosition, wx.DefaultSize, 0 )
        funcBtnMan_4 = {3:self.m_btnFunc_4}
        self.m_funcBtnMan.update(funcBtnMan_4 )
        
        self.m_btnFunc_5 = wx.Button( self.m_funcPanel, wx.ID_ANY, u"Func5", wx.DefaultPosition, wx.DefaultSize, 0 )
        funcBtnMan_5 = {4:self.m_btnFunc_5}
        self.m_funcBtnMan.update(funcBtnMan_5 )
        
        self.m_btnFunc_6 = wx.Button( self.m_funcPanel, wx.ID_ANY, u"Func6", wx.DefaultPosition, wx.DefaultSize, 0 ) 
        funcBtnMan_6 = {5:self.m_btnFunc_6}
        self.m_funcBtnMan.update(funcBtnMan_6 ) 
        
        self.m_funcPanel.SetSizer( m_btnSizer )
        self.m_funcPanel.Layout()
        m_btnSizer.Fit( self.m_funcPanel )
        m_rightSizer.Add( self.m_funcPanel, 1, wx.EXPAND, 5 )
        
        
        m_bottomSizer.Add( m_rightSizer, 1, wx.EXPAND, 5 )
        
        
        m_sizer.Add( m_bottomSizer, 1, 0, 5 )
        
        
        self.SetSizer( m_sizer )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.Bind( wx.EVT_SIZE, self.OnSize )
        self.m_btnDiningRoomSetting.Bind( wx.EVT_LEFT_DOWN, self.OnDiningRoonSetting )
        self.m_btnDishesPublishing.Bind( wx.EVT_LEFT_DOWN, self.OnDishesPublishing )
        self.m_btnStaffMan.Bind( wx.EVT_LEFT_DOWN, self.OnStaffManager )
        self.m_btnReportForms.Bind( wx.EVT_LEFT_DOWN, self.OnReportForms )
        self.m_btnSysSetting.Bind( wx.EVT_LEFT_DOWN, self.OnSystemSetting )
        self.m_btnStockMan.Bind( wx.EVT_LEFT_DOWN, self.OnStockManager )
        self.m_btnExit.Bind( wx.EVT_LEFT_DOWN, parent.OnExit )
        self.m_btnFunc_1.Bind( wx.EVT_LEFT_DOWN, self.OnFunc_1 )
        self.m_btnFunc_2.Bind( wx.EVT_LEFT_DOWN, self.OnFunc_2 )
        self.m_btnFunc_3.Bind( wx.EVT_LEFT_DOWN, self.OnFunc_3 )
        self.m_btnFunc_4.Bind( wx.EVT_LEFT_DOWN, self.OnFunc_4 )
        self.m_btnFunc_5.Bind( wx.EVT_LEFT_DOWN, self.OnFunc_5 )
        self.m_btnFunc_6.Bind( wx.EVT_LEFT_DOWN, self.OnFunc_6 )
    
    def __del__( self ):
        pass
    
    def Initailize(self):
        x, y = CDataMainFrame.GetFrameSize()
        self.SetSize(wx.Size(x, y))
        
        select_item = CDataMainFrame.GetSelectedItem()
        if select_item == "dining_table":
            self.ShowDiningRoonSetting()
        elif select_item == "dishes_publishing":
            self.ShowDishesPublishing()
        elif select_item == "staff_manager":
            self.ShowStaffManager()
        elif select_item == "report_forms":
            self.ShowReportForms()
        elif select_item == "system_setting":
            self.ShowSystemSetting()
        elif select_item == "stock_manager":
            self.ShowStockManager()
        
    def Uninitailize(self):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def OnSize( self, event ):
        event.Skip()
        x, y = self.GetSize()
       
        self.m_logoPanel.SetMinSize( wx.Size( x,50 ) )
        self.m_selectorPanel.SetMaxSize( wx.Size( 200,y-50 ) ) 
        self.m_funcPanel.SetMinSize( wx.Size( x-200,y-50 ) )
        
        self.ShowFuncBtns()
    
    def OnDiningRoonSetting( self, event ):
        event.Skip()
        CDataMainFrame.SetSelectedItem("dining_table")
        self.ShowDiningRoonSetting()
    
    def OnDishesPublishing( self, event ):
        event.Skip()
        CDataMainFrame.SetSelectedItem("dishes_publishing")
        self.ShowDishesPublishing()
    
    def OnStaffManager( self, event ):
        event.Skip()
        CDataMainFrame.SetSelectedItem("staff_manager")
        self.ShowStaffManager()
    
    def OnReportForms( self, event ):
        event.Skip()
        CDataMainFrame.SetSelectedItem("report_forms")
        self.ShowReportForms()
    
    def OnSystemSetting( self, event ):
        event.Skip()
        CDataMainFrame.SetSelectedItem("system_setting")
        self.ShowSystemSetting()
    
    def OnStockManager( self, event ):
        event.Skip()
        CDataMainFrame.SetSelectedItem("stock_manager")
        self.ShowStockManager()
    
    def OnFunc_1( self, event ):
        event.Skip()
        
        select_item = CDataMainFrame.GetSelectedItem()
        if select_item == "dining_table":
            CAppManager.SwitchToApplication('DiningTable')
        elif select_item == "dishes_publishing":
            CAppManager.SwitchToApplication('DishesPublish')
        elif select_item == "staff_manager":
            CAppManager.SwitchToApplication('Employee')
        elif select_item == "report_forms":
            pass
        elif select_item == "system_setting":
            pass
        elif select_item == "stock_manager":
            pass
        
    
    def OnFunc_2( self, event ):
        event.Skip()
        
        select_item = CDataMainFrame.GetSelectedItem()
        if select_item == "dining_table":
            pass
        elif select_item == "dishes_publishing":
            pass
        elif select_item == "staff_manager":
            CAppManager.SwitchToApplication('DutyTable')
        elif select_item == "report_forms":
            pass
        elif select_item == "system_setting":
            pass
        elif select_item == "stock_manager":
            pass
    
    def OnFunc_3( self, event ):
        event.Skip()
    
    def OnFunc_4( self, event ):
        event.Skip()
    
    def OnFunc_5( self, event ):
        event.Skip()
    
    def OnFunc_6( self, event ):
        event.Skip()
        
    def ShowDiningRoonSetting(self):
        self.EnableAllSelector()
        self.HideAllFuncBtn()
        self.m_btnDiningRoomSetting.Enabled = False;
        self.m_btnFunc_1.Show()
        self.m_btnFunc_1.Label = u"餐桌设置"
        self.SetFramTile()
    
    def ShowDishesPublishing(self):
        self.EnableAllSelector()
        self.HideAllFuncBtn()
        self.m_btnDishesPublishing.Enabled = False;
        self.m_btnFunc_1.Show()
        self.m_btnFunc_1.Label = u"菜品发布"
        self.SetFramTile()
        self.ShowFuncBtns()
    
    def ShowStaffManager(self):
        self.EnableAllSelector()
        self.HideAllFuncBtn()
        self.m_btnStaffMan.Enabled = False;
        self.m_btnFunc_1.Show()
        self.m_btnFunc_1.Label = u"员工管理"
        self.m_btnFunc_2.Show()
        self.m_btnFunc_2.Label = u"员工排班"
        self.SetFramTile()
        self.ShowFuncBtns()
    
    def ShowReportForms(self):
        self.EnableAllSelector()
        self.HideAllFuncBtn()
        self.m_btnReportForms.Enabled = False;
        self.m_btnFunc_1.Show()
        self.m_btnFunc_1.Label = u"菜品销售查询"
        self.m_btnFunc_2.Show()
        self.m_btnFunc_2.Label = u"收银情况查询"
        self.m_btnFunc_3.Show()
        self.m_btnFunc_3.Label = u"营业情况查询"
        self.m_btnFunc_4.Show()
        self.m_btnFunc_4.Label = u"消费查询"
        self.m_btnFunc_5.Show()
        self.m_btnFunc_5.Label = u"菜品排行榜"
        self.SetFramTile()
        self.ShowFuncBtns()
    
    def ShowSystemSetting(self):
        self.EnableAllSelector()
        self.HideAllFuncBtn()
        self.m_btnSysSetting.Enabled = False;
        self.m_btnFunc_1.Show()
        self.m_btnFunc_1.Label = u"打印机设置"
        self.m_btnFunc_2.Show()
        self.m_btnFunc_2.Label = u"数据备份"
        self.m_btnFunc_3.Show()
        self.m_btnFunc_3.Label = u"公司信息"
        self.m_btnFunc_4.Show()
        self.m_btnFunc_4.Label = u"注册"
        self.SetFramTile()
        self.ShowFuncBtns()
    
    def ShowStockManager(self):
        self.EnableAllSelector()
        self.HideAllFuncBtn()
        self.m_btnStockMan.Enabled = False;
        self.m_btnFunc_1.Show()
        self.m_btnFunc_1.Label = u"采购管理"
        self.m_btnFunc_2.Show()
        self.m_btnFunc_2.Label = u"库存管理"
        self.SetFramTile()
        self.ShowFuncBtns()
    
    def EnableAllSelector(self):
        self.m_btnDiningRoomSetting.Enabled = True
        self.m_btnDishesPublishing.Enabled = True
        self.m_btnStaffMan.Enabled = True
        self.m_btnReportForms.Enabled = True
        self.m_btnSysSetting.Enabled = True
        self.m_btnStockMan.Enabled = True
        
    def HideAllFuncBtn(self):
        self.m_btnFunc_1.Hide()
        self.m_btnFunc_2.Hide()
        self.m_btnFunc_3.Hide()
        self.m_btnFunc_4.Hide()
        self.m_btnFunc_5.Hide()
        self.m_btnFunc_6.Hide()    
        
    def ShowFuncBtns(self):
        select_item = CDataMainFrame.GetSelectedItem()  
        self.func_num = 1
        if select_item == "dining_table":
            self.func_num = 1
        elif select_item == "dishes_publishing":
            self.func_num = 1
        elif select_item == "staff_manager":
            self.func_num = 2
        elif select_item == "report_forms":
            self.func_num = 5
        elif select_item == "system_setting":
            self.func_num = 4
        elif select_item == "stock_manager":
            self.func_num = 2   
            
        x, y = self.GetSize()
        btn_y = ((y - 50) - 100) / 2
        btn_x = ((x - 200) - ((self.func_num * 100) + ((self.func_num - 1) * 10))) / 2
        for i in range(self.func_num):
            self.m_funcBtnMan[i].Move( wx.Point(btn_x + (i * 110), btn_y) )
            self.m_funcBtnMan[i].SetSize( wx.Size(100,100) )
        
    def SetFramTile(self): 
        select_item = CDataMainFrame.GetSelectedItem()  
        if select_item == "dining_table":
            self.GetParent().SetTitle(u"餐厅设置")
        elif select_item == "dishes_publishing":
            self.GetParent().SetTitle(u"菜品发布")
        elif select_item == "staff_manager":
            self.GetParent().SetTitle(u"员工管理")
        elif select_item == "report_forms":
            self.GetParent().SetTitle(u"报表中心")
        elif select_item == "system_setting":
            self.GetParent().SetTitle(u"菜品发布")
        elif select_item == "stock_manager":
            self.GetParent().SetTitle(u"库存管理")   
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = CMainFrame(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()
