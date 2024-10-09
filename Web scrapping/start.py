import time

import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoAlertPresentException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import matplotlib.pyplot as plt



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
def scroll_down(driver):
    # Scroll down the page by 500 pixels
    driver.execute_script("window.scrollBy(0, 1000);")

def scroll_up(driver):
    # Scroll up the page by 1000 pixels
    driver.execute_script("window.scrollBy(0, -1000);")


def generate_chart(pass_count, fail_count):
    labels = ['Passed', 'Failed']
    sizes = [pass_count, fail_count]
    colors = ['green', 'red']
    explode = (0.1, 0)  # explode the 1st slice

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Test Results')
    plt.savefig('test_results_pie_chart.png')
    plt.show()

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


# def test_user_name_empty(setup):
#     driver = setup
#     time.sleep(1)
#     empty_username = ""
#     valid_password = "123456@abc"
#     login(driver, empty_username, valid_password)
#     try:
#         error_message = WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((By.XPATH, "//div[@id='errordisplayid']"))
#         )
#         assert error_message.is_displayed()
#         take_screenshot(driver, "Username is empty")
#         print("Login Test Passed: Unsuccessful login displayed error message")
#     except Exception as e:
#
#         pytest.fail(f"Login Test Failed: No error message displayed for unsuccessful login. Exception: {e}")
#     # try:
#     #     WebDriverWait(driver, 5).until(EC.alert_is_present())
#     #     alert = driver.switch_to.alert
#     #     assert "Username must be filled out" in alert.text
#     #     alert.accept()
#     # except TimeoutException:
#     #     assert False, "Alert was not presented when expected"
#     take_screenshot(driver, 'Empty_user_name')
#
# def test_only_password_empty(setup):
#     driver = setup
#     time.sleep(1)
#     username = driver.find_element(By.XPATH, "//input[@id='password']")
#     username.clear()
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
#
# def test_wrong_credentials(setup):
#     driver = setup
#     username = driver.find_element(By.XPATH, "//input[@placeholder='Enter username or email']")
#     username.clear()
#     invalid_username = "QA_USER1"
#     invalid_password = "12345@"
#     login(driver, invalid_username, invalid_password)
#     time.sleep(2)
#     try:
#         WebDriverWait(driver, 3).until(EC.alert_is_present())
#         alert = driver.switch_to.alert
#         assert "Password must be between 8 and 25 characters" in alert.text
#         alert.accept()
#     except TimeoutException:
#         pass
#     take_screenshot(driver, 'Invalid_Credentials')

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

def test_dashboard_Suspect_Tracker(setup):
    driver = setup
    time.sleep(2)
    link_to_dashboard = driver.find_element(By.XPATH, "//h6[normalize-space()='Suspect Tracker']")
    blink_element(driver, link_to_dashboard)
    link_to_dashboard.click()
    time.sleep(2)
    assert "Successfully click on Suspect Tracker"
    take_screenshot(driver,"Suscpect tracker")

def test_mouse_on_charts(setup):
    driver=setup
    chart_element = driver.find_element(By.XPATH, "//div[@id='highcharts-2u8gaj8-2']//*[name()='svg']//*[name()='g']")

    # Create ActionChains object
    actions = ActionChains(driver)

    # Move mouse to the chart element
    actions.move_to_element(chart_element).perform()
    time.sleep(5)
    actions.move_to_element(chart_element).click()
    # Optional: Perform additional actions after moving to the chart element
    time.sleep(5)  # Example: Wait for 2 seconds after hovering

    # Example: Click on a specific point on the chart after hovering
    actions.click(chart_element).perform()
    time.sleep(5)
    actions.click(chart_element).click()
    time.sleep(2)  # Wait to observe the click action

    # Locate the element that shows the percentage (this will vary based on your chart implementation)
    percentage_element = driver.find_element(By.XPATH,
                                             "//span[normalize-space()='20%']")  # Replace with the actual selector

    # Verify the percentage (replace with your actual verification logic)
    expected_percentage = "EXPECTED_PERCENTAGE"  # Replace with the actual expected value
    actual_percentage = percentage_element.text
    assert actual_percentage == expected_percentage, f"Expected {expected_percentage}, but got {actual_percentage}"

    # Take a screenshot to confirm the action
    take_screenshot(driver, "chart_percentage_verification")

















