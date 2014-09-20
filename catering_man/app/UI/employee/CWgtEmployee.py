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
## Class CEmployee
###########################################################################

class CWgtEmployee ( wx.Panel ):
    
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        m_sizer = wx.BoxSizer( wx.VERTICAL )
        
        m_topSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_btnNew = wx.Button( self, wx.ID_ANY, u"新增", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnNew.SetMinSize( wx.Size( 50,50 ) )
        
        m_topSizer.Add( self.m_btnNew, 0, 0, 5 )
        
        self.m_btnModify = wx.Button( self, wx.ID_ANY, u"修改", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnModify.SetMinSize( wx.Size( 50,50 ) )
        
        m_topSizer.Add( self.m_btnModify, 0, 0, 5 )
        
        self.m_btnDelete = wx.Button( self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnDelete.SetMinSize( wx.Size( 50,50 ) )
        
        m_topSizer.Add( self.m_btnDelete, 0, 0, 5 )
        
        self.m_btnDepartment = wx.Button( self, wx.ID_ANY, u"行政部门", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnDepartment.SetFont( wx.Font( 8, 70, 90, 90, False, wx.EmptyString ) )
        self.m_btnDepartment.SetMinSize( wx.Size( 50,50 ) )
        
        m_topSizer.Add( self.m_btnDepartment, 0, 0, 5 )
        
        self.m_btnRefresh = wx.Button( self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnRefresh.SetMinSize( wx.Size( 50,50 ) )
        
        m_topSizer.Add( self.m_btnRefresh, 0, 0, 5 )
        
        self.m_btnExit = wx.Button( self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnExit.SetMinSize( wx.Size( 50,50 ) )
        
        m_topSizer.Add( self.m_btnExit, 0, 0, 5 )
        
        self.m_topPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_topPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        m_topSizer.Add( self.m_topPanel, 1, wx.EXPAND, 5 )
        
        
        m_sizer.Add( m_topSizer, 1, wx.EXPAND, 5 )
        
        m_bottomSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        m_leftSizer = wx.BoxSizer( wx.VERTICAL )
        
        m_leftSizer.SetMinSize( wx.Size( 200,600 ) ) 
        self.m_treeCtrl = wx.TreeCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,600 ), wx.TR_DEFAULT_STYLE )
        m_leftSizer.Add( self.m_treeCtrl, 0, wx.EXPAND, 5 )
        
        
        m_bottomSizer.Add( m_leftSizer, 1, 0, 5 )
        
        m_rightSizer = wx.BoxSizer( wx.VERTICAL )
        
        m_rightSizer.SetMinSize( wx.Size( 600,600 ) ) 
        self.m_dataViewList = wx.dataview.DataViewCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_dataViewList.SetMinSize( wx.Size( -1,600 ) )
        
        # Create an instance of our model...
        self.model = CModelEmployee(CDataEmployeeInfo.GetData())
        CDataEmployeeInfo.RefreshItems()
        
        # Tel the DVC to use the model
        self.m_dataViewList.AssociateModel(self.model)
        
        self.m_dataViewColumn = self.m_dataViewList.AppendTextColumn( u"行号", 0 ) 
        self.m_dataViewCode = self.m_dataViewList.AppendTextColumn( u"工号", 1 ) 
        self.m_dataViewName = self.m_dataViewList.AppendTextColumn( u"姓名", 2 ) 
        self.m_dataViewDepartment = self.m_dataViewList.AppendTextColumn( u"行政部门", 3 ) 
        self.m_dataViewDuties = self.m_dataViewList.AppendTextColumn( u"职务", 4 ) 
        self.m_dataViewPhone = self.m_dataViewList.AppendTextColumn( u"电话", 5 ) 
        self.m_dataViewSex = self.m_dataViewList.AppendTextColumn( u"性别", 6 ) 
        self.m_dataViewBirthday = self.m_dataViewList.AppendTextColumn( u"生日", 7 ) 
        self.m_dataViewState = self.m_dataViewList.AppendTextColumn( u"状态", 8 ) 
        m_rightSizer.Add( self.m_dataViewList, 0, wx.EXPAND|wx.LEFT, 5 )
        
        
        m_bottomSizer.Add( m_rightSizer, 1, 0, 5 )
        
        
        m_sizer.Add( m_bottomSizer, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( m_sizer )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.Bind( wx.EVT_SIZE, self.OnSize )
        
        self.m_btnNew.Bind( wx.EVT_BUTTON, self.OnBtnNew )
        self.m_btnModify.Bind( wx.EVT_BUTTON, self.OnBtnModify )
        self.m_btnDelete.Bind( wx.EVT_BUTTON, self.OnBtnDelete )
        self.m_btnDepartment.Bind( wx.EVT_BUTTON, self.OnBtnDepartment )
        self.m_btnRefresh.Bind( wx.EVT_BUTTON, self.OnBtnRefresh )
        self.m_btnExit.Bind( wx.EVT_BUTTON, self.OnBtnExit )
        
        # Show tree ctrl
        self.ShowTreeCtrl()
    
    def __del__( self ):
        pass
    
    def Initailize(self):
        # Add event listenner
        CEvtManager.AddListenner(self, CEnumEvent.EVT_EMPLOYEE_REFRESH, self.OnBtnRefresh)
        
        x, y = CDataDeskTop.GetFrameSize()       
        self.SetSize(wx.Size(x, y))

    def Uninitailize(self):
        # Remove event listenner
        CEvtManager.RemoveListenner(self, CEnumEvent.EVT_EMPLOYEE_REFRESH, self.OnBtnRefresh)
    
    def ShowTreeCtrl(self):
        isz = (16,16)
        il = wx.ImageList(isz[0], isz[1])
        fldridx     = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER,      wx.ART_OTHER, isz))
        fldropenidx = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER_OPEN, wx.ART_OTHER, isz))
        fileidx     = il.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, isz))
        
        self.m_treeCtrl.SetImageList(il)
        self.il = il

        self.root = self.m_treeCtrl.AddRoot(u"全部行政部门")
        self.m_treeCtrl.SetPyData(self.root, None)
        self.m_treeCtrl.SetItemImage(self.root, fldridx, wx.TreeItemIcon_Normal)
        self.m_treeCtrl.SetItemImage(self.root, fldropenidx, wx.TreeItemIcon_Expanded)
        
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
                child = self.m_treeCtrl.AppendItem(self.root, title)
                self.m_treeCtrl.SetPyData(child, None)
                self.m_treeCtrl.SetItemImage(child, fldridx, wx.TreeItemIcon_Normal)
                self.m_treeCtrl.SetItemImage(child, fldropenidx, wx.TreeItemIcon_Expanded)
                for employee_info in department_map[dept.code]:
                    sub_clild = self.m_treeCtrl.AppendItem(child, employee_info.name)
                    self.m_treeCtrl.SetPyData(sub_clild, None)
                    self.m_treeCtrl.SetItemImage(sub_clild, fileidx, wx.TreeItemIcon_Normal)
                    self.m_treeCtrl.SetItemImage(sub_clild, fileidx, wx.TreeItemIcon_Selected)
            else:
                title = "%s(0)" % dept.name
                child = self.m_treeCtrl.AppendItem(self.root, title)
                self.m_treeCtrl.SetPyData(child, None)
                self.m_treeCtrl.SetItemImage(child, fldridx, wx.TreeItemIcon_Normal)
                self.m_treeCtrl.SetItemImage(child, fldropenidx, wx.TreeItemIcon_Expanded)
                
        self.m_treeCtrl.Expand(self.root)
        
    def RefreshUI(self):
        # Refresh treeCtrl
        CDataEmployeeInfo.RefreshItems()
        self.m_treeCtrl.DeleteAllItems()
        self.ShowTreeCtrl()
        
        # Refresh dataviewlist
        result = CDataEmployeeInfo.GetData()
        del self.model.data[0:len(self.model.data)]
        for new_obj in result:
            item = self.model.ObjectToItem(new_obj)
            self.model.data.append(new_obj)
            self.m_dataViewList.GetModel().ItemAdded(wx.dataview.NullDataViewItem, item)
                    
        self.model.Cleared()
    
    # Virtual event handlers, overide them in your derived class
    def OnSize( self, event ):
        event.Skip()
        x, y = self.GetSize()

        self.m_btnNew.SetMaxSize(wx.Size( 50,50 ))
        self.m_btnModify.SetMaxSize(wx.Size( 50,50 ))
        self.m_btnDelete.SetMaxSize(wx.Size( 50,50 ))
        self.m_btnDepartment.SetMaxSize(wx.Size( 50,50 ))
        self.m_btnRefresh.SetMaxSize(wx.Size( 50,50 ))
        self.m_btnExit.SetMaxSize(wx.Size( 50,50 ))
        self.m_topPanel.SetMaxSize( wx.Size( x-300,50 ) ) 
        self.m_treeCtrl.SetMinSize( wx.Size( 200,y-50 ) )
        self.m_dataViewList.SetMinSize( wx.Size( x-200,y-50 ) )
        
    def OnBtnNew( self, event ):
        event.Skip()
        self.popEmployee = CPopEmployee(self, "add")
        self.popEmployee.ShowModal()
    
    def OnBtnModify( self, event ):
        event.Skip()
        item = self.m_dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        index = self.model.data.index(data)
        CDataEmployeeInfo.SetCurItemIndex(index)
        self.popEmployee = CPopEmployee(self, "mod")
        self.popEmployee.ShowModal()
    
    def OnBtnDelete( self, event ):
        event.Skip()
        item = self.m_dataViewList.GetCurrentItem()
        data = self.model.ItemToObject(item)
        self.model.data.remove(data)
        self.m_dataViewList.GetModel().ItemDeleted(wx.dataview.NullDataViewItem, item)
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
