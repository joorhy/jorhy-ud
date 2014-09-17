#!/usr/bin/env python
#_*_ encoding=utf-8 _*_

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from service.CSqlManager import CSqlManager

class CDbUUserInfo(CSqlManager.base_model):
    __tablename__ = 'u_userinfo'

    num_id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))
    vch_psw = Column(String(45))
    num_user_type = Column(ForeignKey(u'u_type.num_id'), index=True)
    num_userdetails_id = Column(ForeignKey(u'u_userdetails.num_id'), index=True)

    u_type = relationship(u'CDbUType')
    num_userdetails = relationship(u'CDbUUserdetail')
    
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
