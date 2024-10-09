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
import allure
import os



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
def scroll_down(driver, pixels):
    # Scroll down the page by 500 pixels

    driver.execute_script(f"window.scrollBy(0, {pixels});")


def scroll_Up(driver, pixels):
    # Scroll up the page by 1000 pixels
    driver.execute_script(f"window.scrollBy(0, -{pixels});")

def scroll_Right(driver, pixels):
    # Scroll up the page by 1000 pixels
    driver.execute_script(f"window.scrollBy(0, -{pixels});")

def test_title_verification(setup):
    driver = setup
    driver.get("https://ppms.psca.gop.pk/Identity/Account/Login?ReturnUrl=%2F")
    expected_title = "- Police_Performance_Evaluation"
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
    time.sleep(2)
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

# def test_performance_form(setup):
#     driver = setup
#     time.sleep(2)
#     Performance = driver.find_element(By.XPATH,"//a[normalize-space()='Input Performance']")
#     blink_element(driver, Performance)
#     Performance.click()

# def test_form_filler(setup):
#     driver = setup
#     time.sleep(1)
#     district = Select(driver.find_element(By.XPATH,"//select[@id='district']"))
#     district.select_by_value("1")
#     month_input = driver.find_element(By.ID, "dateFilter")
#
#     # Use JavaScript to set the value directly
#     driver.execute_script("arguments[0].value = '2024-04';", month_input)


def test_dashboard(setup):
    driver=setup
    # driver.find_element(By.XPATH,"//a[normalize-space()='Dashboard']").click()
    # time.sleep(1)
    # month_input = driver.find_element(By.ID, "dateFilter")

    # Use JavaScript to set the value directly
    # driver.execute_script("arguments[0].value = '2024-08';", month_input)
    # time.sleep(1)
    # scroll_down(driver)

    Data_Button = driver.find_element(By.XPATH,"//button[@id='loadDataButton']")
    blink_element(driver, Data_Button)
    Data_Button.click()
    time.sleep(2)
    scroll_down(driver,1000)
    time.sleep(2)
    Fir_button = driver.find_element(By.XPATH,"//th[text()='Prompt Registration of FIR']")
    blink_element(driver, Fir_button)
    Fir_button.click()
    time.sleep(2)
    scroll_down(driver,9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)

#
# def test_crime(setup):
#     driver = setup
#     driver.find_element(By.XPATH,"//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
#     time.sleep(2)
#     scroll_down(driver, 1000)
#     time.sleep(1)
#     Crime_button = driver.find_element(By.XPATH, "//th[@aria-label='Crime Control: activate to sort column ascending']")
#     blink_element(driver, Crime_button)
#     Crime_button.click()
#     time.sleep(2)
#     scroll_down(driver, 9000)
#     time.sleep(2)
#     scroll_Up(driver, 9000)
#     time.sleep(2)
#
#
#
# def test_Investigation(setup):
#     driver=setup
#     driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
#     time.sleep(2)
#     scroll_down(driver, 1000)
#     time.sleep(1)
#     Inv_button = driver.find_element(By.XPATH,"//th[@aria-label='Investigation: activate to sort column ascending']")
#     blink_element(driver, Inv_button)
#     Inv_button.click()
#     time.sleep(2)
#     scroll_down(driver, 9000)
#     time.sleep(2)
#     scroll_Up(driver, 9000)
#     time.sleep(2)
#
# def test_narcotics(setup):
#     driver=setup
#     driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
#     time.sleep(2)
#     scroll_down(driver, 1000)
#     time.sleep(1)
#     narcotics_button=driver.find_element(By.XPATH,"//th[@aria-label='Action Against Narcotics: activate to sort column ascending']")
#     blink_element(driver, narcotics_button)
#     narcotics_button.click()
#     time.sleep(2)
#     scroll_down(driver, 9000)
#     time.sleep(2)
#     scroll_Up(driver, 9000)
#     time.sleep(2)
#
# def test_law_order(setup):
#     driver=setup
#     driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
#     time.sleep(2)
#     scroll_down(driver, 1000)
#     time.sleep(1)
#     law_button=driver.find_element(By.XPATH,"//th[@aria-label='Law &amp; Order Handling: activate to sort column ascending']")
#     blink_element(driver, law_button)
#     law_button.click()
#     time.sleep(2)
#     scroll_down(driver, 9000)
#     time.sleep(2)
#     scroll_Up(driver, 9000)
#     time.sleep(2)
#
#
# def test_W_P(setup):
#     driver=setup
#     driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
#     time.sleep(2)
#     scroll_down(driver, 1000)
#     time.sleep(1)
#     WP_button=driver.find_element(By.XPATH,"//th[@aria-label='Protection of Women and Vulnerable Groups: activate to sort column ascending']")
#     blink_element(driver, WP_button)
#     WP_button.click()
#     time.sleep(2)
#     scroll_down(driver, 9000)
#     time.sleep(2)
#     scroll_Up(driver, 9000)
#     time.sleep(2)
#
# def test_General_Admin(setup):
#     driver=setup
#     driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
#     time.sleep(2)
#     scroll_down(driver, 1000)
#     time.sleep(1)
#     General_Admin=driver.find_element(By.XPATH,"//th[@aria-label='General Administration: activate to sort column ascending']")
#     blink_element(driver, General_Admin)
#     General_Admin.click()
#     time.sleep(2)
#     scroll_down(driver, 9000)
#     time.sleep(2)
#     scroll_Up(driver, 9000)
#     time.sleep(2)
#
# def test_Complaint_Acc(setup):
#     driver=setup
#     driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
#     time.sleep(2)
#     scroll_down(driver, 1000)
#     time.sleep(1)
#     Complaint_Acc=driver.find_element(By.XPATH,"//th[@aria-label='Complaint Handling and Accessibility: activate to sort column ascending']")
#     blink_element(driver, Complaint_Acc)
#     Complaint_Acc.click()
#     time.sleep(2)
#     scroll_down(driver, 9000)
#     time.sleep(2)
#     scroll_Up(driver, 9000)
#     time.sleep(2)
#
# def test_Security(setup):
#     driver=setup
#     driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
#     time.sleep(2)
#     scroll_down(driver, 1000)
#     time.sleep(1)
#     test_Security_Acc=driver.find_element(By.XPATH,"//th[@aria-label='Security: activate to sort column ascending']")
#     blink_element(driver, test_Security_Acc)
#     test_Security_Acc.click()
#     time.sleep(2)
#     scroll_down(driver, 9000)
#     time.sleep(2)
#     scroll_Up(driver, 9000)
#     time.sleep(2)

