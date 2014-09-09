# -*- coding: utf-8 -*- 
#!/usr/bin/env python
import wx
from framework.CEvtManager import CEvtManager
from framework.CSingleton import CSingleton
from app.logic.CEnumEvent import CEnumEvent

class CDataLogin(CSingleton):
    chechResult = False
    
    def __init__(self):
        pass
    
    def __def__(self):
        pass
    
    def Login(self, strUser, strPasswd):
        if strUser == '0000' and strPasswd == '0000':
            self.chechResult = True
            
        CEvtManager.DispatchEvent(CEnumEvent.EVT_LOGIN, "")
        
    def GetResult(self):
        return self.chechResult
    
