#!/usr/bin/env python
# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
from app.manager.logic.ctrl import * 
from app.manager.logic.model import *
from app.manager.logic.data import *
from app.manager.AppManager import AppManager

import wx
import wx.xrc
import wx.dataview
from wx.dataview import DataViewColumn

###########################################################################
## Class PopDepartment
###########################################################################


class PopDepartment (wx.Dialog):
    def _init_view_sizer(self, parent):
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Create a data view control
        self.dataViewList = wx.dataview.DataViewCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.dataViewList.SetMinSize(wx.Size(600, 300))
        # Add items into data view control
        self.dataViewList.AppendTextColumn(u"行号", 0) 
        self.dataViewList.AppendTextColumn(u"编码", 1, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE) 
        self.dataViewList.AppendTextColumn(u"行政部门", 2, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE) 
        sizer.Add(self.dataViewList, 0, wx.ALL | wx.EXPAND, 5)
        
        # Layout view 
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_ctrl_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # Add new button
        self.btnNew = wx.Button(self, wx.ID_ANY, u"新增", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnNew, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        # Add delete button
        self.btnDelete = wx.Button(self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnDelete, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        # Add spacer
        sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        # Add refresh button
        self.btnRefresh = wx.Button(self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnRefresh, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        # Add save button
        self.btnSave = wx.Button(self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnSave, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnExit, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        
        # Layout control buttons
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"行政部门设置", pos=wx.DefaultPosition,
                           size=wx.Size(600, 400), style=wx.CAPTION | wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.Size(-1, -1), wx.Size(-1, -1))
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_view_sizer(sizer)
        self._init_ctrl_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout() 
        self.Centre(wx.BOTH)
        
        # Create an instance of our model...
        self.model = ModelDepartment(CtrlDepartment.get_data())
        
        # Tel the DVC to use the model
        self.dataViewList.AssociateModel(self.model)

        # Connect Events
        self.btnNew.Bind(wx.EVT_BUTTON, self.on_btn_new)
        self.btnDelete.Bind(wx.EVT_BUTTON, self.on_btn_delete)
        self.btnRefresh.Bind(wx.EVT_BUTTON, self.on_btn_refresh)
        self.btnSave.Bind(wx.EVT_BUTTON, self.on_btn_save)
        self.btnExit.Bind(wx.EVT_BUTTON, self.on_btn_exit)
    
    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def on_btn_new(self, event):
        event.Skip()
        CtrlDepartment.add_item(DataDepartment(0, 0, ""))
        
        data = DataDepartment(CtrlDepartment.get_data_len() + 1, CtrlDepartment.get_id(), "")
        self.model.data.append(data)
        item = self.model.ObjectToItem(data)
        self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
    
    def on_btn_delete(self, event):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        self.model.data.remove(data)
        self.dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
        CtrlDepartment.delete_item(data)
    
    def on_btn_refresh(self, event):
        event.Skip()
        result = CtrlDepartment.get_data()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
                    
        self.model.Cleared()
    
    def on_btn_save(self, event):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        CtrlDepartment.update_item(data)
    
    def on_btn_exit(self, event):
        event.Skip()
        self.Close()

###########################################################################
## Class PopEmployee
###########################################################################


class PopEmployee (wx.Dialog):
    def _init_view_sizer(self, parent):
        notebook = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 300), 0)

        # Add employee main info panel
        main_info_panel = wx.Panel(notebook, wx.ID_ANY, wx.DefaultPosition,
                                   wx.Size(700, 300), wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        main_info_panel.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        main_info_panel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
        main_info_panel.SetMaxSize(wx.Size(-1, 300))
        
        # Add employee main info sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_main_info_view_sizer(main_info_panel, sizer)
        # Layout main info 
        main_info_panel.SetSizer(sizer)
        main_info_panel.Layout()
        # Add main info panel into note book
        notebook.AddPage(main_info_panel, u"主要资料", True)

        # Add employee role info panel
        role_panel = wx.Panel(notebook, wx.ID_ANY, wx.DefaultPosition,
                              wx.Size(700, 300), wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        role_panel.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        role_panel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))

        # Add employee role info sizer
        role_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self._init_role_info_view_sizer(role_panel, role_sizer)
        # Layout role panel
        role_panel.SetSizer(role_sizer)
        role_panel.Layout()
        # Add role info panel into note book
        notebook.AddPage(role_panel, u"角色设置", False)

        # Layout note book 
        parent.Add(notebook, 1, wx.EXPAND | wx.ALL, 5)

    def _init_main_info_view_sizer(self, container, parent):
        g_sizer = wx.GridSizer(1, 3, 0, 0)

        # Add 3 columns sizer for main info
        self._init_main_info_column_1_sizer(container, g_sizer)
        self._init_main_info_column_2_sizer(container, g_sizer)
        self._init_main_info_column_3_sizer(container, g_sizer)
        parent.Add(g_sizer, 1, 0, 5)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.SetMinSize(wx.Size(600, -1))
        # Add 3 rows for main info
        self._init_main_info_3_rows_sizer(container, sizer)
        parent.Add(sizer, 1, 0, 5)

    def _init_main_info_column_1_sizer(self, container, parent):
        g_sizer = wx.GridSizer(3, 1, 0, 0)

        # Add employee's job number sizer
        code_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add job number label
        s_txt_code = wx.StaticText(container, wx.ID_ANY, u"工号：", wx.DefaultPosition, wx.Size(80, -1), 0)
        s_txt_code.Wrap(-1)
        s_txt_code.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        s_txt_code.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        code_sizer.Add(s_txt_code, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add job number text control
        self.txtCode = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        code_sizer.Add(self.txtCode, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Layout job number sizer
        g_sizer.Add(code_sizer, 1, wx.EXPAND, 5)

        # Add employee's duty sizer
        duty_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add duty label
        s_txt_duty = wx.StaticText(container, wx.ID_ANY, u"职务：", wx.DefaultPosition, wx.Size(80, -1), 0)
        s_txt_duty.Wrap(-1)
        s_txt_duty.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        duty_sizer.Add(s_txt_duty, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add duty text control
        self.txtDuty = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        duty_sizer.Add(self.txtDuty, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Layout duty sizer
        g_sizer.Add(duty_sizer, 1, wx.EXPAND, 5)

        # Add employee's telephone number sizer
        tel_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add telephone label
        s_txt_tel = wx.StaticText(container, wx.ID_ANY, u"电话：", wx.DefaultPosition, wx.Size(80, -1), 0)
        s_txt_tel.Wrap(-1)
        s_txt_tel.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        tel_sizer.Add(s_txt_tel, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add telephone text control
        self.txtTelephone = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        tel_sizer.Add(self.txtTelephone, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Layout telephone number sizer
        g_sizer.Add(tel_sizer, 1, wx.EXPAND, 5)

        # Layout main info column 1
        parent.Add(g_sizer, 1, wx.EXPAND, 5)

    def _init_main_info_column_2_sizer(self, container, parent):
        g_sizer = wx.GridSizer(3, 1, 0, 0)

        # Add employee's name sizer
        name_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add name label
        s_txt_name = wx.StaticText(container, wx.ID_ANY, u"员工姓名：", wx.DefaultPosition, wx.Size(80, -1), 0)
        s_txt_name.Wrap(-1)
        s_txt_name.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        name_sizer.Add(s_txt_name, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add name text control
        self.txtName = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        name_sizer.Add(self.txtName, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Layout name
        g_sizer.Add(name_sizer, 1, wx.EXPAND, 5)

        # Add employee's department sizer
        dept_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add department label
        s_txt_dept = wx.StaticText(container, wx.ID_ANY, u"行政部门：", wx.DefaultPosition, wx.Size(80, -1), 0)
        s_txt_dept.Wrap(-1)
        s_txt_dept.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_CAPTIONTEXT))
        dept_sizer.Add(s_txt_dept, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add department combo box
        cbx_department_choices = list()
        self.cbxDepartment = wx.ComboBox(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.Size(-1, -1), cbx_department_choices, 0)
        dept_sizer.Add(self.cbxDepartment, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Layout department
        g_sizer.Add(dept_sizer, 1, wx.EXPAND, 5)

        # Add employee's ID number sizer
        id_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add ID number label
        s_txt_id = wx.StaticText(container, wx.ID_ANY, u"身份证号：", wx.DefaultPosition, wx.Size(80, -1), 0)
        s_txt_id.Wrap(-1)
        s_txt_id.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        id_sizer.Add(s_txt_id, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add ID number text control
        self.txtIdCard = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        id_sizer.Add(self.txtIdCard, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Layout ID number
        g_sizer.Add(id_sizer, 1, wx.EXPAND, 5)
        
        #Layout main info column 2
        parent.Add(g_sizer, 1, wx.EXPAND, 5)

    def _init_main_info_column_3_sizer(self, container, parent):
        g_sizer = wx.GridSizer(3, 1, 0, 0)

        # Add employee's birthday sizer
        birth_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add birthday label
        s_txt_birthday = wx.StaticText(container, wx.ID_ANY, u"生日：", wx.DefaultPosition, wx.Size(60, -1), 0)
        s_txt_birthday.Wrap(-1)
        s_txt_birthday.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        birth_sizer.Add(s_txt_birthday, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add birthday picker control
        self.dateBirthDay = wx.DatePickerCtrl(container, size=(120, -1),
                                              style=wx.TAB_TRAVERSAL | wx.DP_DROPDOWN |
                                              wx.DP_SHOWCENTURY | wx.DP_ALLOWNONE)
        birth_sizer.Add(self.dateBirthDay, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Layout birthday
        g_sizer.Add(birth_sizer, 1, wx.EXPAND, 5)

        # Add employee's gender sizer
        sex_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add gender label
        s_txt_gender = wx.StaticText(container, wx.ID_ANY, u"性别：", wx.DefaultPosition, wx.Size(60, -1), 0)
        s_txt_gender.Wrap(-1)
        s_txt_gender.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_CAPTIONTEXT))
        sex_sizer.Add(s_txt_gender, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add gender panel 
        sex_panel = wx.Panel(container, wx.ID_ANY, wx.DefaultPosition,
                             wx.Size(100, 25), wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        sex_panel.SetMinSize(wx.Size(100, -1))
        # Add gender selector sizer
        sex_select_sizer = wx.BoxSizer(wx.HORIZONTAL)
        sex_select_sizer.SetMinSize(wx.Size(80, 25))
        self.radioBtnMale = wx.RadioButton(sex_panel, wx.ID_ANY, u"男", wx.DefaultPosition, wx.Size(60, -1), 0)
        sex_select_sizer.Add(self.radioBtnMale, 0, wx.ALL, 5)
        self.radioBtnFemale = wx.RadioButton(sex_panel, wx.ID_ANY, u"女", wx.DefaultPosition, wx.Size(60, -1), 0)
        sex_select_sizer.Add(self.radioBtnFemale, 0, wx.ALL, 5)
        # Layout gender sizer
        sex_panel.SetSizer(sex_select_sizer)
        sex_panel.Layout()
        sex_sizer.Add(sex_panel, 1, wx.ALIGN_CENTER | wx.ALL, 5)
        g_sizer.Add(sex_panel, 1, wx.EXPAND, 5)

        # Add employee's job status sizer
        state_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add job status label
        s_txt_status = wx.StaticText(container, wx.ID_ANY, u"状态：", wx.DefaultPosition, wx.Size(60, -1), 0)
        s_txt_status.Wrap(-1)
        s_txt_status.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        state_sizer.Add(s_txt_status, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add job status panel
        status_panel = wx.Panel(container, wx.ID_ANY, wx.DefaultPosition,
                                wx.Size(80, 25), wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        # Add job status selector sizer
        status_select_sizer = wx.BoxSizer(wx.HORIZONTAL)
        status_select_sizer.SetMinSize(wx.Size(80, 25))
        self.radioBtnOnDuty = wx.RadioButton(status_panel, wx.ID_ANY, u"在职", wx.DefaultPosition, wx.Size(60, -1), 0)
        status_select_sizer.Add(self.radioBtnOnDuty, 0, wx.ALL, 5)
        self.radioBtnOffDuty = wx.RadioButton(status_panel, wx.ID_ANY, u"离职", wx.DefaultPosition, wx.Size(60, -1), 0)
        status_select_sizer.Add(self.radioBtnOffDuty, 0, wx.ALL, 5)
        # Layout job status sizer
        status_panel.SetSizer(status_select_sizer)
        status_panel.Layout()
        state_sizer.Add(status_panel, 1, wx.ALIGN_CENTER | wx.ALL, 5)
        g_sizer.Add(state_sizer, 1, wx.EXPAND, 5)

        #Layout main info column 3
        parent.Add(g_sizer, 1, wx.EXPAND, 5)

    def _init_main_info_3_rows_sizer(self, container, parent):
        # Create 3 rows and 1 column grid sizer
        g_sizer = wx.GridSizer(3, 1, 0, 0)
        
        # Add employee's address sizer
        addr_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add address label
        s_txt_addr = wx.StaticText(container, wx.ID_ANY, u"居住地址：", wx.DefaultPosition, wx.Size(80, -1), 0)
        s_txt_addr.Wrap(-1)
        s_txt_addr.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        s_txt_addr.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_CAPTIONTEXT))
        addr_sizer.Add(s_txt_addr, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add address text control
        self.txtAddress = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400, -1), 0)
        addr_sizer.Add(self.txtAddress, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Layout address sizer
        g_sizer.Add(addr_sizer, 1, wx.EXPAND, 5)
        
        # Add employee's email sizer
        email_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add email label
        s_txt_email = wx.StaticText(container, wx.ID_ANY, u"电子邮件：", wx.DefaultPosition, wx.Size(80, -1), 0)
        s_txt_email.Wrap(-1)
        s_txt_email.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        email_sizer.Add(s_txt_email, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add email text control
        self.txtEmail = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400, -1), 0)
        email_sizer.Add(self.txtEmail, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Layout email sizer
        g_sizer.Add(email_sizer, 1, wx.EXPAND, 5)
        
        # Add employee's remarks
        note_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add remarks label
        s_txt_note = wx.StaticText(container, wx.ID_ANY, u"备注：", wx.DefaultPosition, wx.Size(80, -1), 0)
        s_txt_note.Wrap(-1)
        s_txt_note.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        note_sizer.Add(s_txt_note, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add remarks text control
        self.txtNote = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400, -1), 0)
        note_sizer.Add(self.txtNote, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Layout remarks sizer
        g_sizer.Add(note_sizer, 1, wx.EXPAND, 5)
        
        # Layout 3 rows main info of employee, contains address email and remarks
        parent.Add(g_sizer, 1, wx.EXPAND, 5)

    def _init_role_info_view_sizer(self, container, parent):
        # Add data view list sizer
        data_sizer = wx.BoxSizer(wx.HORIZONTAL)
        data_sizer.SetMinSize(wx.Size(500, 300))
        # Add data view list 
        self.dataViewRole = wx.dataview.DataViewCtrl(container, wx.ID_ANY, wx.DefaultPosition,
                                                     wx.Size(500, 300), 0 | wx.TAB_TRAVERSAL)
        self.dataViewRole.SetMaxSize(wx.Size(500, 300))
        # Add items into data view list
        self.dataViewRole.AppendTextColumn(u"行号", 0) 
        self.dataViewRole.AppendTextColumn(u"编码", 1) 
        self.dataViewRole.AppendTextColumn(u"员工角色", 2) 
        self.dataViewRole.AppendTextColumn(u"状态", 3) 
        data_sizer.Add(self.dataViewRole, 0, wx.EXPAND, 5)
        # Layout data view list
        parent.Add(data_sizer, 1, wx.EXPAND, 5)

        # Add control buttons sizer
        ctrl_sizer = wx.BoxSizer(wx.VERTICAL)
        ctrl_sizer.SetMinSize(wx.Size(600, 300))
        # Add new role button
        self.btnNewRole = wx.Button(container, wx.ID_ANY, u"新增角色", wx.DefaultPosition, wx.DefaultSize, 0)
        ctrl_sizer.Add(self.btnNewRole, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add delete role button
        self.btnDeleteRole = wx.Button(container, wx.ID_ANY, u"删除角色", wx.DefaultPosition, wx.DefaultSize, 0)
        ctrl_sizer.Add(self.btnDeleteRole, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add save role button
        self.btnSaveRole = wx.Button(container, wx.ID_ANY, u"保存角色", wx.DefaultPosition, wx.DefaultSize, 0)
        ctrl_sizer.Add(self.btnSaveRole, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Layout control buttons
        parent.Add(ctrl_sizer, 1, wx.EXPAND, 5)

    def _init_ctrl_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.SetMinSize(wx.Size(700, 100))
        # Add spacer 
        sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        # Add save button
        self.btnSave = wx.Button(self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnSave, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnExit, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Layout control sizer
        parent.Add(sizer, 1, wx.BOTTOM, 5)

    def __init__(self, parent, type_="add"):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"员工资料维护", pos=wx.DefaultPosition,
                           size=wx.Size(700, 400), style=wx.CAPTION)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_view_sizer(sizer)
        self._init_ctrl_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout() 
        self.Centre(wx.BOTH)

        # Create an instance of our model...
        self.model = ModelUserRole(CtrlUserRole.get_data())
        
        # Tell the DVC to use the model
        self.dataViewRole.AssociateModel(self.model)
        
        # Connect Events
        self.btnNewRole.Bind(wx.EVT_BUTTON, self.on_btn_new_role)
        self.btnDeleteRole.Bind(wx.EVT_BUTTON, self.on_btn_delete_role)
        self.btnSaveRole.Bind(wx.EVT_BUTTON, self.on_btn_save_role)
        self.btnSave.Bind(wx.EVT_BUTTON, self.on_btn_save)
        self.btnExit.Bind(wx.EVT_BUTTON, self.on_btn_exit)
        
        # Initialize 
        self.index = 0
        self.type = type_
        self.user_id = 0
        self._initialize_view()
    
    def __del__(self):
        pass
    
    def _initialize_view(self):
        if self.type == "add":
            self._init_add_view()
        elif self.type == "mod":
            self.index = CtrlEmployee.get_cur_item_index()
            self._init_mod_view()
            
    def _init_add_view(self):
        li_department = CtrlDepartment.get_data()
        for dept in li_department:
            self.cbxDepartment.Append(dept.name, dept)
        self.cbxDepartment.SetSelection(0)
        
        self.radioBtnMale.SetValue(True)
        self.radioBtnOnDuty.SetValue(True)
        
    def _init_mod_view(self):
        self.txtCode.Enable(False)
        if self.index < 0:
            self.index = 0
            return
        
        items = CtrlEmployee.get_items()
        if self.index >= len(items):
            self.index = len(items) - 1
            return
        
        data = items[self.index]
        self.user_id = data.id
        self.txtCode.SetValue(str(data.code))
        self.txtName.SetValue(data.name)
        self.txtDuty.SetValue(data.duty)
        self.txtTelephone.SetValue(str(data.telephone))
        self.txtIdCard.SetValue(data.id_card)
        self.txtAddress.SetValue(data.addr)
        self.txtEmail.SetValue(data.email)
        self.txtNote.SetValue(data.note)
        if data.sex == 0:
            self.radioBtnMale.SetValue(True)
            self.radioBtnFemale.SetValue(False)
        else:
            self.radioBtnMale.SetValue(False)
            self.radioBtnFemale.SetValue(True)
            
        if data.state == 0:
            self.radioBtnOnDuty.SetValue(True)
            self.radioBtnOffDuty.SetValue(False)
        else:
            self.radioBtnOnDuty.SetValue(False)
            self.radioBtnOffDuty.SetValue(True)
        
        birth_day = wx.DateTime()    
        self.dateBirthDay.SetValue(birth_day)

        li_department = CtrlDepartment.get_data()
        dept_selection = 0
        for dept in li_department:
            self.cbxDepartment.Append(dept.name, dept)
            if dept.code == data.department:
                self.cbxDepartment.SetSelection(dept_selection)
            dept_selection += 1
    
    # Virtual event handlers, override them in your derived class
    def on_btn_new_role(self, event):
        event.Skip()
        CtrlUserRole.add_item(DataUserRole(0, 0, 1, ""))
        
        data = DataUserRole(CtrlUserRole.get_data_len() + 1, CtrlUserRole.get_id(), 0, "")
        self.model.data.append(data)
        item = self.model.ObjectToItem(data)
        self.dataViewRole.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
    
    def on_btn_delete_role(self, event):
        event.Skip()
        item = self.dataViewRole.GetCurrentItem()
        data = self.model.ItemToObject(item)
        self.model.data.remove(data)
        self.dataViewRole.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
        CtrlUserRole.delete_item(data)
    
    def on_btn_save_role(self, event):
        event.Skip()
        item = self.dataViewRole.GetCurrentItem()
        data = self.model.ItemToObject(item)
        CtrlUserRole.update_item(data)
    
    def on_btn_save(self, event):
        event.Skip()
        department = self.cbxDepartment.GetClientData(self.cbxDepartment.GetSelection())
        if self.radioBtnMale.GetValue():
            sex_type = 0
        else:
            sex_type = 1
            
        if self.radioBtnOnDuty.GetValue():
            state_type = 0
        else:
            state_type = 1
            
        data = DataEmployee(self.user_id, 0,
                            self.txtCode.GetValue(),
                            self.txtName.GetValue(),
                            self.dateBirthDay.GetValue().Format("%Y-%m-%d %H:%M:%S"),
                            self.txtDuty.GetValue(),
                            department.code,
                            sex_type,
                            int(self.txtTelephone.GetValue()),
                            self.txtIdCard.GetValue(),
                            state_type,
                            self.txtAddress.GetValue(),
                            self.txtEmail.GetValue(),
                            self.txtNote.GetValue())
        
        if self.type == "add":
            CtrlEmployee.add_item(data)
        elif self.type == "mod":
            CtrlEmployee.update_item(data)
    
    def on_btn_exit(self, event):
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
        self.btnNew.SetMinSize(wx.Size(50, 50))
        sizer.Add(self.btnNew, 0, 0, 5)
        # Add modify button
        self.btnModify = wx.Button(self, wx.ID_ANY, u"修改", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnModify.SetMinSize(wx.Size(50, 50))
        sizer.Add(self.btnModify, 0, 0, 5)
        # Add delete button
        self.btnDelete = wx.Button(self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnDelete.SetMinSize(wx.Size(50, 50))
        sizer.Add(self.btnDelete, 0, 0, 5)
        # Add department setting button
        self.btnDepartment = wx.Button(self, wx.ID_ANY, u"行政部门", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnDepartment.SetFont(wx.Font(8, 70, 90, 90, False, wx.EmptyString))
        self.btnDepartment.SetMinSize(wx.Size(50, 50))
        sizer.Add(self.btnDepartment, 0, 0, 5)
        # Add refresh button
        self.btnRefresh = wx.Button(self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnRefresh.SetMinSize(wx.Size(50, 50))
        sizer.Add(self.btnRefresh, 0, 0, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnExit.SetMinSize(wx.Size(50, 50))
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
        tree_sizer = wx.BoxSizer(wx.VERTICAL)
        tree_sizer.SetMinSize(wx.Size(200, 600))
        self.treeCtrl = wx.TreeCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 600), wx.TR_DEFAULT_STYLE)
        tree_sizer.Add(self.treeCtrl, 0, wx.EXPAND, 5)
        sizer.Add(tree_sizer, 1, 0, 5)
        # Add data view list
        view_sizer = wx.BoxSizer(wx.VERTICAL)
        view_sizer.SetMinSize(wx.Size(600, 600))
        self.dataViewList = wx.dataview.DataViewCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.dataViewList.SetMinSize(wx.Size(-1, 600))
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
        view_sizer.Add(self.dataViewList, 0, wx.EXPAND | wx.LEFT, 5)
        sizer.Add(view_sizer, 1, 0, 5)

        # Layout 
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition,
                          size=wx.Size(800, 600), style=wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_status_bar_sizer(sizer)
        self._init_view_sizer(sizer) 

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Create an instance of our model...
        self.model = ModelEmployee(CtrlEmployee.get_data())
        CtrlEmployee.refresh_items()
        
        # Tell the DVC to use the model
        self.dataViewList.AssociateModel(self.model)

        # Connect Events
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.btnNew.Bind(wx.EVT_BUTTON, self.on_btn_new)
        self.btnModify.Bind(wx.EVT_BUTTON, self.on_btn_modify)
        self.btnDelete.Bind(wx.EVT_BUTTON, self.on_btn_delete)
        self.btnDepartment.Bind(wx.EVT_BUTTON, self.on_btn_department)
        self.btnRefresh.Bind(wx.EVT_BUTTON, self.on_btn_refresh)
        self.btnExit.Bind(wx.EVT_BUTTON, self.on_btn_exit)
        
        # Show tree control
        self._show_tree_ctrl()
    
    def __del__(self):
        pass
    
    def initialize(self):
        # Add event listener
        EvtManager.add_listener(self, EnumEvent.EVT_EMPLOYEE_REFRESH, self.on_btn_refresh)
        
        x, y = CtrlHomePage.get_screen_size()
        self.SetSize(wx.Size(x, y))

    def un_initialize(self):
        # Remove event listener
        EvtManager.remove_listener(self, EnumEvent.EVT_EMPLOYEE_REFRESH, self.on_btn_refresh)
    
    def _show_tree_ctrl(self):
        isz = (16, 16)
        il = wx.ImageList(isz[0], isz[1])
        fl_idx = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, isz))
        fl_open_idx = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER_OPEN, wx.ART_OTHER, isz))
        file_idx = il.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, isz))
        
        self.treeCtrl.SetImageList(il)
        self.il = il

        self.root = self.treeCtrl.AddRoot(u"全部行政部门")
        self.treeCtrl.SetPyData(self.root, None)
        self.treeCtrl.SetItemImage(self.root, fl_idx, wx.TreeItemIcon_Normal)
        self.treeCtrl.SetItemImage(self.root, fl_open_idx, wx.TreeItemIcon_Expanded)
        
        department_map = dict()
        li_items = CtrlEmployee.get_items()
        for item in li_items:
            if item.department in department_map:
                department_map[item.department].append(item)
            else:
                list_tmp = list()
                list_tmp.append(item)
                department_map_tmp = {item.department: list_tmp}
                department_map.update(department_map_tmp)
        
        li_department = CtrlDepartment.get_data()
        for dept in li_department:
            if dept.code in department_map:
                title = "%s(%d)" % (dept.name, len(department_map[dept.code]))
                child = self.treeCtrl.AppendItem(self.root, title)
                self.treeCtrl.SetPyData(child, None)
                self.treeCtrl.SetItemImage(child, fl_idx, wx.TreeItemIcon_Normal)
                self.treeCtrl.SetItemImage(child, fl_open_idx, wx.TreeItemIcon_Expanded)
                for employee_info in department_map[dept.code]:
                    sub_child = self.treeCtrl.AppendItem(child, employee_info.name)
                    self.treeCtrl.SetPyData(sub_child, None)
                    self.treeCtrl.SetItemImage(sub_child, file_idx, wx.TreeItemIcon_Normal)
                    self.treeCtrl.SetItemImage(sub_child, file_idx, wx.TreeItemIcon_Selected)
            else:
                title = "%s(0)" % dept.name
                child = self.treeCtrl.AppendItem(self.root, title)
                self.treeCtrl.SetPyData(child, None)
                self.treeCtrl.SetItemImage(child, fl_idx, wx.TreeItemIcon_Normal)
                self.treeCtrl.SetItemImage(child, fl_open_idx, wx.TreeItemIcon_Expanded)
                
        self.treeCtrl.Expand(self.root)
        
    def _refresh_ui(self):
        # Refresh treeCtrl
        CtrlEmployee.refresh_items()
        self.treeCtrl.DeleteAllItems()
        self._show_tree_ctrl()
        
        # Refresh data view list
        result = CtrlEmployee.get_data()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
                    
        self.model.Cleared()
    
    # Virtual event handlers, override them in your derived class
    def on_size(self, event):
        event.Skip()
        x, y = self.GetSize()

        self.btnNew.SetMaxSize(wx.Size(50, 50))
        self.btnModify.SetMaxSize(wx.Size(50, 50))
        self.btnDelete.SetMaxSize(wx.Size(50, 50))
        self.btnDepartment.SetMaxSize(wx.Size(50, 50))
        self.btnRefresh.SetMaxSize(wx.Size(50, 50))
        self.btnExit.SetMaxSize(wx.Size(50, 50))
        self.topPanel.SetMaxSize(wx.Size(x-300, 50))
        self.treeCtrl.SetMinSize(wx.Size(200, y-50))
        self.dataViewList.SetMinSize(wx.Size(x-200, y-50))
        
    def on_btn_new(self, event):
        event.Skip()
        pop_employee = PopEmployee(self, "add")
        pop_employee.ShowModal()
    
    def on_btn_modify(self, event):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        index = self.model.data.index(data)
        CtrlEmployee.set_cur_item_index(index)
        pop_employee = PopEmployee(self, "mod")
        pop_employee.ShowModal()
    
    def on_btn_delete(self, event):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        self.model.data.remove(data)
        self.dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
        CtrlEmployee.delete_item(data)
    
    def on_btn_department(self, event):
        event.Skip()
        pop_department = PopDepartment(self)
        pop_department.ShowModal()
    
    def on_btn_refresh(self, event):
        event.Skip()
        self._refresh_ui()
    
    def on_btn_exit(self, event):
        event.Skip()
        self.Hide()
        AppManager.switch_to_application('HomePage')
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = WgtEmployee(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()