#!/usr/bin/env python
# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
from app.home_logic import CtrlHomePage
from app.manager.logic.ctrl import * 
from app.manager.logic.model import *
from app.manager.logic.data import *
from app.app_manager import AppManager
from framework.core import TreeImage
from framework.img_button import ImgButton

import wx
import wx.xrc
import wx.dataview
from wx.dataview import DataViewColumn

import sys

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
        self.model = ModelDepartment(CtrlDepartment.get_instance().get_data())
        
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
        CtrlDepartment.get_instance().add_item(DataDepartment(0, 0, ""))
        
        data = DataDepartment(CtrlDepartment.get_instance().get_data_len() + 1,
                              CtrlDepartment.get_instance().get_id(), "")
        self.model.data.append(data)
        item = self.model.ObjectToItem(data)
        self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
    
    def on_btn_delete(self, event):
        event.Skip()
        try:
            item = self.dataViewList.GetCurrentItem()
            data = self.model.ItemToObject(item)
            CtrlDepartment.get_instance().delete_item(data)
            self.model.data.remove(data)
            self.dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
        except Exception, ex:
            print Exception, ":", ex
            pop_error = wx.MessageDialog(self, u"该部门不能删除", caption=u"行政部门")
            pop_error.ShowModal()
    
    def on_btn_refresh(self, event):
        event.Skip()
        result = CtrlDepartment.get_instance().get_data()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
                    
        self.model.Cleared()
    
    def on_btn_save(self, event):
        event.Skip()
        for data in self.model.data:
            CtrlDepartment.get_instance().update_item(data)
    
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
        notebook.AddPage(role_panel, u"权限设置", False)

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
        s_txt_password = wx.StaticText(container, wx.ID_ANY, u"初始密码：", wx.DefaultPosition, wx.Size(80, -1), 0)
        s_txt_password.Wrap(-1)
        s_txt_password.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        id_sizer.Add(s_txt_password, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add ID number text control
        self.txtPassword = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        id_sizer.Add(self.txtPassword, 0, wx.ALIGN_CENTER | wx.ALL, 5)
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
                                              style=wx.DP_DROPDOWN | wx.DP_SHOWCENTURY)
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
        g_sizer.Add(sex_sizer, 1, wx.EXPAND, 5)

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
        g_sizer = wx.GridSizer(4, 1, 0, 0)

        # Add employee's id card sizer
        id_card_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add address label
        s_txt_id_card = wx.StaticText(container, wx.ID_ANY, u"身份证号：", wx.DefaultPosition, wx.Size(80, -1), 0)
        s_txt_id_card.Wrap(-1)
        s_txt_id_card.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        s_txt_id_card.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_CAPTIONTEXT))
        id_card_sizer.Add(s_txt_id_card, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add address text control
        self.txtIdCard = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400, -1), 0)
        id_card_sizer.Add(self.txtIdCard, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Layout id card sizer
        g_sizer.Add(id_card_sizer, 1, wx.EXPAND, 5)

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
        self.dataViewRole.AppendTextColumn(u"员工角色", 3)
        self.dataViewRole.AppendToggleColumn(u"状态", 5, width=80, mode=wx.dataview.DATAVIEW_CELL_ACTIVATABLE)
        data_sizer.Add(self.dataViewRole, 0, wx.EXPAND, 5)
        # Layout data view list
        parent.Add(data_sizer, 1, wx.EXPAND, 5)

        # Add control buttons sizer
        ctrl_sizer = wx.BoxSizer(wx.VERTICAL)
        ctrl_sizer.SetMinSize(wx.Size(600, 300))
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
        
        # Connect Events
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
            self.index = CtrlEmployee.get_instance().get_cur_item_index()
            self._init_mod_view()
            
    def _init_add_view(self):
        li_department = CtrlDepartment.get_instance().get_data()
        for dept in li_department:
            self.cbxDepartment.Append(dept.name, dept)
        self.cbxDepartment.SetSelection(0)
        
        self.radioBtnMale.SetValue(True)
        self.radioBtnOnDuty.SetValue(True)

        # Create an instance of our model...
        self.model = ModelUserRole(CtrlUserRole.get_instance().get_data())

        # Tell the DVC to use the model
        self.dataViewRole.AssociateModel(self.model)
        
    def _init_mod_view(self):
        self.txtCode.Enable(False)
        self.txtPassword.Enable(False)
        if self.index < 0:
            self.index = 0
            return
        
        items = CtrlEmployee.get_instance().get_items()
        if self.index >= len(items):
            self.index = len(items) - 1
            return
        
        data = items[self.index]
        # Create an instance of our model...
        self.model = ModelUserRole(CtrlUserRole.get_instance().get_data_by_user(data))

        # Tell the DVC to use the model
        self.dataViewRole.AssociateModel(self.model)

        self.user_id = data.key
        self.txtCode.SetValue(str(data.code))
        self.txtName.SetValue(data.name)
        self.txtDuty.SetValue(data.duty)
        self.txtTelephone.SetValue(str(data.telephone))
        self.txtIdCard.SetValue(data.id_card)
        self.txtAddress.SetValue(data.address)
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

        if data.birthday is not None:
            birth_day = wx.DateTimeFromDMY(data.birthday.day, data.birthday.month - 1, data.birthday.year)
            self.dateBirthDay.SetValue(birth_day)

        li_department = CtrlDepartment.get_instance().get_data()
        for dept in li_department:
            self.cbxDepartment.Append(dept.name, dept)
            if dept.key == data.department:
                self.cbxDepartment.SetSelection(li_department.index(dept))
    
    # Virtual event handlers, override them in your derived class
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

        data = DataEmployee(0, self.user_id,
                            self.txtCode.GetValue(),
                            self.txtName.GetValue(),
                            self.dateBirthDay.GetValue().Format("%Y-%m-%d %H:%M:%S"),
                            self.txtDuty.GetValue(),
                            self.txtPassword.GetValue(),
                            department.key,
                            sex_type,
                            self.txtTelephone.GetValue(),
                            self.txtIdCard.GetValue(),
                            state_type,
                            self.txtAddress.GetValue(),
                            self.txtEmail.GetValue(),
                            self.txtNote.GetValue())
        
        if self.type == "add":
            CtrlEmployee.get_instance().add_item(data, self.model.data)
        elif self.type == "mod":
            CtrlEmployee.get_instance().update_item(data, self.model.data)
    
    def on_btn_exit(self, event):
        event.Skip()
        self.Close()

###########################################################################
## Class PopPermission
###########################################################################
li_func_type = [u"餐厅设置", u"菜品发布", u"员工管理", u"报表中心", u"打印设置", u"系统设置"]


class PopPermission (wx.Dialog):
    def _init_info_sizer(self, parent):
        sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u""), wx.HORIZONTAL)
        sizer.SetMinSize(wx.Size(600, 50))

        # Add label for dishes code
        s_txt_name = wx.StaticText(self, wx.ID_ANY, u"名称：", wx.DefaultPosition, wx.DefaultSize, 0)
        s_txt_name.Wrap(-1)
        sizer.Add(s_txt_name, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add text control for dishes code
        self.txtRoleName = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.txtRoleName, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Add label for dishes code
        s_txt_desc = wx.StaticText(self, wx.ID_ANY, u"备注：", wx.DefaultPosition, wx.DefaultSize, 0)
        s_txt_desc.Wrap(-1)
        sizer.Add(s_txt_desc, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add text control for dishes code
        self.txtRoleDesc = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
        sizer.Add(self.txtRoleDesc, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_data_view_sizer(self, parent):
        sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u""), wx.HORIZONTAL)
        sizer.SetMinSize(wx.Size(600, 300))

        # Create tree control sizer
        left_sizer = wx.BoxSizer(wx.VERTICAL)
        left_sizer.SetMinSize(wx.Size(200, 300))

        self.treeCtrl = wx.TreeCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE)
        self.treeCtrl.SetMinSize(wx.Size(-1, 300))
        left_sizer.Add(self.treeCtrl, 0, wx.EXPAND, 5)

        sizer.Add(left_sizer, 1, 0, 5)

        # Create data view list sizer
        right_sizer = wx.BoxSizer(wx.VERTICAL)
        right_sizer.SetMinSize(wx.Size(400, 300))

        self.dataViewList = wx.dataview.DataViewCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.dataViewList.SetMinSize(wx.Size(-1, 300))

        self.dataViewList.AppendTextColumn(u"行号", 0)
        self.dataViewList.AppendTextColumn(u"所属类别", 1)
        self.dataViewList.AppendTextColumn(u"权限名称", 2)
        self.dataViewList.AppendToggleColumn(u"状态", 3, width=100, mode=wx.dataview.DATAVIEW_CELL_ACTIVATABLE)
        right_sizer.Add(self.dataViewList, 0, wx.EXPAND | wx.LEFT, 5)

        sizer.Add(right_sizer, 1, 0, 5)

        # Layout data view sizer
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_ctrl_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.SetMinSize(wx.Size(600, 50))

        panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        panel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))

        sizer.Add(panel, 1, wx.EXPAND, 5)
        # Add save button
        self.btnSave = wx.Button(self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnSave, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnExit, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        parent.Add(sizer, 1, wx.EXPAND, 5)

    def __init__(self, parent, type_="add"):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"权限设置", pos=wx.DefaultPosition,
                           size=wx.Size(600, 470), style=wx.CAPTION)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_info_sizer(sizer)
        self._init_data_view_sizer(sizer)
        self._init_ctrl_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.btnSave.Bind(wx.EVT_BUTTON, self.on_btn_save)
        self.btnExit.Bind(wx.EVT_BUTTON, self.on_btn_exit)

        # Initialize
        self.perm_id = 0
        self.index = 0
        self.type = type_
        self._initialize_view()
        self._show_tree_ctrl()

    def __del__(self):
        pass

    def _initialize_view(self):
        if self.type == "add":
            self._init_add_view()
        elif self.type == "mod":
            self.index = CtrlUserRole.get_instance().get_cur_item_index()
            self._init_mod_view()

    def _init_add_view(self):
        # Create an instance of our model...
        self.model = ModelPermList(CtrlPermList.get_instance().get_data())

        # Tell the DVC to use the model
        self.dataViewList.AssociateModel(self.model)

    def _init_mod_view(self):
        self.txtRoleName.Enable(False)
        if self.index < 0:
            self.index = 0
            return

        items = CtrlUserRole.get_instance().get_data()
        if self.index >= len(items):
            self.index = len(items) - 1
            return

        data = items[self.index]
        self.perm_id = data.key
        # Create an instance of our model...
        self.model = ModelPermList(CtrlPermList.get_instance().get_data_by_group(data))

        # Tell the DVC to use the model
        self.dataViewList.AssociateModel(self.model)

        self.txtRoleName.SetValue(data.name)
        self.txtRoleDesc.SetValue(data.desc if data.desc is not None else '')

    def _show_tree_ctrl(self):
        tree_image = TreeImage()
        self.treeCtrl.SetImageList(tree_image.image_list)
        self.il = tree_image.image_list

        self.root = self.treeCtrl.AddRoot(u"全部功能类别")
        self.treeCtrl.SetPyData(self.root, None)
        self.treeCtrl.SetItemImage(self.root, tree_image.folder_idx, wx.TreeItemIcon_Normal)
        self.treeCtrl.SetItemImage(self.root, tree_image.folder_open_idx, wx.TreeItemIcon_Expanded)

        for func_type in li_func_type:
            child = self.treeCtrl.AppendItem(self.root, func_type)
            self.treeCtrl.SetPyData(child, None)
            self.treeCtrl.SetItemImage(child, tree_image.folder_idx, wx.TreeItemIcon_Normal)
            self.treeCtrl.SetItemImage(child, tree_image.folder_open_idx, wx.TreeItemIcon_Expanded)

        self.treeCtrl.Expand(self.root)

    # Virtual event handlers, override them in your derived class
    def on_btn_save(self, event):
        event.Skip()
        data = DataUserRole(0, self.perm_id, '0',
                            self.txtRoleName.GetValue(),
                            self.txtRoleDesc.GetValue())

        if self.type == "add":
            CtrlUserRole.get_instance().add_item(data, self.model.data)
        elif self.type == "mod":
            CtrlUserRole.get_instance().update_item(data, self.model.data)

    def on_btn_exit(self, event):
        event.Skip()
        self.Close()
        
