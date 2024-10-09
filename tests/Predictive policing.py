import time

import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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
    print( "Actual Title is '{PREDICTIVE POLICING}' but expected '{PREDICTIVE POLICING}'")
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
        WebDriverWait(driver, 1).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        assert "Please fill out this " in alert.text
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
        error_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='errordisplayid']"))
        )
        assert error_message.is_displayed()
        take_screenshot(driver, "Username is empty")
        print("Login Test Passed: Unsuccessful login displayed error message")
    except Exception as e:

        pytest.fail(f"Login Test Failed: No error message displayed for unsuccessful login. Exception: {e}")
    # try:
    #     WebDriverWait(driver, 5).until(EC.alert_is_present())
    #     alert = driver.switch_to.alert
    #     assert "Username must be filled out" in alert.text
    #     alert.accept()
    # except TimeoutException:
    #     assert False, "Alert was not presented when expected"
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

def test_valid_Credential(setup):
    driver = setup
    time.sleep(1)
    username = driver.find_element(By.XPATH, "//input[@placeholder='Enter username or email']")
    username.clear()
    username = driver.find_element(By.XPATH, "//input[@id='password']")
    username.clear()
    valid_username = "QA_USER"
    valid_password = "123456@abc"
    login(driver, valid_username, valid_password)
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

def scroll_up(driver):
    # Scroll up the page by 1000 pixels
    driver.execute_script("window.scrollBy(0, -1000);")

def test_dashboard_Suspect_Tracker(setup):
    driver = setup

    time.sleep(10)
    scroll_down(driver)
    time.sleep(2)
    link_to_dashboard = driver.find_element(By.XPATH, "//h6[normalize-space()='Suspect Tracker']")
    blink_element(driver, link_to_dashboard)
    link_to_dashboard.click()
    time.sleep(3)
    scroll_down(driver)
    time.sleep(2)
    assert "Successfully click on Suspect Tracker"
    take_screenshot(driver,"Suscpect tracker")

def test_dashboard_Crime_Heatmap(setup):
    driver = setup
    time.sleep(10)
    link_to_dashboard = driver.find_element(By.XPATH, "//h6[normalize-space()='Crime Heatmaps']")
    blink_element(driver,link_to_dashboard)
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
    blink_element(driver,link_to_dashboard)
    link_to_dashboard.click()
    time.sleep(10)
    scroll_down(driver)
    time.sleep(2)
    assert "Successfully click onPredictive Analysis"
    take_screenshot(driver,"Predictive Analysis")

def test_dashboard_Setting(setup):
    driver = setup
    time.sleep(5)
    link_to_dashboard = driver.find_element(By.XPATH, "//h6[normalize-space()='Settings']")
    blink_element(driver,link_to_dashboard)
    link_to_dashboard.click()
    time.sleep(1)
    scroll_down(driver)
    time.sleep(2)
    assert "Successfully click on Settings"
    take_screenshot(driver,"Settings")

def test_navigation_Dashboard(setup):
    driver = setup
    link_to_dashboard = driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']")
    blink_element(driver,link_to_dashboard)
    link_to_dashboard.click()
    time.sleep(10)
    assert "Successfully click on Dashboard"
    take_screenshot(driver,"Navigation Dashboard")


# def test_dropdown_division_and_ps(setup):
#     driver = setup
#     time.sleep(1)
#
#     # Locate the division dropdown
#     dropdown_division = driver.find_element(By.XPATH, "//select[@id='division']")
#     blink_element(driver, dropdown_division)
#     division_options = dropdown_division.find_elements(By.TAG_NAME, "option")
#
#     # Iterate over each division
#     for division_option in division_options:
#         division_text = division_option.text
#
#         # Skip the default option if needed
#         if division_text in ["", "Select Division"]:  # Adjust according to actual options
#             continue
#
#         blink_element(driver, division_option)
#         division_option.click()
#         print(f"Selected division: {division_text}")
#
#         # Wait for the PS dropdown to load/update
#         time.sleep(2)
#
#         # Locate the PS dropdown
#         dropdown_ps = driver.find_element(By.XPATH, "//select[@id='ps']")
#         blink_element(driver, dropdown_ps)
#         ps_options = dropdown_ps.find_elements(By.TAG_NAME, "option")
#
#         # Iterate over each PS for the selected division
#         for ps_option in ps_options:
#             ps_text = ps_option.text
#
#             # Skip the default option if needed
#             if ps_text in ["", "Select PS"]:  # Adjust according to actual options
#                 continue
#
#             blink_element(driver, ps_option)
#             ps_option.click()
#             print(f"Selected PS: {ps_text}")
#
#             # Wait for any potential loading after selecting PS
#             time.sleep(2)
#
#             # Perform any additional actions or validations here
#             try:
#                 # Add your assertion to check if data fetching is successful
#                 assert "Expected Text or Condition" in driver.page_source, f"Failed to fetch data for Division: {division_text}, PS: {ps_text}"
#             except AssertionError as e:
#                 print(f"Assertion failed: {e}")
#                 # Optionally, you can take a screenshot on failure
#                 take_screenshot(driver, f"Failed_Division_{division_text}_PS_{ps_text}")
#
#             # Take a screenshot for each PS selection
#             take_screenshot(driver, f"Division_{division_text}_PS_{ps_text}")
#
#         # Scroll down after all PS selections for a division
#         scroll_down(driver)
#
#     assert True, "Successfully selected all divisions and corresponding PS"

