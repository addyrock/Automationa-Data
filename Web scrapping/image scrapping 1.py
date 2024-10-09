import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def download_google_images(search_query: str, number_of_images=500, download_path='downloads') -> None:
    '''Download google images with this function
       Takes -> search_query, number_of_images, download_path
       Returns -> None
    '''

    def scroll_to_bottom():
        '''Scroll to the bottom of the page'''
        last_height = driver.execute_script('return document.body.scrollHeight')
        while True:
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(2)
            new_height = driver.execute_script('return document.body.scrollHeight')
            try:
                element = driver.find_element(By.CSS_SELECTOR, '.YstHxe input')
                element.click()
                time.sleep(2)
            except NoSuchElementException:
                pass
            if new_height == last_height:
                break
            last_height = new_height

    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # Run headless Chrome
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')

    print("Initializing Chrome WebDriver")
    driver = webdriver.Chrome(service=service, options=options)
    url = 'https://images.google.com/'
    print(f"Opening URL: {url}")
    driver.get(url)

    try:
        # Wait for the page to fully load
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@name='q']")))
        search_box = driver.find_element(By.XPATH, "//input[@name='q']")
        print(f"Entering search query: {search_query}")
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.ENTER)
    except TimeoutException as e:
        print(f"Search box not found: {e}")
        driver.quit()
        return

    print("Scrolling to bottom to load all images")
    scroll_to_bottom()
    time.sleep(2)

    img_results = driver.find_elements(By.XPATH, "//img[contains(@class,'YQ4gaf')]")
    print(f'Total images found: {len(img_results)}')

    if not os.path.exists(download_path):
        os.makedirs(download_path)
        print(f"Created directory: {download_path}")

    count = 0

    for img_result in img_results:
        try:
            WebDriverWait(driver, 15).until(EC.element_to_be_clickable(img_result))
            img_result.click()
            time.sleep(2)

            actual_img = driver.find_element(By.XPATH, "//img[contains(@class,'cqUGgc')]")
            src = actual_img.get_attribute('src')

            if 'https://' in src:
                img_data = requests.get(src).content
                with open(os.path.join(download_path, f'image_{count + 1}.jpg'), 'wb') as handler:
                    handler.write(img_data)
                print(f'Downloaded image {count + 1}')
            else:
                print(f'Base64 image skipped {count + 1}')
        except ElementClickInterceptedException as e:
            print(f'Image not clickable: {e}')
        except Exception as e:
            print(f'An error occurred: {e}')

        count += 1
        if count >= number_of_images:
            break

    driver.quit()
    print("Download complete")


# # Example usage
# download_google_images('sunset', 10)