#!/usr/bin/env python
# -*- coding: utf-8 -*-
from framework.core import Singleton
from service.logic.manager import SvcDepartment

class CDataDepartment(object):
    def __init__(self, id_, code, name):
        self.id = id_
        self.code = code
        self.name = name

class CDataDepartmentInfo(Singleton):
    data_len = 0
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @staticmethod
    def GetDataLen():
        return CDataDepartmentInfo.data_len - 2
    
    @staticmethod
    def GetData():
        result = SvcDepartment.GetAll()
        data = list()
        for item in result:
            data_item = CDataDepartment(item[0], item[1], item[2])
            data.append(data_item)
            
        CDataDepartmentInfo.data_len = len(data)
            
        return data
    
    @staticmethod
    def GetId():
        return SvcDepartment.GetId()
    
    @staticmethod
    def AddItem(data):
        if isinstance(data, CDataDepartment):
            item = [data.code, data.name]
            SvcDepartment.AddItem(item)
            CDataDepartmentInfo.data_len += 1
            
    @staticmethod
    def DeleteItem(data):
        if isinstance(data, CDataDepartment):
            item = [data.code, data.name]
            SvcDepartment.DeleteItem(item)
            
    @staticmethod
    def UpdateItem(data):
        if isinstance(data, CDataDepartment):
            item = [data.code, data.name]
            SvcDepartment.UpdateItem(item)
