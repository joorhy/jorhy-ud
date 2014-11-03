#!/usr/bin/env python
#_*_ encoding=utf-8 _*_
from framework.core import Singleton


@Singleton
class CtrlHomePage():
    def __init__(self):
        self.frame_width = 800
        self.frame_height = 600
        self.selected_item = 5

    def __def__(self):
        pass

    def get_screen_size(self):
        return self.frame_width, self.frame_height

    def set_screen_size(self, x, y):
        self.frame_width = x
        self.frame_height = y

    def get_selected_item(self):
        return self.selected_item

    def set_selected_item(self, item=5):
        # 0 for dining room setting
        # 1 for dishes publishing
        # 2 for employee manager
        # 3 for printer setting
        # 4 for report form manager
        # 5 for system setting
        self.selected_item = item
