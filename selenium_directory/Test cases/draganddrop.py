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
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()


# act=ActionChains(driver)

# button_drag=driver.find_element(By.XPATH,"//div[@id='draggable']")
# button_drop=driver.find_element(By.XPATH,"//div[@id='droppable']")
# act.drag_and_drop(button_drag,button_drop).perform()

driver.get("https://www.jqueryscript.net/demo/Powerful-Range-Slider-Plugin-jQRangeSlider/demo/")
driver.maximize_window()
act=ActionChains(driver)

min_slider=driver.find_element(By.XPATH,"//div[@class='ui-rangeSlider ui-rangeSlider-withArrows']//div[@class='ui-rangeSlider-label ui-rangeSlider-leftLabel']")
max_slider=driver.find_element(By.XPATH,"//div[@class='ui-rangeSlider ui-rangeSlider-withArrows']//div[@class='ui-rangeSlider-label ui-rangeSlider-rightLabel']")
print(min_slider.location)
print(max_slider.location)

act.drag_and_drop_by_offset(min_slider,10,0).perform()
act.drag_and_drop_by_offset(min_slider,-90,0).perform()
print(min_slider.location)
print(max_slider.location)
