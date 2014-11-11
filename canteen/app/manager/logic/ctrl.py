#!/usr/bin/env python
#_*_ encoding=utf-8 _*_
from framework.core import EvtManager, Singleton
from app.manager.logic.data import *
from app.enum_event import EnumEvent
from service.data_base.manager import *


@Singleton
class CtrlManagerLogin():
    def __init__(self):
        self.check_result = False
        self.user = '0000'
        self.password = '0000'
        self.img_path = ''

    def initialize(self, user, password, img_path):
        self.user = user
        self.password = password
        self.img_path = img_path

    def login(self, user, password):
        try:
            if user == self.user and password == self.password:
                self.check_result = True
            elif get_password_by_user_name(user) == password:
                self.check_result = True
        except:
            self.check_result = False

        EvtManager.dispatch_event(EnumEvent.EVT_LOGIN)

    def get_result(self):
        return self.check_result

    def get_image_path(self):
        return self.img_path


@Singleton
class CtrlArea():
    def __init__(self):
        self.data_len = 0

    def get_data_len(self):
        return self.data_len - 2

    def get_data(self):
        result = get_all('AreaInfo')
        data = list()
        for item in result:
            data.append(DataArea(result.index(item) + 1, item.id_, item.name))
            
        self.data_len = len(data)
            
        return data

    @staticmethod
    def get_id():
        return get_id('AreaInfo')

    def add_item(self, data):
        if isinstance(data, DataArea):
            add_item('AreaInfo', data)
            self.data_len += 1
            
    @staticmethod
    def delete_item(data):
        if isinstance(data, DataArea):
            delete_item('AreaInfo', data)
            
    @staticmethod
    def update_item(data):
        if isinstance(data, DataArea):
            update_item('AreaInfo', data)


@Singleton
class CtrlMinExpense():
    def __init__(self):
        self.data_len = 0

    def get_data_len(self):
        return self.data_len - 2

    def get_data(self):
        result = get_all('MinExpenseInfo')
        data = list()
        for item in result:
            data_item = DataMinExpense(result.index(item) + 1, item.id_, item.name, item.min_price)
            data.append(data_item)
            
        self.data_len = len(data)
            
        return data
    
    @staticmethod
    def get_id():
        return get_id('MinExpenseInfo')

    def add_item(self, data):
        if isinstance(data, DataMinExpense):
            add_item('MinExpenseInfo', data)
            self.data_len += 1
            
    @staticmethod
    def delete_item(data):
        if isinstance(data, DataMinExpense):
            delete_item('MinExpenseInfo', data)
            
    @staticmethod
    def update_item(data):
        if isinstance(data, DataMinExpense):
            update_item('MinExpenseInfo', data)


@Singleton
class CtrlTable():
    def __init__(self):
        self.cur_item_index = 0
        self.table_items = list()

    def get_cur_item_index(self):
        return self.cur_item_index

    def set_cur_item_index(self, index_):
        self.cur_item_index = index_
    
    @staticmethod
    def get_data():
        result = get_all('TableInfo')
        data = list()
        for item in result:
            data_item = DataTable(result.index(item) + 1, item.id_, item.name, item.type_name,
                                  item.area_name, item.people_num, item.expense_name)
            data.append(data_item)
            
        return data

    def refresh_items(self):
        del self.table_items[0:len(self.table_items)]
        result = get_all('TableInfo')
        for item in result:
            data_item = DataTable(result.index(item) + 1, item.id_, item.name, item.type_id,
                                  item.area_id, item.people_num, item.expense_id)
            self.table_items.append(data_item)

    def get_items(self):
        return self.table_items
    
    @staticmethod
    def add_item(data):
        if isinstance(data, DataTable):
            add_item('TableInfo', data)
            EvtManager.dispatch_event(EnumEvent.EVT_DINING_ROOM_REFRESH)
    
    @staticmethod
    def add_items(li_data):
        for data in li_data:
            if isinstance(data, DataTable):
                add_item('TableInfo', data)
        EvtManager.dispatch_event(EnumEvent.EVT_DINING_ROOM_REFRESH)
            
    @staticmethod
    def delete_item(data):
        if isinstance(data, DataTable):
            delete_item('TableInfo', data)
            EvtManager.dispatch_event(EnumEvent.EVT_DINING_ROOM_REFRESH)
            
    @staticmethod
    def update_item(data):
        if isinstance(data, DataTable):
            update_item('TableInfo', data)
            EvtManager.dispatch_event(EnumEvent.EVT_DINING_ROOM_REFRESH)


