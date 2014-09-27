#!/usr/bin/env python
#_*_ encoding=utf-8 _*_
from framework.core import EvtManager
from app.manager.logic.data import *
from service.data_base.manager import *
from app.manager.EnumEvent import EnumEvent


class CtrlHomePage(Singleton):
    m_frame_width = 800
    m_frame_height = 600
    m_selected_item = 5
    
    def __init__(self):
        pass
    
    def __def__(self):
        pass

    @classmethod
    def get_screen_size(cls):
        return CtrlHomePage.m_frame_width, CtrlHomePage.m_frame_height
    
    @classmethod
    def set_screen_size(cls, x, y):
        CtrlHomePage.m_frame_width = x
        CtrlHomePage.m_frame_height = y
        
    @classmethod
    def get_selected_item(cls):
        return CtrlHomePage.m_selected_item
    
    @classmethod
    def set_selected_item(cls, item=5):
        # 0 for dining room setting
        # 1 for dishes publishing
        # 2 for employee manager
        # 3 for printer setting
        # 4 for report form manager
        # 5 for system setting
        CtrlHomePage.m_selected_item = item


class CtrlArea(Singleton):
    data_len = 0

    def __init__(self):
        pass
    
    @classmethod
    def get_data_len(cls):
        return CtrlArea.data_len - 2
    
    @classmethod
    def get_data(cls):
        result = SvcAreaSetting.get_all()
        data = list()
        for item in result:
            data_item = DataArea(item[0], item[1], item[2])
            data.append(data_item)
            
        CtrlArea.data_len = len(data)
            
        return data
    
    @classmethod
    def get_id(cls):
        return SvcAreaSetting.get_id()
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataArea):
            item = [data.code, data.name]
            SvcAreaSetting.add_item(item)
            CtrlArea.data_len += 1
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataArea):
            item = [data.code, data.name]
            SvcAreaSetting.delete_item(item)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataArea):
            item = [data.code, data.name]
            SvcAreaSetting.update_item(item)


class CtrlMinExpense(Singleton):
    data_len = 0

    def __init__(self):
        pass
    
    @classmethod
    def get_data_len(cls):
        return CtrlMinExpense.data_len - 2
    
    @classmethod
    def get_data(cls):
        result = SvcMinExpenseSetting.get_all()
        data = list()
        for item in result:
            data_item = DataMinExpense(item[0], item[1], item[2], item[3])
            data.append(data_item)
            
        CtrlMinExpense.data_len = len(data)
            
        return data
    
    @classmethod
    def get_id(cls):
        return SvcMinExpenseSetting.get_id()
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataMinExpense):
            item = [data.code, data.name, data.price]
            SvcMinExpenseSetting.add_item(item)
            CtrlMinExpense.data_len += 1
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataMinExpense):
            item = [data.code, data.name, data.price]
            SvcMinExpenseSetting.delete_item(item)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataMinExpense):
            item = [data.code, data.name, data.price]
            SvcMinExpenseSetting.update_item(item)


class CtrlTable(Singleton):
    cur_item_index = 0
    table_items = list()
    
    def __init__(self):
        pass
    
    @classmethod
    def get_cur_item_index(cls):
        return CtrlTable.cur_item_index
    
    @classmethod
    def set_cur_item_index(cls, index):
        CtrlTable.cur_item_index = index
    
    @classmethod
    def get_data(cls):
        result = SvcTableInfo.get_all()
        data = list()
        for item in result:
            data_item = DataTable(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            data.append(data_item)
            
        return data
    
    @classmethod
    def refresh_items(cls):
        del CtrlTable.table_items[0:len(CtrlTable.table_items)]
        result = SvcTableInfo.get_items()
        for item in result:
            data_item = DataTable(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            CtrlTable.table_items.append(data_item)
            
    @classmethod
    def get_items(cls):
        return CtrlTable.table_items
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataTable):
            item = [data.code, data.name, data.table_type, data.area, data.people_num, data.min_type]
            SvcTableInfo.add_item(item)
            EvtManager.dispatch_event(EnumEvent.EVT_DINING_ROOM_REFRESH)
    
    @classmethod      
    def add_items(cls, data):
        for obj in data:
            if isinstance(obj, DataTable):
                item = [obj.code, obj.name, obj.table_type, obj.area, obj.people_num, obj.min_type]
                SvcTableInfo.add_item(item)
        EvtManager.dispatch_event(EnumEvent.EVT_DINING_ROOM_REFRESH)
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataTable):
            item = [data.code, data.name, data.table_type, data.area, data.people_num, data.min_type]
            SvcTableInfo.delete_item(item)
            EvtManager.dispatch_event(EnumEvent.EVT_DINING_ROOM_REFRESH)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataTable):
            item = [data.code, data.name, data.table_type, data.area, data.people_num, data.min_type]
            SvcTableInfo.update_item(item)
            EvtManager.dispatch_event(EnumEvent.EVT_DINING_ROOM_REFRESH)


