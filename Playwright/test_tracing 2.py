import time
from playwright.sync_api import sync_playwright, expect


def test_run(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)  # Launch the browser
    context = browser.new_context()
    page = context.new_page()

    # Start tracing
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page.goto("https://www.w3schools.com/python/trypython.asp?filename=demo_default", timeout=90000)
    try:
        print("Pausing the script for debugging. Press Resume in Playwright Inspector to continue.")
        page.locator(".CodeMirror-scroll").click()
        page.get_by_role("textbox").press("Control+a")
        page.get_by_role("textbox").fill("Hello world")
        page.get_by_role("textbox").press("Control+a")
        page.get_by_role("textbox").press("Control+c")
        page.locator("#iframeResult").click()
        page.get_by_text("Hello, World!", exact=True).click()
        page.get_by_text("Hello, World!", exact=True).click()
        page.locator(".CodeMirror-lines").click()

    except Exception as e:
        print(f"Error encountered: {e}")
    finally:
        # Stop tracing and save the trace to a file
        trace_path = "trace.zip"
        context.tracing.stop(path=trace_path)
        print(f"Trace saved to: {trace_path}")
    browser.close()


# Run the Playwright test
with sync_playwright() as playwright:
    test_run(playwright)