@Singleton
class CtrlType():
    def __init__(self):
        self.data_len = 0

    def get_data_len(self):
        return self.data_len - 2

    def get_data(self):
        result = get_all('TableTypeInfo')
        data = list()
        for item in result:
            data.append(DataType(result.index(item) + 1, item.id_, item.name))
            
        self.data_len = len(data)
            
        return data
    
    @staticmethod
    def get_id():
        return get_id('TableTypeInfo')

    def add_item(self, data):
        if isinstance(data, DataType):
            add_item('TableTypeInfo', data)
            self.data_len += 1
            
    @staticmethod
    def delete_item(data):
        if isinstance(data, DataType):
            delete_item('TableTypeInfo', data)
            
    @staticmethod
    def update_item(data):
        if isinstance(data, DataType):
            update_item('TableTypeInfo', data)


@Singleton
class CtrlCategory():
    def __init__(self):
        self.data_len = 0

    def get_data_len(self):
        return self.data_len - 2

    def get_data(self):
        result = get_all('CategoryInfo')
        data = list()
        for item in result:
            data.append(DataCategory(result.index(item) + 1, item.id_, item.name))
            
        self.data_len = len(data)
            
        return data
    
    @staticmethod
    def get_id():
        return get_id('CategoryInfo')

    def add_item(self, data):
        if isinstance(data, DataCategory):
            add_item('CategoryInfo', data)
            self.data_len += 1
            
    @staticmethod
    def delete_item(data):
        if isinstance(data, DataCategory):
            delete_item('CategoryInfo', data)
            
    @staticmethod
    def update_item(data):
        if isinstance(data, DataCategory):
            update_item('CategoryInfo', data)


@Singleton
class CtrlDishes():
    def __init__(self):
        self.cur_item_index = 0
        self.cur_list_data = None
        self.table_items = list()

    def get_cur_item_index(self):
        return self.cur_item_index

    def set_cur_item_index(self, index_):
        self.cur_item_index = index_

    def set_cur_item_index_2(self, item):
        self.cur_item_index = self.table_items.index(item)

    def set_cur_list_data(self, data):
        self.cur_list_data = data

    def get_cur_list_data(self):
        return self.cur_list_data
    
    @staticmethod
    def get_data():
        result = get_all('DishInfo')
        data = list()
        for item in result:
            data_item = DataDishes(result.index(item) + 1, item.id_, item.code, item.name, item.brevity,
                                   item.category_name, item.unit_name, item.commission, item.discount, item.enable,
                                   item.picture_url, item.print_scheme_name, item.is_print)
            data.append(data_item)
            
        return data

    def refresh_items(self):
        del self.table_items[0:len(self.table_items)]
        result = get_all('DishInfo')
        for item in result:
            data_item = DataDishes(result.index(item) + 1, item.id_, item.code, item.name, item.brevity,
                                   item.category_id, item.unit_id, item.commission, item.discount, item.enable,
                                   item.picture_url, item.print_scheme_id, item.is_print)
            self.table_items.append(data_item)

    def get_items(self):
        return self.table_items
    
    @staticmethod
    def add_item(data):
        if isinstance(data, DataDishes):
            add_item('DishInfo', data)
            EvtManager.dispatch_event(EnumEvent.EVT_DISHES_PUBLISH_REFRESH)
            
    @staticmethod
    def delete_item(data):
        if isinstance(data, DataDishes):
            delete_item('DishInfo', data)
            EvtManager.dispatch_event(EnumEvent.EVT_DISHES_PUBLISH_REFRESH)
            
    @staticmethod
    def update_item(data):
        if isinstance(data, DataDishes):
            update_item('DishInfo', data)
            EvtManager.dispatch_event(EnumEvent.EVT_DISHES_PUBLISH_REFRESH)
            
    @staticmethod
    def update_print_scheme(data):
        if isinstance(data, DataDishes):
            update_print_scheme(data)
            EvtManager.dispatch_event(EnumEvent.EVT_DISHES_PUBLISH_REFRESH)


