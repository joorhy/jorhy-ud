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
from app.logic.dining_room.CDataArea import CDataAreaInfo
from app.logic.dining_room.CDataType import CDataTypeInfo
from app.logic.dining_room.CDataTable import CDataTable, CDataTableInfo
from app.logic.dining_room.CDataMinexpense import CDataMinexpenseInfo

###########################################################################
## Class CPopTableInfo
###########################################################################

class CPopTableInfo (wx.Dialog):
	def _init_view_sizer(self, parent):
		panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(600, 200), wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL)
		# Create a grid sizer with 1 row and 2 columns
		gSizer = wx.GridSizer(1, 2, 0, 0)
		gSizer.SetMinSize(wx.Size(600, 200)) 

		# Column 1 also is a grid sizer with 3 rows and 2 columns
		gSizerLeft = wx.GridSizer(3, 2, 0, 0)
		# Add label for dining table code 
		sTxtTableCode = wx.StaticText(panel, wx.ID_ANY, u"餐桌编码：", wx.Point( -1,-1 ), wx.DefaultSize, 0)
		sTxtTableCode.Wrap(-1)
		gSizerLeft.Add(sTxtTableCode, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add text control for dining table code 
		self.txtCode = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(120, -1), 0)
		gSizerLeft.Add(self.txtCode, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add label for dining table type
		sTxtTableType = wx.StaticText(panel, wx.ID_ANY, u"所属类型：", wx.DefaultPosition, wx.DefaultSize, 0)
		sTxtTableType.Wrap(-1)
		gSizerLeft.Add(sTxtTableType, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add combo box for dining table type
		cbxTypeChoices = list()
		self.cbxType = wx.ComboBox(panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(120, -1), cbxTypeChoices, 0)
		gSizerLeft.Add(self.cbxType, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add label for people number
		sTxtPepleNum = wx.StaticText(panel, wx.ID_ANY, u"人数：", wx.DefaultPosition, wx.DefaultSize, 0)
		sTxtPepleNum.Wrap( -1 )
		gSizerLeft.Add(sTxtPepleNum, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add text control for people number
		self.txtPeple = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(120, -1), 0)
		gSizerLeft.Add(self.txtPeple, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Layout column 1
		gSizer.Add(gSizerLeft, 1, wx.EXPAND, 5)
		
		# Column 2 also is a grid sizer with 3 rows and 2 columns
		gSizerRight = wx.GridSizer(3, 2, 0, 0)
		# Add label for dining table name 
		sTxtTalbeName = wx.StaticText(panel, wx.ID_ANY, u"餐桌名称：", wx.DefaultPosition, wx.DefaultSize, 0)
		sTxtTalbeName.Wrap(-1)
		gSizerRight.Add(sTxtTalbeName, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add text control for dining table name 
		self.txtName = wx.TextCtrl(panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(120,-1), 0)
		gSizerRight.Add(self.txtName, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add label for dining table area 
		sTxtTableArea = wx.StaticText(panel, wx.ID_ANY, u"所属区域：", wx.DefaultPosition, wx.DefaultSize, 0)
		sTxtTableArea.Wrap(-1)
		gSizerRight.Add(sTxtTableArea, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add combo box for dining table area 
		cbxAreaChoices = list()
		self.cbxArea = wx.ComboBox(panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(120,-1), cbxAreaChoices, 0)
		gSizerRight.Add(self.cbxArea, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add label for consumer type 
		sTxtContype = wx.StaticText(panel, wx.ID_ANY, u"消费类型：", wx.DefaultPosition, wx.DefaultSize, 0)
		sTxtContype.Wrap(-1)
		gSizerRight.Add(sTxtContype, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add combo box for consumer type 
		cbxMinExpenseChoices = list()
		self.cbxMinExpense = wx.ComboBox(panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(120,-1), cbxMinExpenseChoices, 0)
		gSizerRight.Add(self.cbxMinExpense, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Layout column 2
		gSizer.Add(gSizerRight, 1, wx.EXPAND, 5)
		
		# Layout data view
		panel.SetSizer(gSizer)
		panel.Layout()
		parent.Add(panel, 1, wx.EXPAND |wx.ALL, 5)
		
	def _init_ctrl_sizer(self, parent):
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		
		# Add static text for track
		self.txtTrack = wx.StaticText(self, wx.ID_ANY, u"1 / 1 ", wx.DefaultPosition, wx.Size(80,-1), wx.ALIGN_CENTRE)
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

		# Layout control buttons
		parent.Add(sizer, 1, wx.EXPAND, 5)
		
	def __init__(self, parent, type_):
		wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"餐桌资料设置", pos=wx.DefaultPosition, size=wx.Size(600, 300), style=wx.CAPTION|wx.TAB_TRAVERSAL)
		self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

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

		# Initialize data view
		self.index = 0
		self.type = type_
		self.InitailizeView()

	def __del__( self ):
		pass

	def InitailizeView(self):
		if self.type == "add":
			self.InitAddView()
		elif self.type == "mod":
			self.index = CDataTableInfo.GetCurItemIndex()
			self.InitModView()

	def InitAddView(self):
		li_area = CDataAreaInfo.GetData()
		for area in li_area:
			self.cbxArea.Append(area.name, area)
		self.cbxArea.SetSelection(0)

		li_table_type = CDataTypeInfo.GetData()
		for table_type in li_table_type:
			self.cbxType.Append(table_type.name, table_type)
		self.cbxType.SetSelection(0)

		li_min_expense = CDataMinexpenseInfo.GetData()
		for min_expense in li_min_expense:
			self.cbxMinExpense.Append(min_expense.name, min_expense)
		self.cbxMinExpense.SetSelection(0)

		self.txtTrack.Enable(False)
		self.btnPrev.Enable(False)
		self.btnNext.Enable(False)

	def InitModView(self):
		self.txtCode.Enable(False) 
		if self.index < 0:
			self.index = 0
			return

		items = CDataTableInfo.GetItems()
		if self.index >= len(items):
			self.index = len(items) - 1
			return

		data = items[self.index]
		self.txtCode.SetValue(str(data.code))
		self.txtName.SetValue(data.name)
		self.txtPeple.SetValue(str(data.peple_num))
		self.txtTrack.SetLabel(("%d / %d" % (self.index+1, len(items))))

		li_area = CDataAreaInfo.GetData()
		area_selection = 0
		for area in li_area:
			self.cbxArea.Append(area.name, area)
			if area.code == data.area:
				self.cbxArea.SetSelection(area_selection)
			area_selection += 1

		li_table_type = CDataTypeInfo.GetData()
		table_type_selection = 0
		for table_type in li_table_type:
			self.cbxType.Append(table_type.name, table_type)
			if table_type.code == data.table_type:
				self.cbxType.SetSelection(table_type_selection)
			table_type_selection += 1

		li_min_expense = CDataMinexpenseInfo.GetData()
		min_expense_selection = 0
		for min_expense in li_min_expense:
			self.cbxMinExpense.Append(min_expense.name, min_expense)
			if min_expense.code == data.min_type:
				self.cbxMinExpense.SetSelection(min_expense_selection)
			min_expense_selection += 1

	# Virtual event handlers, override them in your derived class        
	def OnBtnPrev( self, event ):
		event.Skip()
		self.index -= 1
		self.InitModView()

	def OnBtnNext( self, event ):
		event.Skip()
		self.index += 1
		self.InitModView()

	def OnBtnSave( self, event ):
		event.Skip()
		area = self.cbxArea.GetClientData(self.cbxArea.GetSelection())
		type_ = self.cbxType.GetClientData(self.cbxType.GetSelection())
		min_expense = self.cbxMinExpense.GetClientData(self.cbxMinExpense.GetSelection())
		data = CDataTable(0, 
						int(self.txtCode.GetValue()), 
						self.txtName.GetValue(), 
						type_.code, 
						area.code, 
						int(self.txtPeple.GetValue()), 
						min_expense.code)
		if self.type == "add":
			CDataTableInfo.AddItem(data)
		elif self.type == "mod":
			CDataTableInfo.UpdateItem(data)

	def OnBtnExit( self, event ):
		event.Skip()
		self.Close()

if __name__ == '__main__':
	app = wx.PySimpleApp()
	dlg = CPopTableInfo(None, "add")
	dlg.Show()
	app.MainLoop()

