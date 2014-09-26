#!/usr/bin/env python
# -*- coding: utf-8 -*-
from framework.core import Singleton
from service.logic.manager import SvcAreaSetting

class CDataArea(object):
    def __init__(self, id_, code, name):
        self.id = id_
        self.code = code
        self.name = name

class CDataAreaInfo(Singleton):
    data_len = 0
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @staticmethod
    def GetDataLen():
        return CDataAreaInfo.data_len - 2
    
    @staticmethod
    def GetData():
        result = SvcAreaSetting.GetAll()
        data = list()
        for item in result:
            data_item = CDataArea(item[0], item[1], item[2])
            data.append(data_item)
            
        CDataAreaInfo.data_len = len(data)
            
        return data
    
    @staticmethod
    def GetId():
        return SvcAreaSetting.GetId()
    
    @staticmethod
    def AddItem(data):
        if isinstance(data, CDataArea):
            item = [data.code, data.name]
            SvcAreaSetting.AddItem(item)
            CDataAreaInfo.data_len += 1
            
    @staticmethod
    def DeleteItem(data):
        if isinstance(data, CDataArea):
            item = [data.code, data.name]
            SvcAreaSetting.DeleteItem(item)
            
    @staticmethod
    def UpdateItem(data):
        if isinstance(data, CDataArea):
            item = [data.code, data.name]
            SvcAreaSetting.UpdateItem(item)