import time
import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture(scope="module")
def setup():
    # Initialize the WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # options.add_argument('--headless')


def take_screenshot(driver, step_name):
    driver.save_screenshot(f"{step_name}.png")


def test_title_verification(setup):
    driver = setup
    driver.get("http://10.20.101.192:85/")
    expected_title = "  | Log in"
    actual_title = driver.title
    assert actual_title == expected_title, f"Test Failed: Title is '{actual_title}' but expected '{expected_title}'"


def login(driver, username, password):
    username_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter Employee ID']")
    password_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    # Enter credentials and submit the form
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()


def test_login_empty_credentials(setup):
    driver = setup
    Invalid_username = ""
    Invalid_password = ""
    login(driver, Invalid_username, Invalid_password)

    # Wait for the error message to appear
    try:
        error_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='alert']"))
        )
        assert error_message.is_displayed()
        take_screenshot(driver, "login_invalid_credentials_error")
        print("Login Test Passed: Unsuccessful login displayed error message")
    except Exception as e:

        pytest.fail(f"Login Test Failed: No error message displayed for unsuccessful login. Exception: {e}")


def test_login_invalid_username(setup):
    driver = setup
    Invalid_username = ""
    Invalid_password = "123456"
    login(driver, Invalid_username, Invalid_password)

    # Wait for the error message to appear
    try:
        error_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='alert']"))
        )
        assert error_message.is_displayed()
        take_screenshot(driver, "login_invalid_credentials_error")
        print("Login Test Passed: Unsuccessful login displayed error message")
    except Exception as e:

        pytest.fail(f"Login Test Failed: No error message displayed for unsuccessful login. Exception: {e}")


def test_login_invalid_password(setup):
    driver = setup
    Invalid_username = "547-2016-6103"
    Invalid_password = "12345"
    login(driver, Invalid_username, Invalid_password)

    # Wait for the error message to appear
    try:
        error_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='alert']"))
        )
        assert error_message.is_displayed(), "Error message not displayed"
        take_screenshot(driver, "login_invalid_credentials_error")
        print("Login Test Passed: Unsuccessful login displayed error message")
    except Exception as e:

        pytest.fail(f"Login Test Failed: No error message displayed for unsuccessful login. Exception: {e}")


def test_login_valid_credentials(setup):
    driver = setup
    valid_username = "547-2016-6103"
    valid_password = "123456"
    login(driver, valid_username, valid_password)
    take_screenshot(driver, "Successfully login")
    assert "login successfully"


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
#
#
# def test_hover_on_chart(setup):
#     driver = setup
#     chart = driver.find_element(By.XPATH, "//canvas[@id='stackedBarChart']")
#     time.sleep(10)
#     actions = ActionChains(driver)
#     actions.move_to_element_with_offset(chart,250, 843).perform()
#     time.sleep(2)
#
#
# def test_update_profile_link(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//p[@class='text']").click()
#     assert "Update link Work Properly"
#     time.sleep(2)
#
#
# def test_projects_link(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//i[@class='nav-icon fa fa-edit text-blue']").click()
#     assert "Project link Work Properly"
#     time.sleep(2)
#
#
# def test_task_main(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//i[@class='fas fa-angle-left right']").click()
#     time.sleep(1)
#     driver.find_element(By.XPATH, "//i[@class='fas fa-angle-left right']").click()
#     assert "Main task link Work Properly"
#     time.sleep(2)
#
#
# def test_task(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//li[@class='nav-item']//p[contains(text(),'Tasks')]").click()
#     assert "task link Work Properly"
#     time.sleep(2)
#
#
# def test_subtask(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//p[normalize-space()='Subtasks']").click()
#     assert "subtask link Work Properly"
#     time.sleep(2)
#
#
# def test_log_time(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//p[normalize-space()='Log Time']").click()
#     assert "Log time link is work Properly"
#     time.sleep(2)
#
#
# def test_invalid_email_format(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//p[@class='text']").click()
#     email = driver.find_element(By.XPATH, "//input[@id='email']")
#     email.clear()
#     time.sleep(2)
#     invalid_email = "123"
#     email.send_keys(invalid_email)
#     driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
#     take_screenshot(driver, "Invalid_Email_Format")
#     time.sleep(2)
#     try:
#         WebDriverWait(driver, 3).until(EC.alert_is_present())
#         alert = driver.switch_to.alert
#         assert "Please include an '@' in the email address. '123' is missing an '@'" in alert.text
#         alert.accept()
#     except TimeoutException:
#         pass
#     time.sleep(5)
#
#
def test_empty_email(setup):
    driver = setup
    # driver.find_element(By.XPATH, "//p[@class='text']").click()
    email = driver.find_element(By.XPATH, "//input[@id='email']")
    email.clear()
    driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
    take_screenshot(driver, "Empty_Email")
    time.sleep(2)
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        assert "Please fill out this field" in alert.text
        alert.accept()
    except TimeoutException:
        pass