class CtrlType(Singleton):
    data_len = 0

    def __init__(self):
        pass
    
    @classmethod
    def get_data_len(cls):
        return CtrlType.data_len - 2
    
    @classmethod
    def get_data(cls):
        result = SvcTypeSetting.get_all()
        data = list()
        for item in result:
            data_item = DataType(item[0], item[1], item[2])
            data.append(data_item)
            
        CtrlType.data_len = len(data)
            
        return data
    
    @classmethod
    def get_id(cls):
        return SvcTypeSetting.get_id()
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataType):
            item = [data.code, data.name]
            SvcTypeSetting.add_item(item)
            CtrlType.data_len += 1
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataType):
            item = [data.code, data.name]
            SvcTypeSetting.delete_item(item)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataType):
            item = [data.code, data.name]
            SvcTypeSetting.update_item(item)


class CtrlCategory(Singleton):
    data_len = 0

    def __init__(self):
        pass
    
    @classmethod
    def get_data_len(cls):
        return CtrlCategory.data_len - 2
    
    @classmethod
    def get_data(cls):
        result = SvcCategorySetting.get_all()
        data = list()
        for item in result:
            data_item = DataCategory(item[0], item[1], item[2])
            data.append(data_item)
            
        CtrlCategory.data_len = len(data)
            
        return data
    
    @classmethod
    def get_id(cls):
        return SvcCategorySetting.get_id()
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataCategory):
            item = [data.code, data.name]
            SvcCategorySetting.add_item(item)
            CtrlCategory.data_len += 1
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataCategory):
            item = [data.code, data.name]
            SvcCategorySetting.delete_item(item)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataCategory):
            item = [data.code, data.name]
            SvcCategorySetting.update_item(item)


class CtrlDishes(Singleton):
    cur_item_index = 0
    cur_list_data = None
    table_items = list()
    
    def __init__(self):
        pass
    
    @classmethod
    def get_cur_item_index(cls):
        return CtrlDishes.cur_item_index
    
    @classmethod
    def set_cur_item_index(cls, index):
        CtrlDishes.cur_item_index = index
        
    @classmethod
    def get_cur_item_index_2(cls, item):
        CtrlDishes.cur_item_index = CtrlDishes.table_items.index(item)
    
    @classmethod
    def set_cur_list_data(cls, data):
        CtrlDishes.cur_list_data = data
    
    @classmethod
    def get_cur_list_data(cls):
        return CtrlDishes.cur_list_data
    
    @classmethod
    def get_data(cls):
        result = SvcDishesInfo.get_all()
        data = list()
        for item in result:
            data_item = DataDishes(item[0], item[1], item[2], item[3], item[4], item[5], 
                                   item[6], item[7], item[8], item[9], item[10], item[11],
                                   item[12], item[13], item[14])
            data.append(data_item)
            
        return data
    
    @classmethod
    def refresh_items(cls):
        del CtrlDishes.table_items[0:len(CtrlDishes.table_items)]
        result = SvcDishesInfo.get_items()
        for item in result:
            data_item = DataDishes(item[0], item[1], item[2], item[3], item[4], item[5], 
                                   item[6], item[7], item[8], item[9], item[10], item[11],
                                   item[12], item[13], item[14])
            CtrlDishes.table_items.append(data_item)
            
    @classmethod
    def get_items(cls):
        return CtrlDishes.table_items
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataDishes):
            item = [data.code, data.name, data.spell, data.spec, data.category, data.price, data.unit, 
                    data.style, data.commission, data.discount, data.stop, data.image_url]
            SvcDishesInfo.add_item(item)
            EvtManager.dispatch_event(EnumEvent.EVT_DISHES_PUBLISH_REFRESH)
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataDishes):
            item = [data.id, data.code, data.name]
            SvcDishesInfo.delete_item(item)
            EvtManager.dispatch_event(EnumEvent.EVT_DISHES_PUBLISH_REFRESH)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataDishes):
            item = [data.id, data.code, data.name, data.spell, data.spec, data.category, data.price, data.unit, 
                    data.style, data.commission, data.discount, data.stop, data.image_url]
            SvcDishesInfo.update_item(item)
            EvtManager.dispatch_event(EnumEvent.EVT_DISHES_PUBLISH_REFRESH)
            
    @classmethod        
    def update_print_scheme(cls, data):
        if isinstance(data, DataDishes):
            item = [data.id, data.printer_scheme]
            SvcDishesInfo.update_print_scheme(item)
            EvtManager.dispatch_event(EnumEvent.EVT_DISHES_PUBLISH_REFRESH)


