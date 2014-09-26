#!/usr/bin/env python
#_*_ encoding=utf-8 _*_
from framework.core import Singleton, EvtManager
from app.manager.logic.data import *
from service.data_base.manager import *
from app.manager.etype import EnumEvent

class CtrlHomePage(Singleton):
    m_frame_width = 800
    m_frame_height = 600
    m_selected_item = 5
    
    def __init__(self):
        pass
    
    def __def__(self):
        pass

    @classmethod
    def GetFrameSize(cls):
        return CtrlHomePage.m_frame_width, CtrlHomePage.m_frame_height
    
    @classmethod
    def SetFrameSize(cls, x, y):
        CtrlHomePage.m_frame_width = x
        CtrlHomePage.m_frame_height = y
        
    @classmethod
    def GetSelectedItem(cls):
        return CtrlHomePage.m_selected_item
    
    @classmethod
    def SetSelectedItem(cls, strItem = 5):
        # 0 for dining room setting
        # 1 for dishes publishing
        # 2 for employee manager
        # 3 for printer setting
        # 4 for report form manager
        # 5 for system setting
        CtrlHomePage.m_selected_item = strItem
        
class CtrlArea(Singleton):
    data_len = 0
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @classmethod
    def GetDataLen(cls):
        return CtrlArea.data_len - 2
    
    @classmethod
    def GetData(cls):
        result = SvcAreaSetting.GetAll()
        data = list()
        for item in result:
            data_item = CtrlArea(item[0], item[1], item[2])
            data.append(data_item)
            
        CtrlArea.data_len = len(data)
            
        return data
    
    @classmethod
    def GetId(cls):
        return SvcAreaSetting.GetId()
    
    @classmethod
    def AddItem(cls, data):
        if isinstance(data, DataArea):
            item = [data.code, data.name]
            SvcAreaSetting.AddItem(item)
            CtrlArea.data_len += 1
            
    @classmethod
    def DeleteItem(cls, data):
        if isinstance(data, DataArea):
            item = [data.code, data.name]
            SvcAreaSetting.DeleteItem(item)
            
    @classmethod
    def UpdateItem(cls, data):
        if isinstance(data, DataArea):
            item = [data.code, data.name]
            SvcAreaSetting.UpdateItem(item)
            
class CtrlMinexpense(Singleton):
    data_len = 0
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @classmethod
    def GetDataLen(cls):
        return CtrlMinexpense.data_len - 2
    
    @classmethod
    def GetData(cls):
        result = SvcMinexpenseSetting.GetAll()
        data = list()
        for item in result:
            data_item = DataMinexpense(item[0], item[1], item[2], item[3])
            data.append(data_item)
            
        CtrlMinexpense.data_len = len(data)
            
        return data
    
    @classmethod
    def GetId(cls):
        return SvcMinexpenseSetting.GetId()
    
    @classmethod
    def AddItem(cls, data):
        if isinstance(data, DataMinexpense):
            item = [data.code, data.name, data.price]
            SvcMinexpenseSetting.AddItem(item)
            CtrlMinexpense.data_len += 1
            
    @classmethod
    def DeleteItem(cls, data):
        if isinstance(data, DataMinexpense):
            item = [data.code, data.name, data.price]
            SvcMinexpenseSetting.DeleteItem(item)
            
    @classmethod
    def UpdateItem(cls, data):
        if isinstance(data, DataMinexpense):
            item = [data.code, data.name, data.price]
            SvcMinexpenseSetting.UpdateItem(item)
            