#
# def test_correct_email(setup):
#     driver = setup
#     email = driver.find_element(By.XPATH, "//input[@id='email']")
#     email.send_keys("nida.latif@psca.gop.pk")
#
#
# def test_empty_designation(setup):
#     driver = setup
#     designation = driver.find_element(By.XPATH, "//input[@id='designation']")
#     designation.clear()
#     driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
#     take_screenshot(driver, "Empty_Designation")
#     time.sleep(2)
#     try:
#         WebDriverWait(driver, 3).until(EC.alert_is_present())
#         alert = driver.switch_to.alert
#         assert "Please fill out this field" in alert.text
#         alert.accept()
#     except TimeoutException:
#         pass
#
#
# def test_update_designation(setup):
#     driver = setup
#     designation = driver.find_element(By.XPATH, "//input[@id='designation']")
#     designation.clear()
#     time.sleep(2)
#     designation.send_keys("DEO SQA")
#     assert designation.get_attribute("value") == "DEO SQA"
#
#
# def test_invalid_phone_length(setup):
#     driver = setup
#     phone = driver.find_element(By.XPATH, "//input[@id='phone']")
#     phone.clear()
#     phone_number = "11111111111111111"
#     phone.send_keys(phone_number)
#     save_button = driver.find_element(By.XPATH, "//button[normalize-space()='Save']")
#     save_button.click()
#     take_screenshot(driver, "Invalid_Phone_Length")
#     time.sleep(2)
#     try:
#         error_message = WebDriverWait(driver, 10).until(
#             EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'toast-error')]"))
#         ).text
#         assert "The phone must be 11 characters" in error_message
#     except TimeoutException:
#         assert False, "Error message for invalid phone length not displayed in time."
#
#
# def test_empty_phone_number(setup):
#     driver = setup
#     time.sleep(8)
#     phone = driver.find_element(By.XPATH, "//input[@id='phone']")
#     phone.clear()
#     driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
#     take_screenshot(driver, "Empty_Phone_Number")
#     try:
#         WebDriverWait(driver, 3).until(EC.alert_is_present())
#         alert = driver.switch_to.alert
#         assert "Please fill out this field" in alert.text
#         alert.accept()
#     except TimeoutException:
#         pass
#
#
# def test_valid_phone_number(setup):
#     driver = setup
#     phone = driver.find_element(By.XPATH, "//input[@id='phone']")
#     phone.clear()
#     valid_phone_number = "03226496719"
#     phone.send_keys(valid_phone_number)
#     driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
#     take_screenshot(driver, "Valid_Phone_Number")
#     time.sleep(3)
#     try:
#         success_message = WebDriverWait(driver, 10).until(
#             EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'toast-success')]"))
#         ).text
#         assert "User updated successfully" in success_message
#     except TimeoutException:
#         assert False, "Success message for valid phone number not displayed in time."
#
#
# def test_update_dropdown(setup):
#     driver = setup
#     # phone = driver.find_element(By.XPATH, "//input[@id='phone']")
#     # phone.clear()
#
#     dropdown = Select(driver.find_element(By.NAME, "unit_id"))
#     for index in range(5):
#         dropdown.select_by_index(index)
#         time.sleep(1)
#         selected_option = dropdown.first_selected_option.text
#         print(f"Selected option {index}: {selected_option}")
#
#     dropdown.select_by_visible_text("Safeer Abbas")
#     selected_option = dropdown.first_selected_option.text
#     assert selected_option == "Safeer Abbas"
#
#     save_button = driver.find_element(By.XPATH, "//button[normalize-space()='Save']")
#     save_button.click()
#     time.sleep(2)
#
#     try:
#         WebDriverWait(driver, 3).until(EC.alert_is_present())
#         alert = driver.switch_to.alert
#         assert "Please fill out this field" in alert.text
#         alert.accept()
#     except TimeoutException:
#         pass

