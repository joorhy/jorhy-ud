#!/usr/bin/env python
# -*- coding: utf-8 -*-
from framework.CSingleton import CSingleton
from service.logic.manager import SvcEmployee
from framework.CEvtManager import CEvtManager
from app.logic.CEnumEvent import CEnumEvent

class CDataEmployee(object):
    def __init__(self, num_id, line, code, name, birthday, duty, 
                 department, sex, telephone, id_card, state, addr, email, note):
        self.id = num_id
        self.line = line
        self.code = code
        self.name = name
        self.birthday = birthday
        self.duty = duty
        self.department = department
        self.sex = sex
        self.telephone = telephone
        self.id_card = id_card
        self.state = state
        self.addr = addr
        self.email = email
        self.note = note
        
class CDataEmployeeInfo(CSingleton):
    cur_item_index = 0
    table_items = list()
    
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @staticmethod
    def GetCurItemIndex():
        return CDataEmployeeInfo.cur_item_index
    
    @staticmethod
    def SetCurItemIndex(index):
        CDataEmployeeInfo.cur_item_index = index
    
    @staticmethod
    def GetData():
        result = SvcEmployee.GetAll()
        data = list()
        for item in result:
            data_item = CDataEmployee(item[0], item[1], item[2], item[3], item[4], item[5], item[6],
                                      item[7], item[8], item[9], item[10], item[11], item[12], item[13])
            data.append(data_item)
            
        return data
    
    @staticmethod
    def RefreshItems():
        del CDataEmployeeInfo.table_items[0:len(CDataEmployeeInfo.table_items)]
        result = SvcEmployee.GetItems()
        for item in result:
            data_item = CDataEmployee(item[0], item[1], item[2], item[3], item[4], item[5], item[6],
                                      item[7], item[8], item[9], item[10], item[11], item[12], item[13])
            CDataEmployeeInfo.table_items.append(data_item)
            
    @staticmethod
    def GetItems():            
        return CDataEmployeeInfo.table_items
    
    @staticmethod
    def AddItem(data):
        if isinstance(data, CDataEmployee):
            item = [data.code, data.name, data.birthday, data.duty, data.department, data.sex,
                    data.telephone, data.id_card, data.state, data.addr, data.email, data.note]
            SvcEmployee.AddItem(item)
            CEvtManager.DispatchEvent(CEnumEvent.EVT_EMPLOYEE_REFRESH)      
            
    @staticmethod
    def DeleteItem(data):
        if isinstance(data, CDataEmployee):
            item = [data.id, data.code, data.name]
            SvcEmployee.DeleteItem(item)
            CEvtManager.DispatchEvent(CEnumEvent.EVT_EMPLOYEE_REFRESH)
            
    @staticmethod
    def UpdateItem(data):
        if isinstance(data, CDataEmployee):
            item = [data.id, data.code, data.name, data.birthday, data.duty, data.department, data.sex,
                    data.telephone, data.id_card, data.state, data.addr, data.email, data.note]
            SvcEmployee.UpdateItem(item)
            CEvtManager.DispatchEvent(CEnumEvent.EVT_EMPLOYEE_REFRESH)