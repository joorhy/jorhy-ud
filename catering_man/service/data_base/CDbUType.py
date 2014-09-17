#!/usr/bin/env python
#_*_ encoding=utf-8 _*_

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from service.CSqlManager import CSqlManager
import CDbUPermission

class CDbUType(CSqlManager.base_model):
    __tablename__ = 'u_type'

    num_id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))
    num_perm_id = Column(ForeignKey(u'u_permission.num_id'), index=True)

    num_perm = relationship(u'CDbUPermission')
    
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
