import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

# define function for taking screenshot
def take_screenshot(step_name):
    driver.save_screenshot(f"{step_name}.png")

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# List of items to search
items_to_search = ['Laptop', 'Camera', 'Phone','Shoes','watch','Cloth','Bag']

for index, item in enumerate(items_to_search, start=1):
    search_input = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
    search_input.clear()
    search_input.send_keys(item)
    search_input.submit()
    take_screenshot(f"{index}_{item.replace(' ', '_')}_search")
    time.sleep(2)  # Wait for page to load completely

driver.quit()
