#!/usr/bin/env python
# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import os
import wx
import wx.xrc
import wx.dataview
from app.logic.dishes.CDataDishes import CDataDishesInfo, CDataDishes
from app.logic.dishes.CModelSpec import CModelSpec
from app.logic.dishes.CDataSpec import CDataSpec, CDataSpecInfo
from app.logic.dishes.CModelStyle import CModelStyle
from app.logic.dishes.CDataStyle import CDataStyle, CDataStyleInfo
from app.logic.dishes.CDataUnit import CDataUnitInfo
from app.logic.dishes.CDataCategory import CDataCategoryInfo
from framework.core import BrevityCode

###########################################################################
## Class CPopDishesInfo
###########################################################################

# This is how you pre-establish a file filter so that the dialog
# only shows the extension(s) you want it to.
wildcard = "bitmap image (*.bmp)|*.bmp|"    \
		   "png image (*.png)|*.png|"     	\
           "jpg image (*.jpg)|*.jpg|"     	\
		   "jpeg image (*.jpeg)|*.jpeg|"  	\
           "All files (*.*)|*.*"

class CPopDishesInfo (wx.Dialog):
	def _init_status_bar_sizer(self, parent):
		sizer = wx.BoxSizer(wx.HORIZONTAL)

		# Add static text for track
		self.txtTrack = wx.StaticText(self, wx.ID_ANY, u"1 / 1", wx.DefaultPosition, wx.DefaultSize, 0)
		self.txtTrack.Wrap(-1)
		sizer.Add(self.txtTrack, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add previous record button
		self.btnPrev = wx.Button(self, wx.ID_ANY, u"上一记录", wx.DefaultPosition, wx.DefaultSize, 0)
		sizer.Add(self.btnPrev, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add next record button
		self.btnNext = wx.Button(self, wx.ID_ANY, u"下一记录", wx.DefaultPosition, wx.DefaultSize, 0)
		sizer.Add(self.btnNext, 0, wx.ALL, 5)
		# Add spacer
		sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
		# Add save button
		self.btnSave = wx.Button(self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0)
		sizer.Add(self.btnSave, 0, wx.ALL, 5)
		# Add exit button
		self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
		sizer.Add(self.btnExit, 0, wx.ALIGN_CENTER|wx.ALL, 5)

		# Layout status bar
		parent.Add(sizer, 1, wx.EXPAND, 5)
		
	def _init_view_sizer(self, parent):
		fgSizer = wx.FlexGridSizer(0, 2, 0, 0)
		fgSizer.SetFlexibleDirection(wx.BOTH)
		fgSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
		
		self._init_data_view_sizer(fgSizer)
		self._init_image_view_sizer(fgSizer)
		
		# Layout data view
		parent.Add(fgSizer, 1, wx.EXPAND, 5)	
		
	def _init_data_view_sizer(self, parent):
		sizer = wx.BoxSizer(wx.VERTICAL)
		
		# Add data view panel
		panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(500,200), wx.STATIC_BORDER|wx.TAB_TRAVERSAL)
		panel.SetMaxSize(wx.Size(-1,200))
		
		# Add data view panel sizer
		panelSizer = wx.BoxSizer(wx.HORIZONTAL)
		panelSizer.SetMinSize(wx.Size(500,200)) 

		self._init_data_view_left_column_sizer(panel, panelSizer)
		self._init_data_view_right_column_sizer(panel, panelSizer)
		
		panel.SetSizer(panelSizer)
		panel.Layout()
		sizer.Add(panel, 1, wx.EXPAND |wx.ALL, 5)
		
		# Layout data view sizer
		parent.Add(sizer, 1, wx.EXPAND, 5)		
		
	def _init_data_view_left_column_sizer(self, container, parent):
		# Add grid sizer with 6 rows and 2 columns
		gSizer = wx.GridSizer(6, 2, 0, 0)
		# Add label for dishes code
		sTxtCode = wx.StaticText(container, wx.ID_ANY, u"品码：", wx.DefaultPosition, wx.DefaultSize, 0)
		sTxtCode.Wrap(-1)
		gSizer.Add(sTxtCode, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add text control for dishes code
		self.txtDishCode = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		gSizer.Add(self.txtDishCode, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add label for dishes unit
		sTxtUnit = wx.StaticText(container, wx.ID_ANY, u"单位：", wx.DefaultPosition, wx.DefaultSize, 0)
		sTxtUnit.Wrap(-1)
		gSizer.Add(sTxtUnit, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add combo box for dishes unit
		cbxUnitChoices = list()
		self.cbxUnit = wx.ComboBox(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(110,-1), cbxUnitChoices, 0)
		gSizer.Add(self.cbxUnit, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add label for dishes price
		sTxtPrice = wx.StaticText(container, wx.ID_ANY, u"售价：", wx.DefaultPosition, wx.DefaultSize, 0)
		sTxtPrice.Wrap(-1)
		gSizer.Add(sTxtPrice, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add text control for dishes price
		self.txtPrice = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		gSizer.Add(self.txtPrice, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add label for dishes specification
		sTxtSpec = wx.StaticText(container, wx.ID_ANY, u"规格：", wx.DefaultPosition, wx.DefaultSize, 0)
		sTxtSpec.Wrap(-1)
		gSizer.Add(sTxtSpec, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		# Add comb box for dishes specification
		cbxSpecChoices = list()
		self.cbxSpec = wx.ComboBox(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(110,-1), cbxSpecChoices, 0)
		gSizer.Add(self.cbxSpec, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add label for dishes style
		sTxtStyle = wx.StaticText(container, wx.ID_ANY, u"做法：", wx.DefaultPosition, wx.DefaultSize, 0)
		sTxtStyle.Wrap(-1)
		gSizer.Add(sTxtStyle, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		# Add combo box for dishes style
		cbxStyleChoices = list()
		self.cbxStyle = wx.ComboBox(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(110,-1), cbxStyleChoices, 0)
		gSizer.Add(self.cbxStyle, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add label for dishes state
		sTxtState = wx.StaticText(container, wx.ID_ANY, u"停用：", wx.DefaultPosition, wx.DefaultSize, 0)
		sTxtState.Wrap(-1)
		gSizer.Add(sTxtState, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add check box for dishes state
		self.cbxStop = wx.CheckBox(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0)
		gSizer.Add(self.cbxStop, 0, wx.ALIGN_CENTER, 5)
		# Layout 
		parent.Add(gSizer, 1, wx.EXPAND, 5)
		
	def _init_data_view_right_column_sizer(self, container, parent):
		# Add grid sizer with 6 rows and 2 columns
		gSizer = wx.GridSizer(6, 2, 0, 0)
		# Add label for dishes name
		sTxtName = wx.StaticText(container, wx.ID_ANY, u"菜品名称：", wx.DefaultPosition, wx.DefaultSize, 0)
		sTxtName.Wrap(-1)
		gSizer.Add(sTxtName, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add text control for dishes name
		self.txtDishName = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		gSizer.Add(self.txtDishName, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add label for dishes brevity code
		sTxtBrevityCode = wx.StaticText(container, wx.ID_ANY, u"拼音简码：", wx.DefaultPosition, wx.DefaultSize, 0)
		sTxtBrevityCode.Wrap(-1)
		gSizer.Add(sTxtBrevityCode, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add text control for dishes brevity code
		self.txtBrevityCode = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
		gSizer.Add(self.txtBrevityCode, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add label for dishes type
		sTxtType = wx.StaticText(container, wx.ID_ANY, u"所属类别：", wx.DefaultPosition, wx.DefaultSize, 0)
		sTxtType.Wrap( -1 )
		gSizer.Add(sTxtType, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add combo box for dishes type
		cbxCategoryChoices = list()
		self.cbxCategory = wx.ComboBox(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(110,-1), cbxCategoryChoices, 0)
		gSizer.Add(self.cbxCategory, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add label for dishes discount
		sTxtDiscount = wx.StaticText(container, wx.ID_ANY, u"折扣比率：", wx.DefaultPosition, wx.DefaultSize, 0)
		sTxtDiscount.Wrap(-1)
		gSizer.Add(sTxtDiscount, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add text control for dishes discount
		self.txtDiscount = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		gSizer.Add(self.txtDiscount, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add label for dishes commission
		sTxtCommition = wx.StaticText(container, wx.ID_ANY, u"提成比率：", wx.DefaultPosition, wx.DefaultSize, 0)
		sTxtCommition.Wrap(-1)
		gSizer.Add(sTxtCommition, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add label for dishes commission
		self.txtCommition = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		gSizer.Add(self.txtCommition, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Layout 
		parent.Add(gSizer, 1, wx.EXPAND, 5)
		
	def _init_image_view_sizer(self, parent):
		fgSizer = wx.FlexGridSizer(2, 1, 0, 0)
		fgSizer.SetFlexibleDirection(wx.BOTH)
		fgSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
		
		# Create image sizer contain a static bitmap 
		imageSizer = wx.BoxSizer(wx.VERTICAL)
		self.bmpImage = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size(165,165), wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL)
		imageSizer.Add(self.bmpImage, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		fgSizer.Add(imageSizer, 1, wx.EXPAND, 5)

		# Create control sizer contain tow button
		ctrlSiezr = wx.BoxSizer(wx.HORIZONTAL)
		# Add import button
		self.btnImport = wx.Button(self, wx.ID_ANY, u"图片导入", wx.DefaultPosition, wx.Size(80,30), 0|wx.TAB_TRAVERSAL)
		ctrlSiezr.Add(self.btnImport, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		# Add clean button
		self.btnClean = wx.Button(self, wx.ID_ANY, u"图片清除", wx.DefaultPosition, wx.DefaultSize, 0|wx.TAB_TRAVERSAL)
		ctrlSiezr.Add(self.btnClean, 0, wx.ALIGN_CENTER|wx.ALL, 5)

		fgSizer.Add(ctrlSiezr, 1, wx.EXPAND, 5)

		# Layout image data view
		parent.Add(fgSizer, 1, wx.EXPAND, 5)
		
	def _init_expand_sizer(self, parent):
		sbSizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"规格和做法设置"), wx.HORIZONTAL)
		
		self._init_spec_sizer(sbSizer)
		self._init_style_sizer(sbSizer)
		
		# Layout
		parent.Add(sbSizer, 1, wx.EXPAND, 5)
	
	def _init_spec_sizer(self, parent):
		sizer = wx.BoxSizer(wx.VERTICAL)
		
		viewSizer = wx.BoxSizer(wx.VERTICAL)
		# Create specification data view list 
		self.dataViewListSpec = wx.dataview.DataViewCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1,140), 0)
		# Add items into specification data view list
		self.dataViewListSpec.AppendTextColumn(u"编码", 0)
		self.dataViewListSpec.AppendTextColumn(u"规格", 1, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE) 
		self.dataViewListSpec.AppendTextColumn(u"价格", 2, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE) 
		viewSizer.Add(self.dataViewListSpec, 0, wx.ALL|wx.EXPAND, 5)
		sizer.Add(viewSizer, 1, wx.EXPAND, 5)
		
		ctrlSizer = wx.BoxSizer(wx.HORIZONTAL)
		ctrlSizer.SetMinSize(wx.Size(-1,200)) 
		# Add new button
		self.btnNewSpec = wx.Button(self, wx.ID_ANY, u"新增规格", wx.DefaultPosition, wx.DefaultSize, 0)
		ctrlSizer.Add(self.btnNewSpec, 0, wx.ALL, 5)
		# Add delete button
		self.btnDelSpec = wx.Button(self, wx.ID_ANY, u"删除规格", wx.DefaultPosition, wx.DefaultSize, 0)
		ctrlSizer.Add(self.btnDelSpec, 0, wx.ALL, 5)
		# Add save button
		self.btnSaveSpec = wx.Button(self, wx.ID_ANY, u"保存规格", wx.DefaultPosition, wx.DefaultSize, 0)
		ctrlSizer.Add(self.btnSaveSpec, 0, wx.ALL, 5) 
		sizer.Add(ctrlSizer, 1, wx.EXPAND, 5)

		# Layout specification sizer
		parent.Add(sizer, 1, wx.EXPAND, 5)
		
	def _init_style_sizer(self, parent):
		sizer = wx.BoxSizer(wx.VERTICAL)

		viewSizer = wx.BoxSizer(wx.VERTICAL)
		# Create style data view list 
		self.dataViewListStyle = wx.dataview.DataViewCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1,140), 0)
		# Add items into style data view list
		self.dataViewListStyle.AppendTextColumn(u"编码", 0)
		self.dataViewListStyle.AppendTextColumn(u"做法说明", 1, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE) 
		self.dataViewListStyle.AppendTextColumn(u"加价金额", 2, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE) 
		self.dataViewListStyle.AppendTextColumn(u"按量加价", 3, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE) 
		viewSizer.Add(self.dataViewListStyle, 0, wx.ALL|wx.EXPAND, 5)
		sizer.Add(viewSizer, 1, wx.EXPAND, 5)
		
		ctrlSizer = wx.BoxSizer(wx.HORIZONTAL)
		# Add new button
		self.btnNewStyle = wx.Button(self, wx.ID_ANY, u"新增做法", wx.DefaultPosition, wx.DefaultSize, 0)
		ctrlSizer.Add(self.btnNewStyle, 0, wx.ALL, 5 )
		# Add delete button
		self.btnDelStyle = wx.Button(self, wx.ID_ANY, u"删除做法", wx.DefaultPosition, wx.DefaultSize, 0)
		ctrlSizer.Add(self.btnDelStyle, 0, wx.ALL, 5)
		# Add save button
		self.btnSaveStyle = wx.Button(self, wx.ID_ANY, u"保存做法", wx.DefaultPosition, wx.DefaultSize, 0)
		ctrlSizer.Add(self.btnSaveStyle, 0, wx.ALL, 5)
		sizer.Add(ctrlSizer, 1, wx.EXPAND, 5)
		
		# Layout style sizer
		parent.Add(sizer, 1, wx.EXPAND, 5)

	def __init__(self, parent, type_="add"):
		wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"菜品资料维护", pos=wx.DefaultPosition, size=wx.Size(700,500), style=wx.CAPTION)

		self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

		fgSizer = wx.FlexGridSizer(3, 1, 0, 0)
		fgSizer.SetFlexibleDirection(wx.BOTH)
		fgSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

		self._init_status_bar_sizer(fgSizer)
		self._init_view_sizer(fgSizer)
		self._init_expand_sizer(fgSizer)
		
		self.SetSizer(fgSizer)
		self.Layout()
		self.Centre(wx.BOTH)

		# Create an instance of our specification model...
		self.model_spec = CModelSpec(CDataSpecInfo.GetData())

		# Tell the DVC to use the specification model
		self.dataViewListSpec.AssociateModel(self.model_spec)

		# Create an instance of our style model...
		self.model_style = CModelStyle(CDataStyleInfo.GetData())

		# Tell the DVC to use the style model
		self.dataViewListStyle.AssociateModel(self.model_style)

		# Connect Events
		self.btnPrev.Bind(wx.EVT_BUTTON, self.OnBtnPrev)
		self.btnNext.Bind(wx.EVT_BUTTON, self.OnBtnNext)
		self.btnSave.Bind(wx.EVT_BUTTON, self.OnBtnSave)
		self.btnExit.Bind(wx.EVT_BUTTON, self.OnBtnExit)
		self.btnImport.Bind(wx.EVT_BUTTON, self.OnBtnImport)
		self.btnClean.Bind(wx.EVT_BUTTON, self.OnBtnClean)
		
		self.btnNewSpec.Bind(wx.EVT_BUTTON, self.OnBtnNewSpec)
		self.btnDelSpec.Bind(wx.EVT_BUTTON, self.OnBtnDelSpec)
		self.btnSaveSpec.Bind(wx.EVT_BUTTON, self.OnBtnSaveSpec)
		
		self.btnNewStyle.Bind(wx.EVT_BUTTON, self.OnBtnNewStyle)
		self.btnDelStyle.Bind(wx.EVT_BUTTON, self.OnBtnDelStyle)
		self.btnSaveStyle.Bind(wx.EVT_BUTTON, self.OnBtnSaveStyle)

		self.txtDishName.Bind(wx.EVT_TEXT, self.OnDishNameText)

		# Initialize data view 
		self.index = 0
		self.type = type_
		self.image_url = ""
		self.item_id = 0
		self.InitailizeView()

	def __del__( self ):
		pass

	def InitailizeView(self):
		if self.type == "add":
			self.InitAddView()
		elif self.type == "mod":
			self.index = CDataDishesInfo.GetCurItemIndex()
			self.InitModView()

	def InitAddView(self):
		li_unit = CDataUnitInfo.GetData()
		for unit in li_unit:
			self.cbxUnit.Append(unit.name, unit)
		self.cbxUnit.SetSelection(0)

		li_spec = CDataSpecInfo.GetData()
		for spec in li_spec:
			self.cbxSpec.Append(spec.name, spec)
		self.cbxSpec.SetSelection(0)

		li_style = CDataStyleInfo.GetData()
		for style in li_style:
			self.cbxStyle.Append(style.name, style)
		self.cbxStyle.SetSelection(0)

		li_category = CDataCategoryInfo.GetData()
		for category in li_category:
			self.cbxCategory.Append(category.name, category)
		self.cbxCategory.SetSelection(0)

		self.txtTrack.Enable(False)
		self.btnPrev.Enable(False)
		self.btnNext.Enable(False)

	def InitModView(self):
		if self.index < 0:
			self.index = 0
			return

		items = CDataDishesInfo.GetItems()
		if self.index >= len(items):
			self.index = len(items) - 1
			return

		data = items[self.index]
		self.item_id = data.id
		self.txtDishCode.SetValue(str(data.code))
		self.txtDishName.SetValue(data.name)
		self.txtBrevityCode.SetValue(str(data.spell))
		self.txtPrice.SetValue(str(data.price))
		self.txtCommition.SetValue(str(data.commistion))
		self.txtDiscount.SetValue(str(data.discount))
		self.cbxStop.SetValue(data.stop)
		self.txtTrack.SetLabel(("%d / %d" % (self.index+1, len(items))))
		if data.image_url == "":
			self.bmpImage.SetBitmap(wx.NullBitmap)
		else:
			img = wx.Image(data.image_url, wx.BITMAP_TYPE_ANY)
			img.Rescale(165, 165)
			self.bmpImage.SetBitmap(img.ConvertToBitmap())

		li_unit = CDataUnitInfo.GetData()
		unit_selection = 0
		for unit in li_unit:
			self.cbxUnit.Append(unit.name, unit)
			if unit.code == data.unit:
				self.cbxUnit.SetSelection(unit_selection)
			unit_selection += 1

		li_spec = CDataSpecInfo.GetData()
		spec_selection = 0
		for spec in li_spec:
			self.cbxSpec.Append(spec.name, spec)
			if spec.code == data.spec:
				self.cbxSpec.SetSelection(spec_selection)
			spec_selection += 1

		li_style = CDataStyleInfo.GetData()
		style_selection = 0
		for style in li_style:
			self.cbxStyle.Append(style.name, style)
			if style.code == data.style:
				self.cbxStyle.SetSelection(style_selection)
			style_selection += 1

		li_category = CDataCategoryInfo.GetData()
		category_selection = 0
		for category in li_category:
			self.cbxCategory.Append(category.name, category)
			if category.code == data.category:
				self.cbxCategory.SetSelection(category_selection)
			category_selection += 1

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
		unit = self.cbxUnit.GetClientData(self.cbxUnit.GetSelection())
		spec = self.cbxSpec.GetClientData(self.cbxSpec.GetSelection())
		style = self.cbxStyle.GetClientData(self.cbxStyle.GetSelection())
		category = self.cbxCategory.GetClientData(self.cbxCategory.GetSelection())
		data = CDataDishes(0, self.item_id, 
						int(self.txtDishCode.GetValue()), 
						self.txtDishName.GetValue(), 
						self.txtBrevityCode.GetValue(),
						spec.code, 
						category.code, 
						int(self.txtPrice.GetValue()), 
						unit.code,
						style.code,
						float(self.txtCommition.GetValue()),
						float(self.txtDiscount.GetValue()),
						self.cbxStop.GetValue(),
						self.image_url, "")
		if self.type == "add":
			CDataDishesInfo.AddItem(data)
		elif self.type == "mod":
			CDataDishesInfo.UpdateItem(data)

	def OnBtnExit( self, event ):
		event.Skip()
		self.Close()

	def OnBtnImport( self, event ):
		event.Skip()
		dlg = wx.FileDialog(
            self, message=u"选择图片",
            defaultDir="E:", #os.getcwd(), 
            defaultFile="",
            wildcard=wildcard,
            style=wx.OPEN | wx.CHANGE_DIR
            )

		# Show the dialog and retrieve the user response. If it is the OK response, 
		# process the data.
		if dlg.ShowModal() == wx.ID_OK:
			# This returns a Python list of files that were selected.
			paths = dlg.GetPath()
			self.image_url = paths

			img = wx.Image(self.image_url, wx.BITMAP_TYPE_ANY)
			img.Rescale(165, 165)
			self.bmpImage.SetBitmap(img.ConvertToBitmap())

	def OnBtnClean( self, event ):
		event.Skip()
		self.image_url = ""
		self.bmpImage.SetBitmap(wx.NullBitmap)

	def OnBtnNewSpec( self, event ):
		event.Skip()
		CDataSpecInfo.AddItem(CDataSpec(0, "", 0))

		data = CDataSpec(CDataSpecInfo.GetId(), "", 0)
		self.model_spec.data.append(data)
		item = self.model_spec.ObjectToItem(data)
		self.dataViewListSpec.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)

	def OnBtnDelSpec( self, event ):
		event.Skip()
		item = self.dataViewListSpec.GetCurrentItem()
		data = self.model_spec.ItemToObject(item)
		self.model_spec.data.remove(data)
		self.dataViewListSpec.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
		CDataSpecInfo.DeleteItem(data)

	def OnBtnSaveSpec( self, event ):
		event.Skip()
		item = self.dataViewListSpec.GetCurrentItem()
		data = self.model_spec.ItemToObject(item)
		CDataSpecInfo.UpdateItem(data)

	def OnBtnNewStyle( self, event ):
		event.Skip()
		CDataStyleInfo.AddItem(CDataStyle(0, "", 0, "N"))

		data = CDataStyle(CDataStyleInfo.GetId(), "", 0, "N")
		self.model_style.data.append(data)
		item = self.model_style.ObjectToItem(data)
		self.dataViewListStyle.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)

	def OnBtnDelStyle( self, event ):
		event.Skip()
		item = self.dataViewListStyle.GetCurrentItem()
		data = self.model_style.ItemToObject(item)
		self.model_style.data.remove(data)
		self.dataViewListStyle.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
		CDataStyleInfo.DeleteItem(data)

	def OnBtnSaveStyle( self, event ):
		event.Skip()
		item = self.dataViewListStyle.GetCurrentItem()
		data = self.model_style.ItemToObject(item)
		CDataStyleInfo.UpdateItem(data)

	def OnDishNameText( self, event ):
		event.Skip()
		brevity_code = CBrevityCode.MultiGetLetter(self.txtDishName.GetValue())
		print brevity_code
		self.txtBrevityCode.SetValue(brevity_code)

if __name__ == '__main__':
	app = wx.PySimpleApp()
	dlg = CPopDishesInfo(None, "mod")
	dlg.Show()
	app.MainLoop()

