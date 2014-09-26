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
from framework.core import BrevityCode

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class CPopCategorySetting
###########################################################################

class PopCategorySetting (wx.Dialog):
    def _init_view_sizer(self, parent):
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Create data view list
        self.dataViewList = wx.dataview.DataViewCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.dataViewList.SetMinSize(wx.Size(600,300))
        # Add items into data view list
        self.dataViewList.AppendTextColumn(u"行号", 0) 
        self.dataViewList.AppendTextColumn(u"编码", 1, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE) 
        self.dataViewList.AppendTextColumn(u"菜品类名", 2, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE) 
        sizer.Add(self.dataViewList, 0, wx.ALL|wx.EXPAND, 5)
        
        # Layout data view list
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
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"菜品类别设置", pos=wx.DefaultPosition, size=wx.Size(600,400), style=wx.CAPTION|wx.TAB_TRAVERSAL) 
        self.SetSizeHintsSz(wx.Size(-1,-1), wx.Size(-1,-1))
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        self._init_view_sizer(sizer)
        self._init_ctrl_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)
        
        # Create an instance of our model...
        self.model = ModelCategory(CtrlCategory.GetData())
        
        # Tell the DVC to use the model
        self.dataViewList.AssociateModel(self.model)

        # Connect Events
        self.btnNew.Bind(wx.EVT_BUTTON, self.OnBtnNew)
        self.btnDelete.Bind(wx.EVT_BUTTON, self.OnBtnDelete)
        self.btnRefresh.Bind(wx.EVT_BUTTON, self.OnBtnRefresh)
        self.btnSave.Bind(wx.EVT_BUTTON, self.OnBtnSave)
        self.btnExit.Bind(wx.EVT_BUTTON, self.OnBtnExit)
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, override them in your derived class
    def OnBtnNew( self, event ):
        event.Skip()
        CtrlCategory.AddItem(DataCategory(0, 0, ""))
        
        data = DataCategory(CtrlCategory.GetDataLen() + 1, CtrlCategory.GetId(), "")
        self.model.data.append(data)
        item = self.model.ObjectToItem(data)
        self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
    
    def OnBtnDelete( self, event ):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        self.model.data.remove(data)
        self.dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
        CtrlCategory.DeleteItem(data)
    
    def OnBtnRefresh( self, event ):
        event.Skip()
        
        result = CtrlCategory.GetData()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
                    
        self.model.Cleared()
    
    def OnBtnSave( self, event ):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        CtrlCategory.UpdateItem(data)
    
    def OnBtnExit( self, event ):
        event.Skip()
        self.Close()

###########################################################################
## Class CPopDishesInfo
###########################################################################

# This is how you pre-establish a file filter so that the dialog
# only shows the extension(s) you want it to.
wildcard = "bitmap image (*.bmp)|*.bmp|"    \
           "png image (*.png)|*.png|"         \
           "jpg image (*.jpg)|*.jpg|"         \
           "jpeg image (*.jpeg)|*.jpeg|"      \
           "All files (*.*)|*.*"

