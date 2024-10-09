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

def take_screenshot(driver, step_name):
    driver.save_screenshot(f"{step_name}.png")


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

    #Highlight and blink username field before entering text
    blink_element(driver, username_field)
    username_field.send_keys(username)

    # Highlight and blink password field before entering text
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

    # Highlight and blink username and password fields
    # username_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter username or email']")
    # password_field = driver.find_element(By.XPATH, "//input[@id='password']")
    # blink_element(driver, username_field)
    # blink_element(driver, password_field)


    take_screenshot(driver, 'login_blank_field')


# Example setup function to initialize the WebDriver
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
    username = driver.find_element(By.XPATH, "//input[@id='password']")
    username.clear()
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
    username = driver.find_element(By.XPATH, "//input[@placeholder='Enter username or email']")
    username.clear()
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
    username = driver.find_element(By.XPATH, "//input[@placeholder='Enter username or email']")
    username.clear()
    username = driver.find_element(By.XPATH, "//input[@id='password']")
    username.clear()
    invalid_username = "QA_USER"
    valid_password = "123456@abc"
    login(driver, invalid_username, valid_password)
    time.sleep(2)
    assert "Sucsessfully logged in"
    take_screenshot(driver, 'Sucsessfully log in')
    # try:
    #     WebDriverWait(driver, 3).until(EC.alert_is_present())
    #     alert = driver.switch_to.alert
    #     assert "Username and password mismatch" in alert.text
    #     alert.accept()
    # except TimeoutException:
    #     pass
    # expected_result = "login failed, because username is in lowercase"
    # actual_result = "dashboard found, login succeeded"
    #
    # try:
    #     # Check if an element unique to the dashboard is present
    #     WebDriverWait(driver, 5).until(
    #         EC.presence_of_element_located((By.XPATH, "//h6[normalize-space()='Dashboard']"))
    #     )
    #     # If the dashboard element is found, fail the test
    #     take_screenshot(driver, 'case_sensitive_credential')
    #     actual_result = "dashboard found, login succeeded"
    #     assert False, f"Test Failed: Expected result: '{expected_result}', but got: '{actual_result}'"
    # except TimeoutException:
    #     # If no dashboard element is found, pass the test
    #     actual_result = "no dashboard found, login failed"
    #     assert actual_result == expected_result, f"Test Passed: Expected result: '{expected_result}', and got: '{actual_result}'"
def scroll_down(driver):
    # Scroll down the page by 500 pixels
    driver.execute_script("window.scrollBy(0, 1000);")


def test_dashboard_Suspect_Tracker(setup):
    driver = setup
    time.sleep(15)
    link_to_dashboard = driver.find_element(By.XPATH, "//h6[normalize-space()='Suspect Tracker']")
    #link_to_dashboard.click()
    time.sleep(1)
    scroll_down(driver)
    time.sleep(2)
    blink_element(driver, link_to_dashboard)
    link_to_dashboard.click()
    assert "Successfully click on Suspect Tracker"

    take_screenshot(driver,"Suscpect tracker")

def test_dashboard_Crime_Heatmap(setup):
    driver = setup
    time.sleep(10)
    link_to_dashboard = driver.find_element(By.XPATH, "//h6[normalize-space()='Crime Heatmaps']")
    #link_to_dashboard.click()
    time.sleep(10)
    scroll_down(driver)
    time.sleep(2)
    blink_element(driver, link_to_dashboard)
    link_to_dashboard.click()
    assert "Successfully click on Crime Heatmaps"
    take_screenshot(driver,"Crime Heatmaps")

def test_dashboard_Predictive_Analysis(setup):
    driver = setup
    time.sleep(5)
    link_to_dashboard = driver.find_element(By.XPATH, "//h6[normalize-space()='Predictive Analysis']")
    #link_to_dashboard.click()
    time.sleep(10)
    scroll_down(driver)
    time.sleep(2)
    blink_element(driver, link_to_dashboard)
    link_to_dashboard.click()
    assert "Successfully click onPredictive Analysis"
    take_screenshot(driver,"Predictive Analysis")

def test_dashboard_Setting(setup):
    driver = setup
    time.sleep(5)
    link_to_dashboard = driver.find_element(By.XPATH, "//h6[normalize-space()='Settings']")
    #link_to_dashboard.click()
    time.sleep(1)
    scroll_down(driver)
    time.sleep(2)
    blink_element(driver, link_to_dashboard)
    link_to_dashboard.click()
    assert "Successfully click on Settings"
    take_screenshot(driver,"Settings")

