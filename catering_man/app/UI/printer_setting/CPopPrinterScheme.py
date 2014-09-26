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
from app.logic.printer_setting.CDataPrinterScheme import CDataPrinterSchemeInfo, CDataPrinterScheme
from app.logic.printer_setting.CDataSchemeType import CDataSchemeTypeInfo

###########################################################################
## Class CPopPrinterScheme
###########################################################################

class CPopPrinterScheme(wx.Dialog):
	def _init_view_sizer(self, parent):
		panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		# Create a tow rows and 1 column grid sizer for scheme and printer
		gSizer = wx.GridSizer(2, 1, 0, 0)
		gSizer.SetMinSize(wx.Size(600,300))
		
		# Create scheme panel
		topPanel = wx.Panel(panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL)
		topGSizer = wx.GridSizer(1, 2, 0, 0)
		# Add column 1 of scheme
		self._init_scheme_colume_1_sizer(topPanel, topGSizer)
		# Add column 2 of scheme
		self._init_scheme_colume_2_sizer(topPanel, topGSizer)
		# Layout scheme panel
		topPanel.SetSizer(topGSizer)
		topPanel.Layout()
		topGSizer.Fit(topPanel)
		gSizer.Add(topPanel, 1, wx.EXPAND, 5)
		
		# Create printer panel
		bottomPanel = wx.Panel(panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL)
		bottomGSizer = wx.GridSizer(3, 1, 0, 0)
		# Add printer driver sizer
		self._init_priner_row_1_sizer(bottomPanel, bottomGSizer)
		# Layout printer panel
		bottomPanel.SetSizer(bottomGSizer)
		bottomPanel.Layout()
		bottomGSizer.Fit(bottomPanel)
		gSizer.Add(bottomPanel, 1, wx.EXPAND, 5)
		
		# Layout view sizer
		panel.SetSizer(gSizer)
		panel.Layout()
		gSizer.Fit(panel)
		parent.Add(panel, 1, wx.EXPAND |wx.ALL, 5)
		
	def _init_scheme_colume_1_sizer(self, container, parent):
		gSizer = wx.GridSizer(3, 1, 0, 0)
		# Add scheme number sizer
		codeSizer = wx.BoxSizer(wx.HORIZONTAL)
		sTxtCode = wx.StaticText(container, wx.ID_ANY, u"方案编号：", wx.DefaultPosition, wx.Size(80,-1), 0)
		sTxtCode.Wrap(-1)
		codeSizer.Add(sTxtCode, 0, wx.ALIGN_CENTER|wx.ALL, 5)

		self.txtCode = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		codeSizer.Add(self.txtCode, 0, wx.ALIGN_CENTER|wx.ALL, 5)

		self.ckxValid = wx.CheckBox(container, wx.ID_ANY, u"生效：", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT)
		codeSizer.Add(self.ckxValid, 0, wx.ALIGN_CENTER|wx.ALL, 5)

		gSizer.Add(codeSizer, 1, wx.EXPAND, 5)
		# Add invoice type sizer
		typeSizer = wx.BoxSizer(wx.HORIZONTAL)
		sTxtInvoice = wx.StaticText(container, wx.ID_ANY, u"厨打单类：", wx.DefaultPosition, wx.Size(80,-1), 0)
		sTxtInvoice.Wrap(-1)
		typeSizer.Add(sTxtInvoice, 0, wx.ALIGN_CENTER|wx.ALL, 5)

		cbxTypeChoices = list()
		self.cbxType = wx.ComboBox(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(110,-1), cbxTypeChoices, 0)
		typeSizer.Add(self.cbxType, 0, wx.ALIGN_CENTER|wx.ALL, 5)

		gSizer.Add(typeSizer, 1, wx.EXPAND, 5)
		# Add reserve scheme sizer
		backupSizer = wx.BoxSizer(wx.HORIZONTAL)
		sTxtReserve = wx.StaticText(container, wx.ID_ANY, u"后备方案：", wx.DefaultPosition, wx.Size(80,-1), 0)
		sTxtReserve.Wrap(-1)
		backupSizer.Add(sTxtReserve, 0, wx.ALIGN_CENTER|wx.ALL, 5)

		self.txtBackup = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		backupSizer.Add(self.txtBackup, 0, wx.ALIGN_CENTER|wx.ALL, 5)

		gSizer.Add(backupSizer, 1, wx.EXPAND, 5)
		
		# Layout column 1 of scheme
		parent.Add(gSizer, 1, wx.EXPAND, 5)

	def _init_scheme_colume_2_sizer(self, container, parent):
		gSizer = wx.GridSizer(3, 1, 0, 0)
		# Add scheme name sizer
		nameSizer = wx.BoxSizer(wx.HORIZONTAL)
		sTxtName = wx.StaticText(container, wx.ID_ANY, u"方案名称：", wx.DefaultPosition, wx.Size(80,-1), 0)
		sTxtName.Wrap(-1)
		nameSizer.Add(sTxtName, 0, wx.ALIGN_CENTER|wx.ALL, 5)

		self.txtName = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		nameSizer.Add(self.txtName, 0, wx.ALIGN_CENTER|wx.ALL, 5)

		gSizer.Add(nameSizer, 1, wx.EXPAND, 5)
		# Add print number sizer
		printNumSizer = wx.BoxSizer(wx.HORIZONTAL)
		sTxtNum = wx.StaticText(container, wx.ID_ANY, u"厨打份数：", wx.DefaultPosition, wx.Size(80,-1), 0)
		sTxtNum.Wrap(-1)
		printNumSizer.Add(sTxtNum, 0, wx.ALIGN_CENTER|wx.ALL, 5)

		cbxPrintNumChoices = list()
		self.cbxPrintNum = wx.ComboBox(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(110,-1), cbxPrintNumChoices, 0)
		printNumSizer.Add(self.cbxPrintNum, 0, wx.ALIGN_CENTER|wx.ALL, 5)

		gSizer.Add(printNumSizer, 1, wx.EXPAND, 5)
		
		# Layout column 2 of scheme
		parent.Add(gSizer, 1, wx.EXPAND, 5)
		
	def _init_priner_row_1_sizer(self, container, parent):
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Add printer driver label
		sTxtDriver = wx.StaticText(container, wx.ID_ANY, u"打印机：", wx.DefaultPosition, wx.Size(80,-1), 0)
		sTxtDriver.Wrap(-1)
		sizer.Add(sTxtDriver, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		# Add printer driver combo box 
		cbxPrintDriverChoices = list()
		self.cbxPrintDriver = wx.ComboBox(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400,-1), cbxPrintDriverChoices, 0)
		sizer.Add(self.cbxPrintDriver, 0, wx.ALL, 5)
		# Layout printer driver 
		parent.Add(sizer, 1, wx.EXPAND, 5)
		
	def _init_ctrl_sizer(self, parent):
		sizer = wx.BoxSizer( wx.HORIZONTAL )

		# Add track number
		self.txtTrack = wx.StaticText(self, wx.ID_ANY, u"1 / 1", wx.DefaultPosition, wx.DefaultSize, 0)
		self.txtTrack.Wrap(-1)
		sizer.Add(self.txtTrack, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add previous record button
		self.btnPrev = wx.Button(self, wx.ID_ANY, u"上一记录", wx.DefaultPosition, wx.DefaultSize, 0)
		sizer.Add(self.btnPrev, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add next record button
		self.btnNext = wx.Button(self, wx.ID_ANY, u"下一记录", wx.DefaultPosition, wx.DefaultSize, 0)
		sizer.Add(self.btnNext, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add spacer
		sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
		# Add save button
		self.btnSave = wx.Button(self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0)
		sizer.Add(self.btnSave, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add exit button
		self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
		sizer.Add(self.btnExit, 0, wx.ALIGN_CENTER|wx.ALL, 5)

		# Layout control sizer
		parent.Add(sizer, 1, wx.EXPAND, 5)
		
	def __init__(self, parent, type_="add"):
		wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"厨打基本方案设置", pos=wx.DefaultPosition, size=wx.Size(600,400), style=wx.CAPTION)
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		sizer = wx.BoxSizer(wx.VERTICAL)
		self._init_view_sizer(sizer)
		self._init_ctrl_sizer(sizer)

		self.SetSizer(sizer)
		self.Layout()
		self.Centre(wx.BOTH)

		# Connect Events
		self.btnPrev.Bind(wx.EVT_BUTTON, self.OnBtnPrev)
		self.btnNext.Bind(wx.EVT_BUTTON, self.OnBtnNext)
		self.btnSave.Bind(wx.EVT_BUTTON, self.OnBtnSave)
		self.btnExit.Bind(wx.EVT_BUTTON, self.OnBtnExit)

		# Initialize 
		self.index = 0
		self.type = type_
		self.InitializeView()

	def __del__( self ):
		pass

	def InitializeView(self):
		for index in range(4):
			self.cbxPrintNum.Append("%d" % (index + 1))

		if self.type == "add":
			self.InitAddView()
		elif self.type == "mod":
			self.index = CDataPrinterSchemeInfo.GetCurItemIndex()
			self.InitModView()

	def InitAddView(self):
		li_scheme_type = CDataSchemeTypeInfo.GetData()
		for scheme_type in li_scheme_type:
			self.cbxType.Append(scheme_type.name, scheme_type)
		self.cbxType.SetSelection(0)

		self.cbxPrintNum.SetSelection(0)

		self.txtTrack.Enable(False)
		self.btnPrev.Enable(False)
		self.btnNext.Enable(False)

	def InitModView(self):
		self.txtCode.Enable(False)
		if self.index < 0:
			self.index = 0
			return

		items = CDataPrinterSchemeInfo.GetItems()
		if self.index >= len(items):
			self.index = len(items) - 1
			return

		data = items[self.index]
		self.txtCode.SetValue(str(data.code))
		self.txtName.SetValue(data.name)
		self.ckxValid.SetValue(data.valid)
		self.txtBackup.SetValue(data.backup)
		self.staticTxtNum.SetLabel(("%d / %d" % (self.index+1, len(items))))

		li_scheme_type = CDataSchemeTypeInfo.GetData()
		scheme_type_selection = 0
		for scheme_type in li_scheme_type:
			self.cbxType.Append(scheme_type.name, scheme_type)
			if scheme_type.code == data.scheme_type:
				self.cbxType.SetSelection(scheme_type_selection)
			scheme_type_selection += 1

		self.cbxPrintNum.SetSelection(data.print_count - 1)

	# Virtual event handlers, override them in your derived class
	def OnBtnPrev(self, event):
		event.Skip()
		self.index -= 1
		self.InitModInfo()

	def OnBtnNext(self, event):
		event.Skip()
		self.index += 1
		self.InitModView()

	def OnBtnSave(self, event):
		event.Skip()
		scheme_type = self.cbxType.GetClientData(self.cbxType.GetSelection())
		print_count = int(self.cbxPrintNum.GetValue())
		data = CDataPrinterScheme(0, 
							int(self.txtCode.GetValue()), 
							self.txtName.GetValue(), 
							self.ckxValid.GetValue(), 
							scheme_type.code, 
							print_count, 
							self.txtBackup.GetValue())
		if self.type == "add":
			CDataPrinterSchemeInfo.AddItem(data)
		elif self.type == "mod":
			CDataPrinterSchemeInfo.UpdateItem(data)

	def OnBtnExit(self, event):
		event.Skip()
		self.Close()

if __name__ == '__main__':
	app = wx.PySimpleApp()
	dlg = CPopPrinterScheme(None)
	dlg.Show()
	app.MainLoop()
