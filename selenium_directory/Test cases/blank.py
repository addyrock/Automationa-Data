import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Initialize WebDriver
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# Open the page with marquee element
driver.get("https://www.w3schools.com/html/html_marquee_tag.asp")

# Locate the marquee element
marquee_element = driver.find_element(By.TAG_NAME, "marquee")

# Scroll to the marquee element using JavaScript
driver.execute_script("arguments[0].scrollIntoView();", marquee_element)
time.sleep(2)  # Wait for the element to stabilize (optional)

# Perform mouse hover action on the marquee element
action = ActionChains(driver)
action.move_to_element(marquee_element).perform()

# Example: Click on a link within the marquee
link_element = marquee_element.find_element(By.TAG_NAME, "a")
link_text = link_element.text
link_element.click()

# Take a screenshot or perform other actions as needed
driver.save_screenshot("marquee_hover.png")

# Close the browser session
driver.quit()
