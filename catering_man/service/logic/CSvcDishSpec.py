#!/usr/bin/env python
#_*_ encoding=utf-8 _*_

from framework.CSingleton import CSingleton
from service.CSqlManager import CSqlManager
from service.data_base.CDbDishSpec import CDbDishSpec

class CSvcDishSpec(CSingleton):
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @staticmethod
    def GetAll():
        session = CSqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(CDbDishSpec).all()
        data = list()
        for item in result:
            data.append([int(item.num_id), item.vch_name, int(item.num_price)])
            
        return data
    
    @staticmethod
    def GetId():
        session = CSqlManager.session
        result = session.query(CDbDishSpec.num_id).all()
        result.reverse()
        return int(result[0][0])
    
    @staticmethod
    def AddItem(data):
        if not data:
            return
        
        dishSpec = CDbDishSpec()
        dishSpec.vch_name = data[1]
        dishSpec.num_price = data[2]
            
        session = CSqlManager.session
        session.add(dishSpec)
        session.flush()
        session.commit()
        
    @staticmethod
    def DeleteItem(data):
        if not data:
            return
        
        session = CSqlManager.session
        session.query(CDbDishSpec).filter(CDbDishSpec.num_id == data[0]).delete()
        session.flush()
        session.commit()
    
    @staticmethod
    def UpdateItem(data):
        if not data:
            return
        
        session = CSqlManager.session
        session.query(CDbDishSpec).filter(CDbDishSpec.num_id == data[0]).update({CDbDishSpec.vch_name:data[1], 
                                                                                 CDbDishSpec.num_price:data[2]})
        session.flush()
        session.commit()