import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    return driver


def download_images(driver, save_folder, num_images=20):
    # Wait for the images to load
    time.sleep(3)

    # Get all the image elements
    images = driver.find_elements(By.CSS_SELECTOR, ".rg_i")

    # Ensure we have at most `num_images` images
    images = images[:num_images]

    # Create the folder if it doesn't exist
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # Download each image
    for i, image in enumerate(images):
        # Click on the image to open the preview
        driver.execute_script("arguments[0].scrollIntoView(true);", image)
        driver.execute_script("arguments[0].click();", image)
        time.sleep(2)

        # Find the image URL
        image_url = driver.find_element(By.CSS_SELECTOR, ".n3VNCb").get_attribute("src")

        # Download the image
        response = requests.get(image_url)
        image_path = os.path.join(save_folder, f"fawad_khan_{i+1}.png")
        with open(image_path, "wb") as image_file:
            image_file.write(response.content)

        print(f"Downloaded image {i+1}/{num_images}")

        # Close the preview
        driver.find_element(By.CSS_SELECTOR, ".TVtLec").click()
        time.sleep(2)


def main():
    # Set up the driver
    driver = setup_driver()

    # Navigate to Google Images
    driver.get("https://www.google.com/imghp")

    # Search for "Fawad Khan"
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Fawad Khan")
    search_box.send_keys(Keys.RETURN)

    # Click on "Images" tab
    images_tab = driver.find_element(By.XPATH, "//a[contains(@href, 'tbm=isch')]")
    images_tab.click()

    # Download the images
    download_images(driver, "fawad_khan_images", num_images=20)

    # Close the driver
    driver.quit()


if __name__ == "__main__":
    main()