###########################################################################
## Class WgtEmployee
###########################################################################


class WgtEmployee (wx.Panel):
    def _init_status_bar_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.SetMinSize(wx.Size(-1, 82))
        # Add fix space panel
        self.topPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        sizer.Add(self.topPanel, 1, wx.EXPAND, 5)
        # Add new button
        self.btnNew = ImgButton(self.topPanel, u"new.png", u"s_new.png")
        # Add modify button
        self.btnModify = ImgButton(self.topPanel, u"modify.png", u"s_modify.png")
        # Add delete button
        self.btnDelete = ImgButton(self.topPanel, u"delete.png", u"s_delete.png")
        # Add department setting button
        self.btnDepartment = ImgButton(self.topPanel, u"department.png", u"s_department.png")
        # Add refresh button
        self.btnRefresh = ImgButton(self.topPanel, u"refresh.png", u"s_refresh.png")
        # Add exit button
        self.btnExit = ImgButton(self.topPanel, u"tool_exit.png", u"s_tool_exit.png")
        
        # Layout status bar 
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_view_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # Add a tree control
        tree_sizer = wx.BoxSizer(wx.VERTICAL)
        tree_sizer.SetMinSize(wx.Size(200, 600))
        self.treeCtrl = wx.TreeCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 600), wx.TR_DEFAULT_STYLE)
        self.treeCtrl.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
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
        self.dataViewList.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        view_sizer.Add(self.dataViewList, 0, wx.EXPAND | wx.LEFT, 5)
        sizer.Add(view_sizer, 1, 0, 5)

        # Layout 
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(800, 600),
                          style=wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(0x51, 0x1c, 0x0a))
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_status_bar_sizer(sizer)
        self._init_view_sizer(sizer) 

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.btnNew.Bind(wx.EVT_BUTTON, self.on_btn_new)
        self.btnModify.Bind(wx.EVT_BUTTON, self.on_btn_modify)
        self.btnDelete.Bind(wx.EVT_BUTTON, self.on_btn_delete)
        self.btnDepartment.Bind(wx.EVT_BUTTON, self.on_btn_department)
        self.btnRefresh.Bind(wx.EVT_BUTTON, self.on_btn_refresh)
        self.btnExit.Bind(wx.EVT_BUTTON, self.on_btn_exit)

        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.on_sel_changed, self.treeCtrl)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.on_activate, self.treeCtrl)
        
        # define variable
        self.model = None
        self.tree_data = None
    
    def __del__(self):
        pass
    
    def initialize(self):
        # Create an instance of our model...
        self.model = ModelEmployee(CtrlEmployee.get_instance().get_data())
        CtrlEmployee.get_instance().refresh_items()
        # Tell the DVC to use the model
        self.dataViewList.AssociateModel(self.model)
        # Show tree control
        self._show_tree_ctrl()

        # Add event listener
        EvtManager.add_listener(self, EnumEvent.EVT_EMPLOYEE_REFRESH, self.on_btn_refresh)
        
        x, y = CtrlHomePage.get_instance().get_screen_size()
        self.SetSize(wx.Size(x, y))

    def un_initialize(self):
        # Remove event listener
        EvtManager.remove_listener(self, EnumEvent.EVT_EMPLOYEE_REFRESH, self.on_btn_refresh)
    
    def _show_tree_ctrl(self):
        self.treeCtrl.DeleteAllItems()
        tree_image = TreeImage()
        self.treeCtrl.SetImageList(tree_image.image_list)
        self.il = tree_image.image_list

        self.root = self.treeCtrl.AddRoot(u"全部行政部门")
        self.treeCtrl.SetPyData(self.root, None)
        self.treeCtrl.SetItemImage(self.root, tree_image.folder_idx, wx.TreeItemIcon_Normal)
        self.treeCtrl.SetItemImage(self.root, tree_image.folder_open_idx, wx.TreeItemIcon_Expanded)
        
        department_map = dict()
        li_items = CtrlEmployee.get_instance().get_items()
        for item in li_items:
            if item.department in department_map:
                department_map[item.department].append(item)
            else:
                list_tmp = list()
                list_tmp.append(item)
                department_map_tmp = {item.department: list_tmp}
                department_map.update(department_map_tmp)
        
        li_department = CtrlDepartment.get_instance().get_data()
        for dept in li_department:
            if dept.key in department_map:
                title = "%s(%d)" % (dept.name, len(department_map[dept.key]))
                child = self.treeCtrl.AppendItem(self.root, title)
                self.treeCtrl.SetPyData(child, dept)
                self.treeCtrl.SetItemImage(child, tree_image.folder_idx, wx.TreeItemIcon_Normal)
                self.treeCtrl.SetItemImage(child, tree_image.folder_open_idx, wx.TreeItemIcon_Expanded)
                for employee_info in department_map[dept.key]:
                    sub_child = self.treeCtrl.AppendItem(child, employee_info.name)
                    self.treeCtrl.SetPyData(sub_child, employee_info)
                    self.treeCtrl.SetItemImage(sub_child, tree_image.file_idx, wx.TreeItemIcon_Normal)
                    self.treeCtrl.SetItemImage(sub_child, tree_image.file_idx, wx.TreeItemIcon_Selected)
            else:
                title = "%s(0)" % dept.name
                child = self.treeCtrl.AppendItem(self.root, title)
                self.treeCtrl.SetPyData(child, None)
                self.treeCtrl.SetItemImage(child, tree_image.folder_idx, wx.TreeItemIcon_Normal)
                self.treeCtrl.SetItemImage(child, tree_image.folder_open_idx, wx.TreeItemIcon_Expanded)
                
        self.treeCtrl.Expand(self.root)
        
    def _refresh_ui(self):
        # Refresh treeCtrl
        CtrlEmployee.get_instance().refresh_items()
        self.treeCtrl.DeleteAllItems()
        self._show_tree_ctrl()
        
        # Refresh data view list
        result = CtrlEmployee.get_instance().get_data()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
                    
        self.model.Cleared()
    
    # Virtual event handlers, override them in your derived class
    def on_paint(self, event):
        dc = wx.ClientDC(self.topPanel)
        dc.Clear()

        sz = self.GetClientSize()
        bg_img = wx.Image(sys.path[0] + "\\..\\image\\top_bg.png", wx.BITMAP_TYPE_PNG).Scale(sz.x, 82)
        bg_bmp = bg_img.ConvertToBitmap()

        mem_dc = wx.MemoryDC()
        mem_dc.SelectObject(bg_bmp)
        dc.Blit(0, 0,
                bg_bmp.GetWidth(), bg_bmp.GetHeight(),
                mem_dc, 0, 0, wx.COPY, True)

        self._refresh_btns()

    def _refresh_btns(self):
        self.btnNew.Refresh()
        self.btnModify.Refresh()
        self.btnDelete.Refresh()
        self.btnDepartment.Refresh()
        self.btnRefresh.Refresh()
        self.btnExit.Refresh()

    def on_size(self, event):
        event.Skip()
        x, y = self.GetSize()

        self.btnNew.SetSize(wx.Size(63, 70))
        self.btnNew.SetPosition(wx.Point(0, 6))

        self.btnModify.SetSize(wx.Size(63, 70))
        self.btnModify.SetPosition(wx.Point(65, 6))

        self.btnDelete.SetSize(wx.Size(63, 70))
        self.btnDelete.SetPosition(wx.Point(130, 6))

        self.btnDepartment.SetSize(wx.Size(103, 70))
        self.btnDepartment.SetPosition(wx.Point(195, 6))

        self.btnRefresh.SetSize(wx.Size(63, 70))
        self.btnRefresh.SetPosition(wx.Point(300, 6))

        self.btnExit.SetSize(wx.Size(63, 70))
        self.btnExit.SetPosition(wx.Point(365, 6))

        self.topPanel.SetMaxSize(wx.Size(x, 82))
        self.treeCtrl.SetMinSize(wx.Size(200, y-82))
        self.dataViewList.SetMinSize(wx.Size(x-200, y-82))

        self.Refresh()
        
    def on_btn_new(self, event):
        event.Skip()
        pop_employee = PopEmployee(self, "add")
        pop_employee.ShowModal()
    
    def on_btn_modify(self, event):
        event.Skip()
        try:
            item = self.dataViewList.GetCurrentItem()
            try:
                data = self.model.ItemToObject(item)
            except Exception, ex:
                print Exception, ":", ex
                for item_ in self.model.data:
                    if item_.key == self.tree_data.key:
                        data = item_
            index_ = self.model.data.index(data)
            CtrlEmployee.get_instance().set_cur_item_index(index_)
            pop_employee = PopEmployee(self, "mod")
            pop_employee.ShowModal()
        except Exception, ex:
            print Exception, ":", ex
            print 'WgtEmployee: on_btn_modify error'
    
    def on_btn_delete(self, event):
        event.Skip()
        try:
            item = self.dataViewList.GetCurrentItem()
            try:
                data = self.model.ItemToObject(item)
            except:
                for item_ in self.model.data:
                    if item_.key == self.tree_data.key:
                        data = item_
            self.model.data.remove(data)
            self.dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
            CtrlEmployee.get_instance().delete_item(data)
        except:
            print 'WgtEmployee: on_btn_delete error'
    
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
        AppManager.get_instance().switch_to_application('HomePage')

    def on_sel_changed(self, event):
        event.Skip()
        self.tree_data = self.treeCtrl.GetPyData(event.GetItem())

    def on_activate(self, event):
        event.Skip()
        self.tree_data = self.treeCtrl.GetPyData(event.GetItem())
        if isinstance(self.tree_data, DataEmployee):
            self.on_btn_modify(event)

