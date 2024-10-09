from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver
driver = webdriver.Chrome()

url = "https://testautomationpractice.blogspot.com/"
driver.get(url)
driver.maximize_window()

# Find the link element
link_element = driver.find_element(By.XPATH, "//a[normalize-space()='open cart']")

# Execute JavaScript to open the link in a new tab
driver.execute_script("window.open(arguments[0].getAttribute('href'), '_blank');", link_element)

# Close the WebDriver
driver.quit()