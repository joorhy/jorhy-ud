#_*_ encoding=utf-8 _*_
#!/usr/bin/env python
import wx
from framework.core import Singleton
from Tkconstants import BOTH
from app.manager.MainScreen import MainScreen 

class AppManager(Singleton):
    mainScreen = None
    panel = None
    
    @classmethod
    def Initailize(cls):
        if AppManager.mainScreen == None:
            AppManager.mainScreen = MainScreen(None)
            AppManager.mainScreen.Show(True)
            AppManager.mainScreen.Center()
    
    @classmethod
    def SwitchToApplication(cls, app):   
        if AppManager.panel != None:
            AppManager.panel.Hide()
            AppManager.panel = None
                     
        if app == 'Login':
            from app.manager.UI.login import WgtLogin
            AppManager.panel = WgtLogin(AppManager.mainScreen) 
        elif app == 'HomePage':
            from app.manager.UI.home_page import WgtHomePage
            AppManager.panel = WgtHomePage(AppManager.mainScreen)
        elif app == 'DiningTable':
            from app.manager.UI.dining_room import WgtDiningTable
            AppManager.panel = WgtDiningTable(AppManager.mainScreen)
        elif app == 'DishesPublish':
            from app.manager.UI.dishes_publish import WgtDishesPublish
            AppManager.panel = WgtDishesPublish(AppManager.mainScreen)
        elif app == 'Employee':
            from app.manager.UI.employee import WgtEmployee
            AppManager.panel = WgtEmployee(AppManager.mainScreen)
        elif app == 'PrinterScheme':
            from app.manager.UI.kitchen_printer import WgtPrinterScheme
            AppManager.panel = WgtPrinterScheme(AppManager.mainScreen)
        elif app == 'SchemeRelated':
            from app.manager.UI.kitchen_printer import WgtSchemeRelated
            AppManager.panel = WgtSchemeRelated(AppManager.mainScreen)
        
        AppManager.mainScreen.SetPanel(AppManager.panel)
        AppManager.panel.Initailize() 
        AppManager.panel.Show(True)
        AppManager.panel.Centre()