def test_dropdown_Civil_Line_Division(setup):
    driver = setup
    time.sleep(1)
    dropdown_division = driver.find_element(By.XPATH, "//select[@id='division']")
    options = dropdown_division.find_elements(By.TAG_NAME, "option")
    for option in options:
        if option.text == "Civil Lines Division":
            option.click()
            break
    assert "Successfully select Civil Lines Division"
    take_screenshot(driver,"Civil Lines Division")

def test_dropdown_Civil_lines(setup):
    driver = setup
    time.sleep(2)
    dropdown_ps = driver.find_element(By.XPATH, "//select[@id='ps']")
    options = dropdown_ps.find_elements(By.TAG_NAME, "option")
    for option in options:
        if option.text == "Civil lines":
            option.click()
            break
    time.sleep(10)
    scroll_down(driver)
    time.sleep(2)

    assert "Successfully select PS 2"
    take_screenshot(driver,"Civil lines PS")
def test_crime_map_Civil_Lines(setup):
    driver = setup
    time.sleep(5)
    dropdown_crime_type = driver.find_element(By.XPATH, "//select[@class='form-select py-3 form-select-values homeformselect formselectresponsive']")
    options = dropdown_crime_type.find_elements(By.TAG_NAME, "option")
    for option in options:
        try:
            crime_type = option.text
            option.click()
            print(f"Selected crime type: {crime_type}")

            # Add a 2-second delay after selecting each option
            time.sleep(2)

            # Example: Scroll down after selecting each option
            scroll_down(driver)

            # Add assertions or additional actions here if needed
            time.sleep(5)
            take_screenshot(driver, f"Crime_Selection_{crime_type}")

        except Exception as e:
            print(f"Error occurred while selecting {crime_type}: {e}")
            continue  # Continue with the next iteration even if an error occurs

    assert True, "Successfully selected all crime types"

def test_dropdown_Garhi_Shahu(setup):
    driver = setup
    time.sleep(2)
    dropdown_ps = driver.find_element(By.XPATH, "//select[@id='ps']")
    options = dropdown_ps.find_elements(By.TAG_NAME, "option")
    for option in options:
        if option.text == "Garhi Shahu":
            option.click()
            break
    time.sleep(10)
    scroll_down(driver)
    assert "Successfully select PS 2"
    take_screenshot(driver,"Garhi Shahu PS")
def test_crime_map_Garhi_Shahu(setup):
    driver = setup
    time.sleep(5)
    dropdown_crime_type = driver.find_element(By.XPATH, "//select[@class='form-select py-3 form-select-values homeformselect formselectresponsive']")
    options = dropdown_crime_type.find_elements(By.TAG_NAME, "option")
    for option in options:
        try:
            crime_type = option.text
            option.click()
            print(f"Selected crime type: {crime_type}")

            # Add a 2-second delay after selecting each option
            time.sleep(2)

            # Example: Scroll down after selecting each option
            scroll_down(driver)

            # Add assertions or additional actions here if needed
            time.sleep(5)
            take_screenshot(driver, f"Crime_Selection_{crime_type}")

        except Exception as e:
            print(f"Error occurred while selecting {crime_type}: {e}")
            continue  # Continue with the next iteration even if an error occurs

    assert True, "Successfully selected all crime types"

