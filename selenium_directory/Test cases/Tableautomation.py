import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notification")

serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj,options=ops)

driver.get("https://testautomationpractice.blogspot.com/")
driver.get_screenshot_as_file("table.png")
noofrows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr"))
driver.get_screenshot_as_file("table.png")
noofcoloums=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr/th"))
driver.get_screenshot_as_file("table.png")
print(noofrows)
print(noofcoloums)

# driver.get("https://testautomationpractice.blogspot.com/")
data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr").text
print(len(data))
print(data)
# driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr/th")
data2=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[5]").text
print(data2)
print(len(data2))

for r in range(2,noofrows+1):
    for c in range(1,noofcoloums+1):
        data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data,end="        ")
    print()
driver.implicitly_wait(10)

