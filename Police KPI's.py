import time

import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoAlertPresentException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="module")
def setup():
    # Configure Chrome options
    chrome_options = Options()
    # chrome_options.add_argument('--ignore-certificate-errors')
    # chrome_options.add_argument('--ignore-ssl-errors')
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
def scroll_down(driver):
    # Scroll down the page by 500 pixels
    driver.execute_script("window.scrollBy(0, 1000);")

def scroll_up(driver):
    # Scroll up the page by 1000 pixels
    driver.execute_script("window.scrollBy(0, -2000);")

def test_title_verification(setup):
    driver = setup
    driver.get("http://10.20.180.204:1121/Identity/Account/Login")
    expected_title = " - Police_Performance_Evaluation"
    actual_title = driver.title
    assert actual_title == expected_title, f"Test Failed: Title is '{actual_title}' but expected '{expected_title}'"
    take_screenshot(driver, 'title_verification')


def login(driver, username, password):
    username_field = driver.find_element(By.XPATH, "//input[@id='Input_UserName']")
    password_field = driver.find_element(By.XPATH, "//input[@id='Input_Password']")
    login_button = driver.find_element(By.XPATH, "//button[@id='login-submit']")

    # Enter credentials and submit the form
    blink_element(driver, username_field)
    username_field.send_keys(username)
    blink_element(driver, password_field)
    password_field.send_keys(password)
    blink_element(driver, login_button)
    login_button.click()


# def test_login_blank_field(setup):
#     driver = setup
#     time.sleep(1)
#     empty_username = ""
#     empty_password = ""
#     login(driver, empty_username, empty_password)
#
#     try:
#         WebDriverWait(driver, 1).until(EC.alert_is_present())
#         alert = driver.switch_to.alert
#         assert "Please fill out this " in alert.text
#         alert.accept()
#     except TimeoutException:
#         pass
#     take_screenshot(driver, 'login_blank_field')
#     print("Login Test Passed: Unsuccessful login displayed error message")
#
# def test_login_monkey_testing(setup):
#     driver = setup
#     time.sleep(1)
#     empty_username = ".....@#$%^&*"
#     empty_password = "@@@@"
#     login(driver, empty_username, empty_password)
#
#     try:
#         WebDriverWait(driver, 1).until(EC.alert_is_present())
#         alert = driver.switch_to.alert
#         assert "Please fill out this " in alert.text
#         alert.accept()
#     except TimeoutException:
#         pass
#     take_screenshot(driver, 'login_blank_field')
#     print("Login Test Passed: Unsuccessful login displayed error message")
#
# def test_login_dot_field(setup):
#     driver = setup
#     time.sleep(1)
#     username = driver.find_element(By.XPATH, "//input[@id='Input_UserName']")
#     username.clear()
#     username = driver.find_element(By.XPATH, "//input[@id='Input_Password']")
#     username.clear()
#     time.sleep(1)
#     empty_username = ".QA-User."
#     empty_password = ""
#     login(driver, empty_username, empty_password)
#
#     try:
#         WebDriverWait(driver, 1).until(EC.alert_is_present())
#         alert = driver.switch_to.alert
#         assert "Please fill out this " in alert.text
#         alert.accept()
#     except TimeoutException:
#         pass
#     take_screenshot(driver, 'login_blank_field')
#     print("Login Test Passed: Unsuccessful login displayed error message")
#
#
# def test_only_password_empty(setup):
#     driver = setup
#     time.sleep(1)
#     username = driver.find_element(By.XPATH, "//input[@id='Input_UserName']")
#     username.clear()
#     password = driver.find_element(By.XPATH, "//input[@id='Input_UserName']")
#     password.clear()
#     valid_username = "QA_USER"
#     empty_password = ""
#     login(driver, valid_username, empty_password)
#
#     try:
#         WebDriverWait(driver, 3).until(EC.alert_is_present())
#         alert = driver.switch_to.alert
#         assert "Please fill out this field" in alert.text
#         alert.accept()
#     except TimeoutException:
#         pass
#     take_screenshot(driver, 'Empty_Password')
#     print("Login Test Passed: Unsuccessful login displayed error message")

def test_valid_Credential(setup):
    driver = setup
    time.sleep(1)
    username = driver.find_element(By.XPATH, "//input[@id='Input_UserName']")
    username.clear()
    password = driver.find_element(By.XPATH, "//input[@id='Input_Password']")
    password.clear()
    valid_username = "admin"
    valid_password = "Psca@123"
    login(driver, valid_username, valid_password)
    time.sleep(2)
    assert "Sucsessfully logged in"
    take_screenshot(driver, 'Sucsessfully log in')
    print("Login Test Passed: Successful login ")

