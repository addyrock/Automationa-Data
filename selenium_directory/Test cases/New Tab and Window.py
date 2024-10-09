import time
from selenium import webdriver
from selenium.webdriver import Keys

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(3)



driver.find_element(By.LINK_TEXT,"Register").send_keys(Keys.CONTROL+Keys.RETURN)
