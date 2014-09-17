#!/usr/bin/env python
#_*_ encoding=utf-8 _*_

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from service.CSqlManager import CSqlManager
import CDbUDuty, CDbUUserStatu, CDbUDept

class CDbUUserdetail(CSqlManager.base_model):
    __tablename__ = 'u_userdetails'

    num_id = Column(Integer, primary_key=True)
    vch_realname = Column(String(45))
    vch_englishname = Column(String(45))
    vch_email = Column(String(45))
    vch_hobbies = Column(String(45))
    num_dept = Column(ForeignKey(u'u_dept.num_id'), index=True)
    num_duty = Column(ForeignKey(u'u_duty.num_id'), index=True)
    num_phone = Column(Integer)
    num_gender = Column(Integer)
    dt_birthday = Column(DateTime)
    num_status = Column(ForeignKey(u'u_user_status.num_id'), index=True)
    vch_idcard = Column(String(45))
    vch_address = Column(String(45))
    vch_memo = Column(String(45))

    u_dept = relationship(u'CDbUDept')
    u_duty = relationship(u'CDbUDuty')
    u_user_statu = relationship(u'CDbUUserStatu')
    
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
