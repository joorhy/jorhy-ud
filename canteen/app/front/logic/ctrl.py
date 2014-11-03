#!/usr/bin/env python
#_*_ encoding=utf-8 _*_
from app.front.config import CONFIG
from framework.core import EvtManager, Singleton
from app.enum_event import EnumEvent
from app.front.logic.data import *
from service.http_json.http_service import HttpService

import random
import time


@Singleton
class CtrlFrontLogin():
    def __init__(self):
        self.check_result = False

    def login(self, user, password):
        try:
            if user == '0000' and password == '0000':
                self.check_result = True
            else:
                self.check_result = HttpService.get_instance().login(user, password)
        except:
            self.check_result = False

        EvtManager.dispatch_event(EnumEvent.EVT_LOGIN)

    def get_result(self):
        return self.check_result


@Singleton
class CtrlTableInfo():
    def __init__(self):
        self.li_table_items = list()
        self.li_waiter_items = list()
        self.di_table_order = dict()

        if CONFIG.useTemp:
            self.order_seq = 1

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

    def get_table_item(self, table_num):
        for item in self.li_table_items:
            if item.table_num == str(table_num):
                return item
        return None

    def open_table(self, index_, data):
        if isinstance(data, DataTableItem):
            self.li_table_items[index_].is_open = True

        EvtManager.dispatch_event(EnumEvent.EVT_FRONT_PAGE_REFRESH)

    def change_table(self, src_table_num, dst_table_num):
        for item in self.li_table_items:
            if item.table_num == src_table_num:
                item.table_num = dst_table_num
            elif item.table_num == dst_table_num:
                item.table_num = src_table_num

        self.li_table_items.sort(lambda x, y: cmp(int(x.table_num), int(y.table_num)))

        EvtManager.dispatch_event(EnumEvent.EVT_FRONT_PAGE_REFRESH)

    def order_dishes(self, table_num):
        order_num = None
        if table_num in self.di_table_order:
            order_num = self.di_table_order[table_num]
        else:
            if CONFIG.useTemp:
                order_num = time.strftime('B%Y%m%d') + str(self.order_seq)
                self.order_seq += 1
            else:
                pass

            table_order_tmp = {table_num: order_num}
            self.di_table_order.update(table_order_tmp)

        return order_num


@Singleton
class CtrlDishesInfo():
    def __init__(self):
        self.li_type_items = list()
        self.li_dishes_items = list()

    def get_type_items(self):
        if len(self.li_type_items) == 0:
            if CONFIG.useTemp:
                for i in range(10):
                    item = DataTypeItem()
                    item.type_id = i + 10000
                    item.type_name = u"菜品" + str(i)
                    self.li_type_items.append(item)
            else:
                pass

        return self.li_type_items

    def get_dishes_items(self):
        if len(self.li_dishes_items) == 0:
            if CONFIG.useTemp:
                for i in range(100):
                    item = DataDishesItem()
                    item.dishes_id = i
                    item.dishes_code = str(i + 1)
                    item.dishes_name = u"测试菜" + str(i)
                    self.li_dishes_items.append(item)
            else:
                pass

        return self.li_dishes_items

    def get_dishes_item(self, dishes_code):
        for item in self.li_dishes_items:
            if item.dishes_code == dishes_code:
                return item

        return None


@Singleton
class CtrlOrderInfo():
    def __init__(self):
        self.cur_order_num = None
        self.di_order_item = dict()

    def create_order(self, order_num):
        self.cur_order_num = order_num
        if order_num not in self.di_order_item:
            item = DataOrderItem()
            item.order_num = order_num

            order_item_tmp = {order_num: item}
            self.di_order_item.update(order_item_tmp)

    def add_dishes(self, dishes_code, count=1):
        cur_order_item = self.di_order_item[self.cur_order_num]
        if dishes_code in cur_order_item.di_order_dishes_items:
            cur_order_item.di_order_dishes_items[dishes_code].dishes_count += count
        else:
            item = DataOrderDishesItem()
            item.dishes_code = dishes_code
            item.dishes_count = count
            order_dishes_item_tmp = {dishes_code: item}
            cur_order_item.di_order_dishes_items.update(order_dishes_item_tmp)

        EvtManager.dispatch_event(EnumEvent.EVT_ORDER_DISHES_ITEMS_REFRESH)

    def del_dishes(self, dishes_code, count=1):
        cur_order_item = self.di_order_item[self.cur_order_num]
        if dishes_code in cur_order_item.di_order_dishes_items:
            if cur_order_item.di_order_dishes_items[dishes_code].dishes_count <= count:
                del cur_order_item.di_order_dishes_items[dishes_code]
            else:
                cur_order_item.di_order_dishes_items[dishes_code].dishes_count -= count

            EvtManager.dispatch_event(EnumEvent.EVT_ORDER_DISHES_ITEMS_REFRESH)


    def get_dishes_items(self):
        li_ordered_items = list()
        cur_order_item = self.di_order_item[self.cur_order_num]
        for (key, item) in cur_order_item.di_order_dishes_items.items():
            ordered_item = DataOrderedDishesItem()
            dishes_item = CtrlDishesInfo.get_instance().get_dishes_item(str(item.dishes_code))
            ordered_item.dishes_name = dishes_item.dishes_name
            ordered_item.dishes_spec = dishes_item.dishes_spec
            ordered_item.dishes_unit = dishes_item.dishes_unit
            ordered_item.dishes_count = item.dishes_count

            li_ordered_items.append(ordered_item)

        return li_ordered_items