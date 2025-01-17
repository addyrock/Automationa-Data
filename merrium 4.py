from selenium import webdriver
from selenium.webdriver.common.by import By
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

# Step 2: Wait for the words container to load
try:
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "more-words-of-day-container")))
except Exception as e:
    print("Error locating the words container:", e)

# Step 3: Fetch all words, dates, definitions, noun, and pronunciation
words_data = []
try:
    while True:
        # Re-fetch the container and its items to avoid stale references
        words_container = driver.find_element(By.CLASS_NAME, "more-words-of-day-container")
        words_items = words_container.find_elements(By.CSS_SELECTOR, "ul.more-wod-items li")

        for i in range(len(words_items)):
            # Re-fetch the individual item to avoid stale references
            words_items = driver.find_elements(By.CSS_SELECTOR, "ul.more-wod-items li")
            item = words_items[i]

            # Scroll to the item
            driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", item)
            time.sleep(2)

            # Extract details
            date = item.find_element(By.TAG_NAME, "h4").text
            word_element = item.find_element(By.TAG_NAME, "h2").find_element(By.TAG_NAME, "a")
            word = word_element.text

            # Click on the word link to go to the details page
            word_element.click()

            # Wait for the definition, noun, and pronunciation to load


            # Fetch the noun
            try:
                noun_element = driver.find_element(By.CSS_SELECTOR, "span.main-attr")
                noun = noun_element.text
            except Exception:
                noun = "Noun not found"

            # Fetch the pronunciation
            try:
                pronunciation_element = driver.find_element(By.CSS_SELECTOR, "span.word-syllables")
                pronunciation = pronunciation_element.text
            except Exception:
                pronunciation = "Pronunciation not found"
            try:
                time.sleep(5)
                definition_paragraph = wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "p"))
                )
                driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });",
                                      definition_paragraph)
                definition = definition_paragraph.text
            except Exception as e:
                print(f"Error fetching definition for {word}: {e}")
                definition = "Definition not found"
            # Append data to the list
            words_data.append((date, word, definition, noun, pronunciation))

            # Go back to the main page
            driver.back()
            time.sleep(5)  # Wait for the main page to reload

        break  # Remove this line if there are multiple pages to process
except Exception as e:
    print("Error processing words:", e)

# Step 4: Save the words to an Excel file
try:
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Words of the Day"
    sheet.append(["Date", "Word", "Definition", "Noun", "Pronunciation"])  # Updated header row

    for word_entry in words_data:
        sheet.append(word_entry)

    workbook.save("Words_of_the_Day.xlsx")
    print("Words and definitions saved to 'Words_of_the_Day.xlsx'")
except Exception as e:
    print("Error saving to Excel:", e)

# Clean up
driver.quit()
