#_*_ encoding=utf-8 _*_
#!/usr/bin/env python
from framework.CSingleton import CSingleton
from service.CSqlManager import CSqlManager
from service.data_base.CDbTableInfoType import CDbTableInfoType

class CSvcTypeSetting(CSingleton):
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @staticmethod
    def GetAll():
        session = CSqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(CDbTableInfoType).all()
        index = 0
        data = list()
        for item in result:
            data.append([index, int(item.num_id), item.vch_name])
            index += 1
            
        return data
    
    @staticmethod
    def GetId():
        session = CSqlManager.session
        result = session.query(CDbTableInfoType.num_id).all()
        result.reverse()
        print result[0][0]
        return int(result[0][0])
    
    @staticmethod
    def AddItem(data):
        if not data:
            return
        
        tableInfoType = CDbTableInfoType()
        tableInfoType.vch_name = data[1]
            
        session = CSqlManager.session
        session.add(tableInfoType)
        session.flush()
        session.commit()
        
    @staticmethod
    def DeleteItem(data):
        if not data:
            return
        
        session = CSqlManager.session
        session.query(CDbTableInfoType).filter(CDbTableInfoType.num_id == data[0]).delete()
        session.flush()
        session.commit()
    
    @staticmethod
    def UpdateItem(data):
        if not data:
            return
        
        session = CSqlManager.session
        session.query(CDbTableInfoType).filter(CDbTableInfoType.num_id == data[0]).update({CDbTableInfoType.vch_name:data[1]})
        session.flush()
        session.commit()