#!/usr/bin/env python
#_*_ encoding=utf-8 _*_

from sqlalchemy import Column, Integer, String
from service.CSqlManager import CSqlManager

class CDbPrinterScheme(CSqlManager.base_model):
    __tablename__ = 'printer_scheme'

    num_id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))
    num_valid = Column(Integer)
    num_bill_type = Column(Integer)
    num_print_count = Column(Integer)
    num_produced_count = Column(Integer)
    
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
