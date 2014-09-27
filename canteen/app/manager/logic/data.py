#!/usr/bin/env python
#_*_ encoding=utf-8 _*_


class DataArea(object):
    def __init__(self, id_, code, name):
        self.id = id_
        self.code = code
        self.name = name


class DataMinExpense(object):
    def __init__(self, id_, code, name, price):
        self.id = id_
        self.code = code
        self.name = name
        self.price = price


class DataTable(object):
    def __init__(self, id_, code, name, table_type, area, people_num, min_type):
        self.id = id_
        self.code = code
        self.name = name
        self.table_type = table_type
        self.area = area
        self.people_num = people_num
        self.min_type = min_type


class DataType(object):
    def __init__(self, id_, code, name):
        self.id = id_
        self.code = code
        self.name = name


class DataCategory(object):
    def __init__(self, id_, code, name):
        self.id = id_
        self.code = code
        self.name = name


class DataDishes(object):
    def __init__(self, line, id_, code, name, spell, spec, category, 
                 price, unit, style, commission, discount, stop, image_url, printer_scheme):
        self.line = line
        self.id = id_
        self.code = code
        self.name = name
        self.spell = spell
        self.spec = spec
        self.category = category
        self.price = price
        self.unit = unit
        self.style = style
        self.commission = commission
        self.discount = discount
        self.stop = stop
        self.image_url = image_url
        self.printer_scheme = printer_scheme


class DataSpec(object):
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price


class DataStyle(object):
    def __init__(self, code, name, price_add, amount_add):
        self.code = code
        self.name = name
        self.price_add = price_add
        self.amount_add = amount_add


class DataUnit(object):
    def __init__(self, id_, code, name):
        self.id = id_
        self.code = code
        self.name = name


class DataDepartment(object):
    def __init__(self, id_, code, name):
        self.id = id_
        self.code = code
        self.name = name


class DataEmployee(object):
    def __init__(self, num_id, line, code, name, birthday, duty, 
                 department, sex, telephone, id_card, state, address, email, note):
        self.id = num_id
        self.line = line
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
    def __init__(self, line, id_, code, name):
        self.line = line
        self.id = id_
        self.code = code
        self.name = name


class DataPrinterScheme(object):
    def __init__(self, id_, code, name, valid, scheme_type, print_count, backup):
        self.id = id_
        self.code = code
        self.name = name
        self.valid = valid
        self.scheme_type = scheme_type
        self.print_count = print_count
        self.backup = backup


class DataSchemeType(object):
    def __init__(self, id_, code, name):
        self.id = id_
        self.code = code
        self.name = name