class CtrlTable(Singleton):
    cur_item_index = 0
    table_items = list()
    
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @classmethod
    def GetCurItemIndex(cls):
        return CtrlTable.cur_item_index
    
    @classmethod
    def SetCurItemIndex(cls, index):
        CtrlTable.cur_item_index = index
    
    @classmethod
    def GetData(cls):
        result = SvcTableInfo.GetAll()
        data = list()
        for item in result:
            data_item = DataTable(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            data.append(data_item)
            
        return data
    
    @classmethod
    def RefreshItems(cls):
        del CtrlTable.table_items[0:len(CtrlTable.table_items)]
        result = SvcTableInfo.GetItems()
        for item in result:
            data_item = DataTable(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            CtrlTable.table_items.append(data_item)
            
    @classmethod
    def GetItems(cls):            
        return CtrlTable.table_items
    
    @classmethod
    def AddItem(cls, data):
        if isinstance(data, DataTable):
            item = [data.code, data.name, data.table_type, data.area, data.peple_num, data.min_type]
            SvcTableInfo.AddItem(item)
            EvtManager.DispatchEvent(EnumEvent.EVT_DINING_ROOM_REFRESH)
    
    @classmethod      
    def AddItems(cls, data):
        for obj in data:
            if isinstance(obj, DataTable):
                item = [obj.code, obj.name, obj.table_type, obj.area, obj.peple_num, obj.min_type]
                SvcTableInfo.AddItem(item)
        EvtManager.DispatchEvent(EnumEvent.EVT_DINING_ROOM_REFRESH)         
            
    @classmethod
    def DeleteItem(cls, data):
        if isinstance(data, DataTable):
            item = [data.code, data.name, data.table_type, data.area, data.peple_num, data.min_type]
            SvcTableInfo.DeleteItem(item)
            EvtManager.DispatchEvent(EnumEvent.EVT_DINING_ROOM_REFRESH)
            
    @classmethod
    def UpdateItem(cls, data):
        if isinstance(data, DataTable):
            item = [data.code, data.name, data.table_type, data.area, data.peple_num, data.min_type]
            SvcTableInfo.UpdateItem(item)
            EvtManager.DispatchEvent(EnumEvent.EVT_DINING_ROOM_REFRESH)
            
class CtrlType(Singleton):
    data_len = 0
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @classmethod
    def GetDataLen(cls):
        return CtrlType.data_len - 2
    
    @classmethod
    def GetData(cls):
        result = SvcTypeSetting.GetAll()
        data = list()
        for item in result:
            data_item = DataType(item[0], item[1], item[2])
            data.append(data_item)
            
        CtrlType.data_len = len(data)
            
        return data
    
    @classmethod
    def GetId(cls):
        return SvcTypeSetting.GetId()
    
    @classmethod
    def AddItem(cls, data):
        if isinstance(data, DataType):
            item = [data.code, data.name]
            SvcTypeSetting.AddItem(item)
            CtrlType.data_len += 1
            
    @classmethod
    def DeleteItem(cls, data):
        if isinstance(data, DataType):
            item = [data.code, data.name]
            SvcTypeSetting.DeleteItem(item)
            
    @classmethod
    def UpdateItem(cls, data):
        if isinstance(data, DataType):
            item = [data.code, data.name]
            SvcTypeSetting.UpdateItem(item)

class CtrlCategory(Singleton):
    data_len = 0
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @classmethod
    def GetDataLen(cls):
        return CtrlCategory.data_len - 2
    
    @classmethod
    def GetData(cls):
        result = SvcCategorySetting.GetAll()
        data = list()
        for item in result:
            data_item = DataCategory(item[0], item[1], item[2])
            data.append(data_item)
            
        CtrlCategory.data_len = len(data)
            
        return data
    
    @classmethod
    def GetId(cls):
        return SvcCategorySetting.GetId()
    
    @classmethod
    def AddItem(cls, data):
        if isinstance(data, DataCategory):
            item = [data.code, data.name]
            SvcCategorySetting.AddItem(item)
            CtrlCategory.data_len += 1
            
    @classmethod
    def DeleteItem(cls, data):
        if isinstance(data, DataCategory):
            item = [data.code, data.name]
            SvcCategorySetting.DeleteItem(item)
            
    @classmethod
    def UpdateItem(cls, data):
        if isinstance(data, DataCategory):
            item = [data.code, data.name]
            SvcCategorySetting.UpdateItem(item)
            
class CtrlDishes(Singleton):
    cur_item_index = 0
    cur_list_data = None
    table_items = list()
    
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @classmethod
    def GetCurItemIndex(cls):
        return CtrlDishes.cur_item_index
    
    @classmethod
    def SetCurItemIndex(cls, index):
        CtrlDishes.cur_item_index = index
        
    @classmethod
    def SetCurItemIndex2(cls, item):
        CtrlDishes.cur_item_index = CtrlDishes.table_items.index(item)
    
    @classmethod
    def SetCurListData(cls, data):
        CtrlDishes.cur_list_data = data
    
    @classmethod
    def GetCurListData(cls):
        return CtrlDishes.cur_list_data
    
    @classmethod
    def GetData(cls):
        result = SvcDishesInfo.GetAll()
        data = list()
        for item in result:
            data_item = DataDishes(item[0], item[1], item[2], item[3], item[4], item[5], 
                                    item[6], item[7], item[8], item[9], item[10], item[11], 
                                    item[12], item[13], item[14])
            data.append(data_item)
            
        return data
    
    @classmethod
    def RefreshItems(cls):
        del CtrlDishes.table_items[0:len(CtrlDishes.table_items)]
        result = SvcDishesInfo.GetItems()
        for item in result:
            data_item = DataDishes(item[0], item[1], item[2], item[3], item[4], item[5], 
                                    item[6], item[7], item[8], item[9], item[10], item[11],
                                    item[12], item[13], item[14])
            CtrlDishes.table_items.append(data_item)
            
    @classmethod
    def GetItems(cls):            
        return CtrlDishes.table_items
    
    @classmethod
    def AddItem(cls, data):
        if isinstance(data, DataDishes):
            item = [data.code, data.name, data.spell, data.spec, data.category, data.price, data.unit, 
                    data.style, data.commistion, data.discount, data.stop, data.image_url]
            SvcDishesInfo.AddItem(item)
            EvtManager.DispatchEvent(type.EVT_DISHES_PUBLISH_REFRESH)        
            
    @classmethod
    def DeleteItem(cls, data):
        if isinstance(data, DataDishes):
            item = [data.id, data.code, data.name]
            SvcDishesInfo.DeleteItem(item)
            EvtManager.DispatchEvent(type.EVT_DISHES_PUBLISH_REFRESH)
            
    @classmethod
    def UpdateItem(cls, data):
        if isinstance(data, DataDishes):
            item = [data.id, data.code, data.name, data.spell, data.spec, data.category, data.price, data.unit, 
                    data.style, data.commistion, data.discount, data.stop, data.image_url]
            SvcDishesInfo.UpdateItem(item)
            EvtManager.DispatchEvent(type.EVT_DISHES_PUBLISH_REFRESH)
            
    @classmethod        
    def UpdatePrinterScheme(cls, data):
        if isinstance(data, DataDishes):
            item = [data.id, data.printer_scheme]
            SvcDishesInfo.UpdatePrinterScheme(item)
            EvtManager.DispatchEvent(type.EVT_DISHES_PUBLISH_REFRESH)
            
class CtrlSpec(Singleton):
    data_len = 0
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @classmethod
    def GetDataLen(cls):
        return CtrlSpec.data_len - 2
    
    @classmethod
    def GetData(cls):
        result = SvcDishSpec.GetAll()
        data = list()
        for item in result:
            data_item = DataSpec(item[0], item[1], item[2])
            data.append(data_item)
            
        CtrlSpec.data_len = len(data)
            
        return data
    
    @classmethod
    def GetId(cls):
        return SvcDishSpec.GetId()
    
    @classmethod
    def AddItem(cls, data):
        if isinstance(data, DataSpec):
            item = [data.code, data.name, data.price]
            SvcDishSpec.AddItem(item)
            CtrlSpec.data_len += 1
            
    @classmethod
    def DeleteItem(cls, data):
        if isinstance(data, DataSpec):
            item = [data.code, data.name]
            SvcDishSpec.DeleteItem(item)
            
    @classmethod
    def UpdateItem(cls, data):
        if isinstance(data, DataSpec):
            item = [data.code, data.name, data.price]
            SvcDishSpec.UpdateItem(item)

class CtrlStyle(Singleton):
    data_len = 0
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @classmethod
    def GetDataLen(cls):
        return CtrlStyle.data_len - 2
    
    @classmethod
    def GetData(cls):
        result = SvcDishStyle.GetAll()
        data = list()
        for item in result:
            data_item = DataStyle(item[0], item[1], item[2], item[3])
            data.append(data_item)
            
        CtrlStyle.data_len = len(data)
            
        return data
    
    @classmethod
    def GetId(cls):
        return SvcDishStyle.GetId()
    
    @classmethod
    def AddItem(cls, data):
        if isinstance(data, DataStyle):
            item = [data.code, data.name, data.price_add, data.amount_add]
            SvcDishStyle.AddItem(item)
            CtrlStyle.data_len += 1
            
    @classmethod
    def DeleteItem(cls, data):
        if isinstance(data, DataStyle):
            item = [data.code, data.name]
            SvcDishStyle.DeleteItem(item)
            
    @classmethod
    def UpdateItem(cls, data):
        if isinstance(data, DataStyle):
            item = [data.code, data.name, data.price_add, data.amount_add]
            SvcDishStyle.UpdateItem(item)

class CtrlUnit(Singleton):
    data_len = 0
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @classmethod
    def GetDataLen(cls):
        return CtrlUnit.data_len - 2
    
    @classmethod
    def GetData(cls):
        result = SvcUnitSetting.GetAll()
        data = list()
        for item in result:
            data_item = DataUnit(item[0], item[1], item[2])
            data.append(data_item)
            
        CtrlUnit.data_len = len(data)
            
        return data
    
    @classmethod
    def GetId(cls):
        return SvcUnitSetting.GetId()
    
    @classmethod
    def AddItem(cls, data):
        if isinstance(data, DataUnit):
            item = [data.code, data.name]
            SvcUnitSetting.AddItem(item)
            CtrlUnit.data_len += 1
            
    @classmethod
    def DeleteItem(cls, data):
        if isinstance(data, DataUnit):
            item = [data.code, data.name]
            SvcUnitSetting.DeleteItem(item)
            
    @classmethod
    def UpdateItem(cls, data):
        if isinstance(data, DataUnit):
            item = [data.code, data.name]
            SvcUnitSetting.UpdateItem(item)

class CtrlDepartment(Singleton):
    data_len = 0
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @classmethod
    def GetDataLen(cls):
        return CtrlDepartment.data_len - 2
    
    @classmethod
    def GetData(cls):
        result = SvcDepartment.GetAll()
        data = list()
        for item in result:
            data_item = DataDepartment(item[0], item[1], item[2])
            data.append(data_item)
            
        CtrlDepartment.data_len = len(data)
            
        return data
    
    @classmethod
    def GetId(cls):
        return SvcDepartment.GetId()
    
    @classmethod
    def AddItem(cls, data):
        if isinstance(data, DataDepartment):
            item = [data.code, data.name]
            SvcDepartment.AddItem(item)
            CtrlDepartment.data_len += 1
            
    @classmethod
    def DeleteItem(cls, data):
        if isinstance(data, DataDepartment):
            item = [data.code, data.name]
            SvcDepartment.DeleteItem(item)
            
    @classmethod
    def UpdateItem(cls, data):
        if isinstance(data, DataDepartment):
            item = [data.code, data.name]
            SvcDepartment.UpdateItem(item)

class CtrlEmployee(Singleton):
    cur_item_index = 0
    table_items = list()
    
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @classmethod
    def GetCurItemIndex(cls):
        return CtrlEmployee.cur_item_index
    
    @classmethod
    def SetCurItemIndex(cls, index):
        CtrlEmployee.cur_item_index = index
    
    @classmethod
    def GetData(cls):
        result = SvcEmployee.GetAll()
        data = list()
        for item in result:
            data_item = DataEmployee(item[0], item[1], item[2], item[3], item[4], item[5], item[6],
                                      item[7], item[8], item[9], item[10], item[11], item[12], item[13])
            data.append(data_item)
            
        return data
    
    @classmethod
    def RefreshItems(cls):
        del CtrlEmployee.table_items[0:len(CtrlEmployee.table_items)]
        result = SvcEmployee.GetItems()
        for item in result:
            data_item = DataEmployee(item[0], item[1], item[2], item[3], item[4], item[5], item[6],
                                      item[7], item[8], item[9], item[10], item[11], item[12], item[13])
            CtrlEmployee.table_items.append(data_item)
            
    @classmethod
    def GetItems(cls):            
        return CtrlEmployee.table_items
    
    @classmethod
    def AddItem(cls, data):
        if isinstance(data, DataEmployee):
            item = [data.code, data.name, data.birthday, data.duty, data.department, data.sex,
                    data.telephone, data.id_card, data.state, data.addr, data.email, data.note]
            SvcEmployee.AddItem(item)
            EvtManager.DispatchEvent(type.EVT_EMPLOYEE_REFRESH)      
            
    @classmethod
    def DeleteItem(cls, data):
        if isinstance(data, DataEmployee):
            item = [data.id, data.code, data.name]
            SvcEmployee.DeleteItem(item)
            EvtManager.DispatchEvent(type.EVT_EMPLOYEE_REFRESH)
            
    @classmethod
    def UpdateItem(cls, data):
        if isinstance(data, DataEmployee):
            item = [data.id, data.code, data.name, data.birthday, data.duty, data.department, data.sex,
                    data.telephone, data.id_card, data.state, data.addr, data.email, data.note]
            SvcEmployee.UpdateItem(item)
            EvtManager.DispatchEvent(type.EVT_EMPLOYEE_REFRESH)
            
class CtrlUserRole(Singleton):
    data_len = 0
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @classmethod
    def GetDataLen(cls):
        return CtrlUserRole.data_len - 2
    
    @classmethod
    def GetData(cls):
        result = SvcUserRole.GetAll()
        data = list()
        for item in result:
            data_item = DataUserRole(item[0], item[1], item[2], item[3])
            data.append(data_item)
            
        CtrlUserRole.data_len = len(data)
            
        return data
    
    @classmethod
    def GetId(cls):
        return SvcUserRole.GetId()
    
    @classmethod
    def AddItem(cls, data):
        if isinstance(data, DataUserRole):
            item = [data.id, data.code, data.name]
            SvcUserRole.AddItem(item)
            CtrlUserRole.data_len += 1
            
    @classmethod
    def DeleteItem(cls, data):
        if isinstance(data, DataUserRole):
            item = [data.id, data.code, data.name]
            SvcUserRole.DeleteItem(item)
            
    @classmethod
    def UpdateItem(cls, data):
        if isinstance(data, DataUserRole):
            item = [data.id, data.code, data.name]
            SvcUserRole.UpdateItem(item)

class CtrlLogin(Singleton):
    chechResult = False
    
    def __init__(self):
        pass
    
    def __def__(self):
        pass
    
    def Login(self, strUser, strPasswd):
        if strUser == '0000' and strPasswd == '0000':
            self.chechResult = True
            
        EvtManager.DispatchEvent(EnumEvent.EVT_LOGIN)
        
    def GetResult(self):
        return self.chechResult
    
class CtrlPrinterScheme(Singleton):
    cur_item_index = 0
    table_items = list()
    
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @classmethod
    def GetCurItemIndex(cls):
        return CtrlPrinterScheme.cur_item_index
    
    @classmethod
    def SetCurItemIndex(cls, index):
        CtrlPrinterScheme.cur_item_index = index
    
    @classmethod
    def GetData(cls):
        result = SvcPrinterScheme.GetAll()
        data = list()
        for item in result:
            data_item = DataPrinterScheme(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            data.append(data_item)
            
        return data
    
    @classmethod
    def RefreshItems(cls):
        del CtrlPrinterScheme.table_items[0:len(CtrlPrinterScheme.table_items)]
        result = SvcPrinterScheme.GetItems()
        for item in result:
            data_item = DataPrinterScheme(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            CtrlPrinterScheme.table_items.append(data_item)
            
    @classmethod
    def GetItems(cls):            
        return CtrlPrinterScheme.table_items
    
    @classmethod
    def AddItem(cls, data):
        if isinstance(data, DataPrinterScheme):
            item = [data.code, data.name, data.valid, data.scheme_type, data.print_count, data.backup]
            SvcPrinterScheme.AddItem(item)
            EvtManager.DispatchEvent(type.EVT_PRINTER_SCHEME_REFRESH)       
            
    @classmethod
    def DeleteItem(cls, data):
        if isinstance(data, DataPrinterScheme):
            item = [data.code, data.name]
            SvcPrinterScheme.DeleteItem(item)
            EvtManager.DispatchEvent(type.EVT_PRINTER_SCHEME_REFRESH)
            
    @classmethod
    def UpdateItem(cls, data):
        if isinstance(data, DataPrinterScheme):
            item = [data.code, data.name, data.valid, data.scheme_type, data.print_count, data.backup]
            SvcPrinterScheme.UpdateItem(item)
            EvtManager.DispatchEvent(type.EVT_PRINTER_SCHEME_REFRESH)
            
class CtrlSchemeType(Singleton):
    data_len = 0
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
    
    @classmethod
    def GetDataLen(cls):
        return CtrlSchemeType.data_len - 2
    
    @classmethod
    def GetData(cls):
        result = SvcSchemeType.GetAll()
        data = list()
        for item in result:
            data_item = DataSchemeType(item[0], item[1], item[2])
            data.append(data_item)
            
        CtrlSchemeType.data_len = len(data)
            
        return data
    
    @classmethod
    def GetId(cls):
        return SvcSchemeType.GetId()
    
    @classmethod
    def AddItem(cls, data):
        if isinstance(data, DataSchemeType):
            item = [data.code, data.name]
            SvcSchemeType.AddItem(item)
            CtrlSchemeType.data_len += 1
            
    @classmethod
    def DeleteItem(cls, data):
        if isinstance(data, DataSchemeType):
            item = [data.code, data.name]
            SvcSchemeType.DeleteItem(item)
            
    @classmethod
    def UpdateItem(cls, data):
        if isinstance(data, DataSchemeType):
            item = [data.code, data.name]
            SvcSchemeType.UpdateItem(item)