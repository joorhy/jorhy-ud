#!/usr/bin/env python
# -*- coding: utf-8 -*-
from framework.CSingleton import CSingleton
from service.logic.manager import SvcUserRole

class CDataUserRole(object):
    def __init__(self, line, id_, code, name):
        self.line = line
        self.id = id_
        self.code = code
        self.name = name

class CDataUserRoleInfo(CSingleton):
    data_len = 0
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @staticmethod
    def GetDataLen():
        return CDataUserRoleInfo.data_len - 2
    
    @staticmethod
    def GetData():
        result = SvcUserRole.GetAll()
        data = list()
        for item in result:
            data_item = CDataUserRole(item[0], item[1], item[2], item[3])
            data.append(data_item)
            
        CDataUserRoleInfo.data_len = len(data)
            
        return data
    
    @staticmethod
    def GetId():
        return SvcUserRole.GetId()
    
    @staticmethod
    def AddItem(data):
        if isinstance(data, CDataUserRole):
            item = [data.id, data.code, data.name]
            SvcUserRole.AddItem(item)
            CDataUserRoleInfo.data_len += 1
            
    @staticmethod
    def DeleteItem(data):
        if isinstance(data, CDataUserRole):
            item = [data.id, data.code, data.name]
            SvcUserRole.DeleteItem(item)
            
    @staticmethod
    def UpdateItem(data):
        if isinstance(data, CDataUserRole):
            item = [data.id, data.code, data.name]
            SvcUserRole.UpdateItem(item)
