#!/usr/bin/env python
# -*- coding: utf-8 -*-
from framework.core import Singleton, EvtManager
from service.logic.manager import SvcDishesInfo
from app.logic.CEnumEvent import CEnumEvent

class CDataDishes(object):
    def __init__(self, line, id_, code, name, spell, spec, category, 
                 price, unit, style, commistion, discount, stop, image_url, printer_scheme):
        self.line = line
        self.id = id_
        self.code = code
        self.name = name
        self.spell = spell
        self.spec = spec
        self.category = category
        self.price = price
        self.unit = unit
        self.style = style
        self.commistion = commistion
        self.discount = discount
        self.stop = stop
        self.image_url = image_url
        self.printer_scheme = printer_scheme
        
class CDataDishesInfo(Singleton):
    cur_item_index = 0
    cur_list_data = None
    table_items = list()
    
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @staticmethod
    def GetCurItemIndex():
        return CDataDishesInfo.cur_item_index
    
    @staticmethod
    def SetCurItemIndex(index):
        CDataDishesInfo.cur_item_index = index
        
    @staticmethod
    def SetCurItemIndex2(item):
        CDataDishesInfo.cur_item_index = CDataDishesInfo.table_items.index(item)
    
    @staticmethod
    def SetCurListData(data):
        CDataDishesInfo.cur_list_data = data
    
    @staticmethod
    def GetCurListData():
        return CDataDishesInfo.cur_list_data
    
    @staticmethod
    def GetData():
        result = SvcDishesInfo.GetAll()
        data = list()
        for item in result:
            data_item = CDataDishes(item[0], item[1], item[2], item[3], item[4], item[5], 
                                    item[6], item[7], item[8], item[9], item[10], item[11], 
                                    item[12], item[13], item[14])
            data.append(data_item)
            
        return data
    
    @staticmethod
    def RefreshItems():
        del CDataDishesInfo.table_items[0:len(CDataDishesInfo.table_items)]
        result = SvcDishesInfo.GetItems()
        for item in result:
            data_item = CDataDishes(item[0], item[1], item[2], item[3], item[4], item[5], 
                                    item[6], item[7], item[8], item[9], item[10], item[11],
                                    item[12], item[13], item[14])
            CDataDishesInfo.table_items.append(data_item)
            
    @staticmethod
    def GetItems():            
        return CDataDishesInfo.table_items
    
    @staticmethod
    def AddItem(data):
        if isinstance(data, CDataDishes):
            item = [data.code, data.name, data.spell, data.spec, data.category, data.price, data.unit, 
                    data.style, data.commistion, data.discount, data.stop, data.image_url]
            SvcDishesInfo.AddItem(item)
            EvtManager.DispatchEvent(CEnumEvent.EVT_DISHES_PUBLISH_REFRESH)        
            
    @staticmethod
    def DeleteItem(data):
        if isinstance(data, CDataDishes):
            item = [data.id, data.code, data.name]
            SvcDishesInfo.DeleteItem(item)
            EvtManager.DispatchEvent(CEnumEvent.EVT_DISHES_PUBLISH_REFRESH)
            
    @staticmethod
    def UpdateItem(data):
        if isinstance(data, CDataDishes):
            item = [data.id, data.code, data.name, data.spell, data.spec, data.category, data.price, data.unit, 
                    data.style, data.commistion, data.discount, data.stop, data.image_url]
            SvcDishesInfo.UpdateItem(item)
            EvtManager.DispatchEvent(CEnumEvent.EVT_DISHES_PUBLISH_REFRESH)
            
    @staticmethod        
    def UpdatePrinterScheme(data):
        if isinstance(data, CDataDishes):
            item = [data.id, data.printer_scheme]
            SvcDishesInfo.UpdatePrinterScheme(item)
            EvtManager.DispatchEvent(CEnumEvent.EVT_DISHES_PUBLISH_REFRESH)