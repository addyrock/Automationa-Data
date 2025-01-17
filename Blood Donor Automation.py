import time
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoAlertPresentException, NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import os
import subprocess

def run_allure_report():
    # Run Allure serve to generate and display the report
    allure_results_dir = "allure-results"
    if not os.path.exists(allure_results_dir):
        os.makedirs(allure_results_dir)

    # Run pytest with Allure
    subprocess.run(["pytest", "--alluredir", allure_results_dir], check=True)

    # Generate and serve the Allure report
    subprocess.run(["allure", "serve", allure_results_dir], check=True)

#-------------------------------------------Test Execution Setup-------------------------------------------
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
#-------------------------------------------Take Screenshot------------------------------------------------

def take_screenshot(driver, step_name):
    driver.save_screenshot(f"{step_name}.png")

# ------------------------------------------ Blink Element -------------------------------------------------

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

# ------------------------------------------ Title Verification --------------------------------------------

def test_title_verification(setup):
    driver = setup
    driver.get("https://blooddonors.psca.gop.pk/login")
    expected_title = "Blood Donor (PSCA)"
    actual_title = driver.title
    assert actual_title == expected_title, f"Test Failed: Title is '{actual_title}' but expected '{expected_title}'"
    print( "Actual Title is '{Blood Donor (PSCA)}' but expected '{Blood Donor (PSCA)'")
    take_screenshot(driver, 'title_verification')


def login(driver, username, password):
    username_field = driver.find_element(By.XPATH, "//input[@id='username']")
    password_field = driver.find_element(By.XPATH, "//input[@id='password']")
    login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Sign Me In']")


    # Enter credentials and submit the form
    blink_element(driver, username_field)
    username_field.send_keys(username)
    blink_element(driver, password_field)
    password_field.send_keys(password)
    blink_element(driver, login_button)
    login_button.click()

# ------------------------------------------ Login Page -----------------------------------------------------

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
    username = driver.find_element(By.XPATH, "//input[@id='username']")
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
    username = driver.find_element(By.XPATH, "//input[@id='username']")
    username.clear()
    username = driver.find_element(By.XPATH, "//input[@id='password']")
    username.clear()
    valid_username = "qa.psca.gop.pk"
    valid_password = "psca@123"
    login(driver, valid_username, valid_password)
    time.sleep(2)
    assert "Sucsessfully logged in"
    take_screenshot(driver, 'Sucsessfully log in')

# -------------------------------------Scroll Bar--------------------------------------------------

def scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)


# ---------------------------------Nevigate To Website --------------------------------------------

def test_donor_register(setup):
    driver=setup
    time.sleep(2)
    link_to_donor_register = driver.find_element(By.XPATH, "//a[@href='https://blooddonors.psca.gop.pk/donars']")
    blink_element(driver, link_to_donor_register)
    link_to_donor_register.click()
    time.sleep(3)
    tar_new_donor =driver.find_element(By.XPATH,"//button[normalize-space()='Add']")
    blink_element(driver,tar_new_donor)
    tar_new_donor.click()
    time.sleep(2)
    assert "Successfully click on new donor"
    take_screenshot(driver,"Click Screenshot")

# -----------------------------------New Donor Registration ---------------------------------------

