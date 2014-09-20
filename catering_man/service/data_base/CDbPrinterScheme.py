#!/usr/bin/env python
#_*_ encoding=utf-8 _*_

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from service.CSqlManager import CSqlManager
import CDbPrinterSchemeType

class CDbPrinterScheme(CSqlManager.base_model):
    __tablename__ = 'printer_scheme'

    num_id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))
    num_valid = Column(Integer)
    num_bill_type = Column(ForeignKey(u'printer_scheme_type.num_id'), index=True)
    num_print_count = Column(Integer)
    num_produced_count = Column(Integer)

    printer_scheme_type = relationship(u'CDbPrinterSchemeType')
    
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
