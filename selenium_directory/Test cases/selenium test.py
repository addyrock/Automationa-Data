import unittest
import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from testingbotclient import TestingBotClient

class TestTestingBotClient(unittest.TestCase):

    def setUp(self):
		desired_cap = {'platform': 'Windows', 'browserName': 'chrome', 'version': 'latest-1' }

		self.driver = webdriver.Remote(
		    command_executor='http://key:secret@localhost:4445/wd/hub',
		    desired_capabilities=desired_cap)

    def test_google_example(self):
		self.driver.get("https://www.google.com")
		if not "Google" in self.driver.title:
		    raise Exception("Unable to load google page!")
		elem = self.driver.find_element_by_name("q")
		elem.send_keys("TestingBot")
		elem.submit()

    def tearDown(self):
		self.driver.quit()
		status = sys.exc_info() == (None, None, None)
		tb_client = TestingBotClient('key', 'secret')
		tb_client.tests.update_test(self.driver.session_id, self._testMethodName, status)

if __name__ == '__main__':
    unittest.main()