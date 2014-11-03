# -*- coding: utf-8 -*-
#!/usr/bin/env python

from framework.core import Singleton

import httplib
import json


@Singleton
class HttpService():
    def __init__(self):
        self.ip_address = '192.168.123.112'
        self.port = '8080'
        self.conn = httplib.HTTPConnection(self.ip_address, self.port)

    def login(self, user, password):
        login_url = "/canteen/user/signin?para={\"username\":\"" + user + "\",\"password\":\"" + password + "\"}"
        self.conn.request("POST", login_url)
        response = self.conn.getresponse()
        if response.status == 200:
            json_txt = response.read()
            result = json.loads(json_txt)
            return result['Registration']

        return False
