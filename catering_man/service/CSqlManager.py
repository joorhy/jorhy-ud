
#_*_ encoding=utf-8 _*_
#!/usr/bin/env python
import framework.CSingleton as Singleton
from sqlalchemy.orm import mapper
from sqlalchemy import Table, MetaData, Column, Integer, String  
from sqlalchemy.engine import create_engine 
from sqlalchemy.orm import sessionmaker

class CUnit(object):pass

class CSqlManager(Singleton.CSingleton):
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
    
    Session = sessionmaker()  
    Session.configure(bind=engine) 
    session = Session()
    
    @staticmethod
    def Initailize():
        metadata = MetaData()
        unit = Table( #unit  
                'unit', metadata,  
                Column('num_id', Integer, primary_key=True),  
                Column('vch_name', String(16), unique=True, nullable=False),  
                )
        
        mapper(CUnit, unit)
        metadata.create_all(CSqlManager.engine)
    
    @staticmethod
    def Uninitailize():
        pass
    
if __name__ == '__main__':
    CSqlManager.Initailize()
    
    #print (CSqlManager.session.query(CUnit).all())
    ret = CSqlManager.session.query(CUnit).all()
    for item in ret:
        print item.vch_name
    '''unit = CUnit()
    #print unit.vch_name
    unit.num_id = 2
    unit.vch_name = 'affaf'
    
    Session = sessionmaker()  
    Session.configure(bind=CSqlManager.engine) 
    session = Session()  
    session.add(unit)
    session.flush()  
    session.commit()'''
    