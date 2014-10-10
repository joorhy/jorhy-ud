#!/usr/bin/env python
#_*_ encoding=utf-8 _*_
from framework.core import EvtManager
from app.manager.logic.data import *
from app.manager.EnumEvent import EnumEvent
from service.data_base.manager import *


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
        result = get_all('AreaInfo')
        data = list()
        for item in result:
            data.append(DataArea(result.index(item) + 1, item.id_, item.name))
            
        CtrlArea.data_len = len(data)
            
        return data
    
    @classmethod
    def get_id(cls):
        return get_id('AreaInfo')
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataArea):
            add_item('AreaInfo', data)
            CtrlArea.data_len += 1
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataArea):
            delete_item('AreaInfo', data)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataArea):
            update_item('AreaInfo', data)


class CtrlMinExpense():
    data_len = 0

    def __init__(self):
        pass
    
    @classmethod
    def get_data_len(cls):
        return CtrlMinExpense.data_len - 2
    
    @classmethod
    def get_data(cls):
        result = get_all('MinExpenseInfo')
        data = list()
        for item in result:
            data_item = DataMinExpense(result.index(item) + 1, item.id_, item.name, item.min_price)
            data.append(data_item)
            
        CtrlMinExpense.data_len = len(data)
            
        return data
    
    @classmethod
    def get_id(cls):
        return get_id('MinExpenseInfo')
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataMinExpense):
            add_item('MinExpenseInfo', data)
            CtrlMinExpense.data_len += 1
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataMinExpense):
            delete_item('MinExpenseInfo', data)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataMinExpense):
            update_item('MinExpenseInfo', data)


class CtrlTable():
    cur_item_index = 0
    table_items = list()
    
    def __init__(self):
        pass
    
    @classmethod
    def get_cur_item_index(cls):
        return CtrlTable.cur_item_index
    
    @classmethod
    def set_cur_item_index(cls, index_):
        CtrlTable.cur_item_index = index_
    
    @classmethod
    def get_data(cls):
        result = get_all('TableInfo')
        data = list()
        for item in result:
            data_item = DataTable(result.index(item) + 1, item.id_, item.name, item.type_name,
                                  item.area_name, item.people_num, item.expense_name)
            data.append(data_item)
            
        return data
    
    @classmethod
    def refresh_items(cls):
        del CtrlTable.table_items[0:len(CtrlTable.table_items)]
        result = get_all('TableInfo')
        for item in result:
            data_item = DataTable(result.index(item) + 1, item.id_, item.name, item.type_id,
                                  item.area_id, item.people_num, item.expense_id)
            CtrlTable.table_items.append(data_item)
            
    @classmethod
    def get_items(cls):
        return CtrlTable.table_items
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataTable):
            add_item('TableInfo', data)
            EvtManager.dispatch_event(EnumEvent.EVT_DINING_ROOM_REFRESH)
    
    @classmethod      
    def add_items(cls, li_data):
        for data in li_data:
            if isinstance(data, DataTable):
                add_item('TableInfo', data)
        EvtManager.dispatch_event(EnumEvent.EVT_DINING_ROOM_REFRESH)
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataTable):
            delete_item('TableInfo', data)
            EvtManager.dispatch_event(EnumEvent.EVT_DINING_ROOM_REFRESH)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataTable):
            update_item('TableInfo', data)
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
        result = get_all('TableTypeInfo')
        data = list()
        for item in result:
            data.append(DataType(result.index(item) + 1, item.id_, item.name))
            
        CtrlType.data_len = len(data)
            
        return data
    
    @classmethod
    def get_id(cls):
        return get_id('TableTypeInfo')
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataType):
            add_item('TableTypeInfo', data)
            CtrlType.data_len += 1
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataType):
            delete_item('TableTypeInfo', data)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataType):
            update_item('TableTypeInfo', data)


