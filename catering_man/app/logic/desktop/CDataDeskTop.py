#!/usr/bin/env python
#_*_ encoding=utf-8 _*_
from framework.CSingleton import CSingleton

class CDataDeskTop(CSingleton):
    m_frame_width = 800
    m_frame_height = 600
    m_selected_item = "dining_table"
    
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
    def SetSelectedItem(strItem):
       CDataDeskTop.m_selected_item = strItem