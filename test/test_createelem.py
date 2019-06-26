from __future__ import absolute_import

import os
from datetime import datetime

import pytest

from . import utilities
from ..automation import TaskManager
from ..automation.utilities import db_utils
from .openwpmtest import OpenWPMTest

ELEMENT_TEST_URL = u"%s/create_element_test.html" % utilities.BASE_TEST_URL

# A shorter version of test_extension.py with only the new instrumentation.
# To-do: Add to test_extension.py

class TestExtension(OpenWPMTest):

    def get_config(self, data_dir=""):
        manager_params, browser_params = self.get_test_config(data_dir)
        browser_params[0]['js_instrument'] = True
        browser_params[0]['headless'] = False #Need this for Mac.
        return manager_params, browser_params

    def test_createelem(self):
        db = self.visit(ELEMENT_TEST_URL, sleep_after = 60)
        #db = self.visit('http://www.google.com', sleep_after = 60)
        rows = db_utils.get_javascript_entries(db)
        #For now, just printing rows. To-do: add asserts
        for row in rows:
            print(row)