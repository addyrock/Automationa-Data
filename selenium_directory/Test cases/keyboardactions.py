import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException

serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)

# driver.implicitly_wait(10)
driver.get("https://text-compare.com/")
driver.maximize_window()

box_1=driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
box_2=driver.find_element(By.XPATH,"//textarea[@id='inputText2']")
box_1.send_keys("Welcome to selenium")

act=ActionChains(driver)
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()
act.send_keys(Keys.TAB).perform()
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(10)