#!/usr/bin/env python
#_*_ encoding=utf-8 _*_
from framework.core import EvtManager, Singleton
from app.manager.logic.data import *
from app.enum_event import EnumEvent
from service.data_base.manager import *

import tablib
tablib.__version__


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
                self.user = user
                self.password = password
                self.check_result = True
        except:
            self.check_result = False

        EvtManager.dispatch_event(EnumEvent.EVT_LOGIN)

    def modify_password(self, old_password, new_password):
        if old_password == self.password:
            modify_password(self.user, new_password)
            return True

        return False

    def get_result(self):
        return self.check_result

    def get_image_path(self):
        return self.img_path


@Singleton
class CtrlCompany():
    def __init__(self):
        self.company_id = None

    def get_company_info(self):
        result = get_company_info()
        if result is not None:
            self.company_id = result.id_
            company_info = DataCompany(result.company_name, result.boss_name, result.company_address,
                                       result.company_email, result.boss_phone)

            return company_info

        return None

    def set_company_info(self, company_info):
        set_company_info(self.company_id, company_info)

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
                bat_add_items('TableInfo', data)

        bat_add_commit()
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
                                   item.category_name, item.unit_name, item.spec_id, item.commission, item.discount,
                                   item.on_sale, item.recommend, item.enable, item.picture_url, item.print_scheme_name,
                                   item.command, item.is_print)
            data.append(data_item)
            
        return data

    def refresh_items(self):
        del self.table_items[0:len(self.table_items)]
        result = get_all('DishInfo')
        for item in result:
            data_item = DataDishes(result.index(item) + 1, item.id_, item.code, item.name, item.brevity,
                                   item.category_id, item.unit_id, item.spec_id, item.commission, item.discount,
                                   item.on_sale, item.recommend, item.enable, item.picture_url, item.print_scheme_id,
                                   item.command, item.is_print)
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
            data_item = DataEmployee(result.index(item) + 1, item.id_, item.code, item.name, item.birthday, item.duty,
                                     item.pass_word,item.dept_name, item.gender, item.telephone, item.id_card,
                                     item.status, item.address, item.email, item.memo)
            data.append(data_item)
            
        return data

    def refresh_items(self):
        del self.table_items[0:len(self.table_items)]
        result = get_all('EmployeeInfo')
        for item in result:
            data_item = DataEmployee(result.index(item) + 1, item.id_, item.code, item.name, item.birthday, item.duty,
                                     item.pass_word, item.dept_id, item.gender, item.telephone, item.id_card,
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
    def update_item(data, group_list):
        if isinstance(data, DataEmployee):
            update_user_info(data, group_list)
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
                                          item.type_name, item.count, item.backup_id, item.printer_name)
            data.append(data_item)
            
        return data

    def refresh_items(self):
        del self.table_items[0:len(self.table_items)]
        result = get_all('PrintSchemeInfo')
        for item in result:
            data_item = DataPrinterScheme(result.index(item) + 1, item.id_, item.code, item.name, item.valid,
                                          item.type_id, item.count, item.backup_id, item.printer_name)
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


