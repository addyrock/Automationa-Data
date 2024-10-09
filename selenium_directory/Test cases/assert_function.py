import time
import unittest
from turtledemo.chaos import g
from typing import Self

import self
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By

# class TestWebpage(unittest.TestCase):
#
#     def setUp(self):
#
#         self.driver = webdriver.Chrome()
#
#  def test_title(self):
#
# Self. driver.get("https://www.selenium.dev/")
#
#    self.assertEqual(self.driver.title, “Expected Title”)
import unittest
from selenium import webdriver


# class TestWebpage(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#
#     # def tearDown(self):
#     #     self.driver.quit()
#
#     def test_title(self):
#         self.driver.get("https://www.selenium.dev/")
#         expected_title = "Selenium"
#         self.assertEqual(self.driver.title, expected_title)

class TestID(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_element_presence(self):
        self.driver.get("https://www.selenium.dev/")

        element = self.driver.find_element(By.XPATH,"//a[normalize-space()='More news']").click()

        self.assertEqual(element)



from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys("webElement")

    # Get attribute of current active element
attr = driver.switch_to.active_element.get_attribute("title")
print(attr)


