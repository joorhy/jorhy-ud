
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from framework.CSingleton import CSingleton
from service.logic.CSvcTypeSetting import CSvcTypeSetting

class CDataType(object):
    def __init__(self, id_, code, name):
        self.id = id_
        self.code = code
        self.name = name

class CDataTypeInfo(CSingleton):
    data_len = 0
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @staticmethod
    def GetDataLen():
        return CDataTypeInfo.data_len - 2
    
    @staticmethod
    def GetData():
        result = CSvcTypeSetting.GetAll()
        data = list()
        for item in result:
            data_item = CDataType(item[0], item[1], item[2])
            data.append(data_item)
            
        CDataTypeInfo.data_len = len(data)
            
        return data
    
    @staticmethod
    def GetId():
        return CSvcTypeSetting.GetId()
    
    @staticmethod
    def AddItem(data):
        if isinstance(data, CDataType):
            item = [data.code, data.name]
            CSvcTypeSetting.AddItem(item)
            CDataTypeInfo.data_len += 1
            
    @staticmethod
    def DeleteItem(data):
        if isinstance(data, CDataType):
            item = [data.code, data.name]
            CSvcTypeSetting.DeleteItem(item)
            
    @staticmethod
    def UpdateItem(data):
        if isinstance(data, CDataType):
            item = [data.code, data.name]
            CSvcTypeSetting.UpdateItem(item)