# import time
# from playwright.sync_api import sync_playwright
#
# with sync_playwright() as p:
#     # First browser instance (non-headless mode)
#     browser = p.chromium.launch(headless=False)
#     page1 = browser.new_page()
#     page1.goto("https://google.com")
#     print("First tab opened with Google in non-headless mode!")
#     time.sleep(5)
#
#     # Open a new tab in the same browser instance
#     page2 = browser.new_page()
#     page2.goto("https://google.com")
#     print("Second tab opened with Google in the same browser instance!")
#     time.sleep(5)
#
#     browser.close()
# import time
# from playwright.sync_api import sync_playwright
#
# with sync_playwright() as p:
#     # Launch the browser in non-headless mode
#     browser = p.chromium.launch(headless=False)
#
#     # Open the first tab and navigate to Google
#     context = browser.new_context()  # Create a browser context to manage tabs
#     page1 = context.new_page()
#     page1.goto("https://google.com")
#     print("First tab opened with Google in non-headless mode!")
#     time.sleep(5)
#
#     # Open a second tab in the same browser window and navigate to Google
#     page2 = context.new_page()
#     page2.goto("https://google.com")
#     print("Second tab opened with Google in the same browser window!")
#     time.sleep(5)
#     page2.click("//textarea[@id='APjFqb']")
#     page2.fill("//textarea[@id='APjFqb']","Python Tutorial")
#     page2.keyboard.press("Enter")
#     # Close the browser
#     browser.close()

# import time
# from playwright.sync_api import sync_playwright
#
# with sync_playwright() as p:
#     # Launch the browser in non-headless mode
#     browser = p.chromium.launch(headless=False)
#
#     # Open the first tab and navigate to Google
#     context = browser.new_context()  # Create a browser context to manage tabs
#     page1 = context.new_page()
#     page1.goto("https://google.com")
#     print("First tab opened with Google in non-headless mode!")
#     time.sleep(5)
#
#     # Open a second tab in the same browser window and navigate to Google
#     page2 = context.new_page()
#     page2.goto("https://google.com")
#     print("Second tab opened with Google in the same browser window!")
#
#     # Wait for the search box to be visible before interacting
#     page2.wait_for_selector("input[name='q']", timeout=5000)  # Wait for the search box to be ready
#
#     # Click and fill the search box
#     page2.fill("input[name='q']", "Python Tutorial")
#     page2.keyboard.press("Enter")  # Press Enter key to initiate search
#
#     time.sleep(5)  # Wait to observe the search results
#
#     # Close the browser
#     browser.close()

import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch the browser in non-headless mode
    browser = p.chromium.launch(headless=False)

    # Open the first tab and navigate to Google
    context = browser.new_context()  # Create a browser context to manage tabs
    page1 = context.new_page()
    page1.goto("https://google.com", wait_until="load")  # Wait until the page fully loads
    print("First tab opened with Google in non-headless mode!")
    time.sleep(5)

    # Open a second tab in the same browser window and navigate to Google
    page2 = context.new_page()
    page2.goto("https://google.com", wait_until="load")  # Ensure the page is loaded
    print("Second tab opened with Google in the same browser window!")

    # Wait for the search box to be visible before interacting
    page2.wait_for_selector("input[name='q']", timeout=10000)  # Wait for the search box to be ready

    # Click and fill the search box
    page2.fill("input[name='q']", "Python Tutorial")
    page2.keyboard.press("Enter")  # Press Enter key to initiate search

    time.sleep(5)  # Wait to observe the search results

    # Close the browser
    browser.close()

