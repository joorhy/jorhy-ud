#_*_ encoding=utf-8 _*_
#!/usr/bin/env python
import wx
from framework.core import Singleton
from Tkconstants import BOTH
from app.UI.CScnMain import CScnMain

class CAppManager(Singleton):
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
        elif app == 'DeskTop':
            from app.UI.desktop.CWgtDeskTop import CWgtDeskTop
            CAppManager.panel = CWgtDeskTop(CAppManager.mainScreen)
        elif app == 'DiningTable':
            from app.UI.dining_room.CWgtDiningTable import CWgtDiningTable
            CAppManager.panel = CWgtDiningTable(CAppManager.mainScreen)
        elif app == 'DishesPublish':
            from app.UI.dishes.CWgtDishesPublish import CWgtDishesPublish
            CAppManager.panel = CWgtDishesPublish(CAppManager.mainScreen)
        elif app == 'Employee':
            from app.UI.employee.CWgtEmployee import CWgtEmployee
            CAppManager.panel = CWgtEmployee(CAppManager.mainScreen)
        elif app == 'DutyTable':
            from app.UI.employee.CWgtDutyTable import CWgtDutyTable
            CAppManager.panel = CWgtDutyTable(CAppManager.mainScreen)
        elif app == 'PrinterScheme':
            from app.UI.printer_setting.CWgtPrinterScheme import CWgtPrinterScheme
            CAppManager.panel = CWgtPrinterScheme(CAppManager.mainScreen)
        elif app == 'SchemeRelated':
            from app.UI.printer_setting.CWgtSchemeRelated import CWgtSchemeRelated
            CAppManager.panel = CWgtSchemeRelated(CAppManager.mainScreen)
        
        CAppManager.mainScreen.SetPanel(CAppManager.panel)
        CAppManager.panel.Initailize() 
        CAppManager.panel.Show(True)
        CAppManager.panel.Centre()