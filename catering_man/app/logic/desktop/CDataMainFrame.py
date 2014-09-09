#_*_ encoding=utf-8 _*_
#!/usr/bin/env python
from framework.CSingleton import CSingleton

class CDataMainFrame(CSingleton):
    m_frame_width = 800
    m_frame_height = 600
    m_selected_item = "dining_table"
    
    def __init__(self):
        pass
    
    def __def__(self):
        pass

    @staticmethod
    def GetFrameSize():
        return CDataMainFrame.m_frame_width, CDataMainFrame.m_frame_height
    
    @staticmethod
    def SetFrameSize(x, y):
        CDataMainFrame.m_frame_width = x
        CDataMainFrame.m_frame_height = y
        
    @staticmethod
    def GetSelectedItem():
        return CDataMainFrame.m_selected_item
    
    @staticmethod
    def SetSelectedItem(strItem):
       CDataMainFrame.m_selected_item = strItem