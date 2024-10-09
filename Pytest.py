import time
import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.get("http://10.22.16.115/")  # Replace with the correct URL
    driver.maximize_window()
    # Add your login code here if needed
    yield driver
    driver.quit()
def login(driver, username, password):
    username_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter Emp-ID']")
    password_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    # Enter credentials and submit the form
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()


def test_login_valid_credentials(setup):
    driver = setup
    valid_username = "547-2019-5130"
    valid_password = "123456"
    login(driver, valid_username, valid_password)
    assert  "login succsessfully"

def test_phone_number_validation(setup):
    driver = setup
    time.sleep(1)
    # Locate the phone number input field
    driver.find_element(By.XPATH, "//p[@class='text']").click()
    phone_input = driver.find_element(By.XPATH, "//input[@id='phone']")

    # Test valid phone number
    phone_input.clear()
    phone_input.send_keys("03226496719")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    # Check that no error message is displayed for a valid phone number
    try:
        error_message = driver.find_element(By.XPATH, "//div[@class='toast toast-error']")
        assert False, "Error message displayed for a valid phone number"
    except NoSuchElementException:
        pass  # No error message found, as expected

    # Test for invalid phone number
    phone_input.clear()
    phone_input.send_keys("1111")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    # Wait for the error message to appear
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='toast toast-error']")))
    # Assert that the error message for invalid phone number is present
    assert driver.find_element(By.XPATH, "//div[@class='toast toast-error']"), "No error message displayed for invalid phone number"

    # Test for numeric characters only
    phone_input.clear()
    phone_input.send_keys("abc123")
    cleaned_value = ''.join(filter(str.isdigit, phone_input.get_attribute("value")))
    assert cleaned_value == "123"

    # Test for maximum length
    phone_input.clear()
    phone_input.send_keys("12345678901234567890")
    assert len(phone_input.get_attribute("value")) == 11