def test_new_donor_registration(setup):
    driver = setup
    time.sleep(2)
    donor_name = driver.find_element(By.XPATH,"//input[@placeholder='Enter Donar Name...']")
    blink_element(driver,donor_name)
    donor_name.send_keys("Test Automation SQA")

    Contact_Num = driver.find_element(By.XPATH, "//input[@placeholder='03451234567...']")
    blink_element(driver, Contact_Num)
    Contact_Num.send_keys("03000000000")

    Cnic_Num = driver.find_element(By.XPATH, "//input[@placeholder='3520169542386']")
    blink_element(driver, Cnic_Num)
    Cnic_Num.send_keys("3520234761115")
    time.sleep(2)
    Dist_drop = Select(driver.find_element(By.XPATH, "//select[@id='district_id']"))
    blink_element(driver,Dist_drop._el)
    Dist_drop.select_by_visible_text("Lahore")
    time.sleep(2)
    POL_drop = Select(driver.find_element(By.XPATH, "//select[@id='police_station_id']"))
    blink_element(driver,POL_drop._el)
    POL_drop.select_by_visible_text("Millat Park")
    time.sleep(2)
    Donor_Add = driver.find_element(By.XPATH, "//textarea[@id='validationCustom04']")
    blink_element(driver, Donor_Add)
    Donor_Add.send_keys("House No 1 , Test Ichra Lahore")

    Fath_Add = driver.find_element(By.XPATH, "//input[@placeholder='Enter Father Name']")
    blink_element(driver, Fath_Add)
    Fath_Add.send_keys("Blood Donor")
    time.sleep(1)
    blood_group= Select(driver.find_element(By.XPATH,"//select[@name='blood_group']"))
    blink_element(driver, blood_group._el)
    blood_group.select_by_visible_text("AB+")
    time.sleep(1)
    dob_Add = driver.find_element(By.XPATH, "//input[@placeholder='Date of Birth']")
    blink_element(driver, dob_Add)
    dob_Add.send_keys("17/05/1993")
    time.sleep(1)
    diese_opt = Select(driver.find_element(By.XPATH, "//select[@name='disease']"))
    blink_element(driver, diese_opt._el)
    diese_opt.select_by_visible_text("No")
    time.sleep(1)
    last_don = driver.find_element(By.XPATH, "//input[@placeholder='Date last blood donation']")
    blink_element(driver, last_don)
    last_don.send_keys("12/11/2024")
    time.sleep(1)
    sour_opt = Select(driver.find_element(By.XPATH, "//select[@id='department']"))
    blink_element(driver, sour_opt._el)
    sour_opt.select_by_visible_text("Police")
    time.sleep(1)
    submit_opt = driver.find_element(By.XPATH, "//button[normalize-space()='Submit']")
    blink_element(driver, submit_opt)
    submit_opt.click()
    time.sleep(2)

def test_donation_req(setup):
    driver = setup
    don_req = driver.find_element(By.XPATH,"//button[normalize-space()='Donation Request']")
    blink_element(driver,don_req)
    don_req.click()
    time.sleep(2)
    ent_num = driver.find_element(By.XPATH,"//input[@id='request_phone_number']")
    blink_element(driver,ent_num)
    ent_num.send_keys("03000000002")
    pro_button = driver.find_element(By.XPATH,"//button[normalize-space()='Proceed']")
    blink_element(driver,pro_button)
    pro_button.click()


def test_case_info(setup):
    driver = setup
    donor_name = driver.find_element(By.XPATH, "//input[@id='contact_person_name']")
    blink_element(driver, donor_name)
    donor_name.send_keys("Test Automation")
    time.sleep(2)
    Contact_Num = driver.find_element(By.XPATH, "//input[@id='contact_person_phone']")
    blink_element(driver, Contact_Num)
    Contact_Num.send_keys("03000000002")
    time.sleep(2)
    pat_Name = driver.find_element(By.XPATH, "//input[@id='patient_name']")
    blink_element(driver, pat_Name)
    pat_Name.send_keys("Test Case")
    time.sleep(2)
    Pat_gen = Select(driver.find_element(By.XPATH, "//select[@id='patient_gender']"))
    blink_element(driver, Pat_gen._el)
    Pat_gen.select_by_visible_text("Male")
    time.sleep(2)
    Pat_drop = driver.find_element(By.XPATH, "//input[@id='patient_age']")
    blink_element(driver, Pat_drop)
    Pat_drop.send_keys("30")
    time.sleep(2)
    blod_Add = Select(driver.find_element(By.XPATH, "//select[@id='required_blood_group']"))
    blink_element(driver, blod_Add._el)
    blod_Add.select_by_visible_text("AB+")
    time.sleep(2)
    bot_Add = driver.find_element(By.XPATH, "//input[@id='bottle_quantity']")
    blink_element(driver, bot_Add)
    bot_Add.send_keys("1")
    time.sleep(1)
    dist_nam = Select(driver.find_element(By.XPATH, "//select[@id='district_id']"))
    blink_element(driver, dist_nam._el)
    dist_nam.select_by_visible_text("Lahore")
    time.sleep(2)
    pol_Add = Select(driver.find_element(By.XPATH, "//select[@id='police_station_id']"))
    blink_element(driver, pol_Add._el)
    pol_Add.select_by_visible_text("Millat Park")
    time.sleep(2)
    hop_add = driver.find_element(By.XPATH, "//textarea[@id='hospital_address']")
    blink_element(driver,hop_add)
    hop_add.send_keys("Shadman Lahore")
    time.sleep(2)
    req_donate = driver.find_element(By.XPATH, "//input[@id='blood_required_date_time']")
    req_donate.clear()
    req_donate.send_keys("15-03-2025")
    # Optionally, simulate pressing 'Enter' if required
    req_donate.send_keys(Keys.RETURN)
    time.sleep(3)

    # Assuming the time input is separate and needs to be handled after the date is selected
    # Find the time input field and enter the time (6:06 AM)
    req_donate1 = driver.find_element(By.XPATH, "//input[@id='blood_required_date_time']")
    # req_donate1.clear()
    req_donate1.send_keys("6:06 AM")
    # Optionally, simulate pressing 'Enter' if required
    req_donate1.send_keys(Keys.RETURN)

    time.sleep(3)

    blood_opt = Select(driver.find_element(By.XPATH, "//select[@id='purpose_of_blood']"))
    blink_element(driver,blood_opt._el)
    blood_opt.select_by_visible_text("Other")
    time.sleep(2)


