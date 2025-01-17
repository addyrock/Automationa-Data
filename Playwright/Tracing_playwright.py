from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)  # Launch the browser
    context = browser.new_context()
    page = context.new_page()

