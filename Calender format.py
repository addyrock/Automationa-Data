import time
from datetime import datetime
import pytest
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://blooddonors.psca.gop.pk/login")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@id='username']").send_keys("qa.psca.gop.pk")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("psca@123")
driver.find_element(By.XPATH, "//button[normalize-space()='Sign Me In']").click()
time.sleep(5)



case_cli= driver.find_element(By.XPATH,"//span[normalize-space()='Cases']")

case_cli.click()
time.sleep(2)
serch_box = driver.find_element(By.XPATH,"//input[@type='search']")

serch_box.send_keys("Test Automation")
time.sleep(2)
drag_button = driver.find_element(By.XPATH,"//td[@class='sorting_1 dtr-control'][normalize-space()='1']")

drag_button.click()

view_button = driver.find_element(By.XPATH,"//span[@class='dtr-data']//a[@title='view case']")

view_button.click()
time.sleep(2)

time.sleep(2)
add_folo = driver.find_element(By.XPATH,"//button[normalize-space()='Add Followup']")

add_folo.click()
time.sleep(2)
sel_drop = Select(driver.find_element(By.XPATH,"//select[@id='status_id']"))

sel_drop.select_by_visible_text("Pending")

rem_com = driver.find_element(By.XPATH,"//textarea[@id='remarks']")

rem_com.send_keys("This is a test remark.")
time.sleep(2)
but_cl= driver.find_element(By.XPATH,"//form[@id='AddFollowupForm']//button[@type='submit'][normalize-space()='Save']")

but_cl.click()
time.sleep(10)



# don_req = driver.find_element(By.XPATH,"//button[normalize-space()='Donation Request']")
#
# don_req.click()
# time.sleep(2)
# ent_num = driver.find_element(By.XPATH,"//input[@id='request_phone_number']")
#
# ent_num.send_keys("03000000002")
# time.sleep(5)
# pro_button = driver.find_element(By.XPATH,"//button[normalize-space()='Proceed']")
#
# pro_button.click()
# time.sleep(5)
# # Find the date input field and enter the date (15-03-2025)
# req_donate = driver.find_element(By.XPATH, "//input[@id='blood_required_date_time']")
# req_donate.clear()
# req_donate.send_keys("15-03-2025")
# # Optionally, simulate pressing 'Enter' if required
# req_donate.send_keys(Keys.RETURN)
# time.sleep(3)
#
# # Assuming the time input is separate and needs to be handled after the date is selected
# # Find the time input field and enter the time (6:06 AM)
# req_donate1 = driver.find_element(By.XPATH, "//input[@id='blood_required_date_time']")
# # req_donate1.clear()
# req_donate1.send_keys("6:06 AM")
# # Optionally, simulate pressing 'Enter' if required
# req_donate1.send_keys(Keys.RETURN)
#
# time.sleep(3)

# last_don = driver.find_element(By.XPATH, "//input[@id='blood_required_date_time']")
#
# # Use JavaScript to set the value with the full date and time
# date_time_value = "14/01/2025 10:11 am"
# driver.execute_script(f"arguments[0].setAttribute('value', '{date_time_value}')", last_don)
# last_don = driver.find_element(By.XPATH, "//input[@id='blood_required_date_time']")

# lost_don = driver.find_element(By.XPATH, "//input[@id='blood_required_date_time']")
# lost_don.click()
# lost_don.send_keys("14/01/2025")
# last_don = driver.find_element(By.XPATH, "//input[@id='blood_required_date_time']")
#
# last_don.send_keys("10:30am")



# last_don = driver.find_element(By.XPATH, "//input[@id='blood_required_date_time']")
#
# # Clear the field (if any pre-filled value exists)
# last_don.clear()

# Enter the date and time in the expected format (dd/MM/yyyy hh:mm am/pm)
# date_time_value = "14/01/2025 10:11 am"
# last_don.send_keys(date_time_value)
# last_don = driver.find_element(By.XPATH, "//input[@id='blood_required_date_time']")
#
#     # Use JavaScript to set the value
# date_time_value = "14/01/2025 10:11 am"
# driver.execute_script("arguments[0].value = arguments[1];", last_don, date_time_value)
# last_don = driver.find_element(By.XPATH, "//input[@id='blood_required_date_time']")
# driver.execute_script("arguments[0].value = '14/01/2025 10:11 am';", last_don)

# last_don.send_keys("14/01/2025 T22:11")

# last_don = driver.find_element(By.XPATH, "//input[@type='datetime-local']")
#
# # Step 2: Click to open the calendar and time picker
# last_don.click()
#
# # Step 3: Select the date from the calendar
# # The calendar is part of the input's popup, so the date selection would typically be via the UI in the browser.
# # Since we're working with 'datetime-local', you can set the value directly.
#
# # For example, if you want to set the date as "14/01/2025 10:30 AM":
# # Convert the time to 24-hour format for 'datetime-local' input.
# date_time_value = "2025-01-14T10:30"  # The format must be "YYYY-MM-DDTHH:MM" (24-hour format)
#
# # Step 4: Set the value directly in the input field
# last_don.clear()  # Clear any pre-filled value
# last_don.send_keys(date_time_value)

# last_don = driver.find_element(By.XPATH, "//input[@type='datetime-local']")
#
# # Step 2: Click to open the calendar and time picker
# last_don.click()
#
# # Step 3: Set the date and time in the correct format (YYYY-MM-DDTHH:MM)
# # Ensure the year is four digits
# # date_time_value = "T14/01/2025T10:30TAM"  # YYYY-MM-DDTHH:MM (24-hour format)
# # last_don.send_keys(date_time_value)
# # # Step 4: Clear any pre-filled value and send the correctly formatted value
# #
# # last_don.send_keys(date_time_value)
#
# last_don = driver.find_element(By.XPATH, "//input[@id='blood_required_date_time']")
#
# # Clear any pre-filled value
# last_don.clear()
#
# # Set the correct date (dd/MM/yyyy) and time (hh:mm am/pm)
# date_value = "14/01/2025"  # Date in dd/MM/yyyy format
# time_value = "T10:30 am"    # Time in hh:mm am/pm format
#
# # Combine date and time
# date_time_value = f"{date_value} {time_value}"
#
# # Send the correctly formatted date and time
# last_don.send_keys(date_time_value)
# last_don.send_keys(time_value)
#
# time.sleep(10)
#









