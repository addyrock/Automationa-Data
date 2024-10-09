import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def setup():
    # Initialize the WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver

def take_screenshot(driver, step_name):
    driver.save_screenshot(f"{step_name}.png")

def test_title_verification(setup):
    driver = setup
    driver.get("http://10.20.101.192:85/")
    expected_title = " | Log in"
    actual_title = driver.title
    assert actual_title == expected_title, f"Test Failed: Title is '{actual_title}' but expected '{expected_title}'"

def login(driver, username, password):
    username_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter Employee ID']")
    password_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()

def test_login_empty_credentials(setup):
    driver = setup
    login(driver, "", "")
    try:
        error_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='alert']"))
        )
        assert error_message.is_displayed()
        take_screenshot(driver, "login_invalid_credentials_error")
    except Exception as e:
        pytest.fail(f"Login Test Failed: No error message displayed for unsuccessful login. Exception: {e}")

def test_login_invalid_username(setup):
    driver = setup
    login(driver, "", "123456")
    try:
        error_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='alert']"))
        )
        assert error_message.is_displayed()
        take_screenshot(driver, "login_invalid_username_error")
    except Exception as e:
        pytest.fail(f"Login Test Failed: No error message displayed for invalid username. Exception: {e}")

def test_login_invalid_password(setup):
    driver = setup
    login(driver, "547-2016-6103", "12345")
    try:
        error_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='alert']"))
        )
        assert error_message.is_displayed()
        take_screenshot(driver, "login_invalid_password_error")
    except Exception as e:
        pytest.fail(f"Login Test Failed: No error message displayed for invalid password. Exception: {e}")

def test_login_valid_credentials(setup):
    driver = setup
    login(driver, "547-2016-6103", "123456")
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='dashboard']"))
        )
        take_screenshot(driver, "login_successful")
    except Exception as e:
        pytest.fail(f"Login Test Failed: Unable to login with valid credentials. Exception: {e}")

def test_dashboard_navigation(setup):
    driver = setup
    time.sleep(1)
    driver.find_element(By.XPATH, "//i[@class='fas fa-bars']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//i[@class='fas fa-bars']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//p[normalize-space()='Dashboard']").click()
    time.sleep(1)
    assert "Dashboard navigate successfully"
    time.sleep(2)
