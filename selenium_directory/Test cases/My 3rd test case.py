import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser")
driver.maximize_window()

# below 3 lines will log into the application
driver.find_element(By.NAME, "username").send_keys("edmin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[@class='oxd-main-menu-item active']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//div[4]//div[1]//div[6]//div[1]//button[1]//i[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[normalize-space()='Yes, Delete']").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
time.sleep(2)
# driver.close()
# print(driver.title)
# print(driver.current_url)
# driver.refresh()
#
orange_link=driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc")
orange_link.click()