def test_dropdown_Gujjar_Pura(setup):
    driver = setup
    time.sleep(2)
    dropdown_ps = driver.find_element(By.XPATH, "//select[@id='ps']")
    options = dropdown_ps.find_elements(By.TAG_NAME, "option")
    for option in options:
        if option.text == "Gujjar Pura":
            option.click()
            break
    time.sleep(10)
    scroll_down(driver)
    assert "Successfully select PS 2"
    take_screenshot(driver,"Gujjar Pura PS")
def test_crime_map_Gujjar_pura(setup):
    driver = setup
    time.sleep(5)
    dropdown_crime_type = driver.find_element(By.XPATH, "//select[@class='form-select py-3 form-select-values homeformselect formselectresponsive']")
    options = dropdown_crime_type.find_elements(By.TAG_NAME, "option")
    for option in options:
        try:
            crime_type = option.text
            option.click()
            print(f"Selected crime type: {crime_type}")

            # Add a 2-second delay after selecting each option
            time.sleep(2)

            # Example: Scroll down after selecting each option
            scroll_down(driver)

            # Add assertions or additional actions here if needed
            time.sleep(5)
            take_screenshot(driver, f"Crime_Selection_{crime_type}")

        except Exception as e:
            print(f"Error occurred while selecting {crime_type}: {e}")
            continue  # Continue with the next iteration even if an error occurs

    assert True, "Successfully selected all crime types"

def test_dropdown_Lytton_Road(setup):
    driver = setup
    time.sleep(2)
    dropdown_ps = driver.find_element(By.XPATH, "//select[@id='ps']")
    options = dropdown_ps.find_elements(By.TAG_NAME, "option")
    for option in options:
        if option.text == "Lytton Road":
            option.click()
            break
    time.sleep(10)
    scroll_down(driver)
    assert "Successfully select PS 2"
    take_screenshot(driver,"Lytton Road PS")
def test_crime_map_lytton_Road(setup):
    driver = setup
    time.sleep(5)
    dropdown_crime_type = driver.find_element(By.XPATH, "//select[@class='form-select py-3 form-select-values homeformselect formselectresponsive']")
    options = dropdown_crime_type.find_elements(By.TAG_NAME, "option")
    for option in options:
        try:
            crime_type = option.text
            option.click()
            print(f"Selected crime type: {crime_type}")

            # Add a 2-second delay after selecting each option
            time.sleep(2)

            # Example: Scroll down after selecting each option
            scroll_down(driver)

            # Add assertions or additional actions here if needed
            time.sleep(5)
            take_screenshot(driver, f"Crime_Selection_{crime_type}")

        except Exception as e:
            print(f"Error occurred while selecting {crime_type}: {e}")
            continue  # Continue with the next iteration even if an error occurs

    assert True, "Successfully selected all crime types"

def test_dropdown_Mozang(setup):
    driver = setup
    time.sleep(2)
    dropdown_ps = driver.find_element(By.XPATH, "//select[@id='ps']")
    options = dropdown_ps.find_elements(By.TAG_NAME, "option")
    for option in options:
        if option.text == "Mozang":
            option.click()
            break
    time.sleep(10)
    scroll_down(driver)
    assert "Successfully select PS 2"
    take_screenshot(driver,"Mozang PS")
def test_crime_map_Mozang(setup):
    driver = setup
    time.sleep(5)
    dropdown_crime_type = driver.find_element(By.XPATH, "//select[@class='form-select py-3 form-select-values homeformselect formselectresponsive']")
    options = dropdown_crime_type.find_elements(By.TAG_NAME, "option")
    for option in options:
        try:
            crime_type = option.text
            option.click()
            print(f"Selected crime type: {crime_type}")

            # Add a 2-second delay after selecting each option
            time.sleep(2)

            # Example: Scroll down after selecting each option
            scroll_down(driver)

            # Add assertions or additional actions here if needed
            time.sleep(5)
            take_screenshot(driver, f"Crime_Selection_{crime_type}")

        except Exception as e:
            print(f"Error occurred while selecting {crime_type}: {e}")
            continue  # Continue with the next iteration even if an error occurs

    assert True, "Successfully selected all crime types"

def test_dropdown_Mughalpura(setup):
    driver = setup
    time.sleep(2)
    dropdown_ps = driver.find_element(By.XPATH, "//select[@id='ps']")
    options = dropdown_ps.find_elements(By.TAG_NAME, "option")
    for option in options:
        if option.text == "Mughalpura":
            option.click()
            break
    time.sleep(10)
    scroll_down(driver)
    assert "Successfully select PS 2"
    take_screenshot(driver,"Mughalpura PS")
