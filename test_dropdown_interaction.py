
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from conftest import login, take_screenshot


def test_dropdown_interaction(setup):
    driver = setup
    driver.get("http://10.22.16.115/")
    valid_username = "547-2019-5130"
    valid_password = "123456"
    login(driver, valid_username, valid_password)
    time.sleep(1)
    driver.find_element(By.XPATH, "//p[@class='text']").click()
    time.sleep(1)
    dropdown = Select(driver.find_element(By.NAME, "unit_id"))

    for index in range(10):
        dropdown.select_by_index(index)
        time.sleep(1)

    # Select by visible text
    dropdown.select_by_visible_text("Safeer Abbas")
    driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
    take_screenshot(driver, "Update_User_Information_Successfully")

    # Refresh and Logout
    driver.refresh()
    time.sleep(5)
    driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()

    # Re-login to ensure changes
    login(driver, valid_username, valid_password)
    time.sleep(5)
    driver.find_element(By.XPATH, "//p[@class='text']").click()
    time.sleep(5)
