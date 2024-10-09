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

def scroll_down(driver):
    # Scroll down the page by 500 pixels
    driver.execute_script("window.scrollBy(0, 1000);")

def scroll_up(driver):
    # Scroll up the page by 1000 pixels
    driver.execute_script("window.scrollBy(0, -1000);")


def test_Criminal_Face_Detection_CRO(setup):
    driver = setup
    time.sleep(15)
    show_detail=driver.find_element(By.XPATH, "//a[@id='showdetailsmarquee']")
    show_detail.click()
    time.sleep(5)
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
    take_screenshot(driver, 'File_Upload')
    time.sleep(5)
    try:
        CRO_Message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h5[@id='responseModalLabel']"))
        )
        assert CRO_Message.is_displayed()
        time.sleep(10)
        take_screenshot(driver, "CRO")
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
    take_screenshot(driver, 'File_Upload')
    time.sleep(5)
    try:
        CRO_Message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h5[@id='responseModalLabel']"))
        )
        assert CRO_Message.is_displayed()
        time.sleep(10)
        take_screenshot(driver, "CRO")
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
    take_screenshot(driver, 'File_Upload')
    time.sleep(5)
    try:
        CRO_Message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h5[@id='responseModalLabel']"))
        )
        assert CRO_Message.is_displayed()
        time.sleep(10)
        take_screenshot(driver, "CRO")
        driver.find_element(By.XPATH,"//img[@alt='Close']").click()
        time.sleep(5)
        print("Login Test Passed: Succsesfully CRO data Matched")
    except Exception as e:
         pytest.fail(f"Login Test Failed: No error message displayed for unsuccessful login. Exception: {e}")