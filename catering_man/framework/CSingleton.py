#_*_ encoding=utf-8 _*_

class CSingleton(object):  
    def __new__(cls, *args, **kw):  
        if not hasattr(cls, '_instance'):  
            orig = super(CSingleton, cls)  
            cls._instance = orig.__new__(cls, *args, **kw)  
            
        return cls._instance  