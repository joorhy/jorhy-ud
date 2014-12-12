#!/usr/bin/env python
#_*_ encoding=utf-8 _*_


class DataCompany(object):
    def __init__(self, name, person, address, email, phone):
        self.name = name
        self.person = person
        self.address = address
        self.email = email
        self.phone = phone


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
    def __init__(self, line, key, code, name, spell, category, unit, spec_id, commission, discount,
                 on_sale, recommend, stop, image_url, printer_scheme, is_print='0'):
        self.line = line
        self.key = key
        self.code = code
        self.name = name
        self.spell = spell
        self.category = category
        self.unit = unit
        self.spec_id = spec_id
        self.commission = commission
        self.discount = discount
        self.on_sale = on_sale
        self.recommend = recommend
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
    def __init__(self, line, key, code, name, birthday, duty, password,
                 department, sex, telephone, id_card, state, address, email, note):
        self.line = line
        self.key = key
        self.code = code
        self.name = name
        self.birthday = birthday
        self.duty = duty
        self.password = password
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
    def __init__(self, line, key, code, name, valid, scheme_type, print_count, backup, printer_name):
        self.line = line
        self.key = key
        self.code = code
        self.name = name
        self.valid = valid
        self.scheme_type = scheme_type
        self.print_count = print_count
        self.backup = backup
        self.printer_name = printer_name


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


class DataBusinessInfo(object):
    def __init__(self, line, key, table_num, consumer_num, consume_money, free_money,
                 real_money, bill_num, average_money, cash, coupon, membership, pos,
                 group, credit, boss_sign, consume_time):
        self.line = line
        self.key = key
        self.table_num = int(table_num)
        self.consumer_num = int(consumer_num)
        self.consume_money = consume_money
        self.free_money = free_money
        self.real_money = real_money
        self.bill_num = bill_num
        self.average_money = average_money
        self.cash = cash
        self.coupon = coupon
        self.membership = membership
        self.pos = pos
        self.group = group
        self.credit = credit
        self.boss_sign = boss_sign
        self.consume_time = consume_time


class DataSalesInfo(object):
    def __init__(self, line, key, table_num, consumer_num, consume_money, free_money, real_money, bill_num, cash,
                 coupon, membership, pos, group, credit, boss_sign, consume_time):
        self.line = line
        self.key = key
        self.table_num = int(table_num)
        self.consumer_num = int(consumer_num)
        self.consume_money = consume_money
        self.free_money = free_money
        self.real_money = real_money
        self.bill_num = bill_num
        self.cash = cash
        self.coupon = coupon
        self.membership = membership
        self.pos = pos
        self.group = group
        self.credit = credit
        self.boss_sign = boss_sign
        self.consume_time = consume_time


class DataBillboardInfo(object):
    def __init__(self, line, key, dishes_name, brevity_code, dishes_category, dishes_unit,
                 sale_count, average_count, total_money, retreat_count, retreat_money):
        self.line = line
        self.key = key
        self.dishes_name = dishes_name
        self.brevity_code = brevity_code
        self.dishes_category = dishes_category
        self.dishes_unit = dishes_unit
        self.sale_count = sale_count
        self.average_count = average_count
        self.total_money = total_money
        self.retreat_count = retreat_count
        self.retreat_money = retreat_money