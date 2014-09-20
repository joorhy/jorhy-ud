#!/usr/bin/env python
#_*_ encoding=utf-8 _*_

from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from service.CSqlManager import CSqlManager
from service.data_base.CDbPrinterScheme import CDbPrinterScheme

class CDbDishPublish(CSqlManager.base_model):
    __tablename__ = 'dish_publish'

    num_id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))
    num_code = Column(Integer)
    vch_spell = Column(String(45))
    num_default_price = Column(Integer)
    vch_picname = Column(String(45))
    num_style_id = Column(ForeignKey(u'dish_style.num_id'), index=True)
    num_spec_id = Column(ForeignKey(u'dish_spec.num_id'), index=True)
    num_category = Column(ForeignKey(u'dish_category.num_id'), index=True)
    num_unit = Column(ForeignKey(u'unit.num_id'), index=True)
    num_ticheng = Column(Float)
    num_discount = Column(Float)
    num_change_code = Column(Integer)
    num_printer_scheme_id = Column(ForeignKey(u'printer_scheme.num_id'), index=True)

    dish_category = relationship(u'CDbDishCategory')
    num_printer_scheme = relationship(u'CDbPrinterScheme')
    num_spec = relationship(u'CDbDishSpec')
    num_style = relationship(u'CDbDishStyle')
    unit = relationship(u'CDbUnit')
    
    def __repr__(self):
        return '%s' % (self.__class__.__name__)