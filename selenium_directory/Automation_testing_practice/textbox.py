import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

def test_automation():
    driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Muhammad Arslan Arif Gorssi")
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@id='email']").send_keys("addyrock680@gmail.com")
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@id='phone']").send_keys("03226496719")
    time.sleep(1)
    driver.find_element(By.XPATH,"//textarea[@id='textarea']").send_keys("house # 1 ,Chouhdry street Gunjh Bukhsh road ichra lahore")
    time.sleep(1)
    radio1=driver.find_element(By.XPATH,"//label[normalize-space()='Male']")
    radio1.click()
    time.sleep(1)
    radio2=driver.find_element(By.XPATH,"//label[normalize-space()='Female']")
    radio2.click()
    time.sleep(1)
    checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
    for checkbox in checkboxes:
        checkbox.click()
        time.sleep(1)

    # checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
    # for checkbox in checkboxes:
    #  if checkbox.is_selected():
    #      checkbox.click()
    #      time.sleep(1)

    dropdown = Select(driver.find_element(By.ID,"country"))
    time.sleep(1)
    dropdown.select_by_index(0)
    time.sleep(1)
    dropdown.select_by_index(1)
    time.sleep(1)
    dropdown.select_by_index(2)
    time.sleep(1)
    dropdown.select_by_index(3)
    time.sleep(1)
    dropdown.select_by_index(4)
    time.sleep(1)
    dropdown.select_by_index(5)
    time.sleep(1)
    dropdown.select_by_index(6)
    time.sleep(1)
    dropdown.select_by_index(7)
    time.sleep(1)
    dropdown.select_by_index(8)
    time.sleep(1)
    dropdown.select_by_index(9)
    time.sleep(1)

    dropdown = Select(driver.find_element(By.ID, "colors"))
    dropdown.select_by_index(0)
    dropdown.deselect_by_index(0)
    time.sleep(1)
    dropdown.select_by_index(1)
    dropdown.deselect_by_index(1)
    time.sleep(1)
    dropdown.select_by_index(2)
    dropdown.deselect_by_index(2)
    time.sleep(1)
    dropdown.select_by_index(3)
    dropdown.deselect_by_index(3)
    time.sleep(1)
    dropdown.select_by_index(4)
    dropdown.deselect_by_index(4)
    time.sleep(1)

    driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
    time.sleep(1)

    driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("04/05/2024")



    # driver.execute_script("window.open('link_element');")
    # link_element=driver.find_element(By.XPATH,"//a[normalize-space()='open cart']").click()
    # driver.switch_to.window(driver.window_handles[1])

    time.sleep(1)
    driver.execute_script("window.open('https://demo.opencart.com/');")
    # driver.find_element(By.XPATH,"//a[normalize-space()='open cart']").click()
    driver.switch_to.window(driver.window_handles[1])

    driver.switch_to.window(driver.window_handles[0])



    time.sleep(1)
    driver.execute_script("window.open('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login');")
    # driver.find_element(By.XPATH,"//a[normalize-space()='open cart']").click()
    driver.switch_to.window(driver.window_handles[2])

    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[normalize-space()='Home']").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//a[normalize-space()='Posts (Atom)']").click()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    driver.find_element(By.XPATH,"//body[1]/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[4]/input[1]").click()

    pages=driver.find_elements(By.XPATH,"//ul[@id='pagination']")
    for page in pages:
         page.click()


# driver.switch_to.window(driver.window_handles[1])
#
# driver.switch_to.window(driver.window_handles[0])





# driver.switch_to.new_window('tab')
# driver.execute_script("window.open('');")
# driver.switch_to.window(driver.window_handles[1])
# driver.implicitly_wait(10)



















# define function for taking screenshot
# def take_screenshot(step_name):
#     driver.save_screenshot(f"{step_name}.png")

# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
#
# checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
# print(len('checkbox'))
#
# time.sleep(1)
# for checkbox in checkboxes:
#   if checkbox.is_selected():
#      checkbox.click()
#






# for checkbox in checkboxes:
#     checkbox.click()
# # #
# #
# # time.sleep(1)
#
# if checkbox.is_selected():
#      checkbox.click()
# for checkbox in checkboxes:
#     weekname = checkbox.get_attribute('id')
#     if weekname == 'monday' or weekname == 'friday':
#      checkbox.click()

# for checkbox in checkboxes:
#     weekname= checkbox.get_attribute('id')
#     if weekname == 'monday' or weekname == 'friday' or weekname =='Saturday' or weekname=='tuesday':
#         checkbox.click()
#
# for i in range(len(checkboxes)-2,len('checkboxes')):
#          checkboxes[i].click()

# for i in range(len(checkboxes)):
#     if i<7:
#         checkboxes[i].click()

# country= driver.find_elements(By.XPATH,"//label[normalize-space()='Country:']")


#
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By
# import time

