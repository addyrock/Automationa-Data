from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import openpyxl

# Set up the WebDriver
driver = webdriver.Chrome()

# Navigate to the Merriam-Webster Word of the Day page
driver.get("https://www.merriam-webster.com/")
driver.maximize_window()
time.sleep(5)

wait = WebDriverWait(driver, 10)
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

# Initialize Excel Workbook
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Words of the Day"
sheet.append(["Date", "Word", "Definition", "Noun", "Pronunciation"])  # Header row

words_data = []

try:
    # Find the container for all months
    months = driver.find_elements(By.CLASS_NAME, "more-words-of-day-container")

    for month_index, month in enumerate(months):
        # Expand month if toggle is available
        try:
            toggle_trigger = month.find_element(By.CLASS_NAME, "toggle-trigger")
            if toggle_trigger.is_displayed():
                driver.execute_script("arguments[0].click();", toggle_trigger)
                time.sleep(2)
        except Exception:
            print(f"No toggle trigger found or not required for month index {month_index}.")

        # Re-fetch days in the current month after potential toggle
        days = month.find_elements(By.CSS_SELECTOR, "ul.more-wod-items li")

        for day_index in range(len(days)):
            days = month.find_elements(By.CSS_SELECTOR, "ul.more-wod-items li")  # Re-fetch elements
            day = days[day_index]

            # Scroll to the day item and ensure visibility
            driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", day)
            time.sleep(1)

            # Extract date and word details
            date = day.find_element(By.TAG_NAME, "h4").text
            word_element = day.find_element(By.TAG_NAME, "h2").find_element(By.TAG_NAME, "a")
            word = word_element.text

            # Click the word to open details
            try:
                driver.execute_script("arguments[0].click();", word_element)
            except Exception as e:
                print(f"Error clicking word {word}: {e}")
                continue

            # Wait for the details page to load
            try:
                definition = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "p"))).text
            except Exception:
                definition = "Definition not found"

            try:
                noun = driver.find_element(By.CSS_SELECTOR, "span.main-attr").text
            except Exception:
                noun = "Noun not found"

            try:
                pronunciation = driver.find_element(By.CSS_SELECTOR, "span.word-syllables").text
            except Exception:
                pronunciation = "Pronunciation not found"

            # Append data to the list
            words_data.append((date, word, definition, noun, pronunciation))

            # Navigate back to the archive page
            driver.back()
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "wod-archive-box")))  # Wait for reload

except Exception as e:
    print("Error processing words:", e)

finally:
    # Save the words to an Excel file
    try:
        for word_entry in words_data:
            sheet.append(word_entry)
        workbook.save("Words_of_the_Day_All_Months.xlsx")
        print("Words and definitions saved to 'Words_of_the_Day_All_Months.xlsx'")
    except Exception as e:
        print("Error saving to Excel:", e)

    # Clean up
    driver.quit()
