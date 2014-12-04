#!/usr/bin/env python
# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
from app.app_manager import AppManager
from app.manager.logic.ctrl import *
from app.manager.logic.data import *

import wx
import wx.xrc


###########################################################################
## Class PopCompany
###########################################################################


class PopCompany (wx.Dialog):
    def _init_view_sizer(self, parent):
        panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.STATIC_BORDER | wx.TAB_TRAVERSAL)
        panel.SetMinSize(wx.Size(-1, 300))

        # Create a 6 rows and 1 column grid sizer
        g_sizer = wx.GridSizer(6, 1, 0, 0)
        g_sizer.SetMinSize(wx.Size(-1, 300))

        # Add company name sizer
        name_sizer = wx.BoxSizer(wx.HORIZONTAL)
        s_txt_name = wx.StaticText(panel, wx.ID_ANY, u"名称：", wx.DefaultPosition, wx.Size(120, -1), wx.ALIGN_RIGHT)
        s_txt_name.Wrap(-1)
        s_txt_name.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        name_sizer.Add(s_txt_name, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtName = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(360, -1), 0)
        name_sizer.Add(self.txtName, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        g_sizer.Add(name_sizer, 1, wx.EXPAND, 5)
        # Add person in charge sizer
        person_sizer = wx.BoxSizer(wx.HORIZONTAL)
        s_txt_person = wx.StaticText(panel, wx.ID_ANY, u"负责人：", wx.DefaultPosition, wx.Size(120, -1), wx.ALIGN_RIGHT)
        s_txt_person.Wrap(-1)
        person_sizer.Add(s_txt_person, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtPerson = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(180, -1), 0)
        person_sizer.Add(self.txtPerson, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        g_sizer.Add(person_sizer, 1, wx.EXPAND, 5)
        # Add telephone sizer
        telephone_sizer = wx.BoxSizer(wx.HORIZONTAL)
        s_txt_telephone = wx.StaticText(panel, wx.ID_ANY, u"联系电话：", wx.DefaultPosition,
                                        wx.Size(120, -1), wx.ALIGN_RIGHT)
        s_txt_telephone.Wrap(-1)
        telephone_sizer.Add(s_txt_telephone, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtPhone = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(180, -1), 0)
        telephone_sizer.Add(self.txtPhone, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        g_sizer.Add(telephone_sizer, 1, wx.EXPAND, 5)
        # Add email sizer
        email_sizer = wx.BoxSizer(wx.HORIZONTAL)
        s_txt_email = wx.StaticText(panel, wx.ID_ANY, u"电子邮箱：", wx.DefaultPosition, wx.Size(120, -1), wx.ALIGN_RIGHT)
        s_txt_email.Wrap(-1)
        email_sizer.Add(s_txt_email, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtEmail = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(360, -1), 0)
        email_sizer.Add(self.txtEmail, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        g_sizer.Add(email_sizer, 1, wx.EXPAND, 5)
        # Add address sizer
        address_sizer = wx.BoxSizer(wx.HORIZONTAL)

        s_txt_address = wx.StaticText(panel, wx.ID_ANY, u"地址：", wx.DefaultPosition,
                                      wx.Size(120, -1), wx.ALIGN_RIGHT)
        s_txt_address.Wrap(-1)
        address_sizer.Add(s_txt_address, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        self.txtAddress = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(360, -1), 0)
        address_sizer.Add(self.txtAddress, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        g_sizer.Add(address_sizer, 1, wx.EXPAND, 5)

        # Layout
        panel.SetSizer(g_sizer)
        panel.Layout()
        g_sizer.Fit(panel)
        parent.Add(panel, 1, wx.EXPAND | wx.ALL, 5)

    def _init_ctrl_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Add spacer
        sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        # Add save button
        self.m_btnSave = wx.Button(self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.m_btnSave, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add exit button
        self.m_btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.m_btnExit, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Layout
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"公司信息", pos=wx.DefaultPosition,
                           size=wx.Size(600, 400), style=wx.CAPTION)
        
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_view_sizer(sizer)
        self._init_ctrl_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)
        
        # Connect Events
        self.m_btnSave.Bind(wx.EVT_BUTTON, self.on_btn_save)
        self.m_btnExit.Bind(wx.EVT_BUTTON, self.on_btn_exit)

        # Initialize
        self._init_info()
    
    def __del__(self):
        pass

    def _init_info(self):
        company_info = CtrlCompany.get_instance().get_company_info()
        if company_info is not None:
            self.txtName.SetValue(str(company_info.name))
            self.txtPerson.SetValue(str(company_info.person))
            self.txtPhone.SetValue(str(company_info.phone))
            self.txtAddress.SetValue(str(company_info.address))
            self.txtEmail.SetValue(str(company_info.email))

    # Virtual event handlers, override them in your derived class
    def on_btn_save(self, event):
        event.Skip()
        company_info = DataCompany(self.txtName.GetValue(), self.txtPerson.GetValue(), self.txtAddress.GetValue(),
                                   self.txtEmail.GetValue(), self.txtPhone.GetValue())
        CtrlCompany.get_instance().set_company_info(company_info)
    
    def on_btn_exit(self, event):
        event.Skip()
        self.Close()

###########################################################################
## Class PopRegister
###########################################################################


class PopRegister (wx.Dialog):
    def _init_application_sizer(self, parent):
        sb_sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"申请授权"), wx.VERTICAL)
        # Add data view sizer
        view_sizer = wx.BoxSizer(wx.VERTICAL)
        top_sizer_apply = wx.BoxSizer(wx.HORIZONTAL)

        s_txt_number = wx.StaticText(self, wx.ID_ANY, u"终端数：", wx.DefaultPosition, wx.DefaultSize, 0)
        s_txt_number.Wrap(-1)
        top_sizer_apply.Add(s_txt_number, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtTerminalNum = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        top_sizer_apply.Add(self.txtTerminalNum, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        view_sizer.Add(top_sizer_apply, 1, wx.ALIGN_CENTER, 5)

        sb_sizer.Add(view_sizer, 1, wx.EXPAND, 5)
        # Add control sizer
        ctrl_sizer = wx.BoxSizer(wx.VERTICAL)

        self.btnApply = wx.Button(self, wx.ID_ANY, u"申请", wx.DefaultPosition, wx.DefaultSize, 0)
        ctrl_sizer.Add(self.btnApply, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        sb_sizer.Add(ctrl_sizer, 1, wx.EXPAND, 5)

        # Layout
        parent.Add(sb_sizer, 1, wx.EXPAND, 5)

    def _init_verify_sizer(self, parent):
        sb_sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"验证码校验"), wx.VERTICAL)
        # Add data view sizer
        view_sizer = wx.BoxSizer(wx.VERTICAL)
        inner_verify_sizer = wx.BoxSizer(wx.HORIZONTAL)

        s_txt_code = wx.StaticText(self, wx.ID_ANY, u"验证码：", wx.DefaultPosition, wx.DefaultSize, 0)
        s_txt_code.Wrap(-1)
        inner_verify_sizer.Add(s_txt_code, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.txtKey = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400, -1), 0)
        inner_verify_sizer.Add(self.txtKey, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        view_sizer.Add(inner_verify_sizer, 1, wx.ALIGN_CENTER, 5)

        sb_sizer.Add(view_sizer, 1, wx.EXPAND, 5)
        # Add control sizer
        ctrl_sizer = wx.BoxSizer(wx.VERTICAL)

        self.btnVerify = wx.Button(self, wx.ID_ANY, u"确认", wx.DefaultPosition, wx.DefaultSize, 0)
        ctrl_sizer.Add(self.btnVerify, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        sb_sizer.Add(ctrl_sizer, 1, wx.EXPAND, 5)

        # Layout
        parent.Add(sb_sizer, 1, wx.EXPAND, 5)

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"注册", pos=wx.DefaultPosition,
                           size=wx.Size(600, 300), style=wx.DEFAULT_DIALOG_STYLE)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        
        g_sizer = wx.GridSizer(2, 1, 0, 0)
        self._init_application_sizer(g_sizer)
        self._init_verify_sizer(g_sizer)
        
        self.SetSizer(g_sizer)
        self.Layout()
        self.Centre(wx.BOTH)
        
        # Connect Events
        self.btnApply.Bind(wx.EVT_BUTTON, self.on_btn_apply)
        self.btnVerify.Bind(wx.EVT_BUTTON, self.on_btn_verify)
    
    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def on_btn_apply(self, event):
        event.Skip()
        self.Close()
    
    def on_btn_verify(self, event):
        event.Skip()
        self.Close()