@Singleton
class CtrlBusinessInfo():
    def __init__(self):
        self.date_from = None
        self.time_from = None
        self.date_to = None
        self.time_to = None
        self.li_business = list()

        self.consume_price = 0
        self.real_price = 0
        self.consumer_num = 0
        self.bill_total = 0
        self.cash_total = 0
        self.coupon_total = 0
        self.membership_total = 0
        self.pos_total = 0
        self.group_total = 0
        self.credit_total = 0
        self.boss_sign_total = 0

    def get_business_items(self):
        return self.li_business

    def get_query_time(self):
        return self.date_from, self.time_from, self.date_to, self.time_to

    def get_summary_info(self):
        return self.consume_price, self.real_price, self.consumer_num, self.bill_total, self.cash_total, \
            self.coupon_total, self.membership_total, self.pos_total, self.group_total, self.credit_total, \
            self.boss_sign_total

    def query_business(self, date_from, time_from, date_to, time_to):
        self.consume_price = 0
        self.real_price = 0
        self.consumer_num = 0
        self.bill_total = 0
        self.cash_total = 0
        self.coupon_total = 0
        self.membership_total = 0
        self.pos_total = 0
        self.group_total = 0
        self.credit_total = 0
        self.boss_sign_total = 0
        self.date_from = date_from
        self.time_from = time_from
        self.date_to = date_to
        self.time_to = time_to
        del self.li_business[0:len(self.li_business)]
        result = get_business_info(date_from, time_from, date_to, time_to)
        if len(result) > 0:
            for key, info in result.items():
                free_price = info.price - info.real_price if info.real_price is not None else 0
                average_price = round(info.price / info.consumer, 2)
                self.consume_price = self.consume_price + info.price
                self.real_price = self.real_price + info.real_price
                self.consumer_num = self.consumer_num + info.consumer
                self.bill_total = self.bill_total + info.bill_num
                self.cash_total = self.cash_total + info.cash
                self.coupon_total = self.coupon_total + info.coupon
                self.membership_total = self.membership_total + info.membership
                self.pos_total = self.pos_total + info.pos
                self.group_total = self.group_total + info.group
                self.credit_total = self.credit_total + info.credit
                self.boss_sign_total = self.boss_sign_total + info.boss_sign
                item = DataBusinessInfo(0, 0, info.table_num, info.consumer, info.price, free_price, info.real_price,
                                        info.bill_num, average_price, info.cash, info.coupon, info.membership,
                                        info.pos, info.group, info.credit, info.boss_sign, info.checkout_time)
                self.li_business.append(item)
            #self.li_business.sort(lambda x, y: cmp(int(x.consumer_num), int(y.consumer_num)))
            self.li_business.sort(lambda x, y: cmp(str(x.consume_time.strftime("%Y-%m-%d")),
                                                   str(y.consume_time.strftime("%Y-%m-%d"))))

        EvtManager.dispatch_event(EnumEvent.EVT_BUSINESS_INFO_REFRESH)

    def export_business(self, file_name):
        business_data_set = tablib.Dataset()
        business_header = (u'序号', u'桌次', u'消费人次', u'消费金额', u'优惠金额', u'收款金额', u"发票金额", u'人均消费',
                           u"现金", u"优惠券", u"会员卡", u"POS支付", u"团购", u"挂账", u"老板签单", u'时间')
        business_data_set.headers = business_header
        if len(self.li_business) > 0:
            for item in self.li_business:
                business_data_set.append([self.li_business.index(item), item.table_num, item.consumer_num,
                                          item.consume_money, item.free_money, item.real_money, item.bill_num,
                                          item.average_money, item.cash, item.coupon, item.membership, item.pos,
                                          item.group, item.credit, item.boss_sign, item.consume_time])

        business_data_set.title = u'消费报表'
        business_file = open(file_name, 'wb')
        business_file.write(business_data_set.xlsx)
        business_file.close()


