#!/usr/bin/env python
#_*_ encoding=utf-8 _*_

from framework.CSingleton import CSingleton
from service.CSqlManager import CSqlManager
from service.data_base.canteen import DishStyle

class CSvcDishStyle(CSingleton):
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @staticmethod
    def GetAll():
        session = CSqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(DishStyle).all()
        data = list()
        for item in result:
            data.append([int(item.num_id), item.vch_name, int(item.num_priceadd), item.ch_mountadd])
            
        return data
    
    @staticmethod
    def GetId():
        session = CSqlManager.session
        result = session.query(DishStyle.num_id).all()
        result.reverse()
        return int(result[0][0])
    
    @staticmethod
    def AddItem(data):
        if not data:
            return
        
        dishStyle = DishStyle()
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
        session.query(DishStyle).filter(DishStyle.num_id == data[0]).delete()
        session.flush()
        session.commit()
    
    @staticmethod
    def UpdateItem(data):
        if not data:
            return
        
        session = CSqlManager.session
        session.query(DishStyle).filter(DishStyle.num_id == data[0]).update({DishStyle.vch_name:data[1], 
                                                                                   DishStyle.num_priceadd:data[2],
                                                                                   DishStyle.ch_mountadd:data[3]})
        session.flush()
        session.commit()