@Singleton
class CtrlSpec():
    def __init__(self):
        self.data_len = 0

    def get_data_len(self):
        return self.data_len - 2

    def get_data(self):
        result = get_all('SpecInfo')
        data = list()
        for item in result:
            data_item = DataSpec(result.index(item) + 1, item.id_, item.dish_code, item.name, item.price)
            data.append(data_item)
            
        self.data_len = len(data)
            
        return data

    def get_data_by_dish_code(self, dish_code):
        result = get_spec_by_dish_code(dish_code)
        data = list()
        for item in result:
            data_item = DataSpec(result.index(item) + 1, item.id_, item.dish_code, item.name, item.price)
            data.append(data_item)

        self.data_len = len(data)

        return data
    
    @staticmethod
    def get_id():
        return get_id('SpecInfo')

    def add_item(self, data):
        if isinstance(data, DataSpec):
            add_item('SpecInfo', data)
            self.data_len += 1
            
    @staticmethod
    def delete_item(data):
        if isinstance(data, DataSpec):
            delete_item('SpecInfo', data)

    @staticmethod
    def delete_item_by_dish_code(dish_code):
        delete_spec_by_dish_code(dish_code)
            
    @staticmethod
    def update_item(data):
        if isinstance(data, DataSpec):
            update_item('SpecInfo', data)

    @staticmethod
    def has_spec(spec_id):
        return is_has_spec(spec_id)


@Singleton
class CtrlStyle():
    def __init__(self):
        self.data_len = 0

    def get_data_len(self):
        return self.data_len - 2

    def get_data(self):
        result = get_all('StyleInfo')
        data = list()
        for item in result:
            data.append(DataStyle(result.index(item) + 1, item.id_, item.dish_code,
                                  item.name, item.price, item.is_add_price))
            
        self.data_len = len(data)
            
        return data

    def get_data_by_dish_code(self, dish_code):
        result = get_style_by_dish_code(dish_code)
        data = list()
        for item in result:
            data.append(DataStyle(result.index(item) + 1, item.id_, item.dish_code,
                                  item.name, item.price, item.is_add_price))

        self.data_len = len(data)

        return data
    
    @staticmethod
    def get_id():
        return get_id('StyleInfo')

    def add_item(self, data):
        if isinstance(data, DataStyle):
            add_item('StyleInfo', data)
            self.data_len += 1
            
    @staticmethod
    def delete_item(data):
        if isinstance(data, DataStyle):
            delete_item('StyleInfo', data)

    @staticmethod
    def delete_item_by_dish_code(dish_code):
        delete_style_by_dish_code(dish_code)
            
    @staticmethod
    def update_item(data):
        if isinstance(data, DataStyle):
            update_item('StyleInfo', data)

    @staticmethod
    def has_style(style_id):
        return is_has_style(style_id)


@Singleton
class CtrlUnit():
    def __init__(self):
        self.data_len = 0

    def get_data_len(self):
        return self.data_len - 2

    def get_data(self):
        result = get_all('UnitInfo')
        data = list()
        for item in result:
            data_item = DataUnit(result.index(item) + 1, item.id_, item.name)
            data.append(data_item)
            
        self.data_len = len(data)
            
        return data
    
    @staticmethod
    def get_id():
        return get_id('UnitInfo')

    def add_item(self, data):
        if isinstance(data, DataUnit):
            add_item('UnitInfo', data)
            self.data_len += 1
            
    @staticmethod
    def delete_item(data):
        if isinstance(data, DataUnit):
            delete_item('UnitInfo', data)
            
    @staticmethod
    def update_item(data):
        if isinstance(data, DataUnit):
            update_item('UnitInfo', data)