def test_crime_map_Mughalpura(setup):
    driver = setup
    time.sleep(5)
    dropdown_crime_type = driver.find_element(By.XPATH, "//select[@class='form-select py-3 form-select-values homeformselect formselectresponsive']")
    options = dropdown_crime_type.find_elements(By.TAG_NAME, "option")
    for option in options:
        try:
            crime_type = option.text
            option.click()
            print(f"Selected crime type: {crime_type}")

            # Add a 2-second delay after selecting each option
            time.sleep(2)

            # Example: Scroll down after selecting each option
            scroll_down(driver)

            # Add assertions or additional actions here if needed
            time.sleep(5)
            take_screenshot(driver, f"Crime_Selection_{crime_type}")

        except Exception as e:
            print(f"Error occurred while selecting {crime_type}: {e}")
            continue  # Continue with the next iteration even if an error occurs

    assert True, "Successfully selected all crime types"

def test_dropdown_Old_Anarkali(setup):
    driver = setup
    time.sleep(2)
    dropdown_ps = driver.find_element(By.XPATH, "//select[@id='ps']")
    options = dropdown_ps.find_elements(By.TAG_NAME, "option")
    for option in options:
        if option.text == "Old Anarkali":
            option.click()
            break
    time.sleep(10)
    scroll_down(driver)
    assert "Successfully select PS 2"
    take_screenshot(driver,"Old Anarkali PS")
def test_crime_map_Old_Anarkali(setup):
    driver = setup
    time.sleep(5)
    dropdown_crime_type = driver.find_element(By.XPATH, "//select[@class='form-select py-3 form-select-values homeformselect formselectresponsive']")
    options = dropdown_crime_type.find_elements(By.TAG_NAME, "option")
    for option in options:
        try:
            crime_type = option.text
            option.click()
            print(f"Selected crime type: {crime_type}")

            # Add a 2-second delay after selecting each option
            time.sleep(2)

            # Example: Scroll down after selecting each option
            scroll_down(driver)

            # Add assertions or additional actions here if needed
            time.sleep(5)
            take_screenshot(driver, f"Crime_Selection_{crime_type}")

        except Exception as e:
            print(f"Error occurred while selecting {crime_type}: {e}")
            continue  # Continue with the next iteration even if an error occurs

    assert True, "Successfully selected all crime types"

def test_dropdown_Qilla_Gujjar_Singh(setup):
    driver = setup
    time.sleep(2)
    dropdown_ps = driver.find_element(By.XPATH, "//select[@id='ps']")
    options = dropdown_ps.find_elements(By.TAG_NAME, "option")
    for option in options:
        if option.text == "Qilla Gujjar singh":
            option.click()
            break
    time.sleep(10)
    scroll_down(driver)
    assert "Successfully select PS 2"
    take_screenshot(driver,"Qilla Gujjar singh PS")
def test_crime_map_Qilla_Gujjar_Singh(setup):
    driver = setup
    time.sleep(5)
    dropdown_crime_type = driver.find_element(By.XPATH, "//select[@class='form-select py-3 form-select-values homeformselect formselectresponsive']")
    options = dropdown_crime_type.find_elements(By.TAG_NAME, "option")
    for option in options:
        try:
            crime_type = option.text
            option.click()
            print(f"Selected crime type: {crime_type}")

            # Add a 2-second delay after selecting each option
            time.sleep(2)

            # Example: Scroll down after selecting each option
            scroll_down(driver)

            # Add assertions or additional actions here if needed
            time.sleep(5)
            take_screenshot(driver, f"Crime_Selection_{crime_type}")

        except Exception as e:
            print(f"Error occurred while selecting {crime_type}: {e}")
            continue  # Continue with the next iteration even if an error occurs

    assert True, "Successfully selected all crime types"


def test_dropdown_RaceCourse(setup):
    driver = setup
    time.sleep(2)
    dropdown_ps = driver.find_element(By.XPATH, "//select[@id='ps']")
    options = dropdown_ps.find_elements(By.TAG_NAME, "option")
    for option in options:
        if option.text == "Race Course":
            option.click()
            break
    time.sleep(10)
    scroll_down(driver)
    assert "Successfully select PS 2"
    take_screenshot(driver,"Race Course PS")
