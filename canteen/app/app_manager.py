#_*_ encoding=utf-8 _*_
#!/usr/bin/env python
from framework.core import Singleton
from app.main_screen import MainScreen


@Singleton
class AppManager():
    def __init__(self):
        self.mainScreen = None
        self.panel = None
        self.app_title = ""

    def initialize(self):
        if self.mainScreen is None:
            self.mainScreen = MainScreen(None)
            #self.mainScreen.ShowFullScreen(True)
            self.mainScreen.Show(True)
            self.mainScreen.Center()

    def get_app_title(self):
        return self.app_title

    def set_app_title(self, title):
        self.app_title = title

    def destroy_panel(self):
        if self.panel is not None:
            self.panel.Hide()
            #self.panel = None

    def switch_to_application(self, wgt, app=""):
        if wgt == "":
            return

        if self.panel is not None:
            self.panel.Hide()
            self.panel = None
                     
        if wgt == 'Login':
            from app.login import WgtLogin
            self.panel = WgtLogin(self.mainScreen, app)
        elif wgt == 'HomePage':
            from app.manager.UI.home_page import WgtHomePage
            self.panel = WgtHomePage(self.mainScreen)
        elif wgt == 'DiningTable':
            from app.manager.UI.dining_room import WgtDiningTable
            self.panel = WgtDiningTable(self.mainScreen)
        elif wgt == 'DishesPublish':
            from app.manager.UI.dishes_publish import WgtDishesPublish
            self.panel = WgtDishesPublish(self.mainScreen)
        elif wgt == 'Employee':
            from app.manager.UI.employee import WgtEmployee
            self.panel = WgtEmployee(self.mainScreen)
        elif wgt == 'PrinterScheme':
            from app.manager.UI.kitchen_printer import WgtPrinterScheme
            self.panel = WgtPrinterScheme(self.mainScreen)
        elif wgt == 'SchemeRelated':
            from app.manager.UI.kitchen_printer import WgtSchemeRelated
            self.panel = WgtSchemeRelated(self.mainScreen)
        elif wgt == 'UserPermission':
            from app.manager.UI.employee import WgtPermission
            self.panel = WgtPermission(self.mainScreen)
        elif wgt == 'FrontPage':
            from app.front.UI.front_page import WgtFrontPage
            self.panel = WgtFrontPage(self.mainScreen)
        elif wgt == 'OrderDishes':
            from app.front.UI.order_dishes import WgtOrderDishes
            self.panel = WgtOrderDishes(self.mainScreen)
        elif wgt == 'CheckOut':
            from app.front.UI.check_out import WgtCheckout
            self.panel = WgtCheckout(self.mainScreen)
        
        self.mainScreen.set_panel(self.panel)
        self.panel.initialize()
        self.panel.Show(True)
        self.panel.Centre()