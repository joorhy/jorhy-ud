#!/usr/bin/env python
#_*_ encoding=utf-8 _*_
from service.data_base.canteen import *


class ModeCompany():
    def __init__(self, obj):
        if isinstance(obj, CompanyInfo):
            self.id_ = int(obj.id)
            self.register_id = obj.vch_uid
            self.company_name = obj.vch_name
            self.boss_name = obj.vch_boss_name
            self.boss_phone = obj.num_boss_phone
            self.company_email = obj.vch_email
            self.company_address = obj.vch_address


class ModeVacationType():
    def __init__(self, obj):
        if isinstance(obj, DeprecatedUUserScheduleStatu):
            self.id_ = int(obj.id)
            self.vacation_type = obj.vch_name


class ModeJobStatus():
    def __init__(self, obj):
        if isinstance(obj, DeprecatedUUserStatu):
            self.id_ = int(obj.id)
            self.status = obj.vch_name


class ModeDeviceInfo():
    def __init__(self, obj):
        if isinstance(obj, DeviceRegistration):
            self.id_ = int(obj.id)
            self.device_mac = obj.vch_device_mac
            self.device_name = obj.vch_device_name


class ModeDishCategory():
    def __init__(self, obj):
        if isinstance(obj, DishCategory):
            self.id_ = int(obj.id)
            self.name = obj.vch_name


class ModeDishPublish():
    def __init__(self, obj):
        if isinstance(obj, DishPublish):
            self.id_ = int(obj.id)
            self.name = obj.vch_name
            self.code = obj.vch_code
            self.brevity = obj.vch_spell
            self.picture_url = obj.vch_picname
            self.style_id = obj.num_style_id
            self.spec_id = obj.num_spec_id
            self.category_id = obj.num_category
            self.unit_id = obj.num_unit
            self.commission = obj.num_ticheng
            self.discount = obj.num_discount
            self.change_code = obj.num_change_code
            self.print_scheme_id = obj.num_printer_scheme_id
            self.enable = obj.ch_disabled
            self.is_print = obj.ch_is_print

            self.category_name = obj.dish_category.vch_name
            self.print_scheme_name = obj.num_printer_scheme.vch_name if obj.num_printer_scheme is not None else ''
            self.unit_name = obj.unit.vch_name if obj.unit is not None else ''


class ModeDishSpec():
    def __init__(self, obj):
        if isinstance(obj, DishSpec):
            self.id_ = int(obj.id)
            self.dish_code = obj.vch_dish_code
            self.name = obj.vch_name
            self.price = obj.num_price


class ModeDishStyle():
    def __init__(self, obj):
        if isinstance(obj, DishStyle):
            self.id_ = int(obj.id)
            self.dish_code = obj.vch_dish_code
            self.name = obj.vch_name
            self.price = obj.num_priceadd
            self.is_add_price = obj.ch_mountadd


class ModePrintScheme():
    def __init__(self, obj):
        if isinstance(obj, PrinterScheme):
            self.id_ = int(obj.id)
            self.name = obj.vch_name
            self.valid = obj.num_valid
            self.type_id = obj.num_scheme_type
            self.count = int(obj.num_print_count)
            self.code = obj.vch_code
            self.backup_id = obj.num_backup_scheme_id
            self.type_name = obj.printer_scheme_type.vch_name if obj.printer_scheme_type is not None else ''
            self.printer_name = 'Microsoft XPS Document Writer'


class ModePrintSchemeType():
    def __init__(self, obj):
        if isinstance(obj, PrinterSchemeType):
            self.id_ = int(obj.id)
            self.name = obj.vch_name


class ModeTableInfo():
    def __init__(self, obj):
        if isinstance(obj, TableInfo):
            self.id_ = int(obj.id)
            self.name = obj.vch_name
            self.type_id = obj.num_type
            self.area_id = obj.num_area
            self.people_num = int(obj.num_people_amount)
            self.expense_id = obj.num_minexpense_id
            self.type_name = obj.table_info_type.vch_name
            self.area_name = obj.table_info_area.vch_name
            self.expense_name = obj.num_minexpense.vch_name if obj.num_minexpense is not None else ''


