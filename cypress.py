import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Set up Selenium WebDriver
options = Options()
# Uncomment the line below to run Chrome in headless mode (without a UI)
# options.add_argument("--headless")
driver = webdriver.Chrome()
driver.maximize_window()

# Load the URLs from the Excel file
file_path = 'C:\\Users\\arslan.arif\\Desktop\\Criminal Pic for Testing\\ITMS_road_point_data.xlsx'  # Replace with your Excel file path
urls_df = pd.read_excel(file_path)

# Open Google Maps
driver.get("https://www.google.com/maps")
time.sleep(5)  # Wait for Google Maps to load

# Iterate over the URLs in the Excel file
for index, row in urls_df.iterrows():
    url = row['URL']

    # Navigate to the URL
    driver.get(url)

    # Wait for the map to load and traffic data to display
    time.sleep(10)  # Adjust based on your internet speed

    # Turn on the traffic layer
    try:

        traffic_button=driver.find_element(By.XPATH,"//img[@aria-label='Driving']")

        traffic_button.click()
        time.sleep(3)  # Wait for the traffic layer to load
    except Exception as e:
        print(f"Traffic layer button not found: {e}")

    # Take a screenshot of the map with the traffic data
    screenshot_path = f"screenshots/congestion_{index}.png"
    driver.save_screenshot(screenshot_path)

    print(f"Screenshot captured for URL: {url}")

    # Optionally wait before moving to the next URL
    time.sleep(2)

# Close the browser after processing all URLs
driver.quit()
