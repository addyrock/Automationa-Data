import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load the Excel file
chrome_options = Options()
file_path = 'D:\\Arslan testing Data\\POIS.xlsx'  # Replace with your actual Excel file path
df = pd.read_excel(file_path)

# Set up Chrome options
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-software-rasterizer")
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
# chrome_options.add_argument('--headless')  # Uncomment if you want to run in headless mode

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()


# Open Google Maps
driver.get("https://www.google.com/maps")
time.sleep(3)  # Wait for the page to load

# Create a list to hold the data
address_data = []

# Iterate over each row in the Excel file
for index, row in df.iterrows():
    location_name = row['Location Name']
    city_name = row['City Name']

    try:
        # Find the search box and enter the location and city name
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "searchboxinput"))
        )
        search_box.clear()
        search_box.send_keys(f"{location_name}, {city_name}")
        search_box.send_keys(Keys.RETURN)

        # Wait for the address to appear
        address_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(@class, 'Io6YTe') and contains(@class, 'fontBodyMedium')]")
            )
        )
        # Extract the address text
        address = address_element.text.strip()

        # Extract the category information using the provided XPath
        try:
            category_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/span/span/button')
                )
            )
            category = category_element.text.strip()
        except Exception:
            category = "Category not found"

        # Extract the contact number using the provided XPath
        try:
            contact_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]/div[6]/button/div/div[2]/div[1]')
                )
            )
            contact_number = contact_element.text.strip()
        except Exception:
            contact_number = "Contact not found"

        print(f"Location: {location_name}, {city_name} - Address: {address}, Category: {category}, Contact: {contact_number}")

        # Append the location, address, category, and contact to the list
        address_data.append([location_name, city_name, address, category, contact_number])

    except Exception as e:
        print(f"Could not find information for {location_name}, {city_name}: {str(e)}")
        address_data.append([location_name, city_name, "Address not found", "Category not found", "Contact not found"])

    # Wait before processing the next row
    time.sleep(2)

# Create a DataFrame from the collected data
output_df = pd.DataFrame(address_data, columns=["Location Name", "City Name", "Address", "Category", "Contact Number"])

# Save the data to an Excel file
output_df.to_excel("extracted_addresses.xlsx", index=False)
print("Addresses, categories, and contact numbers saved to extracted_addresses.xlsx.")

# Close the browser after processing all locations
driver.quit()
