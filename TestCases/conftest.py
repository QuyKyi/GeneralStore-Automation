import time

import allure
import pytest
from allure_commons.types import AttachmentType

from appium import webdriver
import logging

from Consts.consts import Consts
from Utilities.LogUtil import Logger
from Utilities.configReader import readConfig

log = Logger(__name__, logging.INFO)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


# @pytest.fixture(scope="function")
@pytest.fixture(scope="class")
def appium_driver(request):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = 'Android'
    desired_caps['noReset'] = False
    desired_caps['appPackage'] = 'com.androidsample.generalstore'
    desired_caps['appActivity'] = 'com.androidsample.generalstore.SplashActivity'

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield driver
    log.logger.info("[DRIVER] --> Quit")
    driver.quit()


@pytest.fixture()
def check_result_after_test(request, appium_driver):
    yield
    log.logger.info("----check these steps above---")
    item = request.node  # print(str(request.cls)) #<class 'TestCases.Android.JP.test_04_NotLocalise_Logined.Flow_04_NotLocalise_Logined'>
    tc_name = request.node.name
    driver = appium_driver
    if item.rep_call.failed:  # When testcase Failed
        # ScreeShoot
        path = Consts.SCREENSHOT_DIR + tc_name + ".png"
        driver.save_screenshot(path)
        log.logger.info("[SCREEN SHOT] image: " + path)
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
    else:  # When testcase Passed
        log.logger.info("[RESULT - PASSED]")

    log.logger.info("<-----End of testcase\n\n\n")