# def test_Criminal_Face_Detection_CRO(setup):
#     driver = setup
#     time.sleep(2)
#     scroll_down(driver)
#     time.sleep(2)
#     scroll_up(driver)
#     time.sleep(2)
#     # show_detail = driver.find_element(By.XPATH, "//a[@id='showdetailsmarquee']")
#     # show_detail.click()
#     # time.sleep(5)
#     element = driver.find_element(By.XPATH, "//div[@id='dragAndDrop']")
#     blink_element(driver, element)
#     file_input = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
#     )
#     blink_element(driver, file_input)
#     file_path = "C:\\Users\\arslan.arif\\Desktop\\Criminal Pic for Testing\\download.png"
#     file_input.send_keys(file_path)
#     take_screenshot(driver, 'File_Upload')
#     time.sleep(5)
#     try:
#         CRO_Message = WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((By.XPATH, "//h5[@id='responseModalLabel']"))
#         )
#         assert CRO_Message.is_displayed()
#         time.sleep(5)
#         take_screenshot(driver, "CRO")
#         driver.find_element(By.XPATH,"//img[@alt='Close']").click()
#
#         print("Login Test Passed: Succsesfully CRO data Matched")
#     except Exception as e:
#          pytest.fail(f"Login Test Failed: No error message displayed for unsuccessful login. Exception: {e}")
#
# def test_Criminal_Face_Detection_CRO_1(setup):
#     driver = setup
#     time.sleep(2)
#     file_input = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
#     )
#     blink_element(driver, file_input)
#     file_path = "C:\\Users\\arslan.arif\\Desktop\\Criminal Pic for Testing\\download (1).png"
#     file_input.send_keys(file_path)
#     take_screenshot(driver, 'File_Upload1')
#     time.sleep(5)
#     try:
#         CRO_Message = WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((By.XPATH, "//h5[@id='responseModalLabel']"))
#         )
#         assert CRO_Message.is_displayed()
#         time.sleep(10)
#         take_screenshot(driver, "CRO1")
#         driver.find_element(By.XPATH,"//img[@alt='Close']").click()
#
#         print("Login Test Passed: Succsesfully CRO data Matched")
#     except Exception as e:
#          pytest.fail(f"Login Test Failed: No error message displayed for unsuccessful login. Exception: {e}")
#
# def test_Criminal_Face_Detection_CRO_2(setup):
#     driver = setup
#     time.sleep(2)
#     file_input = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
#     )
#     blink_element(driver, file_input)
#     file_path = "C:\\Users\\arslan.arif\\Desktop\\Criminal Pic for Testing\\download (2).png"
#     file_input.send_keys(file_path)
#     take_screenshot(driver, 'File_Upload2')
#     time.sleep(5)
#     try:
#         CRO_Message = WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((By.XPATH, "//h5[@id='responseModalLabel']"))
#         )
#         assert CRO_Message.is_displayed()
#         time.sleep(10)
#         take_screenshot(driver, "CRO2")
#         driver.find_element(By.XPATH,"//img[@alt='Close']").click()
#
#         print("Login Test Passed: Succsesfully CRO data Matched")
#     except Exception as e:
#          pytest.fail(f"Login Test Failed: No error message displayed for unsuccessful login. Exception: {e}")
# def test_Criminal_Face_Detection_CRO_3(setup):
#     driver = setup
#     time.sleep(2)
#     file_input = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
#     )
#     blink_element(driver, file_input)
#     file_path = "C:\\Users\\arslan.arif\\Desktop\\Criminal Pic for Testing\\download (3).png"
#     file_input.send_keys(file_path)
#     take_screenshot(driver, 'File_Upload3')
#     time.sleep(5)
#     try:
#         CRO_Message = WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((By.XPATH, "//h5[@id='responseModalLabel']"))
#         )
#         assert CRO_Message.is_displayed()
#         time.sleep(10)
#         take_screenshot(driver, "CRO3")
#         driver.find_element(By.XPATH,"//img[@alt='Close']").click()
#         time.sleep(5)
#         print("Login Test Passed: Succsesfully CRO data Matched")
#     except Exception as e:
#          pytest.fail(f"Login Test Failed: No error message displayed for unsuccessful login. Exception: {e}")
#
# def test_Predictive_Analysis_Cantt(setup):
#     driver = setup
#     driver.find_element(By.XPATH, "//h6[normalize-space()='Predictive Analysis']").click()
#     time.sleep(2)
#     first_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='divisionselected']"))  # Update the locator to match your page
#     first_dropdown.select_by_index(1)  # Select by index, value, or visible text
#     blink_element(driver, first_dropdown._el)  # Use the underlying web element
#
#     # Locate the second dropdown
#     second_dropdown = Select(
#         driver.find_element(By.XPATH, "//select[@id='psselected']"))  # Update the locator to match your page
#     blink_element(driver, second_dropdown._el)  # Use the underlying web element
#
#     # Get all options from the second dropdown
#     all_options = second_dropdown.options
#
#     # Iterate through all options in the second dropdown
#     for index in range(0, len(all_options)):  # Skipping the first option (index 0) if it's a placeholder
#         second_dropdown.select_by_index(index)
#         time.sleep(2)  # Add a delay to observe the selection (if needed)
#
#         # Click the button after each selection
#         button = driver.find_element(By.XPATH, "//button[@id='showResultNew']")  # Update the locator to match your page
#         button.click()
#         time.sleep(2)  # Add a delay to observe the button click action
#
#         # Take a screenshot after each selection
#         screenshot_name = f"Analysis_{index}"
#         take_screenshot(driver, screenshot_name)


