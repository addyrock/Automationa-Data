import time

import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture(scope="module")
def setup():
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    # chrome_options.add_argument('--headless')  # Uncomment if you want to run in headless mode

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver


def take_screenshot(driver, step_name):
    driver.save_screenshot(f"{step_name}.png")


def blink_element(driver, element, duration=1, iterations=3):
    """Blinks a Selenium Webdriver element"""
    original_style = element.get_attribute('style')
    highlight_style = "background: yellow; border: 5px solid red;"

    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)

    for _ in range(iterations):
        apply_style(highlight_style)
        time.sleep(duration / (2 * iterations))
        apply_style(original_style)
        time.sleep(duration / (2 * iterations))

def test_title_verification(setup):
    driver = setup
    driver.get("https://10.20.170.151/predictivepolicing/login.php")
    expected_title = "PREDICTIVE POLICING"
    actual_title = driver.title
    assert actual_title == expected_title, f"Test Failed: Title is '{actual_title}' but expected '{expected_title}'"
    take_screenshot(driver, 'title_verification')


def login(driver, username, password):
    username_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter username or email']")
    password_field = driver.find_element(By.XPATH, "//input[@id='password']")
    login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']")

    # Blink the fields before interacting
    # blink_element(driver, username_field)
    # blink_element(driver, password_field)
    # blink_element(driver, login_button)

    # Enter credentials and submit the form
    blink_element(driver, username_field)
    username_field.send_keys(username)
    blink_element(driver, password_field)
    password_field.send_keys(password)
    blink_element(driver, login_button)
    login_button.click()


def test_login_blank_field(setup):
    driver = setup
    time.sleep(1)
    empty_username = ""
    empty_password = ""
    login(driver, empty_username, empty_password)

    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        assert "Please fill out this field" in alert.text
        alert.accept()
    except TimeoutException:
        pass
    take_screenshot(driver, 'login_blank_field')


def test_user_name_empty(setup):
    driver = setup
    time.sleep(1)
    empty_username = ""
    valid_password = "123456@abc"
    login(driver, empty_username, valid_password)

    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        assert "Username must be filled out" in alert.text
        alert.accept()
    except TimeoutException:
        pass
    take_screenshot(driver, 'Empty_user_name')

def test_only_password_empty(setup):
    driver = setup
    time.sleep(1)
    valid_username = "QA_USER"
    empty_password = ""
    login(driver, valid_username, empty_password)

    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        assert "Please fill out this field" in alert.text
        alert.accept()
    except TimeoutException:
        pass
    take_screenshot(driver, 'Empty_Password')

def test_wrong_credentials(setup):
    driver = setup
    invalid_username = "QA_USER1"
    invalid_password = "12345@"
    login(driver, invalid_username, invalid_password)
    time.sleep(2)
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        assert "Password must be between 8 and 25 characters" in alert.text
        alert.accept()
    except TimeoutException:
        pass
    take_screenshot(driver, 'Invalid_Credentials')

def test_small_casesensitive(setup):
    driver = setup
    time.sleep(1)
    invalid_username = "QA_USER"
    valid_password = "123456@abc"
    login(driver, invalid_username, valid_password)
    time.sleep(2)
    assert "Successfully logged in"
    take_screenshot(driver, 'Successfully log in')


def scroll_down(driver):
    # Scroll down the page by 500 pixels
    driver.execute_script("window.scrollBy(0, 1000);")


def test_dashboard_Suspect_Tracker(setup):
    driver = setup
    time.sleep(15)
    link_to_dashboard = driver.find_element(By.XPATH, "//h6[normalize-space()='Suspect Tracker']")
    blink_element(driver, link_to_dashboard)
    link_to_dashboard.click()
    time.sleep(1)
    scroll_down(driver)
    time.sleep(2)
    assert "Successfully click on Suspect Tracker"
    take_screenshot(driver,"Suspect tracker")

def test_dashboard_Crime_Heatmap(setup):
    driver = setup
    time.sleep(10)
    link_to_dashboard = driver.find_element(By.XPATH, "//h6[normalize-space()='Crime Heatmaps']")
    blink_element(driver, link_to_dashboard)
    link_to_dashboard.click()
    time.sleep(10)
    scroll_down(driver)
    time.sleep(2)
    assert "Successfully click on Crime Heatmaps"
    take_screenshot(driver,"Crime Heatmaps")

def test_dashboard_Predictive_Analysis(setup):
    driver = setup
    time.sleep(5)
    link_to_dashboard = driver.find_element(By.XPATH, "//h6[normalize-space()='Predictive Analysis']")
    blink_element(driver, link_to_dashboard)
    link_to_dashboard.click()
    time.sleep(10)
    scroll_down(driver)
    time.sleep(2)
    assert "Successfully click on Predictive Analysis"
    take_screenshot(driver,"Predictive Analysis")

def test_dashboard_Setting(setup):
    driver = setup
    time.sleep(5)
    link_to_dashboard = driver.find_element(By.XPATH, "//h6[normalize-space()='Settings']")
    blink_element(driver, link_to_dashboard)
    link_to_dashboard.click()
    time.sleep(1)
    scroll_down(driver)
    time.sleep(2)
    assert "Successfully click on Settings"
    take_screenshot(driver,"Settings")

def test_navigation_Dashboard(setup):
    driver = setup
    link_to_dashboard = driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']")
    blink_element(driver, link_to_dashboard)
    link_to_dashboard.click()
    time.sleep(10)
    assert "Successfully click on Dashboard"
    take_screenshot(driver,"Navigation Dashboard")


def test_dropdown_division_and_ps(setup):
    driver = setup
    time.sleep(1)

    # Locate the division dropdown
    dropdown_division = driver.find_element(By.XPATH, "//select[@id='division']")
    division_options = dropdown_division.find_elements(By.TAG_NAME, "option")

    # Iterate over each division
    for division_option in division_options:
        division_text = division_option.text

        # Skip the default option if needed
        if division_text in ["", "Select Division"]:  # Adjust according to actual options
            continue

        blink_element(driver, division_option)
        division_option.click()
        print(f"Selected division: {division_text}")

        # Wait for the PS dropdown to load/update
        time.sleep(2)

        # Locate the PS dropdown
        dropdown_ps = driver.find_element(By.XPATH, "//select[@id='ps']")
        ps_options = dropdown_ps.find_elements(By.TAG_NAME, "option")

        # Iterate over each PS for the selected division
        for ps_option in ps_options:
            ps_text = ps_option.text

            # Skip the default option if needed
            if ps_text in ["", "Select PS"]:  # Adjust according to actual options
                continue

            blink_element(driver, ps_option)
            ps_option.click()
            print(f"Selected PS: {ps_text}")

            # Wait for any potential loading after selecting PS
            time.sleep(2)

            # Perform any additional actions or validations here

            # Take a screenshot for each PS selection
            take_screenshot(driver, f"Division_{division_text}_PS_{ps_text}")

        # Scroll down after all PS selections for a division
        scroll_down(driver)

    assert True, "Successfully selected all divisions and corresponding PS"

def test_map_ps_zoom_in(setup):
    driver = setup
    time.sleep(5)

    try:
        # Find and click the zoom in button multiple times
        for _ in range(5):  # Adjust the number of clicks as needed for full zoom
            zoom_in_button = driver.find_element(By.XPATH, "//a[@title='Zoom in']")
            blink_element(driver, zoom_in_button)
            zoom_in_button.click()
            time.sleep(1)  # Wait for the map to update after each zoom
    except Exception as e:
        print(f"Error: {e}")

    take_screenshot(driver, 'Zoom_in_on_Map')
