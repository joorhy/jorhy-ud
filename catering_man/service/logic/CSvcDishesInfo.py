#!/usr/bin/env python
#_*_ encoding=utf-8 _*_
from framework.CSingleton import CSingleton
from service.data_base.CDbDishPublish import CDbDishPublish
from service.CSqlManager import CSqlManager

class CSvcDishesInfo(CSingleton):
    def __repr__(self):
        return '%s' % (self.__class__.__name__)

    @staticmethod
    def GetAll():
        session = CSqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(CDbDishPublish).all()   
                               
        index = 0
        data = list()
        for item in result:
            data.append([index, int(item.num_id), 
                         int(item.num_code),
                         item.vch_name, 
                         item.vch_spell,
                         item.num_spec.vch_name, 
                         item.dish_category.vch_name, 
                         int(item.num_default_price), 
                         item.unit.vch_name,
                         item.num_style.vch_name,
                         item.num_ticheng,
                         item.num_discount,
                         True,
                         item.vch_picname])
            index += 1
            
        return data
    
    @staticmethod
    def GetItems():
        session = CSqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(CDbDishPublish).all()
        index = 0
        data = list()
        for item in result:
            data.append([index, int(item.num_id), 
                         int(item.num_code),
                         item.vch_name, 
                         item.vch_spell,
                         item.num_spec_id, 
                         item.num_category, 
                         int(item.num_default_price), 
                         item.num_unit,
                         item.num_style_id,
                         item.num_ticheng,
                         item.num_discount,
                         True,
                         item.vch_picname])
            index += 1
            
        return data
    
    @staticmethod
    def AddItem(data):
        if not data:
            return
        
        dishPublish = CDbDishPublish()
        dishPublish.num_code = data[0]
        dishPublish.vch_name = data[1]
        dishPublish.vch_spell = data[2]
        dishPublish.num_spec_id = data[3]
        dishPublish.num_category = data[4]
        dishPublish.num_default_price = data[5]
        dishPublish.num_unit = data[6]
        dishPublish.num_style_id = data[7]
        dishPublish.num_ticheng = data[8]
        dishPublish.num_discount = data[9]
        dishPublish.vch_picname = data[11]
            
        session = CSqlManager.session
        session.add(dishPublish)
        session.flush()
        session.commit()
        
    @staticmethod
    def DeleteItem(data):
        if not data:
            return
        
        session = CSqlManager.session
        session.query(CDbDishPublish).filter(CDbDishPublish.num_id == data[0]).delete()
        session.flush()
        session.commit()
    
    @staticmethod
    def UpdateItem(data):
        if not data:
            return
        
        session = CSqlManager.session
        session.query(CDbDishPublish).filter(
                                           CDbDishPublish.num_id == data[0]
                                           ).update({
                                                     CDbDishPublish.num_code:data[1],
                                                     CDbDishPublish.vch_name:data[2],
                                                     CDbDishPublish.vch_spell:data[3],
                                                     CDbDishPublish.num_spec_id:data[4],
                                                     CDbDishPublish.num_category:data[5],
                                                     CDbDishPublish.num_default_price:data[6],
                                                     CDbDishPublish.num_unit:data[7],
                                                     CDbDishPublish.num_style_id:data[8],
                                                     CDbDishPublish.num_ticheng:data[9],
                                                     CDbDishPublish.num_discount:data[10],
                                                     CDbDishPublish.vch_picname:data[12]})
        session.flush()
        session.commit()