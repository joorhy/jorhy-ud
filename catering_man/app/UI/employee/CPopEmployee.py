#!/usr/bin/env python
# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview
import datetime
from app.logic.employee.CModelUserRole import CModelUserRole
from app.logic.employee.CDataUserRole import CDataUserRoleInfo, CDataUserRole
from app.logic.employee.CDataEmployee import CDataEmployeeInfo, CDataEmployee
from app.logic.employee.CDataDepartment import CDataDepartmentInfo

###########################################################################
## Class CPopEmployee
###########################################################################

class CPopEmployee ( wx.Dialog ):
    
    def __init__( self, parent, type = "add" ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"员工资料维护", pos = wx.DefaultPosition, size = wx.Size( 700,400 ), style = wx.CAPTION )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        m_sizer = wx.BoxSizer( wx.VERTICAL )
        
        self.m_notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,300 ), 0 )
        self.m_mainInfoPanel = wx.Panel( self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.Size( 700,300 ), wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
        self.m_mainInfoPanel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
        self.m_mainInfoPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        self.m_mainInfoPanel.SetMaxSize( wx.Size( -1,300 ) )
        
        m_mainPanelSizer = wx.BoxSizer( wx.VERTICAL )
        
        m_mainTopGSizer = wx.GridSizer( 1, 3, 0, 0 )
        
        m_topLeftGSizer = wx.GridSizer( 3, 1, 0, 0 )
        
        m_codeSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self.m_mainInfoPanel, wx.ID_ANY, u"工号：", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        self.m_staticText1.Wrap( -1 )
        self.m_staticText1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
        self.m_staticText1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        
        m_codeSizer.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_txtCode = wx.TextCtrl( self.m_mainInfoPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        m_codeSizer.Add( self.m_txtCode, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_topLeftGSizer.Add( m_codeSizer, 1, wx.EXPAND, 5 )
        
        m_dutySizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2 = wx.StaticText( self.m_mainInfoPanel, wx.ID_ANY, u"职务：", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        self.m_staticText2.Wrap( -1 )
        self.m_staticText2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
        
        m_dutySizer.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_txtDuty = wx.TextCtrl( self.m_mainInfoPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        m_dutySizer.Add( self.m_txtDuty, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_topLeftGSizer.Add( m_dutySizer, 1, wx.EXPAND, 5 )
        
        m_telSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText3 = wx.StaticText( self.m_mainInfoPanel, wx.ID_ANY, u"电话：", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        self.m_staticText3.Wrap( -1 )
        self.m_staticText3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
        
        m_telSizer.Add( self.m_staticText3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_txtTelephone = wx.TextCtrl( self.m_mainInfoPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        m_telSizer.Add( self.m_txtTelephone, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_topLeftGSizer.Add( m_telSizer, 1, wx.EXPAND, 5 )
        
        
        m_mainTopGSizer.Add( m_topLeftGSizer, 1, wx.EXPAND, 5 )
        
        m_topMidGSizer = wx.GridSizer( 3, 1, 0, 0 )
        
        m_nameSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText4 = wx.StaticText( self.m_mainInfoPanel, wx.ID_ANY, u"员工姓名：", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        self.m_staticText4.Wrap( -1 )
        self.m_staticText4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
        
        m_nameSizer.Add( self.m_staticText4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_txtName = wx.TextCtrl( self.m_mainInfoPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        m_nameSizer.Add( self.m_txtName, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_topMidGSizer.Add( m_nameSizer, 1, wx.EXPAND, 5 )
        
        m_deptSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText5 = wx.StaticText( self.m_mainInfoPanel, wx.ID_ANY, u"行政部门：", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        self.m_staticText5.Wrap( -1 )
        self.m_staticText5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )
        
        m_deptSizer.Add( self.m_staticText5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        m_cbxDepartmentChoices = []
        self.m_cbxDepartment = wx.ComboBox( self.m_mainInfoPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), m_cbxDepartmentChoices, 0 )
        m_deptSizer.Add( self.m_cbxDepartment, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_topMidGSizer.Add( m_deptSizer, 1, wx.EXPAND, 5 )
        
        m_idSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText6 = wx.StaticText( self.m_mainInfoPanel, wx.ID_ANY, u"身份证号：", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        self.m_staticText6.Wrap( -1 )
        self.m_staticText6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
        
        m_idSizer.Add( self.m_staticText6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_txtIdcard = wx.TextCtrl( self.m_mainInfoPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        m_idSizer.Add( self.m_txtIdcard, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_topMidGSizer.Add( m_idSizer, 1, wx.EXPAND, 5 )
        
        
        m_mainTopGSizer.Add( m_topMidGSizer, 1, wx.EXPAND, 5 )
        
        m_topBottomGSizer = wx.GridSizer( 3, 1, 0, 0 )
        
        m_brithSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText7 = wx.StaticText( self.m_mainInfoPanel, wx.ID_ANY, u"生日：", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        self.m_staticText7.Wrap( -1 )
        self.m_staticText7.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
        
        m_brithSizer.Add( self.m_staticText7, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_dateBrithDay = wx.DatePickerCtrl( self.m_mainInfoPanel, size = ( 120,-1 ),
                                                         style = wx.TAB_TRAVERSAL| wx.DP_DROPDOWN| wx.DP_SHOWCENTURY | wx.DP_ALLOWNONE )
        m_brithSizer.Add( self.m_dateBrithDay, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        m_topBottomGSizer.Add( m_brithSizer, 1, wx.EXPAND, 5 )
        
        m_sexSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText8 = wx.StaticText( self.m_mainInfoPanel, wx.ID_ANY, u"性别：", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        self.m_staticText8.Wrap( -1 )
        self.m_staticText8.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )
        
        m_sexSizer.Add( self.m_staticText8, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_sexPanel = wx.Panel( self.m_mainInfoPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,25 ), wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
        self.m_sexPanel.SetMinSize( wx.Size( 100,-1 ) )
        
        m_sexSelectSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        m_sexSelectSizer.SetMinSize( wx.Size( 80,25 ) ) 
        self.m_rbtnMan = wx.RadioButton( self.m_sexPanel, wx.ID_ANY, u"男", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        m_sexSelectSizer.Add( self.m_rbtnMan, 0, wx.ALL, 5 )
        
        self.m_rbtnFeman = wx.RadioButton( self.m_sexPanel, wx.ID_ANY, u"女", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        m_sexSelectSizer.Add( self.m_rbtnFeman, 0, wx.ALL, 5 )
        
        
        self.m_sexPanel.SetSizer( m_sexSelectSizer )
        self.m_sexPanel.Layout()
        m_sexSizer.Add( self.m_sexPanel, 1, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_topBottomGSizer.Add( m_sexSizer, 1, wx.EXPAND, 5 )
        
        m_stateSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText9 = wx.StaticText( self.m_mainInfoPanel, wx.ID_ANY, u"状态：", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        self.m_staticText9.Wrap( -1 )
        self.m_staticText9.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
        
        m_stateSizer.Add( self.m_staticText9, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_statePanel = wx.Panel( self.m_mainInfoPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,25 ), wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
        m_stateSelectSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        m_stateSelectSizer.SetMinSize( wx.Size( 80,25 ) ) 
        self.m_rbtnOnDuty = wx.RadioButton( self.m_statePanel, wx.ID_ANY, u"在职", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        m_stateSelectSizer.Add( self.m_rbtnOnDuty, 0, wx.ALL, 5 )
        
        self.m_rbtnOffDuty = wx.RadioButton( self.m_statePanel, wx.ID_ANY, u"离职", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        m_stateSelectSizer.Add( self.m_rbtnOffDuty, 0, wx.ALL, 5 )
        
        
        self.m_statePanel.SetSizer( m_stateSelectSizer )
        self.m_statePanel.Layout()
        m_stateSizer.Add( self.m_statePanel, 1, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_topBottomGSizer.Add( m_stateSizer, 1, wx.EXPAND, 5 )
        
        
        m_mainTopGSizer.Add( m_topBottomGSizer, 1, wx.EXPAND, 5 )
        
        
        m_mainPanelSizer.Add( m_mainTopGSizer, 1, 0, 5 )
        
        m_mainBottomSizer = wx.BoxSizer( wx.VERTICAL )
        
        m_mainBottomSizer.SetMinSize( wx.Size( 600,-1 ) ) 
        m_mainBottomGSizer = wx.GridSizer( 3, 1, 0, 0 )
        
        m_addrSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText10 = wx.StaticText( self.m_mainInfoPanel, wx.ID_ANY, u"居住地址：", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        self.m_staticText10.Wrap( -1 )
        self.m_staticText10.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
        self.m_staticText10.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )
        
        m_addrSizer.Add( self.m_staticText10, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_txtAddr = wx.TextCtrl( self.m_mainInfoPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
        m_addrSizer.Add( self.m_txtAddr, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_mainBottomGSizer.Add( m_addrSizer, 1, wx.EXPAND, 5 )
        
        m_emailSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText11 = wx.StaticText( self.m_mainInfoPanel, wx.ID_ANY, u"电子邮件：", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        self.m_staticText11.Wrap( -1 )
        self.m_staticText11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
        
        m_emailSizer.Add( self.m_staticText11, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_txtEmail = wx.TextCtrl( self.m_mainInfoPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
        m_emailSizer.Add( self.m_txtEmail, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_mainBottomGSizer.Add( m_emailSizer, 1, wx.EXPAND, 5 )
        
        m_noteSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText12 = wx.StaticText( self.m_mainInfoPanel, wx.ID_ANY, u"备注：", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        self.m_staticText12.Wrap( -1 )
        self.m_staticText12.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
        
        m_noteSizer.Add( self.m_staticText12, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_txtNote = wx.TextCtrl( self.m_mainInfoPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
        m_noteSizer.Add( self.m_txtNote, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_mainBottomGSizer.Add( m_noteSizer, 1, wx.EXPAND, 5 )
        
        
        m_mainBottomSizer.Add( m_mainBottomGSizer, 1, wx.EXPAND, 5 )
        
        
        m_mainPanelSizer.Add( m_mainBottomSizer, 1, 0, 5 )
        
        
        self.m_mainInfoPanel.SetSizer( m_mainPanelSizer )
        self.m_mainInfoPanel.Layout()
        self.m_notebook.AddPage( self.m_mainInfoPanel, u"主要资料", True )
        self.m_rolePanel = wx.Panel( self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.Size( 700,300 ), wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
        self.m_rolePanel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
        self.m_rolePanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        m_roleSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        m_roleLeftSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        m_roleLeftSizer.SetMinSize( wx.Size( 500,300 ) ) 
        self.m_dataViewRole = wx.dataview.DataViewCtrl( self.m_rolePanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,300 ), 0|wx.TAB_TRAVERSAL )
        self.m_dataViewRole.SetMaxSize( wx.Size( 500,300 ) )
        
        # Create an instance of our model...
        self.model = CModelUserRole(CDataUserRoleInfo.GetData())
        
        # Tel the DVC to use the model
        self.m_dataViewRole.AssociateModel(self.model)
        
        self.m_dataViewListRole = self.m_dataViewRole.AppendTextColumn( u"行号", 0 ) 
        self.m_dataViewListRole = self.m_dataViewRole.AppendTextColumn( u"编码", 1 ) 
        self.m_dataViewListRole = self.m_dataViewRole.AppendTextColumn( u"员工角色", 2 ) 
        self.m_dataViewListState = self.m_dataViewRole.AppendTextColumn( u"状态", 3) 
        m_roleLeftSizer.Add( self.m_dataViewRole, 0, wx.EXPAND, 5 )
        
        
        m_roleSizer.Add( m_roleLeftSizer, 1, wx.EXPAND, 5 )
        
        m_roleRightSizer = wx.BoxSizer( wx.VERTICAL )
        
        m_roleRightSizer.SetMinSize( wx.Size( 600,300 ) ) 
        self.m_btnNewRole = wx.Button( self.m_rolePanel, wx.ID_ANY, u"新增角色", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_roleRightSizer.Add( self.m_btnNewRole, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_btnDeleteRole = wx.Button( self.m_rolePanel, wx.ID_ANY, u"删除角色", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_roleRightSizer.Add( self.m_btnDeleteRole, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_btnSaveRole = wx.Button( self.m_rolePanel, wx.ID_ANY, u"保存角色", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_roleRightSizer.Add( self.m_btnSaveRole, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_roleSizer.Add( m_roleRightSizer, 1, wx.EXPAND, 5 )
        
        
        self.m_rolePanel.SetSizer( m_roleSizer )
        self.m_rolePanel.Layout()
        self.m_notebook.AddPage( self.m_rolePanel, u"角色设置", False )
        
        m_sizer.Add( self.m_notebook, 1, wx.EXPAND |wx.ALL, 5 )
        
        m_sizerBottom = wx.BoxSizer( wx.HORIZONTAL )
        
        m_sizerBottom.SetMinSize( wx.Size( 700,100 ) ) 
        
        m_sizerBottom.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_btnSave = wx.Button( self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_sizerBottom.Add( self.m_btnSave, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_btnExit = wx.Button( self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_sizerBottom.Add( self.m_btnExit, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_sizer.Add( m_sizerBottom, 1, wx.BOTTOM, 5 )
        
        
        self.SetSizer( m_sizer )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_btnNewRole.Bind( wx.EVT_BUTTON, self.OnBtnNewRole )
        self.m_btnDeleteRole.Bind( wx.EVT_BUTTON, self.OnBtnDeleteRole )
        self.m_btnSaveRole.Bind( wx.EVT_BUTTON, self.OnBtnSaveRole )
        self.m_btnSave.Bind( wx.EVT_BUTTON, self.OnBtnSave )
        self.m_btnExit.Bind( wx.EVT_BUTTON, self.OnBtnExit )
        
        # Initailize 
        self.index = 0
        self.type = type
        self.user_id = 0
        self.Initailize()
    
    def __del__( self ):
        pass
    
    def Initailize(self):
        if self.type == "add":
            self.InitAddInfo()
        elif self.type == "mod":
            self.index = CDataEmployeeInfo.GetCurItemIndex()
            self.InitModInfo()
            
    def InitAddInfo(self):
        li_department = CDataDepartmentInfo.GetData()
        for dept in li_department:
            self.m_cbxDepartment.Append(dept.name, dept)
        self.m_cbxDepartment.SetSelection(0)
        
        self.m_rbtnMan.SetValue(True)
        self.m_rbtnOnDuty.SetValue(True)
        
    def InitModInfo(self):
        self.m_txtCode.Enable(False)
        if self.index < 0:
            self.index = 0
            return
        
        items = CDataEmployeeInfo.GetItems()
        if self.index >= len(items):
            self.index = len(items) - 1
            return
        
        data = items[self.index]
        self.user_id = data.id
        self.m_txtCode.SetValue(str(data.code))
        self.m_txtName.SetValue(data.name)
        self.m_txtDuty.SetValue(data.duty)
        self.m_txtTelephone.SetValue(str(data.telephone))
        self.m_txtIdcard.SetValue(data.id_card)
        self.m_txtAddr.SetValue(data.addr)
        self.m_txtEmail.SetValue(data.email)
        self.m_txtNote.SetValue(data.note)
        if data.sex == 0:
            self.m_rbtnMan.SetValue(True)
            self.m_rbtnFeman.SetValue(False)
        else:
            self.m_rbtnMan.SetValue(False)
            self.m_rbtnFeman.SetValue(True)
            
        if data.state == 0:
            self.m_rbtnOnDuty.SetValue(True)
            self.m_rbtnOffDuty.SetValue(False)
        else:
            self.m_rbtnOnDuty.SetValue(False)
            self.m_rbtnOffDuty.SetValue(True)
        
        birth_day = wx.DateTime()    
        self.m_dateBrithDay.SetValue(birth_day)

        li_department = CDataDepartmentInfo.GetData()
        dept_selection = 0
        for dept in li_department:
            self.m_cbxDepartment.Append(dept.name, dept)
            if dept.code == data.department:
                self.m_cbxDepartment.SetSelection(dept_selection)
            dept_selection += 1
    
    # Virtual event handlers, overide them in your derived class
    def OnBtnNewRole( self, event ):
        event.Skip()
        CDataUserRoleInfo.AddItem(CDataUserRole(0, 0, 1, ""))
        
        data = CDataUserRole(CDataUserRoleInfo.GetDataLen() + 1, CDataUserRoleInfo.GetId(), 0, "")
        self.model.data.append(data)
        item = self.model.ObjectToItem(data)
        self.m_dataViewRole.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
    
    def OnBtnDeleteRole( self, event ):
        event.Skip()
        item = self.m_dataViewRole.GetCurrentItem()
        data = self.model.ItemToObject(item)
        self.model.data.remove(data)
        self.m_dataViewRole.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
        CDataUserRoleInfo.DeleteItem(data)
    
    def OnBtnSaveRole( self, event ):
        event.Skip()
        item = self.m_dataViewRole.GetCurrentItem()
        data = self.model.ItemToObject(item)
        CDataUserRoleInfo.UpdateItem(data)
    
    def OnBtnSave( self, event ):
        event.Skip()
        department = self.m_cbxDepartment.GetClientData(self.m_cbxDepartment.GetSelection())
        if self.m_rbtnMan.GetValue() == True:
            sex_type = 0
        else:
            sex_type = 1
            
        if self.m_rbtnOnDuty.GetValue() == True:
            state_type = 0
        else:
            state_type = 1
            
        data = CDataEmployee(self.user_id, 0,
                          self.m_txtCode.GetValue(), 
                          self.m_txtName.GetValue(), 
                          self.m_dateBrithDay.GetValue().Format("%Y-%m-%d %H:%M:%S"), 
                          self.m_txtDuty.GetValue(), 
                          department.code,
                          sex_type, 
                          int(self.m_txtTelephone.GetValue()),
                          self.m_txtIdcard.GetValue(),
                          state_type,
                          self.m_txtAddr.GetValue(),
                          self.m_txtEmail.GetValue(), 
                          self.m_txtNote.GetValue())
        
        if self.type == "add":
            CDataEmployeeInfo.AddItem(data)
        elif self.type == "mod":
            CDataEmployeeInfo.UpdateItem(data)
    
    def OnBtnExit( self, event ):
        event.Skip()
        self.Close()
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    dlg = CPopEmployee(None)
    dlg.Show()
    app.MainLoop()
