#!/usr/bin/env python
# -*- coding: utf-8 -*-
from framework.CSingleton import CSingleton
from service.logic.CSvcDepartment import CSvcDepartment

class CDataDepartment(object):
    def __init__(self, id_, code, name):
        self.id = id_
        self.code = code
        self.name = name

class CDataDepartmentInfo(CSingleton):
    data_len = 0
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @staticmethod
    def GetDataLen():
        return CDataDepartmentInfo.data_len - 2
    
    @staticmethod
    def GetData():
        result = CSvcDepartment.GetAll()
        data = list()
        for item in result:
            data_item = CDataDepartment(item[0], item[1], item[2])
            data.append(data_item)
            
        CDataDepartmentInfo.data_len = len(data)
            
        return data
    
    @staticmethod
    def GetId():
        return CSvcDepartment.GetId()
    
    @staticmethod
    def AddItem(data):
        if isinstance(data, CDataDepartment):
            item = [data.code, data.name]
            CSvcDepartment.AddItem(item)
            CDataDepartmentInfo.data_len += 1
            
    @staticmethod
    def DeleteItem(data):
        if isinstance(data, CDataDepartment):
            item = [data.code, data.name]
            CSvcDepartment.DeleteItem(item)
            
    @staticmethod
    def UpdateItem(data):
        if isinstance(data, CDataDepartment):
            item = [data.code, data.name]
            CSvcDepartment.UpdateItem(item)