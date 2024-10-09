import re
from test_example.sync_api import Page, expect


def test_has_title(page: Page):
    # Navigate to the Playwright website
    page.goto("https://playwright.dev/")

    # Expect the title of the page to contain the substring "Playwright"
    expect(page).to_have_title(re.compile("Playwright"))


def test_get_started_link(page: Page):
    # Navigate to the Playwright website
    page.goto("https://playwright.dev/")

    # Click on the "Get started" link
    page.get_by_role("link", name="Get started").click()

    # Expect the page to have a heading with the name "Installation"
    expect(page.get_by_role("heading", name="installation")).to_be_visible()