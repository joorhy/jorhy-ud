#!/usr/bin/env python
# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
from framework.core import BrevityCode
from app.home_logic import CtrlHomePage
from app.manager.logic.ctrl import * 
from app.manager.logic.model import *
from app.manager.logic.data import *
from app.app_manager import AppManager
from framework.core import TreeImage

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class PopCategorySetting
###########################################################################


class PopCategorySetting (wx.Dialog):
    def _init_view_sizer(self, parent):
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Create data view list
        self.dataViewList = wx.dataview.DataViewCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.dataViewList.SetMinSize(wx.Size(600, 300))
        # Add items into data view list
        self.dataViewList.AppendTextColumn(u"行号", 0) 
        self.dataViewList.AppendTextColumn(u"编码", 1, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE) 
        self.dataViewList.AppendTextColumn(u"菜品类名", 2, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE) 
        sizer.Add(self.dataViewList, 0, wx.ALL | wx.EXPAND, 5)
        
        # Layout data view list
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
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"菜品类别设置", pos=wx.DefaultPosition,
                           size=wx.Size(600, 400), style=wx.CAPTION | wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.Size(-1, -1), wx.Size(-1, -1))
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        self._init_view_sizer(sizer)
        self._init_ctrl_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)
        
        # Create an instance of our model...
        self.model = ModelCategory(CtrlCategory.get_data())
        
        # Tell the DVC to use the model
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
        CtrlCategory.add_item(DataCategory())
        
        data = DataCategory(CtrlCategory.get_data_len() + 1, CtrlCategory.get_id())
        self.model.data.append(data)
        item = self.model.ObjectToItem(data)
        self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
    
    def on_btn_delete(self, event):
        event.Skip()
        try:
            item = self.dataViewList.GetCurrentItem()
            data = self.model.ItemToObject(item)
            self.model.data.remove(data)
            self.dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
            CtrlCategory.delete_item(data)
        except:
            print 'PopCategorySetting on_btn_delete error'
    
    def on_btn_refresh(self, event):
        event.Skip()
        
        result = CtrlCategory.get_data()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
                    
        self.model.Cleared()
    
    def on_btn_save(self, event):
        event.Skip()
        for data in self.model.data:
            CtrlCategory.update_item(data)
    
    def on_btn_exit(self, event):
        event.Skip()
        self.Close()

