#_*_ encoding=utf-8 _*_
#!/usr/bin/env python
from sqlalchemy import Column, Integer, String 
from service.CSqlManager import CSqlManager

class CDbTableInfoType(CSqlManager.base_model):
    __tablename__ = 'table_info_type'
    num_id = Column(Integer, primary_key=True)
    vch_name = Column(String(16), unique=True, nullable=True)
     
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
