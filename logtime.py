import time
import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture(scope="module")
def setup():
    # Initialize the WebDriver with options
    # options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--window-size=1920x1080')
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver



def take_screenshot(driver, step_name):
    driver.save_screenshot(f"{step_name}.png")


def test_title_verification(setup):
    driver = setup
    driver.get("http://10.22.16.115/")
    expected_title = " | Log in"
    actual_title = driver.title
    assert actual_title == expected_title, f"Test Failed: Title is '{actual_title}' but expected '{expected_title}'"


def login(driver, username, password):
    username_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter Employee ID']")
    password_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    # Enter credentials and submit the form
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()


def test_login_empty_credentials(setup):
    driver = setup
    Invalid_username = ""
    Invalid_password = ""
    login(driver, Invalid_username, Invalid_password)

    # Wait for the error message to appear
    try:
        error_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='alert']"))
        )
        assert error_message.is_displayed()
        take_screenshot(driver, "login_invalid_credentials_error")
        print("Login Test Passed: Unsuccessful login displayed error message")
    except Exception as e:

        pytest.fail(f"Login Test Failed: No error message displayed for unsuccessful login. Exception: {e}")


def test_login_invalid_username(setup):
    driver = setup
    Invalid_username = ""
    Invalid_password = "123456"
    login(driver, Invalid_username, Invalid_password)

    # Wait for the error message to appear
    try:
        error_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='alert']"))
        )
        assert error_message.is_displayed()
        take_screenshot(driver, "login_invalid_credentials_error")
        print("Login Test Passed: Unsuccessful login displayed error message")
    except Exception as e:

        pytest.fail(f"Login Test Failed: No error message displayed for unsuccessful login. Exception: {e}")


def test_login_invalid_password(setup):
    driver = setup
    Invalid_username = "547-2019-5130"
    Invalid_password = "12345"
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
    assert "login successfully"


def test_log_time_functionality(setup):
    driver = setup
    driver.find_element(By.XPATH, "//p[normalize-space()='Log Time']").click()
    driver.find_element(By.XPATH,"//button[@name='submit_row_3']").click()
    time.sleep(3)

    try:
        # Wait for the error messages to appear and collect them
        error_elements = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//div[contains(@class, 'toast-error')]"))
        )
        error_messages = [error.text for error in error_elements]

        # Check that all expected error messages are present
        expected_errors = [
            "Please select subtask status.",
            "Remarks field is required.",
            "Subtask field is required."
        ]

        for expected_error in expected_errors:
            assert expected_error in error_messages, f"Expected error message '{expected_error}' not found in: {error_messages}"

    except TimeoutException:
        assert False, "Error messages not displayed in time."

    # Additional steps can be added here if necessary
    time.sleep(5)


def test_log_functionality_1(setup):
    driver = setup
    time.sleep(5)
    dropdown = Select(driver.find_element(By.XPATH, "//select[@name='subtask_3']"))
    dropdown.select_by_visible_text("Main page Designing")
    driver.find_element(By.XPATH, "//button[@name='submit_row_3']").click()
    time.sleep(3)

    try:
        # Wait for the error messages to appear and collect them
        error_elements = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//div[contains(@class, 'toast-error')]"))
        )
        error_messages = [error.text for error in error_elements]

        # Check that all expected error messages are present
        expected_errors = [
            "Please select subtask status.",
            "Remarks field is required."
        ]

        for expected_error in expected_errors:
            assert expected_error in error_messages, f"Expected error message '{expected_error}' not found in: {error_messages}"

    except TimeoutException:
        assert False, "Error messages not displayed in time."

    # Additional steps can be added here if necessary
    time.sleep(5)


def test_log_functionality_2(setup):
    driver = setup
    time.sleep(5)
    dropdown = Select(driver.find_element(By.XPATH, "//select[@name='subtask_3']"))
    dropdown.select_by_visible_text("Main page Designing")
    driver.find_element(By.XPATH, "//textarea[@name='sub_description_3']").send_keys("Regression Testing")
    driver.find_element(By.XPATH, "//button[@name='submit_row_3']").click()
    time.sleep(3)

    try:
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'toast-error')]"))
        ).text
        assert "Please select subtask status." in error_message
    except TimeoutException:
        assert False, "Error message not displayed in time "


def test_log_functionality_submit(setup):
    driver = setup
    time.sleep(5)
    dropdown = Select(driver.find_element(By.XPATH, "//select[@name='subtask_3']"))
    dropdown.select_by_visible_text("Main page Designing")
    driver.find_element(By.XPATH, "//textarea[@name='sub_description_3']").send_keys("Functional Testing")
    radio1 = driver.find_element(By.XPATH, "//tbody/tr[4]/td[5]/div[1]/input[1]")
    radio1.click()
    time.sleep(1)
    radio2 = driver.find_element(By.XPATH, "//tbody/tr[4]/td[5]/div[1]/input[1]")
    radio2.click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[@name='submit_row_3']").click()
    time.sleep(3)
    take_screenshot(driver, "Time Logged Successfully")

    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'toast-success')]"))
        ).text
        assert "Time logged Successfully" in success_message
    except TimeoutException:
        assert False, "Success message for valid phone number not displayed in time."


def test_subtask_again(setup):
    driver = setup
    driver.find_element(By.XPATH, "//p[normalize-space()='Subtasks']").click()
    time.sleep(2)
    take_screenshot(driver,"Subtask Review Screenshot")
    try:
        status_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//tbody/tr[1]/td[9]"))
        )
        assert status_element.text == "Completed"
    except TimeoutException:
        take_screenshot(driver, "Subtask_Review_Timeout")
        assert False, "In process"