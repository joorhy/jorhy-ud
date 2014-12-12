#!/usr/bin/env python
#_*_ encoding=utf-8 _*_
from app.front.config import CONFIG
from framework.core import EvtManager, Singleton
from app.enum_event import EnumEvent
from app.front.logic.data import *
from service.http_json.http_service import HttpService
from framework.core import Log

import random
import time
import re
from threading import Timer


@Singleton
class CtrlFrontLogin():
    def __init__(self):
        self.check_result = False
        self.user = ""
        self.password = ""

    def login(self, user, password):
        try:
            if user == '0000' and password == '0000':
                self.check_result = True
            else:
                self.check_result = HttpService.get_instance().login(user, password)
                if self.check_result:
                    self.user = user
                    self.password = password
        except Exception, ex:
            print Exception, ":", ex
            self.check_result = False

        EvtManager.dispatch_event(EnumEvent.EVT_LOGIN)

    def get_result(self):
        return self.check_result

    def get_user(self):
        return self.user

    def get_password(self):
        return self.password


@Singleton
class CtrlTableInfo():
    def __init__(self):
        self.li_table_items = list()
        self.li_waiter_items = list()
        self.di_table_order = dict()
        self.selected_table_num = None

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
                result = HttpService.get_instance().get_waiter_items()
                if result is not None:
                    for info in result:
                        item = DataWaiterItem()
                        item.waiter_id = info["id"]
                        item.waiter_name = info["name"]
                        self.li_waiter_items.append(item)

        return self.li_waiter_items

    def refresh_table_items(self):
        del self.li_table_items[0: len(self.li_table_items)]
        EvtManager.dispatch_event(EnumEvent.EVT_FRONT_PAGE_REFRESH)

    def get_table_items(self):
        if len(self.li_table_items) == 0:
            if CONFIG.useTemp:
                for i in range(20):
                    item = DataTableItem()
                    item.table_id = i
                    item.table_num = str(i)
                    item.table_name = u"餐桌" + str(i + 1)
                    item.table_type = u"餐桌" if random.randint(4, 6) == 6 else u"麻将桌"
                    item.table_area = u"大厅" if random.randint(4, 6) == 6 else u"二楼"
                    item.table_status = 0
                    item.people_num = random.randint(4, 10)
                    if item.table_status != 0:
                        item.amount = round(random.random() * 123, 2)
                    self.li_table_items.append(item)
            else:
                result = HttpService.get_instance().get_table_items()
                for info in result:
                    item = DataTableItem()
                    item.table_id = info['num_table_id']
                    item.table_num = str(info['num_table_id'])
                    item.table_name = info['vch_name']
                    item.open_time = info['dt_checkin_start']
                    item.table_type = info['vch_table_type']
                    item.table_area = info['vch_table_area']
                    item.table_status = int(info['ch_openflag'])
                    item.people_num = info['num_people_amount']
                    item.customer_num = info['num_consumers']
                    item.order_id = info['num_order_id']
                    item.order_num = info['vch_code']
                    if item.table_status != 0:
                        table_order_tmp = {item.table_id: item.order_num}
                        self.di_table_order.update(table_order_tmp)
                    #if item.table_status == 2:
                    #    CtrlOrderInfo.get_instance().create_order(item.order_num, 2)
                    #    item.amount = round(random.random() * 123, 2)
                    self.li_table_items.append(item)

        return self.li_table_items

    def set_selected_item_id(self, table_num):
        self.selected_table_num = table_num
        for item in self.li_table_items:
            if int(item.table_num) == table_num:
                item.is_selected = True
            else:
                item.is_selected = False

    def get_selected_item_id(self):
        for item in self.li_table_items:
            if item.is_selected:
                return int(item.table_num)

        return None

    def get_selected_table_num(self):
        return self.selected_table_num

    def get_free_tables(self):
        li_free_tables = list()
        for item in self.li_table_items:
            if item.table_status == 0:
                li_free_tables.append(item)

        return li_free_tables

    def get_table_item(self, table_num):
        for item in self.li_table_items:
            if item.table_num == str(table_num):
                return item

        return None

    def open_table(self, data):
        if isinstance(data, DataTableItem):
            table_item = None
            for item in self.li_table_items:
                if item.table_id == data.table_id:
                    table_item = item

            table_item.waiter = data.waiter
            table_item.customer_num = int(data.customer_num)
            table_item.deposit = data.deposit
            table_item.memo = data.memo
            if CONFIG.useTemp:
                table_item.table_status = 1
                table_item.order_num = time.strftime('B%Y%m%d') + str(self.order_seq)
                self.order_seq += 1
            else:
                result = HttpService.get_instance().open_table(data.table_id, data.customer_num,
                                                               CtrlFrontLogin.get_instance().get_user(),
                                                               CtrlFrontLogin.get_instance().get_password())
                if result is not None:
                    table_item.table_status = 1
                    table_item.order_id = result
                    table_item.order_num = str(result)

            table_order_tmp = {table_item.table_id: table_item.order_num}
            self.di_table_order.update(table_order_tmp)

        EvtManager.dispatch_event(EnumEvent.EVT_FRONT_PAGE_REFRESH)

    def close_table(self, table_num):
        if CONFIG.useTemp:
            pass
        else:
            result = HttpService.get_instance().close_table(table_num)
            if result:
                for item in self.li_table_items:
                    if item.table_id == table_num:
                        item.table_status = 0
                EvtManager.dispatch_event(EnumEvent.EVT_FRONT_PAGE_REFRESH)

    def change_table(self, src_table_num, dst_table_num):
        src_order_num = None
        if int(src_table_num) in self.di_table_order:
            src_order_num = self.di_table_order[int(src_table_num)]

        src_order_id = None
        table_item = CtrlTableInfo.get_instance().get_table_item(src_table_num)
        if table_item is not None:
            src_order_id = table_item.order_id

        result = HttpService.get_instance().change_table(src_table_num, dst_table_num, src_order_id)
        if result is not None:
            for item in self.li_table_items:
                if item.table_num == src_table_num:
                    item.table_num = dst_table_num
                elif item.table_num == dst_table_num:
                    item.table_num = src_table_num

            if src_order_num is not None:
                self.di_table_order[int(dst_table_num)] = src_order_num
                del self.di_table_order[int(src_table_num)]

            self.li_table_items.sort(lambda x, y: cmp(int(x.table_num), int(y.table_num)))

            EvtManager.dispatch_event(EnumEvent.EVT_FRONT_PAGE_REFRESH)

    def get_order_num(self, table_num):
        if table_num in self.di_table_order:
            return self.di_table_order[table_num]

        return None

    def change_table_status(self, table_num, status):
        for item in self.li_table_items:
            if item.table_id == table_num:
                item.table_status = status
        EvtManager.dispatch_event(EnumEvent.EVT_FRONT_PAGE_REFRESH)


