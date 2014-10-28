#!/usr/bin/env python
#_*_ encoding=utf-8 _*_
from app.front.config import CONFIG
from framework.core import EvtManager, Singleton
from app.enum_event import EnumEvent
from app.front.logic.data import *

import random


@Singleton
class CtrlFrontLogin():
    def __init__(self):
        self.check_result = False

    def login(self, user, password):
        try:
            if user == '0000' and password == '0000':
                self.check_result = True
            else:
                self.check_result = False
        except TypeError:
            self.check_result = False

        EvtManager.dispatch_event(EnumEvent.EVT_LOGIN)

    def get_result(self):
        return self.check_result


@Singleton
class CtrlTableInfo():
    def __init__(self):
        self.li_table_items = list()
        self.li_waiter_items = list()

    def get_waiter_items(self):
        if len(self.li_waiter_items) == 0:
            if CONFIG.useTemp:
                for i in range(5):
                    item = DataWaiterItem()
                    item.waiter_id = i
                    item.waiter_name = u"服务员" + str(i + 1)
                    self.li_waiter_items.append(item)
            else:
                pass

        return self.li_waiter_items

    def get_table_items(self):
        if len(self.li_table_items) == 0:
            if CONFIG.useTemp:
                for i in range(20):
                    item = DataTableItem()
                    item.table_id = i
                    item.table_num = str(i + 1)
                    item.table_name = str(i + 1) + u"号餐桌"
                    item.is_open = True if random.randint(4, 10) == 6 else False
                    item.people_num = random.randint(4, 10)
                    if item.is_open:
                        item.amount = round(random.random() * 123, 2)
                    self.li_table_items.append(item)
            else:
                pass

        return self.li_table_items

    def get_free_tables(self):
        li_free_tables = list()
        for item in self.li_table_items:
            if not item.is_open:
                li_free_tables.append(item)

        return li_free_tables

    def get_table_item(self, index_):
        if (index_ >= 0) and (index_ < len(self.li_table_items)):
            return self.li_table_items[index_]
        else:
            return None

    def open_table(self, index_, data):
        if isinstance(data, DataTableItem):
            self.li_table_items[index_].is_open = True

        EvtManager.dispatch_event(EnumEvent.EVT_FRONT_PAGE_REFRESH)


