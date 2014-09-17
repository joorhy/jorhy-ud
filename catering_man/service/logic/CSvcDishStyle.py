#!/usr/bin/env python
#_*_ encoding=utf-8 _*_

from framework.CSingleton import CSingleton
from service.CSqlManager import CSqlManager
from service.data_base.CDbDishStyle import CDbDishStyle

class CSvcDishStyle(CSingleton):
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @staticmethod
    def GetAll():
        session = CSqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(CDbDishStyle).all()
        data = list()
        for item in result:
            data.append([int(item.num_id), item.vch_name, int(item.num_priceadd), item.ch_mountadd])
            
        return data
    
    @staticmethod
    def GetId():
        session = CSqlManager.session
        result = session.query(CDbDishStyle.num_id).all()
        result.reverse()
        return int(result[0][0])
    
    @staticmethod
    def AddItem(data):
        if not data:
            return
        
        dishStyle = CDbDishStyle()
        dishStyle.vch_name = data[1]
        dishStyle.num_priceadd = data[2]
        dishStyle.ch_mountadd = data[3]
            
        session = CSqlManager.session
        session.add(dishStyle)
        session.flush()
        session.commit()
        
    @staticmethod
    def DeleteItem(data):
        if not data:
            return
        
        session = CSqlManager.session
        session.query(CDbDishStyle).filter(CDbDishStyle.num_id == data[0]).delete()
        session.flush()
        session.commit()
    
    @staticmethod
    def UpdateItem(data):
        if not data:
            return
        
        session = CSqlManager.session
        session.query(CDbDishStyle).filter(CDbDishStyle.num_id == data[0]).update({CDbDishStyle.vch_name:data[1], 
                                                                                   CDbDishStyle.num_priceadd:data[2],
                                                                                   CDbDishStyle.ch_mountadd:data[3]})
        session.flush()
        session.commit()