#!/usr/bin/env python
#_*_ encoding=utf-8 _*_

from sqlalchemy import MetaData
from sqlalchemy.engine import create_engine 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from framework.core import Singleton


@Singleton
class SqlManager():
    def __init__(self):
        self.host = '127.0.0.1'
        self.user = 'root'
        self.password = '123456'

        self.engine = None
        self.metadata = None
        self.session = None
        self.base_model = None

    def initialize(self, host='127.0.0.1', user='root', password='123456'):
        self.host = host
        self.user = user
        self.password = password
        self.engine = create_engine('mysql://%s:%s@%s/%s?charset=%s' % (self.user, self.password, self.host,
                                                                        'canteen', 'utf8'), echo=True)

        self.metadata = MetaData()
        cls_session = sessionmaker()
        cls_session.configure(bind=self.engine)
        self.session = cls_session()

        self.base_model = declarative_base()
        self.base_model.metadata.create_all(self.engine)

    def un_initialize(self):
        self.base_model.metadata.drop_all(self.engine)
    
if __name__ == '__main__':
    SqlManager.get_instance().initialize()
    
    from service.data_base.canteen import TableInfoArea
    ret = SqlManager.get_instance().session.query(TableInfoArea).all()
    for item in ret:
        print item.vch_name