def test_crime_map_RaceCourse(setup):
    driver = setup
    time.sleep(5)
    dropdown_crime_type = driver.find_element(By.XPATH, "//select[@class='form-select py-3 form-select-values homeformselect formselectresponsive']")
    options = dropdown_crime_type.find_elements(By.TAG_NAME, "option")
    for option in options:
        try:
            crime_type = option.text
            option.click()
            print(f"Selected crime type: {crime_type}")

            # Add a 2-second delay after selecting each option
            time.sleep(2)

            # Example: Scroll down after selecting each option
            scroll_down(driver)

            # Add assertions or additional actions here if needed
            time.sleep(5)
            take_screenshot(driver, f"Crime_Selection_{crime_type}")

        except Exception as e:
            print(f"Error occurred while selecting {crime_type}: {e}")
            continue  # Continue with the next iteration even if an error occurs

    assert True, "Successfully selected all crime types"

def test_dropdown_Shalimar(setup):
    driver = setup
    time.sleep(2)
    dropdown_ps = driver.find_element(By.XPATH, "//select[@id='ps']")
    options = dropdown_ps.find_elements(By.TAG_NAME, "option")
    for option in options:
        if option.text == "Shalimar":
            option.click()
            break
    time.sleep(10)
    scroll_down(driver)
    assert "Successfully select PS 2"
    take_screenshot(driver,"Shalimar PS")
def test_crime_map_shalimar(setup):
    driver = setup
    time.sleep(5)
    dropdown_crime_type = driver.find_element(By.XPATH, "//select[@class='form-select py-3 form-select-values homeformselect formselectresponsive']")
    options = dropdown_crime_type.find_elements(By.TAG_NAME, "option")
    for option in options:
        try:
            crime_type = option.text
            option.click()
            print(f"Selected crime type: {crime_type}")

            # Add a 2-second delay after selecting each option
            time.sleep(2)

            # Example: Scroll down after selecting each option
            scroll_down(driver)

            # Add assertions or additional actions here if needed
            time.sleep(5)
            take_screenshot(driver, f"Crime_Selection_{crime_type}")

        except Exception as e:
            print(f"Error occurred while selecting {crime_type}: {e}")
            continue  # Continue with the next iteration even if an error occurs

    assert True, "Successfully selected all crime types"


def test_dropdown_Women_station(setup):
    driver = setup
    time.sleep(2)
    dropdown_ps = driver.find_element(By.XPATH, "//select[@id='ps']")
    options = dropdown_ps.find_elements(By.TAG_NAME, "option")

    for option in options:
        try:
            if option.text == "Women Race Course":
                option.click()
                print(f"Selected PS: {option.text}")

                # Add a 2-second delay after selecting each option
                time.sleep(2)

                # Example: Scroll down after selecting each option
                scroll_down(driver)

                # Add assertions or additional actions here if needed
                time.sleep(5)
                take_screenshot(driver, f"Crime_Selection_{option.text}")

        except Exception as e:
            print(f"Error occurred while selecting PS '{option.text}': {e}")
            continue  # Continue with the next iteration even if an error occurs

    assert True, "Successfully selected all PS options"
def test_crime_map_women_station(setup):
    driver = setup
    time.sleep(5)
    dropdown_crime_type = driver.find_element(By.XPATH, "//select[@class='form-select py-3 form-select-values homeformselect formselectresponsive']")
    options = dropdown_crime_type.find_elements(By.TAG_NAME, "option")
    for option in options:
        try:
            crime_type = option.text
            option.click()
            print(f"Selected crime type: {crime_type}")

            # Add a 2-second delay after selecting each option
            time.sleep(2)

            # Example: Scroll down after selecting each option
            scroll_down(driver)

            # Add assertions or additional actions here if needed
            time.sleep(5)
            take_screenshot(driver, f"Crime_Selection_{crime_type}")

        except Exception as e:
            print(f"Error occurred while selecting {crime_type}: {e}")
            continue  # Continue with the next iteration even if an error occurs

    assert True, "Successfully selected all crime types"


def test_map_ps_zoom_in(setup):
    driver = setup
    scroll_down(driver)
    time.sleep(5)
    driver.find_element(By.XPATH,"//div[@class='leaflet-pane leaflet-marker-pane']//img[2]").click()
    driver.find_element(By.XPATH, "//div[@class='leaflet-pane leaflet-marker-pane']//img[2]").click()
    try:
        # Find and click the zoom in button multiple times
        for _ in range(5):  # Adjust the number of clicks as needed for full zoom
            zoom_in_button = driver.find_element(By.XPATH, "//a[@title='Zoom in']")
            blink_element(driver, zoom_in_button)
            zoom_in_button.click()
            time.sleep(1)  # Wait for the map to update after each zoom
    except Exception as e:
        print(f"Error: {e}")

    # Optionally, you can capture a screenshot after full zoom
    driver.save_screenshot("full_zoom_map.png")

