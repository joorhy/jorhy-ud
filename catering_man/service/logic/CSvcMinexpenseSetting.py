#!/usr/bin/env python
#_*_ encoding=utf-8 _*_

from framework.CSingleton import CSingleton
from service.CSqlManager import CSqlManager
from service.data_base.canteen import TableInfoMinexpense

class CSvcMinexpenseSetting(CSingleton):
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @staticmethod
    def GetAll():
        session = CSqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(TableInfoMinexpense).all()
        index = 0
        data = list()
        for item in result:
            data.append([index, int(item.num_id), item.vch_name, int(item.num_amount)])
            index += 1
            
        return data
    
    @staticmethod
    def GetId():
        session = CSqlManager.session
        result = session.query(TableInfoMinexpense.num_id).all()
        result.reverse()
        print result[0][0]
        return int(result[0][0])
    
    @staticmethod
    def AddItem(data):
        if not data:
            return
        
        tableInfoMinexpense = TableInfoMinexpense()
        tableInfoMinexpense.vch_name = data[1]
        tableInfoMinexpense.num_amount = data[2]
            
        session = CSqlManager.session
        session.add(tableInfoMinexpense)
        session.flush()
        session.commit()
        
    @staticmethod
    def DeleteItem(data):
        if not data:
            return
        
        session = CSqlManager.session
        session.query(TableInfoMinexpense).filter(TableInfoMinexpense.num_id == data[0]).delete()
        session.flush()
        session.commit()
    
    @staticmethod
    def UpdateItem(data):
        if not data:
            return
        
        session = CSqlManager.session
        session.query(TableInfoMinexpense).filter(TableInfoMinexpense.num_id == data[0]).update({TableInfoMinexpense.vch_name:data[1],TableInfoMinexpense.num_amount:data[2]})
        session.flush()
        session.commit()
