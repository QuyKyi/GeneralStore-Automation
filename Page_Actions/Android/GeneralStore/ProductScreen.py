import math
import time

from appium.webdriver.common.mobileby import MobileBy
from Page_Actions.BasePage import BasePage
import logging

from Utilities.configReader import writeConfig


class MenuScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
    # Define elements
    txtview_navigation_bar = (MobileBy.ID, "toolbar_title")
    txtview_item_on_cart = (MobileBy.ID,"counterText")
    icon_cart = (MobileBy.ID,"appbar_btn_cart")

    def is_on_product_screen(self):
        self.verifyTextview(self.txtview_navigation_bar, "Products")

    def add_items_to_cart(self, item_name_list):
        final_price = 0
        item_name_list_added = []
        item_num = len(item_name_list)
        i = 0
        while i < item_num:
            for item_name in item_name_list:
                is_new_item = self.check_item_added(item_name,item_name_list_added)
                if is_new_item and self.is_display(item_name):
                    self.click_on_xpath("//android.widget.LinearLayout/android.widget.TextView[@text=\""+item_name+"\"]/following-sibling::android.widget.LinearLayout[@index=3]/android.widget.TextView[@index=1]")
                    item_name_list_added.append(item_name)
                    item_price = self.get_item_price(item_name)
                    final_price = final_price + item_price
                    i = i + 1
            self.scroll_down()
        final_price = math.floor(final_price * 100) / 100
        writeConfig("GeneralStore", "final_price", str(final_price))

    def check_item_added(self, item_name, item_name_list_added):
        new_item = True
        for x in item_name_list_added:
            if x == item_name:
                new_item = False
        return new_item

    def get_item_price(self, item_name):
        price = self.gettext_on_xpath(
            "//android.widget.LinearLayout/android.widget.TextView[@text=\""+ item_name + "\"]/following-sibling::android.widget.LinearLayout[@index=3]/android.widget.TextView[@index=0]")
        price = str(price).replace("$", "")
        price = float(price)
        return price

    def verify_the_number_of_item_on_cart(self, item_number):
        item_number_on_app = self.getText(self.txtview_item_on_cart)
        assert str(item_number) == item_number_on_app

    def click_on_icon_cart(self):
        self.click(self.icon_cart)

