import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()  # You can use other drivers like Firefox, Edge, etc.
    driver.get("http://10.22.16.115/")  # Replace with the correct login URL
    driver.maximize_window()
    # Add login steps
    username_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter Emp-ID']")
    password_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    username_field.send_keys("547-2019-5130")  # Replace with a valid username
    password_field.send_keys("123456")  # Replace with a valid password
    login_button.click()
    # Wait until the login process completes and the user is redirected
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//i[@class='fas fa-bars']")))
    driver.get("http://10.22.16.115/admin/user/edit/118")
    yield driver


def test_user_edit(setup):
    driver = setup

    # Test updating user information
    email_input = driver.find_element(By.XPATH, "//input[@id='email']")
    designation_input = driver.find_element(By.XPATH, "//input[@id='designation']")
    phone_input = driver.find_element(By.XPATH, "//input[@id='phone']")
    save_button = driver.find_element(By.XPATH, "//button[normalize-space()='Save']")

    # Test valid data
    email_input.clear()
    time.sleep(2)
    email_input.send_keys("testuser@example.com")
    designation_input.clear()
    time.sleep(2)
    designation_input.send_keys("Software Engineer")
    phone_input.clear()
    time.sleep(2)
    phone_input.send_keys("03226496719")
    save_button.click()

    phone_input = driver.find_element(By.XPATH, "//input[@id='phone']")
    # Test invalid phone number
    phone_input.clear()
    time.sleep(2)
    phone_input.send_keys("1111")
    save_button.click()

    # Wait for and verify error message

    phone_input = driver.find_element(By.XPATH, "//input[@id='phone']")
    # Test numeric characters only in phone number
    phone_input.clear()
    time.sleep(2)
    phone_input.send_keys("abc123")
    save_button.click()
    cleaned_value = ''.join(filter(str.isdigit, phone_input.get_attribute("value")))
    assert cleaned_value == "123", "Non-numeric characters were not filtered out"

    phone_input = driver.find_element(By.XPATH, "//input[@id='phone']")# Test for maximum length in phone number
    phone_input.clear()
    time.sleep(2)
    phone_input.send_keys("12345678901234567890")
    assert len(phone_input.get_attribute("value")) == 11, "Phone number input exceeded maximum length"

if __name__ == "__main__":
    pytest.main()
