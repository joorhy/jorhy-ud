#!/usr/bin/env python
# -*- coding: utf-8 -*-
from framework.CSingleton import CSingleton
from service.logic.CSvcTableInfo import CSvcTableInfo
from framework.CEvtManager import CEvtManager
from app.logic.CEnumEvent import CEnumEvent

class CDataTable(object):
    def __init__(self, id_, code, name, table_type, area, peple_num, min_type):
        self.id = id_
        self.code = code
        self.name = name
        self.table_type = table_type
        self.area = area
        self.peple_num = peple_num
        self.min_type = min_type
        
class CDataTableInfo(CSingleton):
    cur_item_index = 0
    table_items = list()
    
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @staticmethod
    def GetCurItemIndex():
        return CDataTableInfo.cur_item_index
    
    @staticmethod
    def SetCurItemIndex(index):
        CDataTableInfo.cur_item_index = index
    
    @staticmethod
    def GetData():
        result = CSvcTableInfo.GetAll()
        data = list()
        for item in result:
            data_item = CDataTable(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            data.append(data_item)
            
        #CDataTypeInfo.data_len = len(data)
            
        return data
    
    @staticmethod
    def RefreshItems():
        del CDataTableInfo.table_items[0:len(CDataTableInfo.table_items)]
        result = CSvcTableInfo.GetItems()
        for item in result:
            data_item = CDataTable(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            CDataTableInfo.table_items.append(data_item)
            
    @staticmethod
    def GetItems():            
        return CDataTableInfo.table_items
    
    @staticmethod
    def AddItem(data):
        if isinstance(data, CDataTable):
            item = [data.code, data.name, data.table_type, data.area, data.peple_num, data.min_type]
            CSvcTableInfo.AddItem(item)
            CEvtManager.DispatchEvent(CEnumEvent.EVT_DINING_ROOM_REFRESH)
    
    @staticmethod      
    def AddItems(data):
        for obj in data:
            if isinstance(obj, CDataTable):
                item = [obj.code, obj.name, obj.table_type, obj.area, obj.peple_num, obj.min_type]
                CSvcTableInfo.AddItem(item)
        CEvtManager.DispatchEvent(CEnumEvent.EVT_DINING_ROOM_REFRESH)         
            
    @staticmethod
    def DeleteItem(data):
        if isinstance(data, CDataTable):
            item = [data.code, data.name, data.table_type, data.area, data.peple_num, data.min_type]
            CSvcTableInfo.DeleteItem(item)
            CEvtManager.DispatchEvent(CEnumEvent.EVT_DINING_ROOM_REFRESH)
            
    @staticmethod
    def UpdateItem(data):
        if isinstance(data, CDataTable):
            item = [data.code, data.name, data.table_type, data.area, data.peple_num, data.min_type]
            CSvcTableInfo.UpdateItem(item)
            CEvtManager.DispatchEvent(CEnumEvent.EVT_DINING_ROOM_REFRESH)