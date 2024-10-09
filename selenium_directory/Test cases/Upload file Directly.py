
import time
from turtledemo.chaos import g

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By

serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.filemail.com/share/upload-file")
driver.maximize_window()

click_method=driver.find_element(By.XPATH,"//span[normalize-space()='Add Files']").click()
time.sleep(10)
