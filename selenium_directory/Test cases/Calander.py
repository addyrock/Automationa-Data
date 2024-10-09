import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
# driver.implicitly_wait(10)
driver.switch_to.frame(0)
# driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("04/08/2024")
year = "2025"
month = "March"
date = "30"

driver.find_element(By.XPATH, "//input[@id='datepicker']").click()

while True:
    mon = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
    yr = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text

    if mon == month and yr == year:
        break
    else:
        driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]/span").click()
time.sleep(5)
# driver.find_element(By.XPATH,"//a[normalize-space()='18']").click()
dates = driver.find_elements(By.XPATH, "//div[@id='ui-datepicker-div']//table//td/a")
driver.implicitly_wait(10)
for ele in dates:
    if ele.text == date:
        ele.click()
        break