# def test_Predictive_Analysis_Iqbal_town(setup):
#     driver = setup
#     first_dropdown = Select(
#         driver.find_element(By.XPATH, "//select[@id='divisionselected']"))  # Update the locator to match your page
#     first_dropdown.select_by_index(2)  # Select by index, value, or visible text
#     blink_element(driver, first_dropdown._el)  # Use the underlying web element
#
#     # Locate the second dropdown
#     second_dropdown = Select(
#         driver.find_element(By.XPATH, "//select[@id='psselected']"))  # Update the locator to match your page
#     blink_element(driver, second_dropdown._el)  # Use the underlying web element
#
#     # Get all options from the second dropdown
#     all_options = second_dropdown.options
#
#     # Iterate through all options in the second dropdown
#     for index in range(1, len(all_options)):  # Skipping the first option (index 0) if it's a placeholder
#         second_dropdown.select_by_index(index)
#         time.sleep(2)  # Add a delay to observe the selection (if needed)
#
#         # Click the button after each selection
#         button = driver.find_element(By.XPATH, "//button[@id='showResultNew']")  # Update the locator to match your page
#         button.click()
#         time.sleep(2)  # Add a delay to observe the button click action
#
#         # Take a screenshot after each selection
#         screenshot_name = f"Analysis_{index}"
#         take_screenshot(driver, screenshot_name)
def test_custom_predictive_analysis(setup):
    driver = setup
    scroll_down(driver)
    driver.find_element(By.XPATH, "//h6[normalize-space()='Predictive Analysis']").click()
    time.sleep(2)
    # Start Date
    start_date = driver.find_element(By.XPATH, "//input[@id='start-date']")
    blink_element(driver, start_date)
    start_date.clear()
    start_date.send_keys("07/01/2024")
    take_screenshot(driver, "start_date_set")

    # End Date
    end_date = driver.find_element(By.XPATH, "//input[@id='end-date']")
    blink_element(driver, end_date)
    end_date.clear()
    end_date.send_keys("07/27/2024")
    end_date.send_keys(Keys.TAB)
    take_screenshot(driver, "end_date_set")

    # Category Dropdown
    category_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='crime-category-new']"))
    blink_element(driver, category_dropdown._el)

    # Get all options from the second dropdown
    all_options = category_dropdown.options

    # Iterate through all options in the second dropdown
    for index in range(0, len(all_options)):  # Skipping the first option (index 0) if it's a placeholder
        category_dropdown.select_by_index(index)
        time.sleep(2)

        # Take a screenshot after each selection
        screenshot_name = f"custom_predictive_analysis_{index}"
        take_screenshot(driver, screenshot_name)
