import time
from playwright.sync_api import sync_playwright, expect


def highlight_and_blink_with_bg(page, selector, border_color="red", bg_color="yellow", times=3, interval=500):
    """Highlights an element with a border and background color, and makes it blink."""
    page.evaluate(
        f"""
        (async function() {{
            const element = document.querySelector("{selector}");
            if (element) {{
                const originalStyle = element.style.cssText;  // Save original styles
                for (let i = 0; i < {times}; i++) {{
                    element.style.border = "3px solid {border_color}";
                    element.style.backgroundColor = "{bg_color}";
                    await new Promise(resolve => setTimeout(resolve, {interval}));
                    element.style.border = "none";
                    element.style.backgroundColor = "transparent";
                    await new Promise(resolve => setTimeout(resolve, {interval}));
                }}
                element.style.cssText = originalStyle;  // Restore original styles
            }}
        }})();
        """
    )

def test_run(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=2000 )  # Launch the browser
    context = browser.new_context()
    page = context.new_page()

    # Start tracing
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page.goto("https://meripehchan.psca.gop.pk/")
    try:
        page.get_by_placeholder("Username").fill("admin")
        page.get_by_placeholder("Username").click()
        page.get_by_placeholder("Password").fill("123456")
        page.get_by_placeholder("Password").click()
        page.get_by_role("button", name="Login").click()
        page.get_by_role("link", name=" 1 To N Scan").click()
        page.get_by_role("link", name=" 1 To N Image").click()
        page.locator("select[name=\"RequestCode\"]").select_option("2")
        page.locator("#CategoryId").select_option("1")
        page.get_by_role("textbox").fill("test")
        page.get_by_role("textbox").click()
        page.get_by_role("button", name="Submit Request").click()
        expect(page.locator("#fingerprintError")).to_contain_text("At least one fingerprint scan is required!")


    # page.pause()


    except Exception as e:
        print(f"Error encountered: {e}")
    finally:
        # Stop tracing and save the trace to a file
        trace_path = "trace.zip"
        context.tracing.stop(path=trace_path)
        print(f"Trace saved to: {trace_path}")
        time.sleep(5)
    browser.close()


# Run the Playwright test
with sync_playwright() as playwright:
    test_run(playwright)