class CtrlSpec(Singleton):
    data_len = 0

    def __init__(self):
        pass
    
    @classmethod
    def get_data_len(cls):
        return CtrlSpec.data_len - 2
    
    @classmethod
    def get_data(cls):
        result = SvcDishSpec.get_all()
        data = list()
        for item in result:
            data_item = DataSpec(item[0], item[1], item[2])
            data.append(data_item)
            
        CtrlSpec.data_len = len(data)
            
        return data
    
    @classmethod
    def get_id(cls):
        return SvcDishSpec.get_id()
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataSpec):
            item = [data.code, data.name, data.price]
            SvcDishSpec.add_item(item)
            CtrlSpec.data_len += 1
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataSpec):
            item = [data.code, data.name]
            SvcDishSpec.delete_item(item)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataSpec):
            item = [data.code, data.name, data.price]
            SvcDishSpec.update_item(item)


class CtrlStyle(Singleton):
    data_len = 0

    def __init__(self):
        pass
    
    @classmethod
    def get_data_len(cls):
        return CtrlStyle.data_len - 2
    
    @classmethod
    def get_data(cls):
        result = SvcDishStyle.get_all()
        data = list()
        for item in result:
            data_item = DataStyle(item[0], item[1], item[2], item[3])
            data.append(data_item)
            
        CtrlStyle.data_len = len(data)
            
        return data
    
    @classmethod
    def get_id(cls):
        return SvcDishStyle.get_id()
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataStyle):
            item = [data.code, data.name, data.price_add, data.amount_add]
            SvcDishStyle.add_item(item)
            CtrlStyle.data_len += 1
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataStyle):
            item = [data.code, data.name]
            SvcDishStyle.delete_item(item)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataStyle):
            item = [data.code, data.name, data.price_add, data.amount_add]
            SvcDishStyle.update_item(item)


class CtrlUnit(Singleton):
    data_len = 0

    def __init__(self):
        pass
    
    @classmethod
    def get_data_len(cls):
        return CtrlUnit.data_len - 2
    
    @classmethod
    def get_data(cls):
        result = SvcUnitSetting.get_all()
        data = list()
        for item in result:
            data_item = DataUnit(item[0], item[1], item[2])
            data.append(data_item)
            
        CtrlUnit.data_len = len(data)
            
        return data
    
    @classmethod
    def get_id(cls):
        return SvcUnitSetting.get_id()
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataUnit):
            item = [data.code, data.name]
            SvcUnitSetting.add_item(item)
            CtrlUnit.data_len += 1
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataUnit):
            item = [data.code, data.name]
            SvcUnitSetting.delete_item(item)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataUnit):
            item = [data.code, data.name]
            SvcUnitSetting.update_item(item)


class CtrlDepartment(Singleton):
    data_len = 0

    def __init__(self):
        pass
    
    @classmethod
    def get_data_len(cls):
        return CtrlDepartment.data_len - 2
    
    @classmethod
    def get_data(cls):
        result = SvcDepartment.get_all()
        data = list()
        for item in result:
            data_item = DataDepartment(item[0], item[1], item[2])
            data.append(data_item)
            
        CtrlDepartment.data_len = len(data)
            
        return data
    
    @classmethod
    def get_id(cls):
        return SvcDepartment.get_id()
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataDepartment):
            item = [data.code, data.name]
            SvcDepartment.add_item(item)
            CtrlDepartment.data_len += 1
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataDepartment):
            item = [data.code, data.name]
            SvcDepartment.delete_item(item)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataDepartment):
            item = [data.code, data.name]
            SvcDepartment.update_item(item)


class CtrlEmployee(Singleton):
    cur_item_index = 0
    table_items = list()
    
    def __init__(self):
        pass
    
    @classmethod
    def get_cur_item_index(cls):
        return CtrlEmployee.cur_item_index
    
    @classmethod
    def set_cur_item_index(cls, index):
        CtrlEmployee.cur_item_index = index
    
    @classmethod
    def get_data(cls):
        result = SvcEmployee.get_all()
        data = list()
        for item in result:
            data_item = DataEmployee(item[0], item[1], item[2], item[3], item[4], item[5], item[6],
                                     item[7], item[8], item[9], item[10], item[11], item[12], item[13])
            data.append(data_item)
            
        return data
    
    @classmethod
    def refresh_items(cls):
        del CtrlEmployee.table_items[0:len(CtrlEmployee.table_items)]
        result = SvcEmployee.get_items()
        for item in result:
            data_item = DataEmployee(item[0], item[1], item[2], item[3], item[4], item[5], item[6],
                                     item[7], item[8], item[9], item[10], item[11], item[12], item[13])
            CtrlEmployee.table_items.append(data_item)
            
    @classmethod
    def get_items(cls):            
        return CtrlEmployee.table_items
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataEmployee):
            item = [data.code, data.name, data.birthday, data.duty, data.department, data.sex,
                    data.telephone, data.id_card, data.state, data.address, data.email, data.note]
            SvcEmployee.add_item(item)
            EvtManager.dispatch_event(EnumEvent.EVT_EMPLOYEE_REFRESH)
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataEmployee):
            item = [data.id, data.code, data.name]
            SvcEmployee.delete_item(item)
            EvtManager.dispatch_event(EnumEvent.EVT_EMPLOYEE_REFRESH)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataEmployee):
            item = [data.id, data.code, data.name, data.birthday, data.duty, data.department, data.sex,
                    data.telephone, data.id_card, data.state, data.address, data.email, data.note]
            SvcEmployee.update_item(item)
            EvtManager.dispatch_event(EnumEvent.EVT_EMPLOYEE_REFRESH)


