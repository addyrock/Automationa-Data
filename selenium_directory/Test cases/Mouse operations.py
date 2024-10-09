"""
Actionchains
1: mouse hover
2: single click
3: double click
4: drag and drop

"""
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException

serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser")
driver.maximize_window()
driver.implicitly_wait(10)
# below 3 lines will log into the application
time.sleep(3)
driver.find_element(By.NAME, "username").send_keys("Admin")
time.sleep(3)
driver.find_element(By.NAME, "password").send_keys("admin123")
time.sleep(3)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(3)
admin=driver.find_element(By.XPATH,"//a[@class='oxd-main-menu-item active']//span[1]")
time.sleep(1)
usermgmt=(driver.find_element(By.XPATH,"//span[normalize-space()='User Management']"))
time.sleep(2)
usermgmt_2=driver.find_element(By.XPATH, "//ul[@role='menu']//li")
time.sleep(2)
Actions=ActionChains(driver)
Actions.move_to_element(admin).move_to_element(usermgmt).click()
Actions.click(usermgmt_2).perform()


# # Assuming you've already logged in and are on the correct page
#
# # Wait for the admin menu to be clickable
# admin_menu = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//a[@class='oxd-main-menu-item active']//span[1]"))
# )
#
# # Hover over the admin menu
# ActionChains(driver).move_to_element(admin_menu).perform()
#
# # Wait for the User Management submenu to be visible
# user_management_submenu = WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='User Management']"))
# )
#
# # Hover over the User Management submenu
# ActionChains(driver).move_to_element(user_management_submenu).perform()
#
# # Wait for the Users option to be visible
# users_option = WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.XPATH, "//ul[@class='oxd-dropdown-menu']//li"))
# )
#
# # Click on the Users option
# users_option.click()
