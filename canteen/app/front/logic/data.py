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
