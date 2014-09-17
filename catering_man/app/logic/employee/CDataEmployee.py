#!/usr/bin/env python
# -*- coding: utf-8 -*-
from framework.CSingleton import CSingleton
from service.logic.CSvcEmployee import CSvcEmployee
from framework.CEvtManager import CEvtManager
from app.logic.CEnumEvent import CEnumEvent

class CDataEmployee(object):
    def __init__(self, id_, code, name, table_type, area, peple_num, min_type):
        self.id = id_
        self.code = code
        self.name = name
        self.table_type = table_type
        self.area = area
        self.peple_num = peple_num
        self.min_type = min_type
        
class CDataEmployeeInfo(CSingleton):
    cur_item_index = 0
    table_items = list()
    
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @staticmethod
    def GetCurItemIndex():
        return CDataEmployeeInfo.cur_item_index
    
    @staticmethod
    def SetCurItemIndex(index):
        CDataEmployeeInfo.cur_item_index = index
    
    @staticmethod
    def GetData():
        result = CSvcEmployee.GetAll()
        data = list()
        for item in result:
            data_item = CDataEmployee(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            data.append(data_item)
            
        #CDataTypeInfo.data_len = len(data)
            
        return data
    
    @staticmethod
    def RefreshItems():
        del CDataEmployeeInfo.table_items[0:len(CDataEmployeeInfo.table_items)]
        result = CSvcEmployee.GetItems()
        for item in result:
            data_item = CDataEmployee(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            CDataEmployeeInfo.table_items.append(data_item)
            
    @staticmethod
    def GetItems():            
        return CDataEmployeeInfo.table_items
    
    @staticmethod
    def AddItem(data):
        if isinstance(data, CDataEmployee):
            item = [data.code, data.name, data.table_type, data.area, data.peple_num, data.min_type]
            CSvcEmployee.AddItem(item)
            CEvtManager.DispatchEvent(CEnumEvent.EVT_DINING_ROOM_REFRESH)
    
    @staticmethod      
    def AddItems(data):
        for obj in data:
            if isinstance(obj, CDataEmployee):
                item = [obj.code, obj.name, obj.table_type, obj.area, obj.peple_num, obj.min_type]
                CSvcEmployee.AddItem(item)
        CEvtManager.DispatchEvent(CEnumEvent.EVT_DINING_ROOM_REFRESH)         
            
    @staticmethod
    def DeleteItem(data):
        if isinstance(data, CDataEmployee):
            item = [data.code, data.name, data.table_type, data.area, data.peple_num, data.min_type]
            CSvcEmployee.DeleteItem(item)
            CEvtManager.DispatchEvent(CEnumEvent.EVT_DINING_ROOM_REFRESH)
            
    @staticmethod
    def UpdateItem(data):
        if isinstance(data, CDataEmployee):
            item = [data.code, data.name, data.table_type, data.area, data.peple_num, data.min_type]
            CSvcEmployee.UpdateItem(item)
            CEvtManager.DispatchEvent(CEnumEvent.EVT_DINING_ROOM_REFRESH)