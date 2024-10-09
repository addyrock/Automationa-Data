# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def setup():
    # Initialize the WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # Teardown - Close the browser
    driver.quit()

def login(driver, username, password):
    # Find and interact with the login elements
    username_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter Emp-ID']")
    password_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    # Enter credentials and submit the form
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()


def take_screenshot():
    return None