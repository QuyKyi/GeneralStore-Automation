import logging
import unittest

import allure
import pytest

from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


@pytest.mark.usefixtures("check_result_after_test", "appium_driver")
class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        log.logger.info("-------------------------------------------------")
        log.logger.info("------------Start test new feature---------------")
        log.logger.info("-------------------------------------------------")

    @classmethod
    def tearDownClass(cls) -> None:
        log.logger.info("---End test feature---")

    def setUp(self) -> None:
        arr_path = self.id().split('.')
        tcname = arr_path[len(arr_path) - 1]
        log.logger.info("Start test new testcase-----> " + tcname)

    def tearDown(self) -> None:
        pass
        # get testcase id from test name
        # arr_path = self.id().split('.')  # ['TestCases', 'Android', 'JP', 'test_00_setup_datatest_and_testrail', 'setup_datatest_and_cretetestrun_testrail', 'test_001_sample_callAPI_setup_datatest_to_excel']
        # tcname = arr_path[len(arr_path) - 1]  # test_001_345_tc0
        # Get test result after run testcase
        # if hasattr(self._outcome, 'errors'):
        #     # Python 3.4 - 3.10  (These two methods have no side effects)
        #     result = self.defaultTestResult()
        #     self._feedErrorsToResult(result, self._outcome.errors)
        # else:
        #     # Python 3.11+
        #     result = self._outcome.result
        # ok = all(test != self for test, text in result.errors + result.failures)
        #
        # if ok:  # When testcase Passed
        #     pass
        #
        # else:  # When testcase FAILED
        #     for typ, errors in (('ERROR', result.errors), ('FAIL', result.failures)):
        #         for test, text in errors:
        #             if test is self:
        #                 msg = [x for x in text.split('\n')[1:]
        #                        if not x.startswith(' ')][0]
        #                 log.logger.info("[RESULT - FAILED]: Reason: " + msg)
