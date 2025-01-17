from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import openpyxl

# Set up the WebDriver
driver = webdriver.Chrome()

# Navigate to the web page
driver.get("https://www.merriam-webster.com/")
driver.maximize_window()
time.sleep(5)
# Wait for the page to load
wait = WebDriverWait(driver, 10)

# Step 1: Click on the "SEE ALL WORDS OF THE DAY" link
try:
    driver.find_element(By.XPATH,
                        "//li[@class='d-none d-lg-flex position-relative me-xl-2 justify-content-between flex-column flex-lg-row']//a[@id='mw-global-nav-wod']").click()
    time.sleep(10)

    element = driver.find_element(By.LINK_TEXT, "SEE ALL WORDS OF THE DAY")

    # Scroll down to the element
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", element)

    # Optional: Wait to ensure the scrolling is complete
    time.sleep(1)

    # Click on the element
    element.click()
except Exception as e:
    print("Error clicking on the link:", e)



# Step 2: Wait for the words container to load and scroll to it
try:
    words_container = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "more-words-of-day-container")))
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'start' });", words_container)
except Exception as e:
    print("Error locating the words container:", e)


# Step 3: Fetch all words, dates, and definitions
words_data = []
try:

    words_items = words_container.find_elements(By.CSS_SELECTOR, "ul.more-wod-items li")

    for item in words_items:
        date = item.find_element(By.TAG_NAME, "h4").text
        word_element = item.find_element(By.TAG_NAME, "h2").find_element(By.TAG_NAME, "a")
        word = word_element.text

        # Click on the word link to go to the details page
        word_element.click()

        # Wait for the definition to load
        try:
            time.sleep(5)

            definition_paragraph = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "p"))
            )
            driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", definition_paragraph)
            definition = definition_paragraph.text
        except Exception as e:
            print(f"Error fetching definition for {word}: {e}")
            definition = "Definition not found"

        # Append data to the list
        words_data.append((date, word, definition))

        # Go back to the main page
        driver.back()

        # Re-locate the words container to proceed with the next word

        words_container = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "more-words-of-day-container")))
        words_items = words_container.find_elements(By.CSS_SELECTOR, "ul.more-wod-items li")
except Exception as e:
    print("Error processing words:", e)

# Step 4: Save the words to an Excel file
try:
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Words of the Day"
    sheet.append(["Date", "Word", "Definition"])  # Header row

    for word_entry in words_data:
        sheet.append(word_entry)

    workbook.save("Words_of_the_Day.xlsx")
    print("Words and definitions saved to 'Words_of_the_Day.xlsx'")
except Exception as e:
    print("Error saving to Excel:", e)

# Clean up
driver.quit()
