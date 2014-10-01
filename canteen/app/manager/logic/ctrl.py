#!/usr/bin/env python
#_*_ encoding=utf-8 _*_
from framework.core import EvtManager
from app.manager.logic.data import *
from service.data_base.manager import *
from app.manager.EnumEvent import EnumEvent


class CtrlHomePage():
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


class CtrlArea():
    data_len = 0

    def __init__(self):
        pass
    
    @classmethod
    def get_data_len(cls):
        return CtrlArea.data_len - 2
    
    @classmethod
    def get_data(cls):
        svc_obj = SvcCanteenInfo('AreaInfo')
        result = svc_obj.get_all()
        data = list()
        for item in result:
            data.append(DataArea(result.index(item), item.id_, item.name))
            
        CtrlArea.data_len = len(data)
            
        return data
    
    @classmethod
    def get_id(cls):
        svc_obj = SvcCanteenInfo('AreaInfo')
        return svc_obj.get_id()
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataArea):
            svc_obj = SvcCanteenInfo('AreaInfo')
            svc_obj.add_item(data)
            CtrlArea.data_len += 1
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataArea):
            svc_obj = SvcCanteenInfo('AreaInfo')
            svc_obj.delete_item(data)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataArea):
            svc_obj = SvcCanteenInfo('AreaInfo')
            svc_obj.update_item(data)


class CtrlMinExpense():
    data_len = 0

    def __init__(self):
        pass
    
    @classmethod
    def get_data_len(cls):
        return CtrlMinExpense.data_len - 2
    
    @classmethod
    def get_data(cls):
        svc_obj = SvcCanteenInfo('MinExpenseInfo')
        result = svc_obj.get_all()
        data = list()
        for item in result:
            data_item = DataMinExpense(result.index(item), item.id_, item.name, item.min_price)
            data.append(data_item)
            
        CtrlMinExpense.data_len = len(data)
            
        return data
    
    @classmethod
    def get_id(cls):
        svc_obj = SvcCanteenInfo('MinExpenseInfo')
        return svc_obj.get_id()
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataMinExpense):
            svc_obj = SvcCanteenInfo('MinExpenseInfo')
            svc_obj.add_item(data)
            CtrlMinExpense.data_len += 1
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataMinExpense):
            svc_obj = SvcCanteenInfo('MinExpenseInfo')
            svc_obj.delete_item(data)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataMinExpense):
            svc_obj = SvcCanteenInfo('MinExpenseInfo')
            svc_obj.update_item(data)


class CtrlTable():
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
        svc_obj = SvcCanteenInfo('TableInfo')
        result = svc_obj.get_all()
        data = list()
        for item in result:
            data_item = DataTable(result.index(item), item.id_, item.name, item.type_name,
                                  item.area_name, item.people_num, item.expense_name)
            data.append(data_item)
            
        return data
    
    @classmethod
    def refresh_items(cls):
        del CtrlTable.table_items[0:len(CtrlTable.table_items)]
        svc_obj = SvcCanteenInfo('TableInfo')
        result = svc_obj.get_all()
        for item in result:
            data_item = DataTable(result.index(item), item.id_, item.name, item.type_id,
                                  item.area_id, item.people_num, item.expense_id)
            CtrlTable.table_items.append(data_item)
            
    @classmethod
    def get_items(cls):
        return CtrlTable.table_items
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataTable):
            svc_obj = SvcCanteenInfo('TableInfo')
            svc_obj.add_item(data)
            EvtManager.dispatch_event(EnumEvent.EVT_DINING_ROOM_REFRESH)
    
    @classmethod      
    def add_items(cls, data):
        for obj in data:
            if isinstance(obj, DataTable):
                svc_obj = SvcCanteenInfo('TableInfo')
                svc_obj.add_item(data)
        EvtManager.dispatch_event(EnumEvent.EVT_DINING_ROOM_REFRESH)
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataTable):
            svc_obj = SvcCanteenInfo('TableInfo')
            svc_obj.delete_item(data)
            EvtManager.dispatch_event(EnumEvent.EVT_DINING_ROOM_REFRESH)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataTable):
            svc_obj = SvcCanteenInfo('TableInfo')
            svc_obj.update_item(data)
            EvtManager.dispatch_event(EnumEvent.EVT_DINING_ROOM_REFRESH)