class PopDishesInfo (wx.Dialog):
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
        self.model_spec = ModelSpec(CtrlSpec.GetData())

        # Tell the DVC to use the specification model
        self.dataViewListSpec.AssociateModel(self.model_spec)

        # Create an instance of our style model...
        self.model_style = ModelStyle(CtrlStyle.GetData())

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
            self.index = CtrlDishes.GetCurItemIndex()
            self.InitModView()

    def InitAddView(self):
        li_unit = CtrlUnit.GetData()
        for unit in li_unit:
            self.cbxUnit.Append(unit.name, unit)
        self.cbxUnit.SetSelection(0)

        li_spec = CtrlSpec.GetData()
        for spec in li_spec:
            self.cbxSpec.Append(spec.name, spec)
        self.cbxSpec.SetSelection(0)

        li_style = CtrlStyle.GetData()
        for style in li_style:
            self.cbxStyle.Append(style.name, style)
        self.cbxStyle.SetSelection(0)

        li_category = CtrlCategory.GetData()
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

        items = CtrlDishes.GetItems()
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

        li_unit = CtrlUnit.GetData()
        unit_selection = 0
        for unit in li_unit:
            self.cbxUnit.Append(unit.name, unit)
            if unit.code == data.unit:
                self.cbxUnit.SetSelection(unit_selection)
            unit_selection += 1

        li_spec = CtrlSpec.GetData()
        spec_selection = 0
        for spec in li_spec:
            self.cbxSpec.Append(spec.name, spec)
            if spec.code == data.spec:
                self.cbxSpec.SetSelection(spec_selection)
            spec_selection += 1

        li_style = CtrlStyle.GetData()
        style_selection = 0
        for style in li_style:
            self.cbxStyle.Append(style.name, style)
            if style.code == data.style:
                self.cbxStyle.SetSelection(style_selection)
            style_selection += 1

        li_category = CtrlCategory.GetData()
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
        data = DataDishes(0, self.item_id, 
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
            CtrlDishes.AddItem(data)
        elif self.type == "mod":
            CtrlDishes.UpdateItem(data)

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
        CtrlSpec.AddItem(DataSpec(0, "", 0))

        data = DataSpec(CtrlSpec.GetId(), "", 0)
        self.model_spec.data.append(data)
        item = self.model_spec.ObjectToItem(data)
        self.dataViewListSpec.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)

    def OnBtnDelSpec( self, event ):
        event.Skip()
        item = self.dataViewListSpec.GetCurrentItem()
        data = self.model_spec.ItemToObject(item)
        self.model_spec.data.remove(data)
        self.dataViewListSpec.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
        CtrlSpec.DeleteItem(data)

    def OnBtnSaveSpec( self, event ):
        event.Skip()
        item = self.dataViewListSpec.GetCurrentItem()
        data = self.model_spec.ItemToObject(item)
        CtrlSpec.UpdateItem(data)

    def OnBtnNewStyle( self, event ):
        event.Skip()
        CtrlStyle.AddItem(DataStyle(0, "", 0, "N"))

        data = DataStyle(CtrlStyle.GetId(), "", 0, "N")
        self.model_style.data.append(data)
        item = self.model_style.ObjectToItem(data)
        self.dataViewListStyle.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)

    def OnBtnDelStyle( self, event ):
        event.Skip()
        item = self.dataViewListStyle.GetCurrentItem()
        data = self.model_style.ItemToObject(item)
        self.model_style.data.remove(data)
        self.dataViewListStyle.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
        CtrlStyle.DeleteItem(data)

    def OnBtnSaveStyle( self, event ):
        event.Skip()
        item = self.dataViewListStyle.GetCurrentItem()
        data = self.model_style.ItemToObject(item)
        CtrlStyle.UpdateItem(data)

    def OnDishNameText( self, event ):
        event.Skip()
        brevity_code = BrevityCode.MultiGetLetter(self.txtDishName.GetValue())
        print brevity_code
        self.txtBrevityCode.SetValue(brevity_code)

###########################################################################
## Class CPopUnitSetting
###########################################################################