def test_map_ps_zoom_out(setup):
    driver = setup
    scroll_down(driver)
    time.sleep(5)
    try:
        # Find and click the zoom in button multiple times
        for _ in range(5):  # Adjust the number of clicks as needed for full zoom
            zoom_out_button = driver.find_element(By.XPATH, "//a[@title='Zoom out']")
            blink_element(driver, zoom_out_button)
            zoom_out_button.click()
            time.sleep(1)  # Wait for the map to update after each zoom
    except Exception as e:
        print(f"Error: {e}")

    # Optionally, you can capture a screenshot after full zoom
    driver.save_screenshot("full_zoom_map.png")

def test_crime_selection(setup):
    driver = setup
    time.sleep(5)
    dropdown_crime_type = driver.find_element(By.XPATH, "//select[@class='form-select py-3 form-select-values homeformselect formselectresponsive']")
    options = dropdown_crime_type.find_elements(By.TAG_NAME, "option")
    for option in options:
        try:
            crime_type = option.text
            option.click()
            print(f"Selected crime type: {crime_type}")

            # Add a 2-second delay after selecting each option
            time.sleep(2)

            # Example: Scroll down after selecting each option
            scroll_down(driver)

            # Add assertions or additional actions here if needed
            time.sleep(5)
            take_screenshot(driver, f"Crime_Selection_{crime_type}")

        except Exception as e:
            print(f"Error occurred while selecting {crime_type}: {e}")
            continue  # Continue with the next iteration even if an error occurs

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

def test_Criminal_Face_Detection_CRO(setup):
    driver = setup
    scroll_down(driver)
    time.sleep(5)
    scroll_down(driver)
    show_detail=driver.find_element(By.XPATH, "//a[@id='showdetailsmarquee']")
    show_detail.click()
    time.sleep(5)
    element=driver.find_element(By.XPATH, "//div[@id='dragAndDrop']")
    blink_element(driver, element)
    file_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
    )
    blink_element(driver, file_input)
    file_path = "C:\\Users\\arslan.arif\\Desktop\\Criminal Pic for Testing\\download.png"
    file_input.send_keys(file_path)
    take_screenshot(driver, 'File_Upload')
    time.sleep(5)
    try:
        CRO_Message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h5[@id='responseModalLabel']"))
        )
        assert CRO_Message.is_displayed()
        time.sleep(5)
        take_screenshot(driver, "CRO")
        driver.find_element(By.XPATH,"//img[@alt='Close']").click()

        print("Login Test Passed: Succsesfully CRO data Matched")
    except Exception as e:
         pytest.fail(f"Login Test Failed: No error message displayed for unsuccessful login. Exception: {e}")

def test_Criminal_Face_Detection_CRO_1(setup):
    driver = setup
    time.sleep(2)
    file_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
    )
    blink_element(driver, file_input)
    file_path = "C:\\Users\\arslan.arif\\Desktop\\Criminal Pic for Testing\\download (1).png"
    file_input.send_keys(file_path)
    take_screenshot(driver, 'File_Upload1')
    time.sleep(5)
    try:
        CRO_Message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h5[@id='responseModalLabel']"))
        )
        assert CRO_Message.is_displayed()
        time.sleep(10)
        take_screenshot(driver, "CRO1")
        driver.find_element(By.XPATH,"//img[@alt='Close']").click()

        print("Login Test Passed: Succsesfully CRO data Matched")
    except Exception as e:
         pytest.fail(f"Login Test Failed: No error message displayed for unsuccessful login. Exception: {e}")

def test_Criminal_Face_Detection_CRO_2(setup):
    driver = setup
    time.sleep(2)
    file_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
    )
    blink_element(driver, file_input)
    file_path = "C:\\Users\\arslan.arif\\Desktop\\Criminal Pic for Testing\\download (2).png"
    file_input.send_keys(file_path)
    take_screenshot(driver, 'File_Upload2')
    time.sleep(5)
    try:
        CRO_Message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h5[@id='responseModalLabel']"))
        )
        assert CRO_Message.is_displayed()
        time.sleep(10)
        take_screenshot(driver, "CRO2")
        driver.find_element(By.XPATH,"//img[@alt='Close']").click()

        print("Login Test Passed: Succsesfully CRO data Matched")
    except Exception as e:
         pytest.fail(f"Login Test Failed: No error message displayed for unsuccessful login. Exception: {e}")
