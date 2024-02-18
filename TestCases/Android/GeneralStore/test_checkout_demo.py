import time

import pytest

from Page_Actions.Android.GeneralStore.CartScreen import CartScreen
from Page_Actions.Android.GeneralStore.HomeScreen import HomeScreen
from Page_Actions.Android.GeneralStore.ProductScreen import MenuScreen
from TestCases.BaseTest import BaseTest
from Utilities.configReader import readConfig

class GeneralStore_Application(BaseTest):
    """
        check around when user is not localise yet

    """

    def test_001_homescreen_select_India_and_let_shop(self):
        home = HomeScreen(self.driver)
        # Select India as the country
        home.change_the_country()
        # Enter a test user's information (name and gender) and tap the "Let's Shop" button.
        home.input_customer_info()
        home.click_on_let_shop_button()

    def test_002_menuscreen_add_items_to_cart(self):
        menu = MenuScreen(self.driver)
        # Verify that the product screen is displayed
        menu.is_on_product_screen()
        # Scroll down and add two items to the cart: PG3 and Nike SFB Jungle
        items_list = readConfig("GeneralStore","items_list").split(",")
        items_number = len(items_list)
        menu.add_items_to_cart(items_list)
        menu.verify_the_number_of_item_on_cart(items_number)
        # Tap the cart button on the top of the screen
        menu.click_on_icon_cart()

    def test_003_checkout(self):
        cart = CartScreen(self.driver)
        # Verify that the cart screen is displayed and that the correct items have been added to the cart.
        cart.is_on_cart_screen()
        items_list = readConfig("GeneralStore", "items_list").split(",")
        cart.verify_the_items_added_on_cart(items_list)
        # Verify that the total purchase amount is correctly displayed (should be the sum of the prices of the two items added to the cart).
        cart.verify_the_final_price()
        # Tap the "Send me emails for discounts" checkbox
        # Tap the "Visit to website" button.
        # Enter "General Store" in the search bar
        # Navigate back to the General Store app home screen
        cart.visit_to_website()

    @pytest.mark.skip
    def test_004_check_failed(self):
        assert 1 == 2

