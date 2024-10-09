import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

# define function for taking screenshot
def take_screenshot(step_name):
    driver.save_screenshot(f"{step_name}.png")

driver.get("http://10.20.10.137:800/")
driver.maximize_window()
time.sleep(2)
take_screenshot("after_navigation")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='txtLoginName']").send_keys("547-2016-6103")
take_screenshot("after_entering_username")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='txtPassword']").send_keys("35202-3476111-5")
take_screenshot("after_entering_password")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='btnLogin']").click()
take_screenshot("after_clicking_login")
time.sleep(2)
# driver.find_element(By.XPATH,"//li[@id='LiAppraisal']//a[@class='dropdown-toggle']").click()
# take_screenshot("after_appraisal_dropdown")
# time.sleep(2)
# driver.find_element(By.XPATH,"//a[normalize-space()='Appraisal Employee']").click()
# take_screenshot("after_appraisal_employee")
# time.sleep(2)
# driver.find_element(By.XPATH,"//span[normalize-space()='Roster Management']").click()
# take_screenshot("after_roster_management")
# time.sleep(2)
# driver.find_element(By.XPATH,"//a[normalize-space()='Off Adjustment']").click()
# take_screenshot("after_off_adjustment")
# time.sleep(2)
# driver.find_element(By.XPATH,"//li[@id='LiLeave']//a[@class='dropdown-toggle']").click()
# take_screenshot("after_leave_dropdown")
# time.sleep(2)
# driver.find_element(By.XPATH,"//span[normalize-space()='Leave Request']").click()
# take_screenshot("after_leave_dropdown")
# driver.find_element(By.XPATH,"//li[@id='LiInsuranceM']//a[@class='dropdown-toggle']//span[@class='menu-text']").click()
# take_screenshot("after_insurance_request")
# time.sleep(2)
# driver.find_element(By.XPATH,"//span[normalize-space()='Insurance Request']").click()
# take_screenshot("after_insurance_request")
# time.sleep(2)
# driver.find_element(By.XPATH,"//li[@id='LiVehicleRequisition']//a[@class='dropdown-toggle']//span[@class='menu-text']").click()
# take_screenshot("after_vehicle_requisition_dropdown")
# time.sleep(2)
# driver.find_element(By.XPATH,"//span[normalize-space()='Vehicle Requisition Form']").click()
# take_screenshot("after_vehicle_requisition_form")
# time.sleep(2)
# driver.find_element(By.XPATH,"//li[@id='LiReportIssue']//a[@class='dropdown-toggle']//span[@class='menu-text']").click()
# take_screenshot("after_report_issue_dropdown")
# time.sleep(2)
# driver.find_element(By.XPATH,"//a[@href='ReportIssue.aspx']").click()
# take_screenshot("after_report_issue_2")
# time.sleep(2)
driver.find_element(By.XPATH,"//span[normalize-space()='Knowledge Base']").click()
take_screenshot("Knowlwdge base")
time.sleep(2)
driver.find_element(By.XPATH,"//li[1]//h5[1]//a[1]//i[1]").click()
take_screenshot("Knowlwdge base")
time.sleep(10)
# driver.switch_to.default_content()
# time.sleep(2)







# total number of links
# links=driver.find_elements(By.TAG_NAME,"a")
# print(len(links))
