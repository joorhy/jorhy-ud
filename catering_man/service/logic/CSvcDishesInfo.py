#!/usr/bin/env python
#_*_ encoding=utf-8 _*_
from framework.CSingleton import CSingleton
from service.CSqlManager import CSqlManager
from service.data_base.canteen import DishPublish

class CSvcDishesInfo(CSingleton):
    def __repr__(self):
        return '%s' % (self.__class__.__name__)

    @staticmethod
    def GetAll():
        session = CSqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(DishPublish).all()   
                               
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
                         item.vch_picname,
                         "" if item.num_printer_scheme == None else item.num_printer_scheme.vch_name])
            index += 1
            
        return data
    
    @staticmethod
    def GetItems():
        session = CSqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(DishPublish).all()
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
                         item.vch_picname,
                         item.num_printer_scheme_id])
            index += 1
            
        return data
    
    @staticmethod
    def AddItem(data):
        if not data:
            return
        
        dishPublish = DishPublish()
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
        session.query(DishPublish).filter(DishPublish.num_id == data[0]).delete()
        session.flush()
        session.commit()
    
    @staticmethod
    def UpdateItem(data):
        if not data:
            return
        
        session = CSqlManager.session
        session.query(DishPublish).filter(DishPublish.num_id == data[0]
                                           ).update({
                                                     DishPublish.num_code:data[1],
                                                     DishPublish.vch_name:data[2],
                                                     DishPublish.vch_spell:data[3],
                                                     DishPublish.num_spec_id:data[4],
                                                     DishPublish.num_category:data[5],
                                                     DishPublish.num_default_price:data[6],
                                                     DishPublish.num_unit:data[7],
                                                     DishPublish.num_style_id:data[8],
                                                     DishPublish.num_ticheng:data[9],
                                                     DishPublish.num_discount:data[10],
                                                     DishPublish.vch_picname:data[12],
                                                     DishPublish.num_printer_scheme_id:data[13]})
        session.flush()
        session.commit()
        
    @staticmethod
    def UpdatePrinterScheme(data):
        if not data:
            return
            
        session = CSqlManager.session
        session.query(DishPublish).filter(DishPublish.num_id == data[0]
                                           ).update({DishPublish.num_printer_scheme_id:data[1]})
        session.flush()
        session.commit()
        