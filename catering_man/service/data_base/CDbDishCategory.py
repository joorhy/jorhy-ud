#_*_ encoding=utf-8 _*_
#!/usr/bin/env python
from sqlalchemy import Column, Integer, String 
from service.CSqlManager import CSqlManager

class CDbDishCategory(CSqlManager.base_model):
    __tablename__ = 'dish_category'

    num_id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))
     
    def __repr__(self):
        return '%s' % (self.__class__.__name__)