class CtrlCategory():
    data_len = 0

    def __init__(self):
        pass
    
    @classmethod
    def get_data_len(cls):
        return CtrlCategory.data_len - 2
    
    @classmethod
    def get_data(cls):
        result = get_all('CategoryInfo')
        data = list()
        for item in result:
            data.append(DataCategory(result.index(item) + 1, item.id_, item.name))
            
        CtrlCategory.data_len = len(data)
            
        return data
    
    @classmethod
    def get_id(cls):
        return get_id('CategoryInfo')
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataCategory):
            add_item('CategoryInfo', data)
            CtrlCategory.data_len += 1
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataCategory):
            delete_item('CategoryInfo', data)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataCategory):
            update_item('CategoryInfo', data)


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
    def set_cur_item_index(cls, index_):
        CtrlDishes.cur_item_index = index_
        
    @classmethod
    def set_cur_item_index_2(cls, item):
        CtrlDishes.cur_item_index = CtrlDishes.table_items.index(item)
    
    @classmethod
    def set_cur_list_data(cls, data):
        CtrlDishes.cur_list_data = data
    
    @classmethod
    def get_cur_list_data(cls):
        return CtrlDishes.cur_list_data
    
    @classmethod
    def get_data(cls):
        result = get_all('DishInfo')
        data = list()
        for item in result:
            data_item = DataDishes(result.index(item) + 1, item.id_, item.code, item.name, item.brevity,
                                   item.category_name, item.unit_name, item.commission, item.discount, item.enable,
                                   item.picture_url, item.print_scheme_name, item.is_print)
            data.append(data_item)
            
        return data
    
    @classmethod
    def refresh_items(cls):
        del CtrlDishes.table_items[0:len(CtrlDishes.table_items)]
        result = get_all('DishInfo')
        for item in result:
            data_item = DataDishes(result.index(item) + 1, item.id_, item.code, item.name, item.brevity,
                                   item.category_id, item.unit_id, item.commission, item.discount, item.enable,
                                   item.picture_url, item.print_scheme_id, item.is_print)
            CtrlDishes.table_items.append(data_item)
            
    @classmethod
    def get_items(cls):
        return CtrlDishes.table_items
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataDishes):
            add_item('DishInfo', data)
            EvtManager.dispatch_event(EnumEvent.EVT_DISHES_PUBLISH_REFRESH)
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataDishes):
            delete_item('DishInfo', data)
            EvtManager.dispatch_event(EnumEvent.EVT_DISHES_PUBLISH_REFRESH)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataDishes):
            update_item('DishInfo', data)
            EvtManager.dispatch_event(EnumEvent.EVT_DISHES_PUBLISH_REFRESH)
            
    @classmethod        
    def update_print_scheme(cls, data):
        if isinstance(data, DataDishes):
            update_print_scheme(data)
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
        result = get_all('SpecInfo')
        data = list()
        for item in result:
            data_item = DataSpec(result.index(item) + 1, item.id_, item.dish_code, item.name, item.price)
            data.append(data_item)
            
        CtrlSpec.data_len = len(data)
            
        return data

    @classmethod
    def get_data_by_dish_code(cls, dish_code):
        result = get_spec_by_dish_code(dish_code)
        data = list()
        for item in result:
            data_item = DataSpec(result.index(item) + 1, item.id_, item.dish_code, item.name, item.price)
            data.append(data_item)

        CtrlSpec.data_len = len(data)

        return data
    
    @classmethod
    def get_id(cls):
        return get_id('SpecInfo')
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataSpec):
            add_item('SpecInfo', data)
            CtrlSpec.data_len += 1
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataSpec):
            delete_item('SpecInfo', data)

    @classmethod
    def delete_item_by_dish_code(cls, dish_code):
        delete_spec_by_dish_code(dish_code)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataSpec):
            update_item('SpecInfo', data)


class CtrlStyle():
    data_len = 0

    def __init__(self):
        pass
    
    @classmethod
    def get_data_len(cls):
        return CtrlStyle.data_len - 2
    
    @classmethod
    def get_data(cls):
        result = get_all('StyleInfo')
        data = list()
        for item in result:
            data.append(DataStyle(result.index(item) + 1, item.id_, item.dish_code,
                                  item.name, item.price, item.is_add_price))
            
        CtrlStyle.data_len = len(data)
            
        return data

    @classmethod
    def get_data_by_dish_code(cls, dish_code):
        result = get_style_by_dish_code(dish_code)
        data = list()
        for item in result:
            data.append(DataStyle(result.index(item) + 1, item.id_, item.dish_code,
                                  item.name, item.price, item.is_add_price))

        CtrlStyle.data_len = len(data)

        return data
    
    @classmethod
    def get_id(cls):
        return get_id('StyleInfo')
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataStyle):
            add_item('StyleInfo', data)
            CtrlStyle.data_len += 1
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataStyle):
            delete_item('StyleInfo', data)

    @classmethod
    def delete_item_by_dish_code(cls, dish_code):
        delete_style_by_dish_code(dish_code)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataStyle):
            update_item('StyleInfo', data)


