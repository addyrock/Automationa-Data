from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Open browser in maximized mode
chrome_options.add_argument("--disable-infobars")  # Disable the automation bar
chrome_options.add_argument("--disable-extensions")

driver_path = 'path_to_chromedriver'  # Specify path to ChromeDriver
service = Service(driver_path)

driver = webdriver.Chrome()
driver.get("https://firms.modaps.eosdis.nasa.gov/map/#d:24hrs;@0.0,0.0,3.0z")  # Replace with the actual URL
time.sleep(3)
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,"//div[@id='_disclaimer_ok']").click()
time.sleep(2)
location_click=driver.find_element(By.XPATH,"//button[@id='tatraLocation']//span//*[name()='svg']")
location_click.click()
time.sleep(5)
tab_click=driver.find_element(By.XPATH,"//div[@id='locator-tab-2']")
tab_click.click()
search_bar=driver.find_element(By.XPATH,"//input[@id='locator-search']")
search_bar.send_keys("Pakistan")
time.sleep(2)  # Short delay before pressing Enter
driver.find_element(By.XPATH,"//span[normalize-space()='Pakistan']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//div[@id='locatorClose-0']").click()
time.sleep(2)
for _ in range(3):
    driver.find_element(By.XPATH, "//button[@title='Zoom out']").click()
    time.sleep(10)  # Wait a bit between clicks to allow the map to zoom out

try:
    # Locate the canvas element
    canvas = driver.find_element(By.XPATH, "//canvas[@width='978' and @height='879']")

    # Perform an action on the canvas
    driver.execute_script("arguments[0].click();", canvas)
    print("Canvas element clicked!")

except Exception as e:
    print(f"Error: {str(e)}")
finally:
    driver.quit()