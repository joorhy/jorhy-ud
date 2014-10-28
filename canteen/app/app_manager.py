#_*_ encoding=utf-8 _*_
#!/usr/bin/env python
from framework.core import Singleton
from app.main_screen import MainScreen


class AppManager(Singleton):
    mainScreen = None
    panel = None
    app_title = ""
    
    @classmethod
    def initialize(cls):
        if AppManager.mainScreen is None:
            AppManager.mainScreen = MainScreen(None)
            AppManager.mainScreen.Show(True)
            AppManager.mainScreen.Center()

    @classmethod
    def get_app_title(cls):
        return AppManager.app_title

    @classmethod
    def set_app_title(cls, title):
        AppManager.app_title = title

    @classmethod
    def destroy_panel(cls):
        if AppManager.panel is not None:
            AppManager.panel.Hide()
            #AppManager.panel = None
    
    @classmethod
    def switch_to_application(cls, wgt, app=""):
        if AppManager.panel is not None:
            AppManager.panel.Hide()
            AppManager.panel = None
                     
        if wgt == 'Login':
            from app.login import WgtLogin
            AppManager.panel = WgtLogin(AppManager.mainScreen, app)
        elif wgt == 'HomePage':
            from app.manager.UI.home_page import WgtHomePage
            AppManager.panel = WgtHomePage(AppManager.mainScreen)
        elif wgt == 'DiningTable':
            from app.manager.UI.dining_room import WgtDiningTable
            AppManager.panel = WgtDiningTable(AppManager.mainScreen)
        elif wgt == 'DishesPublish':
            from app.manager.UI.dishes_publish import WgtDishesPublish
            AppManager.panel = WgtDishesPublish(AppManager.mainScreen)
        elif wgt == 'Employee':
            from app.manager.UI.employee import WgtEmployee
            AppManager.panel = WgtEmployee(AppManager.mainScreen)
        elif wgt == 'PrinterScheme':
            from app.manager.UI.kitchen_printer import WgtPrinterScheme
            AppManager.panel = WgtPrinterScheme(AppManager.mainScreen)
        elif wgt == 'SchemeRelated':
            from app.manager.UI.kitchen_printer import WgtSchemeRelated
            AppManager.panel = WgtSchemeRelated(AppManager.mainScreen)
        elif wgt == 'UserPermission':
            from app.manager.UI.employee import WgtPermission
            AppManager.panel = WgtPermission(AppManager.mainScreen)
        elif wgt == 'FrontPage':
            from app.front.UI.front_page import WgtFrontPage
            AppManager.panel = WgtFrontPage(AppManager.mainScreen)
        elif wgt == 'OrderDishes':
            from app.front.UI.order_dishes import WgtOrderDishes
            AppManager.panel = WgtOrderDishes(AppManager.mainScreen)
        elif wgt == 'CheckOut':
            from app.front.UI.check_out import WgtCheckout
            AppManager.panel = WgtCheckout(AppManager.mainScreen)
        
        AppManager.mainScreen.set_panel(AppManager.panel)
        AppManager.panel.initialize()
        AppManager.panel.Show(True)
        AppManager.panel.Centre()