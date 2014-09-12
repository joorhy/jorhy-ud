#_*_ encoding=utf-8 _*_
#!/usr/bin/env python
from sqlalchemy import Column, Integer, String 
from service.CSqlManager import CSqlManager

class CDbTableInfo(CSqlManager.base_model):
    __tablename__ = 'table_info'
    num_id              = Column(Integer, primary_key=True)
    vch_name            = Column(String(45), unique=True, nullable=True)
    num_type            = Column(Integer, nullable=True)
    num_area            = Column(Integer, nullable=True)
    num_people_amount   = Column(Integer, nullable=True)
    num_minexpense_type = Column(Integer, nullable=True)
    
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
