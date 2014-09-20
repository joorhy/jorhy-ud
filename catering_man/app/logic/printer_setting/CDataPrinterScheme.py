#!/usr/bin/env python
# -*- coding: utf-8 -*-
from framework.CSingleton import CSingleton
from service.logic.CSvcPrinterScheme import CSvcPrinterScheme
from framework.CEvtManager import CEvtManager
from app.logic.CEnumEvent import CEnumEvent

class CDataPrinterScheme(object):
    def __init__(self, id_, code, name, valid, scheme_type, print_count, backup):
        self.id = id_
        self.code = code
        self.name = name
        self.valid = valid
        self.scheme_type = scheme_type
        self.print_count = print_count
        self.backup = backup
        
class CDataPrinterSchemeInfo(CSingleton):
    cur_item_index = 0
    table_items = list()
    
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @staticmethod
    def GetCurItemIndex():
        return CDataPrinterSchemeInfo.cur_item_index
    
    @staticmethod
    def SetCurItemIndex(index):
        CDataPrinterSchemeInfo.cur_item_index = index
    
    @staticmethod
    def GetData():
        result = CSvcPrinterScheme.GetAll()
        data = list()
        for item in result:
            data_item = CDataPrinterScheme(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            data.append(data_item)
            
        return data
    
    @staticmethod
    def RefreshItems():
        del CDataPrinterSchemeInfo.table_items[0:len(CDataPrinterSchemeInfo.table_items)]
        result = CSvcPrinterScheme.GetItems()
        for item in result:
            data_item = CDataPrinterScheme(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            CDataPrinterSchemeInfo.table_items.append(data_item)
            
    @staticmethod
    def GetItems():            
        return CDataPrinterSchemeInfo.table_items
    
    @staticmethod
    def AddItem(data):
        if isinstance(data, CDataPrinterScheme):
            item = [data.code, data.name, data.valid, data.scheme_type, data.print_count, data.backup]
            CSvcPrinterScheme.AddItem(item)
            CEvtManager.DispatchEvent(CEnumEvent.EVT_PRINTER_SCHEME_REFRESH)       
            
    @staticmethod
    def DeleteItem(data):
        if isinstance(data, CDataPrinterScheme):
            item = [data.code, data.name]
            CSvcPrinterScheme.DeleteItem(item)
            CEvtManager.DispatchEvent(CEnumEvent.EVT_PRINTER_SCHEME_REFRESH)
            
    @staticmethod
    def UpdateItem(data):
        if isinstance(data, CDataPrinterScheme):
            item = [data.code, data.name, data.valid, data.scheme_type, data.print_count, data.backup]
            CSvcPrinterScheme.UpdateItem(item)
            CEvtManager.DispatchEvent(CEnumEvent.EVT_PRINTER_SCHEME_REFRESH)