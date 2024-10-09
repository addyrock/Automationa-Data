import time
import re
import pyperclip
import csv
import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait

# Setup Chrome driver
service = Service()
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

# CSV file path
csv_file_path = 'location_data.csv'


# Define a function to perform the search and data extraction
def search_and_extract_data(location_name):
    try:
        # Navigate to Google Maps
        driver.get("https://www.google.com/maps")
        driver.maximize_window()
        time.sleep(5)

        # Search for the location
        search_box = driver.find_element(By.XPATH, "//input[@id='searchboxinput']")
        search_box.clear()
        search_box.send_keys("park")
        time.sleep(2)

        search_button = driver.find_element(By.XPATH, "//button[@id='searchbox-searchbutton']")
        search_button.click()
        time.sleep(5)

        # Implement scrolling logic
        scrollable_div = driver.find_element(By.CSS_SELECTOR, 'div[role="feed"]')
        driver.execute_script("""
            var scrollableDiv = arguments[0];
            function scrollWithinElement(scrollableDiv) {
                return new Promise((resolve, reject) => {
                    var totalHeight = 0;
                    var distance = 1000;
                    var scrollDelay = 3000;

                    var timer = setInterval(() => {
                        var scrollHeightBefore = scrollableDiv.scrollHeight;
                        scrollableDiv.scrollBy(0, distance);
                        totalHeight += distance;

                        if (totalHeight >= scrollHeightBefore) {
                            totalHeight = 0;
                            setTimeout(() => {
                                var scrollHeightAfter = scrollableDiv.scrollHeight;
                                if (scrollHeightAfter > scrollHeightBefore) {
                                    return;
                                } else {
                                    clearInterval(timer);
                                    resolve();
                                }
                            }, scrollDelay);
                        }
                    }, 200);
                });
            }
            return scrollWithinElement(scrollableDiv);
        """, scrollable_div)
        time.sleep(10)  # Adjust the sleep time as needed to ensure scrolling is complete

        # Find all search results after scrolling
        search_results = driver.find_elements(By.XPATH, "//a[@class='hfpxzc']")

        # Open the CSV file for writing
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Write the header
            writer.writerow(
                ["Category", "Locality", "Location", "Phone Number/Website", "Phone Number/Website", "Latitude",
                 "Longitude"])

            # Loop through each search result
            for result in search_results:
                try:
                    # Scroll the element into view
                    driver.execute_script("arguments[0].scrollIntoView(true);", result)
                    # Wait until the element is clickable
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(result))
                    # Click on the search result
                    result.click()
                    time.sleep(5)  # Adjust the sleep time as needed

                    # If specific_span is found, click it
                    specific_span = driver.find_element(By.XPATH, "//span[@class='Cw1rxd google-symbols G47vBd SwaGS']")
                    specific_span.click()
                    time.sleep(5)  # Adjust the sleep time as needed

                    # Find the h1 element by class name
                    h1_element = driver.find_element(By.CLASS_NAME, "DUwDvf")
                    # Get the text of the h1 element
                    h1_text = h1_element.text
                    print("Locality Name:", h1_text)

                    # Get text from clipboard
                    clipboard_text = pyperclip.paste()
                    print("Location:", clipboard_text)

                    # Extract the Phone number from the first div element
                    Phone_elements = driver.find_elements(By.CSS_SELECTOR, '.Io6YTe.fontBodyMedium.kR99db')
                    if Phone_elements:
                        Phone1_div_text = Phone_elements[1].text
                        Phone2_div_text = Phone_elements[2].text
                        # Print the phone number text
                        print("Phone Number/Website:", Phone1_div_text, "/", Phone2_div_text)
                    else:
                        print("No elements found with the given class names.")

                        # Get the current URL
                    current_url = driver.current_url
                    print("Current URL:", current_url)

                    # Extract latitude and longitude
                    latitude, longitude = None, None
                    matches = re.findall(r'3d([-+]?\d+\.\d+).*?4d([-+]?\d+\.\d+)', current_url)
                    if matches:
                        for match in matches:
                            latitude = match[0]  # Latitude from '3d'
                            longitude = match[1]  # Longitude from '4d'
                            print("Latitude extracted between '3d' and '!':", latitude)
                            print("Longitude extracted between '4d' and '!':", longitude)
                    else:
                        print("No specific values found in the URL.")
                    # Write data to the CSV file
                    writer.writerow(
                        [location_name, h1_text, clipboard_text, Phone1_div_text, Phone2_div_text, latitude, longitude])

                except ElementClickInterceptedException:
                    print("Element click intercepted, trying to click again...")
                    time.sleep(2)
                    driver.execute_script("arguments[0].click();", result)

    except NoSuchElementException as e:
        print("An element was not found:", e)
    except ConnectionResetError as e:
        print("Connection was reset. Retrying...", e)
        time.sleep(5)
        search_and_extract_data(location_name)  # Retry the function

    finally:
        driver.quit()


# Define the function to be called when the button is clicked
def on_search_button_click():
    location_name = location_entry.get()
    search_and_extract_data(location_name)
    messagebox.showinfo("Done", "Data extraction is complete.")


# Create the main window
root = tk.Tk()
root.title("Location Data Extractor")

# Create and place the label and entry widget
location_label = tk.Label(root, text="Enter Location Name:")
location_label.pack(pady=10)

location_entry = tk.Entry(root, width=50)
location_entry.pack(pady=10)

# Create and place the search button
search_button = tk.Button(root, text="Search", command=on_search_button_click)
search_button.pack(pady=20)

# Run the application
root.mainloop()


