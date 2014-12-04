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

        self.login_panel = None

        ''' for manager UI'''
        self.home_page_panel = None
        self.dining_table_panel = None
        self.dishes_publish_panel = None
        self.employee_panel = None
        self.printer_scheme_panel = None
        self.scheme_related_panel = None
        self.user_permission_panel = None
        self.business_panel = None
        self.sales_panel = None
        self.billboard_panel = None

        ''' for front UI'''
        self.front_page_panel = None
        self.order_dishes_panel = None
        self.checkout_panel = None

    def initialize(self, app_type):
        if self.mainScreen is None:
            self.mainScreen = MainScreen(None)
            #self.mainScreen.ShowFullScreen(True)
            #self.mainScreen.Show(True)
            #self.mainScreen.Center()
            self.mainScreen.Maximize()

        if self.login_panel is None:
            from app.login import WgtLogin
            self.login_panel = WgtLogin(self.mainScreen, app_type)

        if app_type == "manager":
            if self.home_page_panel is None:
                from app.manager.UI.home_page import WgtHomePage
                self.home_page_panel = WgtHomePage(self.mainScreen)
                self.home_page_panel.Hide()

            if self.dining_table_panel is None:
                from app.manager.UI.dining_room import WgtDiningTable
                self.dining_table_panel = WgtDiningTable(self.mainScreen)
                self.dining_table_panel.Hide()

            if self.dishes_publish_panel is None:
                from app.manager.UI.dishes_publish import WgtDishesPublish
                self.dishes_publish_panel = WgtDishesPublish(self.mainScreen)
                self.dishes_publish_panel.Hide()

            if self.employee_panel is None:
                from app.manager.UI.employee import WgtEmployee
                self.employee_panel = WgtEmployee(self.mainScreen)
                self.employee_panel.Hide()

            if self.printer_scheme_panel is None:
                from app.manager.UI.kitchen_printer import WgtPrinterScheme
                self.printer_scheme_panel = WgtPrinterScheme(self.mainScreen)
                self.printer_scheme_panel.Hide()

            if self.scheme_related_panel is None:
                from app.manager.UI.kitchen_printer import WgtSchemeRelated
                self.scheme_related_panel = WgtSchemeRelated(self.mainScreen)
                self.scheme_related_panel.Hide()

            if self.user_permission_panel is None:
                from app.manager.UI.employee import WgtPermission
                self.user_permission_panel = WgtPermission(self.mainScreen)
                self.user_permission_panel.Hide()

            if self.business_panel is None:
                from app.manager.UI.report_forms import WgtBusinessInfo
                self.business_panel = WgtBusinessInfo(self.mainScreen)
                self.business_panel.Hide()

            if self.sales_panel is None:
                from app.manager.UI.report_forms import WgtSalesInfo
                self.sales_panel = WgtSalesInfo(self.mainScreen)
                self.sales_panel.Hide()

            if self.billboard_panel is None:
                from app.manager.UI.report_forms import WgtBillboardInfo
                self.billboard_panel = WgtBillboardInfo(self.mainScreen)
                self.billboard_panel.Hide()

        elif app_type == "front":
            if self.front_page_panel is None:
                from app.front.UI.front_page import WgtFrontPage
                self.front_page_panel = WgtFrontPage(self.mainScreen)
                self.front_page_panel.Hide()

            if self.order_dishes_panel is None:
                from app.front.UI.order_dishes import WgtOrderDishes
                self.order_dishes_panel = WgtOrderDishes(self.mainScreen)
                self.order_dishes_panel.Hide()

            if self.checkout_panel is None:
                from app.front.UI.check_out import WgtCheckout
                self.checkout_panel = WgtCheckout(self.mainScreen)
                self.checkout_panel.Hide()

        self.mainScreen.Show(True)

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
            if self.login_panel is None:
                from app.login import WgtLogin
                self.login_panel = WgtLogin(self.mainScreen, app)
            self.panel = self.login_panel
        elif wgt == 'HomePage':
            if self.home_page_panel is None:
                from app.manager.UI.home_page import WgtHomePage
                self.home_page_panel = WgtHomePage(self.mainScreen)
            self.panel = self.home_page_panel
        elif wgt == 'DiningTable':
            if self.dining_table_panel is None:
                from app.manager.UI.dining_room import WgtDiningTable
                self.dining_table_panel = WgtDiningTable(self.mainScreen)
            self.panel = self.dining_table_panel
        elif wgt == 'DishesPublish':
            if self.dishes_publish_panel is None:
                from app.manager.UI.dishes_publish import WgtDishesPublish
                self.dishes_publish_panel = WgtDishesPublish(self.mainScreen)
            self.panel = self.dishes_publish_panel
        elif wgt == 'Employee':
            if self.employee_panel is None:
                from app.manager.UI.employee import WgtEmployee
                self.employee_panel = WgtEmployee(self.mainScreen)
            self.panel = self.employee_panel
        elif wgt == 'PrinterScheme':
            if self.printer_scheme_panel is None:
                from app.manager.UI.kitchen_printer import WgtPrinterScheme
                self.printer_scheme_panel = WgtPrinterScheme(self.mainScreen)
            self.panel = self.printer_scheme_panel
        elif wgt == 'SchemeRelated':
            if self.scheme_related_panel is None:
                from app.manager.UI.kitchen_printer import WgtSchemeRelated
                self.scheme_related_panel = WgtSchemeRelated(self.mainScreen)
            self.panel = self.scheme_related_panel
        elif wgt == 'UserPermission':
            if self.user_permission_panel is None:
                from app.manager.UI.employee import WgtPermission
                self.user_permission_panel = WgtPermission(self.mainScreen)
            self.panel = self.user_permission_panel
        elif wgt == "BusinessInfo":
            if self.business_panel is None:
                from app.manager.UI.report_forms import WgtBusinessInfo
                self.business_panel = WgtBusinessInfo(self.mainScreen)
            self.panel = self.business_panel
        elif wgt == "SalesInfo":
            if self.sales_panel is None:
                from app.manager.UI.report_forms import WgtSalesInfo
                self.sales_panel = WgtSalesInfo(self.mainScreen)
            self.panel = self.sales_panel
        elif wgt == "BillboardInfo":
            if self.billboard_panel is None:
                from app.manager.UI.report_forms import WgtBillboardInfo
                self.billboard_panel = WgtBillboardInfo(self.mainScreen)
            self.panel = self.billboard_panel
        elif wgt == 'FrontPage':
            if self.front_page_panel is None:
                from app.front.UI.front_page import WgtFrontPage
                self.front_page_panel = WgtFrontPage(self.mainScreen)
            self.panel = self.front_page_panel
        elif wgt == 'OrderDishes':
            if self.order_dishes_panel is None:
                from app.front.UI.order_dishes import WgtOrderDishes
                self.order_dishes_panel = WgtOrderDishes(self.mainScreen)
            self.panel = self.order_dishes_panel
        elif wgt == 'CheckOut':
            if self.checkout_panel is None:
                from app.front.UI.check_out import WgtCheckout
                self.checkout_panel = WgtCheckout(self.mainScreen)
            self.panel = self.checkout_panel
        
        self.mainScreen.set_panel(self.panel)
        self.panel.initialize()
        self.panel.Show(True)
        self.panel.Centre()