class PopUnitSetting (wx.Dialog):
    def _init_view_sizer(self, parent):
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Create data view list
        self.dataViewList = wx.dataview.DataViewCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.dataViewList.SetMinSize(wx.Size(600,300))
        # Add items into data view list
        self.dataViewList.AppendTextColumn(u"行号", 0) 
        self.dataViewList.AppendTextColumn(u"编码", 1, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE) 
        self.dataViewList.AppendTextColumn(u"菜品单位", 2, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE) 
        sizer.Add(self.dataViewList, 0, wx.ALL|wx.EXPAND, 5)
        # Layout data view 
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
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"菜品单位设置", pos=wx.DefaultPosition, size=wx.Size(600,400), style=wx.CAPTION|wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz( wx.Size( -1,-1 ), wx.Size( -1,-1 ) )
        
        sizer = wx.BoxSizer(wx.VERTICAL) 
        self._init_view_sizer(sizer)
        self._init_ctrl_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout() 
        self.Centre(wx.BOTH)

        # Create an instance of our model...
        self.model = ModelUnit(CtrlUnit.GetData())
        
        # Tell the DVC to use the model
        self.dataViewList.AssociateModel(self.model)
        
        # Connect Events
        self.btnNew.Bind(wx.EVT_BUTTON, self.OnBtnNew)
        self.btnDelete.Bind(wx.EVT_BUTTON, self.OnBtnDelete)
        self.btnRefresh.Bind(wx.EVT_BUTTON, self.OnBtnRefresh)
        self.btnSave.Bind(wx.EVT_BUTTON, self.OnBtnSave)
        self.btnExit.Bind(wx.EVT_BUTTON, self.OnBtnExit)
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, override them in your derived class
    def OnBtnNew( self, event ):
        event.Skip()
        CtrlUnit.AddItem(DataUnit(0, 0, ""))
        
        data = DataUnit(CtrlUnit.GetDataLen() + 1, CtrlUnit.GetId(), "")
        self.model.data.append(data)
        item = self.model.ObjectToItem(data)
        self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
    
    def OnBtnDelete( self, event ):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        self.model.data.remove(data)
        self.dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
        CtrlUnit.DeleteItem(data)
    
    def OnBtnRefresh( self, event ):
        event.Skip()
        result = CtrlUnit.GetData()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
                    
        self.model.Cleared()
    
    def OnBtnSave( self, event ):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        CtrlUnit.UpdateItem(data)
    
    def OnBtnExit( self, event ):
        event.Skip()
        self.Close()

###########################################################################
## Class CWgtDishesPublish
###########################################################################

