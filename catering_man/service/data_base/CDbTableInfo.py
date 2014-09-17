#!/usr/bin/env python
#_*_ encoding=utf-8 _*_

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from service.CSqlManager import CSqlManager

class CDbTableInfo(CSqlManager.base_model):
    __tablename__ = 'table_info'

    num_id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))
    num_type = Column(ForeignKey(u'table_info_type.num_id'), index=True)
    num_area = Column(ForeignKey(u'table_info_area.num_id'), index=True)
    num_people_amount = Column(Integer)
    num_minexpense_type = Column(ForeignKey(u'table_info_minexpense.num_id'), index=True)

    table_info_area = relationship(u'CDbTableInfoArea')
    table_info_minexpense = relationship(u'CDbTableInfoMinexpense')
    table_info_type = relationship(u'CDbTableInfoType')
    
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
