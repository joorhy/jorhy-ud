#!/usr/bin/env python
#_*_ encoding=utf-8 _*_


class DataArea(object):
    def __init__(self, line=0, key=0, name=''):
        self.line = line
        self.key = key
        self.name = name


class DataMinExpense(object):
    def __init__(self, line=0, key=0, name='', price=0):
        self.line = line
        self.key = key
        self.name = name
        self.price = price


class DataTable(object):
    def __init__(self, line=0, key=0, name='', table_type=0, area=0, people_num=0, min_type=0):
        self.line = line
        self.key = key
        self.name = name
        self.table_type = table_type
        self.area = area
        self.people_num = people_num
        self.min_type = min_type


class DataType(object):
    def __init__(self, line=0, key=0, name=''):
        self.line = line
        self.key = key
        self.name = name


class DataCategory(object):
    def __init__(self, line=0, key=0, name=''):
        self.line = line
        self.key = key
        self.name = name


class DataDishes(object):
    def __init__(self, line, key, code, name, spell, category, unit,
                 commission, discount, stop, image_url, printer_scheme, is_print='0'):
        self.line = line
        self.key = key
        self.code = code
        self.name = name
        self.spell = spell
        self.category = category
        self.unit = unit
        self.commission = commission
        self.discount = discount
        self.stop = stop
        self.image_url = image_url
        self.printer_scheme = printer_scheme
        self.is_print = is_print


class DataSpec(object):
    def __init__(self, line=0, key=0, dish_code='', name='', price=0):
        self.line = line
        self.key = key
        self.dish_code = dish_code
        self.name = name
        self.price = price


class DataStyle(object):
    def __init__(self, line=0, key=0, dish_code='', name='', price_add=0, amount_add='N'):
        self.line = line
        self.key = key
        self.dish_code = dish_code
        self.name = name
        self.price_add = price_add
        self.amount_add = amount_add


class DataUnit(object):
    def __init__(self, line=0, key=0, name=''):
        self.line = line
        self.key = key
        self.name = name


class DataDepartment(object):
    def __init__(self, line, key, name):
        self.line = line
        self.key = key
        self.name = name


class DataEmployee(object):
    def __init__(self, line, key, code, name, birthday, duty,
                 department, sex, telephone, id_card, state, address, email, note):
        self.line = line
        self.key = key
        self.code = code
        self.name = name
        self.birthday = birthday
        self.duty = duty
        self.department = department
        self.sex = sex
        self.telephone = telephone
        self.id_card = id_card
        self.state = state
        self.address = address
        self.email = email
        self.note = note


class DataUserRole(object):
    def __init__(self, line, key, type_, name, desc='', selected=False):
        self.line = line
        self.key = key
        self.type = type_
        self.name = name
        self.desc = desc
        self.selected = selected


class DataPrinterScheme(object):
    def __init__(self, line, key, code, name, valid, scheme_type, print_count, backup):
        self.line = line
        self.key = key
        self.code = code
        self.name = name
        self.valid = valid
        self.scheme_type = scheme_type
        self.print_count = print_count
        self.backup = backup


class DataSchemeType(object):
    def __init__(self, line, key, name):
        self.line = line
        self.key = key
        self.name = name


class DataPermList(object):
    def __init__(self, line, key, code, p_code, name, selected=False):
        self.line = line
        self.key = key
        self.code = code
        self.p_code = p_code
        self.name = name
        self.selected = selected