class CtrlType():
    data_len = 0

    def __init__(self):
        pass
    
    @classmethod
    def get_data_len(cls):
        return CtrlType.data_len - 2
    
    @classmethod
    def get_data(cls):
        svc_obj = SvcCanteenInfo('TableTypeInfo')
        result = svc_obj.get_all()
        data = list()
        for item in result:
            data.append(DataType(result.index(item), item.id_, item.name))
            
        CtrlType.data_len = len(data)
            
        return data
    
    @classmethod
    def get_id(cls):
        svc_obj = SvcCanteenInfo('TableTypeInfo')
        return svc_obj.get_id()
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataType):
            svc_obj = SvcCanteenInfo('TableTypeInfo')
            svc_obj.add_item(data)
            CtrlType.data_len += 1
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataType):
            svc_obj = SvcCanteenInfo('TableTypeInfo')
            svc_obj.delete_item(data)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataType):
            svc_obj = SvcCanteenInfo('TableTypeInfo')
            svc_obj.update_item(data)


class CtrlCategory():
    data_len = 0

    def __init__(self):
        pass
    
    @classmethod
    def get_data_len(cls):
        return CtrlCategory.data_len - 2
    
    @classmethod
    def get_data(cls):
        svc_obj = SvcCanteenInfo('CategoryInfo')
        result = svc_obj.get_all()
        data = list()
        for item in result:
            data.append(DataCategory(result.index(item), item.id_, item.name))
            
        CtrlCategory.data_len = len(data)
            
        return data
    
    @classmethod
    def get_id(cls):
        svc_obj = SvcCanteenInfo('CategoryInfo')
        return svc_obj.get_id()
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataCategory):
            svc_obj = SvcCanteenInfo('CategoryInfo')
            svc_obj.add_item(data)
            CtrlCategory.data_len += 1
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataCategory):
            svc_obj = SvcCanteenInfo('CategoryInfo')
            svc_obj.delete_item(data)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataCategory):
            svc_obj = SvcCanteenInfo('CategoryInfo')
            svc_obj.update_item(data)


class CtrlDishes():
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
        svc_obj = SvcCanteenInfo('DishInfo')
        result = svc_obj.get_all()
        data = list()
        for item in result:
            data_item = DataDishes(result.index(item), item.id_, item.code, item.name, item.brevity,
                                   item.spec_name, item.category_name, item.default_price, item.unit_name,
                                   item.style_name, item.commission, item.discount, item.enable,
                                   item.picture_url, item.print_scheme_name)
            data.append(data_item)
            
        return data
    
    @classmethod
    def refresh_items(cls):
        del CtrlDishes.table_items[0:len(CtrlDishes.table_items)]
        svc_obj = SvcCanteenInfo('DishInfo')
        result = svc_obj.get_all()
        for item in result:
            data_item = DataDishes(result.index(item), item.id_, item.code, item.name, item.brevity,
                                   item.spec_id, item.category_id, item.default_price, item.unit_id,
                                   item.style_id, item.commission, item.discount, item.enable,
                                   item.picture_url, item.print_scheme_id)
            CtrlDishes.table_items.append(data_item)
            
    @classmethod
    def get_items(cls):
        return CtrlDishes.table_items
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataDishes):
            svc_obj = SvcCanteenInfo('DishInfo')
            svc_obj.add_item(data)
            EvtManager.dispatch_event(EnumEvent.EVT_DISHES_PUBLISH_REFRESH)
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataDishes):
            svc_obj = SvcCanteenInfo('DishInfo')
            svc_obj.delete_item(data)
            EvtManager.dispatch_event(EnumEvent.EVT_DISHES_PUBLISH_REFRESH)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataDishes):
            svc_obj = SvcCanteenInfo('DishInfo')
            svc_obj.update_item(data)
            EvtManager.dispatch_event(EnumEvent.EVT_DISHES_PUBLISH_REFRESH)
            
    @classmethod        
    def update_print_scheme(cls, data):
        if isinstance(data, DataDishes):
            svc_obj = SvcPrintScheme()
            svc_obj.update_print_scheme(data)
            EvtManager.dispatch_event(EnumEvent.EVT_DISHES_PUBLISH_REFRESH)


class CtrlSpec():
    data_len = 0

    def __init__(self):
        pass
    
    @classmethod
    def get_data_len(cls):
        return CtrlSpec.data_len - 2
    
    @classmethod
    def get_data(cls):
        svc_obj = SvcCanteenInfo('SpecInfo')
        result = svc_obj.get_all()
        data = list()
        for item in result:
            data_item = DataSpec(result.index(item), item.id_, item.name)
            data.append(data_item)
            
        CtrlSpec.data_len = len(data)
            
        return data
    
    @classmethod
    def get_id(cls):
        svc_obj = SvcCanteenInfo('SpecInfo')
        return svc_obj.get_id()
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataSpec):
            svc_obj = SvcCanteenInfo('SpecInfo')
            svc_obj.add_item(data)
            CtrlSpec.data_len += 1
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataSpec):
            svc_obj = SvcCanteenInfo('SpecInfo')
            svc_obj.delete_item(data)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataSpec):
            svc_obj = SvcCanteenInfo('SpecInfo')
            svc_obj.update_item(data)


