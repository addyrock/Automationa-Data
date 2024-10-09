import time
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

# from conftest import login


@pytest.fixture(scope="module")
def setup():
    # Initialize the WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # Teardown - Close the browser


def take_screenshot(driver, step_name):
    driver.save_screenshot(f"{step_name}.png")


def test_title_verification(setup):
    driver = setup
    driver.get("http://10.22.16.115/")
    expected_title = "| Log in"
    actual_title = driver.title
    assert actual_title == expected_title, f"Test Failed: Title is '{actual_title}' but expected '{expected_title}'"

# def login(driver, username, password):
#     # Find and interact with the login elements
#     username_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter Emp-ID']")
#     password_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
#     login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
#
#     # Enter credentials and submit the form
#     username_field.send_keys("547-2019-5130")
#     password_field.send_keys("123456")
#     login_button.click()

def login(driver, username, password):
    username_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter Emp-ID']")
    password_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    # Enter credentials and submit the form
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()


def test_login_invalid_credentials(setup):
    driver = setup
    Invalid_username = ""
    Invalid_password = "123456"
    login(driver, Invalid_username, Invalid_password)

    # Wait for the error message to appear
    try:
        error_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='alert']"))
        )
        assert error_message.is_displayed(), "Error message not displayed"
        take_screenshot(driver, "login_invalid_credentials_error")
        print("Login Test Passed: Unsuccessful login displayed error message")
    except Exception as e:

       pytest.fail(f"Login Test Failed: No error message displayed for unsuccessful login. Exception: {e}")

def test_login_valid_credentials(setup):
    driver = setup
    valid_username = "547-2019-5130"
    valid_password = "123456"
    login(driver, valid_username, valid_password)
    take_screenshot(driver, "Successfully login")
    assert  "login succsessfully"
    # Wait for the error message to appear
    # try:
    #     message = WebDriverWait(driver, 20).until(
    #         EC.presence_of_element_located((By.XPATH, "//div[@role='alert']"))
    #     )
    #     assert message.is_displayed(), "Succsessfully login"
    #     print("Login Test Passed: Successfully login ")
    # except Exception as e:
    #     take_screenshot(driver, "login_invalid_credentials_error")
    #     pytest.fail(f"Login Test Failed: No error message displayed for unsuccessful login. Exception: {e}")


def test_dashboard_navigation(setup):
    driver = setup

    driver.find_element(By.XPATH, "//i[@class='fas fa-bars']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//i[@class='fas fa-bars']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//p[normalize-space()='Dashboard']").click()
    time.sleep(1)


# def test_dropdown_interaction(setup):
#     driver = setup
#
#     driver.find_element(By.XPATH, "//p[@class='text']").click()
#     time.sleep(1)
#     dropdown = Select(driver.find_element(By.NAME, "unit_id"))
#
#     for index in range(5):
#         dropdown.select_by_index(index)
#         time.sleep(1)
#
#     # Select by visible text
#     dropdown.select_by_visible_text("Safeer Abbas")
#     # driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
#     take_screenshot(driver, "Update_User_Information_Successfully")


def test_phone_number_validation(setup):
    driver = setup
    time.sleep(1)
    # Locate the phone number input field
    driver.find_element(By.XPATH, "//p[@class='text']").click()
    phone_input = driver.find_element(By.XPATH, "//input[@id='phone']")

    # Test valid phone number
    phone_input.clear()
    time.sleep(2)
    phone_input.send_keys("03226496719")
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Wait for the error message to appear
    # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='toast-message']")))
    # # Assert that the error message for invalid phone number is not present
    # try:
    #     assert not EC.presence_of_element_located((By.XPATH, "//div[@class='toast toast-error']"))(driver)
    # except NoSuchElementException:
    #     pass  # NoSuchElementException is expected if the error message is not present

    # Test for invalid phone number
    time.sleep(2)
    phone_input = driver.find_element(By.XPATH, "//input[@id='phone']")
    phone_input.clear()
    time.sleep(2)
    phone_input.send_keys("1111")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    # Wait for the error message to appear
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//script[@type='text/javascript']")))
    # Assert that the error message for invalid phone number is present
    assert EC.presence_of_element_located((By.XPATH, "//script[@type='text/javascript']"))(driver)
    print("Done")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    phone_input.clear()
    phone_input.send_keys("abc123")
    cleaned_value = ''.join(filter(str.isdigit, phone_input.get_attribute("value")))
    assert cleaned_value == "123"
    print("Done")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    phone_input.clear()
    phone_input.send_keys("12345678901")
    assert len(phone_input.get_attribute("value")) == 11
# def test_phone(setup):
#      driver=setup
#      Invalid_phone = ("abc")
#      valid_phone = "03226496719"
#      valid_phone(driver, Invalid_phone,valid_phone)
#      driver.find_element(By.XPATH,"//input[@id='phone']").send_keys("abc")
#      driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
#      try:
#          error_message = WebDriverWait(driver, 20).until(
#              EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save']"))
#          )
#          assert error_message.is_displayed(), "Error message not displayed"
#          print("Login Test Passed: Unsuccessful login displayed error message")
#      except Exception as e:
#          take_screenshot(driver, "login_invalid_credentials_error")
#          pytest.fail(f"Login Test Failed: No error message displayed for unsuccessful login. Exception: {e}")

# def click(setup):
#     driver=setup
#     self._execute(Command.CLICK_ELEMENT)

