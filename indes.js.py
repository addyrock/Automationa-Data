from selenium import webdriver
import time

# Set up the driver (Make sure the path to your driver is correct)
driver = webdriver.Chrome()

# Open the first webpage
driver.get("https://www.google.com")
print("First tab title:", driver.title)
driver.maximize_window()

# Open a new tab by executing JavaScript (Bing)
driver.execute_script("window.open('https://www.bing.com', '_blank');")

# Give time to load the second tab
time.sleep(2)

# Get all open window handles
# tabs = driver.window_handles
#
# # Switch to the second tab (Bing)
# driver.switch_to.window(tabs[1])
# print("Second tab title:", driver.title)

# Open another new tab by executing JavaScript (Playwright Documentation)
AWS=driver.execute_script("window.open('https://playwright.dev/docs/ci-intro', '_blank');")
print(driver.title)
# Give time to load the third tab
time.sleep(2)

# Get updated window handles
# tabs = driver.window_handles
#
# # Switch to the third tab (Playwright Docs)
# driver.switch_to.window(tabs[2])
# print("Third tab title:", driver.title)

# Open a new tab with Selenium Documentation
driver.execute_script("window.open('https://www.selenium.dev/selenium/docs/api/py/', '_blank');")

# Give time to load the fourth tab
time.sleep(2)

# Get updated window handles
tabs = driver.window_handles

# Switch to the fourth tab (Selenium Docs)
# driver.switch_to.window(tabs[3])
# print("Fourth tab title:", driver.title)

# Optionally, switch back to the first tab (Google)
driver.switch_to.window(tabs[0])
print("Switched back to first tab title:", driver.title)

# Pause to see the result before closing
time.sleep(5)

# Close the browser
driver.quit()
