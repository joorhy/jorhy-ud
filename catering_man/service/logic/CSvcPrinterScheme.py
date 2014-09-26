#!/usr/bin/env python
#_*_ encoding=utf-8 _*_
from framework.CSingleton import CSingleton
from service.CSqlManager import CSqlManager
from service.data_base.canteen import PrinterScheme

class CSvcPrinterScheme(CSingleton):
    def __repr__(self):
        return '%s' % (self.__class__.__name__)

    @staticmethod
    def GetAll():
        session = CSqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(PrinterScheme).all()   
                               
        index = 0
        data = list()
        for item in result:
            data.append([index, int(item.num_id), item.vch_name, item.num_valid, 
                         item.printer_scheme_type.vch_name, int(item.num_print_count), u"无"])
            index += 1
            
        return data
    
    @staticmethod
    def GetItems():
        session = CSqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(PrinterScheme).all()
        index = 0
        data = list()
        for item in result:
            data.append([index, int(item.num_id), item.vch_name, item.num_valid, 
                         int(item.num_bill_type), int(item.num_print_count), u"无"])
            index += 1
            
        return data
    
    @staticmethod
    def AddItem(data):
        if not data:
            return
        
        printerScheme = PrinterScheme()
        printerScheme.num_id = data[0]
        printerScheme.vch_name = data[1]
        printerScheme.num_valid = data[2]
        printerScheme.num_bill_type = data[3]
        printerScheme.num_print_count = data[4]
            
        session = CSqlManager.session
        session.add(printerScheme)
        session.flush()
        session.commit()
        
    @staticmethod
    def DeleteItem(data):
        if not data:
            return
        
        session = CSqlManager.session
        session.query(PrinterScheme).filter(PrinterScheme.num_id == data[0]).delete()
        session.flush()
        session.commit()
    
    @staticmethod
    def UpdateItem(data):
        if not data:
            return
        
        session = CSqlManager.session
        session.query(PrinterScheme).filter(PrinterScheme.num_id == data[0]
                                           ).update({
                                                     PrinterScheme.vch_name:data[1],
                                                     PrinterScheme.num_valid:data[2],
                                                     PrinterScheme.num_bill_type:data[3],
                                                     PrinterScheme.num_print_count:data[4]})
        session.flush()
        session.commit()