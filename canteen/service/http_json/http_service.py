# -*- coding: utf-8 -*-
#!/usr/bin/env python

from framework.core import Singleton

import httplib
import json


@Singleton
class HttpService():
    def __init__(self):
        self.ip_address = None
        self.port = None
        self.conn = None

    def initialize(self, address, port):
        self.ip_address = address
        self.port = port
        self.conn = httplib.HTTPConnection(self.ip_address, self.port)

    def login(self, user, password):
        try:
            login_url = "/canteen/user/signin?para={\"username\":\"" + user + "\",\"password\":\"" + password + "\"}"
            self.conn = httplib.HTTPConnection(self.ip_address, self.port)
            self.conn.request("GET", login_url)
            response = self.conn.getresponse()
            if response.status == 200:
                json_txt = response.read()
                result = json.loads(json_txt)
                return result['Registration']
        except Exception, ex:
            print Exception, ":", ex
            return False

        return False

    def get_table_items(self):
        try:
            table_items_url = "/canteen/table/allStatus"
            self.conn = httplib.HTTPConnection(self.ip_address, self.port)
            self.conn.request("GET", table_items_url)
            response = self.conn.getresponse()
            if response.status == 200:
                json_txt = response.read()
                result = json.loads(json_txt)
                return result['list']
        except Exception, ex:
            print Exception, ":", ex
            return None

        return None

    def get_waiter_items(self):
        try:
            waiter_items_url = "/canteen/user/waiters"
            self.conn = httplib.HTTPConnection(self.ip_address, self.port)
            self.conn.request("GET", waiter_items_url)
            response = self.conn.getresponse()
            if response.status == 200:
                json_txt = response.read()
                result = json.loads(json_txt)
                return result['list']
        except Exception, ex:
            print Exception, ":", ex
            return None

        return None

    def open_table(self, table_id, customer_num, user, password):
        try:
            open_table_url = "/canteen/table/open?para={\"tableId\":"\
                             + str(table_id) + ",\"peopleNum\":" + str(customer_num) + "}&signIn={\"username\":\""\
                             + user + "\",\"password\":\"" + password + "\"}"
            self.conn = httplib.HTTPConnection(self.ip_address, self.port)
            self.conn.request("GET", open_table_url)
            response = self.conn.getresponse()
            if response.status == 200:
                json_txt = response.read()
                result = json.loads(json_txt)
                return result['orderId']
        except Exception, ex:
            print Exception, ":", ex
            return None

        return None

    def change_table(self, src_table_id, dst_table_id, order_id):
        try:
            change_table_url = "/canteen/table/alternate?para={\"tableIdPre\":" + str(src_table_id) + \
                               ",\"tableIdNow\":" + str(dst_table_id) + ",\"orderId\":" + str(order_id) + "}"
            self.conn = httplib.HTTPConnection(self.ip_address, self.port)
            self.conn.request("GET", change_table_url)
            response = self.conn.getresponse()
            if response.status == 200:
                json_txt = response.read()
                result = json.loads(json_txt)
                return result['msg']
        except Exception, ex:
            print Exception, ":", ex
            return None

        return None

    def close_table(self, table_id):
        try:
            close_table_url = "/canteen/table/reset?para={\"tableId\":" + str(table_id) + "}"
            self.conn = httplib.HTTPConnection(self.ip_address, self.port)
            self.conn.request("GET", close_table_url)
            response = self.conn.getresponse()
            if response.status == 200:
                json_txt = response.read()
                result = json.loads(json_txt)
                return result['msg']
        except Exception, ex:
            print Exception, ":", ex
            return False

        return False

    def get_dishes_items(self):
        try:
            dishes_url = "/canteen/menu/loadAll"
            self.conn = httplib.HTTPConnection(self.ip_address, self.port)
            self.conn.request("GET", dishes_url)
            response = self.conn.getresponse()
            if response.status == 200:
                json_txt = response.read()
                result = json.loads(json_txt)
                return result['allFiles']
        except Exception, ex:
            print Exception, ":", ex
            return None

        return None

    def get_dishes_type_items(self):
        try:
            dishes_type_url = "/canteen/menu/category"
            self.conn = httplib.HTTPConnection(self.ip_address, self.port)
            self.conn.request("GET", dishes_type_url)
            response = self.conn.getresponse()
            if response.status == 200:
                json_txt = response.read()
                result = json.loads(json_txt)
                return result['category']
        except Exception, ex:
            print Exception, ":", ex
            return None

        return None

    def place_order(self, table_id, order_id, li_order):
        try:
            place_order_url = "/canteen/table/order?para={\"tableId\":" + str(table_id) + ",\"orderId\":" \
                              + str(order_id) + ",\"dish\":" + li_order + "}"
            self.conn = httplib.HTTPConnection(self.ip_address, self.port)
            self.conn.request("GET", place_order_url)
            response = self.conn.getresponse()
            if response.status == 200:
                json_txt = response.read()
                result = json.loads(json_txt)
                return result["list"]
        except Exception, ex:
            print Exception, ":", ex
            return None

        return None

    def add_dishes(self, table_id, order_id, li_order):
        try:
            add_dishes_url = "/canteen/table/add?para={\"tableId\":" + str(table_id) + ",\"orderId\":" + str(order_id) \
                             + ",\"dish\":" + li_order + "}"
            self.conn = httplib.HTTPConnection(self.ip_address, self.port)
            self.conn.request("GET", add_dishes_url)
            response = self.conn.getresponse()
            if response.status == 200:
                json_txt = response.read()
                result = json.loads(json_txt)
                return result["list"]
        except Exception, ex:
            print Exception, ":", ex
            return None

        return None

    def del_dishes(self, order_id, dishes_id, dishes_code, count, desc):
        try:
            del_dishes_url = "/canteen/table/dishBack?para={\"orderId\":" + str(order_id) + ",\"dishId\":" \
                             + str(dishes_id) + ",\"dishCode\":" + str(dishes_code) + ",\"number\":" \
                             + str(count) + ",\"desc\":\"" + desc + "\"}"
            self.conn = httplib.HTTPConnection(self.ip_address, self.port)
            self.conn.request("GET", del_dishes_url)
            response = self.conn.getresponse()
            if response.status == 200:
                json_txt = response.read()
                result = json.loads(json_txt)
                return result
        except Exception, ex:
            print Exception, ":", ex
            return None

        return None

    def check_out(self, table_id, order_id, all_discount, free_price, checkout_person, check_type, cash, coupon,
                  membership, pos, group, credit, boss_sign, bill_num):
        try:
            check_out_url = "/canteen/order/checkOut?para={\"tableId\":" + str(table_id) + ",\"orderId\":" \
                            + str(order_id) + ",\"checkoutType\":" + str(check_type) + ",\"cashier\":\"" \
                            + checkout_person + "\",\"discountRate\":" + str(all_discount) + ",\"discountAmount\":" \
                            + str(free_price) + ",\"payYhq\":" + str(coupon) + ",\"payHyk\":" + str(membership) \
                            + ",\"payXj\":" + str(cash) + ",\"payPos\":" + str(pos) + ",\"payTg\":" + str(group) \
                            + ",\"payGz\":" + str(credit) + ",\"payQd\":" + str(boss_sign) + ",\"payFp\":" \
                            + str(bill_num) + "}"
            self.conn = httplib.HTTPConnection(self.ip_address, self.port)
            self.conn.request("GET", check_out_url)
            response = self.conn.getresponse()
            if response.status == 200:
                json_txt = response.read()
                result = json.loads(json_txt)
                return result
        except Exception, ex:
            print Exception, ":", ex
            return None

        return None

    def prev_print(self, table_id, order_id, all_discount, free_price, checkout_person, check_type, cash, coupon,
                   membership, pos, group, credit, boss_sign):
        try:
            check_out_url = "/canteen/order/prePrint?para={\"tableId\":" + str(table_id) + ",\"orderId\":" \
                            + str(order_id) + ",\"checkoutType\":" + str(check_type) + ",\"cashier\":\"" \
                            + checkout_person + "\",\"discountRate\":" + str(all_discount) + ",\"discountAmount\":" \
                            + str(free_price) + ",\"payYhq\":" + str(coupon) + ",\"payHyk\":" + str(membership) \
                            + ",\"payXj\":" + str(cash) + ",\"payPos\":" + str(pos) + ",\"payTg\":" + str(group) \
                            + ",\"payGz\":" + str(credit) + ",\"payQd\":" + str(boss_sign) + ",\"payFp\":" \
                            + '0' + "}"
            print check_out_url
            self.conn = httplib.HTTPConnection(self.ip_address, self.port)
            self.conn.request("GET", check_out_url)
            response = self.conn.getresponse()
            if response.status == 200:
                json_txt = response.read()
                result = json.loads(json_txt)
                return result
        except Exception, ex:
            print Exception, ":", ex
            return None

        return None

    def get_order_info(self, order_num):
        try:
            order_info_url = "/canteen/order/consumption?para={\"orderCode\":" + order_num + "}"
            self.conn = httplib.HTTPConnection(self.ip_address, self.port)
            self.conn.request("GET", order_info_url)
            response = self.conn.getresponse()
            if response.status == 200:
                json_txt = response.read()
                result = json.loads(json_txt)
                return result["consumption"]
        except Exception, ex:
            print Exception, ":", ex
            return None

        return None