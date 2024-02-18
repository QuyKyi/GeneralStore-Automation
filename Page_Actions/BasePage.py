import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import logging
from Utilities.LogUtil import Logger
import inspect

log = Logger(__name__, logging.INFO)


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def isID(self, element):
        if (element[0] == "id"):
            return True
        else:
            return False

    def add_logfile(self):
        i = 0
        action = ""
        screen = ""
        element_name = ""
        for item in inspect.stack():
            if i == 2:
                code = item.code_context[0]
                action = code.split(".")[1].split("(")[0]
                # add icon action to clearly log
                icon = ""
                if action == "click":
                    icon = "👇 "
                elif action == "verifyTextview":
                    icon = "💋 "
                elif action == "input":
                    icon = "️✍️ "
                action = icon + action
                # get screen
                try:
                    screen = code.split(".")[1].split("(")[1].split(".")[0]
                except:
                    pass
                # get element name
                try:
                    element_name = code.split(".")[2].replace(")", "")
                except:
                    pass
                break
            i = i + 1
        if element_name != "":
            log.logger.info("[" + screen + "] " + action + ": " + element_name)

    def waiting(self, element):

        try:

            if self.isID(element):
                WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, element[1])))
            else:
                WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, element[1])))

        except():
            log.logger.info("[waiting] error element: " + element[1])

    def getAttribute(self, element, atrribute):
        self.add_logfile()
        self.waiting(element)
        if self.isID(element):
            text = self.driver.find_element_by_id(element[1]).get_attribute(atrribute)
        else:
            text = self.driver.find_element_by_xpath(element[1]).get_attribute(atrribute)
        log.logger.info("Get Attribute " + atrribute + " is: " + str(text))
        return text

    def click(self, element):
        self.add_logfile()
        self.waiting(element)
        if self.isID(element):
            self.driver.find_element_by_id(element[1]).click()
        else:
            self.driver.find_element_by_xpath(element[1]).click()

    def input(self, element, value):
        self.add_logfile()
        self.waiting(element)
        if self.isID(element):
            self.driver.find_element_by_id(element[1]).clear()
            self.driver.find_element_by_id(element[1]).send_keys(value)
        else:
            self.driver.find_element_by_xpath(element[1]).clear()
            self.driver.find_element_by_xpath(element[1]).send_keys(value)

    def getText(self, element):
        self.add_logfile()
        self.waiting(element)
        if self.isID(element):
            text = self.driver.find_element_by_id(element[1]).text
        else:
            text = self.driver.find_element_by_xpath(element[1]).text
        log.logger.info("---> The text is: " + text)
        return text

    def verifyTextview(self, element, expected_text):
        self.add_logfile()
        text = self.getText(element)
        log.logger.info("---> Expected is: " + expected_text)
        assert text.strip() == expected_text.strip()

    def is_display(self, text):
        time.sleep(0.5)
        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text=" + "\"" + text + "\"]").click()
            return True
        except:
            return False

    def scrollToText(self, text):
        self.add_logfile()
        # log.logger.info("Scroll down to text: " + text)
        i = 1
        while i < 10:
            time.sleep(1)
            try:
                self.driver.find_element_by_xpath("//android.widget.TextView[@text=" + "\"" + text + "\"]").click()
                log.logger.info("---> The text has displayed")
                break
            except:
                self.scroll_down()
            i += 1

    def scrollToTextAndClick(self, text):
        self.add_logfile()
        # log.logger.info("Scroll down to text and click: " + text)
        i = 0
        while i < 15:
            # time.sleep(1)
            try:
                self.driver.find_element_by_xpath("//android.widget.TextView[@text=" + "\"" + text + "\"]").click()
                log.logger.info("---> Clicked on text")
                return i
            except:
                self.scroll_down()
            i += 1

    def clickontext(self, text):
        self.add_logfile()
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='" + text + "']").click()

    def click_on_xpath(self, xpath):
        self.add_logfile()
        self.driver.find_element_by_xpath(xpath).click()

    def gettext_on_xpath(self, xpath):
        self.add_logfile()
        text = self.driver.find_element_by_xpath(xpath).text
        print(text)
        return text

    def get_list_elements_by_id(self, element_id):
        all_elements = self.driver.find_elements_by_id(element_id)
        result_list = []
        for element in all_elements:
            result_list.append(element.text)
        return result_list

    def scroll_down(self):
        self.add_logfile()
        time.sleep(0.5)
        width_device = self.driver.get_window_size()['width']
        hight_device = self.driver.get_window_size()['height']
        # scroll a to b
        start_x = width_device / 2
        start_y = hight_device * 7 / 8
        end_x = width_device / 2
        end_y = hight_device * 3 / 8
        # end_y = 0
        action = TouchAction(self.driver)
        action.long_press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).release().perform()

    def scroll_down_from_half_screen(self):
        time.sleep(0.5)
        width_device = self.driver.get_window_size()['width']
        hight_device = self.driver.get_window_size()['height']
        # scroll a to b
        start_x = width_device / 2
        start_y = hight_device * 4 / 8
        end_x = width_device / 2
        end_y = hight_device * 2 / 8
        # end_y = 0
        action = TouchAction(self.driver)
        action.long_press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).release().perform()

    def scroll_up(self):
        self.add_logfile()
        width_device = self.driver.get_window_size()['width']
        hight_device = self.driver.get_window_size()['height']
        # scroll a to b
        start_x = width_device / 2
        start_y = hight_device * 1 / 5
        end_x = width_device / 2
        end_y = hight_device * 3 / 4
        # end_y = 0
        action = TouchAction(self.driver)
        action.long_press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).release().perform()

    def back_physical(self):
        log.logger.info("---> Click on Back Physical device")
        self.add_logfile()
        self.driver.press_keycode(4)
