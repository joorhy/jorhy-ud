#!/usr/bin/env python
# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
from app.manager.logic.data import * 
from app.manager.logic.ctrl import * 
from app.manager.logic.model import *
from app.manager.AppManager import AppManager

import wx
import wx.xrc
import wx.dataview
from wx.dataview import DataViewColumn

###########################################################################
## Class CAreaSetting
###########################################################################

class PopDepartment (wx.Dialog):
    def _init_view_sizer(self, parent):
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Create a data view control
        self.dataViewList = wx.dataview.DataViewCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.dataViewList.SetMinSize(wx.Size(600,300))
        # Add items into data view control
        self.dataViewList.AppendTextColumn(u"行号", 0) 
        self.dataViewList.AppendTextColumn(u"编码", 1, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE) 
        self.dataViewList.AppendTextColumn(u"行政部门", 2, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE) 
        sizer.Add(self.dataViewList, 0, wx.ALL|wx.EXPAND, 5)
        
        # Layout view 
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_ctrl_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # Add new button
        self.btnNew = wx.Button(self, wx.ID_ANY, u"新增", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnNew, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        # Add delete button
        self.btnDelete = wx.Button(self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnDelete, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        # Add spacer
        sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        # Add refresh button
        self.btnRefresh = wx.Button(self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnRefresh, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        # Add save button
        self.btnSave = wx.Button(self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnSave, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnExit, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        
        # Layout control buttons
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"行政部门设置", pos=wx.DefaultPosition, size=wx.Size(600,400), style=wx.CAPTION|wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.Size(-1,-1), wx.Size(-1,-1))
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_view_sizer(sizer)
        self._init_ctrl_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout() 
        self.Centre(wx.BOTH)
        
        # Create an instance of our model...
        self.model = ModelDepartment(CtrlDepartment.GetData())
        
        # Tel the DVC to use the model
        self.dataViewList.AssociateModel(self.model)

        # Connect Events
        self.btnNew.Bind(wx.EVT_BUTTON, self.OnBtnNew)
        self.btnDelete.Bind(wx.EVT_BUTTON, self.OnBtnDelete)
        self.btnRefresh.Bind(wx.EVT_BUTTON, self.OnBtnRefresh)
        self.btnSave.Bind(wx.EVT_BUTTON, self.OnBtnSave)
        self.btnExit.Bind(wx.EVT_BUTTON, self.OnBtnExit)
    
    def __del__(self):
        pass
    
    
    # Virtual event handlers, override them in your derived class
    def OnBtnNew(self, event):
        event.Skip()
        CtrlDepartment.AddItem(DataDepartment(0, 0, ""))
        
        data = DataDepartment(CtrlDepartment.GetDataLen() + 1, CtrlDepartment.GetId(), "")
        self.model.data.append(data)
        item = self.model.ObjectToItem(data)
        self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
    
    def OnBtnDelete(self, event):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        self.model.data.remove(data)
        self.dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
        CtrlDepartment.DeleteItem(data)
    
    def OnBtnRefresh(self, event):
        event.Skip()
        result = CtrlDepartment.GetData()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
                    
        self.model.Cleared()
    
    def OnBtnSave(self, event):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        CtrlDepartment.UpdateItem(data)
    
    def OnBtnExit(self, event):
        event.Skip()
        self.Close()

###########################################################################
## Class CPopEmployee
###########################################################################

class PopEmployee (wx.Dialog):
    def _init_view_sizer(self, parent):
        notebook = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1,300), 0)

        # Add employee main info panel
        mainInfoPanel = wx.Panel(notebook, wx.ID_ANY, wx.DefaultPosition, wx.Size(700,300), wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL)
        mainInfoPanel.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        mainInfoPanel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
        mainInfoPanel.SetMaxSize(wx.Size(-1,300))
        
        # Add employee main info sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_main_info_view_sizer(mainInfoPanel, sizer)
        # Layout main info 
        mainInfoPanel.SetSizer(sizer)
        mainInfoPanel.Layout()
        # Add main info panel into note book
        notebook.AddPage(mainInfoPanel, u"主要资料", True)

        # Add employee role info panel
        rolePanel = wx.Panel(notebook, wx.ID_ANY, wx.DefaultPosition, wx.Size(700,300), wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL)
        rolePanel.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        rolePanel.SetBackgroundColour(wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE))

        # Add employee role info sizer
        roleSizer = wx.BoxSizer(wx.HORIZONTAL)
        self._init_role_info_view_sizer(rolePanel, roleSizer)
        # Layout role panel
        rolePanel.SetSizer(roleSizer)
        rolePanel.Layout()
        # Add role info panel into note book
        notebook.AddPage(rolePanel, u"角色设置", False)

        # Layout note book 
        parent.Add(notebook, 1, wx.EXPAND |wx.ALL, 5)

    def _init_main_info_view_sizer(self, container, parent):
        gSizer = wx.GridSizer(1, 3, 0, 0)

        # Add 3 columns sizer for main info
        self._init_main_info_column_1_sizer(container, gSizer)
        self._init_main_info_column_2_sizer(container, gSizer)
        self._init_main_info_column_3_sizer(container, gSizer)
        parent.Add(gSizer, 1, 0, 5)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.SetMinSize(wx.Size(600,-1))
        # Add 3 rows for main info
        self._init_main_info_3_rows_sizer(container, sizer)
        parent.Add(sizer, 1, 0, 5)

    def _init_main_info_column_1_sizer(self, container, parent):
        gSizer = wx.GridSizer(3, 1, 0, 0)

        # Add employee's job number sizer
        codeSizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add job number label
        sTxtCode = wx.StaticText(container, wx.ID_ANY, u"工号：", wx.DefaultPosition, wx.Size(80,-1), 0)
        sTxtCode.Wrap(-1)
        sTxtCode.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        sTxtCode.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        codeSizer.Add(sTxtCode, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add job number text control
        self.txtCode = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1,-1), 0)
        codeSizer.Add(self.txtCode, 0, wx.ALIGN_CENTER|wx.ALL,5)
        # Layout job number sizer
        gSizer.Add(codeSizer, 1, wx.EXPAND, 5)

        # Add employee's duty sizer
        dutySizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add duty label
        sTxtDuty = wx.StaticText(container, wx.ID_ANY, u"职务：", wx.DefaultPosition, wx.Size(80,-1), 0)
        sTxtDuty.Wrap(-1)
        sTxtDuty.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        dutySizer.Add(sTxtDuty, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add duty text control
        self.txtDuty = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1,-1), 0)
        dutySizer.Add(self.txtDuty, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Layout duty sizer
        gSizer.Add(dutySizer, 1, wx.EXPAND, 5)

        # Add employee's telephone number sizer
        telSizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add telephone label
        sTxtTel = wx.StaticText(container, wx.ID_ANY, u"电话：", wx.DefaultPosition, wx.Size(80,-1), 0)
        sTxtTel.Wrap( -1 )
        sTxtTel.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT ))
        telSizer.Add(sTxtTel, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        # Add telephone text control
        self.txtTelephone = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1,-1), 0)
        telSizer.Add(self.txtTelephone, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Layout telephone number sizer
        gSizer.Add(telSizer, 1, wx.EXPAND, 5)

        # Layout main info column 1
        parent.Add(gSizer, 1, wx.EXPAND, 5)

    def _init_main_info_column_2_sizer(self, container, parent):
        gSizer = wx.GridSizer(3, 1, 0, 0)

        # Add employee's name sizer
        nameSizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add name label
        sTxtName = wx.StaticText(container, wx.ID_ANY, u"员工姓名：", wx.DefaultPosition, wx.Size(80,-1), 0)
        sTxtName.Wrap(-1)
        sTxtName.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        nameSizer.Add(sTxtName, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add name text control
        self.txtName = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1,-1), 0)
        nameSizer.Add(self.txtName, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Layout name
        gSizer.Add(nameSizer, 1, wx.EXPAND, 5)

        # Add employee's department sizer
        deptSizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add department label
        sTxtDept = wx.StaticText(container, wx.ID_ANY, u"行政部门：", wx.DefaultPosition, wx.Size(80,-1), 0)
        sTxtDept.Wrap(-1)
        sTxtDept.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_CAPTIONTEXT))
        deptSizer.Add(sTxtDept, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add department combo box
        cbxDepartmentChoices = list()
        self.cbxDepartment = wx.ComboBox(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1,-1), cbxDepartmentChoices, 0)
        deptSizer.Add(self.cbxDepartment, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Layout department
        gSizer.Add(deptSizer, 1, wx.EXPAND, 5)

        # Add employee's ID number sizer
        idSizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add ID number label
        sTxtID = wx.StaticText(container, wx.ID_ANY, u"身份证号：", wx.DefaultPosition, wx.Size(80,-1), 0)
        sTxtID.Wrap(-1)
        sTxtID.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        idSizer.Add(sTxtID, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add ID number text control
        self.txtIdcard = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        idSizer.Add(self.txtIdcard, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Layout ID number
        gSizer.Add(idSizer, 1, wx.EXPAND, 5)
        
        #Layout main info column 2
        parent.Add(gSizer, 1, wx.EXPAND, 5)

    def _init_main_info_column_3_sizer(self, container, parent):
        gSizer = wx.GridSizer(3, 1, 0, 0)

        # Add employee's birthday sizer
        birthSizer = wx.BoxSizer( wx.HORIZONTAL )
        # Add birthday label
        sTxtBirthday = wx.StaticText(container, wx.ID_ANY, u"生日：", wx.DefaultPosition, wx.Size(60,-1), 0)
        sTxtBirthday.Wrap(-1)
        sTxtBirthday.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        birthSizer.Add(sTxtBirthday, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add birthday picker control
        self.dateBrithDay = wx.DatePickerCtrl(container, size=(120,-1), style=wx.TAB_TRAVERSAL| wx.DP_DROPDOWN| wx.DP_SHOWCENTURY | wx.DP_ALLOWNONE)
        birthSizer.Add(self.dateBrithDay, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Layout birthday
        gSizer.Add(birthSizer, 1, wx.EXPAND, 5)

        # Add employee's gender sizer
        sexSizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add gender label
        sTxtGender = wx.StaticText(container, wx.ID_ANY, u"性别：", wx.DefaultPosition, wx.Size(60,-1), 0)
        sTxtGender.Wrap(-1)
        sTxtGender.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_CAPTIONTEXT))
        sexSizer.Add(sTxtGender, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add gender panel 
        sexPanel = wx.Panel(container, wx.ID_ANY, wx.DefaultPosition, wx.Size(100,25), wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL)
        sexPanel.SetMinSize(wx.Size(100,-1))
        # Add gender selector sizer
        sexSelectSizer = wx.BoxSizer(wx.HORIZONTAL)
        sexSelectSizer.SetMinSize(wx.Size(80,25)) 
        self.rbtnMan = wx.RadioButton(sexPanel, wx.ID_ANY, u"男", wx.DefaultPosition, wx.Size(60,-1), 0)
        sexSelectSizer.Add(self.rbtnMan, 0, wx.ALL, 5)
        self.rbtnFeman = wx.RadioButton(sexPanel, wx.ID_ANY, u"女", wx.DefaultPosition, wx.Size(60,-1), 0)
        sexSelectSizer.Add(self.rbtnFeman, 0, wx.ALL, 5)
        # Layout gender sizer
        sexPanel.SetSizer(sexSelectSizer)
        sexPanel.Layout()
        sexSizer.Add(sexPanel, 1, wx.ALIGN_CENTER|wx.ALL, 5)
        gSizer.Add(sexSizer, 1, wx.EXPAND, 5)

        # Add employee's job status sizer
        stateSizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add job status label
        sTxtStatus = wx.StaticText(container, wx.ID_ANY, u"状态：", wx.DefaultPosition, wx.Size(60,-1), 0)
        sTxtStatus.Wrap(-1)
        sTxtStatus.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        stateSizer.Add(sTxtStatus, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add job status panel
        statePanel = wx.Panel(container, wx.ID_ANY, wx.DefaultPosition, wx.Size(80,25), wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL)
        # Add job status selector sizer
        stateSelectSizer = wx.BoxSizer(wx.HORIZONTAL)
        stateSelectSizer.SetMinSize(wx.Size(80,25)) 
        self.rbtnOnDuty = wx.RadioButton(statePanel, wx.ID_ANY, u"在职", wx.DefaultPosition, wx.Size(60,-1), 0)
        stateSelectSizer.Add(self.rbtnOnDuty, 0, wx.ALL, 5) 
        self.rbtnOffDuty = wx.RadioButton(statePanel, wx.ID_ANY, u"离职", wx.DefaultPosition, wx.Size(60,-1), 0)
        stateSelectSizer.Add(self.rbtnOffDuty, 0, wx.ALL, 5)
        # Layout job status sizer
        statePanel.SetSizer(stateSelectSizer)
        statePanel.Layout()
        stateSizer.Add(statePanel, 1, wx.ALIGN_CENTER|wx.ALL, 5)
        gSizer.Add(stateSizer, 1, wx.EXPAND, 5)

        #Layout main info column 3
        parent.Add(gSizer, 1, wx.EXPAND, 5)

    def _init_main_info_3_rows_sizer(self, container, parent):
        # Create 3 rows and 1 column grid sizer
        gSizer = wx.GridSizer(3, 1, 0, 0)
        
        # Add employee's address sizer
        addrSizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add address label
        sTxtAddr = wx.StaticText(container, wx.ID_ANY, u"居住地址：", wx.DefaultPosition, wx.Size(80,-1), 0)
        sTxtAddr.Wrap(-1)
        sTxtAddr.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        sTxtAddr.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_CAPTIONTEXT))
        addrSizer.Add(sTxtAddr, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add address text control
        self.txtAddr = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400,-1), 0)
        addrSizer.Add(self.txtAddr, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Layout address sizer
        gSizer.Add(addrSizer, 1, wx.EXPAND, 5)
        
        # Add employee's email sizer
        emailSizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add email label
        sTxtEmail = wx.StaticText(container, wx.ID_ANY, u"电子邮件：", wx.DefaultPosition, wx.Size(80,-1), 0)
        sTxtEmail.Wrap(-1)
        sTxtEmail.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        emailSizer.Add(sTxtEmail, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add email text control
        self.txtEmail = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400,-1), 0)
        emailSizer.Add(self.txtEmail, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Layout email sizer
        gSizer.Add(emailSizer, 1, wx.EXPAND, 5)
        
        # Add employee's remarks
        noteSizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add remarks label
        sTxtNote = wx.StaticText(container, wx.ID_ANY, u"备注：", wx.DefaultPosition, wx.Size(80,-1), 0)
        sTxtNote.Wrap(-1)
        sTxtNote.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        noteSizer.Add(sTxtNote, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add remarks text control
        self.txtNote = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400,-1), 0)
        noteSizer.Add(self.txtNote, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Layout remarks sizer
        gSizer.Add(noteSizer, 1, wx.EXPAND, 5)
        
        # Layout 3 rows main info of employee, contains address email and remarks
        parent.Add(gSizer, 1, wx.EXPAND, 5)

    def _init_role_info_view_sizer(self, container, parent):
        # Add data view list sizer
        dataSizer = wx.BoxSizer(wx.HORIZONTAL)
        dataSizer.SetMinSize(wx.Size(500,300))     
        # Add data view list 
        self.dataViewRole = wx.dataview.DataViewCtrl(container, wx.ID_ANY, wx.DefaultPosition, wx.Size(500,300), 0|wx.TAB_TRAVERSAL)
        self.dataViewRole.SetMaxSize(wx.Size(500,300))
        # Add items into data view list
        self.dataViewRole.AppendTextColumn(u"行号", 0) 
        self.dataViewRole.AppendTextColumn(u"编码", 1) 
        self.dataViewRole.AppendTextColumn(u"员工角色", 2) 
        self.dataViewRole.AppendTextColumn(u"状态", 3) 
        dataSizer.Add(self.dataViewRole, 0, wx.EXPAND, 5)
        # Layout data view list
        parent.Add(dataSizer, 1, wx.EXPAND, 5)

        # Add control buttons sizer
        ctrlSizer = wx.BoxSizer(wx.VERTICAL)
        ctrlSizer.SetMinSize(wx.Size(600,300))
        # Add new role button
        self.btnNewRole = wx.Button(container, wx.ID_ANY, u"新增角色", wx.DefaultPosition, wx.DefaultSize, 0)
        ctrlSizer.Add( self.btnNewRole, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add delete role button
        self.btnDeleteRole = wx.Button(container, wx.ID_ANY, u"删除角色", wx.DefaultPosition, wx.DefaultSize, 0)
        ctrlSizer.Add(self.btnDeleteRole, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add save role button
        self.btnSaveRole = wx.Button(container, wx.ID_ANY, u"保存角色", wx.DefaultPosition, wx.DefaultSize, 0)
        ctrlSizer.Add(self.btnSaveRole, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Layout control buttons
        parent.Add(ctrlSizer, 1, wx.EXPAND, 5)

    def _init_ctrl_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.SetMinSize(wx.Size(700,100))
        # Add spacer 
        sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        # Add save button
        self.btnSave = wx.Button(self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnSave, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnExit, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        # Layout control sizer
        parent.Add(sizer, 1, wx.BOTTOM, 5)

    def __init__(self, parent, type_ = "add"):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"员工资料维护", pos=wx.DefaultPosition, size=wx.Size(700,400), style=wx.CAPTION)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_view_sizer(sizer)
        self._init_ctrl_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout() 
        self.Centre(wx.BOTH)

        # Create an instance of our model...
        self.model = ModelUserRole(CtrlUserRole.GetData())
        
        # Tell the DVC to use the model
        self.dataViewRole.AssociateModel(self.model)
        
        # Connect Events
        self.btnNewRole.Bind(wx.EVT_BUTTON, self.OnBtnNewRole)
        self.btnDeleteRole.Bind(wx.EVT_BUTTON, self.OnBtnDeleteRole)
        self.btnSaveRole.Bind(wx.EVT_BUTTON, self.OnBtnSaveRole)
        self.btnSave.Bind(wx.EVT_BUTTON, self.OnBtnSave)
        self.btnExit.Bind(wx.EVT_BUTTON, self.OnBtnExit)
        
        # Initialize 
        self.index = 0
        self.type = type_
        self.user_id = 0
        self.InitializeView()
    
    def __del__( self ):
        pass
    
    def InitializeView(self):
        if self.type == "add":
            self.InitAddView()
        elif self.type == "mod":
            self.index = CtrlEmployee.GetCurItemIndex()
            self.InitModView()
            
    def InitAddView(self):
        li_department = CtrlDepartment.GetData()
        for dept in li_department:
            self.cbxDepartment.Append(dept.name, dept)
        self.cbxDepartment.SetSelection(0)
        
        self.rbtnMan.SetValue(True)
        self.rbtnOnDuty.SetValue(True)
        
    def InitModView(self):
        self.txtCode.Enable(False)
        if self.index < 0:
            self.index = 0
            return
        
        items = CtrlEmployee.GetItems()
        if self.index >= len(items):
            self.index = len(items) - 1
            return
        
        data = items[self.index]
        self.user_id = data.id
        self.txtCode.SetValue(str(data.code))
        self.txtName.SetValue(data.name)
        self.txtDuty.SetValue(data.duty)
        self.txtTelephone.SetValue(str(data.telephone))
        self.txtIdcard.SetValue(data.id_card)
        self.txtAddr.SetValue(data.addr)
        self.txtEmail.SetValue(data.email)
        self.txtNote.SetValue(data.note)
        if data.sex == 0:
            self.rbtnMan.SetValue(True)
            self.rbtnFeman.SetValue(False)
        else:
            self.rbtnMan.SetValue(False)
            self.rbtnFeman.SetValue(True)
            
        if data.state == 0:
            self.rbtnOnDuty.SetValue(True)
            self.rbtnOffDuty.SetValue(False)
        else:
            self.rbtnOnDuty.SetValue(False)
            self.rbtnOffDuty.SetValue(True)
        
        birth_day = wx.DateTime()    
        self.dateBrithDay.SetValue(birth_day)

        li_department = CtrlDepartment.GetData()
        dept_selection = 0
        for dept in li_department:
            self.cbxDepartment.Append(dept.name, dept)
            if dept.code == data.department:
                self.cbxDepartment.SetSelection(dept_selection)
            dept_selection += 1
    
    # Virtual event handlers, overide them in your derived class
    def OnBtnNewRole( self, event ):
        event.Skip()
        CtrlUserRole.AddItem(DataUserRole(0, 0, 1, ""))
        
        data = DataUserRole(CtrlUserRole.GetDataLen() + 1, CtrlUserRole.GetId(), 0, "")
        self.model.data.append(data)
        item = self.model.ObjectToItem(data)
        self.dataViewRole.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
    
    def OnBtnDeleteRole( self, event ):
        event.Skip()
        item = self.dataViewRole.GetCurrentItem()
        data = self.model.ItemToObject(item)
        self.model.data.remove(data)
        self.dataViewRole.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
        CtrlUserRole.DeleteItem(data)
    
    def OnBtnSaveRole( self, event ):
        event.Skip()
        item = self.dataViewRole.GetCurrentItem()
        data = self.model.ItemToObject(item)
        CtrlUserRole.UpdateItem(data)
    
    def OnBtnSave( self, event ):
        event.Skip()
        department = self.cbxDepartment.GetClientData(self.cbxDepartment.GetSelection())
        if self.rbtnMan.GetValue() == True:
            sex_type = 0
        else:
            sex_type = 1
            
        if self.rbtnOnDuty.GetValue() == True:
            state_type = 0
        else:
            state_type = 1
            
        data = DataEmployee(self.user_id, 0,
                          self.txtCode.GetValue(), 
                          self.txtName.GetValue(), 
                          self.dateBrithDay.GetValue().Format("%Y-%m-%d %H:%M:%S"), 
                          self.txtDuty.GetValue(), 
                          department.code,
                          sex_type, 
                          int(self.txtTelephone.GetValue()),
                          self.txtIdcard.GetValue(),
                          state_type,
                          self.txtAddr.GetValue(),
                          self.txtEmail.GetValue(), 
                          self.txtNote.GetValue())
        
        if self.type == "add":
            CtrlEmployee.AddItem(data)
        elif self.type == "mod":
            CtrlEmployee.UpdateItem(data)
    
    def OnBtnExit( self, event ):
        event.Skip()
        self.Close()
        
###########################################################################
## Class CWgtEmployee
###########################################################################

class WgtEmployee (wx.Panel):
    def _init_status_bar_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add new button
        self.btnNew = wx.Button(self, wx.ID_ANY, u"新增", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnNew.SetMinSize(wx.Size(50,50 ))
        sizer.Add(self.btnNew, 0, 0, 5)
        # Add modify button
        self.btnModify = wx.Button(self, wx.ID_ANY, u"修改", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnModify.SetMinSize(wx.Size(50,50))
        sizer.Add(self.btnModify, 0, 0, 5)
        # Add delete button
        self.btnDelete = wx.Button(self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnDelete.SetMinSize(wx.Size(50,50))
        sizer.Add(self.btnDelete, 0, 0, 5)
        # Add department setting button
        self.btnDepartment = wx.Button(self, wx.ID_ANY, u"行政部门", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnDepartment.SetFont(wx.Font(8, 70, 90, 90, False, wx.EmptyString))
        self.btnDepartment.SetMinSize(wx.Size(50,50)) 
        sizer.Add(self.btnDepartment, 0, 0, 5)
        # Add refresh button
        self.btnRefresh = wx.Button(self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnRefresh.SetMinSize(wx.Size(50,50))
        sizer.Add(self.btnRefresh, 0, 0, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnExit.SetMinSize(wx.Size(50,50))
        sizer.Add(self.btnExit, 0, 0, 5)
        # Add fix space panel
        self.topPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.topPanel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE)) 
        sizer.Add(self.topPanel, 1, wx.EXPAND, 5)
        
        # Layout status bar 
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_view_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # Add a tree control
        treeSizer = wx.BoxSizer(wx.VERTICAL)
        treeSizer.SetMinSize( wx.Size( 200,600 ) ) 
        self.treeCtrl = wx.TreeCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1,600), wx.TR_DEFAULT_STYLE)
        treeSizer.Add(self.treeCtrl, 0, wx.EXPAND, 5)
        sizer.Add(treeSizer, 1, 0, 5 )
        # Add data view list
        viewSizer = wx.BoxSizer(wx.VERTICAL)
        viewSizer.SetMinSize(wx.Size(600,600)) 
        self.dataViewList = wx.dataview.DataViewCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.dataViewList.SetMinSize(wx.Size(-1,600))
        # Add items into data view list
        self.dataViewList.AppendTextColumn(u"行号", 0) 
        self.dataViewList.AppendTextColumn(u"工号", 1) 
        self.dataViewList.AppendTextColumn(u"姓名", 2) 
        self.dataViewList.AppendTextColumn(u"行政部门", 3) 
        self.dataViewList.AppendTextColumn(u"职务", 4) 
        self.dataViewList.AppendTextColumn(u"电话", 5) 
        self.dataViewList.AppendTextColumn(u"性别", 6) 
        self.dataViewList.AppendTextColumn(u"生日", 7) 
        self.dataViewList.AppendTextColumn(u"状态", 8) 
        viewSizer.Add(self.dataViewList, 0, wx.EXPAND|wx.LEFT, 5)
        sizer.Add(viewSizer, 1, 0, 5)

        # Layout 
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(800,600), style=wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_status_bar_sizer(sizer)
        self._init_view_sizer(sizer) 

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Create an instance of our model...
        self.model = ModelEmployee(CtrlEmployee.GetData())
        CtrlEmployee.RefreshItems()
        
        # Tell the DVC to use the model
        self.dataViewList.AssociateModel(self.model)

        # Connect Events
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.btnNew.Bind(wx.EVT_BUTTON, self.OnBtnNew)
        self.btnModify.Bind(wx.EVT_BUTTON, self.OnBtnModify)
        self.btnDelete.Bind(wx.EVT_BUTTON, self.OnBtnDelete)
        self.btnDepartment.Bind(wx.EVT_BUTTON, self.OnBtnDepartment)
        self.btnRefresh.Bind(wx.EVT_BUTTON, self.OnBtnRefresh)
        self.btnExit.Bind(wx.EVT_BUTTON, self.OnBtnExit)
        
        # Show tree control
        self.ShowTreeCtrl()
    
    def __del__( self ):
        pass
    
    def Initailize(self):
        # Add event listener
        EvtManager.AddListener(self, EnumEvent.EVT_EMPLOYEE_REFRESH, self.OnBtnRefresh)
        
        x, y = CtrlHomePage.GetFrameSize()       
        self.SetSize(wx.Size(x, y))

    def Uninitailize(self):
        # Remove event listener
        EvtManager.RemoveListener(self, EnumEvent.EVT_EMPLOYEE_REFRESH, self.OnBtnRefresh)
    
    def ShowTreeCtrl(self):
        isz = (16,16)
        il = wx.ImageList(isz[0], isz[1])
        fldridx     = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER,      wx.ART_OTHER, isz))
        fldropenidx = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER_OPEN, wx.ART_OTHER, isz))
        fileidx     = il.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, isz))
        
        self.treeCtrl.SetImageList(il)
        self.il = il

        self.root = self.treeCtrl.AddRoot(u"全部行政部门")
        self.treeCtrl.SetPyData(self.root, None)
        self.treeCtrl.SetItemImage(self.root, fldridx, wx.TreeItemIcon_Normal)
        self.treeCtrl.SetItemImage(self.root, fldropenidx, wx.TreeItemIcon_Expanded)
        
        department_map = dict()
        li_items = CtrlEmployee.GetItems()
        for item in li_items:
            if department_map.has_key(item.department):
                department_map[item.department].append(item)
            else:
                list_tmp = []
                list_tmp.append(item)
                department_map_tmp = {item.department:list_tmp}
                department_map.update(department_map_tmp)
        
        li_department = CtrlDepartment.GetData()
        for dept in li_department:
            if department_map.has_key(dept.code):
                title = "%s(%d)" % (dept.name, len(department_map[dept.code]))
                child = self.treeCtrl.AppendItem(self.root, title)
                self.treeCtrl.SetPyData(child, None)
                self.treeCtrl.SetItemImage(child, fldridx, wx.TreeItemIcon_Normal)
                self.treeCtrl.SetItemImage(child, fldropenidx, wx.TreeItemIcon_Expanded)
                for employee_info in department_map[dept.code]:
                    sub_clild = self.treeCtrl.AppendItem(child, employee_info.name)
                    self.treeCtrl.SetPyData(sub_clild, None)
                    self.treeCtrl.SetItemImage(sub_clild, fileidx, wx.TreeItemIcon_Normal)
                    self.treeCtrl.SetItemImage(sub_clild, fileidx, wx.TreeItemIcon_Selected)
            else:
                title = "%s(0)" % dept.name
                child = self.treeCtrl.AppendItem(self.root, title)
                self.treeCtrl.SetPyData(child, None)
                self.treeCtrl.SetItemImage(child, fldridx, wx.TreeItemIcon_Normal)
                self.treeCtrl.SetItemImage(child, fldropenidx, wx.TreeItemIcon_Expanded)
                
        self.treeCtrl.Expand(self.root)
        
    def RefreshUI(self):
        # Refresh treeCtrl
        CtrlEmployee.RefreshItems()
        self.treeCtrl.DeleteAllItems()
        self.ShowTreeCtrl()
        
        # Refresh data view list
        result = CtrlEmployee.GetData()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
                    
        self.model.Cleared()
    
    # Virtual event handlers, override them in your derived class
    def OnSize( self, event ):
        event.Skip()
        x, y = self.GetSize()

        self.btnNew.SetMaxSize(wx.Size(50,50))
        self.btnModify.SetMaxSize(wx.Size(50,50))
        self.btnDelete.SetMaxSize(wx.Size(50,50))
        self.btnDepartment.SetMaxSize(wx.Size(50,50))
        self.btnRefresh.SetMaxSize(wx.Size(50,50))
        self.btnExit.SetMaxSize(wx.Size(50,50))
        self.topPanel.SetMaxSize(wx.Size(x-300,50)) 
        self.treeCtrl.SetMinSize(wx.Size(200,y-50))
        self.dataViewList.SetMinSize(wx.Size(x-200,y-50))
        
    def OnBtnNew( self, event ):
        event.Skip()
        self.popEmployee = PopEmployee(self, "add")
        self.popEmployee.ShowModal()
    
    def OnBtnModify( self, event ):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        index = self.model.data.index(data)
        CtrlEmployee.SetCurItemIndex(index)
        self.popEmployee = PopEmployee(self, "mod")
        self.popEmployee.ShowModal()
    
    def OnBtnDelete( self, event ):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        self.model.data.remove(data)
        self.dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
        CtrlEmployee.DeleteItem(data)
    
    def OnBtnDepartment( self, event ):
        event.Skip()
        self.popDepartment = PopDepartment(self)
        self.popDepartment.ShowModal()
    
    def OnBtnRefresh( self, event ):
        event.Skip()
        self.RefreshUI()
    
    def OnBtnExit( self, event ):
        event.Skip()
        AppManager.SwitchToApplication('HomePage')
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = WgtEmployee(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()