@Singleton
class CtrlDishesInfo():
    def __init__(self):
        self.li_type_items = list()
        self.li_dishes_items = list()
        self.cur_dishes_type = None

    def get_code_by_di(self, dishes_id):
        for item in self.li_dishes_items:
            if item.dishes_id == dishes_id:
                return item.dishes_code

        return None

    def get_type_items(self):
        if len(self.li_type_items) == 0:
            if CONFIG.useTemp:
                for i in range(10):
                    item = DataTypeItem()
                    item.type_id = i + 10000
                    item.type_name = u"菜品" + str(i)
                    self.li_type_items.append(item)
            else:
                result = HttpService.get_instance().get_dishes_type_items()
                if result is not None:
                    for info in result:
                        item = DataTypeItem()
                        item.type_id = info['id']
                        item.type_name = info['vch_name']
                        self.li_type_items.append(item)

        return self.li_type_items

    def set_cur_dishes_type(self, dishes_type):
        self.cur_dishes_type = dishes_type

    def get_dishes_items(self):
        if len(self.li_dishes_items) == 0:
            if CONFIG.useTemp:
                brevity_dict = {0: 'HUG', 1: 'TDS', 2: 'YXRS', 3: 'JTB', 4: 'YJR', 5: 'XJDMG'}
                for i in range(100):
                    item = DataDishesItem()
                    item.dishes_id = i
                    item.dishes_code = str(i + 1)
                    item.dishes_name = u"测试菜" + str(i)
                    item.dishes_type = random.randint(10000, 10009)
                    index_ = random.randint(0, 5)
                    item.dishes_brevity = brevity_dict[index_]
                    self.li_dishes_items.append(item)
            else:
                result = HttpService.get_instance().get_dishes_items()
                if result is not None:
                    for info in result:
                        item = DataDishesItem()
                        item.dishes_id = info['id']
                        item.dishes_code = info['vch_code']
                        item.dishes_name = info['vch_name']
                        item.dishes_type = info['num_category']['id']
                        item.dishes_brevity = info['vch_spell']
                        item.dishes_spec = info['num_spec_id']
                        item.dishes_unit = info['num_unit']
                        item.dishes_style = info['num_style_id']
                        item.dishes_discount = info['num_discount']
                        self.li_dishes_items.append(item)
        else:
            if self.cur_dishes_type is not None:
                li_dishes_items = list()
                for dishes in self.li_dishes_items:
                    if dishes.dishes_type == self.cur_dishes_type or self.cur_dishes_type == 10000:
                        li_dishes_items.append(dishes)

                return li_dishes_items

        return self.li_dishes_items

    def get_dishes_item(self, dishes_code):
        for item in self.li_dishes_items:
            if item.dishes_code == dishes_code:
                return item

        return None

    def search_dishes_item(self, code):
        for item in self.li_dishes_items:
            if item.dishes_code == code or item.dishes_brevity == code:
                return item

        return None


