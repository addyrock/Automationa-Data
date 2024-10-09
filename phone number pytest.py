import time
import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.get("http://10.22.16.115/")
    driver.maximize_window()

# def login(driver, username, password):
#         username_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter Emp-ID']")
#         password_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
#         login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
#
#         # Enter credentials and submit the form
#         username_field.send_keys(username)
#         password_field.send_keys(password)
#         login_button.click()
#
# def test_login_invalid_credentials(setup):
#         driver = setup
#         Invalid_username = ""
#         Invalid_password = "123456"
#         login(driver, Invalid_username, Invalid_password)
#
#         # Wait for the error message to appear
#         try:
#             error_message = WebDriverWait(driver, 20).until(
#                 EC.presence_of_element_located((By.XPATH, "//div[@role='alert']"))
#             )
#             assert error_message.is_displayed(), "Error message not displayed"
#             take_screenshot(driver, "login_invalid_credentials_error")
#             print("Login Test Passed: Unsuccessful login displayed error message")
#         except Exception as e:
#
#             pytest.fail(f"Login Test Failed: No error message displayed for unsuccessful login. Exception: {e}")
#
#     # Add login steps if needed

def test_title_verification(setup):
        driver = setup
        # driver.get("http://10.22.16.115/")
        expected_title = "| Log in"
        actual_title = driver.title
        assert actual_title == expected_title, f"Test Failed: Title is '{actual_title}' but expected '{expected_title}'"



    # driver.quit()
def take_screenshot(driver, step_name):
    driver.save_screenshot(f"{step_name}.png")



def test_update_email(setup):
    driver = setup
    email = driver.find_element(By.XPATH, "//input[@id='email']")
    email.clear()
    time.sleep(2)
    email.send_keys("nida.latif@psca.gop.pk")
    assert email.get_attribute("value") == "nida.latif@psca.gop.pk"

def test_update_designation(setup):
    driver = setup
    designation = driver.find_element(By.XPATH, "//input[@id='designation']")
    designation.clear()
    time.sleep(2)
    designation.send_keys("DEO SQA")
    assert designation.get_attribute("value") == "DEO SQA"

# def test_update_phone(setup):
#     driver = setup
#     phone = driver.find_element(By.XPATH, "//input[@id='phone']")

    # Test null value
    # phone.clear()
    # driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
    # time.sleep(2)
    # try:
    #     error_message = WebDriverWait(driver, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'toast-error')]"))
    #     ).text
    #     assert "Please fill out this field" in error_message, "Error message for null phone number not displayed correctly."
    # except TimeoutException:
    #     assert False, "Error message for null phone number not displayed in time."

    # Test 12-digit value
    # phone.clear()
    # phone_number = "11111111111111111"
    # phone.send_keys(phone_number)
    # try:
    #     error_message = WebDriverWait(driver, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'toast-error')]"))
    #     ).text
    #     assert "The phone must be 11 characters" in error_message, "Error message for 12-digit phone number not displayed correctly."
    #  except TimeoutException:
    #     assert False, "Error message for 12-digit phone number not displayed in time."

    # Test valid phone number
    # phone.clear()
    # valid_phone_number = "03226496719"
    # phone.send_keys(valid_phone_number)
    # driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
    # time.sleep(2)
    # try:
    #     success_message = WebDriverWait(driver, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'toast-success')]"))
    #     ).text
    #     assert "User updated successfully" in success_message, "Success message for valid phone number not displayed correctly."
    # except TimeoutException:
    #     assert False, "Success message for valid phone number not displayed in time."
    #
    # driver = setup
    # phone = driver.find_element(By.XPATH, "//input[@id='phone']")
    # phone.clear()
    # time.sleep(2)
    #
    #     # Input phone number one digit at a time
    # phone_number = "0","1","1111",""
    # for digit in phone_number:
    #     phone.send_keys(digit)
    #     time.sleep(0.5)
    #     assert phone.get_attribute("value") == phone_number
    # dropdown = Select(driver.find_element(By.NAME, "unit_id"))
    # for index in range(5):
    #     dropdown.select_by_index(index)
    #     time.sleep(1)
    #     selected_option = dropdown.first_selected_option.text
    #     print(f"Selected option {index}: {selected_option}")
    #
    # dropdown.select_by_visible_text("Safeer Abbas")
    # selected_option = dropdown.first_selected_option.text
    # assert selected_option == "Safeer Abbas", "Dropdown did not select 'Safeer Abbas'."
    #
    # save_button = driver.find_element(By.XPATH, "//button[normalize-space()='Save']")
    # save_button.click()
    # time.sleep(2)
    # try:
    #     WebDriverWait(driver, 3).until(EC.alert_is_present())
    #     alert = driver.switch_to.alert
    #     assert "Please fill out this field" in alert.text, "Required field validation message not displayed."
    #     alert.accept()
    # except TimeoutException:
    #     pass

def test_update_dropdown(setup,phone=None):
    driver = setup
    phone = driver.find_element(By.XPATH, "//input[@id='phone']")
    phone.clear()
    # save_button = driver.find_element(By.XPATH, "//button[normalize-space()='Save']")
    # save_button.click()

    dropdown = Select(driver.find_element(By.NAME, "unit_id"))
    for index in range(5):
        dropdown.select_by_index(index)
        time.sleep(1)
        selected_option = dropdown.first_selected_option.text
        print(f"Selected option {index}: {selected_option}")

    dropdown.select_by_visible_text("Safeer Abbas")
    selected_option = dropdown.first_selected_option.text
    assert selected_option == "Safeer Abbas"

    save_button = driver.find_element(By.XPATH, "//button[normalize-space()='Save']")
    save_button.click()
    time.sleep(2)

    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        assert "Please fill out this field" in alert.text
        alert.accept()
    except TimeoutException:
        pass

def test_length(setup):
    driver = setup
    phone = driver.find_element(By.XPATH, "//input[@id='phone']")
    phone_number = "11111111111111111"
    phone.send_keys(phone_number)
    save_button = driver.find_element(By.XPATH, "//button[normalize-space()='Save']")
    save_button.click()
    take_screenshot("11 digit_Phone_Number")
    time.sleep(2)
    try:
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'toast-error')]"))
        ).text
        assert "The phone must be 11 characters" in error_message
    except TimeoutException:
        assert False, "Error message for 12-digit phone number not displayed in time."

def test_valid_num(setup):
    driver = setup
    phone = driver.find_element(By.XPATH, "//input[@id='phone']")
    phone.clear()
    valid_phone_number = "03226496719"
    phone.send_keys(valid_phone_number)
    driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
    take_screenshot("Valid_Phone_Number")
    time.sleep(2)
    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'toast-success')]"))
        ).text
        assert "User updated successfully" in success_message, "Success message for valid phone number not displayed correctly."
    except TimeoutException:
        assert False, "Success message for valid phone number not displayed in time."

    time.sleep(5)




#
# def test_check_success_message(setup):
#     driver = setup
#     # Wait for and verify success message
#     try:
#         WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='toast-message']")))
#         success_message = driver.find_element(By.XPATH, "//div[@class='toast-message']").text
#         assert "The phone must be 11 characters." in success_message
#     except TimeoutException:
#         assert False, "Success message not displayed in time."
#
