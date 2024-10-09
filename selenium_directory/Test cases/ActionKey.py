#import webdriver
from selenium import webdriver

# import Action chains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Chrome()

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# get element
element=driver.find_element(By.XPATH, "//span[normalize-space()='Courses']").click()

# create action chain object
action = ActionChains(driver)

# click the item
action.click(on_element=element)

# perform the operation
action.perform()