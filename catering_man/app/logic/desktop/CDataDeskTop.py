#!/usr/bin/env python
#_*_ encoding=utf-8 _*_
from framework.CSingleton import CSingleton

class CDataDeskTop(CSingleton):
    m_frame_width = 800
    m_frame_height = 600
    m_selected_item = 5
    
    def __init__(self):
        pass
    
    def __def__(self):
        pass

    @staticmethod
    def GetFrameSize():
        return CDataDeskTop.m_frame_width, CDataDeskTop.m_frame_height
    
    @staticmethod
    def SetFrameSize(x, y):
        CDataDeskTop.m_frame_width = x
        CDataDeskTop.m_frame_height = y
        
    @staticmethod
    def GetSelectedItem():
        return CDataDeskTop.m_selected_item
    
    @staticmethod
    def SetSelectedItem(strItem = 5):
        # 0 for dining room setting
        # 1 for dishes publishing
        # 2 for employee manager
        # 3 for printer setting
        # 4 for report form manager
        # 5 for system setting
        CDataDeskTop.m_selected_item = strItem