from __future__ import absolute_import

import os
from datetime import datetime

import pytest

from . import utilities
from ..automation import TaskManager
from ..automation.utilities import db_utils
from .openwpmtest import OpenWPMTest

WEBSOCKET_TEST_URL = u"%s/websocket_test.html" % utilities.BASE_TEST_URL

class TestExtension(OpenWPMTest):

    def get_config(self, data_dir=""):
        manager_params, browser_params = self.get_test_config(data_dir)
        browser_params[0]['js_instrument'] = True
        browser_params[0]['headless'] = False
        return manager_params, browser_params

    def test_websocket(self):
        db = self.visit(WEBSOCKET_TEST_URL)
        rows = db_utils.get_javascript_entries(db)
        for row in rows:
            if ('WebSocket' in row['symbol']):
                print(row)