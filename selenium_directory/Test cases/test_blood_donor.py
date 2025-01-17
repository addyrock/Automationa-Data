import time
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import subprocess

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Run Allure Report after pytest execution
def run_allure_report():
    allure_results_dir = "allure-results"
    allure_report_dir = "allure-report"

    if not os.path.exists(allure_results_dir):
        os.makedirs(allure_results_dir)

    # Run pytest and generate Allure results
    subprocess.run(["pytest", "--alluredir", allure_results_dir], check=True)

    # Generate the Allure report
    subprocess.run(["allure", "generate", allure_results_dir, "-o", allure_report_dir, "--clean"], check=True)

    # Serve the Allure report
    subprocess.run(["allure", "open", allure_report_dir], check=True)


@pytest.fixture(scope="module")
def setup():
    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()


def take_screenshot(driver, step_name):
    driver.save_screenshot(f"{step_name}.png")


def test_title_verification(setup):
    driver = setup
    driver.get("https://blooddonors.psca.gop.pk/login")
    expected_title = "Blood Donor (PSCA)"
    actual_title = driver.title
    assert actual_title == expected_title, f"Test Failed: Title is '{actual_title}' but expected '{expected_title}'"
    take_screenshot(driver, 'title_verification')


def login(driver, username, password):
    username_field = driver.find_element(By.XPATH, "//input[@id='username']")
    password_field = driver.find_element(By.XPATH, "//input[@id='password']")
    login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Sign Me In']")
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()


def test_login_blank_field(setup):
    driver = setup
    time.sleep(1)
    login(driver, "", "")
    try:
        WebDriverWait(driver, 1).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        assert "Please fill out this field" in alert.text
        alert.accept()
    except TimeoutException:
        pass
    take_screenshot(driver, 'login_blank_field')


if __name__ == "__main__":
    # Run the tests first
    subprocess.run(["pytest", "--maxfail=1", "--disable-warnings", "-q"])

    # After tests are finished, generate and open the Allure report
    run_allure_report()
