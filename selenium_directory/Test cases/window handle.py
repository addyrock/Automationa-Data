import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
time.sleep(3)
driver.switch_to.window(driver.window_handles[0])

# driver.implicitly_wait(10)
# driver.get("https://demo.automationtesting.in/Frames.html")
# # driver.maximize_window()
# driver.find_element(By.XPATH,"//iframe[@id='singleframe']")
# time.sleep(3)
#
# iframe=driver.find_element(By.TAG_NAME,"a").send_keys("welcome")
# driver.switch_to.frame(iframe)
# time.sleep(5)
#
from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver.get("https://seleniumhq.github.io")
#
#     # Setup wait for later
# wait = WebDriverWait(driver, 10)
#
#     # Store the ID of the original window
# original_window = driver.current_window_handle
#
#     # Check we don't have other windows open already
# assert len(driver.window_handles) == 1
#
#     # Click the link which opens in a new window
# driver.find_element(By.LINK_TEXT, "new window").click()
#
#     # Wait for the new window or tab
# wait.until(EC.number_of_windows_to_be(2))
#
#     # Loop through until we find a new window handle
# for window_handle in driver.window_handles:
#         if window_handle != original_window:
#             driver.switch_to.window(window_handle)
#             break
#     wait.until(EC.title_is("SeleniumHQ Browser Automation"))
#
