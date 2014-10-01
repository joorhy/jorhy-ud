#!/usr/bin/env python
#_*_ encoding=utf-8 _*_
from service.data_base.canteen import *


class ModeCompany():
    def __init__(self, obj):
        if isinstance(obj, CompanyInfo):
            self.id_ = obj.id
            self.register_id = obj.vch_uid
            self.company_name = obj.vch_name
            self.boss_name = obj.vch_boss_name
            self.boss_phone = obj.num_boss_phone
            self.company_email = obj.vch_email
            self.company_address = obj.vch_address


class ModeVacationType():
    def __init__(self, obj):
        if isinstance(obj, DeprecatedUUserScheduleStatu):
            self.id_ = obj.id
            self.vacation_type = obj.vch_name


class ModeJobStatus():
    def __init__(self, obj):
        if isinstance(obj, DeprecatedUUserStatu):
            self.id_ = obj.id
            self.status = obj.vch_name


class ModeDeviceInfo():
    def __init__(self, obj):
        if isinstance(obj, DeviceRegistration):
            self.id_ = obj.id
            self.device_mac = obj.vch_device_mac
            self.device_name = obj.vch_device_name


class ModeDishCategory():
    def __init__(self, obj):
        if isinstance(obj, DishCategory):
            self.id_ = obj.id
            self.name = obj.vch_name


class ModeDishPublish():
    def __init__(self, obj):
        if isinstance(obj, DishPublish):
            self.id_ = obj.id
            self.name = obj.vch_name
            self.code = obj.num_code
            self.brevity = obj.vch_spell
            self.default_price = obj.num_default_price
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
            self.print_scheme_name = obj.num_printer_scheme.vch_name
            self.spec_name = obj.num_spec.vch_name
            self.style_name = obj.num_style.vch_name
            self.unit_name = obj.num_unit.vch_name


class ModeDishSpec():
    def __init__(self, obj):
        if isinstance(obj, DishSpec):
            self.id_ = obj.id
            self.name = obj.vch_name
            self.price = obj.num_price


class ModeDishStyle():
    def __init__(self, obj):
        if isinstance(obj, DishStyle):
            self.id_ = obj.id
            self.name = obj.vch_name
            self.is_add_price = obj.ch_mountadd


class ModePrintScheme():
    def __init__(self, obj):
        if isinstance(obj, PrinterScheme):
            self.id_ = obj.id
            self.name = obj.vch_name
            self.valid = obj.num_valid
            self.type_id = obj.num_scheme_type
            self.count = obj.num_print_count
            self.backup_id = obj.num_backup_scheme_id
            self.type_name = obj.printer_scheme_type.vch_name


class ModePrintSchemeType():
    def __init__(self, obj):
        if isinstance(obj, PrinterSchemeType):
            self.id_ = obj.id
            self.name = obj.vch_name


class ModeTableInfo():
    def __init__(self, obj):
        if isinstance(obj, TableInfo):
            self.id_ = obj.id
            self.name = obj.vch_name
            self.type_id = obj.num_type
            self.area_id = obj.num_area
            self.people_num = obj.num_people_amount
            self.expense_id = obj.num_minexpense_id
            self.type_name = obj.table_info_type.vch_name
            self.area_name = obj.table_info_area.vch_name
            self.expense_name = obj.num_minexpense.vch_name if obj.num_minexpense is not None else ''


class ModeTableInfoArea():
    def __init__(self, obj):
        if isinstance(obj, TableInfoArea):
            self.id_ = obj.id
            self.name = obj.vch_name


class ModeTableInfoExpense():
    def __init__(self, obj):
        if isinstance(obj, TableInfoMinexpense):
            self.id_ = obj.id
            self.name = obj.vch_name
            self.min_price = obj.num_amount


class ModeTableInfoType():
    def __init__(self, obj):
        if isinstance(obj, TableInfoType):
            self.id_ = obj.id
            self.name = obj.vch_name


class ModeUDept():
    def __init__(self, obj):
        if isinstance(obj, UDept):
            self.id_ = obj.id
            self.name = obj.vch_name


class ModeUPermList():
    def __init__(self, obj):
        if isinstance(obj, UPermList):
            self.id_ = obj.id
            self.parent_id = obj.pid
            self.name = obj.vch_name


class ModeUPermission():
    def __init__(self, obj):
        if isinstance(obj, UPermission):
            self.id_ = obj.id
            self.code = obj.num_perm_code
            self.name = obj.vch_perm_desc


class ModeUType():
    def __init__(self, obj):
        if isinstance(obj, UType):
            self.id_ = obj.id
            self.name = obj.vch_name


class ModeUUserInfo():
    def __init__(self, obj):
        if isinstance(obj, UUserinfo):
            self.id_ = obj.id
            self.code = obj.vch_name
            self.pass_word = obj.vch_psw
            self.type = obj.num_user_type
            self.details_id = obj.num_userdetails_id
            self.name = obj.num_userdetails.vch_realname
            self.en_name = obj.num_userdetails.vch_englishname
            self.email = obj.num_userdetails.vch_email
            self.dept_id = obj.num_userdetails.num_dept_id
            self.dept_name = obj.num_userdetails.num_dept.vch_name
            self.duty = obj.num_userdetails.vch_duty
            self.duty_type_id = obj.num_userdetails.num_userdetails_type_id
            self.duty_type_name = obj.num_userdetails.num_userdetails_type.vch_name
            self.telephone = obj.num_userdetails.vch_phone
            self.gender = obj.num_userdetails.num_gender
            self.birthday = obj.num_userdetails.dt_birthday
            self.status = obj.num_userdetails.num_status
            self.id_card = obj.num_userdetails.vch_idcard
            self.address = obj.num_userdetails.vch_address
            self.memo = obj.num_userdetails.vch_memo


class ModeUnit():
    def __init__(self, obj):
        if isinstance(obj, Unit):
            self.id_ = obj.id
            self.name = obj.vch_name