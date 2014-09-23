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
from app.logic.dining_room.CDataTable import CDataTable, CDataTableInfo
from app.logic.dining_room.CDataArea import CDataAreaInfo
from app.logic.dining_room.CDataType import CDataTypeInfo
from app.logic.dining_room.CDataMinexpense import CDataMinexpenseInfo

###########################################################################
## Class CPopTableBatAdd
###########################################################################

class CPopTableBatAdd (wx.Dialog):
	def _init_view_sizer(self, parent):
		sizer = wx.BoxSizer(wx.VERTICAL)
		
		# Create grid sizer for 1 row and 2 column
		gSizer = wx.GridSizer(1, 2, 0, 0)
		
		# Column 1 is another grid sizer for 4 rows and 2 column
		gSizerLeft = wx.GridSizer(4, 2, 0, 0)
		# Add label for code prefix
		sTxtCodePre = wx.StaticText(self, wx.ID_ANY, u"编号前缀：", wx.DefaultPosition, wx.DefaultSize, 0)
		sTxtCodePre.Wrap(-1)
		gSizerLeft.Add(sTxtCodePre, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add text for code prefix
		self.txtCodePre = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		gSizerLeft.Add(self.txtCodePre, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add label for from
		sTxtFrom = wx.StaticText(self, wx.ID_ANY, u"从：", wx.DefaultPosition, wx.DefaultSize, 0)
		sTxtFrom.Wrap(-1)
		gSizerLeft.Add(sTxtFrom, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add text for from
		self.txtFrom = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		gSizerLeft.Add(self.txtFrom, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add label for area
		sTxtArea = wx.StaticText(self, wx.ID_ANY, u"区域：", wx.DefaultPosition, wx.DefaultSize, 0)
		sTxtArea.Wrap(-1)
		gSizerLeft.Add(sTxtArea, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add combo box for area
		cbxAreaChoices = list()
		self.cbxArea = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, cbxAreaChoices, 0)
		gSizerLeft.Add(self.cbxArea, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add label for consumer type 
		sTxtContype = wx.StaticText(self, wx.ID_ANY, u"消费类型：", wx.DefaultPosition, wx.DefaultSize, 0)
		sTxtContype.Wrap(-1)
		gSizerLeft.Add(sTxtContype, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add combo box for consumer type 
		cbxMinExpenseChoices = list()
		self.cbxMinExpense = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, cbxMinExpenseChoices, 0)
		gSizerLeft.Add(self.cbxMinExpense, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Layout column 1
		gSizer.Add(gSizerLeft, 1, wx.EXPAND, 5)
		
		# Column 2 is another grid sizer for 4 rows and 2 columns
		gSizerRight = wx.GridSizer(4, 2, 0, 0)
		# Add spacer
		gSizerRight.AddSpacer((0, 0), 1, wx.EXPAND, 5)
		gSizerRight.AddSpacer((0, 0), 1, wx.EXPAND, 5)
		# Add label for to
		sTxtTo = wx.StaticText(self, wx.ID_ANY, u"到：", wx.DefaultPosition, wx.DefaultSize, 0)
		sTxtTo.Wrap(-1)
		gSizerRight.Add(sTxtTo, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add text control for to
		self.txtTo = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		gSizerRight.Add(self.txtTo, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add label for dining table type
		sTxtTableType = wx.StaticText(self, wx.ID_ANY, u"餐桌类型：", wx.DefaultPosition, wx.DefaultSize, 0)
		sTxtTableType.Wrap(-1)
		gSizerRight.Add(sTxtTableType, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add combo box for dining table type
		cbxTypeChoices = list()
		self.cbxType = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, cbxTypeChoices, 0)
		gSizerRight.Add(self.cbxType, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add label for people number
		sTxtPepleNum = wx.StaticText(self, wx.ID_ANY, u"人数：", wx.DefaultPosition, wx.DefaultSize, 0)
		sTxtPepleNum.Wrap( -1 )
		gSizerRight.Add(sTxtPepleNum, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add text control for people number
		self.txtPepleNum = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		gSizerRight.Add(self.txtPepleNum, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Layout column 2
		gSizer.Add(gSizerRight, 1, wx.EXPAND, 5)
		
		# Layout data view
		sizer.Add(gSizer, 1, wx.EXPAND, 5)
		parent.Add(sizer, 1, wx.EXPAND, 5)
		
	def _init_ctrl_sizer(self, parent):
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Add spacer
		sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
		# Add create button
		self.btnCreate = wx.Button(self, wx.ID_ANY, u"生成", wx.DefaultPosition, wx.DefaultSize, 0)
		sizer.Add(self.btnCreate, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add exit button
		self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
		sizer.Add(self.btnExit, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Layout control 
		parent.Add(sizer, 1, wx.EXPAND, 5)
		
	def __init__(self, parent):
		wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"批量生成餐桌", pos=wx.DefaultPosition, size=wx.Size(480, 220), style=wx.CAPTION)
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		sizer = wx.BoxSizer( wx.VERTICAL )
		
		self._init_view_sizer(sizer)
		self._init_ctrl_sizer(sizer)

		self.SetSizer(sizer)
		self.Layout()
		self.Centre(wx.BOTH)

		# Connect Events
		self.btnCreate.Bind(wx.EVT_BUTTON, self.OnBtnCreate)
		self.btnExit.Bind(wx.EVT_BUTTON, self.OnBtnExit)

		# Initialize data on view list
		self.InitailizeView()

	def __del__( self ):
		pass

	def InitailizeView(self):
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

	# Virtual event handlers, override them in your derived class
	def OnBtnCreate( self, event ):
		event.Skip()
		area = self.cbxArea.GetClientData(self.cbxArea.GetSelection())
		table_type = self.cbxType.GetClientData(self.cbxType.GetSelection())
		min_expense = self.cbxMinExpense.GetClientData(self.cbxMinExpense.GetSelection())
		i_from = int(self.txtFrom.GetValue())
		i_to = int(self.txtTo.GetValue())
		i_peple_num = int(self.txtPepleNum.GetValue())
		table_items = list()
		for index in range(i_from, i_to + 1):
			table_items.append(CDataTable(0, 0, ("餐桌%d" % index), table_type.code, area.code, i_peple_num, min_expense.code))

		CDataTableInfo.AddItems(table_items)

	def OnBtnExit( self, event ):
		event.Skip()
		self.Close()

if __name__ == '__main__':
	app = wx.PySimpleApp()
	dlg = CPopTableBatAdd(None)
	dlg.Show()
	app.MainLoop()

