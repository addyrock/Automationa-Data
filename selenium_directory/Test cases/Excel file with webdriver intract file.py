import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Day24 import XLutility

serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver.maximize_window()

file="D:\\Arslan testing Data\\Testing Calculator.xlsx"
rows=XLutility.getRowCount(file,"Sheet1")

for r in range(2,rows+1):
    Principle=XLutility.readData(file,"Sheet1",r,1)
    RateofIntrest=XLutility.readData(file,"Sheet1",r,2)
    per1=XLutility.readData(file, "Sheet1", r, 3)
    per2=XLutility.readData(file, "Sheet1", r, 4)
    Frequency=XLutility.readData(file, "Sheet1", r, 5)
    exp_value=XLutility.readData(file, "Sheet1", r, 6)

    driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(Principle)
    driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(RateofIntrest)
    driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(per1)



    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@id='tenurePeriod']")))

    perioddrop=Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
    perioddrop.select_by_visible_text(per2)

    print("Selected period text:", per2)
    frequencydrop=Select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
    frequencydrop.select_by_visible_text(Frequency)
    print("Selected frequency drop:",frequencydrop)
    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[1]/img").click()
    act_value=driver.find_element(By.XPATH,"//span[@id='resp_matval']/strong").text
    driver.find_element(By.XPATH,"//*[@id ='fdMatVal']/div[2]/a[2]/img").click()

    # validation
    if float(exp_value)==float(act_value):
        print("Test Passed")
        XLutility.writeData(file,"Sheet1",r,8,"Passed")
        XLutility.fillGreenColor(file,"Sheet1",r,8)
    else:
        print("test failed")
        XLutility.writeData(file,"Sheet1",r,8,"Failed")
        XLutility.fillRedColor(file,"Sheet1",r,8)