def test_Public(setup):
    driver = setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 1000)
    time.sleep(1)
    test_Security_Acc = driver.find_element(By.XPATH, "//th[@aria-label='Services to Public: activate to sort column ascending']")
    blink_element(driver, test_Security_Acc)
    test_Security_Acc.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)

def test_Special_Intiative(setup):
    driver = setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 1000)
    time.sleep(1)
    Special_button = driver.find_element(By.XPATH, "//th[@aria-label='Special Initiative: activate to sort column ascending']")
    blink_element(driver, Special_button)
    Special_button.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)

def test_Total_Score(setup):
    driver = setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 4000)
    time.sleep(5)
    scroll_Right(driver,1000)
    time.sleep(2)
    scroll_Up(driver,2200)
    time.sleep(2)
    Total_Score = driver.find_element(By.XPATH, "//th[@aria-label='District Total Score: activate to sort column ascending']")
    blink_element(driver, Total_Score)
    Total_Score.click()
    time.sleep(2)
    scroll_down(driver, 4000)
    time.sleep(2)
    for i in range(0, driver.execute_script("return document.body.scrollWidth;"), 100):
        driver.execute_script(f"window.scrollTo({i}, window.scrollY);")
        time.sleep(2)
    scroll_Up(driver, 4000)
    time.sleep(2)

def test_child_attock(setup):
    driver=setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 1000)
    time.sleep(1)
    attock_link= driver.find_element(By.XPATH,"//a[normalize-space()='Attock']")
    blink_element(driver,attock_link)
    attock_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)


def test_child_Bahawalnagar(setup):
    driver=setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 1000)
    time.sleep(1)
    bahawalnagar_link= driver.find_element(By.XPATH,"//a[normalize-space()='Bahawalnagar']")
    blink_element(driver,bahawalnagar_link)
    bahawalnagar_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)


def test_child_Bahawalpur(setup):
    driver=setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 1000)
    time.sleep(1)
    Bahawalpur_link= driver.find_element(By.XPATH,"//a[normalize-space()='Bahawalpur']")
    blink_element(driver,Bahawalpur_link)
    Bahawalpur_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)

def test_child_Bhakkar(setup):
    driver=setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 1000)
    time.sleep(1)
    Bhakkar_link= driver.find_element(By.XPATH,"//a[normalize-space()='Bhakkar']")
    blink_element(driver,Bhakkar_link)
    Bhakkar_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)



def test_child_Chakwal(setup):
    driver=setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 1000)
    time.sleep(1)
    Chakwal_link= driver.find_element(By.XPATH,"//a[normalize-space()='Chakwal']")
    blink_element(driver,Chakwal_link)
    Chakwal_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)