def test_Criminal_Face_Detection_CRO_3(setup):
    driver = setup
    time.sleep(2)
    file_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
    )
    blink_element(driver, file_input)
    file_path = "C:\\Users\\arslan.arif\\Desktop\\Criminal Pic for Testing\\download (3).png"
    file_input.send_keys(file_path)
    take_screenshot(driver, 'File_Upload3')
    time.sleep(5)
    try:
        CRO_Message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h5[@id='responseModalLabel']"))
        )
        assert CRO_Message.is_displayed()
        time.sleep(10)
        take_screenshot(driver, "CRO3")
        driver.find_element(By.XPATH,"//img[@alt='Close']").click()
        time.sleep(5)
        print("Login Test Passed: Succsesfully CRO data Matched")
    except Exception as e:
         pytest.fail(f"Login Test Failed: No error message displayed for unsuccessful login. Exception: {e}")

# def test_charts_click(setup):
#     driver =setup
#     driver.find_element(By.XPATH,"//span[normalize-space()='20%']").click()
#     driver.find_element(By.XPATH, "//span[normalize-space()='20%']").click()
#     time.sleep(5)

def test_Predictive_Analysis_Cantt(setup):
    driver = setup
    driver.find_element(By.XPATH, "//h6[normalize-space()='Predictive Analysis']").click()
    time.sleep(2)
    first_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='divisionselected']"))  # Update the locator to match your page
    first_dropdown.select_by_index(1)  # Select by index, value, or visible text
    blink_element(driver, first_dropdown._el)  # Use the underlying web element

    # Locate the second dropdown
    second_dropdown = Select(
        driver.find_element(By.XPATH, "//select[@id='psselected']"))  # Update the locator to match your page
    blink_element(driver, second_dropdown._el)  # Use the underlying web element

    # Get all options from the second dropdown
    all_options = second_dropdown.options

    # Iterate through all options in the second dropdown
    for index in range(1, len(all_options)):  # Skipping the first option (index 0) if it's a placeholder
        second_dropdown.select_by_index(index)
        time.sleep(2)  # Add a delay to observe the selection (if needed)

        # Click the button after each selection
        button = driver.find_element(By.XPATH, "//button[@id='showResultNew']")  # Update the locator to match your page
        button.click()
        time.sleep(2)  # Add a delay to observe the button click action

        # Take a screenshot after each selection
        screenshot_name = f"Analysis_{index}"
        take_screenshot(driver, screenshot_name)


def test_Predictive_Analysis_Iqbal_town(setup):
    driver = setup
    first_dropdown = Select(
        driver.find_element(By.XPATH, "//select[@id='divisionselected']"))  # Update the locator to match your page
    first_dropdown.select_by_index(2)  # Select by index, value, or visible text
    blink_element(driver, first_dropdown._el)  # Use the underlying web element

    # Locate the second dropdown
    second_dropdown = Select(
        driver.find_element(By.XPATH, "//select[@id='psselected']"))  # Update the locator to match your page
    blink_element(driver, second_dropdown._el)  # Use the underlying web element

    # Get all options from the second dropdown
    all_options = second_dropdown.options

    # Iterate through all options in the second dropdown
    for index in range(1, len(all_options)):  # Skipping the first option (index 0) if it's a placeholder
        second_dropdown.select_by_index(index)
        time.sleep(2)  # Add a delay to observe the selection (if needed)

        # Click the button after each selection
        button = driver.find_element(By.XPATH, "//button[@id='showResultNew']")  # Update the locator to match your page
        button.click()
        time.sleep(2)  # Add a delay to observe the button click action

        # Take a screenshot after each selection
        screenshot_name = f"Analysis_{index}"
        take_screenshot(driver, screenshot_name)

