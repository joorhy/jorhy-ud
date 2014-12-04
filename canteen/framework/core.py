#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import wx

import logging
import os


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

    @staticmethod
    def multi_get_letter(str_input):
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


class Singleton:
    """
    A non-thread-safe helper class to ease implementing singletons.
    This should be used as a decorator -- not a metaclass -- to the
    class that should be a singleton.

    The decorated class can define one `__init__` function that
    takes only the `self` argument. Other than that, there are
    no restrictions that apply to the decorated class.

    To get the singleton instance, use the `Instance` method. Trying
    to use `__call__` will result in a `TypeError` being raised.

    Limitations: The decorated class cannot be inherited from.

    """

    def __init__(self, decorated):
        self._decorated = decorated
        self._instance = None

    def get_instance(self):
        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.

        """
        if self._instance is not None:
            return self._instance
        else:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)


class MyEvent(wx.PyEvent):
    def __init__(self, evt_id, evt_data):
        wx.PyEvent.__init__(self)
        self.SetEventType(evt_id)
        self.data = evt_data
        
evt_map = dict()


class EvtManager():
    def __init__(self):
        pass

    @staticmethod
    def add_listener(win, evt_id, func):
        win.Connect(-1, -1, evt_id, func)    
        if evt_id in evt_map:
            evt_map[evt_id].append(win)
        else:
            list_tmp = list()
            list_tmp.append(win)
            evt_map_tmp = {evt_id: list_tmp}
            evt_map.update(evt_map_tmp)
            
    @staticmethod
    def remove_listener(win, evt_id, func):
        pass
    
    @staticmethod
    def dispatch_event(evt_id, evt_data=""):
        if evt_id in evt_map:
            for item in evt_map[evt_id]:
                wx.PostEvent(item, MyEvent(evt_id, evt_data))


class TreeImage(Singleton):
    def __init__(self):
        isz = (16, 16)
        self.il = wx.ImageList(isz[0], isz[1])
        self.fl_idx = self.il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, isz))
        self.fl_open_idx = self.il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER_OPEN, wx.ART_OTHER, isz))
        self.fi_idx = self.il.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, isz))

    def __getattr__(self, item):
        if item == 'image_list':
            return self.il
        elif item == 'folder_idx':
            return self.fl_idx
        elif item == 'folder_open_idx':
            return self.fl_open_idx
        elif item == 'file_idx':
            return self.fi_idx


class Log():
    def __init__(self):
        pass

    @staticmethod
    def initialize(file_name):
        return
        '''logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logging.basicConfig(format='%(asctime)s-%(name)s-%(levelname)s:%(message)s',
                            filename=os.path.join(os.getcwd(), file_name), level=logging.DEBUG)'''

    @staticmethod
    def info(context):
        return
        '''print context
        logging.debug(context)'''