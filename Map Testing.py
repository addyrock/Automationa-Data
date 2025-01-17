import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()

# Open Google Maps
driver.get("https://www.google.com/maps")
time.sleep(3)

# Wait for the search box and enter the query
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "searchboxinput"))
)
search_box.send_keys("AhmadPur Public School")
search_box.send_keys(Keys.RETURN)

# Wait for results to load
time.sleep(15)



# iframe = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.TAG_NAME, "iframe"))
# )
# driver.switch_to.frame(iframe)

# map_click = WebDriverWait(driver, 15).until(
#     EC.element_to_be_clickable((By.XPATH, "//a[contains(@aria-label, 'AhmadPur Public School')]"))
# )
# map_click.click()




first_result = driver.find_element(By.XPATH, "(//div[contains(@class, 'Nv2PK')])[3]")
first_result.click()
time.sleep(15)

