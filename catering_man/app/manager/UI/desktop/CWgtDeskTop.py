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
from app.logic.desktop.CDataDeskTop import CDataDeskTop
from app.UI.system.CPopCompany import CPopCompany
from app.UI.system.CPopRegister import CPopRegister

###########################################################################
## Class CWgtDeskTop
###########################################################################

li_funcwidget_1 = ['DiningTable', 'DishesPublish', 'Employee', 'PrinterScheme', '', 'Company']
li_funcwidget_2 = ['', '', 'DutyTable', 'SchemeRelated', '', 'Register']

li_title = [u"餐厅设置", u"菜品发布", u"员工管理", u"打印设置", u"报表中心", u"系统设置"]

class CWgtDeskTop (wx.Panel):
	def _init_status_bar_sizer(self, parent):
		sizer = wx.BoxSizer( wx.VERTICAL )

		# Add status bar panel
		sizer.SetMinSize(wx.Size(800, 50)) 
		self.logoPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		self.logoPanel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
		self.logoPanel.SetMinSize(wx.Size(50, 50))
		sizer.Add(self.logoPanel, 1, wx.EXPAND|wx.BOTTOM, 5)
		parent.Add(sizer, 1, 0, 5)
		
	def _init_screen_sizer(self, parent):
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		sizer.SetMinSize(wx.Size(800, 750))
		
		self._init_selector_sizer(sizer)
		self._init_funcwidget_sizer(sizer)
		
		parent.Add(sizer, 1, 0, 5 )
		
	def _init_selector_sizer(self, parent):
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.SetMinSize(wx.Size(200,750)) 
		
		# Selector panel initialize
		self.selectorPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		self.selectorPanel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))
		
		selectorSizer = wx.BoxSizer(wx.VERTICAL)
		
		# Add enough space on top 
		selectorTopSizer = wx.BoxSizer(wx.VERTICAL)
		selectorTopSizer.SetMinSize(wx.Size(200, 50)) 
		selectorTopSizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
		selectorSizer.Add(selectorTopSizer, 1, 0, 5)
		
		# Set the selector buttons
		selectorBottomSizer = wx.BoxSizer(wx.VERTICAL)
		selectorBottomSizer.SetMinSize(wx.Size(200, 550)) 
		# Add dining room setting button
		self.btnDiningRoomSetting = wx.Button(self.selectorPanel, wx.ID_ANY, u"餐厅设置", wx.Point(50, 50), wx.DefaultSize, 0)
		selectorBottomSizer.Add(self.btnDiningRoomSetting, 0, wx.ALIGN_CENTER, 5)
		# Add dishes publish button
		self.btnDishesPublishing = wx.Button(self.selectorPanel, wx.ID_ANY, u"菜品发布", wx.DefaultPosition, wx.DefaultSize, 0)
		selectorBottomSizer.Add(self.btnDishesPublishing, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add employee manager button
		self.btnStaffMan = wx.Button(self.selectorPanel, wx.ID_ANY, u"员工管理", wx.DefaultPosition, wx.DefaultSize, 0)
		selectorBottomSizer.Add(self.btnStaffMan, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add printer setting button
		self.btnPrinter = wx.Button(self.selectorPanel, wx.ID_ANY, u"打印设置", wx.DefaultPosition, wx.DefaultSize, 0)
		selectorBottomSizer.Add(self.btnPrinter, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add report forms button
		self.btnReportForms = wx.Button(self.selectorPanel, wx.ID_ANY, u"报表中心", wx.DefaultPosition, wx.DefaultSize, 0)
		selectorBottomSizer.Add(self.btnReportForms, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add system setting button
		self.btnSysSetting = wx.Button(self.selectorPanel, wx.ID_ANY, u"系统设置", wx.DefaultPosition, wx.DefaultSize, 0)
		selectorBottomSizer.Add(self.btnSysSetting, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add exit button
		self.btnExit = wx.Button(self.selectorPanel, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
		selectorBottomSizer.Add(self.btnExit, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		
		# Layout selector buttons
		selectorSizer.Add(selectorBottomSizer, 1, 0, 5)
		self.selectorPanel.SetSizer(selectorSizer)
		self.selectorPanel.Layout()
		selectorSizer.Fit(self.selectorPanel)
		sizer.Add(self.selectorPanel, 1, wx.EXPAND|wx.RIGHT, 5)
		parent.Add(sizer, 1, 0, 5)
		
	def _init_funcwidget_sizer(self, parent):
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.SetMinSize(wx.Size(600, 750)) 
		
		# Function widget panel initialize
		self.funcPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		self.funcPanel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))
		self.funcPanel.SetMinSize(wx.Size(800, 600))
		
		funcSizer = wx.BoxSizer(wx.HORIZONTAL)
		
		# Define function buttons dictionary
		self.di_funcButtons = dict()
		# Add function 1
		self.btnFunc_1 = wx.Button(self.funcPanel, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0)  
		funcBtnItem_1 = {0:self.btnFunc_1}
		self.di_funcButtons.update(funcBtnItem_1)
		# Add function 2
		self.btnFunc_2 = wx.Button(self.funcPanel, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0)
		funcBtnItem_2 = {1:self.btnFunc_2}
		self.di_funcButtons.update(funcBtnItem_2 )
		# Add function 3
		self.btnFunc_3 = wx.Button(self.funcPanel, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0)
		funcBtnItem_3 = {2:self.btnFunc_3}
		self.di_funcButtons.update(funcBtnItem_3)
		# Add function 4
		self.btnFunc_4 = wx.Button(self.funcPanel, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0)
		funcBtnItem_4 = {3:self.btnFunc_4}
		self.di_funcButtons.update(funcBtnItem_4)
		# Add function 5
		self.btnFunc_5 = wx.Button(self.funcPanel, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0)
		funcBtnItem_5 = {4:self.btnFunc_5}
		self.di_funcButtons.update(funcBtnItem_5 )
		# Add function 6
		self.btnFunc_6 = wx.Button(self.funcPanel, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0) 
		funcBtnItem_6 = {5:self.btnFunc_6}
		self.di_funcButtons.update(funcBtnItem_6 ) 
		
		# Layout function widget items
		self.funcPanel.SetSizer(funcSizer)
		self.funcPanel.Layout()
		funcSizer.Fit(self.funcPanel)
		sizer.Add(self.funcPanel, 1, wx.EXPAND, 5)
		parent.Add(sizer, 1, wx.EXPAND, 5)

	def __init__(self, parent):
		wx.Panel.__init__ (self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(800, 600), style=wx.TAB_TRAVERSAL)

		self.SetSizeHintsSz(wx.Size(800, 600), wx.DefaultSize)
		self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWFRAME))

		sizer = wx.BoxSizer(wx.VERTICAL)
		self._init_status_bar_sizer(sizer)
		self._init_screen_sizer(sizer)

		self.SetSizer(sizer)
		self.Layout()
		self.Centre(wx.BOTH)

		# Connect Events
		self.Bind(wx.EVT_SIZE, self.OnSize)
		self.btnDiningRoomSetting.Bind(wx.EVT_LEFT_DOWN, self.OnDiningRoonSetting)
		self.btnDishesPublishing.Bind(wx.EVT_LEFT_DOWN, self.OnDishesPublishing)
		self.btnStaffMan.Bind(wx.EVT_LEFT_DOWN, self.OnEmployeeManager)
		self.btnPrinter.Bind(wx.EVT_LEFT_DOWN, self.OnPrinterSetting)
		self.btnReportForms.Bind(wx.EVT_LEFT_DOWN, self.OnReportForms)
		self.btnSysSetting.Bind(wx.EVT_LEFT_DOWN, self.OnSystemSetting)
		self.btnExit.Bind(wx.EVT_LEFT_DOWN, parent.OnExit)
		self.btnFunc_1.Bind(wx.EVT_LEFT_DOWN, self.OnFunc_1)
		self.btnFunc_2.Bind(wx.EVT_LEFT_DOWN, self.OnFunc_2)
		self.btnFunc_3.Bind(wx.EVT_LEFT_DOWN, self.OnFunc_3)
		self.btnFunc_4.Bind(wx.EVT_LEFT_DOWN, self.OnFunc_4)
		self.btnFunc_5.Bind(wx.EVT_LEFT_DOWN, self.OnFunc_5)
		self.btnFunc_6.Bind(wx.EVT_LEFT_DOWN, self.OnFunc_6)

	def __del__( self ):
		pass

	# Override function, initialize user interface
	def Initailize(self):
		x, y = CDataDeskTop.GetFrameSize()
		self.SetSize(wx.Size(x, y))

		select_item = CDataDeskTop.GetSelectedItem()
		if select_item == 0:
			self.ShowDiningRoonSetting()
		elif select_item == 1:
			self.ShowDishesPublishing()
		elif select_item == 2:
			self.ShowStaffManager()
		elif select_item == 3:
			self.ShowPrinter()
		elif select_item == 4:
			self.ShowReportForms()
		elif select_item == 5:
			self.ShowSystemSetting()

	# Override function un initialize user interface
	def Uninitailize(self):
		pass

	# Virtual event handlers, override them in your derived class
	def OnSize(self, event):
		event.Skip()
		x, y = self.GetSize()

		self.logoPanel.SetMinSize(wx.Size(x,50))
		self.selectorPanel.SetMaxSize(wx.Size(200,y-50)) 
		self.funcPanel.SetMinSize(wx.Size(x-200,y-50))

		self.ShowFuncBtns()

	def OnDiningRoonSetting(self, event):
		event.Skip()
		CDataDeskTop.SetSelectedItem(0)
		self.ShowDiningRoonSetting()

	def OnDishesPublishing(self, event):
		event.Skip()
		CDataDeskTop.SetSelectedItem(1)
		self.ShowDishesPublishing()

	def OnEmployeeManager(self, event):
		event.Skip()
		CDataDeskTop.SetSelectedItem(2)
		self.ShowStaffManager()

	def OnPrinterSetting(self, event):
		event.Skip()
		CDataDeskTop.SetSelectedItem(3)
		self.ShowPrinter()

	def OnReportForms(self, event):
		event.Skip()
		CDataDeskTop.SetSelectedItem(4)
		self.ShowReportForms()

	def OnSystemSetting(self, event):
		event.Skip()
		CDataDeskTop.SetSelectedItem(5)
		self.ShowSystemSetting()

	def OnFunc_1(self, event):
		event.Skip()
		select_item = CDataDeskTop.GetSelectedItem()
		if select_item != 5:
			CAppManager.SwitchToApplication(li_funcwidget_1[select_item])
		else:
			self.popCompany = CPopCompany(self)
			self.popCompany.ShowModal()
			self.Refresh()

	def OnFunc_2(self, event):
		event.Skip()
		select_item = CDataDeskTop.GetSelectedItem()
		if select_item != 5:
			CAppManager.SwitchToApplication(li_funcwidget_2[select_item])
		else:
			self.popRigster = CPopRegister(self)
			self.popRigster.ShowModal()
			self.Refresh()

	def OnFunc_3(self, event):
		event.Skip()

	def OnFunc_4(self, event):
		event.Skip()

	def OnFunc_5(self, event):
		event.Skip()

	def OnFunc_6(self, event):
		event.Skip()

	def ShowDiningRoonSetting(self):
		self.EnableAllSelector()
		self.HideAllFuncBtn()
		self.btnDiningRoomSetting.Enabled = False;
		#self.btnFunc_1.Show()
		#self.btnFunc_1.Label = u"餐桌设置"
		CAppManager.SwitchToApplication(li_funcwidget_1[0])
		self.SetFramTile()

	def ShowDishesPublishing(self):
		self.EnableAllSelector()
		self.HideAllFuncBtn()
		self.btnDishesPublishing.Enabled = False;
		#self.btnFunc_1.Show()
		#self.btnFunc_1.Label = u"菜品发布"
		CAppManager.SwitchToApplication(li_funcwidget_1[1])
		self.SetFramTile()
		self.ShowFuncBtns()

	def ShowStaffManager(self):
		self.EnableAllSelector()
		self.HideAllFuncBtn()
		self.btnStaffMan.Enabled = False;
		self.btnFunc_1.Show()
		self.btnFunc_1.Label = u"员工管理"
		self.btnFunc_2.Show()
		self.btnFunc_2.Label = u"权限管理"
		self.btnFunc_3.Show()
		self.btnFunc_3.Label = u"员工排班"
		self.SetFramTile()
		self.ShowFuncBtns()

	def ShowPrinter(self):
		self.EnableAllSelector()
		self.HideAllFuncBtn()
		self.btnPrinter.Enabled = False;
		self.btnFunc_1.Show()
		self.btnFunc_1.Label = u"厨打方案"
		self.btnFunc_2.Show()
		self.btnFunc_2.Label = u"菜品关联"
		self.SetFramTile()
		self.ShowFuncBtns()

	def ShowReportForms(self):
		self.EnableAllSelector()
		self.HideAllFuncBtn()
		self.btnReportForms.Enabled = False;
		self.btnFunc_1.Show()
		self.btnFunc_1.Label = u"菜品销售查询"
		self.btnFunc_2.Show()
		self.btnFunc_2.Label = u"收银情况查询"
		self.btnFunc_3.Show()
		self.btnFunc_3.Label = u"营业情况查询"
		self.btnFunc_4.Show()
		self.btnFunc_4.Label = u"消费查询"
		self.btnFunc_5.Show()
		self.btnFunc_5.Label = u"菜品排行榜"
		self.SetFramTile()
		self.ShowFuncBtns()

	def ShowSystemSetting(self):
		self.EnableAllSelector()
		self.HideAllFuncBtn()
		self.btnSysSetting.Enabled = False;
		self.btnFunc_1.Show()
		self.btnFunc_1.Label = u"公司信息"
		self.btnFunc_2.Show()
		self.btnFunc_2.Label = u"注册"
		self.btnFunc_3.Show()
		self.btnFunc_3.Label = u"数据备份"
		self.SetFramTile()
		self.ShowFuncBtns()

	def EnableAllSelector(self):
		self.btnDiningRoomSetting.Enabled = True
		self.btnDishesPublishing.Enabled = True
		self.btnStaffMan.Enabled = True
		self.btnPrinter.Enabled = True
		self.btnReportForms.Enabled = True
		self.btnSysSetting.Enabled = True

	def HideAllFuncBtn(self):
		self.btnFunc_1.Hide()
		self.btnFunc_2.Hide()
		self.btnFunc_3.Hide()
		self.btnFunc_4.Hide()
		self.btnFunc_5.Hide()
		self.btnFunc_6.Hide()    

	def ShowFuncBtns(self):
		select_item = CDataDeskTop.GetSelectedItem()  
		self.func_num = 1
		if select_item == 0:
			self.func_num = 1
		elif select_item == 1:
			self.func_num = 1
		elif select_item == 2:
			self.func_num = 3
		elif select_item == 3:
			self.func_num = 2
		elif select_item == 4:
			self.func_num = 5
		elif select_item == 5:
			self.func_num = 3 
			
		x, y = self.GetSize()
		btn_y = ((y - 50) - 100) / 2
		btn_x = ((x - 200) - ((self.func_num * 100) + ((self.func_num - 1) * 10))) / 2
		for i in range(self.func_num):
			self.di_funcButtons[i].Move(wx.Point(btn_x + (i*110), btn_y))
			self.di_funcButtons[i].SetSize(wx.Size(100,100))

	def SetFramTile(self): 
		select_item = CDataDeskTop.GetSelectedItem()  
		self.GetParent().SetTitle(li_title[select_item])

if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = CWgtDeskTop(None)
	frame.Show(True)
	frame.Center()
	app.MainLoop()