def test_child_Chiniot(setup):
    driver=setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 1000)
    time.sleep(1)
    Chiniot_link= driver.find_element(By.XPATH,"//a[normalize-space()='Chiniot']")
    blink_element(driver,Chiniot_link)
    Chiniot_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)


def test_child_DGK(setup):
    driver=setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 1200)
    time.sleep(1)
    DGK_link= driver.find_element(By.XPATH,"//a[normalize-space()='Dera Ghazi Khan']")
    blink_element(driver,DGK_link)
    DGK_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)



def test_child_Faisalabad(setup):
    driver=setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 1200)
    time.sleep(1)
    Faisalabad_link= driver.find_element(By.XPATH,"//a[normalize-space()='Faisalabad']")
    blink_element(driver,Faisalabad_link)
    Faisalabad_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)


def test_child_Gujranwala(setup):
    driver=setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 1200)
    time.sleep(1)
    Gujranwala_link= driver.find_element(By.XPATH,"//a[normalize-space()='Gujranwala']")
    blink_element(driver,Gujranwala_link)
    Gujranwala_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)


def test_child_Gujrat(setup):
    driver=setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 1300)
    time.sleep(1)
    Gujrat_link= driver.find_element(By.XPATH,"//a[normalize-space()='Gujrat']")
    blink_element(driver,Gujrat_link)
    Gujrat_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)



def test_child_Hafizabad(setup):
    driver=setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 1300)
    time.sleep(1)
    Hafizabad_link= driver.find_element(By.XPATH,"//a[normalize-space()='Hafizabad']")
    blink_element(driver,Hafizabad_link)
    Hafizabad_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)



def test_child_Jhang(setup):
    driver=setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 1300)
    time.sleep(1)
    Jhang_link= driver.find_element(By.XPATH,"//a[normalize-space()='Jhang']")
    blink_element(driver,Jhang_link)
    Jhang_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)

def test_child_Jhelum(setup):
    driver=setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 1400)
    time.sleep(1)
    Jhelum_link= driver.find_element(By.XPATH,"//a[normalize-space()='Jhelum']")
    blink_element(driver,Jhelum_link)
    Jhelum_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)


def test_child_Kasur(setup):
    driver=setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 1400)
    time.sleep(1)
    Kasur_link= driver.find_element(By.XPATH,"//a[normalize-space()='Kasur']")
    blink_element(driver,Kasur_link)
    Kasur_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)


def test_child_Khanewal(setup):
    driver=setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 1500)
    time.sleep(1)
    Khanewal_link= driver.find_element(By.XPATH,"//a[normalize-space()='Khanewal']")
    blink_element(driver,Khanewal_link)
    Khanewal_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)


def test_child_Khushab(setup):
    driver=setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 1500)
    time.sleep(1)
    Khushab_link= driver.find_element(By.XPATH,"//a[normalize-space()='Khushab']")
    blink_element(driver,Khushab_link)
    Khushab_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)


def test_child_Lahore(setup):
    driver=setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 1500)
    time.sleep(1)
    Lahore_link= driver.find_element(By.XPATH,"//a[normalize-space()='Lahore']")
    blink_element(driver,Lahore_link)
    Lahore_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)


def test_child_Layyah(setup):
    driver=setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 1600)
    time.sleep(1)
    Layyah_link= driver.find_element(By.XPATH,"//a[normalize-space()='Layyah']")
    blink_element(driver,Layyah_link)
    Layyah_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)


def test_child_Lodhran(setup):
    driver=setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 1600)
    time.sleep(1)
    Lodhran_link= driver.find_element(By.XPATH,"//a[normalize-space()='Lodhran']")
    blink_element(driver,Lodhran_link)
    Lodhran_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)



def test_child_MBD(setup):
    driver=setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 1600)
    time.sleep(1)
    MBD_link= driver.find_element(By.XPATH,"//a[normalize-space()='M B Din']")
    blink_element(driver,MBD_link)
    MBD_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)


def test_child_Mianwali(setup):
    driver=setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 1700)
    time.sleep(1)
    Mianwali_link= driver.find_element(By.XPATH,"//a[normalize-space()='Mianwali']")
    blink_element(driver,Mianwali_link)
    Mianwali_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)


def test_child_Multan(setup):
    driver = setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 1700)
    time.sleep(1)
    Multan_link= driver.find_element(By.XPATH,"//a[normalize-space()='Multan']")
    blink_element(driver,Multan_link)
    Multan_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)



def test_child_Muzaffargarh(setup):
    driver = setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 1800)
    time.sleep(1)
    Muzaffargarh_link= driver.find_element(By.XPATH,"//a[normalize-space()='Muzaffargarh']")
    blink_element(driver,Muzaffargarh_link)
    Muzaffargarh_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)


