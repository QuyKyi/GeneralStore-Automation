import math
import time

from appium.webdriver.common.mobileby import MobileBy
from Page_Actions.BasePage import BasePage
import logging

from Utilities.configReader import readConfig


class CartScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
    # Define elements
    txtview_navigation_bar = (MobileBy.ID, "toolbar_title")
    txtview_total_price = (MobileBy.ID,"totalAmountLbl")
    checkbox_sendemail = (MobileBy.XPATH,"//android.widget.CheckBox[@index=1]")
    btn_visit_website_to_complete_purchase = (MobileBy.ID,"btnProceed")
    txtfield_google = (MobileBy.XPATH,"//android.widget.EditText[@index=0]")

    def is_on_cart_screen(self):
        self.verifyTextview(self.txtview_navigation_bar, "Cart")

    def verify_the_items_added_on_cart(self,items_name_list):
        number_of_item = len(items_name_list)
        number_item_of_line_on_cart = int(readConfig("GeneralStore","number_item_of_line_on_cart"))
        number_of_line_item = math.ceil(int(number_of_item)/number_item_of_line_on_cart)
        items_list_on_app = self.get_list_elements_by_id("productName")
        if number_of_line_item > 1:
            i = 1
            while i < number_of_line_item:
                self.scroll_down_from_half_screen()
                items_list_on_app = items_list_on_app + self.get_list_elements_by_id("productName")
                i = i + 1
        items_list_on_app = list(dict.fromkeys(items_list_on_app))
        items_list_on_app.sort()
        items_name_list.sort()
        assert items_list_on_app == items_name_list

    def verify_the_final_price(self):
        total_price_on_app = str(self.getText(self.txtview_total_price))
        print(total_price_on_app)
        total_price_on_app = total_price_on_app.replace("$ ", "")
        total_price_calc = readConfig("GeneralStore","final_price")
        assert total_price_on_app == total_price_calc

    def visit_to_website(self):
        self.click(self.checkbox_sendemail)
        self.click(self.btn_visit_website_to_complete_purchase)
        self.input(self.txtfield_google,"General Store")
        time.sleep(5)
        self.back_physical()
        time.sleep(5)