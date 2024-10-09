import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# define function for taking screenshot
def take_screenshot(step_name):
    driver.save_screenshot(f"{step_name}.png")

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#NUMBER OF LINKS
links = driver.find_elements(By.TAG_NAME,"a")
print(len(links))
for link in links:
    print(f"Link text: {link.text}")  #print all links text
    print(f"Link URL: {link.get_attribute('href')}")  #print all links url
driver.find_element(By.XPATH,"//a[normalize-space()='Register']").click()
time.sleep(5)
take_screenshot("23_Gender")
driver.find_element(By.XPATH,"//label[normalize-space()='Male']").click()
time.sleep(1)
take_screenshot("24_Name")
driver.find_element(By.XPATH,"//input[@id='FirstName']").send_keys("Arslan Arif Gorssi")
time.sleep(1)
take_screenshot("25_Father_Name")
driver.find_element(By.XPATH,"//input[@id='LastName']").send_keys("Muhammad Arif")
time.sleep(1)
take_screenshot("26_DOB")
dropdown=Select(driver.find_element(By.XPATH,"//select[@name='DateOfBirthDay']"))
# dropdown.select_by_value("17")
all_options = dropdown.options

# Iterate through all options and select each one by index
for index in range(len(all_options)):
    dropdown.select_by_index(index)
    time.sleep(1)  # Add delay to observe the selection (optional)


# driver.find_element(By.XPATH,"//select[@name='DateOfBirthDay']").send_keys("17")
# time.sleep(5)
take_screenshot("27_Month")

dropdown=Select(driver.find_element(By.XPATH,"//select[@name='DateOfBirthMonth']"))
dropdown.select_by_visible_text("February")


# driver.find_element(By.XPATH,"//select[@name='DateOfBirthMonth']").send_keys("May")
# time.sleep(1)
take_screenshot("28_year")
driver.find_element(By.XPATH,"//select[@name='DateOfBirthYear']").send_keys("1993")
time.sleep(1)
take_screenshot("29_Email")
driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("addyrock680@gmail.com")
time.sleep(1)
take_screenshot("30_Company")
driver.find_element(By.XPATH,"//input[@id='Company']").send_keys("Punjab Safe cities Authority")
time.sleep(1)
take_screenshot("31_Password")
driver.find_element(By.XPATH,"//input[@id='Password']").send_keys("A007arslan")
time.sleep(1)
take_screenshot("32_Password")
driver.find_element(By.XPATH,"//input[@id='ConfirmPassword']").send_keys("A007arslan")
time.sleep(1)
take_screenshot("33_click_register")
driver.find_element(By.XPATH,"//button[@id='register-button']").click()
time.sleep(1)
# driver.find_element(By.XPATH,"//a[@class='ico-logout']").click()
time.sleep(1)
#Login the Page
take_screenshot("34_Login")
driver.find_element(By.XPATH,"//a[normalize-space()='Log in']").click()
time.sleep(1)
take_screenshot("35_EMAIL")
driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("Addyrock680@gmail.com")
time.sleep(1)
take_screenshot("36_Passowrd")
driver.find_element(By.XPATH,"//input[@id='Password']").send_keys("A007arslan")
time.sleep(1)
take_screenshot("37_login")
driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()
time.sleep(1)
take_screenshot("38_logout")
driver.find_element(By.XPATH,"//a[normalize-space()='Log out']").click()
time.sleep(1)