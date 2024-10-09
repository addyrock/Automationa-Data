import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_invalid_credentials(setup):
    driver = setup
    driver.get("http://10.22.16.115/")

    invalid_username = "547-2019-5130"
    invalid_password = "123456"

    from conftest import login, take_screenshot
    login(driver, invalid_username, invalid_password)

    # Wait for the error message to appear
    try:
        error_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='alert']"))
        )
        assert error_message.is_displayed(), "Error message not displayed"
        print("Login Test Passed: Unsuccessful login displayed error message")
    except Exception as e:
        take_screenshot(driver, "login_invalid_credentials_error")
        pytest.fail(f"Login Test Failed: No error message displayed for unsuccessful login. Exception: {e}")

