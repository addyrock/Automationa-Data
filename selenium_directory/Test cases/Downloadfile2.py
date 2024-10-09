from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)



driver.get("https://filesamples.com/formats/doc")
driver.maximize_window()

# Wait for the download link to be clickable
download_link = driver.find_element(By.XPATH, "//div[@class='output']//div[1]//a[1]")
download_link.click()