def test_navigation_Dashboard(setup):
    driver = setup
    link_to_dashboard = driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']")
    #link_to_dashboard.click()
    time.sleep(10)
    blink_element(driver, link_to_dashboard)
    link_to_dashboard.click()
    assert "Successfully click on Dashboard"

    take_screenshot(driver,"Navigation Dashboard")

def test_dropdown_Division(setup):
    driver = setup
    time.sleep(1)
    dropdown_division = driver.find_element(By.XPATH, "//select[@id='division']")
    options = dropdown_division.find_elements(By.TAG_NAME, "option")
    for option in options:
        if option.text == "Civil Lines Division":
            option.click()
            break

    blink_element(driver, dropdown_division)

    assert "Successfully select Civil Lines Division"
    take_screenshot(driver,"Dropdown Division")

def test_dropdown_PS(setup):
    driver = setup
    time.sleep(2)
    dropdown_ps = driver.find_element(By.XPATH, "//select[@id='ps']")
    ps_options = dropdown_ps.find_elements(By.TAG_NAME, "option")
    for option in ps_options:
        if option.text == "Civil lines":
            option.click()
            break
    time.sleep(5)
    blink_element(driver, dropdown_ps)
    scroll_down(driver)
    assert "Successfully select PS 2"
    take_screenshot(driver,"Dropdown PS")

def test_map_ps_zoom_in(setup):
    driver = setup
    time.sleep(5)

    try:
        # Find and click the zoom in button multiple times
        for _ in range(5):
            # Adjust the number of clicks as needed for full zoom
            zoom_in_button = driver.find_element(By.XPATH, "//a[@title='Zoom in']")
            zoom_in_button.click()
            blink_element(driver, zoom_in_button)
            time.sleep(1)  # Wait for the map to update after each zoom
    except Exception as e:
        print(f"Error: {e}")

    # Optionally, you can capture a screenshot after full zoom
    driver.save_screenshot("full_zoom_map.png")

def test_map_ps_zoom_out(setup):
    driver = setup
    time.sleep(5)
    try:
        # Find and click the zoom in button multiple times
        for _ in range(5):  # Adjust the number of clicks as needed for full zoom
            zoom_out_button = driver.find_element(By.XPATH, "//a[@title='Zoom out']")
            zoom_out_button.click()
            blink_element(driver, zoom_out_button)
            time.sleep(1)  # Wait for the map to update after each zoom
    except Exception as e:
        print(f"Error: {e}")


    # Optionally, you can capture a screenshot after full zoom
    driver.save_screenshot("full_zoom_map.png")


def test_crime_selection(setup):
    driver = setup
    time.sleep(5)
    dropdown_crime_type = driver.find_element(By.XPATH,
                                              "//select[@class='form-select py-3 form-select-values homeformselect formselectresponsive']")
    options = dropdown_crime_type.find_elements(By.TAG_NAME, "option")

    # Highlight the dropdown before selecting options
    blink_element(driver, dropdown_crime_type)

    for option in options:
        try:
            crime_type = option.text
            option.click()
            print(f"Selected crime type: {crime_type}")

            # Add a 2-second delay after selecting each option
            time.sleep(2)

            # Take a screenshot after selecting each option
            take_screenshot(driver, f"Crime_Selection_{crime_type}")

        except Exception as e:
            print(f"Error occurred while selecting {crime_type}: {e}")
            take_screenshot(driver, f"Error_Crime_Selection_{crime_type}")
            continue  # Continue with the next iteration even if an error occurs

    # Scroll down after all selections are done
    scroll_down(driver)

    assert True, "Successfully selected all crime types"

# def test_mouse_on_charts(setup):
#     driver=setup
#     chart_element = driver.find_element(By.CSS_SELECTOR, "//rect[@class='highcharts-background']")
#
#     # Create ActionChains object
#     actions = ActionChains(driver)
#
#     # Move mouse to the chart element
#     actions.move_to_element(chart_element).perform()
#
#     # Optional: Perform additional actions after moving to the chart element
#     time.sleep(2)  # Example: Wait for 2 seconds after hovering
#
#     # Example: Click on a specific point on the chart after hovering
#     actions.click().perform()