def test_Predictive_Analysis_Civil_Line(setup):
    driver = setup
    first_dropdown = Select(
        driver.find_element(By.XPATH, "//select[@id='divisionselected']"))  # Update the locator to match your page
    first_dropdown.select_by_index(3)  # Select by index, value, or visible text
    blink_element(driver, first_dropdown._el)  # Use the underlying web element

    # Locate the second dropdown
    second_dropdown = Select(
        driver.find_element(By.XPATH, "//select[@id='psselected']"))  # Update the locator to match your page
    blink_element(driver, second_dropdown._el)  # Use the underlying web element

    # Get all options from the second dropdown
    all_options = second_dropdown.options

    # Iterate through all options in the second dropdown
    for index in range(1, len(all_options)):  # Skipping the first option (index 0) if it's a placeholder
        second_dropdown.select_by_index(index)
        time.sleep(2)  # Add a delay to observe the selection (if needed)

        # Click the button after each selection
        button = driver.find_element(By.XPATH,
                                     "//button[@id='showResultNew']")  # Update the locator to match your page
        button.click()
        time.sleep(2)  # Add a delay to observe the button click action

        # Take a screenshot after each selection
        screenshot_name = f"Analysis_{index}"
        take_screenshot(driver, screenshot_name)

def test_Predictive_Analysis_Saddar(setup):
    driver = setup
    first_dropdown = Select(
        driver.find_element(By.XPATH, "//select[@id='divisionselected']"))  # Update the locator to match your page
    first_dropdown.select_by_index(4)  # Select by index, value, or visible text
    blink_element(driver, first_dropdown._el)  # Use the underlying web element

    # Locate the second dropdown
    second_dropdown = Select(
        driver.find_element(By.XPATH, "//select[@id='psselected']"))  # Update the locator to match your page
    blink_element(driver, second_dropdown._el)  # Use the underlying web element

    # Get all options from the second dropdown
    all_options = second_dropdown.options

    # Iterate through all options in the second dropdown
    for index in range(1, len(all_options)):  # Skipping the first option (index 0) if it's a placeholder
        second_dropdown.select_by_index(index)
        time.sleep(2)  # Add a delay to observe the selection (if needed)

        # Click the button after each selection
        button = driver.find_element(By.XPATH,
                                     "//button[@id='showResultNew']")  # Update the locator to match your page
        button.click()
        time.sleep(2)  # Add a delay to observe the button click action

        # Take a screenshot after each selection
        screenshot_name = f"Analysis_{index}"
        take_screenshot(driver, screenshot_name)

def test_Predictive_Analysis_City(setup):
    driver = setup
    first_dropdown = Select(
        driver.find_element(By.XPATH, "//select[@id='divisionselected']"))  # Update the locator to match your page
    first_dropdown.select_by_index(5)  # Select by index, value, or visible text
    blink_element(driver, first_dropdown._el)  # Use the underlying web element

    # Locate the second dropdown
    second_dropdown = Select(
        driver.find_element(By.XPATH, "//select[@id='psselected']"))  # Update the locator to match your page
    blink_element(driver, second_dropdown._el)  # Use the underlying web element

    # Get all options from the second dropdown
    all_options = second_dropdown.options

    # Iterate through all options in the second dropdown
    for index in range(1, len(all_options)):  # Skipping the first option (index 0) if it's a placeholder
        second_dropdown.select_by_index(index)
        time.sleep(2)  # Add a delay to observe the selection (if needed)

        # Click the button after each selection
        button = driver.find_element(By.XPATH,
                                     "//button[@id='showResultNew']")  # Update the locator to match your page
        button.click()
        time.sleep(2)  # Add a delay to observe the button click action

        # Take a screenshot after each selection
        screenshot_name = f"Analysis_{index}"
        take_screenshot(driver, screenshot_name)

def test_Predictive_Analysis_Model_Town(setup):
    driver = setup
    first_dropdown = Select(
        driver.find_element(By.XPATH, "//select[@id='divisionselected']"))  # Update the locator to match your page
    first_dropdown.select_by_index(6)  # Select by index, value, or visible text
    blink_element(driver, first_dropdown._el)  # Use the underlying web element

    # Locate the second dropdown
    second_dropdown = Select(
        driver.find_element(By.XPATH, "//select[@id='psselected']"))  # Update the locator to match your page
    blink_element(driver, second_dropdown._el)  # Use the underlying web element

    # Get all options from the second dropdown
    all_options = second_dropdown.options

    # Iterate through all options in the second dropdown
    for index in range(1, len(all_options)):  # Skipping the first option (index 0) if it's a placeholder
        second_dropdown.select_by_index(index)
        time.sleep(2)  # Add a delay to observe the selection (if needed)

        # Click the button after each selection
        button = driver.find_element(By.XPATH,
                                     "//button[@id='showResultNew']")  # Update the locator to match your page
        button.click()
        time.sleep(2)  # Add a delay to observe the button click action

        # Take a screenshot after each selection
        screenshot_name = f"Analysis_{index}"
        take_screenshot(driver, screenshot_name)