#--------------------
# def test_custom_pridictive_analysis(setup):
#     driver = setup
#     scroll_down(driver)
#     start_date = driver.find_element(By.XPATH, "//input[@id='start-date']")
#     start_date.clear()
#     start_date.send_keys("2024-07-01")
#     start_date.click()
#     blink_element(driver, start_date)
#     end_date = driver.find_element(By.XPATH, "//input[@id='end-date']")
#     end_date.clear()
#     end_date.send_keys("2024-07-21")
#     end_date.click()
#     blink_element(driver, end_date)
#     category_dropdown = Select(
#         driver.find_element(By.XPATH, "//select[@id='crime-category-new']"))  # Update the locator to match your page
#     blink_element(driver, category_dropdown._el)  # Use the underlying web element
#
#     # Get all options from the second dropdown
#     all_options = category_dropdown.options
#
#     # Iterate through all options in the second dropdown
#     for index in range(0, len(all_options)):  # Skipping the first option (index 0) if it's a placeholder
#         category_dropdown.select_by_index(index)
#         time.sleep(2)
#
#         # Take a screenshot after each selection
#         screenshot_name = f"custom_predictive_analysis{index}"
#         take_screenshot(driver, screenshot_name)

#----------------------------------



















def test_logout(setup):
    driver = setup
    button = driver.find_element(By.XPATH, "//h6[normalize-space()='Logout']")
    blink_element(driver,button)
    button.click()
    time.sleep(3)
    driver.switch_to.alert.accept()
    time.sleep(5)





