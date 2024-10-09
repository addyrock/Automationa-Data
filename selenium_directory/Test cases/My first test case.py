# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# # Initialize the WebDriver
# driver = webdriver.Chrome()
#
# # Open the webpage
# url = "https://testautomationpractice.blogspot.com/"
# driver.get(url)
#
# # Click on the datepicker and enter a date
# datepicker = driver.find_element(By.XPATH, "//input[@id='datepicker']")
# datepicker.click()
# datepicker.send_keys("04/05/2024")
#
# time.sleep(2)
#
# # Execute JavaScript to open a new tab
# driver.execute_script("window.open('');")
# time.sleep(2)
#
# # Switch to the new tab
# driver.switch_to.window(driver.window_handles[1])
# time.sleep(2)
# # Open the link in the new tab
# url_1 = "https://opensource-demo.orangehrmlive.com/"
# driver.get(url_1)
# #
# # # Switch back to the original tab
# driver.execute_script("window.open('');")
# driver.switch_to.window(driver.window_handles[2])
# url_2="https://demo.opencart.com/"
# driver.get(url_2)
#
# driver.switch_to.window(driver.window_handles[0])


