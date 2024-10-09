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
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick")
driver.maximize_window()

driver.switch_to.frame("iframeResult")
act=ActionChains(driver)

button=driver.find_element(By.XPATH,"//button[normalize-space()='Double-click me']")
act.double_click(button).perform()