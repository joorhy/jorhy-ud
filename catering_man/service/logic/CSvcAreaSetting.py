#!/usr/bin/env python
#_*_ encoding=utf-8 _*_

from framework.CSingleton import CSingleton
from service.CSqlManager import CSqlManager
from service.data_base.CDbTableInfoArea import CDbTableInfoArea

class CSvcAreaSetting(CSingleton):
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @staticmethod
    def GetAll():
        session = CSqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(CDbTableInfoArea).all()
        index = 0
        data = list()
        for item in result:
            data.append([index, int(item.num_id), item.vch_name])
            index += 1
            
        return data
    
    @staticmethod
    def GetId():
        session = CSqlManager.session
        result = session.query(CDbTableInfoArea.num_id).all()
        result.reverse()
        print result[0][0]
        return int(result[0][0])
    
    @staticmethod
    def AddItem(data):
        if not data:
            return
        
        tableInfoArea = CDbTableInfoArea()
        tableInfoArea.vch_name = data[1]
            
        session = CSqlManager.session
        session.add(tableInfoArea)
        session.flush()
        session.commit()
        
    @staticmethod
    def DeleteItem(data):
        if not data:
            return
        
        session = CSqlManager.session
        session.query(CDbTableInfoArea).filter(CDbTableInfoArea.num_id == data[0]).delete()
        session.flush()
        session.commit()
    
    @staticmethod
    def UpdateItem(data):
        if not data:
            return
        
        session = CSqlManager.session
        session.query(CDbTableInfoArea).filter(CDbTableInfoArea.num_id == data[0]).update({CDbTableInfoArea.vch_name:data[1]})
        session.flush()
        session.commit()