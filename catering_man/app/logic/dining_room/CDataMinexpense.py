#!/usr/bin/env python
# -*- coding: utf-8 -*-
from framework.CSingleton import CSingleton
from service.logic.CSvcMinexpenseSetting import CSvcMinexpenseSetting

class CDataMinexpense(object):
    def __init__(self, id_, code, name, price):
        self.id = id_
        self.code = code
        self.name = name
        self.price = price

class CDataMinexpenseInfo(CSingleton):
    data_len = 0
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @staticmethod
    def GetDataLen():
        return CDataMinexpenseInfo.data_len - 2
    
    @staticmethod
    def GetData():
        result = CSvcMinexpenseSetting.GetAll()
        data = list()
        for item in result:
            data_item = CDataMinexpense(item[0], item[1], item[2], item[3])
            data.append(data_item)
            
        CDataMinexpenseInfo.data_len = len(data)
            
        return data
    
    @staticmethod
    def GetId():
        return CSvcMinexpenseSetting.GetId()
    
    @staticmethod
    def AddItem(data):
        if isinstance(data, CDataMinexpense):
            item = [data.code, data.name, data.price]
            CSvcMinexpenseSetting.AddItem(item)
            CDataMinexpenseInfo.data_len += 1
            
    @staticmethod
    def DeleteItem(data):
        if isinstance(data, CDataMinexpense):
            item = [data.code, data.name, data.price]
            CSvcMinexpenseSetting.DeleteItem(item)
            
    @staticmethod
    def UpdateItem(data):
        if isinstance(data, CDataMinexpense):
            item = [data.code, data.name, data.price]
            CSvcMinexpenseSetting.UpdateItem(item)