class WgtDishesPublish (wx.Panel):
    def _init_status_bar_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.SetMinSize(wx.Size(-1,50)) 

        # Add new button
        self.btnNew = wx.Button(self, wx.ID_ANY, u"新增", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnNew.SetMinSize(wx.Size(50,50))
        sizer.Add(self.btnNew, 0, 0, 5)
        # Add modify button
        self.btnModify = wx.Button(self, wx.ID_ANY, u"修改", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnModify.SetMinSize(wx.Size(50,50))
        sizer.Add(self.btnModify, 0, 0, 5)
        # Add delete button
        self.btnDelete = wx.Button(self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnDelete.SetMinSize(wx.Size(50,50))
        sizer.Add(self.btnDelete, 0, 0, 5)
        # Add dishes type button
        self.btnType = wx.Button(self, wx.ID_ANY, u"类型", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnType.SetMinSize(wx.Size(50,50))
        sizer.Add(self.btnType, 0, 0, 5)
        # Add dishes unit button
        self.btnUnit = wx.Button(self, wx.ID_ANY, u"单位", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnUnit.SetMinSize(wx.Size(50,50))
        sizer.Add(self.btnUnit, 0, 0, 5)
        # Add refresh button
        self.btnRefresh = wx.Button(self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnRefresh.SetMinSize(wx.Size(50,50))
        sizer.Add(self.btnRefresh, 0, 0, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnExit.SetMinSize(wx.Size(50,50))
        sizer.Add(self.btnExit, 0, 0, 5)
        # Add space fix panel 
        self.topPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.topPanel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
        sizer.Add(self.topPanel, 1, wx.EXPAND, 5)
        
        # Layout status bar
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_view_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # This sizer for tree control
        leftSizer = wx.BoxSizer(wx.VERTICAL) 
        leftSizer.SetMinSize(wx.Size(200,600)) 
        # Create a tree control
        self.treeCtrl = wx.TreeCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE)
        self.treeCtrl.SetMinSize(wx.Size(-1,600))
        leftSizer.Add(self.treeCtrl, 0, wx.EXPAND, 5)
        # Layout tree control
        sizer.Add(leftSizer, 1, 0, 5)
        
        # This sizer for data view list
        rightSizer = wx.BoxSizer(wx.VERTICAL)
        rightSizer.SetMinSize(wx.Size(600,600)) 
        # Create a data view list
        self.dataViewList = wx.dataview.DataViewCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1,600), 0)
        # Add items into data view list
        self.dataViewList.AppendTextColumn(u"行号", 0) 
        self.dataViewList.AppendTextColumn(u"品码", 1) 
        self.dataViewList.AppendTextColumn(u"品名", 2) 
        self.dataViewList.AppendTextColumn(u"拼音简码", 3) 
        self.dataViewList.AppendTextColumn(u"规格", 4) 
        self.dataViewList.AppendTextColumn(u"做法", 5) 
        self.dataViewList.AppendTextColumn(u"所属类", 6) 
        self.dataViewList.AppendTextColumn(u"单位", 7) 
        self.dataViewList.AppendTextColumn(u"售价", 8) 
        self.dataViewList.AppendToggleColumn(u"停用", 9) 
        rightSizer.Add(self.dataViewList, 0, wx.EXPAND|wx.LEFT, 5)
        # Layout data view list
        sizer.Add(rightSizer, 1, 0, 5)
        
        # Layout view sizer
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
        self.model = ModelDishes(CtrlDishes.GetData())
        CtrlDishes.RefreshItems()
        
        # Tel the DVC to use the model
        self.dataViewList.AssociateModel(self.model)

        # Connect Events
        self.Bind(wx.EVT_SIZE, self.OnSize)
        
        self.btnNew.Bind(wx.EVT_BUTTON, self.OnBtnNew)
        self.btnModify.Bind(wx.EVT_BUTTON, self.OnBtnModify)
        self.btnDelete.Bind(wx.EVT_BUTTON, self.OnBtnDelete)
        self.btnType.Bind(wx.EVT_BUTTON, self.OnBtnType)
        self.btnUnit.Bind(wx.EVT_BUTTON, self.OnBtnUnit)
        self.btnRefresh.Bind(wx.EVT_BUTTON, self.OnBtnRefresh)
        self.btnExit.Bind(wx.EVT_BUTTON, self.OnBtnExit)
        
        # Show tree control
        self.ShowTreeCtrl()
    
    def __del__( self ):
        pass
    
    def Initailize(self):
        # Add event listener
        EvtManager.AddListener(self, EnumEvent.EVT_DISHES_PUBLISH_REFRESH, self.OnBtnRefresh)
        
        x, y = CtrlHomePage.GetFrameSize()        
        self.SetSize(wx.Size(x, y))

    def Uninitailize(self):
        # Remove event listener
        EvtManager.RemoveListener(self, EnumEvent.EVT_DISHES_PUBLISH_REFRESH, self.OnBtnRefresh)
    
    def ShowTreeCtrl(self):
        isz = (16,16)
        il = wx.ImageList(isz[0], isz[1])
        fldridx     = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER,      wx.ART_OTHER, isz))
        fldropenidx = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER_OPEN, wx.ART_OTHER, isz))
        fileidx     = il.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, isz))
        
        self.treeCtrl.SetImageList(il)
        self.il = il

        self.root = self.treeCtrl.AddRoot(u"全部菜品")
        self.treeCtrl.SetPyData(self.root, None)
        self.treeCtrl.SetItemImage(self.root, fldridx, wx.TreeItemIcon_Normal)
        self.treeCtrl.SetItemImage(self.root, fldropenidx, wx.TreeItemIcon_Expanded)
        
        dishes_map = dict()
        li_items = CtrlDishes.GetItems()
        for item in li_items:
            if dishes_map.has_key(item.category):
                dishes_map[item.category].append(item)
            else:
                list_tmp = []
                list_tmp.append(item)
                dishes_map_tmp = {item.category:list_tmp}
                dishes_map.update(dishes_map_tmp)
        
        li_category = CtrlCategory.GetData()
        for category in li_category:
            if dishes_map.has_key(category.code):
                title = "%s(%d)" % (category.name, len(dishes_map[category.code]))
                child = self.treeCtrl.AppendItem(self.root, title)
                self.treeCtrl.SetPyData(child, None)
                self.treeCtrl.SetItemImage(child, fldridx, wx.TreeItemIcon_Normal)
                self.treeCtrl.SetItemImage(child, fldropenidx, wx.TreeItemIcon_Expanded)
                for dishes in dishes_map[category.code]:
                    sub_clild = self.treeCtrl.AppendItem(child, dishes.name)
                    self.treeCtrl.SetPyData(sub_clild, None)
                    self.treeCtrl.SetItemImage(sub_clild, fileidx, wx.TreeItemIcon_Normal)
                    self.treeCtrl.SetItemImage(sub_clild, fileidx, wx.TreeItemIcon_Selected)
            else:
                title = "%s(0)" % category.name
                child = self.treeCtrl.AppendItem(self.root, title)
                self.treeCtrl.SetPyData(child, None)
                self.treeCtrl.SetItemImage(child, fldridx, wx.TreeItemIcon_Normal)
                self.treeCtrl.SetItemImage(child, fldropenidx, wx.TreeItemIcon_Expanded)
                
        self.treeCtrl.Expand(self.root)
    
    def RefreshUI(self):
        # Refresh treeCtrl
        CtrlDishes.RefreshItems()
        self.treeCtrl.DeleteAllItems()
        self.ShowTreeCtrl()
        
        # Refresh data view list
        result = CtrlDishes.GetData()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
                    
        self.model.Cleared()
    
    # Virtual event handlers, override them in your derived class
    def OnSize(self, event):
        event.Skip()
        x, y = self.GetSize()
        
        self.btnNew.SetMaxSize(wx.Size(50,50))
        self.btnModify.SetMaxSize(wx.Size(50,50))
        self.btnDelete.SetMaxSize(wx.Size(50,50))
        self.btnType.SetMaxSize(wx.Size(50,50))
        self.btnUnit.SetMaxSize(wx.Size(50,50))
        self.btnRefresh.SetMaxSize(wx.Size(50,50))
        self.btnExit.SetMaxSize(wx.Size(50,50))
        self.topPanel.SetMaxSize(wx.Size(x-350,50)) 
        self.treeCtrl.SetMinSize(wx.Size(200,y-50))
        self.dataViewList.SetMinSize(wx.Size(x-200,y-50))
        
    def OnBtnNew(self, event):
        event.Skip()
        self.popDishesInfo = PopDishesInfo(self, "add")
        self.popDishesInfo.ShowModal()
    
    def OnBtnModify(self, event):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        index = self.model.data.index(data)
        CtrlDishes.SetCurItemIndex(index)
        self.popDishesInfo = PopDishesInfo(self, "mod")
        self.popDishesInfo.ShowModal()
    
    def OnBtnDelete(self, event):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        self.model.data.remove(data)
        self.dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
        CtrlDishes.DeleteItem(data)
    
    def OnBtnType(self, event):
        event.Skip()
        self.popCategory = PopCategorySetting(self)
        self.popCategory.ShowModal()
    
    def OnBtnUnit(self, event):
        event.Skip()
        self.popUnit = PopUnitSetting(self)
        self.popUnit.ShowModal()
    
    def OnBtnRefresh(self, event):
        event.Skip()
        self.RefreshUI()
    
    def OnBtnExit(self, event):
        event.Skip()
        CtrlHomePage.SetSelectedItem()
        AppManager.SwitchToApplication('HomePage')
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = WgtDishesPublish(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()
