import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC




driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser")
driver.maximize_window()

# below 3 lines will log into the application
time.sleep(2)
driver.find_element(By.NAME, "username").send_keys("Admin")
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys("admin123")
time.sleep(2)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)

driver.find_element(By.XPATH,"//span[normalize-space()='User Management']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//ul[@role='menu']//li").click()

