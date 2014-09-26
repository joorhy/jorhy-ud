#!/usr/bin/env python
#_*_ encoding=utf-8 _*_

from framework.CSingleton import CSingleton
from service.CSqlManager import CSqlManager
from service.data_base.canteen import UPermission

class CSvcUserRole(CSingleton):
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @staticmethod
    def GetAll():
        session = CSqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(UPermission).all()
        index = 0
        data = list()
        for item in result:
            data.append([index, int(item.num_id), int(item.num_perm_code), item.vch_perm_desc])
            index += 1
            
        return data
    
    @staticmethod
    def GetId():
        session = CSqlManager.session
        result = session.query(UPermission.num_id).all()
        result.reverse()
        print result[0][0]
        return int(result[0][0])
    
    @staticmethod
    def AddItem(data):
        if not data:
            return
        
        user_role = UPermission()
        user_role.num_perm_code = data[1]
        user_role.vch_perm_desc = data[2]
            
        session = CSqlManager.session
        session.add(user_role)
        session.flush()
        session.commit()
        
    @staticmethod
    def DeleteItem(data):
        if not data:
            return
        
        session = CSqlManager.session
        session.query(UPermission).filter(UPermission.num_id == data[0]).delete()
        session.flush()
        session.commit()
    
    @staticmethod
    def UpdateItem(data):
        if not data:
            return
        
        session = CSqlManager.session
        session.query(UPermission).filter(UPermission.num_id == data[0]).update({UPermission.num_perm_code:data[1], UPermission.vch_perm_desc:data[2]})
        session.flush()
        session.commit()