import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
#
# serv_obj = Service()
# driver = webdriver.Chrome(service=serv_obj)
# driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
# driver.maximize_window()
# driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()
# Countries_List=driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
# print(len(Countries_List))
# for Country in Countries_List:
#      if Country.text=="Spain":
#          Country.click()
#          break
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the WebDriver (adjust the path to your WebDriver)
driver = webdriver.Chrome()

# Open the login page
driver.get("http://10.22.16.115/")

# Function to attempt login
def login(username, password):
    # Find and interact with the login elements
    username_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter Emp-ID']")  # Replace with actual name attribute
    password_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']")  # Replace with actual name attribute
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")       # Replace with actual name attribute or selector



    # Enter credentials and submit the form
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()

# Test invalid credentials
invalid_username = "nida.latif@psca.gop."  # Replace with invalid username
invalid_password = "12345"  # Replace with invalid password
login(invalid_username, invalid_password)

# Wait for the error message to appear
driver.implicitly_wait(10)  # Waits up to 10 seconds for elements to appear

# Check for unsuccessful login by verifying the error message
try:
    # Check for an error message (adjust the selector to match your error message element)
    error_message = driver.find_element(By.XPATH, "//div[@role='alert']")  # Replace with the actual selector for error message
    print("Login Test Passed: Unsuccessful login displayed error message")
except:
    print("Login Test Failed: No error message displayed for unsuccessful login")

# Close the browser
driver.quit()
