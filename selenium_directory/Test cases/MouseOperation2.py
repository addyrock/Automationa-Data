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
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

com=driver.find_element(By.LINK_TEXT,"Computers")
time.sleep(2)
des=driver.find_element(By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Desktops']")
time.sleep(2)
act=ActionChains(driver)
act.move_to_element(com).move_to_element(des).click().perform()