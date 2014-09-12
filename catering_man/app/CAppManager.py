#_*_ encoding=utf-8 _*_
#!/usr/bin/env python
import wx
from framework.CSingleton import CSingleton
from Tkconstants import BOTH
from app.UI.CScnMain import CScnMain

class CAppManager(CSingleton):
    mainScreen = None
    panel = None
    
    @staticmethod
    def Initailize():
        if CAppManager.mainScreen == None:
            CAppManager.mainScreen = CScnMain(None)
            CAppManager.mainScreen.Show(True)
            CAppManager.mainScreen.Center()
    
    @staticmethod
    def SwitchToApplication(app):   
        if CAppManager.panel != None:
            CAppManager.panel.Hide()
            CAppManager.panel = None
                     
        if app == 'Login':
            from app.UI.login.CWgtLogin import CWgtLogin
            CAppManager.panel = CWgtLogin(CAppManager.mainScreen) 
        elif app == 'MainFrame':
            from app.UI.desktop.CWgtDeskTop import CWgtDeskTop
            CAppManager.panel = CWgtDeskTop(CAppManager.mainScreen)
        elif app == 'DiningTable':
            from app.UI.dining_room.CWgtDiningTable import CWgtDiningTable
            CAppManager.panel = CWgtDiningTable(CAppManager.mainScreen)
        elif app == 'DishesPublish':
            from app.UI.dishes.CDishesPublish import CDishesPublish
            CAppManager.panel = CDishesPublish(CAppManager.mainScreen)
        elif app == 'Employee':
            from app.UI.employee.CEmployee import CEmployee
            CAppManager.panel = CEmployee(CAppManager.mainScreen)
        elif app == 'DutyTable':
            from app.UI.employee.CDutyTable import CDutyTable
            CAppManager.panel = CDutyTable(CAppManager.mainScreen)
         
        CAppManager.mainScreen.SetPanel(CAppManager.panel)
        CAppManager.panel.Initailize() 
        CAppManager.panel.Show(True)
        CAppManager.panel.Centre()