###########################################################################
## Class PopDishesInfo
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
        sizer.Add(self.txtTrack, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add previous record button
        self.btnPrev = wx.Button(self, wx.ID_ANY, u"上一记录", wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(self.btnPrev, 0, wx.ALIGN_CENTER | wx.ALL, 5)
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
        sizer.Add(self.btnExit, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Layout status bar
        parent.Add(sizer, 1, wx.EXPAND, 5)
        
    def _init_view_sizer(self, parent):
        fg_sizer = wx.FlexGridSizer(0, 2, 0, 0)
        fg_sizer.SetFlexibleDirection(wx.BOTH)
        fg_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        
        self._init_data_view_sizer(fg_sizer)
        self._init_image_view_sizer(fg_sizer)
        
        # Layout data view
        parent.Add(fg_sizer, 1, wx.EXPAND, 5)
        
    def _init_data_view_sizer(self, parent):
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Add data view panel
        panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(500, 200), wx.STATIC_BORDER | wx.TAB_TRAVERSAL)
        panel.SetMaxSize(wx.Size(-1, 200))
        
        # Add data view panel sizer
        panel_sizer = wx.BoxSizer(wx.HORIZONTAL)
        panel_sizer.SetMinSize(wx.Size(500, 200))

        self._init_data_view_left_column_sizer(panel, panel_sizer)
        self._init_data_view_right_column_sizer(panel, panel_sizer)
        
        panel.SetSizer(panel_sizer)
        panel.Layout()
        sizer.Add(panel, 1, wx.EXPAND | wx.ALL, 5)
        
        # Layout data view sizer
        parent.Add(sizer, 1, wx.EXPAND, 5)        
        
    def _init_data_view_left_column_sizer(self, container, parent):
        # Add grid sizer with 6 rows and 2 columns
        g_sizer = wx.GridSizer(6, 2, 0, 0)
        # Add label for dishes code
        s_txt_code = wx.StaticText(container, wx.ID_ANY, u"品码：", wx.DefaultPosition, wx.DefaultSize, 0)
        s_txt_code.Wrap(-1)
        g_sizer.Add(s_txt_code, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add text control for dishes code
        self.txtDishCode = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        g_sizer.Add(self.txtDishCode, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add label for dishes unit
        s_txt_unit = wx.StaticText(container, wx.ID_ANY, u"单位：", wx.DefaultPosition, wx.DefaultSize, 0)
        s_txt_unit.Wrap(-1)
        g_sizer.Add(s_txt_unit, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add combo box for dishes unit
        cbx_unit_choices = list()
        self.cbxUnit = wx.ComboBox(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.Size(110, -1), cbx_unit_choices, 0)
        g_sizer.Add(self.cbxUnit, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add label for dishes discount
        s_txt_discount = wx.StaticText(container, wx.ID_ANY, u"折扣比率：", wx.DefaultPosition, wx.DefaultSize, 0)
        s_txt_discount.Wrap(-1)
        g_sizer.Add(s_txt_discount, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add text control for dishes discount
        self.txtDiscount = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        g_sizer.Add(self.txtDiscount, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add label for dishes commission
        s_txt_commission = wx.StaticText(container, wx.ID_ANY, u"提成比率：", wx.DefaultPosition, wx.DefaultSize, 0)
        s_txt_commission.Wrap(-1)
        g_sizer.Add(s_txt_commission, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add label for dishes commission
        self.txtCommission = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        g_sizer.Add(self.txtCommission, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Layout 
        parent.Add(g_sizer, 1, wx.EXPAND, 5)
        
    def _init_data_view_right_column_sizer(self, container, parent):
        # Add grid sizer with 6 rows and 2 columns
        g_sizer = wx.GridSizer(6, 2, 0, 0)
        # Add label for dishes name
        s_txt_name = wx.StaticText(container, wx.ID_ANY, u"菜品名称：", wx.DefaultPosition, wx.DefaultSize, 0)
        s_txt_name.Wrap(-1)
        g_sizer.Add(s_txt_name, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add text control for dishes name
        self.txtDishName = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        g_sizer.Add(self.txtDishName, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add label for dishes brevity code
        s_txt_brevity_code = wx.StaticText(container, wx.ID_ANY, u"拼音简码：", wx.DefaultPosition, wx.DefaultSize, 0)
        s_txt_brevity_code.Wrap(-1)
        g_sizer.Add(s_txt_brevity_code, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add text control for dishes brevity code
        self.txtBrevityCode = wx.TextCtrl(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.DefaultSize, wx.TE_READONLY)
        g_sizer.Add(self.txtBrevityCode, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add label for dishes type
        s_txt_type = wx.StaticText(container, wx.ID_ANY, u"所属类别：", wx.DefaultPosition, wx.DefaultSize, 0)
        s_txt_type.Wrap(-1)
        g_sizer.Add(s_txt_type, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add combo box for dishes type
        cbx_category_choices = list()
        self.cbxCategory = wx.ComboBox(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.Size(110,  -1), cbx_category_choices, 0)
        g_sizer.Add(self.cbxCategory, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add label for dishes status
        s_txt_status = wx.StaticText(container, wx.ID_ANY, u"停用：", wx.DefaultPosition, wx.DefaultSize, 0)
        s_txt_status.Wrap(-1)
        g_sizer.Add(s_txt_status, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add check box for dishes state
        self.cbxStop = wx.CheckBox(container, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        g_sizer.Add(self.cbxStop, 0, wx.ALIGN_CENTER, 5)
        # Layout 
        parent.Add(g_sizer, 1, wx.EXPAND, 5)
        
    def _init_image_view_sizer(self, parent):
        fg_sizer = wx.FlexGridSizer(2, 1, 0, 0)
        fg_sizer.SetFlexibleDirection(wx.BOTH)
        fg_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        
        # Create image sizer contain a static bitmap 
        image_sizer = wx.BoxSizer(wx.VERTICAL)
        self.bmpImage = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                        wx.Size(165, 165), wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL)
        image_sizer.Add(self.bmpImage, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        fg_sizer.Add(image_sizer, 1, wx.EXPAND, 5)

        # Create control sizer contain tow button
        ctrl_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add import button
        self.btnImport = wx.Button(self, wx.ID_ANY, u"图片导入", wx.DefaultPosition, wx.Size(80, 30), 0 | wx.TAB_TRAVERSAL)
        ctrl_sizer.Add(self.btnImport, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        # Add clean button
        self.btnClean = wx.Button(self, wx.ID_ANY, u"图片清除", wx.DefaultPosition, wx.DefaultSize, 0 | wx.TAB_TRAVERSAL)
        ctrl_sizer.Add(self.btnClean, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        fg_sizer.Add(ctrl_sizer, 1, wx.EXPAND, 5)

        # Layout image data view
        parent.Add(fg_sizer, 1, wx.EXPAND, 5)
        
    def _init_expand_sizer(self, parent):
        sb_sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"规格和做法设置"), wx.HORIZONTAL)
        
        self._init_spec_sizer(sb_sizer)
        self._init_style_sizer(sb_sizer)
        
        # Layout
        parent.Add(sb_sizer, 1, wx.EXPAND, 5)
    
    def _init_spec_sizer(self, parent):
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        view_sizer = wx.BoxSizer(wx.VERTICAL)
        # Create specification data view list 
        self.dataViewListSpec = wx.dataview.DataViewCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 140), 0)
        # Add items into specification data view list
        self.dataViewListSpec.AppendTextColumn(u"编码", 0)
        self.dataViewListSpec.AppendTextColumn(u"规格", 1, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE) 
        self.dataViewListSpec.AppendTextColumn(u"价格", 2, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE) 
        view_sizer.Add(self.dataViewListSpec, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(view_sizer, 1, wx.EXPAND, 5)
        
        ctrl_sizer = wx.BoxSizer(wx.HORIZONTAL)
        ctrl_sizer.SetMinSize(wx.Size(-1, 200))
        # Add Spacer
        ctrl_sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        # Add new button
        self.btnNewSpec = wx.Button(self, wx.ID_ANY, u"新增规格", wx.DefaultPosition, wx.DefaultSize, 0)
        ctrl_sizer.Add(self.btnNewSpec, 0, wx.ALL, 5)
        # Add delete button
        self.btnDelSpec = wx.Button(self, wx.ID_ANY, u"删除规格", wx.DefaultPosition, wx.DefaultSize, 0)
        ctrl_sizer.Add(self.btnDelSpec, 0, wx.ALL, 5)
        sizer.Add(ctrl_sizer, 1, wx.EXPAND, 5)

        # Layout specification sizer
        parent.Add(sizer, 1, wx.EXPAND, 5)
        
    def _init_style_sizer(self, parent):
        sizer = wx.BoxSizer(wx.VERTICAL)

        view_sizer = wx.BoxSizer(wx.VERTICAL)
        # Create style data view list 
        self.dataViewListStyle = wx.dataview.DataViewCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 140), 0)
        # Add items into style data view list
        self.dataViewListStyle.AppendTextColumn(u"编码", 0)
        self.dataViewListStyle.AppendTextColumn(u"做法说明", 1, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE) 
        self.dataViewListStyle.AppendTextColumn(u"加价金额", 2, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE) 
        self.dataViewListStyle.AppendTextColumn(u"按量加价", 3, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE) 
        view_sizer.Add(self.dataViewListStyle, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(view_sizer, 1, wx.EXPAND, 5)
        
        ctrl_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add Spacer
        ctrl_sizer.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        # Add new button
        self.btnNewStyle = wx.Button(self, wx.ID_ANY, u"新增做法", wx.DefaultPosition, wx.DefaultSize, 0)
        ctrl_sizer.Add(self.btnNewStyle, 0, wx.ALL, 5)
        # Add delete button
        self.btnDelStyle = wx.Button(self, wx.ID_ANY, u"删除做法", wx.DefaultPosition, wx.DefaultSize, 0)
        ctrl_sizer.Add(self.btnDelStyle, 0, wx.ALL, 5)
        sizer.Add(ctrl_sizer, 1, wx.EXPAND, 5)
        
        # Layout style sizer
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def __init__(self, parent, type_="add"):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"菜品资料维护", pos=wx.DefaultPosition,
                           size=wx.Size(700, 500), style=wx.CAPTION)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        fg_sizer = wx.FlexGridSizer(3, 1, 0, 0)
        fg_sizer.SetFlexibleDirection(wx.BOTH)
        fg_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self._init_status_bar_sizer(fg_sizer)
        self._init_view_sizer(fg_sizer)
        self._init_expand_sizer(fg_sizer)
        
        self.SetSizer(fg_sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Connect Events
        self.btnPrev.Bind(wx.EVT_BUTTON, self.on_btn_prev)
        self.btnNext.Bind(wx.EVT_BUTTON, self.on_btn_next)
        self.btnSave.Bind(wx.EVT_BUTTON, self.on_btn_save)
        self.btnExit.Bind(wx.EVT_BUTTON, self.on_btn_exit)
        self.btnImport.Bind(wx.EVT_BUTTON, self.on_btn_import)
        self.btnClean.Bind(wx.EVT_BUTTON, self.on_btn_clean)
        
        self.btnNewSpec.Bind(wx.EVT_BUTTON, self.on_btn_new_spec)
        self.btnDelSpec.Bind(wx.EVT_BUTTON, self.on_btn_delete_spec)
        
        self.btnNewStyle.Bind(wx.EVT_BUTTON, self.on_btn_new_style)
        self.btnDelStyle.Bind(wx.EVT_BUTTON, self.on_btn_delete_style)

        self.txtDishName.Bind(wx.EVT_TEXT, self.on_dish_name_text)

        # Initialize data view 
        self.index = 0
        self.type = type_
        self.image_url = ""
        self.item_id = 0
        self._initialize_view()

    def __del__(self):
        pass

    def _initialize_view(self):
        if self.type == "add":
            self._init_add_view()
        elif self.type == "mod":
            self.index = CtrlDishes.get_cur_item_index()
            self._init_mod_view()

    def _init_add_view(self):
        # Create an instance of our specification model...
        self.model_spec = ModelSpec(list())

        # Tell the DVC to use the specification model
        self.dataViewListSpec.AssociateModel(self.model_spec)

        # Create an instance of our style model...
        self.model_style = ModelStyle(list())

        # Tell the DVC to use the style model
        self.dataViewListStyle.AssociateModel(self.model_style)

        li_unit = CtrlUnit.get_data()
        for unit in li_unit:
            self.cbxUnit.Append(unit.name, unit)
        self.cbxUnit.SetSelection(0)

        li_category = CtrlCategory.get_data()
        for category in li_category:
            self.cbxCategory.Append(category.name, category)
        self.cbxCategory.SetSelection(0)

        self.txtTrack.Enable(False)
        self.btnPrev.Enable(False)
        self.btnNext.Enable(False)

    def _init_mod_view(self):
        if self.index < 0:
            self.index = 0
            return

        items = CtrlDishes.get_items()
        if self.index >= len(items):
            self.index = len(items) - 1
            return

        data = items[self.index]

        # Create an instance of our specification model...
        self.model_spec = ModelSpec(CtrlSpec.get_data_by_dish_code(data.code))

        # Tell the DVC to use the specification model
        self.dataViewListSpec.AssociateModel(self.model_spec)

        # Create an instance of our style model...
        self.model_style = ModelStyle(CtrlStyle.get_data_by_dish_code(data.code))

        # Tell the DVC to use the style model
        self.dataViewListStyle.AssociateModel(self.model_style)

        self.item_id = data.key
        self.txtDishCode.SetValue(data.code)
        self.txtDishName.SetValue(data.name)
        self.txtBrevityCode.SetValue(str(data.spell))
        self.txtCommission.SetValue(str(data.commission))
        self.txtDiscount.SetValue(str(data.discount))
        self.cbxStop.SetValue(True if data.stop == u'1' else False)
        self.txtTrack.SetLabel(("%d / %d" % (self.index+1, len(items))))
        if data.image_url == "":
            self.bmpImage.SetBitmap(wx.NullBitmap)
        else:
            img = wx.Image(data.image_url, wx.BITMAP_TYPE_ANY)
            img.Rescale(165, 165)
            self.bmpImage.SetBitmap(img.ConvertToBitmap())

        li_unit = CtrlUnit.get_data()
        for unit in li_unit:
            self.cbxUnit.Append(unit.name, unit)
            if unit.key == data.unit:
                self.cbxUnit.SetSelection(li_unit.index(unit))

        li_category = CtrlCategory.get_data()
        for category in li_category:
            self.cbxCategory.Append(category.name, category)
            if category.key == data.category:
                self.cbxCategory.SetSelection(li_category.index(category))

    # Virtual event handlers, override them in your derived class
    def on_btn_prev(self, event):
        event.Skip()
        self.index -= 1
        self._init_mod_view()

    def on_btn_next(self, event):
        event.Skip()
        self.index += 1
        self._init_mod_view()

    def on_btn_save(self, event):
        event.Skip()
        unit = self.cbxUnit.GetClientData(self.cbxUnit.GetSelection())
        category = self.cbxCategory.GetClientData(self.cbxCategory.GetSelection())
        data = DataDishes(0, self.item_id, 
                          self.txtDishCode.GetValue(),
                          self.txtDishName.GetValue(),
                          self.txtBrevityCode.GetValue(),
                          category.key,
                          unit.key,
                          float(self.txtCommission.GetValue()) if self.txtCommission.GetValue() != '' else 0,
                          float(self.txtDiscount.GetValue()) if self.txtDiscount.GetValue() != '' else 0,
                          self.cbxStop.GetValue(),
                          self.image_url, "")
        if self.type == "add":
            CtrlDishes.add_item(data)
            for spec_data in self.model_spec.data:
                data = DataSpec(dish_code=self.txtDishCode.GetValue(), name=spec_data.name, price=spec_data.price)
                CtrlSpec.add_item(data)

            for style_data in self.model_style.data:
                data = DataStyle(dish_code=self.txtDishCode.GetValue(), name=style_data.name,
                                 price_add=style_data.price_add, amount_add=style_data.amount_add)
                CtrlStyle.add_item(data)
        elif self.type == "mod":
            CtrlDishes.update_item(data)

            for spec_data in self.model_spec.data:
                data = DataSpec(dish_code=self.txtDishCode.GetValue(), name=spec_data.name, price=spec_data.price)
                CtrlSpec.update_item(data)

            for style_data in self.model_style.data:
                data = DataStyle(dish_code=self.txtDishCode.GetValue(), name=style_data.name,
                                 price_add=style_data.price_add, amount_add=style_data.amount_add)
                CtrlStyle.update_item(data)

    def on_btn_exit(self, event):
        event.Skip()
        self.Close()

    def on_btn_import(self, event):
        event.Skip()
        dlg = wx.FileDialog(
            self, message=u"选择图片",
            defaultDir="E:",    # os.getcwd()
            defaultFile="",
            wildcard=wildcard,
            style=wx.OPEN | wx.CHANGE_DIR)

        # Show the dialog and retrieve the user response. If it is the OK response, 
        # process the data.
        if dlg.ShowModal() == wx.ID_OK:
            # This returns a Python list of files that were selected.
            paths = dlg.GetPath()
            self.image_url = paths

            img = wx.Image(self.image_url, wx.BITMAP_TYPE_ANY)
            img.Rescale(165, 165)
            self.bmpImage.SetBitmap(img.ConvertToBitmap())

    def on_btn_clean(self, event):
        event.Skip()
        self.image_url = ""
        self.bmpImage.SetBitmap(wx.NullBitmap)

    def on_btn_new_spec(self, event):
        event.Skip()

        data = DataSpec()
        self.model_spec.data.append(data)
        item = self.model_spec.ObjectToItem(data)
        self.dataViewListSpec.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)

    def on_btn_delete_spec(self, event):
        event.Skip()
        try:
            item = self.dataViewListSpec.GetCurrentItem()
            data = self.model_spec.ItemToObject(item)
            self.model_spec.data.remove(data)
            self.dataViewListSpec.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
            CtrlSpec.delete_item(data)
        except:
            print 'PopDishesInfo on_btn_delete_spec error'

    def on_btn_new_style(self, event):
        event.Skip()

        data = DataStyle()
        self.model_style.data.append(data)
        item = self.model_style.ObjectToItem(data)
        self.dataViewListStyle.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)

    def on_btn_delete_style(self, event):
        event.Skip()
        try:
            item = self.dataViewListStyle.GetCurrentItem()
            data = self.model_style.ItemToObject(item)
            self.model_style.data.remove(data)
            self.dataViewListStyle.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
            CtrlStyle.delete_item(data)
        except:
            print 'PopDishesInfo on_btn_delete_style error'

    def on_dish_name_text(self, event):
        event.Skip()
        brevity_code = BrevityCode.multi_get_letter(self.txtDishName.GetValue())
        print brevity_code
        self.txtBrevityCode.SetValue(brevity_code)

###########################################################################
## Class PopUnitSetting
###########################################################################


class PopUnitSetting (wx.Dialog):
    def _init_view_sizer(self, parent):
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Create data view list
        self.dataViewList = wx.dataview.DataViewCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.dataViewList.SetMinSize(wx.Size(600, 300))
        # Add items into data view list
        self.dataViewList.AppendTextColumn(u"行号", 0) 
        self.dataViewList.AppendTextColumn(u"编码", 1, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE) 
        self.dataViewList.AppendTextColumn(u"菜品单位", 2, width=-1, mode=wx.dataview.DATAVIEW_CELL_EDITABLE) 
        sizer.Add(self.dataViewList, 0, wx.ALL | wx.EXPAND, 5)
        # Layout data view 
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
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"菜品单位设置", pos=wx.DefaultPosition,
                           size=wx.Size(600, 400), style=wx.CAPTION | wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.Size(-1, -1), wx.Size(-1, -1))
        
        sizer = wx.BoxSizer(wx.VERTICAL) 
        self._init_view_sizer(sizer)
        self._init_ctrl_sizer(sizer)

        self.SetSizer(sizer)
        self.Layout() 
        self.Centre(wx.BOTH)

        # Create an instance of our model...
        self.model = ModelUnit(CtrlUnit.get_data())
        
        # Tell the DVC to use the model
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
        CtrlUnit.add_item(DataUnit())

        data = DataUnit(CtrlUnit.get_data_len() + 1, CtrlUnit.get_id())
        self.model.data.append(data)
        item = self.model.ObjectToItem(data)
        self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
    
    def on_btn_delete(self, event):
        event.Skip()
        try:
            item = self.dataViewList.GetCurrentItem()
            data = self.model.ItemToObject(item)
            self.model.data.remove(data)
            self.dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
            CtrlUnit.delete_item(data)
        except:
            print 'PopUnitSetting on_btn_delete error'
    
    def on_btn_refresh(self, event):
        event.Skip()
        result = CtrlUnit.get_data()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
                    
        self.model.Cleared()
    
    def on_btn_save(self, event):
        event.Skip()
        for data in self.model.data:
            CtrlUnit.update_item(data)
    
    def on_btn_exit(self, event):
        event.Skip()
        self.Close()

###########################################################################
## Class WgtDishesPublish
###########################################################################


class WgtDishesPublish (wx.Panel):
    def _init_status_bar_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.SetMinSize(wx.Size(-1, 50))

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
        # Add dishes type button
        self.btnType = wx.Button(self, wx.ID_ANY, u"类型", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnType.SetMinSize(wx.Size(50, 50))
        sizer.Add(self.btnType, 0, 0, 5)
        # Add dishes unit button
        self.btnUnit = wx.Button(self, wx.ID_ANY, u"单位", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnUnit.SetMinSize(wx.Size(50, 50))
        sizer.Add(self.btnUnit, 0, 0, 5)
        # Add refresh button
        self.btnRefresh = wx.Button(self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnRefresh.SetMinSize(wx.Size(50, 50))
        sizer.Add(self.btnRefresh, 0, 0, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnExit.SetMinSize(wx.Size(50, 50))
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
        left_sizer = wx.BoxSizer(wx.VERTICAL)
        left_sizer.SetMinSize(wx.Size(200, 600))
        # Create a tree control
        self.treeCtrl = wx.TreeCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE)
        self.treeCtrl.SetMinSize(wx.Size(-1, 600))
        left_sizer.Add(self.treeCtrl, 0, wx.EXPAND, 5)
        # Layout tree control
        sizer.Add(left_sizer, 1, 0, 5)
        
        # This sizer for data view list
        right_sizer = wx.BoxSizer(wx.VERTICAL)
        right_sizer.SetMinSize(wx.Size(600, 600))
        # Create a data view list
        self.dataViewList = wx.dataview.DataViewCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 600), 0)
        # Add items into data view list
        self.dataViewList.AppendTextColumn(u"行号", 0) 
        self.dataViewList.AppendTextColumn(u"品码", 1) 
        self.dataViewList.AppendTextColumn(u"品名", 2) 
        self.dataViewList.AppendTextColumn(u"拼音简码", 3)
        self.dataViewList.AppendTextColumn(u"所属类", 4)
        self.dataViewList.AppendTextColumn(u"单位", 5)
        self.dataViewList.AppendToggleColumn(u"停用", 6, width=80)
        right_sizer.Add(self.dataViewList, 0, wx.EXPAND | wx.LEFT, 5)
        # Layout data view list
        sizer.Add(right_sizer, 1, 0, 5)
        
        # Layout view sizer
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
        self.model = ModelDishes(CtrlDishes.get_data())
        CtrlDishes.refresh_items()
        
        # Tel the DVC to use the model
        self.dataViewList.AssociateModel(self.model)

        # Connect Events
        self.Bind(wx.EVT_SIZE, self.on_size)
        
        self.btnNew.Bind(wx.EVT_BUTTON, self.on_btn_new)
        self.btnModify.Bind(wx.EVT_BUTTON, self.on_btn_modify)
        self.btnDelete.Bind(wx.EVT_BUTTON, self.on_btn_delete)
        self.btnType.Bind(wx.EVT_BUTTON, self.on_btn_type)
        self.btnUnit.Bind(wx.EVT_BUTTON, self.on_btn_unit)
        self.btnRefresh.Bind(wx.EVT_BUTTON, self.on_btn_refresh)
        self.btnExit.Bind(wx.EVT_BUTTON, self.on_btn_exit)

        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.on_sel_changed, self.treeCtrl)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.on_activate, self.treeCtrl)
        
        # Show tree control
        self.tree_data = None
        self._show_tree_ctrl()
    
    def __del__(self):
        pass
    
    def initialize(self):
        # Add event listener
        EvtManager.add_listener(self, EnumEvent.EVT_DISHES_PUBLISH_REFRESH, self.on_btn_refresh)
        
        x, y = CtrlHomePage.get_screen_size()
        self.SetSize(wx.Size(x, y))

    def un_initialize(self):
        # Remove event listener
        EvtManager.remove_listener(self, EnumEvent.EVT_DISHES_PUBLISH_REFRESH, self.on_btn_refresh)
    
    def _show_tree_ctrl(self):
        tree_image = TreeImage()
        self.treeCtrl.SetImageList(tree_image.image_list)
        self.il = tree_image.image_list

        self.root = self.treeCtrl.AddRoot(u"全部菜品")
        self.treeCtrl.SetPyData(self.root, None)
        self.treeCtrl.SetItemImage(self.root, tree_image.folder_idx, wx.TreeItemIcon_Normal)
        self.treeCtrl.SetItemImage(self.root, tree_image.folder_open_idx, wx.TreeItemIcon_Expanded)
        
        dishes_map = dict()
        li_items = CtrlDishes.get_items()
        for item in li_items:
            if item.category in dishes_map:
                dishes_map[item.category].append(item)
            else:
                list_tmp = list()
                list_tmp.append(item)
                dishes_map_tmp = {item.category: list_tmp}
                dishes_map.update(dishes_map_tmp)
        
        li_category = CtrlCategory.get_data()
        for category in li_category:
            if category.key in dishes_map:
                title = "%s(%d)" % (category.name, len(dishes_map[category.key]))
                child = self.treeCtrl.AppendItem(self.root, title)
                self.treeCtrl.SetPyData(child, category)
                self.treeCtrl.SetItemImage(child, tree_image.folder_idx, wx.TreeItemIcon_Normal)
                self.treeCtrl.SetItemImage(child, tree_image.folder_open_idx, wx.TreeItemIcon_Expanded)
                for dishes in dishes_map[category.key]:
                    sub_child = self.treeCtrl.AppendItem(child, dishes.name)
                    self.treeCtrl.SetPyData(sub_child, dishes)
                    self.treeCtrl.SetItemImage(sub_child, tree_image.file_idx, wx.TreeItemIcon_Normal)
                    self.treeCtrl.SetItemImage(sub_child, tree_image.file_idx, wx.TreeItemIcon_Selected)
            else:
                title = "%s(0)" % category.name
                child = self.treeCtrl.AppendItem(self.root, title)
                self.treeCtrl.SetPyData(child, None)
                self.treeCtrl.SetItemImage(child, tree_image.folder_idx, wx.TreeItemIcon_Normal)
                self.treeCtrl.SetItemImage(child, tree_image.folder_open_idx, wx.TreeItemIcon_Expanded)
                
        self.treeCtrl.Expand(self.root)
    
    def _refresh_ui(self):
        # Refresh treeCtrl
        CtrlDishes.refresh_items()
        self.treeCtrl.DeleteAllItems()
        self._show_tree_ctrl()
        
        # Refresh data view list
        result = CtrlDishes.get_data()
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
        self.btnType.SetMaxSize(wx.Size(50, 50))
        self.btnUnit.SetMaxSize(wx.Size(50, 50))
        self.btnRefresh.SetMaxSize(wx.Size(50, 50))
        self.btnExit.SetMaxSize(wx.Size(50, 50))
        self.topPanel.SetMaxSize(wx.Size(x-350, 50))
        self.treeCtrl.SetMinSize(wx.Size(200, y-50))
        self.dataViewList.SetMinSize(wx.Size(x-200, y-50))
        
    def on_btn_new(self, event):
        event.Skip()
        pop_dishes_info = PopDishesInfo(self, "add")
        pop_dishes_info.ShowModal()
    
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
            CtrlDishes.set_cur_item_index(index_)
            pop_dishes_info = PopDishesInfo(self, "mod")
            pop_dishes_info.ShowModal()
        except:
            print 'WgtDishesPublish: on_btn_modify error'
    
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
            CtrlDishes.delete_item(data)
            CtrlSpec.delete_item_by_dish_code(data.code)
            CtrlStyle.delete_item_by_dish_code(data.code)
        except:
            print 'WgtDishesPublish: on_btn_delete error'
    
    def on_btn_type(self, event):
        event.Skip()
        pop_category = PopCategorySetting(self)
        pop_category.ShowModal()
    
    def on_btn_unit(self, event):
        event.Skip()
        pop_unit = PopUnitSetting(self)
        pop_unit.ShowModal()
    
    def on_btn_refresh(self, event):
        event.Skip()
        self._refresh_ui()
    
    def on_btn_exit(self, event):
        event.Skip()
        self.Hide()
        CtrlHomePage.set_selected_item()
        AppManager.switch_to_application('HomePage')

    def on_sel_changed(self, event):
        event.Skip()
        self.tree_data = self.treeCtrl.GetPyData(event.GetItem())

    def on_activate(self, event):
        event.Skip()
        self.tree_data = self.treeCtrl.GetPyData(event.GetItem())
        if isinstance(self.tree_data, DataDishes):
            self.on_btn_modify(event)
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = WgtDishesPublish(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()
