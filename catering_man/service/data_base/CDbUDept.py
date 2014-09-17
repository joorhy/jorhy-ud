#!/usr/bin/env python
#_*_ encoding=utf-8 _*_

from sqlalchemy import Column, Integer, String 
from service.CSqlManager import CSqlManager
class CDbUDept(CSqlManager.base_model):
    __tablename__ = 'u_dept'

    num_id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))
    
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
