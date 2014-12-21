#!/usr/bin/env python
#_*_ encoding=utf-8 _*_


class DataWaiterItem():
    def __init__(self):
        self.waiter_id = -1
        self.waiter_name = None


class DataTableItem():
    def __init__(self):
        self.table_id = -1
        self.table_num = 0
        self.table_name = ""
        self.table_type = ""
        self.table_area = ""
        self.table_status = 0
        self.open_time = ""
        self.waiter = ""
        self.people_num = 0
        self.customer_num = 0
        self.deposit = ""
        self.memo = ""
        self.amount = None
        self.is_selected = False
        self.order_id = None
        self.order_num = ""
        self.operator = ""


class DataTypeItem():
    def __init__(self):
        self.type_id = -1
        self.type_name = ""


class DataDishesItem():
    def __init__(self):
        self.dishes_id = -1
        self.dishes_code = -1
        self.dishes_name = ""
        self.dishes_spec = None
        self.dishes_unit = None
        self.dishes_style = None
        self.dishes_type = 0
        self.dishes_brevity = ""
        self.dishes_discount = 1


class DataOrderDishesItem():
    def __init__(self):
        self.dishes_id = 0
        self.dishes_code = 0
        self.dishes_count = 0
        self.dishes_retreat_count = 0
        self.dishes_spec_discount = 1.0
        self.dishes_price = 0
        self.dishes_spec = None
        self.dishes_style = None
        self.dishes_unit = ''
        self.dishes_demand = ''
        self.li_dishes_log_id = list()


class DataOrderItem():
    def __init__(self):
        self.order_num = 0
        self.order_money = 0
        self.place_money = 0
        self.real_money = 0
        self.order_status = 0
        self.all_discount = 1
        self.free_price = 0
        self.cashier_cash = 0.0
        self.cashier_coupon = 0.0
        self.cashier_membership = 0.0
        self.cashier_pos = 0.0
        self.cashier_group = 0.0
        self.cashier_credit = 0.0
        self.cashier_boss_sign = 0.0
        self.bill_num = 0.0
        self.change_num = 0.0
        self.dishes_discount = 0.0
        self.di_order_dishes_items = dict()
        self.di_place_dishes_items = dict()


class DataOrderedDishesItem():
    def __init__(self):
        self.dishes_code = ''
        self.dishes_name = ''
        self.dishes_spec = ''
        self.dishes_spec_id = 0
        self.dishes_style_id = 0
        self.customer_demand = ''
        self.dishes_unit = ''
        self.dishes_count = 0
        self.dishes_retreat_count = 0
        self.dishes_spec_discount = 1.0
        self.dishes_amount = 0
        self.dishes_recive_amount = 0
        self.dishes_real_amount = 0
        self.dishes_status = u"新增"


class DataDishesDiscount():
    def __init__(self, dishes_id, dishes_code, dishes_discount = 1.0):
        self.dishes_id = dishes_id
        self.dishes_code = dishes_code
        self.dishes_discount = dishes_discount


