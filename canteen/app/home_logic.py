#!/usr/bin/env python
#_*_ encoding=utf-8 _*_


class CtrlHomePage():
    m_frame_width = 800
    m_frame_height = 600
    m_selected_item = 5

    def __init__(self):
        pass

    def __def__(self):
        pass

    @classmethod
    def get_screen_size(cls):
        return CtrlHomePage.m_frame_width, CtrlHomePage.m_frame_height

    @classmethod
    def set_screen_size(cls, x, y):
        CtrlHomePage.m_frame_width = x
        CtrlHomePage.m_frame_height = y

    @classmethod
    def get_selected_item(cls):
        return CtrlHomePage.m_selected_item

    @classmethod
    def set_selected_item(cls, item=5):
        # 0 for dining room setting
        # 1 for dishes publishing
        # 2 for employee manager
        # 3 for printer setting
        # 4 for report form manager
        # 5 for system setting
        CtrlHomePage.m_selected_item = item
