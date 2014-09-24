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
import wx.dataview
from app.CAppManager import CAppManager
from app.logic.desktop.CDataDeskTop import CDataDeskTop
from app.UI.employee.CPopDepartment import CPopDepartment
from app.logic.employee.CModelEmployee import CModelEmployee
from app.logic.employee.CDataEmployee import CDataEmployeeInfo, CDataEmployee
from app.UI.employee.CPopEmployee import CPopEmployee
from app.logic.employee.CDataDepartment import CDataDepartmentInfo
from framework.CEvtManager import CEvtManager
from app.logic.CEnumEvent import CEnumEvent

###########################################################################
## Class CWgtEmployee
###########################################################################

class CWgtEmployee (wx.Panel):
    def _init_status_bar_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add new button
        self.btnNew = wx.Button(self, wx.ID_ANY, u"新增", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnNew.SetMinSize(wx.Size(50,50 ))
        sizer.Add(self.btnNew, 0, 0, 5)
        # Add modify button
        self.btnModify = wx.Button(self, wx.ID_ANY, u"修改", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnModify.SetMinSize(wx.Size(50,50))
        sizer.Add(self.btnModify, 0, 0, 5)
        # Add delete button
        self.btnDelete = wx.Button(self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnDelete.SetMinSize(wx.Size(50,50))
        sizer.Add(self.btnDelete, 0, 0, 5)
        # Add department setting button
        self.btnDepartment = wx.Button(self, wx.ID_ANY, u"行政部门", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnDepartment.SetFont(wx.Font(8, 70, 90, 90, False, wx.EmptyString))
        self.btnDepartment.SetMinSize(wx.Size(50,50)) 
        sizer.Add(self.btnDepartment, 0, 0, 5)
        # Add refresh button
        self.btnRefresh = wx.Button(self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnRefresh.SetMinSize(wx.Size(50,50))
        sizer.Add(self.btnRefresh, 0, 0, 5)
        # Add exit button
        self.btnExit = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnExit.SetMinSize(wx.Size(50,50))
        sizer.Add(self.btnExit, 0, 0, 5)
        # Add fix space panel
        self.topPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.topPanel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE)) 
        sizer.Add(self.topPanel, 1, wx.EXPAND, 5)
        
        # Layout status bar 
        parent.Add(sizer, 1, wx.EXPAND, 5)

    def _init_view_sizer(self, parent):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # Add a tree control
        treeSizer = wx.BoxSizer(wx.VERTICAL)
        treeSizer.SetMinSize( wx.Size( 200,600 ) ) 
        self.treeCtrl = wx.TreeCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1,600), wx.TR_DEFAULT_STYLE)
        treeSizer.Add(self.treeCtrl, 0, wx.EXPAND, 5)
        sizer.Add(treeSizer, 1, 0, 5 )
        # Add data view list
        viewSizer = wx.BoxSizer(wx.VERTICAL)
        viewSizer.SetMinSize(wx.Size(600,600)) 
        self.dataViewList = wx.dataview.DataViewCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.dataViewList.SetMinSize(wx.Size(-1,600))
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
        viewSizer.Add(self.dataViewList, 0, wx.EXPAND|wx.LEFT, 5)
        sizer.Add(viewSizer, 1, 0, 5)

        # Layout 
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
        self.model = CModelEmployee(CDataEmployeeInfo.GetData())
        CDataEmployeeInfo.RefreshItems()
        
        # Tell the DVC to use the model
        self.dataViewList.AssociateModel(self.model)

        # Connect Events
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.btnNew.Bind(wx.EVT_BUTTON, self.OnBtnNew)
        self.btnModify.Bind(wx.EVT_BUTTON, self.OnBtnModify)
        self.btnDelete.Bind(wx.EVT_BUTTON, self.OnBtnDelete)
        self.btnDepartment.Bind(wx.EVT_BUTTON, self.OnBtnDepartment)
        self.btnRefresh.Bind(wx.EVT_BUTTON, self.OnBtnRefresh)
        self.btnExit.Bind(wx.EVT_BUTTON, self.OnBtnExit)
        
        # Show tree control
        self.ShowTreeCtrl()
    
    def __del__( self ):
        pass
    
    def Initailize(self):
        # Add event listener
        CEvtManager.AddListener(self, CEnumEvent.EVT_EMPLOYEE_REFRESH, self.OnBtnRefresh)
        
        x, y = CDataDeskTop.GetFrameSize()       
        self.SetSize(wx.Size(x, y))

    def Uninitailize(self):
        # Remove event listener
        CEvtManager.RemoveListener(self, CEnumEvent.EVT_EMPLOYEE_REFRESH, self.OnBtnRefresh)
    
    def ShowTreeCtrl(self):
        isz = (16,16)
        il = wx.ImageList(isz[0], isz[1])
        fldridx     = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER,      wx.ART_OTHER, isz))
        fldropenidx = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER_OPEN, wx.ART_OTHER, isz))
        fileidx     = il.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, isz))
        
        self.treeCtrl.SetImageList(il)
        self.il = il

        self.root = self.treeCtrl.AddRoot(u"全部行政部门")
        self.treeCtrl.SetPyData(self.root, None)
        self.treeCtrl.SetItemImage(self.root, fldridx, wx.TreeItemIcon_Normal)
        self.treeCtrl.SetItemImage(self.root, fldropenidx, wx.TreeItemIcon_Expanded)
        
        department_map = dict()
        li_items = CDataEmployeeInfo.GetItems()
        for item in li_items:
            if department_map.has_key(item.department):
                department_map[item.department].append(item)
            else:
                list_tmp = []
                list_tmp.append(item)
                department_map_tmp = {item.department:list_tmp}
                department_map.update(department_map_tmp)
        
        li_department = CDataDepartmentInfo.GetData()
        for dept in li_department:
            if department_map.has_key(dept.code):
                title = "%s(%d)" % (dept.name, len(department_map[dept.code]))
                child = self.treeCtrl.AppendItem(self.root, title)
                self.treeCtrl.SetPyData(child, None)
                self.treeCtrl.SetItemImage(child, fldridx, wx.TreeItemIcon_Normal)
                self.treeCtrl.SetItemImage(child, fldropenidx, wx.TreeItemIcon_Expanded)
                for employee_info in department_map[dept.code]:
                    sub_clild = self.treeCtrl.AppendItem(child, employee_info.name)
                    self.treeCtrl.SetPyData(sub_clild, None)
                    self.treeCtrl.SetItemImage(sub_clild, fileidx, wx.TreeItemIcon_Normal)
                    self.treeCtrl.SetItemImage(sub_clild, fileidx, wx.TreeItemIcon_Selected)
            else:
                title = "%s(0)" % dept.name
                child = self.treeCtrl.AppendItem(self.root, title)
                self.treeCtrl.SetPyData(child, None)
                self.treeCtrl.SetItemImage(child, fldridx, wx.TreeItemIcon_Normal)
                self.treeCtrl.SetItemImage(child, fldropenidx, wx.TreeItemIcon_Expanded)
                
        self.treeCtrl.Expand(self.root)
        
    def RefreshUI(self):
        # Refresh treeCtrl
        CDataEmployeeInfo.RefreshItems()
        self.treeCtrl.DeleteAllItems()
        self.ShowTreeCtrl()
        
        # Refresh data view list
        result = CDataEmployeeInfo.GetData()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
                    
        self.model.Cleared()
    
    # Virtual event handlers, override them in your derived class
    def OnSize( self, event ):
        event.Skip()
        x, y = self.GetSize()

        self.btnNew.SetMaxSize(wx.Size(50,50))
        self.btnModify.SetMaxSize(wx.Size(50,50))
        self.btnDelete.SetMaxSize(wx.Size(50,50))
        self.btnDepartment.SetMaxSize(wx.Size(50,50))
        self.btnRefresh.SetMaxSize(wx.Size(50,50))
        self.btnExit.SetMaxSize(wx.Size(50,50))
        self.topPanel.SetMaxSize(wx.Size(x-300,50)) 
        self.treeCtrl.SetMinSize(wx.Size(200,y-50))
        self.dataViewList.SetMinSize(wx.Size(x-200,y-50))
        
    def OnBtnNew( self, event ):
        event.Skip()
        self.popEmployee = CPopEmployee(self, "add")
        self.popEmployee.ShowModal()
    
    def OnBtnModify( self, event ):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        index = self.model.data.index(data)
        CDataEmployeeInfo.SetCurItemIndex(index)
        self.popEmployee = CPopEmployee(self, "mod")
        self.popEmployee.ShowModal()
    
    def OnBtnDelete( self, event ):
        event.Skip()
        item = self.dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        self.model.data.remove(data)
        self.dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
        CDataEmployeeInfo.DeleteItem(data)
    
    def OnBtnDepartment( self, event ):
        event.Skip()
        self.popDepartment = CPopDepartment(self)
        self.popDepartment.ShowModal()
    
    def OnBtnRefresh( self, event ):
        event.Skip()
        self.RefreshUI()
    
    def OnBtnExit( self, event ):
        event.Skip()
        CAppManager.SwitchToApplication('DeskTop')
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = CWgtEmployee(None)
    frame.Show(True)
    frame.Center()
    app.MainLoop()

