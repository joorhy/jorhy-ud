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
import wx.dataview
from app.CAppManager import CAppManager
from app.logic.desktop.CDataDeskTop import CDataDeskTop
from app.UI.employee.CPopDepartment import CPopDepartment
from app.logic.employee.CModelEmployee import CModelEmployee
from app.logic.employee.CDataEmployee import CDataEmployeeInfo
from app.UI.employee.CPopEmployee import CPopEmployee

###########################################################################
## Class CEmployee
###########################################################################

class CWgtEmployee ( wx.Panel ):
    
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        m_sizer = wx.BoxSizer( wx.VERTICAL )
        
        m_topSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_btnNew = wx.Button( self, wx.ID_ANY, u"新增", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnNew.SetMinSize( wx.Size( 50,50 ) )
        
        m_topSizer.Add( self.m_btnNew, 0, 0, 5 )
        
        self.m_btnModify = wx.Button( self, wx.ID_ANY, u"修改", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnModify.SetMinSize( wx.Size( 50,50 ) )
        
        m_topSizer.Add( self.m_btnModify, 0, 0, 5 )
        
        self.m_btnDelete = wx.Button( self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnDelete.SetMinSize( wx.Size( 50,50 ) )
        
        m_topSizer.Add( self.m_btnDelete, 0, 0, 5 )
        
        '''self.m_btnState = wx.Button( self, wx.ID_ANY, u"离职", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnState.SetMinSize( wx.Size( 50,50 ) )
        
        m_topSizer.Add( self.m_btnState, 0, 0, 5 )'''
        
        self.m_btnDepartment = wx.Button( self, wx.ID_ANY, u"行政部门", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnDepartment.SetFont( wx.Font( 8, 70, 90, 90, False, wx.EmptyString ) )
        self.m_btnDepartment.SetMinSize( wx.Size( 50,50 ) )
        
        m_topSizer.Add( self.m_btnDepartment, 0, 0, 5 )
        
        self.m_btnRefresh = wx.Button( self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnRefresh.SetMinSize( wx.Size( 50,50 ) )
        
        m_topSizer.Add( self.m_btnRefresh, 0, 0, 5 )
        
        self.m_btnExit = wx.Button( self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnExit.SetMinSize( wx.Size( 50,50 ) )
        
        m_topSizer.Add( self.m_btnExit, 0, 0, 5 )
        
        self.m_topPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_topPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        m_topSizer.Add( self.m_topPanel, 1, wx.EXPAND, 5 )
        
        
        m_sizer.Add( m_topSizer, 1, wx.EXPAND, 5 )
        
        m_bottomSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        m_leftSizer = wx.BoxSizer( wx.VERTICAL )
        
        m_leftSizer.SetMinSize( wx.Size( 200,600 ) ) 
        self.m_treeCtrl = wx.TreeCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,600 ), wx.TR_DEFAULT_STYLE )
        m_leftSizer.Add( self.m_treeCtrl, 0, wx.EXPAND, 5 )
        
        
        m_bottomSizer.Add( m_leftSizer, 1, 0, 5 )
        
        m_rightSizer = wx.BoxSizer( wx.VERTICAL )
        
        m_rightSizer.SetMinSize( wx.Size( 600,600 ) ) 
        self.m_dataViewList = wx.dataview.DataViewCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_dataViewList.SetMinSize( wx.Size( -1,600 ) )
        
        # Create an instance of our model...
        self.model = CModelEmployee(CDataEmployeeInfo.GetData())
        CDataEmployeeInfo.RefreshItems()
        
        # Tel the DVC to use the model
        self.m_dataViewList.AssociateModel(self.model)
        
        self.m_dataViewColumn = self.m_dataViewList.AppendTextColumn( u"行号", 0 ) 
        self.m_dataViewCode = self.m_dataViewList.AppendTextColumn( u"工号", 1 ) 
        self.m_dataViewName = self.m_dataViewList.AppendTextColumn( u"姓名", 2 ) 
        self.m_dataViewDepartment = self.m_dataViewList.AppendTextColumn( u"行政部门", 3 ) 
        self.m_dataViewDuties = self.m_dataViewList.AppendTextColumn( u"职务", 4 ) 
        self.m_dataViewPhone = self.m_dataViewList.AppendTextColumn( u"电话", 5 ) 
        self.m_dataViewSex = self.m_dataViewList.AppendTextColumn( u"性别", 6 ) 
        self.m_dataViewBirthday = self.m_dataViewList.AppendTextColumn( u"生日", 7 ) 
        self.m_dataViewState = self.m_dataViewList.AppendTextColumn( u"状态", 8 ) 
        m_rightSizer.Add( self.m_dataViewList, 0, wx.EXPAND|wx.LEFT, 5 )
        
        
        m_bottomSizer.Add( m_rightSizer, 1, 0, 5 )
        
        
        m_sizer.Add( m_bottomSizer, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( m_sizer )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.Bind( wx.EVT_SIZE, self.OnSize )
        
        self.m_btnNew.Bind( wx.EVT_BUTTON, self.OnBtnNew )
        self.m_btnModify.Bind( wx.EVT_BUTTON, self.OnBtnModify )
        self.m_btnDelete.Bind( wx.EVT_BUTTON, self.OnBtnDelete )
        #self.m_btnState.Bind( wx.EVT_BUTTON, self.OnBtnState )
        self.m_btnDepartment.Bind( wx.EVT_BUTTON, self.OnBtnDepartment )
        self.m_btnRefresh.Bind( wx.EVT_BUTTON, self.OnBtnRefresh )
        self.m_btnExit.Bind( wx.EVT_BUTTON, self.OnBtnExit )
    
    def __del__( self ):
        pass
    
    def Initailize(self):
        x, y = CDataDeskTop.GetFrameSize()       
        self.SetSize(wx.Size(x, y))

    def Uninitailize(self):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def OnSize( self, event ):
        event.Skip()
        x, y = self.GetSize()

        self.m_btnNew.SetMaxSize(wx.Size( 50,50 ))
        self.m_btnModify.SetMaxSize(wx.Size( 50,50 ))
        self.m_btnDelete.SetMaxSize(wx.Size( 50,50 ))
        #self.m_btnState.SetMaxSize(wx.Size( 50,50 ))
        self.m_btnDepartment.SetMaxSize(wx.Size( 50,50 ))
        self.m_btnRefresh.SetMaxSize(wx.Size( 50,50 ))
        self.m_btnExit.SetMaxSize(wx.Size( 50,50 ))
        self.m_topPanel.SetMaxSize( wx.Size( x-300,50 ) ) 
        self.m_treeCtrl.SetMinSize( wx.Size( 200,y-50 ) )
        self.m_dataViewList.SetMinSize( wx.Size( x-200,y-50 ) )
        
    def OnBtnNew( self, event ):
        event.Skip()
        self.popEmployee = CPopEmployee(self, "add")
        self.popEmployee.ShowModal()
    
    def OnBtnModify( self, event ):
        event.Skip()
        self.popEmployee = CPopEmployee(self, "mod")
        self.popEmployee.ShowModal()
    
    def OnBtnDelete( self, event ):
        event.Skip()
    
    '''def OnBtnState( self, event ):
        event.Skip()'''
    
    def OnBtnDepartment( self, event ):
        event.Skip()
        self.popDepartment = CPopDepartment(self)
        self.popDepartment.ShowModal()
    
    def OnBtnRefresh( self, event ):
        event.Skip()
    
    def OnBtnExit( self, event ):
        event.Skip()
        CAppManager.SwitchToApplication('DeskTop')
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = CWgtEmployee(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()