class CtrlStyle():
    data_len = 0

    def __init__(self):
        pass
    
    @classmethod
    def get_data_len(cls):
        return CtrlStyle.data_len - 2
    
    @classmethod
    def get_data(cls):
        svc_obj = SvcCanteenInfo('StyleInfo')
        result = svc_obj.get_all()
        data = list()
        for item in result:
            data.append(DataStyle(result.index(item), item.id_, item.name, item.is_add_price))
            
        CtrlStyle.data_len = len(data)
            
        return data
    
    @classmethod
    def get_id(cls):
        svc_obj = SvcCanteenInfo('StyleInfo')
        return svc_obj.get_id()
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataStyle):
            svc_obj = SvcCanteenInfo('StyleInfo')
            svc_obj.add_item(data)
            CtrlStyle.data_len += 1
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataStyle):
            svc_obj = SvcCanteenInfo('StyleInfo')
            svc_obj.delete_item(data)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataStyle):
            svc_obj = SvcCanteenInfo('StyleInfo')
            svc_obj.update_item(data)


class CtrlUnit():
    data_len = 0

    def __init__(self):
        pass
    
    @classmethod
    def get_data_len(cls):
        return CtrlUnit.data_len - 2
    
    @classmethod
    def get_data(cls):
        svc_obj = SvcCanteenInfo('UnitInfo')
        result = svc_obj.get_all()
        data = list()
        for item in result:
            data_item = DataUnit(result.index(item), item.id_, item.name)
            data.append(data_item)
            
        CtrlUnit.data_len = len(data)
            
        return data
    
    @classmethod
    def get_id(cls):
        svc_obj = SvcCanteenInfo('UnitInfo')
        return svc_obj.get_id()
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataUnit):
            svc_obj = SvcCanteenInfo('UnitInfo')
            svc_obj.add_item(data)
            CtrlUnit.data_len += 1
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataUnit):
            svc_obj = SvcCanteenInfo('UnitInfo')
            svc_obj.delete_item(data)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataUnit):
            svc_obj = SvcCanteenInfo('UnitInfo')
            svc_obj.update_item(data)


class CtrlDepartment():
    data_len = 0

    def __init__(self):
        pass
    
    @classmethod
    def get_data_len(cls):
        return CtrlDepartment.data_len - 2
    
    @classmethod
    def get_data(cls):
        svc_obj = SvcCanteenInfo('DepartmentInfo')
        result = svc_obj.get_all()
        data = list()
        for item in result:
            data.append(DataDepartment(result.index(item), item.id_, item.name))
            
        CtrlDepartment.data_len = len(data)
            
        return data
    
    @classmethod
    def get_id(cls):
        svc_obj = SvcCanteenInfo('DepartmentInfo')
        return svc_obj.get_id()
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataDepartment):
            svc_obj = SvcCanteenInfo('DepartmentInfo')
            svc_obj.add_item(data)
            CtrlDepartment.data_len += 1
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataDepartment):
            svc_obj = SvcCanteenInfo('DepartmentInfo')
            svc_obj.delete_item(data)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataDepartment):
            svc_obj = SvcCanteenInfo('DepartmentInfo')
            svc_obj.update_item(data)


class CtrlEmployee():
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
        svc_obj = SvcCanteenInfo('EmployeeInfo')
        result = svc_obj.get_all()
        data = list()
        for item in result:
            data_item = DataEmployee(item.id_, result.index(item), item.code, item.name, item.birthday,
                                     item.duty, item.dept_name, item.gender, item.telephone, item.id_card,
                                     item.status, item.address, item.email, item.memo)
            data.append(data_item)
            
        return data
    
    @classmethod
    def refresh_items(cls):
        del CtrlEmployee.table_items[0:len(CtrlEmployee.table_items)]
        svc_obj = SvcCanteenInfo('EmployeeInfo')
        result = svc_obj.get_all()
        for item in result:
            data_item = DataEmployee(item.id_, result.index(item), item.code, item.name, item.birthday,
                                     item.duty, item.dept_id, item.gender, item.telephone, item.id_card,
                                     item.status, item.address, item.email, item.memo)
            CtrlEmployee.table_items.append(data_item)
            
    @classmethod
    def get_items(cls):            
        return CtrlEmployee.table_items
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataEmployee):
            svc_obj = SvcCanteenInfo('EmployeeInfo')
            svc_obj.add_item(data)
            EvtManager.dispatch_event(EnumEvent.EVT_EMPLOYEE_REFRESH)
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataEmployee):
            svc_obj = SvcCanteenInfo('EmployeeInfo')
            svc_obj.delete_item(data)
            EvtManager.dispatch_event(EnumEvent.EVT_EMPLOYEE_REFRESH)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataEmployee):
            svc_obj = SvcCanteenInfo('EmployeeInfo')
            svc_obj.update_item(data)
            EvtManager.dispatch_event(EnumEvent.EVT_EMPLOYEE_REFRESH)


