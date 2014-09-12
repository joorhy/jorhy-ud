#!/usr/bin/env python
#_*_ encoding=utf-8 _*_

from sqlalchemy import MetaData
from sqlalchemy.engine import create_engine 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from framework.CSingleton import CSingleton

class CSqlManager(CSingleton):
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
    
    @staticmethod
    def Initailize():
        CSqlManager.base_model.metadata.create_all(CSqlManager.engine)
        '''# map table_info_area to class CDbTableInfoArea
        table_area_info = Table( #table_info_area  
                'table_info_area', CSqlManager.metadata,  
                Column('num_id', Integer, primary_key=True),  
                Column('vch_name', String(16), unique=True, nullable=True),  
                )
        mapper(CDbTableInfoArea, table_area_info)'''
    
    @staticmethod
    def Uninitailize():
        CSqlManager.base_model.metadata.drop_all(CSqlManager.engine)
    
if __name__ == '__main__':
    CSqlManager.Initailize()
    
    from service.data_base.CDbTableInfoArea import CDbTableInfoArea
    ret = CSqlManager.session.query(CDbTableInfoArea).all()
    for item in ret:
        print item.vch_name
    