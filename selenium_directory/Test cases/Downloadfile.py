from appium.webdriver.extensions import location
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
location=os.getcwd()

def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    serv_obj = Service("C:\Driver")

    # preferences ={"download.defualt_directory":location}
    ops = webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/msword")
    ops.set_preference("browser.download.manager.shownWhenStarting",False)
    driver = webdriver.Firefox(service=serv_obj,options=ops)
    return driver

driver=firefox_setup()

driver.get("https://filesamples.com/formats/doc")
driver.maximize_window()
driver.find_element(By.XPATH,"//div[@class='output']//div[1]//a[1]").click()
