import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)

def take_screenshot(step_name):
    driver.save_screenshot(f"{step_name}.png")

driver.get("http://10.22.16.115/")
driver.maximize_window()
expected_title = "| Log in"

actual_title = driver.title

# Print the result
if actual_title == expected_title:
    print("Test Passed: Title is correct")
else:
    print(f"Test Failed: Title is '{actual_title}' but expected '{expected_title}'")
def login(username, password):
    # Find and interact with the login elements
    username_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter Emp-ID']")
    print("Username enter successfully")
    password_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    # Enter credentials and submit the form
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()

# Test invalid credentials
invalid_username = "547-2019-5130"
invalid_password = "123456"
login(invalid_username, invalid_password)


driver.implicitly_wait(10)

# Check for unsuccessful login by verifying the error message
try:

    error_message = driver.find_element(By.XPATH, "//div[@role='alert']")
    print("Login Test Passed: Unsuccessful login displayed error message")
except:
    print("Login Test Failed: No error message displayed for unsuccessful login")
take_screenshot("Login Successfully")
driver.find_element(By.XPATH,"//i[@class='fas fa-bars']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//i[@class='fas fa-bars']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//p[normalize-space()='Dashboard']").click()
time.sleep(1)

#test Subtask module
take_screenshot("Main Dashboard View")
driver.find_element(By.XPATH,"//a[@href='#']//p[contains(text(),'Tasks')]").click()
driver.find_element(By.XPATH,"//li[@class='nav-item menu-is-opening menu-open']//li[1]//a[1]").click()
driver.find_element(By.XPATH,"//tr[@class='odd']//i[@class='fa fa-eye']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[@href='#']//p[contains(text(),'Tasks')]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//li[@class='nav-item menu-is-opening menu-open']//li[1]//a[1]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//tr[@class='odd']//i[@class='far fa-comment-alt']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='Name']").send_keys(" Selenium test subtask")
time.sleep(2)
driver.find_element(By.XPATH,"//textarea[@name='description']").send_keys("Selenium Webdriver test Script with Python")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='duration']").send_keys("6")
time.sleep(2)
dropdown = Select(driver.find_element(By.XPATH,"//select[@id='status']"))
dropdown.select_by_visible_text("In Progress")
driver.find_element(By.XPATH,"//div[@id='addActivityModal']//button[@type='submit'][normalize-space()='Add']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[@href='#']//p[contains(text(),'Tasks')]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//p[normalize-space()='Subtasks']").click()
time.sleep(2)

driver.find_element(By.XPATH,"//tbody/tr[1]/td[11]/a[1]/i[1]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//p[normalize-space()='Subtasks']").click()
time.sleep(2)
print("Subtask done")
driver.find_element(By.XPATH,"//tbody/tr[1]/td[11]/a[2]/i[1]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//p[normalize-space()='Subtasks']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//tbody/tr[1]/td[11]/a[3]/i[1]").click()
time.sleep(2)
driver.switch_to.alert.accept()
take_screenshot("Subtask Cancelled Successfully")
time.sleep(5)
driver.refresh()
take_screenshot("Subtask main view")
time.sleep(5)
driver.find_element(By.XPATH,"//p[normalize-space()='Dashboard']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//div[@class='small-box bg-warning']//a[@class='small-box-footer'][normalize-space()='More info']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//p[normalize-space()='Dashboard']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='small-box bg-success']//a[@class='small-box-footer'][normalize-space()='More info']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//p[normalize-space()='Dashboard']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='small-box bg-danger']//a[@class='small-box-footer'][normalize-space()='More info']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//p[@class='text']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//input[@id='nameshow']").send_keys("123")
time.sleep(5)
print("text box is disabled")
email=driver.find_element(By.XPATH,"//input[@id='email']")
email.clear()
time.sleep(2)
email.send_keys("nida.latif@psca.gop.pk")

time.sleep(5)
ele=driver.find_element(By.XPATH,"//input[@id='designation']")
ele.clear()
time.sleep(2)
ele.send_keys("DEO SQA")

phone=driver.find_element(By.XPATH,"//input[@id='phone']")
phone.clear()
time.sleep(2)
phone.send_keys("03226496719")

#for loop to select name from dropdown
dropdown = Select(driver.find_element(By.NAME,"unit_id"))
for index in range(5):
    dropdown.select_by_index(index)
    time.sleep(1)
dropdown.select_by_visible_text("Safeer Abbas")
driver.find_element(By.XPATH,"//button[normalize-space()='Save']").click()
time.sleep(2)
take_screenshot("Update User Information Successfully")
print("user information update Successfully")
time.sleep(5)
driver.find_element(By.XPATH,"//a[normalize-space()='Logout']").click()
time.sleep(5)
driver.quit()



