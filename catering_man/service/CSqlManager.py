
#_*_ encoding=utf-8 _*_
#!/usr/bin/env python
import framework.CSingleton as Singleton
from sqlalchemy.orm import mapper
from sqlalchemy import Table, MetaData, Column, Integer, String  
from sqlalchemy.engine import create_engine 
from sqlalchemy.orm import sessionmaker

class CUnit(object):pass

class CSqlManager(Singleton.CSingleton):
    def __init__(self):
        pass
    
    def Initailize(self):
        db_config = {
                     'host' : '127.0.0.1',
                     'user' : 'root',
                     'passwd' : '123456',
                     'db' : 'canteen',
                     'charset' : 'utf8'}
    
        self.engine = create_engine('mysql://%s:%s@%s/%s?charset=%s'%(db_config['user'],
                                                         db_config['passwd'],
                                                         db_config['host'],
                                                         db_config['db'],
                                                         db_config['charset']), echo=True)
        
        metadata = MetaData()
        
        unit = Table( #unit  
                'unit', metadata,  
                Column('num_id', Integer, primary_key=True),  
                Column('vch_name', String(16), unique=True, nullable=False),  
                )
        
        mapper(CUnit, unit)
        
        metadata.create_all(self.engine)
    
    def Uninitailize(self):
        pass
    
    def GetEngine(self):
        return self.engine
    
if __name__ == '__main__':
    
    man = CSqlManager()
    man.Initailize()
    
    unit = CUnit()
    print unit.vch_name
    '''unit.num_id = 1
    unit.vch_name = 'affaf'
    
    Session = sessionmaker()  
    Session.configure(bind=man.engine) 
    session = Session()  
    session.add(unit)
    session.flush()  
    session.commit() '''
    