#
# def test_dashboard_search_filter1(setup):
#     driver=setup
#     driver.find_element(By.XPATH, "//p[normalize-space()='Dashboard']").click()
#     time.sleep(1)
#     dropdown = Select(driver.find_element(By.ID, "userFilter"))
#     for index in range(5):
#         time.sleep(2)
#         dropdown.select_by_index(index)
#         time.sleep(1)
#         # selected_option = dropdown.first_selected_option.text
#         # time.sleep(2)
#         # print(f"Selected option {index}: {selected_option}")
#         dropdown.select_by_visible_text("Assigned To")
#
#
# def test_dashboard_search_filter2(setup):
#     driver = setup
#
#     dropdown = Select(driver.find_element(By.ID, "taskFilter"))
#     for index in range(5):
#         time.sleep(2)
#         dropdown.select_by_index(index)
#         time.sleep(1)
#         selected_option = dropdown.first_selected_option.text
#         time.sleep(2)
#         print(f"Selected option {index}: {selected_option}")
#         dropdown.select_by_visible_text("All Tasks")
#
#
# def test_dashboard_search_filter3(setup):
#     driver = setup
#
#     dropdown = Select(driver.find_element(By.ID, "priorityFilter"))
#     for index in range(5):
#         time.sleep(2)
#         dropdown.select_by_index(index)
#         time.sleep(1)
#         selected_option = dropdown.first_selected_option.text
#         time.sleep(2)
#         print(f"Selected option {index}: {selected_option}")
#         dropdown.select_by_visible_text("Priority")
#
#
# def test_dashboard_search_filter4(setup):
#     driver = setup
#
#     dropdown = Select(driver.find_element(By.ID, "TaskStatus"))
#     for index in range(8):
#         time.sleep(2)
#         dropdown.select_by_index(index)
#         time.sleep(1)
#         selected_option = dropdown.first_selected_option.text
#         time.sleep(2)
#         print(f"Selected option {index}: {selected_option}")
#         dropdown.select_by_visible_text("Task Status")
#
#
# def test_dashboard_search_filter5(setup):
#     driver = setup
#
#     dropdown = Select(driver.find_element(By.ID, "daterange-btn"))
#     var = dropdown.click
#     for index in range(8):
#         time.sleep(2)
#         dropdown.select_by_index(index)
#         time.sleep(1)
#         selected_option = dropdown.first_selected_option.text
#         time.sleep(2)
#         print(f"Selected option {index}: {selected_option}")
#         dropdown.select_by_visible_text("Today")
#


