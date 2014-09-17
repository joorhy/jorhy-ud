#!/usr/bin/env python
#_*_ encoding=utf-8 _*_

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from service.CSqlManager import CSqlManager
import CDbUPermList

class CDbUPermission(CSqlManager.base_model):
    __tablename__ = 'u_permission'

    num_id = Column(Integer, primary_key=True)
    num_perm_code = Column(ForeignKey(u'u_perm_list.num_id'), index=True)
    vch_perm_desc = Column(String(45))

    u_perm_list = relationship(u'CDbUPermList')
    
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