class ModeTableInfoArea():
    def __init__(self, obj):
        if isinstance(obj, TableInfoArea):
            self.id_ = int(obj.id)
            self.name = obj.vch_name


class ModeTableInfoExpense():
    def __init__(self, obj):
        if isinstance(obj, TableInfoMinexpense):
            self.id_ = int(obj.id)
            self.name = obj.vch_name
            self.min_price = float(obj.num_amount)


class ModeTableInfoType():
    def __init__(self, obj):
        if isinstance(obj, TableInfoType):
            self.id_ = int(obj.id)
            self.name = obj.vch_name


class ModeUDept():
    def __init__(self, obj):
        if isinstance(obj, UDept):
            self.id_ = int(obj.id)
            self.name = obj.vch_name


class ModeUPermList():
    def __init__(self, obj):
        if isinstance(obj, UPermList):
            self.id_ = int(obj.id)
            self.code = obj.vch_code
            self.p_code = obj.vch_pcode
            self.name = obj.vch_name
            self.selected = False


class ModeUPermGroup():
    def __init__(self, obj):
        if isinstance(obj, UPermGroup):
            self.id_ = int(obj.id)
            self.type = obj.vch_type
            self.name = obj.vch_name
            self.desc = obj.vch_desc
            self.selected = False


class ModeUType():
    def __init__(self, obj):
        if isinstance(obj, UType):
            self.id_ = int(obj.id)
            self.name = obj.vch_name


class ModeUUserInfo():
    def __init__(self, obj):
        if isinstance(obj, UUserinfo):
            self.id_ = int(obj.id)
            self.code = obj.vch_name
            self.pass_word = obj.vch_psw
            self.type = obj.num_user_type
            self.details_id = obj.num_userdetails_id
            self.name = obj.num_userdetails.vch_realname
            self.en_name = obj.num_userdetails.vch_englishname
            self.email = obj.num_userdetails.vch_email
            self.dept_id = obj.num_userdetails.num_dept_id
            self.dept_name = obj.num_userdetails.num_dept.vch_name
            self.duty = obj.num_userdetails.vch_duty if obj.num_userdetails.vch_duty is not None else ''
            self.duty_type_id = obj.num_userdetails.num_userdetails_type_id
            self.duty_type_name = obj.num_userdetails.num_userdetails_type.vch_name \
                if obj.num_userdetails.num_userdetails_type is not None else ''
            self.telephone = obj.num_userdetails.vch_phone if obj.num_userdetails.vch_phone is not None else ''
            self.gender = obj.num_userdetails.num_gender
            self.birthday = obj.num_userdetails.dt_birthday
            self.status = obj.num_userdetails.num_status
            self.id_card = obj.num_userdetails.vch_idcard if obj.num_userdetails.vch_idcard is not None else ''
            self.address = obj.num_userdetails.vch_address if obj.num_userdetails.vch_address is not None else ''
            self.memo = obj.num_userdetails.vch_memo if obj.num_userdetails.vch_memo is not None else ''


class ModeUnit():
    def __init__(self, obj):
        if isinstance(obj, Unit):
            self.id_ = int(obj.id)
            self.name = obj.vch_name


class ModeBusinessInfo():
    def __init__(self):
        self.price = 0
        self.real_price = 0
        self.checkout_time = ''
        self.table_num = 1
        self.consumer = 0


class ModeSalesInfo():
    def __init__(self, order_obj):
        if isinstance(order_obj, TableOrder):
            self.price = order_obj.num_price
            self.real_price = order_obj.num_price_real
            self.checkout_time = order_obj.dt_checkout
            self.table_num = order_obj.num_table_book.num_table_id
            self.consumer = order_obj.num_table_book.num_consumers


class ModeBillboardInfo():
    def __init__(self):
        self.dishes_code = ''
        self.dishes_name = ''
        self.brevity_code = ''
        self.total_money = 0
        self.unit = ''
        self.category = ''
        self.dishes_count = 0