from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# Set up WebDriver
driver = webdriver.Chrome()  # Or the browser driver you're using
driver.get("https://www.google.com/maps")

# Wait for the page to load (adjust as needed)
driver.implicitly_wait(10)

# Perform a search
search_box = driver.find_element(By.XPATH, "//input[@id='searchboxinput']")
search_box.send_keys("ADIL PUBLIC SCHOOL,AHMADPUR EAST")  # Replace "School" with your search term
search_box.send_keys(Keys.RETURN)

# Wait for the results to appear
driver.implicitly_wait(10)  # You can replace this with an explicit wait for better results

# Locate all search results
search_results = driver.find_elements(By.XPATH, "//div[@role='article']")

# Iterate through the results


# Close the browser
driver.quit()
