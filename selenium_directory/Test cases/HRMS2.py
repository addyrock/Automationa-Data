import time
from _ast import Assert


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

# Define function for taking screenshot
def take_screenshot(step_name):
    driver.save_screenshot(f"{step_name}.png")

# Function to perform action and take screenshot
def perform_action(action_function, screenshot_name):
    action_function()
    take_screenshot(screenshot_name)
    time.sleep(2)  # Adjust sleep time as needed

# Define your actions
def login():
    driver.get("http://10.20.10.137:800/")
    driver.maximize_window()
    # Assert.assertEquals(driver.getCurrentUrl(),"http://10.20.10.137:800/")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "txtLoginName")))
    driver.find_element(By.ID, "txtLoginName").send_keys("547-2016-6103")
    driver.find_element(By.ID, "txtPassword").send_keys("35202-3476111-5")
    driver.find_element(By.ID, "btnLogin").click()

def click_appraisal_dropdown():
    driver.find_element(By.XPATH,"//li[@id='LiAppraisal']//a[@class='dropdown-toggle']").click()

def click_appraisal_employee():
    driver.find_element(By.XPATH,"//a[normalize-space()='Appraisal Employee']").click()

def click_roster_management():
    driver.find_element(By.XPATH,"//span[normalize-space()='Roster Management']").click()

def click_knowledge_base():
    driver.find_element(By.XPATH,"//span[normalize-space()='Knowledge Base']").click()

def open_document_in_new_tab():
    # Store the current window handle
    original_window = driver.current_window_handle

    # Open the document link in a new tab using JavaScript
    document_link = driver.find_element(By.XPATH, "//li[1]//h5[1]//a[1]//i[1]")
    driver.execute_script("window.open(arguments[0], '_blank');", document_link.get_attribute("href"))

    # Switch to the new tab
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    # Take a screenshot in the new tab
    take_screenshot("document_in_new_tab")

    # Close the new tab and switch back to the original tab
    driver.close()
    driver.switch_to.window(original_window)

# Perform actions using the wrapper function
perform_action(login, "after_login")
perform_action(click_appraisal_dropdown, "after_appraisal_dropdown")
perform_action(click_appraisal_employee, "after_appraisal_employee")
perform_action(click_roster_management, "after_roster_management")
perform_action(click_knowledge_base, "knowledge_base")
perform_action(open_document_in_new_tab, "document_in_new_tab")
time.sleep(10)  # Adding sleep to ensure visibility
