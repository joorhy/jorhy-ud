#!/usr/bin/env python
# -*- coding: utf-8 -*-
from framework.CSingleton import CSingleton
from service.logic.CSvcDishSpec import CSvcDishSpec

class CDataSpec(object):
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

class CDataSpecInfo(CSingleton):
    data_len = 0
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @staticmethod
    def GetDataLen():
        return CDataSpecInfo.data_len - 2
    
    @staticmethod
    def GetData():
        result = CSvcDishSpec.GetAll()
        data = list()
        for item in result:
            data_item = CDataSpec(item[0], item[1], item[2])
            data.append(data_item)
            
        CDataSpecInfo.data_len = len(data)
            
        return data
    
    @staticmethod
    def GetId():
        return CSvcDishSpec.GetId()
    
    @staticmethod
    def AddItem(data):
        if isinstance(data, CDataSpec):
            item = [data.code, data.name, data.price]
            CSvcDishSpec.AddItem(item)
            CDataSpecInfo.data_len += 1
            
    @staticmethod
    def DeleteItem(data):
        if isinstance(data, CDataSpec):
            item = [data.code, data.name]
            CSvcDishSpec.DeleteItem(item)
            
    @staticmethod
    def UpdateItem(data):
        if isinstance(data, CDataSpec):
            item = [data.code, data.name, data.price]
            CSvcDishSpec.UpdateItem(item)