@Singleton
class CtrlDepartment():
    def __init__(self):
        self.data_len = 0

    def get_data_len(self):
        return self.data_len - 2

    def get_data(self):
        result = get_all('DepartmentInfo')
        data = list()
        for item in result:
            data.append(DataDepartment(result.index(item) + 1, item.id_, item.name))
            
        self.data_len = len(data)
            
        return data
    
    @staticmethod
    def get_id():
        return get_id('DepartmentInfo')

    def add_item(self, data):
        if isinstance(data, DataDepartment):
            add_item('DepartmentInfo', data)
            self.data_len += 1
            
    @staticmethod
    def delete_item(data):
        if isinstance(data, DataDepartment):
            delete_item('DepartmentInfo', data)
            
    @staticmethod
    def update_item(data):
        if isinstance(data, DataDepartment):
            update_item('DepartmentInfo', data)


@Singleton
class CtrlEmployee():
    def __init__(self):
        self.cur_item_index = 0
        self.table_items = list()

    def get_cur_item_index(self):
        return self.cur_item_index

    def set_cur_item_index(self, index_):
        self.cur_item_index = index_
    
    @staticmethod
    def get_data():
        result = get_all('EmployeeInfo')
        data = list()
        for item in result:
            data_item = DataEmployee(result.index(item) + 1, item.id_, item.code, item.name, item.birthday,
                                     item.duty, item.dept_name, item.gender, item.telephone, item.id_card,
                                     item.status, item.address, item.email, item.memo)
            data.append(data_item)
            
        return data

    def refresh_items(self):
        del self.table_items[0:len(self.table_items)]
        result = get_all('EmployeeInfo')
        for item in result:
            data_item = DataEmployee(result.index(item) + 1, item.id_, item.code, item.name, item.birthday,
                                     item.duty, item.dept_id, item.gender, item.telephone, item.id_card,
                                     item.status, item.address, item.email, item.memo)
            self.table_items.append(data_item)

    def get_items(self):
        return self.table_items
    
    @staticmethod
    def add_item(data, group_list):
        if isinstance(data, DataEmployee):
            add_user_info(data, group_list)
            EvtManager.dispatch_event(EnumEvent.EVT_EMPLOYEE_REFRESH)
            
    @staticmethod
    def delete_item(data):
        if isinstance(data, DataEmployee):
            delete_item('EmployeeInfo', data)
            EvtManager.dispatch_event(EnumEvent.EVT_EMPLOYEE_REFRESH)
            
    @staticmethod
    def update_item(data):
        if isinstance(data, DataEmployee):
            update_item('EmployeeInfo', data)
            EvtManager.dispatch_event(EnumEvent.EVT_EMPLOYEE_REFRESH)


@Singleton
class CtrlUserRole():
    def __init__(self):
        self.data_len = 0
        self.cur_item_index = 0
        self.table_items = list()

    def get_cur_item_index(self):
        return self.cur_item_index

    def set_cur_item_index(self, index_):
        self.cur_item_index = index_

    def get_data_len(self):
        return self.data_len - 2

    def get_data(self):
        result = get_all('RoleInfo')
        data = list()
        for item in result:
            data.append(DataUserRole(result.index(item) + 1, item.id_, item.type, item.name, item.desc, item.selected))
            
        self.data_len = len(data)
            
        return data

    def get_data_by_user(self, user):
        result = get_group_by_user(user)
        data = list()
        for item in result:
            data.append(DataUserRole(result.index(item) + 1, item.id_, item.type, item.name, item.desc, item.selected))

        self.data_len = len(data)

        return data

    def refresh_items(self):
        del self.table_items[0:len(self.table_items)]
        result = get_all('RoleInfo')
        for item in result:
            data_item = DataUserRole(result.index(item) + 1, item.id_, item.type, item.name, item.desc, item.selected)
            self.table_items.append(data_item)

    @staticmethod
    def get_id():
        return get_id('RoleInfo')

    def add_item(self, data, perm_list):
        if isinstance(data, DataUserRole):
            add_role_info(data, perm_list)
            self.data_len += 1
            EvtManager.dispatch_event(EnumEvent.EVT_PERMISSION_REFRESH)
            
    @staticmethod
    def delete_item(data):
        if isinstance(data, DataUserRole):
            delete_item('RoleInfo', data)
            EvtManager.dispatch_event(EnumEvent.EVT_PERMISSION_REFRESH)
            
    @staticmethod
    def update_item(data, perm_list):
        if isinstance(data, DataUserRole):
            update_role_info(data, perm_list)
            EvtManager.dispatch_event(EnumEvent.EVT_PERMISSION_REFRESH)


