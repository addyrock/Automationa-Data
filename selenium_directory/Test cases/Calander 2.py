import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.switch_to.frame(0)

year = "2025"
month = "March"
date="30"# Corrected capitalization

driver.find_element(By.ID, "datepicker").click()  # Used ID locator

while True:
    mon_element = driver.find_element(By.CLASS_NAME, "ui-datepicker-month")
    yr_element = driver.find_element(By.CLASS_NAME, "ui-datepicker-year")

    mon = mon_element.text
    yr = yr_element.text

    if mon == month and yr == year:
        break
    else:
        driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]/span").click()  # Corrected XPath

time.sleep(5)  # Adjust sleep time as necessary
dwait = WebDriverWait(driver, 10)
date_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='ui-datepicker-div']//table//td/a[text()='{}']".format(date))))

# Scroll to the date element
actions = ActionChains(driver)
actions.move_to_element(date_element).perform()

# Click the date element using JavaScript
driver.execute_script("arguments[0].click();", date_element)