###########################################################################
## Class WgtPermission
###########################################################################
li_group_type = [u"默认组", u"自定义组"]


class WgtPermission (wx.Panel):
    def _init_status_bar_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.SetMinSize(wx.Size(-1, 82))
        # Add fix space panel
        self.topPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        sizer.Add(self.topPanel, 1, wx.EXPAND, 5)
        # Add new button
        self.btnNew = ImgButton(self.topPanel, u"new.png", u"s_new.png")
        # Add modify button
        self.btnModify = ImgButton(self.topPanel, u"modify.png", u"s_modify.png")
        # Add delete button
        self.btnDelete = ImgButton(self.topPanel, u"delete.png", u"s_delete.png")
        # Add refresh button
        self.btnRefresh = ImgButton(self.topPanel, u"refresh.png", u"s_refresh.png")
        # Add exit button
        self.btnExit = ImgButton(self.topPanel, u"tool_exit.png", u"s_tool_exit.png")

        # Layout buttons
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_data_view_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.SetMinSize(wx.Size(800, 550))

        # Add tree control sizer
        left_sizer = wx.BoxSizer(wx.VERTICAL)
        left_sizer.SetMinSize(wx.Size(200, 550))
        self.treeCtrl = wx.TreeCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE)
        self.treeCtrl.SetMinSize(wx.Size(-1, 600))
        self.treeCtrl.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        left_sizer.Add(self.treeCtrl, 0, wx.EXPAND, 5)

        sizer.Add(left_sizer, 1, 0, 5)

        # Add data view list sizer
        right_sizer = wx.BoxSizer(wx.VERTICAL)
        right_sizer.SetMinSize(wx.Size(600, 550))
        self.dataViewList = wx.dataview.DataViewCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.dataViewList.SetMinSize(wx.Size(-1, 600))

        self.dataViewList.AppendTextColumn(u"行号", 0)
        self.dataViewList.AppendTextColumn(u"编码", 1)
        self.dataViewList.AppendTextColumn(u"类型", 2)
        self.dataViewList.AppendTextColumn(u"名称", 3)
        self.dataViewList.AppendTextColumn(u"备注", 4)
        self.dataViewList.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))
        right_sizer.Add(self.dataViewList, 0, wx.EXPAND | wx.LEFT, 5)

        sizer.Add(right_sizer, 1, 0, 5)

        # Layout
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition,
                          size=wx.Size(800, 600), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(0x51, 0x1c, 0x0a))

        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_status_bar_sizer(sizer)
        self._init_data_view_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.btnNew.Bind(wx.EVT_BUTTON, self.on_btn_new)
        self.btnModify.Bind(wx.EVT_BUTTON, self.on_btn_modify)
        self.btnDelete.Bind(wx.EVT_BUTTON, self.on_btn_delete)
        self.btnRefresh.Bind(wx.EVT_BUTTON, self.on_btn_refresh)
        self.btnExit.Bind(wx.EVT_BUTTON, self.on_btn_exit)

        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.on_sel_changed, self.treeCtrl)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.on_activate, self.treeCtrl)

        #define variable
        self.model = None
        self.tree_data = None

    def __del__(self):
        pass

    def initialize(self):
         # Create an instance of our model...
        self.model = ModelUserRole(CtrlUserRole.get_instance().get_data())
        CtrlUserRole.get_instance().refresh_items()
        # Tell the DVC to use the model
        self.dataViewList.AssociateModel(self.model)
         # Show tree control
        self._show_tree_ctrl()

        # Add event listener
        EvtManager.add_listener(self, EnumEvent.EVT_PERMISSION_REFRESH, self.on_btn_refresh)

        x, y = CtrlHomePage.get_instance().get_screen_size()
        self.SetSize(wx.Size(x, y))

    def un_initialize(self):
        # Remove event listener
        EvtManager.remove_listener(self, EnumEvent.EVT_PERMISSION_REFRESH, self.on_btn_refresh)

    def _show_tree_ctrl(self):
        self.treeCtrl.DeleteAllItems()
        tree_image = TreeImage()
        self.treeCtrl.SetImageList(tree_image.image_list)
        self.il = tree_image.image_list

        self.root = self.treeCtrl.AddRoot(u"全部分组")
        self.treeCtrl.SetPyData(self.root, None)
        self.treeCtrl.SetItemImage(self.root, tree_image.folder_idx, wx.TreeItemIcon_Normal)
        self.treeCtrl.SetItemImage(self.root, tree_image.folder_open_idx, wx.TreeItemIcon_Expanded)

        li_role = CtrlUserRole.get_instance().get_data()
        for group_type in li_group_type:
            child = self.treeCtrl.AppendItem(self.root, group_type)
            self.treeCtrl.SetPyData(child, None)
            self.treeCtrl.SetItemImage(child, tree_image.folder_idx, wx.TreeItemIcon_Normal)
            self.treeCtrl.SetItemImage(child, tree_image.folder_open_idx, wx.TreeItemIcon_Expanded)
            if group_type == u"默认组":
                for role in li_role:
                    if role.type == '1':
                        sub_child = self.treeCtrl.AppendItem(child, role.name)
                        self.treeCtrl.SetPyData(sub_child, role)
                        self.treeCtrl.SetItemImage(sub_child, tree_image.file_idx, wx.TreeItemIcon_Normal)
                        self.treeCtrl.SetItemImage(sub_child, tree_image.file_idx, wx.TreeItemIcon_Selected)
            else:
                for role in li_role:
                    if role.type == '0':
                        sub_child = self.treeCtrl.AppendItem(child, role.name)
                        self.treeCtrl.SetPyData(sub_child, role)
                        self.treeCtrl.SetItemImage(sub_child, tree_image.file_idx, wx.TreeItemIcon_Normal)
                        self.treeCtrl.SetItemImage(sub_child, tree_image.file_idx, wx.TreeItemIcon_Selected)

        self.treeCtrl.Expand(self.root)

    def _refresh_ui(self):
        # Refresh treeCtrl
        CtrlUserRole.get_instance().refresh_items()
        self.treeCtrl.DeleteAllItems()
        self._show_tree_ctrl()

        # Refresh data view list
        result = CtrlUserRole.get_instance().get_data()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)

        self.model.Cleared()

    # Virtual event handlers, override them in your derived class
    def on_paint(self, event):
        dc = wx.ClientDC(self.topPanel)
        dc.Clear()

        sz = self.GetClientSize()
        bg_img = wx.Image(sys.path[0] + "\\..\\image\\top_bg.png", wx.BITMAP_TYPE_PNG).Scale(sz.x, 82)
        bg_bmp = bg_img.ConvertToBitmap()

        mem_dc = wx.MemoryDC()
        mem_dc.SelectObject(bg_bmp)
        dc.Blit(0, 0,
                bg_bmp.GetWidth(), bg_bmp.GetHeight(),
                mem_dc, 0, 0, wx.COPY, True)

        self._refresh_btns()

    def _refresh_btns(self):
        self.btnNew.Refresh()
        self.btnModify.Refresh()
        self.btnDelete.Refresh()
        self.btnRefresh.Refresh()
        self.btnExit.Refresh()

    def on_size(self, event):
        event.Skip()
        x, y = self.GetSize()

        self.btnNew.SetSize(wx.Size(63, 70))
        self.btnNew.SetPosition(wx.Point(0, 6))

        self.btnModify.SetSize(wx.Size(63, 70))
        self.btnModify.SetPosition(wx.Point(65, 6))

        self.btnDelete.SetSize(wx.Size(63, 70))
        self.btnDelete.SetPosition(wx.Point(130, 6))

        self.btnRefresh.SetSize(wx.Size(63, 70))
        self.btnRefresh.SetPosition(wx.Point(195, 6))

        self.btnExit.SetSize(wx.Size(63, 70))
        self.btnExit.SetPosition(wx.Point(260, 6))

        self.topPanel.SetSize(wx.Size(x, 82))
        self.treeCtrl.SetMinSize(wx.Size(200, y-82))
        self.dataViewList.SetMinSize(wx.Size(x-200, y-82))

        self.Refresh()

    def on_btn_new(self, event):
        event.Skip()
        pop_permission = PopPermission(self, "add")
        pop_permission.ShowModal()

    def on_btn_modify(self, event):
        event.Skip()
        try:
            item = self.dataViewList.GetCurrentItem()
            try:
                    data = self.model.ItemToObject(item)
            except:
                for item_ in self.model.data:
                    if item_.key == self.tree_data.key:
                        data = item_
            index_ = self.model.data.index(data)
            CtrlUserRole.get_instance().set_cur_item_index(index_)
            pop_permission = PopPermission(self, "mod")
            pop_permission.ShowModal()
        except:
            print 'WgtDiningTable: on_btn_modify error'

    def on_btn_delete(self, event):
        event.Skip()
        try:
            item = self.dataViewList.GetCurrentItem()
            try:
                data = self.model.ItemToObject(item)
            except:
                for item_ in self.model.data:
                    if item_.key == self.tree_data.key:
                        data = item_

            if data.type == '0':
                self.model.data.remove(data)
                self.dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
                CtrlUserRole.get_instance().delete_item(data)
        except:
            print 'WgtPermission: on_btn_delete error'

    def on_btn_refresh(self, event):
        event.Skip()
        self._refresh_ui()

    def on_btn_exit(self, event):
        event.Skip()
        self.Hide()
        AppManager.get_instance().switch_to_application('HomePage')

    def on_sel_changed(self, event):
        event.Skip()
        self.tree_data = self.treeCtrl.GetPyData(event.GetItem())

    def on_activate(self, event):
        event.Skip()
        self.tree_data = self.treeCtrl.GetPyData(event.GetItem())
        if isinstance(self.tree_data, DataUserRole):
            self.on_btn_modify(event)
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = WgtEmployee(None)
    frame = WgtPermission(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()