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
        login_url = "/canteen/user/signin?para={\"username\":\"" + user + "\",\"password\":\"" + password + "\"}"
        self.conn = httplib.HTTPConnection(self.ip_address, self.port)
        self.conn.request("GET", login_url)
        response = self.conn.getresponse()
        if response.status == 200:
            json_txt = response.read()
            result = json.loads(json_txt)
            return result['Registration']

        return False

    def get_table_items(self):
        table_items_url = "/canteen/table/allStatus"
        self.conn = httplib.HTTPConnection(self.ip_address, self.port)
        self.conn.request("GET", table_items_url)
        response = self.conn.getresponse()
        if response.status == 200:
            json_txt = response.read()
            result = json.loads(json_txt)
            return result['list']

        return None

    def get_waiter_items(self):
        waiter_items_url = "/canteen/user/waiters"
        self.conn = httplib.HTTPConnection(self.ip_address, self.port)
        self.conn.request("GET", waiter_items_url)
        response = self.conn.getresponse()
        if response.status == 200:
            json_txt = response.read()
            result = json.loads(json_txt)
            return result['list']

        return None

    def open_table(self, table_id, customer_num, user, password):
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

        return None

    def close_table(self, table_id):
        close_table_url = "/canteen/table/reset?para={\"tableId\":" + str(table_id) + "}"
        self.conn = httplib.HTTPConnection(self.ip_address, self.port)
        self.conn.request("GET", close_table_url)
        response = self.conn.getresponse()
        if response.status == 200:
            json_txt = response.read()
            result = json.loads(json_txt)
            return result['msg']

        return False

    def get_dishes_items(self):
        dishes_url = "/canteen/menu/loadAll"
        self.conn = httplib.HTTPConnection(self.ip_address, self.port)
        self.conn.request("GET", dishes_url)
        response = self.conn.getresponse()
        if response.status == 200:
            json_txt = response.read()
            result = json.loads(json_txt)
            return result['allFiles']

        return None

    def get_dishes_type_items(self):
        dishes_type_url = "/canteen/menu/category"
        self.conn = httplib.HTTPConnection(self.ip_address, self.port)
        self.conn.request("GET", dishes_type_url)
        response = self.conn.getresponse()
        if response.status == 200:
            json_txt = response.read()
            result = json.loads(json_txt)
            return result['category']

        return None

    def place_order(self, table_id, order_id, li_order):
        place_order_url = "/canteen/table/order?para={\"tableId\":" + str(table_id) + ",\"orderId\":" + str(order_id) \
                          + ",\"dish\":" + li_order + "}"
        self.conn = httplib.HTTPConnection(self.ip_address, self.port)
        self.conn.request("GET", place_order_url)
        response = self.conn.getresponse()
        if response.status == 200:
            json_txt = response.read()
            result = json.loads(json_txt)
            return result["list"]

        return None

    def add_dishes(self, table_id, order_id, li_order):
        add_dishes_url = "/canteen/table/add?para={\"tableId\":" + str(table_id) + ",\"orderId\":" + str(order_id) \
                         + ",\"dish\":" + li_order + "}"
        self.conn = httplib.HTTPConnection(self.ip_address, self.port)
        self.conn.request("GET", add_dishes_url)
        response = self.conn.getresponse()
        if response.status == 200:
            json_txt = response.read()
            result = json.loads(json_txt)
            return result["list"]

        return None

    def del_dishes(self, dishes_id, dishes_code, count, desc):
        del_dishes_url = "/canteen/table/dishBack?para={\"dishId\":" + str(dishes_id) + ",\"dishCode\":" \
                         + str(dishes_code) + ",\"number\":" + str(count) + ",\"desc\":\"" + desc + "\"}"
        self.conn = httplib.HTTPConnection(self.ip_address, self.port)
        self.conn.request("GET", del_dishes_url)
        response = self.conn.getresponse()
        if response.status == 200:
            json_txt = response.read()
            result = json.loads(json_txt)
            return result

        return None

    def check_out(self, table_id, order_id, all_discount, free_price, checkout_person, check_type):
        check_out_url = "/canteen/order/checkOut?para={\"tableId\":" + str(table_id) + ",\"orderId\":" \
                        + str(order_id) + ",\"checkoutType\":" + str(check_type) + ",\"cashier\":\""\
                        + checkout_person + "\",\"discountRate\":" \
                        + str(all_discount) + ",\"discountAmount\":" + str(free_price) + "}"
        self.conn = httplib.HTTPConnection(self.ip_address, self.port)
        self.conn.request("GET", check_out_url)
        response = self.conn.getresponse()
        if response.status == 200:
            json_txt = response.read()
            result = json.loads(json_txt)
            return result

        return None

    def get_order_info(self, order_num):
        order_info_url = "/canteen/order/consumption?para={\"orderCode\":" + order_num + "}"
        self.conn = httplib.HTTPConnection(self.ip_address, self.port)
        self.conn.request("GET", order_info_url)
        response = self.conn.getresponse()
        if response.status == 200:
            json_txt = response.read()
            result = json.loads(json_txt)
            return result["consumption"]

        return None