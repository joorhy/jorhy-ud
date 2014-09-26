# -*- coding: utf-8 -*- 
#!/usr/bin/env python
import wx
from framework.core import Singleton, EvtManager
from app.logic.CEnumEvent import CEnumEvent

class CDataLogin(Singleton):
    chechResult = False
    
    def __init__(self):
        pass
    
    def __def__(self):
        pass
    
    def Login(self, strUser, strPasswd):
        if strUser == '0000' and strPasswd == '0000':
            self.chechResult = True
            
        EvtManager.DispatchEvent(CEnumEvent.EVT_LOGIN)
        
    def GetResult(self):
        return self.chechResult
    