def test_search_assign(setup):
    driver=setup
    ser_box = driver.find_element(By.XPATH, "//input[@type='search']")
    scroll_to_element(driver, ser_box)  # Scroll to the search box
    blink_element(driver, ser_box)  # Highlight the element
    ser_box.send_keys("Test Automation")
    time.sleep(2)

    # Locate the 'Assign Donor' link and scroll to it
    sel_per = driver.find_element(By.XPATH, "//a[@title='Assign Donor']")
    scroll_to_element(driver, sel_per)  # Scroll to the 'Assign Donor' link
    blink_element(driver, sel_per)  # Highlight the element
    sel_per.click()
    time.sleep(5)

    # Locate the submit button and scroll to it
    sub_button = driver.find_element(By.XPATH, "//button[normalize-space()='Submit']")
    scroll_to_element(driver, sub_button)  # Scroll to the submit button
    blink_element(driver, sub_button)  # Highlight the element
    sub_button.click()
    time.sleep(5)


def test_case_inf0(setup):
    driver = setup
    time.sleep(2)
    case_cli= driver.find_element(By.XPATH,"//span[normalize-space()='Cases']")
    blink_element(driver,case_cli)
    case_cli.click()
    time.sleep(2)

def test_box_search(setup):
    driver = setup
    serch_box = driver.find_element(By.XPATH,"//input[@type='search']")
    blink_element(driver,serch_box)
    serch_box.send_keys("Test Automation")
    time.sleep(2)
    drag_button = driver.find_element(By.XPATH,"//td[@class='sorting_1 dtr-control'][normalize-space()='1']")
    blink_element(driver,drag_button)
    drag_button.click()
    time.sleep(2)
    view_button = driver.find_element(By.XPATH,"//span[@class='dtr-data']//a[@title='view case']")
    blink_element(driver,view_button)
    view_button.click()
    time.sleep(5)

def test_add_follow_up(setup):
    driver = setup
    time.sleep(2)
    # Scroll to the element


    add_folo = driver.find_element(By.XPATH,"//button[normalize-space()='Add Followup']")
    scroll_to_element(driver,add_folo)
    blink_element(driver,add_folo)
    add_folo.click()
    time.sleep(2)
    sel_drop = Select(driver.find_element(By.XPATH,"//select[@id='status_id']"))
    blink_element(driver, sel_drop._el)
    sel_drop.select_by_visible_text("Pending")

    rem_com = driver.find_element(By.XPATH,"//textarea[@id='remarks']")
    blink_element(driver,rem_com)
    rem_com.send_keys("This is a test remark.")
    time.sleep(2)
    but_cl= driver.find_element(By.XPATH,"//form[@id='AddFollowupForm']//button[@type='submit'][normalize-space()='Save']")
    blink_element(driver, but_cl)
    but_cl.click()
    time.sleep(10)

if __name__ == "__main__":
    run_allure_report()



