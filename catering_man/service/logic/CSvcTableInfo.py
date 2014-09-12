#!/usr/bin/env python
#_*_ encoding=utf-8 _*_
from framework.CSingleton import CSingleton
from service.data_base.CDbTableInfo import CDbTableInfo
from service.CSqlManager import CSqlManager
from service.data_base.CDbTableInfoArea import CDbTableInfoArea
from service.data_base.CDbTableInfoType import CDbTableInfoType
from service.data_base.CDbTableInfoMinexpense import CDbTableInfoMinexpense

class CSvcTableInfo(CSingleton):
    def __repr__(self):
        return '%s' % (self.__class__.__name__)

    @staticmethod
    def GetAll():
        session = CSqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(CDbTableInfo.num_id, 
                               CDbTableInfo.vch_name, 
                               CDbTableInfo.num_people_amount, 
                               CDbTableInfoMinexpense.vch_name, 
                               CDbTableInfoArea.vch_name, 
                               CDbTableInfoType.vch_name
                               ).join(CDbTableInfoArea, 
                                      CDbTableInfo.num_area == CDbTableInfoArea.num_id
                                      ).join(CDbTableInfoType, 
                                             CDbTableInfo.num_type == CDbTableInfoType.num_id
                                             ).join(CDbTableInfoMinexpense,
                                                    CDbTableInfo.num_minexpense_type == CDbTableInfoMinexpense.num_id).all()
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
        
        result = session.query(CDbTableInfo.num_id, 
                               CDbTableInfo.vch_name, 
                               CDbTableInfo.num_people_amount, 
                               CDbTableInfo.num_minexpense_type, 
                               CDbTableInfo.num_area, 
                               CDbTableInfo.num_type
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
        
        tableInfo = CDbTableInfo()
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
        session.query(CDbTableInfo).filter(CDbTableInfo.num_id == data[0]).delete()
        session.flush()
        session.commit()
    
    @staticmethod
    def UpdateItem(data):
        if not data:
            return
        
        session = CSqlManager.session
        session.query(CDbTableInfo).filter(
                                           CDbTableInfo.num_id == data[0]
                                           ).update({
                                                     CDbTableInfo.vch_name:data[1],
                                                     CDbTableInfo.num_type:data[2],
                                                     CDbTableInfo.num_area:data[3],
                                                     CDbTableInfo.num_people_amount:data[4],
                                                     CDbTableInfo.num_minexpense_type:data[5]})
        session.flush()
        session.commit()