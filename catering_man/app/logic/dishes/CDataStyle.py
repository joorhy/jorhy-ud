#!/usr/bin/env python
# -*- coding: utf-8 -*-
from framework.CSingleton import CSingleton
from service.logic.manager import SvcDishStyle

class CDataStyle(object):
    def __init__(self, code, name, price_add, amount_add):
        self.code = code
        self.name = name
        self.price_add = price_add
        self.amount_add = amount_add

class CDataStyleInfo(CSingleton):
    data_len = 0
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @staticmethod
    def GetDataLen():
        return CDataStyleInfo.data_len - 2
    
    @staticmethod
    def GetData():
        result = SvcDishStyle.GetAll()
        data = list()
        for item in result:
            data_item = CDataStyle(item[0], item[1], item[2], item[3])
            data.append(data_item)
            
        CDataStyleInfo.data_len = len(data)
            
        return data
    
    @staticmethod
    def GetId():
        return SvcDishStyle.GetId()
    
    @staticmethod
    def AddItem(data):
        if isinstance(data, CDataStyle):
            item = [data.code, data.name, data.price_add, data.amount_add]
            SvcDishStyle.AddItem(item)
            CDataStyleInfo.data_len += 1
            
    @staticmethod
    def DeleteItem(data):
        if isinstance(data, CDataStyle):
            item = [data.code, data.name]
            SvcDishStyle.DeleteItem(item)
            
    @staticmethod
    def UpdateItem(data):
        if isinstance(data, CDataStyle):
            item = [data.code, data.name, data.price_add, data.amount_add]
            SvcDishStyle.UpdateItem(item)
