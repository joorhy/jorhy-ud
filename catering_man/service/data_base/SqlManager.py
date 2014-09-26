#!/usr/bin/env python
#_*_ encoding=utf-8 _*_

from sqlalchemy import MetaData
from sqlalchemy.engine import create_engine 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from framework.core import Singleton

class SqlManager(Singleton):
    db_config = {
             'host' : '127.0.0.1',
             'user' : 'root',
             'passwd' : '123456',
             'db' : 'canteen',
             'charset' : 'utf8'}
    
    engine = create_engine('mysql://%s:%s@%s/%s?charset=%s'%(db_config['user'],
                                                     db_config['passwd'],
                                                     db_config['host'],
                                                     db_config['db'],
                                                     db_config['charset']), echo=True)
    
    metadata = MetaData()
    
    Session = sessionmaker()  
    Session.configure(bind=engine) 
    session = Session()
    
    base_model = declarative_base()
    
    @classmethod
    def Initailize(cls):
        SqlManager.base_model.metadata.create_all(SqlManager.engine)
    
    @classmethod
    def Uninitailize(cls):
        SqlManager.base_model.metadata.drop_all(SqlManager.engine)
    
if __name__ == '__main__':
    SqlManager.Initailize()
    
    from service.data_base.canteen import TableInfoArea
    ret = SqlManager.session.query(TableInfoArea).all()
    for item in ret:
        print item.vch_name
    