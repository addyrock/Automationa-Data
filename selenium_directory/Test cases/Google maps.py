import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
def take_screenshot(step_name):
    driver.save_screenshot(f"{step_name}.png")
locations = ["Gulberg Lahore", "Liberty Market Lahore", "Shalimar Gardens Lahore", "Badshahi Mosque Lahore", "Lahore Fort"]
driver.get("https://www.google.com/maps")
driver.maximize_window()
time.sleep(5)

for location in locations:
    driver.get("https://www.google.com/maps")
    driver.maximize_window()
    time.sleep(5)

    search_input = driver.find_element(By.XPATH, "//input[@id='searchboxinput']")
    search_input.clear()
    search_input.send_keys(location)
    time.sleep(5)

driver.find_element(By.XPATH,"//span[@class='google-symbols']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//button[@class='vF7Cdb google-symbols yAuNSb']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='searchboxinput']").click()
time.sleep(5)
# take_screenshot("gulberg")
driver.find_element(By.XPATH,"//button[@class='GFG2E']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//span[@class='ExQYxb google-symbols'][contains(text(),'')]").click()
time.sleep(5)
driver.find_element(By.XPATH,"//button[@id='widget-zoom-in']//div[@class='qxwljb']").click()
# take_screenshot("traffic data")
time.sleep(5)
