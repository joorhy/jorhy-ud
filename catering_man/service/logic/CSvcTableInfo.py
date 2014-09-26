#!/usr/bin/env python
#_*_ encoding=utf-8 _*_
from framework.CSingleton import CSingleton
from service.CSqlManager import CSqlManager
from service.data_base.canteen import TableInfo

class CSvcTableInfo(CSingleton):
    def __repr__(self):
        return '%s' % (self.__class__.__name__)

    @staticmethod
    def GetAll():
        session = CSqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(TableInfo).all()   
                               
        index = 0
        data = list()
        for item in result:
            data.append([index, int(item.num_id), item.vch_name, item.table_info_type.vch_name, 
                         item.table_info_area.vch_name, int(item.num_people_amount), item.table_info_minexpense.vch_name])
            index += 1
            
        return data
    
    @staticmethod
    def GetItems():
        session = CSqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(TableInfo.num_id, 
                               TableInfo.vch_name, 
                               TableInfo.num_people_amount, 
                               TableInfo.num_minexpense_type, 
                               TableInfo.num_area, 
                               TableInfo.num_type
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
        
        tableInfo = TableInfo()
        tableInfo.vch_name = data[1]
        tableInfo.num_type = data[2]
        tableInfo.num_area = data[3]
        tableInfo.num_people_amount = data[4]
        tableInfo.num_minexpense_type = data[5]
            
        session = CSqlManager.session
        session.add(tableInfo)
        session.flush()
        session.commit()
        
    @staticmethod
    def DeleteItem(data):
        if not data:
            return
        
        session = CSqlManager.session
        session.query(TableInfo).filter(TableInfo.num_id == data[0]).delete()
        session.flush()
        session.commit()
    
    @staticmethod
    def UpdateItem(data):
        if not data:
            return
        
        session = CSqlManager.session
        session.query(TableInfo).filter(TableInfo.num_id == data[0]
                                        ).update({
                                                 TableInfo.vch_name:data[1],
                                                 TableInfo.num_type:data[2],
                                                 TableInfo.num_area:data[3],
                                                 TableInfo.num_people_amount:data[4],
                                                 TableInfo.num_minexpense_type:data[5]})
        session.flush()
        session.commit()