@Singleton
class CtrlSalesInfo():
    def __init__(self):
        self.date_from = None
        self.time_from = None
        self.date_to = None
        self.time_to = None
        self.li_sales = list()

        self.consume_price = 0
        self.real_price = 0
        self.consumer_num = 0
        self.bill_total = 0
        self.cash_total = 0
        self.coupon_total = 0
        self.membership_total = 0
        self.pos_total = 0
        self.group_total = 0
        self.credit_total = 0
        self.boss_sign_total = 0

    def get_sales_items(self):
        return self.li_sales

    def get_query_time(self):
        return self.date_from, self.time_from, self.date_to, self.time_to

    def get_summary_info(self):
        return self.consume_price, self.real_price, self.consumer_num, self.bill_total, self.cash_total, \
            self.coupon_total, self.membership_total, self.pos_total, self.group_total, self.credit_total, \
            self.boss_sign_total

    def query_sales(self, date_from, time_from, date_to, time_to):
        self.consume_price = 0
        self.real_price = 0
        self.consumer_num = 0
        self.bill_total = 0
        self.cash_total = 0
        self.coupon_total = 0
        self.membership_total = 0
        self.pos_total = 0
        self.group_total = 0
        self.credit_total = 0
        self.boss_sign_total = 0
        self.date_from = date_from
        self.time_from = time_from
        self.date_to = date_to
        self.time_to = time_to
        del self.li_sales[0:len(self.li_sales)]
        result = get_sales_info(date_from, time_from, date_to, time_to)
        if len(result) > 0:
            for info in result:
                free_price = info.price - info.real_price if info.real_price is not None else 0
                self.consume_price = self.consume_price + info.price
                if info.real_price is not None:
                    self.real_price = self.real_price + info.real_price
                self.consumer_num = self.consumer_num + info.consumer
                self.bill_total = self.bill_total + info.bill_num
                self.cash_total = self.cash_total + info.cash
                self.coupon_total = self.coupon_total + info.coupon
                self.membership_total = self.membership_total + info.membership
                self.pos_total = self.pos_total + info.pos
                self.group_total = self.group_total + info.group
                self.credit_total = self.credit_total + info.credit
                self.boss_sign_total = self.boss_sign_total + info.boss_sign
                item = DataSalesInfo(0, 0, info.table_num, info.consumer, info.price, free_price, info.real_price,
                                     info.bill_num, info.cash, info.coupon, info.membership, info.pos,
                                     info.group, info.credit, info.boss_sign, info.checkout_time)
                self.li_sales.append(item)

            self.li_sales.sort(lambda x, y: cmp(str(x.consume_time.strftime("%Y-%m-%d %H:%M:%S")),
                                                str(y.consume_time.strftime("%Y-%m-%d %H:%M:%S"))))
        EvtManager.dispatch_event(EnumEvent.EVT_SALES_INFO_REFRESH)

    def export_sales(self, file_name):
        sales_data_set = tablib.Dataset()
        sales_header = (u'序号', u'桌台', u'人次', u'消费金额', u'优惠金额', u'实际金额', u"发票金额", u"现金", u"优惠券",
                        u'会员卡', u"POS支付", u"团购", u"挂账", u"老板签单", u'时间')
        sales_data_set.headers = sales_header
        if len(self.li_sales) > 0:
            for item in self.li_sales:
                sales_data_set.append([self.li_sales.index(item), item.table_num, item.consumer_num, item.consume_money,
                                       item.free_money, item.real_money, item.bill_num, item.cash, item.coupon,
                                       item.membership, item.pos, item.group, item.credit, item.boss_sign,
                                       item.consume_time])

        sales_data_set.title = u'销售流水查询'
        sales_file = open(file_name, 'wb')
        sales_file.write(sales_data_set.xlsx)
        sales_file.close()


@Singleton
class CtrlBillboardInfo():
    def __init__(self):
        self.time_from = None
        self.time_to = None
        self.days = None
        self.li_billboard = list()

    def get_billboard_items(self):
        return self.li_billboard

    def get_query_time(self):
        return self.time_from, self.time_to

    def query_billboard(self, time_from, time_to, category_id):
        self.time_from = time_from
        self.time_to = time_to
        self.days = (time_to - time_from).days + 1
        del self.li_billboard[0:len(self.li_billboard)]
        result = get_billboard_info(time_from, time_to, category_id)
        if len(result) > 0:
            for key, info in result.items():
                average = info.dishes_count
                if self.days is not None and self.days > 0:
                    average = round(float(info.dishes_count) / self.days, 2)
                item = DataBillboardInfo(0, 0, info.dishes_name, info.brevity_code, info.category, info.unit,
                                         info.dishes_count, average, info.total_money, info.retreat_count,
                                         info.retreat_money)
                self.li_billboard.append(item)

            self.li_billboard.sort(lambda x, y: cmp(int(x.sale_count), int(y.sale_count)), reverse=True)
        EvtManager.dispatch_event(EnumEvent.EVT_BILLBOARD_INFO_REFRESH)

    def export_billboard(self, file_name):
        billboard_data_set = tablib.Dataset()
        billboard_header = (u'序号', u'菜名', u'编码缩写', u'类别', u'单位', u'销售份数', u'日均(份)', u'销售总额',
                            u"退菜份数", u"退菜总额")
        billboard_data_set.headers = billboard_header
        if len(self.li_billboard) > 0:
            for item in self.li_billboard:
                billboard_data_set.append([self.li_billboard.index(item), item.dishes_name, item.brevity_code,
                                           item.dishes_category, item.dishes_unit, item.sale_count, item.average_count,
                                           item.total_money, item.retreat_count, item.retreat_money])

        billboard_data_set.title = u'菜类销售排名'
        sales_file = open(file_name, 'wb')
        sales_file.write(billboard_data_set.xlsx)
        sales_file.close()
