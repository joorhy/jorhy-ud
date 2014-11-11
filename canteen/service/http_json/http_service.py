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
        self.conn.request("GET", login_url)
        response = self.conn.getresponse()
        if response.status == 200:
            json_txt = response.read()
            result = json.loads(json_txt)
            return result['Registration']

        return False

    def get_table_items(self):
        table_items_url = "/canteen/table/allStatus"
        self.conn.request("GET", table_items_url)
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
        self.conn.request("GET", open_table_url)
        response = self.conn.getresponse()
        if response.status == 200:
            json_txt = response.read()
            result = json.loads(json_txt)
            return result['orderId']

        return None

    def close_table(self, table_id):
        close_table_url = "/canteen/table/reset?para={\"tableId\":" + str(table_id) + "}"
        self.conn.request("GET", close_table_url)
        response = self.conn.getresponse()
        if response.status == 200:
            json_txt = response.read()
            result = json.loads(json_txt)
            return result['msg']

        return False

    def get_dishes_items(self):
        dishes_url = "/canteen/menu/loadAll"
        self.conn.request("GET", dishes_url)
        response = self.conn.getresponse()
        if response.status == 200:
            json_txt = response.read()
            result = json.loads(json_txt)
            return result['allFiles']

        return None

    def get_dishes_type_items(self):
        dishes_type_url = "/canteen/menu/category"
        self.conn.request("GET", dishes_type_url)
        response = self.conn.getresponse()
        if response.status == 200:
            json_txt = response.read()
            result = json.loads(json_txt)
            return result['category']

        return None

    def place_order(self, table_id, order_id, li_order, user, password):
        place_order_url = "/canteen/table/order?para={\"tableId\":" + str(table_id) + ",\"orderId\":" + str(order_id) \
                          + ",\"dish\":" + li_order + ",\"signIn\":{\"username\":\"" + user + "\",\"password\":\"" \
                          + password + "\"}}"

        self.conn.request("GET", place_order_url)
        response = self.conn.getresponse()
        if response.status == 200:
            json_txt = response.read()
            result = json.loads(json_txt)
            return result

        return None

    def check_out(self, table_id, order_id):
        check_out_url = "/canteen/table/checkOut?para={\"tableId\":" + str(table_id) + ",\"orderId\":" \
                        + str(order_id) + "}"
        self.conn.request("GET", check_out_url)
        response = self.conn.getresponse()
        if response.status == 200:
            json_txt = response.read()
            result = json.loads(json_txt)
            return result

        return None