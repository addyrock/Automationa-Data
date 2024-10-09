
from selenium import webdriver
from urllib.parse import urlparse
import requests
from selenium.webdriver.common.by import By

# Define the URL of the web page you want to check
URL = "http://www.softwaretestingmaterial.com"

# Initialize the WebDriver
driver = webdriver.Chrome()  # Replace with the appropriate WebDriver
driver.get(URL)

# Collect all the links in the web page based on the <a> tag
links = driver.find_elements(By.LINK_TEXT,"href")

# Initialize a list to store the broken links
broken_links = []

# Iterate through each link and send an HTTP request to check its validity
for link in links:
    href = link.get_attribute("href")

    if href:
        parsed_href = urlparse(href)

        if parsed_href.scheme and parsed_href.netloc:
            try:
                response = requests.get(href)

                if response.status_code >= 400:
                    broken_links.append(href)
            except requests.exceptions.RequestException:
                broken_links.append(href)

# Print or handle the broken links as needed
print("Broken Links:")
for link in broken_links:
    print(link)

# Close the WebDriver
driver.quit()