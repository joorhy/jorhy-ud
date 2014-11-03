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
        self.is_open = False
        self.people_num = 0
        self.amount = None


class DataTypeItem():
    def __init__(self):
        self.type_id = -1
        self.type_name = ""


class DataDishesItem():
    def __init__(self):
        self.dishes_id = -1
        self.dishes_code = -1
        self.dishes_name = ""
        self.dishes_spec = ""
        self.dishes_unit = ""


class DataOrderDishesItem():
    def __init__(self):
        self.dishes_code = -1
        self.dishes_count = 0


class DataOrderItem():
    def __init__(self):
        self.order_num = 0
        self.order_status = 0
        self.di_order_dishes_items = dict()


class DataOrderedDishesItem():
    def __init__(self):
        self.dishes_name = ""
        self.dishes_spec = ""
        self.dishes_unit = ""
        self.dishes_count = 0


