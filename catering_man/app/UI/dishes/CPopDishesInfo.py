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
from framework.CBrevityCode import CBrevityCode

###########################################################################
## Class CPopDishesInfo
###########################################################################

# This is how you pre-establish a file filter so that the dialog
# only shows the extension(s) you want it to.
wildcard = "png image (*.png)|*.png|"     \
           "jpg image (*.jpg)|*.jpg|"     \
           "All files (*.*)|*.*"

class CPopDishesInfo ( wx.Dialog ):
    
    def __init__( self, parent, type = "add" ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"菜品资料维护", pos = wx.DefaultPosition, size = wx.Size( 700,500 ), style = wx.CAPTION )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        m_fgSizer = wx.FlexGridSizer( 3, 1, 0, 0 )
        m_fgSizer.SetFlexibleDirection( wx.BOTH )
        m_fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        m_topSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticTxtNum = wx.StaticText( self, wx.ID_ANY, u"1 / 1", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTxtNum.Wrap( -1 )
        m_topSizer.Add( self.m_staticTxtNum, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_btnPrev = wx.Button( self, wx.ID_ANY, u"上一记录", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_topSizer.Add( self.m_btnPrev, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_btnNext = wx.Button( self, wx.ID_ANY, u"下一记录", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_topSizer.Add( self.m_btnNext, 0, wx.ALL, 5 )
        
        
        m_topSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_btnSave = wx.Button( self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_topSizer.Add( self.m_btnSave, 0, wx.ALL, 5 )
        
        self.m_btnExit = wx.Button( self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_topSizer.Add( self.m_btnExit, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_fgSizer.Add( m_topSizer, 1, wx.EXPAND, 5 )
        
        m_midFgSizer = wx.FlexGridSizer( 0, 2, 0, 0 )
        m_midFgSizer.SetFlexibleDirection( wx.BOTH )
        m_midFgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        m_midLeftSizer = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,200 ), wx.STATIC_BORDER|wx.TAB_TRAVERSAL )
        self.m_panel.SetMaxSize( wx.Size( -1,200 ) )
        
        m_panelSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        m_panelSizer.SetMinSize( wx.Size( 500,200 ) ) 
        m_midLeftGSizer = wx.GridSizer( 6, 2, 0, 0 )
        
        self.m_staticText1 = wx.StaticText( self.m_panel, wx.ID_ANY, u"品码：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        m_midLeftGSizer.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_txtDishCode = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        m_midLeftGSizer.Add( self.m_txtDishCode, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_staticText2 = wx.StaticText( self.m_panel, wx.ID_ANY, u"单位：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        m_midLeftGSizer.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        m_cbxUnitChoices = []
        self.m_cbxUnit = wx.ComboBox( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(110,-1), m_cbxUnitChoices, 0 )
        m_midLeftGSizer.Add( self.m_cbxUnit, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_staticText3 = wx.StaticText( self.m_panel, wx.ID_ANY, u"售价：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        m_midLeftGSizer.Add( self.m_staticText3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_txtPrice = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        m_midLeftGSizer.Add( self.m_txtPrice, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_staticText4 = wx.StaticText( self.m_panel, wx.ID_ANY, u"规格：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        m_midLeftGSizer.Add( self.m_staticText4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        m_cbxSpecChoices = []
        self.m_cbxSpec = wx.ComboBox( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(110,-1), m_cbxSpecChoices, 0 )
        m_midLeftGSizer.Add( self.m_cbxSpec, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_staticText5 = wx.StaticText( self.m_panel, wx.ID_ANY, u"做法：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        m_midLeftGSizer.Add( self.m_staticText5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        m_cbxStyleChoices = []
        self.m_cbxStyle = wx.ComboBox( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(110,-1), m_cbxStyleChoices, 0 )
        m_midLeftGSizer.Add( self.m_cbxStyle, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_staticText101 = wx.StaticText( self.m_panel, wx.ID_ANY, u"停用：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText101.Wrap( -1 )
        m_midLeftGSizer.Add( self.m_staticText101, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_cbxStop = wx.CheckBox( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        m_midLeftGSizer.Add( self.m_cbxStop, 0, wx.ALIGN_CENTER, 5 )
        
        
        m_panelSizer.Add( m_midLeftGSizer, 1, wx.EXPAND, 5 )
        
        m_midRightGSizer = wx.GridSizer( 6, 2, 0, 0 )
        
        self.m_staticText6 = wx.StaticText( self.m_panel, wx.ID_ANY, u"菜品名称：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        m_midRightGSizer.Add( self.m_staticText6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_txtDishName = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        m_midRightGSizer.Add( self.m_txtDishName, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_staticText7 = wx.StaticText( self.m_panel, wx.ID_ANY, u"拼音简码：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        m_midRightGSizer.Add( self.m_staticText7, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_txtBrevityCode = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        m_midRightGSizer.Add( self.m_txtBrevityCode, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_staticText8 = wx.StaticText( self.m_panel, wx.ID_ANY, u"所属类别：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )
        m_midRightGSizer.Add( self.m_staticText8, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        m_cbxCategoryChoices = []
        self.m_cbxCategory = wx.ComboBox( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(110,-1), m_cbxCategoryChoices, 0 )
        m_midRightGSizer.Add( self.m_cbxCategory, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_staticText9 = wx.StaticText( self.m_panel, wx.ID_ANY, u"折扣比率：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        m_midRightGSizer.Add( self.m_staticText9, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_txtDiscount = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        m_midRightGSizer.Add( self.m_txtDiscount, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_staticText10 = wx.StaticText( self.m_panel, wx.ID_ANY, u"提成比率：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )
        m_midRightGSizer.Add( self.m_staticText10, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_txtCommition = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        m_midRightGSizer.Add( self.m_txtCommition, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_panelSizer.Add( m_midRightGSizer, 1, wx.EXPAND, 5 )
        
        
        self.m_panel.SetSizer( m_panelSizer )
        self.m_panel.Layout()
        m_midLeftSizer.Add( self.m_panel, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        m_midFgSizer.Add( m_midLeftSizer, 1, wx.EXPAND, 5 )
        
        m_midRightFgSizer = wx.FlexGridSizer( 2, 1, 0, 0 )
        m_midRightFgSizer.SetFlexibleDirection( wx.BOTH )
        m_midRightFgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        m_midImageSizer = wx.BoxSizer( wx.VERTICAL )
        
        self.m_bmpImage = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 165,165 ), wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL )
        m_midImageSizer.Add( self.m_bmpImage, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_midRightFgSizer.Add( m_midImageSizer, 1, wx.EXPAND, 5 )
        
        m_midCtrlSiezr = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_btnImport = wx.Button( self, wx.ID_ANY, u"图片导入", wx.DefaultPosition, wx.Size( 80,30 ), 0|wx.TAB_TRAVERSAL )
        m_midCtrlSiezr.Add( self.m_btnImport, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.m_btnClean = wx.Button( self, wx.ID_ANY, u"图片清除", wx.DefaultPosition, wx.DefaultSize, 0|wx.TAB_TRAVERSAL )
        m_midCtrlSiezr.Add( self.m_btnClean, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        m_midRightFgSizer.Add( m_midCtrlSiezr, 1, wx.EXPAND, 5 )
        
        
        m_midFgSizer.Add( m_midRightFgSizer, 1, wx.EXPAND, 5 )
        
        
        m_fgSizer.Add( m_midFgSizer, 1, wx.EXPAND, 5 )
        
        m_sbSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"规格和做法设置" ), wx.HORIZONTAL )
        
        m_bottomLeftSizer = wx.BoxSizer( wx.VERTICAL )
        
        m_specListSizer = wx.BoxSizer( wx.VERTICAL )
        
        self.m_dataViewListSpec = wx.dataview.DataViewCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,140 ), 0 )
        
        # Create an instance of our model...
        self.model_spec = CModelSpec(CDataSpecInfo.GetData())
        
        # Tel the DVC to use the model
        self.m_dataViewListSpec.AssociateModel(self.model_spec)
        
        self.m_dataViewListCode = self.m_dataViewListSpec.AppendTextColumn( u"编码", 0 )
        self.m_dataViewListName = self.m_dataViewListSpec.AppendTextColumn( u"规格", 1, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE ) 
        self.m_dataViewListPrice = self.m_dataViewListSpec.AppendTextColumn( u"价格", 2, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE ) 
        m_specListSizer.Add( self.m_dataViewListSpec, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        m_bottomLeftSizer.Add( m_specListSizer, 1, wx.EXPAND, 5 )
        
        m_specCtrlSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        m_specCtrlSizer.SetMinSize( wx.Size( -1,200 ) ) 
        self.m_btnNewSpec = wx.Button( self, wx.ID_ANY, u"新增规格", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_specCtrlSizer.Add( self.m_btnNewSpec, 0, wx.ALL, 5 )
        
        self.m_btnDelSpec = wx.Button( self, wx.ID_ANY, u"删除规格", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_specCtrlSizer.Add( self.m_btnDelSpec, 0, wx.ALL, 5 )
        
        self.m_btnSaveSpec = wx.Button( self, wx.ID_ANY, u"保存规格", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_specCtrlSizer.Add( self.m_btnSaveSpec, 0, wx.ALL, 5 )
        
        
        m_bottomLeftSizer.Add( m_specCtrlSizer, 1, wx.EXPAND, 5 )
        
        
        m_sbSizer.Add( m_bottomLeftSizer, 1, wx.EXPAND, 5 )
        
        m_bottomRightSizer = wx.BoxSizer( wx.VERTICAL )
        
        m_styleListSizer = wx.BoxSizer( wx.VERTICAL )
        
        self.m_dataViewListStyle = wx.dataview.DataViewCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,140 ), 0 )
        
        # Create an instance of our model...
        self.model_style = CModelStyle(CDataStyleInfo.GetData())
        
        # Tel the DVC to use the model
        self.m_dataViewListStyle.AssociateModel(self.model_style)
        
        self.m_dataViewListStyleCode = self.m_dataViewListStyle.AppendTextColumn( u"编码", 0 )
        self.m_dataViewListStyleName = self.m_dataViewListStyle.AppendTextColumn( u"做法说明", 1, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE ) 
        self.m_dataViewListAddPrice = self.m_dataViewListStyle.AppendTextColumn( u"加价金额", 2, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE ) 
        self.m_dataViewListAddUnit = self.m_dataViewListStyle.AppendTextColumn( u"按量加价", 3, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE ) 
        m_styleListSizer.Add( self.m_dataViewListStyle, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        m_bottomRightSizer.Add( m_styleListSizer, 1, wx.EXPAND, 5 )
        
        m_styleCtrlSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_btnNewStyle = wx.Button( self, wx.ID_ANY, u"新增做法", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_styleCtrlSizer.Add( self.m_btnNewStyle, 0, wx.ALL, 5 )
        
        self.m_btnDelStyle = wx.Button( self, wx.ID_ANY, u"删除做法", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_styleCtrlSizer.Add( self.m_btnDelStyle, 0, wx.ALL, 5 )
        
        self.m_btnSaveStyle = wx.Button( self, wx.ID_ANY, u"保存做法", wx.DefaultPosition, wx.DefaultSize, 0 )
        m_styleCtrlSizer.Add( self.m_btnSaveStyle, 0, wx.ALL, 5 )
        
        
        m_bottomRightSizer.Add( m_styleCtrlSizer, 1, wx.EXPAND, 5 )
        
        
        m_sbSizer.Add( m_bottomRightSizer, 1, wx.EXPAND, 5 )
        
        
        m_fgSizer.Add( m_sbSizer, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( m_fgSizer )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_btnPrev.Bind( wx.EVT_BUTTON, self.OnBtnPrev )
        self.m_btnNext.Bind( wx.EVT_BUTTON, self.OnBtnNext )
        self.m_btnSave.Bind( wx.EVT_BUTTON, self.OnBtnSave )
        self.m_btnExit.Bind( wx.EVT_BUTTON, self.OnBtnExit )
        self.m_btnImport.Bind( wx.EVT_BUTTON, self.OnBtnImport )
        self.m_btnClean.Bind( wx.EVT_BUTTON, self.OnBtnClean )
        self.m_btnNewSpec.Bind( wx.EVT_BUTTON, self.OnBtnNewSpec )
        self.m_btnDelSpec.Bind( wx.EVT_BUTTON, self.OnBtnDelSpec )
        self.m_btnSaveSpec.Bind( wx.EVT_BUTTON, self.OnBtnSaveSpec )
        self.m_btnNewStyle.Bind( wx.EVT_BUTTON, self.OnBtnNewStyle )
        self.m_btnDelStyle.Bind( wx.EVT_BUTTON, self.OnBtnDelStyle )
        self.m_btnSaveStyle.Bind( wx.EVT_BUTTON, self.OnBtnSaveStyle )
        
        self.m_txtDishName.Bind( wx.EVT_TEXT, self.OnDishNameText )
    
        # Initailize 
        self.index = 0
        self.type = type
        self.image_url = ""
        self.item_id = 0
        self.Initailize()
        
    def __del__( self ):
        pass
    
    def Initailize(self):
        if self.type == "add":
            self.InitAddInfo()
        elif self.type == "mod":
            self.index = CDataDishesInfo.GetCurItemIndex()
            self.InitModInfo()
            
    def InitAddInfo(self):
        li_unit = CDataUnitInfo.GetData()
        for unit in li_unit:
            self.m_cbxUnit.Append(unit.name, unit)
        self.m_cbxUnit.SetSelection(0)
            
        li_spec = CDataSpecInfo.GetData()
        for spec in li_spec:
            self.m_cbxSpec.Append(spec.name, spec)
        self.m_cbxSpec.SetSelection(0)
        
        li_style = CDataStyleInfo.GetData()
        for style in li_style:
            self.m_cbxStyle.Append(style.name, style)
        self.m_cbxStyle.SetSelection(0)
        
        li_category = CDataCategoryInfo.GetData()
        for category in li_category:
            self.m_cbxCategory.Append(category.name, category)
        self.m_cbxCategory.SetSelection(0)
        
        self.m_staticTxtNum.Enable(False)
        self.m_btnPrev.Enable(False)
        self.m_btnNext.Enable(False)
        
    def InitModInfo(self):
        if self.index < 0:
            self.index = 0
            return
        
        items = CDataDishesInfo.GetItems()
        if self.index >= len(items):
            self.index = len(items) - 1
            return
        
        data = items[self.index]
        self.item_id = data.id
        self.m_txtDishCode.SetValue(str(data.code))
        self.m_txtDishName.SetValue(data.name)
        self.m_txtBrevityCode.SetValue(str(data.spell))
        self.m_txtPrice.SetValue(str(data.price))
        self.m_txtCommition.SetValue(str(data.commistion))
        self.m_txtDiscount.SetValue(str(data.discount))
        self.m_cbxStop.SetValue(data.stop)
        self.m_staticTxtNum.SetLabel(("%d / %d" % (self.index+1, len(items))))
        if data.image_url == "":
            self.m_bmpImage.SetBitmap(wx.NullBitmap)
        else:
            img = wx.Image(data.image_url, wx.BITMAP_TYPE_ANY)
            img.Rescale(165, 165)
            self.m_bmpImage.SetBitmap(img.ConvertToBitmap())

        li_unit = CDataUnitInfo.GetData()
        unit_selection = 0
        for unit in li_unit:
            self.m_cbxUnit.Append(unit.name, unit)
            if unit.code == data.unit:
                self.m_cbxUnit.SetSelection(unit_selection)
            unit_selection += 1
            
        li_spec = CDataSpecInfo.GetData()
        spec_selection = 0
        for spec in li_spec:
            self.m_cbxSpec.Append(spec.name, spec)
            if spec.code == data.spec:
                self.m_cbxSpec.SetSelection(spec_selection)
            spec_selection += 1
        
        li_style = CDataStyleInfo.GetData()
        style_selection = 0
        for style in li_style:
            self.m_cbxStyle.Append(style.name, style)
            if style.code == data.style:
                self.m_cbxStyle.SetSelection(style_selection)
            style_selection += 1
            
        li_category = CDataCategoryInfo.GetData()
        category_selection = 0
        for category in li_category:
            self.m_cbxCategory.Append(category.name, category)
            if category.code == data.category:
                self.m_cbxCategory.SetSelection(category_selection)
            category_selection += 1
            
    # Virtual event handlers, overide them in your derived class
    def OnBtnPrev( self, event ):
        event.Skip()
        self.index -= 1
        self.InitModInfo()
    
    def OnBtnNext( self, event ):
        event.Skip()
        self.index += 1
        self.InitModInfo()
    
    def OnBtnSave( self, event ):
        event.Skip()
        unit = self.m_cbxUnit.GetClientData(self.m_cbxUnit.GetSelection())
        spec = self.m_cbxSpec.GetClientData(self.m_cbxSpec.GetSelection())
        style = self.m_cbxStyle.GetClientData(self.m_cbxStyle.GetSelection())
        category = self.m_cbxCategory.GetClientData(self.m_cbxCategory.GetSelection())
        data = CDataDishes(0, self.item_id, 
                          int(self.m_txtDishCode.GetValue()), 
                          self.m_txtDishName.GetValue(), 
                          self.m_txtBrevityCode.GetValue(),
                          spec.code, 
                          category.code, 
                          int(self.m_txtPrice.GetValue()), 
                          unit.code,
                          style.code,
                          float(self.m_txtCommition.GetValue()),
                          float(self.m_txtDiscount.GetValue()),
                          self.m_cbxStop.GetValue(),
                          self.image_url)
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
            self.m_bmpImage.SetBitmap(img.ConvertToBitmap())
    
    def OnBtnClean( self, event ):
        event.Skip()
        self.image_url = ""
        self.m_bmpImage.SetBitmap(wx.NullBitmap)
    
    def OnBtnNewSpec( self, event ):
        event.Skip()
        CDataSpecInfo.AddItem(CDataSpec(0, "", 0))
        
        data = CDataSpec(CDataSpecInfo.GetId(), "", 0)
        self.model_spec.data.append(data)
        item = self.model_spec.ObjectToItem(data)
        self.m_dataViewListSpec.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
    
    def OnBtnDelSpec( self, event ):
        event.Skip()
        item = self.m_dataViewListSpec.GetCurrentItem()
        data = self.model_spec.ItemToObject(item)
        self.model_spec.data.remove(data)
        self.m_dataViewListSpec.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
        CDataSpecInfo.DeleteItem(data)
        
    def OnBtnSaveSpec( self, event ):
        event.Skip()
        item = self.m_dataViewListSpec.GetCurrentItem()
        data = self.model_spec.ItemToObject(item)
        CDataSpecInfo.UpdateItem(data)
    
    def OnBtnNewStyle( self, event ):
        event.Skip()
        CDataStyleInfo.AddItem(CDataStyle(0, "", 0, "N"))
        
        data = CDataStyle(CDataStyleInfo.GetId(), "", 0, "N")
        self.model_style.data.append(data)
        item = self.model_style.ObjectToItem(data)
        self.m_dataViewListStyle.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
    
    def OnBtnDelStyle( self, event ):
        event.Skip()
        item = self.m_dataViewListStyle.GetCurrentItem()
        data = self.model_style.ItemToObject(item)
        self.model_style.data.remove(data)
        self.m_dataViewListStyle.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
        CDataStyleInfo.DeleteItem(data)
        
    def OnBtnSaveStyle( self, event ):
        event.Skip()
        item = self.m_dataViewListStyle.GetCurrentItem()
        data = self.model_style.ItemToObject(item)
        CDataStyleInfo.UpdateItem(data)
    
    def OnDishNameText( self, event ):
        event.Skip()
        brevity_code = CBrevityCode.MultiGetLetter(self.m_txtDishName.GetValue())
        print brevity_code
        self.m_txtBrevityCode.SetValue(brevity_code)
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    dlg = CPopDishesInfo(None, "mod")
    dlg.Show()
    app.MainLoop()

