import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome()as driver:
    # Open URL
    driver.get("https://seleniumhq.github.io")

    # Setup wait for later
    wait = WebDriverWait(driver, 10)

    # Store the ID of the original window
    original_window = driver.current_window_handle

    # Check we don't have other windows open already
    assert len(driver.window_handles) == 1

    # Click the link which opens in a new window
    driver.find_element(By.LINK_TEXT, "About Selenium").click()

    # Wait for the new window or tab
    wait.until(EC.number_of_windows_to_be(2))

    # Loop through until we find a new window handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    # Wait for the new tab to finish loading content
    wait.until(EC.title_is("SeleniumHQ Browser Automation"))
# def test_forward_click_ab(driver):
#     driver.get("https://www.geeksforgeeks.org/")
#     print(driver.title)
#     assert driver.title=="GeeksforGeeks | A computer science portal for geeks"
#     test_forward_click_ab()
# iframe = driver.find_element(By.XPATH, "//a[@href='https://www.geeksforgeeks.org/c-plus-plus/?ref=footer']")
# ActionChains(driver) \
#     .scroll_to_element(iframe) \
#     .perform()
# print(driver.page_source)
# print(driver.current_url)
# print(driver.current_window_handle)
# print(driver.get_screenshot_as_file("U there.png"))

# driver.set_window_position(1024, 1024, windowHandle ='current')
# print(driver.get_screenshot_as_file("hi.png"))
# print(driver.get_window_rect())
# driver.set_script_timeout(2)
# print(driver.get_log("browser"))

# print(driver.get_window_position(windowHandle='current'))
# get geeksforgeeks.org
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.get_log("browser")
# print(driver.get_cookies())
# one step forward in browser history
# driver.back()
# driver.forward()
# driver.fullscreen_window()