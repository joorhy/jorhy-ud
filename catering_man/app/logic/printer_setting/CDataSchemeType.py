#!/usr/bin/env python
# -*- coding: utf-8 -*-
from framework.CSingleton import CSingleton
from service.logic.CSvcSchemeType import CSvcSchemeType

class CDataSchemeType(object):
    def __init__(self, id_, code, name):
        self.id = id_
        self.code = code
        self.name = name

class CDataSchemeTypeInfo(CSingleton):
    data_len = 0
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @staticmethod
    def GetDataLen():
        return CDataSchemeTypeInfo.data_len - 2
    
    @staticmethod
    def GetData():
        result = CSvcSchemeType.GetAll()
        data = list()
        for item in result:
            data_item = CDataSchemeType(item[0], item[1], item[2])
            data.append(data_item)
            
        CDataSchemeTypeInfo.data_len = len(data)
            
        return data
    
    @staticmethod
    def GetId():
        return CSvcSchemeType.GetId()
    
    @staticmethod
    def AddItem(data):
        if isinstance(data, CDataSchemeType):
            item = [data.code, data.name]
            CSvcSchemeType.AddItem(item)
            CDataSchemeTypeInfo.data_len += 1
            
    @staticmethod
    def DeleteItem(data):
        if isinstance(data, CDataSchemeType):
            item = [data.code, data.name]
            CSvcSchemeType.DeleteItem(item)
            
    @staticmethod
    def UpdateItem(data):
        if isinstance(data, CDataSchemeType):
            item = [data.code, data.name]
            CSvcSchemeType.UpdateItem(item)