def test_performance_form(setup):
    driver = setup
    time.sleep(2)
    Performance = driver.find_element(By.XPATH,"//a[normalize-space()='Input Performance']")
    blink_element(driver, Performance)
    Performance.click()

def test_form_filler(setup):
    driver = setup
    time.sleep(1)
    district = Select(driver.find_element(By.XPATH,"//select[@id='district']"))
    district.select_by_value("1")
    month_input = driver.find_element(By.ID, "dateFilter")

    # Use JavaScript to set the value directly
    driver.execute_script("arguments[0].value = '2024-04';", month_input)

def test_form_Filler0(setup):
    driver = setup
    driver.find_element(By.XPATH,"//input[@id='callsToFIR']").send_keys("15")
    driver.find_element(By.XPATH,"//input[@id='adherenceSIPS']").send_keys("20")
    driver.find_element(By.XPATH,"//input[@id='monthlyComparison']").send_keys("15")
    driver.find_element(By.XPATH,"//input[@id='actionGangs']").send_keys("88")
    driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
    driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
    driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
    driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
    driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
    driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
    driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("10")
    driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("11")
    driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("11")
    driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
    driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("11")
    driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
    driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
    driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("11")
    driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
    driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
    driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
    driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
    driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
    driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
    driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
    driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
    driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
    driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
    driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
    driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
    driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
    driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
    driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
    driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
    driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
    driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
    time.sleep(1)
    scroll_down(driver)

    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Submit Data']")))
    blink_element(driver,element)
    # Now try to click it
    element.click()
    scroll_up(driver)
    time.sleep(5)
