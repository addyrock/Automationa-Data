
import time

from selenium.webdriver.common.by import By

from conftest import login

def test_dashboard_navigation(setup):
    driver = setup
    driver.get("http://10.22.16.115/")
    valid_username = "547-2019-5130"
    valid_password = "123456"
    login(driver, valid_username, valid_password)

    driver.find_element(By.XPATH, "//i[@class='fas fa-bars']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//i[@class='fas fa-bars']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//p[normalize-space()='Dashboard']").click()
    time.sleep(1)