class CtrlUserRole():
    data_len = 0
    
    def __init__(self):
        pass
    
    @classmethod
    def get_data_len(cls):
        return CtrlUserRole.data_len - 2
    
    @classmethod
    def get_data(cls):
        svc_obj = SvcCanteenInfo('RoleInfo')
        result = svc_obj.get_all()
        data = list()
        for item in result:
            data.append(DataUserRole(result.index(item), item.id_, item.code, item.name))
            
        CtrlUserRole.data_len = len(data)
            
        return data
    
    @classmethod
    def get_id(cls):
        svc_obj = SvcCanteenInfo('RoleInfo')
        return svc_obj.get_id()
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataUserRole):
            svc_obj = SvcCanteenInfo('RoleInfo')
            svc_obj.add_item(data)
            CtrlUserRole.data_len += 1
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataUserRole):
            svc_obj = SvcCanteenInfo('RoleInfo')
            svc_obj.delete_item(data)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataUserRole):
            svc_obj = SvcCanteenInfo('RoleInfo')
            svc_obj.update_item(data)


class CtrlLogin():
    check_result = False
    
    def __init__(self):
        pass

    @classmethod
    def login(cls, user, password):
        if user == '0000' and password == '0000':
            cls.check_result = True
            
        EvtManager.dispatch_event(EnumEvent.EVT_LOGIN)

    @classmethod
    def get_result(cls):
        return cls.check_result


class CtrlPrinterScheme():
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
        svc_obj = SvcCanteenInfo('PrintSchemeInfo')
        result = svc_obj.get_all()
        data = list()
        for item in result:
            data_item = DataPrinterScheme(result.index(item), item.id_, item.name, item.valid,
                                          item.type_name, item.count, item.backup_id)
            data.append(data_item)
            
        return data
    
    @classmethod
    def refresh_items(cls):
        del CtrlPrinterScheme.table_items[0:len(CtrlPrinterScheme.table_items)]
        svc_obj = SvcCanteenInfo('PrintSchemeInfo')
        result = svc_obj.get_all()
        for item in result:
            data_item = DataPrinterScheme(result.index(item), item.id_, item.name, item.valid,
                                          item.type_id, item.count, item.backup_id)
            CtrlPrinterScheme.table_items.append(data_item)
            
    @classmethod
    def get_items(cls):            
        return CtrlPrinterScheme.table_items
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataPrinterScheme):
            svc_obj = SvcCanteenInfo('PrintSchemeInfo')
            svc_obj.add_item(data)
            EvtManager.dispatch_event(EnumEvent.EVT_PRINTER_SCHEME_REFRESH)
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataPrinterScheme):
            svc_obj = SvcCanteenInfo('PrintSchemeInfo')
            svc_obj.delete_item(data)
            EvtManager.dispatch_event(EnumEvent.EVT_PRINTER_SCHEME_REFRESH)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataPrinterScheme):
            svc_obj = SvcCanteenInfo('PrintSchemeInfo')
            svc_obj.update_item(data)
            EvtManager.dispatch_event(EnumEvent.EVT_PRINTER_SCHEME_REFRESH)


class CtrlSchemeType():
    data_len = 0

    def __init__(self):
        pass
    
    @classmethod
    def get_data_len(cls):
        return CtrlSchemeType.data_len - 2
    
    @classmethod
    def get_data(cls):
        svc_obj = SvcCanteenInfo('SchemeTypeInfo')
        result = svc_obj.get_all()
        data = list()
        for item in result:
            data.append(DataSchemeType(result.index(item), item.id_, item.name))
            
        CtrlSchemeType.data_len = len(data)
            
        return data
    
    @classmethod
    def get_id(cls):
        svc_obj = SvcCanteenInfo('SchemeTypeInfo')
        return svc_obj.get_id()
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataSchemeType):
            svc_obj = SvcCanteenInfo('SchemeTypeInfo')
            svc_obj.add_item(data)
            CtrlSchemeType.data_len += 1
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataSchemeType):
            svc_obj = SvcCanteenInfo('SchemeTypeInfo')
            svc_obj.delete_item(data)

    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataSchemeType):
            svc_obj = SvcCanteenInfo('SchemeTypeInfo')
            svc_obj.update_item(data)