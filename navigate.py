import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Open the URL
    url = 'https://www.google.com/maps/'
    print(f"Opening URL: {url}")
    driver.get(url)
    driver.maximize_window()

    # Wait for the search box to be present
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='searchboxinput']"))
    )

    # Search for "Hospital"
    search_box.send_keys("Hospital")
    search_box.send_keys(Keys.ENTER)

    # Wait for the search results to load
    time.sleep(5)

    # Function to scroll to the bottom of the page
    def scroll_to_bottom():
        last_height = driver.execute_script('return document.body.scrollHeight')
        while True:
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(2)  # Adjust if necessary

            new_height = driver.execute_script('return document.body.scrollHeight')
            if new_height == last_height:
                break
            last_height = new_height

    # Scroll to the bottom of the page
    scroll_to_bottom()

    # Additional wait time to observe the results
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()
