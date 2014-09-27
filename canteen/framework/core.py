#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import wx


def single_get_first(unicode1): 
    str1 = unicode1.encode('gbk') 
    try:         
        ord(str1) 
        return str1 
    except: 
        asc = ord(str1[0]) * 256 + ord(str1[1]) - 65536 
        if (asc >= -20319) and (asc <= -20284):
            return 'A' 
        if (asc >= -20283) and (asc <= -19776):
            return 'B' 
        if (asc >= -19775) and (asc <= -19219):
            return 'C' 
        if (asc >= -19218) and (asc <= -18711):
            return 'D' 
        if (asc >= -18710) and (asc <= -18527):
            return 'E' 
        if (asc >= -18526) and (asc <= -18240):
            return 'F' 
        if (asc >= -18239) and (asc <= -17923):
            return 'G' 
        if (asc >= -17922) and (asc <= -17418):
            return 'H' 
        if (asc >= -17417) and (asc <= -16475):
            return 'J' 
        if (asc >= -16474) and (asc <= -16213):
            return 'K' 
        if (asc >= -16212) and (asc <= -15641):
            return 'L' 
        if (asc >= -15640) and (asc <= -15166):
            return 'M' 
        if (asc >= -15165) and (asc <= -14923):
            return 'N' 
        if (asc >= -14922) and (asc <= -14915):
            return 'O' 
        if (asc >= -14914) and (asc <= -14631):
            return 'P' 
        if (asc >= -14630) and (asc <= -14150):
            return 'Q' 
        if (asc >= -14149) and (asc <= -14091):
            return 'R' 
        if (asc >= -14090) and (asc <= -13119):
            return 'S' 
        if (asc >= -13118) and (asc <= -12839):
            return 'T' 
        if (asc >= -12838) and (asc <= -12557):
            return 'W' 
        if (asc >= -12556) and (asc <= -11848):
            return 'X' 
        if (asc >= -11847) and (asc <= -11056):
            return 'Y' 
        if (asc >= -11055) and (asc <= -10247):
            return 'Z' 
        return ''


class BrevityCode():
    def __init__(self):
        pass

    @classmethod
    def multi_get_letter(cls, str_input):
        if isinstance(str_input, unicode): 
            unicode_str = str_input 
        else: 
            try: 
                unicode_str = str_input.decode('utf8') 
            except:
                try: 
                    unicode_str = str_input.decode('gbk') 
                except:
                    print 'unknown coding' 
                    return
    
        return_list = [] 
        for one_unicode in unicode_str: 
            return_list.append(single_get_first(one_unicode)) 
            
        brevity_str = ''
        for i in return_list:
            brevity_str = brevity_str + i
            
        return brevity_str


class Singleton(object):  
    def __new__(cls, *args, **kw):  
        if not hasattr(cls, '_instance'):  
            orig = super(Singleton, cls)  
            cls._instance = orig.__new__(cls, *args, **kw)
            
        return cls._instance 


class MyEvent(wx.PyEvent):
    def __init__(self, evt_id, evt_data):
        wx.PyEvent.__init__(self)
        self.SetEventType(evt_id)
        self.data = evt_data
        
evt_map = dict()


class EvtManager(Singleton):
    @classmethod
    def add_listener(cls, win, evt_id, func):
        win.Connect(-1, -1, evt_id, func)    
        if evt_id in evt_map:
            evt_map[evt_id].append(win)
        else:
            list_tmp = list()
            list_tmp.append(win)
            evt_map_tmp = {evt_id: list_tmp}
            evt_map.update(evt_map_tmp)
            
    @classmethod
    def remove_listener(cls, win, evt_id, func):
        pass
    
    @classmethod
    def dispatch_event(cls, evt_id, evt_data=""):
        if evt_id in evt_map:
            for item in evt_map[evt_id]:
                wx.PostEvent(item, MyEvent(evt_id, evt_data))