class CtrlUserRole(Singleton):
    data_len = 0
    
    def __init__(self):
        pass
    
    @classmethod
    def get_data_len(cls):
        return CtrlUserRole.data_len - 2
    
    @classmethod
    def get_data(cls):
        result = SvcUserRole.get_all()
        data = list()
        for item in result:
            data_item = DataUserRole(item[0], item[1], item[2], item[3])
            data.append(data_item)
            
        CtrlUserRole.data_len = len(data)
            
        return data
    
    @classmethod
    def get_id(cls):
        return SvcUserRole.get_id()
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataUserRole):
            item = [data.id, data.code, data.name]
            SvcUserRole.add_item(item)
            CtrlUserRole.data_len += 1
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataUserRole):
            item = [data.id, data.code, data.name]
            SvcUserRole.delete_item(item)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataUserRole):
            item = [data.id, data.code, data.name]
            SvcUserRole.update_item(item)


class CtrlLogin(Singleton):
    check_result = False
    
    def __init__(self):
        pass
    
    def __def__(self):
        pass
    
    def login(self, user, password):
        if user == '0000' and password == '0000':
            self.check_result = True
            
        EvtManager.dispatch_event(EnumEvent.EVT_LOGIN)
        
    def get_result(self):
        return self.check_result


class CtrlPrinterScheme(Singleton):
    cur_item_index = 0
    table_items = list()
    
    def __init__(self):
        pass

    @classmethod
    def get_cur_item_index(cls):
        return CtrlPrinterScheme.cur_item_index
    
    @classmethod
    def set_cur_item_index(cls, index):
        CtrlPrinterScheme.cur_item_index = index
    
    @classmethod
    def get_data(cls):
        result = SvcPrinterScheme.get_all()
        data = list()
        for item in result:
            data_item = DataPrinterScheme(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            data.append(data_item)
            
        return data
    
    @classmethod
    def refresh_items(cls):
        del CtrlPrinterScheme.table_items[0:len(CtrlPrinterScheme.table_items)]
        result = SvcPrinterScheme.get_items()
        for item in result:
            data_item = DataPrinterScheme(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            CtrlPrinterScheme.table_items.append(data_item)
            
    @classmethod
    def get_items(cls):            
        return CtrlPrinterScheme.table_items
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataPrinterScheme):
            item = [data.code, data.name, data.valid, data.scheme_type, data.print_count, data.backup]
            SvcPrinterScheme.add_item(item)
            EvtManager.dispatch_event(EnumEvent.EVT_PRINTER_SCHEME_REFRESH)
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataPrinterScheme):
            item = [data.code, data.name]
            SvcPrinterScheme.delete_item(item)
            EvtManager.dispatch_event(EnumEvent.EVT_PRINTER_SCHEME_REFRESH)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataPrinterScheme):
            item = [data.code, data.name, data.valid, data.scheme_type, data.print_count, data.backup]
            SvcPrinterScheme.update_item(item)
            EvtManager.dispatch_event(EnumEvent.EVT_PRINTER_SCHEME_REFRESH)


class CtrlSchemeType(Singleton):
    data_len = 0

    def __init__(self):
        pass
    
    @classmethod
    def get_data_len(cls):
        return CtrlSchemeType.data_len - 2
    
    @classmethod
    def get_data(cls):
        result = SvcSchemeType.get_all()
        data = list()
        for item in result:
            data_item = DataSchemeType(item[0], item[1], item[2])
            data.append(data_item)
            
        CtrlSchemeType.data_len = len(data)
            
        return data
    
    @classmethod
    def get_id(cls):
        return SvcSchemeType.get_id()
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataSchemeType):
            item = [data.code, data.name]
            SvcSchemeType.add_item(item)
            CtrlSchemeType.data_len += 1
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataSchemeType):
            item = [data.code, data.name]
            SvcSchemeType.delete_item(item)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataSchemeType):
            item = [data.code, data.name]
            SvcSchemeType.update_item(item)