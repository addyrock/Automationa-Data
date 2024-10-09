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
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("https://www.seiyria.com/bootstrap-slider")
slider=driver.find_element(By.CSS_SELECTOR, "div#example-1 div.slider-handle.min-slider-handle.round")

move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(40, 0).release().perform()