def test_child_Nankana(setup):
    driver=setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 1800)
    time.sleep(1)
    Nankana_link= driver.find_element(By.XPATH,"//a[normalize-space()='Nankana Sahib']")
    blink_element(driver,Nankana_link)
    Nankana_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)


def test_child_Narowal(setup):
    driver=setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 1800)
    time.sleep(1)
    Narowal_link= driver.find_element(By.XPATH,"//a[normalize-space()='Narowal']")
    blink_element(driver,Narowal_link)
    Narowal_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)


def test_child_Okara(setup):
    driver=setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 1900)
    time.sleep(1)
    Okara_link= driver.find_element(By.XPATH,"//a[normalize-space()='Okara']")
    blink_element(driver,Okara_link)
    Okara_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)


def test_child_Pakpattan(setup):
    driver=setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 2000)
    time.sleep(1)
    Pakpattan_link= driver.find_element(By.XPATH,"//a[normalize-space()='Pakpattan']")
    blink_element(driver,Pakpattan_link)
    Pakpattan_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)


def test_child_Rahim_Yar_Khan(setup):
    driver=setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 2000)
    time.sleep(1)
    Rahim_Yar_Khan_link= driver.find_element(By.XPATH,"//a[normalize-space()='Rahim Yar Khan']")
    blink_element(driver,Rahim_Yar_Khan_link)
    Rahim_Yar_Khan_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)


def test_child_Rajanpur(setup):
    driver=setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 2000)
    time.sleep(1)
    Rajanpur_link= driver.find_element(By.XPATH,"//a[normalize-space()='Rajanpur']")
    blink_element(driver,Rajanpur_link)
    Rajanpur_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)


def test_child_Rawalpindi(setup):
    driver=setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 2200)
    time.sleep(1)
    Rawalpindi_link= driver.find_element(By.XPATH,"//a[normalize-space()='Rawalpindi']")
    blink_element(driver,Rawalpindi_link)
    Rawalpindi_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)


def test_child_Sahiwal(setup):
    driver=setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 2200)
    time.sleep(1)
    Sahiwal_link= driver.find_element(By.XPATH,"//a[normalize-space()='Sahiwal']")
    blink_element(driver,Sahiwal_link)
    Sahiwal_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)


def test_child_Sargodha(setup):
    driver=setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 2300)
    time.sleep(1)
    Sargodha_link= driver.find_element(By.XPATH,"//a[normalize-space()='Sargodha']")
    blink_element(driver,Sargodha_link)
    Sargodha_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)


def test_child_Sheikhupura(setup):
    driver=setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 2300)
    time.sleep(1)
    Sheikhupura_link= driver.find_element(By.XPATH,"//a[normalize-space()='Sheikhupura']")
    blink_element(driver,Sheikhupura_link)
    Sheikhupura_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)


def test_child_Sialkot(setup):
    driver=setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 2300)
    time.sleep(1)
    Sialkot_link= driver.find_element(By.XPATH,"//a[normalize-space()='Sialkot']")
    blink_element(driver,Sialkot_link)
    Sialkot_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)


def test_child_Toba_Tek(setup):
    driver=setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 2400)
    time.sleep(1)
    Toba_Tek_link= driver.find_element(By.XPATH,"//a[normalize-space()='Toba Tek Singh']")
    blink_element(driver,Toba_Tek_link)
    Toba_Tek_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)

def test_child_Vehari(setup):
    driver=setup
    driver.find_element(By.XPATH, "//a[normalize-space()='Police Performance Evaluation Dashboard']").click()
    time.sleep(2)
    scroll_down(driver, 2400)
    time.sleep(1)
    Vehari_link= driver.find_element(By.XPATH,"//a[normalize-space()='Vehari']")
    blink_element(driver,Vehari_link)
    Vehari_link.click()
    time.sleep(2)
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(2)



def test_total_performance(setup):
    driver=setup
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[normalize-space()='Performance Status']").click()
    time.sleep(2)
    month_input = driver.find_element(By.ID, "dateFilter")
    driver.execute_script("arguments[0].value = '2024-03';", month_input)
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@id='loadDataButton']").click()
    time.sleep(2)
    alert_button=driver.find_element(By.XPATH,"//button[normalize-space()='OK']")
    blink_element(driver,alert_button)
    alert_button.click()
    time.sleep(2)
    month_input = driver.find_element(By.ID, "dateFilter")
    driver.execute_script("arguments[0].value = '2024-08';", month_input)
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[@id='loadDataButton']").click()
    scroll_down(driver, 9000)
    time.sleep(2)
    scroll_Up(driver, 9000)
    time.sleep(1)