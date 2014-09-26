#!/usr/bin/env python
# -*- coding: utf-8 -*-
from framework.core import Singleton
from service.logic.manager import SvcCategorySetting

class CDataCategory(object):
    def __init__(self, id_, code, name):
        self.id = id_
        self.code = code
        self.name = name

class CDataCategoryInfo(Singleton):
    data_len = 0
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @staticmethod
    def GetDataLen():
        return CDataCategoryInfo.data_len - 2
    
    @staticmethod
    def GetData():
        result = SvcCategorySetting.GetAll()
        data = list()
        for item in result:
            data_item = CDataCategory(item[0], item[1], item[2])
            data.append(data_item)
            
        CDataCategoryInfo.data_len = len(data)
            
        return data
    
    @staticmethod
    def GetId():
        return SvcCategorySetting.GetId()
    
    @staticmethod
    def AddItem(data):
        if isinstance(data, CDataCategory):
            item = [data.code, data.name]
            SvcCategorySetting.AddItem(item)
            CDataCategoryInfo.data_len += 1
            
    @staticmethod
    def DeleteItem(data):
        if isinstance(data, CDataCategory):
            item = [data.code, data.name]
            SvcCategorySetting.DeleteItem(item)
            
    @staticmethod
    def UpdateItem(data):
        if isinstance(data, CDataCategory):
            item = [data.code, data.name]
            SvcCategorySetting.UpdateItem(item)
