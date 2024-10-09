from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

# Path to your ChromeDriver executable
 # Replace with the actual path to your chromedriver

driver = webdriver.Chrome()

try:
    # Open the target URL
    driver.get("https://the-internet.herokuapp.com/upload")
    driver.maximize_window()

    # Assert the title of the page
    assert "The Internet" in driver.title, "Title does not match"

    # Assert the URL of the current page
    assert driver.current_url == "https://the-internet.herokuapp.com/upload", "URL does not match"

    # Wait until the file input element is present and interactable
    file_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "file-upload"))
    )

    # Assert that the file input element is present
    assert file_input is not None, "File input element not found"

    # Specify the file path correctly
    file_path = "C:\\Users\\arslan.arif\\Downloads\\Arslan Arif CV (Sr.Software Quailty Engineer.pdf"  # Replace with your actual file path

    # Upload the file by sending the file path to the input field
    file_input.send_keys(file_path)

    # Wait until the upload button is present and clickable, then click it
    upload_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "file-submit"))
    )
    upload_button.click()

    # Wait for the upload result to be visible
    upload_result = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h3[text()='File Uploaded!']"))
    )

    # Assert the presence of the success message
    assert upload_result is not None, "Upload result message not found"

    # Assert the text of the success message
    assert upload_result.text == "File Uploaded!", "Upload result text does not match"

    print("All assertions passed. File uploaded successfully.")

finally:
    # Close the browser
    driver.quit()