#
# def test_Predictive_Analysis_Civil_Line(setup):
#     driver = setup
#     first_dropdown = Select(
#         driver.find_element(By.XPATH, "//select[@id='divisionselected']"))  # Update the locator to match your page
#     first_dropdown.select_by_index(3)  # Select by index, value, or visible text
#     blink_element(driver, first_dropdown._el)  # Use the underlying web element
#
#     # Locate the second dropdown
#     second_dropdown = Select(
#         driver.find_element(By.XPATH, "//select[@id='psselected']"))  # Update the locator to match your page
#     blink_element(driver, second_dropdown._el)  # Use the underlying web element
#
#     # Get all options from the second dropdown
#     all_options = second_dropdown.options
#
#     # Iterate through all options in the second dropdown
#     for index in range(1, len(all_options)):  # Skipping the first option (index 0) if it's a placeholder
#         second_dropdown.select_by_index(index)
#         time.sleep(2)  # Add a delay to observe the selection (if needed)
#
#         # Click the button after each selection
#         button = driver.find_element(By.XPATH,
#                                      "//button[@id='showResultNew']")  # Update the locator to match your page
#         button.click()
#         time.sleep(2)  # Add a delay to observe the button click action
#
#         # Take a screenshot after each selection
#         screenshot_name = f"Analysis_{index}"
#         take_screenshot(driver, screenshot_name)
#
# def test_Predictive_Analysis_Saddar(setup):
#     driver = setup
#     first_dropdown = Select(
#         driver.find_element(By.XPATH, "//select[@id='divisionselected']"))  # Update the locator to match your page
#     first_dropdown.select_by_index(4)  # Select by index, value, or visible text
#     blink_element(driver, first_dropdown._el)  # Use the underlying web element
#
#     # Locate the second dropdown
#     second_dropdown = Select(
#         driver.find_element(By.XPATH, "//select[@id='psselected']"))  # Update the locator to match your page
#     blink_element(driver, second_dropdown._el)  # Use the underlying web element
#
#     # Get all options from the second dropdown
#     all_options = second_dropdown.options
#
#     # Iterate through all options in the second dropdown
#     for index in range(1, len(all_options)):  # Skipping the first option (index 0) if it's a placeholder
#         second_dropdown.select_by_index(index)
#         time.sleep(2)  # Add a delay to observe the selection (if needed)
#
#         # Click the button after each selection
#         button = driver.find_element(By.XPATH,
#                                      "//button[@id='showResultNew']")  # Update the locator to match your page
#         button.click()
#         time.sleep(2)  # Add a delay to observe the button click action
#
#         # Take a screenshot after each selection
#         screenshot_name = f"Analysis_{index}"
#         take_screenshot(driver, screenshot_name)
#
# def test_Predictive_Analysis_City(setup):
#     driver = setup
#     first_dropdown = Select(
#         driver.find_element(By.XPATH, "//select[@id='divisionselected']"))  # Update the locator to match your page
#     first_dropdown.select_by_index(5)  # Select by index, value, or visible text
#     blink_element(driver, first_dropdown._el)  # Use the underlying web element
#
#     # Locate the second dropdown
#     second_dropdown = Select(
#         driver.find_element(By.XPATH, "//select[@id='psselected']"))  # Update the locator to match your page
#     blink_element(driver, second_dropdown._el)  # Use the underlying web element
#
#     # Get all options from the second dropdown
#     all_options = second_dropdown.options
#
#     # Iterate through all options in the second dropdown
#     for index in range(1, len(all_options)):  # Skipping the first option (index 0) if it's a placeholder
#         second_dropdown.select_by_index(index)
#         time.sleep(2)  # Add a delay to observe the selection (if needed)
#
#         # Click the button after each selection
#         button = driver.find_element(By.XPATH,
#                                      "//button[@id='showResultNew']")  # Update the locator to match your page
#         button.click()
#         time.sleep(2)  # Add a delay to observe the button click action
#
#         # Take a screenshot after each selection
#         screenshot_name = f"Analysis_{index}"
#         take_screenshot(driver, screenshot_name)
#
# def test_Predictive_Analysis_Model_Town(setup):
#     driver = setup
#     first_dropdown = Select(
#         driver.find_element(By.XPATH, "//select[@id='divisionselected']"))  # Update the locator to match your page
#     first_dropdown.select_by_index(6)  # Select by index, value, or visible text
#     blink_element(driver, first_dropdown._el)  # Use the underlying web element
#
#     # Locate the second dropdown
#     second_dropdown = Select(
#         driver.find_element(By.XPATH, "//select[@id='psselected']"))  # Update the locator to match your page
#     blink_element(driver, second_dropdown._el)  # Use the underlying web element
#
#     # Get all options from the second dropdown
#     all_options = second_dropdown.options
#
#     # Iterate through all options in the second dropdown
#     for index in range(1, len(all_options)):  # Skipping the first option (index 0) if it's a placeholder
#         second_dropdown.select_by_index(index)
#         time.sleep(2)  # Add a delay to observe the selection (if needed)
#
#         # Click the button after each selection
#         button = driver.find_element(By.XPATH,
#                                      "//button[@id='showResultNew']")  # Update the locator to match your page
#         button.click()
#         time.sleep(2)  # Add a delay to observe the button click action
#
#         # Take a screenshot after each selection
#         screenshot_name = f"Analysis_{index}"
#         take_screenshot(driver, screenshot_name)

    # driver=setup
    # first_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='divisionselected']"))  # Update the locator to match your page
    # first_dropdown.select_by_index(2)  # Select by index, value, or visible text
    #
    # # Locate the second dropdown
    # second_dropdown = Select(
    #     driver.find_element(By.XPATH, "//select[@id='psselected']"))  # Update the locator to match your page
    #
    # # Get all options from the second dropdown
    # all_options = second_dropdown.options
    #
    # # Iterate through all options in the second dropdown
    # for index in range(1, len(all_options)):  # Skipping the first option (index 0) if it's a placeholder
    #     second_dropdown.select_by_index(index)
    #     time.sleep(2)  # Add a delay to observe the selection (if needed)
    #
    #     # Click the button after each selection
    #     button = driver.find_element(By.XPATH, "//button[@id='showResultNew']")  # Update the locator to match your page
    #     button.click()
    #     take_screenshot(driver, 'Analysis1')
    #     # Add a delay to observe the button click action
    #     time.sleep(1)