@Singleton
class CtrlPrinterScheme():
    def __init__(self):
        self.cur_item_index = 0
        self.table_items = list()

    def get_cur_item_index(self):
        return self.cur_item_index

    def set_cur_item_index(self, index_):
        self.cur_item_index = index_
    
    @staticmethod
    def get_data():
        result = get_all('PrintSchemeInfo')
        data = list()
        for item in result:
            data_item = DataPrinterScheme(result.index(item) + 1, item.id_, item.code, item.name, item.valid,
                                          item.type_name, item.count, item.backup_id)
            data.append(data_item)
            
        return data

    def refresh_items(self):
        del self.table_items[0:len(self.table_items)]
        result = get_all('PrintSchemeInfo')
        for item in result:
            data_item = DataPrinterScheme(result.index(item) + 1, item.id_, item.code, item.name, item.valid,
                                          item.type_id, item.count, item.backup_id)
            self.table_items.append(data_item)

    def get_items(self):
        return self.table_items
    
    @staticmethod
    def add_item(data):
        if isinstance(data, DataPrinterScheme):
            add_item('PrintSchemeInfo', data)
            EvtManager.dispatch_event(EnumEvent.EVT_PRINTER_SCHEME_REFRESH)
            
    @staticmethod
    def delete_item(data):
        if isinstance(data, DataPrinterScheme):
            delete_item('PrintSchemeInfo', data)
            EvtManager.dispatch_event(EnumEvent.EVT_PRINTER_SCHEME_REFRESH)
            
    @staticmethod
    def update_item(data):
        if isinstance(data, DataPrinterScheme):
            update_item('PrintSchemeInfo', data)
            EvtManager.dispatch_event(EnumEvent.EVT_PRINTER_SCHEME_REFRESH)


@Singleton
class CtrlSchemeType():
    def __init__(self):
        self.data_len = 0

    def get_data_len(self):
        return self.data_len - 2

    def get_data(self):
        result = get_all('SchemeTypeInfo')
        data = list()
        for item in result:
            data.append(DataSchemeType(result.index(item) + 1, item.id_, item.name))
            
        self.data_len = len(data)
            
        return data
    
    @staticmethod
    def get_id():
        return get_id('SchemeTypeInfo')

    def add_item(self, data):
        if isinstance(data, DataSchemeType):
            add_item('SchemeTypeInfo', data)
            self.data_len += 1
            
    @staticmethod
    def delete_item(data):
        if isinstance(data, DataSchemeType):
            delete_item('SchemeTypeInfo', data)

    @staticmethod
    def update_item(data):
        if isinstance(data, DataSchemeType):
            update_item('SchemeTypeInfo', data)


@Singleton
class CtrlPermList():
    def __init__(self):
        self.data_len = 0

    def get_data_len(self):
        return self.data_len - 2

    def get_data(self):
        result = get_all('PermList')
        data = list()
        for item in result:
            data.append(DataPermList(result.index(item) + 1, item.id_, item.code,
                                     item.p_code, item.name, item.selected))

        self.data_len = len(data)

        return data

    def get_data_by_group(self, group):
        result = get_perm_by_group(group)
        data = list()
        for item in result:
            data.append(DataPermList(result.index(item) + 1, item.id_, item.code,
                                     item.p_code, item.name, item.selected))

        self.data_len = len(data)

        return data

    @staticmethod
    def get_id():
        return get_id('PermList')

    def add_item(self, data):
        if isinstance(data, DataType):
            add_item('PermList', data)
            self.data_len += 1

    @staticmethod
    def delete_item(data):
        if isinstance(data, DataType):
            delete_item('PermList', data)

    @staticmethod
    def update_item(data):
        if isinstance(data, DataType):
            update_item('PermList', data)