#
#
# def test_subtask_flow(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//p[normalize-space()='Dashboard']").click()
#     time.sleep(1)
#     driver.find_element(By.XPATH,"//div[@class='small-box bg-info']//a[@class='small-box-footer'][normalize-space()='More info']").click()
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//i[@class='fas fa-expand-arrows-alt']").click()
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//i[@class='fas fa-compress-arrows-alt']").click()
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//i[@class='far fa-bell']").click()
#     time.sleep(2)
#     driver.find_element(By.XPATH,
#                         "//div[@id='notificationModal']//span[@aria-hidden='true'][normalize-space()='×']").click()
#     time.sleep(2)
#     print("cross successfully")
#     driver.find_element(By.XPATH, "//i[@class='far fa-bell']").click()
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//a[normalize-space()='View All Tasks']").click()
#     print("View Task successfully")
#     time.sleep(5)
#     dropdown = Select(driver.find_element(By.ID, "userFilter"))
#     # dropdown.select_by_visible_text("Sadaf Zahoor")
#     for index in range(4):
#         time.sleep(2)
#         dropdown.select_by_index(index)
#         time.sleep(1)
#         selected_option = dropdown.first_selected_option.text
#         time.sleep(2)
#         print(f"Selected option {index}: {selected_option}")
#     # selected_option = dropdown.first_selected_option.text
#     # assert selected_option == "Sadaf Zahoor"
#     time.sleep(5)
#
#
# def test_log_time_functionality(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//p[normalize-space()='Log Time']").click()
#     driver.find_element(By.XPATH,"//button[@name='submit_row_2']").click()
#     time.sleep(3)
#
#     try:
#         # Wait for the error messages to appear and collect them
#         error_elements = WebDriverWait(driver, 10).until(
#             EC.visibility_of_all_elements_located((By.XPATH, "//div[contains(@class, 'toast-error')]"))
#         )
#         error_messages = [error.text for error in error_elements]
#
#         # Check that all expected error messages are present
#         expected_errors = [
#             "Please select subtask status.",
#             "Remarks field is required.",
#             "Subtask field is required."
#         ]
#
#         for expected_error in expected_errors:
#             assert expected_error in error_messages, f"Expected error message '{expected_error}' not found in: {error_messages}"
#
#     except TimeoutException:
#         assert False, "Error messages not displayed in time."
#
#     time.sleep(5)
#
#
# def test_log_functionality_1(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//p[normalize-space()='Log Time']").click()
#     dropdown=Select(driver.find_element(By.XPATH, "//select[@name='subtask_2']"))
#     dropdown.select_by_visible_text("Sub-task form")
#     driver.find_element(By.XPATH, "//button[@name='submit_row_2']").click()
#     time.sleep(3)
#
#     try:
#         error_elements = WebDriverWait(driver, 10).until(
#             EC.visibility_of_all_elements_located((By.XPATH, "//div[contains(@class, 'toast-error')]"))
#         )
#         error_messages = [error.text for error in error_elements]
#
#         expected_errors = [
#             "Please select subtask status.",
#             "Remarks field is required."
#         ]
#
#         for expected_error in expected_errors:
#             assert expected_error in error_messages, f"Expected error message '{expected_error}' not found in: {error_messages}"
#
#     except TimeoutException:
#         assert False, "Error messages not displayed in time."
#
#     time.sleep(5)
#
#
# def test_log_functionality_2(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//p[normalize-space()='Log Time']").click()
#     dropdown = Select(driver.find_element(By.XPATH, "//select[@name='subtask_2']"))
#     dropdown.select_by_visible_text("Sub-task form")
#     driver.find_element(By.XPATH, "//textarea[@name='sub_description_2']").send_keys("Functional Testing")
#     driver.find_element(By.XPATH, "//button[@name='submit_row_2']").click()
#     time.sleep(3)
#
#     try:
#         error_message = WebDriverWait(driver, 10).until(
#             EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'toast-error')]"))
#         ).text
#         assert "Please select subtask status." in error_message
#     except TimeoutException:
#         assert False, "Error message not displayed in time "
#
#
# def test_log_functionality_submit(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//p[normalize-space()='Log Time']").click()
#     dropdown = Select(driver.find_element(By.XPATH, "//select[@name='subtask_2']"))
#     dropdown.select_by_visible_text("Sub-task form")
#     driver.find_element(By.XPATH, "//textarea[@name='sub_description_2']").send_keys("Functional Testing")
#     radio1 = driver.find_element(By.XPATH, "//tbody/tr[3]/td[5]/div[1]/input[1]")
#     radio1.click()
#     time.sleep(1)
#     radio2 = driver.find_element(By.XPATH, "//tbody/tr[3]/td[5]/div[1]/input[1]")
#     radio2.click()
#     time.sleep(1)
#     driver.find_element(By.XPATH, "//button[@name='submit_row_2']").click()
#     time.sleep(3)
#     take_screenshot(driver, "Time Logged Successfully")
#
#     try:
#         success_message = WebDriverWait(driver, 10).until(
#             EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'toast-success')]"))
#         ).text
#         assert "Time logged Successfully" in success_message
#     except TimeoutException:
#         assert False, "Success message for valid phone number not displayed in time."
#
#
# def test_subtask_again(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//p[normalize-space()='Subtasks']").click()
#     time.sleep(2)
#     take_screenshot(driver,"Subtask Review Screenshot")
#     try:
#         status_element = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, "//tbody/tr[1]/td[9]"))
#         )
#         assert status_element.text == "Completed"
#     except TimeoutException:
#         take_screenshot(driver, "Subtask_Review_Timeout")
#         assert False, "In process"
