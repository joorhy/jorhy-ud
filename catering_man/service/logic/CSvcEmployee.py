#!/usr/bin/env python
#_*_ encoding=utf-8 _*_
from framework.CSingleton import CSingleton
from service.CSqlManager import CSqlManager
from service.data_base.CDbUUserInfo import CDbUUserInfo
from service.data_base.CDbUType import CDbUType
from service.data_base.CDbUUserdetail import CDbUUserdetail

class CSvcEmployee(CSingleton):
    def __repr__(self):
        return '%s' % (self.__class__.__name__)

    @staticmethod
    def GetAll():
        session = CSqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(CDbUUserInfo.num_id, 
                               CDbUUserInfo.vch_name).all()        

        index = 0
        data = list()
        for item in result:
            data.append([index, int(item[0]), item[1], item[5], item[4], int(item[2]), item[3]])
            index += 1
            
        return data
    
    @staticmethod
    def GetItems():
        session = CSqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(CDbUUserInfo.num_id, 
                               CDbUUserInfo.vch_name
                               ).all()
        index = 0
        data = list()
        for item in result:
            data.append([index, int(item[0]), item[1], int(item[5]), int(item[4]), int(item[2]), int(item[3])])
            index += 1
            
        return data
    
    @staticmethod
    def AddItem(data):
        if not data:
            return
        
        tableInfo = CDbUUserInfo()
        tableInfo.vch_name = data[1]
            
        session = CSqlManager.session
        session.add(tableInfo)
        session.flush()
        session.commit()
        
    @staticmethod
    def DeleteItem(data):
        if not data:
            return
        
        session = CSqlManager.session
        session.query(CDbUUserInfo).filter(CDbUUserInfo.num_id == data[0]).delete()
        session.flush()
        session.commit()
    
    @staticmethod
    def UpdateItem(data):
        if not data:
            return
        
        session = CSqlManager.session
        session.query(CDbUUserInfo).filter(
                                           CDbUUserInfo.num_id == data[0]
                                           ).update({
                                                     CDbUUserInfo.vch_name:data[1],
                                                     })
        session.flush()
        session.commit()
