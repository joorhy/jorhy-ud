#!/usr/bin/env python
#_*_ encoding=utf-8 _*_

from sqlalchemy import Column, Integer, String
from service.CSqlManager import CSqlManager

class CDbPrinterSchemeType(CSqlManager.base_model):
    __tablename__ = 'printer_scheme_type'

    num_id = Column(Integer, primary_key=True, index=True)
    vch_name = Column(String(45))
    
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
