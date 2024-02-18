import time

from appium.webdriver.common.mobileby import MobileBy
from Page_Actions.BasePage import BasePage
import logging

from Utilities.configReader import readConfig, writeConfig
class HomeScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Define elements
    txtview_navigation_bar = (MobileBy.ID,"toolbar_title")
    drop_down_list_country = (MobileBy.ID,"spinnerCountry")
    textfield_name = (MobileBy.ID,"nameField")
    radio_gender_male = (MobileBy.ID,"radioMale")
    radio_gender_female = (MobileBy.ID, "radioFemale")
    btn_let_shop = (MobileBy.ID,"btnLetsShop")

    def is_on_home_screen(self):
        self.verifyTextview(self.txtview_navigation_bar,"General Store")

    def change_the_country(self):
        self.click(self.drop_down_list_country)

        country = readConfig("GeneralStore","country")
        number_scroll = int(readConfig("GeneralStore","country_scroll_number"))
        if number_scroll == 0:
            number_scroll = self.scrollToTextAndClick(country)
            writeConfig("GeneralStore","country_scroll_number",str(number_scroll - 1))
        else:
            i = 0
            while i < number_scroll:
                self.scroll_down()
                i = i + 1
            self.scrollToTextAndClick(country)

    def input_customer_info(self):
        customer_name = readConfig("GeneralStore", "customer_name")
        self.input(self.textfield_name,customer_name)

        customer_gender = readConfig("GeneralStore", "customer_gender")
        if customer_gender == "Female":
            self.click(self.radio_gender_female)
        if customer_gender == "Male":
            self.click(self.radio_gender_male)

    def click_on_let_shop_button(self):
        self.click(self.btn_let_shop)