#
# def test_performance_form1(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH,"//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler2(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH,"//select[@id='district']"))
#     district.select_by_value("2")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler1(setup):
#     driver = setup
#     driver.find_element(By.XPATH,"//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH,"//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH,"//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH,"//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH,"//input[@value='Submit Data']").click()
#     time.sleep(5)
#
# def test_performance_form3(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH,"//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler3(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH,"//select[@id='district']"))
#     district.select_by_value("3")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler3(setup):
#     driver = setup
#     driver.find_element(By.XPATH,"//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH,"//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH,"//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH,"//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH,"//input[@value='Submit Data']").click()
#
# def test_performance_form4(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH,"//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler4(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH,"//select[@id='district']"))
#     district.select_by_value("4")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler4(setup):
#     driver = setup
#     driver.find_element(By.XPATH,"//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH,"//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH,"//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH,"//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH,"//input[@value='Submit Data']").click()
#
#
# def test_performance_form5(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH,"//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler5(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH,"//select[@id='district']"))
#     district.select_by_value("5")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler5(setup):
#     driver = setup
#     driver.find_element(By.XPATH,"//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH,"//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH,"//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH,"//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH,"//input[@value='Submit Data']").click()
#
#
# def test_performance_form6(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH,"//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler6(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH,"//select[@id='district']"))
#     district.select_by_value("6")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler6(setup):
#     driver = setup
#     driver.find_element(By.XPATH,"//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH,"//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH,"//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH,"//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH,"//input[@value='Submit Data']").click()
#
#
# def test_performance_form7(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH,"//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler7(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH,"//select[@id='district']"))
#     district.select_by_value("7")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler7(setup):
#     driver = setup
#     driver.find_element(By.XPATH,"//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH,"//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH,"//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH,"//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH,"//input[@value='Submit Data']").click()
#
#
# def test_performance_form8(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH,"//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler8(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH,"//select[@id='district']"))
#     district.select_by_value("8")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler8(setup):
#     driver = setup
#     driver.find_element(By.XPATH,"//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH,"//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH,"//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH,"//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH,"//input[@value='Submit Data']").click()
#
# def test_performance_form9(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH,"//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler9(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH,"//select[@id='district']"))
#     district.select_by_value("9")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler9(setup):
#     driver = setup
#     driver.find_element(By.XPATH,"//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH,"//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH,"//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH,"//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH,"//input[@value='Submit Data']").click()
#
# def test_performance_form10(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH,"//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler10(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH,"//select[@id='district']"))
#     district.select_by_value("10")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler10(setup):
#     driver = setup
#     driver.find_element(By.XPATH,"//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH,"//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH,"//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH,"//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH,"//input[@value='Submit Data']").click()
#
#
# def test_performance_form11(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH,"//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler11(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH,"//select[@id='district']"))
#     district.select_by_value("11")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler11(setup):
#     driver = setup
#     driver.find_element(By.XPATH,"//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH,"//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH,"//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH,"//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH,"//input[@value='Submit Data']").click()
#
#
#
# def test_performance_form12(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH,"//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler12(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH,"//select[@id='district']"))
#     district.select_by_value("12")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler12(setup):
#     driver = setup
#     driver.find_element(By.XPATH,"//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH,"//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH,"//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH,"//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH,"//input[@value='Submit Data']").click()
#
# def test_performance_form13(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH,"//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler13(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH,"//select[@id='district']"))
#     district.select_by_value("13")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler13(setup):
#     driver = setup
#     driver.find_element(By.XPATH,"//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH,"//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH,"//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH,"//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH,"//input[@value='Submit Data']").click()
# #-------------------------------------------------
# def test_performance_form14(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH, "//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler14(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH, "//select[@id='district']"))
#     district.select_by_value("14")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler14(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH, "//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//input[@value='Submit Data']").click()
#
#         #-------------------------------------------------
# def test_performance_form15(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH, "//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler15(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH, "//select[@id='district']"))
#     district.select_by_value("15")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler15(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH, "//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//input[@value='Submit Data']").click()
#
# #-------------------------------------------
#
# def test_performance_form16(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH, "//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler16(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH, "//select[@id='district']"))
#     district.select_by_value("16")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler16(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH, "//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//input[@value='Submit Data']").click()
#
# #------------------------------------------------------
#
# def test_performance_form17(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH, "//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler17(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH, "//select[@id='district']"))
#     district.select_by_value("17")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler17(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH, "//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//input[@value='Submit Data']").click()
#
# #-----------------------------------------
#
# def test_performance_form18(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH, "//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler18(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH, "//select[@id='district']"))
#     district.select_by_value("18")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler18(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH, "//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//input[@value='Submit Data']").click()
#
# #--------------------------------------------------------------
#
# def test_performance_form19(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH, "//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler19(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH, "//select[@id='district']"))
#     district.select_by_value("19")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler19(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH, "//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//input[@value='Submit Data']").click()
#
# #----------------------------------
#
# def test_performance_form20(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH, "//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler20(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH, "//select[@id='district']"))
#     district.select_by_value("20")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler20(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH, "//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//input[@value='Submit Data']").click()
#
# #---------------------------------------
#
# def test_performance_form21(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH, "//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler21(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH, "//select[@id='district']"))
#     district.select_by_value("21")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler21(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH, "//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//input[@value='Submit Data']").click()
#
# #------------------------------------------
#
# def test_performance_form22(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH, "//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler22(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH, "//select[@id='district']"))
#     district.select_by_value("22")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler22(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH, "//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//input[@value='Submit Data']").click()
#
# #---------------------------------------
#
# def test_performance_form23(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH, "//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler23(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH, "//select[@id='district']"))
#     district.select_by_value("23")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler23(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH, "//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//input[@value='Submit Data']").click()
#
#
# #-------------------------------------------
#
# def test_performance_form24(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH, "//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler24(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH, "//select[@id='district']"))
#     district.select_by_value("24")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler24(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH, "//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//input[@value='Submit Data']").click()
#
# #------------------------------------
#
# def test_performance_form25(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH, "//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler25(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH, "//select[@id='district']"))
#     district.select_by_value("25")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler25(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH, "//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//input[@value='Submit Data']").click()
#
# #-----------------------------------------
#
# def test_performance_form26(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH, "//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler26(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH, "//select[@id='district']"))
#     district.select_by_value("26")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler26(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH, "//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//input[@value='Submit Data']").click()
#
# #----------------------------------------
#
# def test_performance_form27(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH, "//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler27(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH, "//select[@id='district']"))
#     district.select_by_value("27")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler27(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH, "//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//input[@value='Submit Data']").click()
#
#
# #----------------------------------------
#
# def test_performance_form28(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH, "//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler28(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH, "//select[@id='district']"))
#     district.select_by_value("28")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler28(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH, "//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//input[@value='Submit Data']").click()
#
# #------------------------------------------
#
# def test_performance_form29(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH, "//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler29(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH, "//select[@id='district']"))
#     district.select_by_value("29")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler29(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH, "//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//input[@value='Submit Data']").click()
#
#
# #----------------------------------
#
# def test_performance_form30(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH, "//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler30(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH, "//select[@id='district']"))
#     district.select_by_value("30")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler30(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH, "//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//input[@value='Submit Data']").click()
#
# #-------------------------------------------------
#
# def test_performance_form31(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH, "//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler31(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH, "//select[@id='district']"))
#     district.select_by_value("31")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler31(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH, "//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//input[@value='Submit Data']").click()
#
#
# #-------------------------------------
#
# def test_performance_form32(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH, "//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler32(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH, "//select[@id='district']"))
#     district.select_by_value("32")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler32(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH, "//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//input[@value='Submit Data']").click()
#
#
# #--------------------------------------
#
# def test_performance_form33(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH, "//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler33(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH, "//select[@id='district']"))
#     district.select_by_value("33")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler33(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH, "//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//input[@value='Submit Data']").click()
#
# #----------------------------------------
#
# def test_performance_form34(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH, "//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler34(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH, "//select[@id='district']"))
#     district.select_by_value("34")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler34(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH, "//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//input[@value='Submit Data']").click()
#
# #-------------------------------------------
#
# def test_performance_form35(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH, "//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler35(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH, "//select[@id='district']"))
#     district.select_by_value("35")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler35(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH, "//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//input[@value='Submit Data']").click()
#
# #---------------------------------
#
# def test_performance_form36(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH, "//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()
#
# def test_form_filler36(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH, "//select[@id='district']"))
#     district.select_by_value("36")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
# def test_form_Filler36(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//input[@id='callsToFIR']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='adherenceSIPS']").send_keys("20")
#     driver.find_element(By.XPATH, "//input[@id='monthlyComparison']").send_keys("15")
#     driver.find_element(By.XPATH, "//input[@id='actionGangs']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='actionCrimePockets']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='actionNoGoAreas']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='searchOperations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='extraordinaryWork']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='kiteStringDeath']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='aerialFiringDeath']").send_keys("34")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeChallan']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='heinousCrimeConviction']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='arrestCategoryAPOs']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='gazettedOfficersVisit']").send_keys("56")
#     driver.find_element(By.XPATH, "//input[@id='arrestNarcoticsDealers']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='narcoticsConviction']").send_keys("91")
#     driver.find_element(By.XPATH, "//input[@id='extraordinarySeizures']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryLOSituations']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='specialExtraordinaryEvents']").send_keys("17")
#     driver.find_element(By.XPATH, "//input[@id='complaintsVWPS']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseArrest']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='rapeSodomyChildAbuseChallan']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='resolutionCMSComplaints']").send_keys("98")
#     driver.find_element(By.XPATH, "//input[@id='casesTahaffuzMeesaq']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='provisionResourcesFuelInvestigation']").send_keys("100")
#     driver.find_element(By.XPATH, "//input[@id='postingsSHOsMoharar']").send_keys("88")
#     driver.find_element(By.XPATH, "//input[@id='disciplinaryActionDecisions']").send_keys("25")
#     driver.find_element(By.XPATH, "//input[@id='inspectionsPoliceStations']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='khuliKacherisHeld']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='complaintsInvestigationResolution']").send_keys("33")
#     driver.find_element(By.XPATH, "//input[@id='complaintsCorruptionResolution']").send_keys("48")
#     driver.find_element(By.XPATH, "//input[@id='securityExtraordinaryEvents']").send_keys("78")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackPKM']").send_keys("89")
#     driver.find_element(By.XPATH, "//input[@id='citizensFeedbackLicensing']").send_keys("11")
#     driver.find_element(By.XPATH, "//input[@id='exceptionalTrafficBlockage']").send_keys("36")
#     driver.find_element(By.XPATH, "//input[@id='innovativeInitiatives']").send_keys("35")
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//input[@value='Submit Data']").click()
#
# def test_Monthly_performance_status(setup):
#     driver = setup
#     time.sleep(1)
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-03';", month_input)
#
#     # Optionally, trigger a change event
#     driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", month_input)
#
#     time.sleep(15)

def test_dashboard(setup):
    driver=setup
    driver.find_element(By.XPATH,"//a[normalize-space()='Dashboard']").click()
    # district = Select(driver.find_element(By.XPATH, "//select[@id='district']"))
    # district.select_by_value("1")
    month_input = driver.find_element(By.ID, "dateFilter")

    # Use JavaScript to set the value directly
    driver.execute_script("arguments[0].value = '2024-08';", month_input)
    driver.find_element(By.XPATH,"//button[@id='loadDataButton']").click()
    driver.find_element(By.XPATH,"//th[@aria-label='Prompt Registration of FIR: activate to sort column ascending']").click()
    scroll_down(driver)
    scroll_up(driver)