@Singleton
class CtrlOrderInfo():
    def __init__(self):
        self.cur_order_num = None
        self.cur_dishes_key = None
        self.cur_dishes_code = None
        self.di_order_item = dict()

    def get_cur_order_id(self):
        return self.cur_order_num

    def update_checkout_info(self):
        EvtManager.dispatch_event(EnumEvent.EVT_CHECKOUT_INFO_REFRESH)

    def create_order(self, order_num, order_status):
        self.cur_order_num = order_num
        if order_num not in self.di_order_item:
            item = DataOrderItem()
            item.order_num = order_num

            if order_status == 2 or order_status == 3:
                result = HttpService.get_instance().get_order_info(order_num)
                if result is not None:
                    for info in result:
                        dishes_item = DataOrderDishesItem()
                        dishes_item.dishes_code = info["vch_dish_code"]
                        dishes_details = CtrlDishesInfo.get_instance().get_dishes_item(dishes_item.dishes_code)
                        spec_id = info["num_spec_id"]
                        style_id = info["num_style_id"]
                        if dishes_details is not None:
                            for spec in dishes_details.dishes_spec:
                                if spec["id"] == spec_id:
                                    dishes_item.dishes_spec = spec
                            if dishes_details.dishes_style is not None:
                                for style in dishes_details.dishes_style:
                                    if style["id"] == style_id:
                                        dishes_item.dishes_style = style
                        dishes_item.dishes_count = info["num_dish_num"]
                        dishes_item.dishes_demand = info["vch_customized_style"]
                        dishes_key = str(dishes_item.dishes_code) + str(spec_id) + str(style_id)
                        if dishes_key in item.di_place_dishes_items:
                            item.di_place_dishes_items[dishes_key].dishes_count = \
                                item.di_place_dishes_items[dishes_key].dishes_count + dishes_item.dishes_count
                            item.di_place_dishes_items[dishes_key].li_dishes_log_id.append(info["dishId"])
                        else:
                            dishes_item.li_dishes_log_id.append(info["dishId"])
                            order_dishes_item_tmp = {dishes_key: dishes_item}
                            item.di_place_dishes_items.update(order_dishes_item_tmp)

            order_item_tmp = {order_num: item}
            self.di_order_item.update(order_item_tmp)

    def update_order(self):
        for order_num, order_item in self.di_order_item.items():
            result = HttpService.get_instance().get_order_info(order_num)
            if result is not None:
                order_item.di_place_dishes_items.clear()
                for info in result:
                    dishes_item = DataOrderDishesItem()
                    dishes_item.dishes_code = info["vch_dish_code"]
                    dishes_details = CtrlDishesInfo.get_instance().get_dishes_item(dishes_item.dishes_code)
                    spec_id = info["num_spec_id"]
                    style_id = info["num_style_id"]
                    if dishes_details is not None:
                        for spec in dishes_details.dishes_spec:
                            if spec["id"] == spec_id:
                                dishes_item.dishes_spec = spec
                        if dishes_details.dishes_style is not None:
                            for style in dishes_details.dishes_style:
                                if style["id"] == style_id:
                                    dishes_item.dishes_style = style
                    dishes_item.dishes_count = info["num_dish_num"]
                    dishes_item.dishes_demand = info["vch_customized_style"]
                    dishes_key = str(dishes_item.dishes_code) + str(spec_id) + str(style_id)
                    if dishes_key in order_item.di_place_dishes_items:
                        order_item.di_place_dishes_items[dishes_key].dishes_count = \
                            order_item.di_place_dishes_items[dishes_key].dishes_count + dishes_item.dishes_count
                        order_item.di_place_dishes_items[dishes_key].li_dishes_log_id.append(info["dishId"])
                    else:
                        dishes_item.li_dishes_log_id.append(info["dishId"])
                        order_dishes_item_tmp = {dishes_key: dishes_item}
                        order_item.di_place_dishes_items.update(order_dishes_item_tmp)

    def get_order_item(self, order_num):
        if order_num in self.di_order_item:
            return self.di_order_item[order_num]

        return None

    def set_all_discount(self, order_num, discount):
        if order_num in self.di_order_item:
            self.di_order_item[order_num].all_discount = discount

    def set_free_price(self, order_num, price):
        if order_num in self.di_order_item:
            self.di_order_item[order_num].free_price = price

    def get_order_dishes_item(self, order_num):
        if order_num in self.di_order_item:
            if self.cur_dishes_key in self.di_order_item[order_num].di_order_dishes_items:
                return self.di_order_item[order_num].di_order_dishes_items[self.cur_dishes_key]
            elif self.cur_dishes_key in self.di_order_item[order_num].di_place_dishes_items:
                return self.di_order_item[order_num].di_place_dishes_items[self.cur_dishes_key]

        return None

    def set_select_dishes_id(self, dishes_code, dishes_spec_id, dishes_style_id):
        if dishes_code is not None:
            self.cur_dishes_key = str(dishes_code) + str(dishes_spec_id) + str(dishes_style_id)
        else:
            self.cur_dishes_key = None

    def get_select_dishes_id(self):
        if self.cur_dishes_key is not None:
            return str(self.cur_dishes_key)
        return None

    def set_select_dishes_code(self, dishes_code):
        self.cur_dishes_code = dishes_code

    def get_select_dishes_code(self):
        if self.cur_dishes_code is not None:
            return str(self.cur_dishes_code)
        return None

    def get_select_dishes_item(self):
        ordered_dishes_item = DataOrderedDishesItem()
        cur_order_item = self.di_order_item[self.cur_order_num]
        if self.cur_dishes_key in cur_order_item.di_order_dishes_items:
            ordered_dishes_item.dishes_count = cur_order_item.di_order_dishes_items[self.cur_dishes_key].dishes_count
        elif self.cur_dishes_key in cur_order_item.di_place_dishes_items:
            ordered_dishes_item.dishes_count = cur_order_item.di_place_dishes_items[self.cur_dishes_key].dishes_count

        dishes_item = CtrlDishesInfo.get_instance().get_dishes_item(str(self.cur_dishes_key))
        if dishes_item is not None:
            ordered_dishes_item.dishes_name = dishes_item.dishes_name

        return ordered_dishes_item

    def order_dishes(self, dishes_code, spec_id, style_id, str_demand):
        cur_order_item = self.di_order_item[self.cur_order_num]
        dishes_key = str(dishes_code) + str(spec_id["id"]) + (str(style_id["id"]) if style_id is not None else "0")
        if dishes_key not in cur_order_item.di_order_dishes_items:
            item = DataOrderDishesItem()
            item.dishes_code = dishes_code
            item.dishes_count = 1
            item.dishes_spec = spec_id
            item.dishes_style = style_id
            item.dishes_demand = str_demand
            order_dishes_item_tmp = {dishes_key: item}
            cur_order_item.di_order_dishes_items.update(order_dishes_item_tmp)

            self.cur_dishes_key = dishes_key
        else:
            item = cur_order_item.di_order_dishes_items[dishes_key]
            item.dishes_code = dishes_code
            item.dishes_count = 1
            item.dishes_spec = spec_id
            item.dishes_style = style_id
            item.dishes_demand = str_demand

        EvtManager.dispatch_event(EnumEvent.EVT_ORDER_DISHES_ITEMS_REFRESH)

    def delete_dishes(self, del_reason=""):
        cur_order_item = self.di_order_item[self.cur_order_num]
        if self.cur_dishes_key in cur_order_item.di_order_dishes_items:
            del cur_order_item.di_order_dishes_items[self.cur_dishes_key]

        if self.cur_dishes_key in cur_order_item.di_place_dishes_items:
            dishes_item = cur_order_item.di_place_dishes_items[self.cur_dishes_key]
            for dishes_log_id in dishes_item.li_dishes_log_id:
                HttpService.get_instance().del_dishes(dishes_log_id, dishes_item.dishes_code, 1, del_reason)
            del cur_order_item.di_place_dishes_items[self.cur_dishes_key]

            self.cur_dishes_key = None
        EvtManager.dispatch_event(EnumEvent.EVT_ORDER_DISHES_ITEMS_REFRESH)

    def plus_dishes(self):
        cur_order_item = self.di_order_item[self.cur_order_num]
        if self.cur_dishes_key in cur_order_item.di_order_dishes_items:
            cur_order_item.di_order_dishes_items[self.cur_dishes_key].dishes_count += 1

            EvtManager.dispatch_event(EnumEvent.EVT_ORDER_DISHES_ITEMS_REFRESH)

    def minus_dishes(self):
        cur_order_item = self.di_order_item[self.cur_order_num]
        if self.cur_dishes_key in cur_order_item.di_order_dishes_items:
            if cur_order_item.di_order_dishes_items[self.cur_dishes_key].dishes_count <= 1:
                del cur_order_item.di_order_dishes_items[self.cur_dishes_key]
                self.cur_dishes_key = None
            else:
                cur_order_item.di_order_dishes_items[self.cur_dishes_key].dishes_count -= 1

        if self.cur_dishes_key in cur_order_item.di_place_dishes_items:
            dishes_item = cur_order_item.di_order_dishes_items[self.cur_dishes_key]
            if len(dishes_item.li_dishes_log_id) > 0:
                HttpService.get_instance().del_dishes(dishes_item.li_dishes_log_id[0], dishes_item.dishes_code, 1, "")
                del dishes_item.li_dishes_log_id[0]

            if cur_order_item.di_order_dishes_items[self.cur_dishes_key].dishes_count <= 1:
                del cur_order_item.di_order_dishes_items[self.cur_dishes_key]
                self.cur_dishes_key = None
            else:
                cur_order_item.di_order_dishes_items[self.cur_dishes_key].dishes_count -= 1

            EvtManager.dispatch_event(EnumEvent.EVT_ORDER_DISHES_ITEMS_REFRESH)

    def mod_dishes(self, count):
        cur_order_item = self.di_order_item[self.cur_order_num]
        if self.cur_dishes_key in cur_order_item.di_order_dishes_items and count > 0:
            cur_order_item.di_order_dishes_items[self.cur_dishes_key].dishes_count = count

            EvtManager.dispatch_event(EnumEvent.EVT_ORDER_DISHES_ITEMS_REFRESH)

    def get_order_dishes_items(self, order_num):
        li_ordered_items = list()
        try:
            cur_order_item = self.di_order_item[order_num]
            cur_order_item.order_money = 0
            cur_order_item.place_money = 0
            for (key, item) in cur_order_item.di_order_dishes_items.items():
                ordered_item = DataOrderedDishesItem()
                dishes_item = CtrlDishesInfo.get_instance().get_dishes_item(str(item.dishes_code))
                ordered_item.dishes_code = dishes_item.dishes_code
                ordered_item.dishes_spec_id = item.dishes_spec['id']
                if item.dishes_style is not None:
                    ordered_item.dishes_style_id = item.dishes_style['id'] if len(item.dishes_style) > 0 \
                        else 0
                ordered_item.dishes_name = dishes_item.dishes_name
                ordered_item.dishes_spec = item.dishes_spec['vch_name']
                ordered_item.dishes_unit = dishes_item.dishes_unit
                ordered_item.dishes_count = item.dishes_count
                ordered_item.dishes_amount = item.dishes_spec['num_price']
                add_price = 0
                if item.dishes_style is not None:
                    if len(item.dishes_style) > 0 and item.dishes_style['ch_mountadd'] == 1:
                        add_price = item.dishes_style['num_priceadd']

                ordered_item.dishes_real_amount = item.dishes_spec['num_price'] + add_price
                ordered_item.dishes_real_amount = ordered_item.dishes_real_amount * ordered_item.dishes_count
                ordered_item.dishes_status = u"新增"

                li_ordered_items.append(ordered_item)
                cur_order_item.order_money = cur_order_item.order_money + ordered_item.dishes_real_amount
            for (key, item) in cur_order_item.di_place_dishes_items.items():
                ordered_item = DataOrderedDishesItem()
                dishes_item = CtrlDishesInfo.get_instance().get_dishes_item(str(item.dishes_code))
                ordered_item.dishes_code = dishes_item.dishes_code
                ordered_item.dishes_spec_id = item.dishes_spec['id']
                if item.dishes_style is not None:
                    ordered_item.dishes_style_id = item.dishes_style['id'] if len(item.dishes_style) > 0 \
                        else 0
                ordered_item.dishes_name = dishes_item.dishes_name
                ordered_item.dishes_spec = item.dishes_spec['vch_name']
                ordered_item.dishes_unit = dishes_item.dishes_unit
                ordered_item.dishes_count = item.dishes_count
                ordered_item.dishes_amount = item.dishes_spec['num_price']
                add_price = 0
                if item.dishes_style is not None:
                    if len(item.dishes_style) > 0 and item.dishes_style['ch_mountadd'] == 1:
                        add_price = item.dishes_style['num_priceadd']

                ordered_item.dishes_real_amount = item.dishes_spec['num_price'] + add_price
                ordered_item.dishes_real_amount = ordered_item.dishes_real_amount * ordered_item.dishes_count
                ordered_item.dishes_status = u"已落单"

                li_ordered_items.append(ordered_item)
                cur_order_item.place_money = cur_order_item.place_money + ordered_item.dishes_real_amount
        except Exception, ex:
            Log.info("get_order_dishes_items error")
            print Exception, ":", ex

        return li_ordered_items

    def get_place_order_dishes_items(self, order_num):
        li_ordered_items = list()
        is_place_order = True
        try:
            cur_order_item = self.di_order_item[order_num]
            cur_order_item.order_money = 0
            cur_order_item.place_money = 0
            if len(cur_order_item.di_place_dishes_items) > 0:
                is_place_order = False

            for (key, item) in cur_order_item.di_order_dishes_items.items():
                ordered_item = DataOrderedDishesItem()
                dishes_item = CtrlDishesInfo.get_instance().get_dishes_item(str(item.dishes_code))
                ordered_item.dishes_code = dishes_item.dishes_code
                ordered_item.dishes_spec_id = item.dishes_spec['id']
                if item.dishes_style is not None:
                    ordered_item.dishes_style_id = item.dishes_style['id'] if len(item.dishes_style) > 0 \
                        else 0
                ordered_item.dishes_name = dishes_item.dishes_name
                ordered_item.dishes_spec = item.dishes_spec['vch_name']
                ordered_item.dishes_unit = dishes_item.dishes_unit
                ordered_item.dishes_count = item.dishes_count
                ordered_item.dishes_amount = item.dishes_spec['num_price']
                add_price = 0
                if item.dishes_style is not None:
                    if len(item.dishes_style) > 0 and item.dishes_style['ch_mountadd'] == 1:
                        add_price = item.dishes_style['num_priceadd']

                ordered_item.dishes_real_amount = item.dishes_spec['num_price'] + add_price
                ordered_item.dishes_real_amount = ordered_item.dishes_real_amount * ordered_item.dishes_count
                ordered_item.dishes_status = u"新增"

                li_ordered_items.append(ordered_item)
                cur_order_item.order_money = cur_order_item.order_money + ordered_item.dishes_real_amount
        except Exception, ex:
            print Exception, ":", ex

        return is_place_order, li_ordered_items

    def place_order(self, table_id, order_id):
        is_place_order, cur_order_item = self.get_place_order_dishes_items(self.cur_order_num)
        li_json_str = "["
        try:
            for item in cur_order_item:
                if len(li_json_str) > 5:
                    li_json_str = li_json_str + ","
                di_json_str = "{\"code\":" + item.dishes_code + ",\"spec\":" + str(item.dishes_spec_id) + ",\"style\":"\
                    + str(item.dishes_style_id) + ",\"num\":" + str(item.dishes_count) + ",\"customizedStyle\":\"" \
                    + item.customer_demand + "\"}"
                li_json_str = li_json_str + di_json_str
        except Exception, ex:
            print Exception, ":", ex
        li_json_str = li_json_str + "]"
        if CONFIG.useTemp:
            pass
        else:
            if is_place_order:
                result = HttpService.get_instance().place_order(table_id, order_id, li_json_str)
            else:
                result = HttpService.get_instance().add_dishes(table_id, order_id, li_json_str)

            if result is not None:
                cur_order_item = self.di_order_item[self.cur_order_num]
                for (key, item) in cur_order_item.di_order_dishes_items.items():
                    cur_place_item_tmp = {key: item}
                    cur_order_item.di_place_dishes_items.update(cur_place_item_tmp)
                cur_order_item.di_order_dishes_items.clear()

                for info in result:
                    dishes_key = str(info["code"]) + str(info["spec"]) + str(info["style"])
                    if dishes_key in cur_order_item.di_place_dishes_items:
                        cur_order_item.di_place_dishes_items[dishes_key].li_dishes_log_id.append(info["logDishId"])

            CtrlTableInfo.get_instance().change_table_status(table_id, 2)

            EvtManager.dispatch_event(EnumEvent.EVT_ORDER_DISHES_ITEMS_REFRESH)

    def check_out(self, table_id, order_id, order_code, bill_num):
        order_item = CtrlOrderInfo.get_instance().get_order_item(order_code)
        if order_item is not None:
            order_item.bill_num = bill_num
            '''calculate the real pay of bill'''
            order_item.order_money = (order_item.place_money * order_item.all_discount) - order_item.free_price
            '''send request to remote service'''
            HttpService.get_instance().check_out(table_id, order_id, order_item.all_discount, order_item.free_price,
                                                 CtrlFrontLogin.get_instance().get_user(), 1, order_item.cashier_cash,
                                                 order_item.cashier_coupon, order_item.cashier_membership,
                                                 order_item.cashier_pos, order_item.cashier_group,
                                                 order_item.cashier_credit, order_item.cashier_boss_sign,
                                                 order_item.bill_num)

            '''change table status to waiting clean state'''
            CtrlTableInfo.get_instance().change_table_status(table_id, 3)


@Singleton
class CtrlWorker():
    def __init__(self):
        self.timer = Timer(1, self.on_timer)
        self.timer.start()
        self.is_run = True

    def start(self):
        self.timer.start()

    def stop(self):
        self.is_run = False
        self.timer.cancel()

    def on_timer(self):
        while self.is_run:
            CtrlOrderInfo.get_instance().update_order()
            time.sleep(2)