class CtrlUnit():
    data_len = 0

    def __init__(self):
        pass
    
    @classmethod
    def get_data_len(cls):
        return CtrlUnit.data_len - 2
    
    @classmethod
    def get_data(cls):
        result = get_all('UnitInfo')
        data = list()
        for item in result:
            data_item = DataUnit(result.index(item) + 1, item.id_, item.name)
            data.append(data_item)
            
        CtrlUnit.data_len = len(data)
            
        return data
    
    @classmethod
    def get_id(cls):
        return get_id('UnitInfo')
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataUnit):
            add_item('UnitInfo', data)
            CtrlUnit.data_len += 1
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataUnit):
            delete_item('UnitInfo', data)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataUnit):
            update_item('UnitInfo', data)


class CtrlDepartment():
    data_len = 0

    def __init__(self):
        pass
    
    @classmethod
    def get_data_len(cls):
        return CtrlDepartment.data_len - 2
    
    @classmethod
    def get_data(cls):
        result = get_all('DepartmentInfo')
        data = list()
        for item in result:
            data.append(DataDepartment(result.index(item) + 1, item.id_, item.name))
            
        CtrlDepartment.data_len = len(data)
            
        return data
    
    @classmethod
    def get_id(cls):
        return get_id('DepartmentInfo')
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataDepartment):
            add_item('DepartmentInfo', data)
            CtrlDepartment.data_len += 1
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataDepartment):
            delete_item('DepartmentInfo', data)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataDepartment):
            update_item('DepartmentInfo', data)


class CtrlEmployee():
    cur_item_index = 0
    table_items = list()
    
    def __init__(self):
        pass
    
    @classmethod
    def get_cur_item_index(cls):
        return CtrlEmployee.cur_item_index
    
    @classmethod
    def set_cur_item_index(cls, index_):
        CtrlEmployee.cur_item_index = index_
    
    @classmethod
    def get_data(cls):
        result = get_all('EmployeeInfo')
        data = list()
        for item in result:
            data_item = DataEmployee(result.index(item) + 1, item.id_, item.code, item.name, item.birthday,
                                     item.duty, item.dept_name, item.gender, item.telephone, item.id_card,
                                     item.status, item.address, item.email, item.memo)
            data.append(data_item)
            
        return data
    
    @classmethod
    def refresh_items(cls):
        del CtrlEmployee.table_items[0:len(CtrlEmployee.table_items)]
        result = get_all('EmployeeInfo')
        for item in result:
            data_item = DataEmployee(result.index(item) + 1, item.id_, item.code, item.name, item.birthday,
                                     item.duty, item.dept_id, item.gender, item.telephone, item.id_card,
                                     item.status, item.address, item.email, item.memo)
            CtrlEmployee.table_items.append(data_item)
            
    @classmethod
    def get_items(cls):            
        return CtrlEmployee.table_items
    
    @classmethod
    def add_item(cls, data, group_list):
        if isinstance(data, DataEmployee):
            add_user_info(data, group_list)
            EvtManager.dispatch_event(EnumEvent.EVT_EMPLOYEE_REFRESH)
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataEmployee):
            delete_item('EmployeeInfo', data)
            EvtManager.dispatch_event(EnumEvent.EVT_EMPLOYEE_REFRESH)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataEmployee):
            update_item('EmployeeInfo', data)
            EvtManager.dispatch_event(EnumEvent.EVT_EMPLOYEE_REFRESH)


class CtrlUserRole():
    data_len = 0
    cur_item_index = 0
    table_items = list()
    
    def __init__(self):
        pass

    @classmethod
    def get_cur_item_index(cls):
        return CtrlEmployee.cur_item_index

    @classmethod
    def set_cur_item_index(cls, index_):
        CtrlEmployee.cur_item_index = index_

    @classmethod
    def get_data_len(cls):
        return CtrlUserRole.data_len - 2
    
    @classmethod
    def get_data(cls):
        result = get_all('RoleInfo')
        data = list()
        for item in result:
            data.append(DataUserRole(result.index(item) + 1, item.id_, item.type, item.name, item.desc, item.selected))
            
        CtrlUserRole.data_len = len(data)
            
        return data

    @classmethod
    def get_data_by_user(cls, user):
        result = get_group_by_user(user)
        data = list()
        for item in result:
            data.append(DataUserRole(result.index(item) + 1, item.id_, item.type, item.name, item.desc, item.selected))

        CtrlUserRole.data_len = len(data)

        return data

    @classmethod
    def refresh_items(cls):
        del CtrlTable.table_items[0:len(CtrlTable.table_items)]
        result = get_all('RoleInfo')
        for item in result:
            data_item = DataUserRole(result.index(item) + 1, item.id_, item.type, item.name, item.desc, item.selected)
            CtrlUserRole.table_items.append(data_item)
    
    @classmethod
    def get_id(cls):
        return get_id('RoleInfo')
    
    @classmethod
    def add_item(cls, data, perm_list):
        if isinstance(data, DataUserRole):
            add_role_info(data, perm_list)
            CtrlUserRole.data_len += 1
            EvtManager.dispatch_event(EnumEvent.EVT_PERMISSION_REFRESH)
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataUserRole):
            delete_item('RoleInfo', data)
            EvtManager.dispatch_event(EnumEvent.EVT_PERMISSION_REFRESH)
            
    @classmethod
    def update_item(cls, data, perm_list):
        if isinstance(data, DataUserRole):
            update_role_info(data, perm_list)
            EvtManager.dispatch_event(EnumEvent.EVT_PERMISSION_REFRESH)


