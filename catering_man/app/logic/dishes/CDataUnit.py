#!/usr/bin/env python
# -*- coding: utf-8 -*-
from framework.core import Singleton
from service.logic.manager import SvcUnitSetting

class CDataUnit(object):
    def __init__(self, id_, code, name):
        self.id = id_
        self.code = code
        self.name = name

class CDataUnitInfo(Singleton):
    data_len = 0
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @staticmethod
    def GetDataLen():
        return CDataUnitInfo.data_len - 2
    
    @staticmethod
    def GetData():
        result = SvcUnitSetting.GetAll()
        data = list()
        for item in result:
            data_item = CDataUnit(item[0], item[1], item[2])
            data.append(data_item)
            
        CDataUnitInfo.data_len = len(data)
            
        return data
    
    @staticmethod
    def GetId():
        return SvcUnitSetting.GetId()
    
    @staticmethod
    def AddItem(data):
        if isinstance(data, CDataUnit):
            item = [data.code, data.name]
            SvcUnitSetting.AddItem(item)
            CDataUnitInfo.data_len += 1
            
    @staticmethod
    def DeleteItem(data):
        if isinstance(data, CDataUnit):
            item = [data.code, data.name]
            SvcUnitSetting.DeleteItem(item)
            
    @staticmethod
    def UpdateItem(data):
        if isinstance(data, CDataUnit):
            item = [data.code, data.name]
            SvcUnitSetting.UpdateItem(item)