class CtrlLogin():
    check_result = False
    
    def __init__(self):
        pass

    @classmethod
    def login(cls, user, password):
        try:
            if user == 'admin' and password == 'admin':
                cls.check_result = True
            elif get_password_by_user_name(user) == password:
                cls.check_result = True
        except:
            cls.check_result = False
            
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
    def set_cur_item_index(cls, index_):
        CtrlPrinterScheme.cur_item_index = index_
    
    @classmethod
    def get_data(cls):
        result = get_all('PrintSchemeInfo')
        data = list()
        for item in result:
            data_item = DataPrinterScheme(result.index(item) + 1, item.id_, item.code, item.name, item.valid,
                                          item.type_name, item.count, item.backup_id)
            data.append(data_item)
            
        return data
    
    @classmethod
    def refresh_items(cls):
        del CtrlPrinterScheme.table_items[0:len(CtrlPrinterScheme.table_items)]
        result = get_all('PrintSchemeInfo')
        for item in result:
            data_item = DataPrinterScheme(result.index(item) + 1, item.id_, item.code, item.name, item.valid,
                                          item.type_id, item.count, item.backup_id)
            CtrlPrinterScheme.table_items.append(data_item)
            
    @classmethod
    def get_items(cls):            
        return CtrlPrinterScheme.table_items
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataPrinterScheme):
            add_item('PrintSchemeInfo', data)
            EvtManager.dispatch_event(EnumEvent.EVT_PRINTER_SCHEME_REFRESH)
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataPrinterScheme):
            delete_item('PrintSchemeInfo', data)
            EvtManager.dispatch_event(EnumEvent.EVT_PRINTER_SCHEME_REFRESH)
            
    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataPrinterScheme):
            update_item('PrintSchemeInfo', data)
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
        result = get_all('SchemeTypeInfo')
        data = list()
        for item in result:
            data.append(DataSchemeType(result.index(item) + 1, item.id_, item.name))
            
        CtrlSchemeType.data_len = len(data)
            
        return data
    
    @classmethod
    def get_id(cls):
        return get_id('SchemeTypeInfo')
    
    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataSchemeType):
            add_item('SchemeTypeInfo', data)
            CtrlSchemeType.data_len += 1
            
    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataSchemeType):
            delete_item('SchemeTypeInfo', data)

    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataSchemeType):
            update_item('SchemeTypeInfo', data)


class CtrlPermList():
    data_len = 0

    def __init__(self):
        pass

    @classmethod
    def get_data_len(cls):
        return CtrlPermList.data_len - 2

    @classmethod
    def get_data(cls):
        result = get_all('PermList')
        data = list()
        for item in result:
            data.append(DataPermList(result.index(item) + 1, item.id_, item.code,
                                     item.p_code, item.name, item.selected))

        CtrlPermList.data_len = len(data)

        return data

    @classmethod
    def get_data_by_group(cls, group):
        result = get_perm_by_group(group)
        data = list()
        for item in result:
            data.append(DataPermList(result.index(item) + 1, item.id_, item.code,
                                     item.p_code, item.name, item.selected))

        CtrlPermList.data_len = len(data)

        return data

    @classmethod
    def get_id(cls):
        return get_id('PermList')

    @classmethod
    def add_item(cls, data):
        if isinstance(data, DataType):
            add_item('PermList', data)
            CtrlPermList.data_len += 1

    @classmethod
    def delete_item(cls, data):
        if isinstance(data, DataType):
            delete_item('PermList', data)

    @classmethod
    def update_item(cls, data):
        if isinstance(data, DataType):
            update_item('PermList', data)
