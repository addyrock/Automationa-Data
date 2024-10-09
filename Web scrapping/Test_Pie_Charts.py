import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import matplotlib.pyplot as plt

# Global dictionary to store test results
test_results = {"passed": 0, "failed": 0}

@pytest.fixture(scope="module")
def setup():
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    # chrome_options.add_argument('--headless')  # Uncomment if you want to run in headless mode

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

def take_screenshot(driver, step_name):
    screenshot_path = f"{step_name}.png"
    driver.save_screenshot(screenshot_path)

def generate_pie_chart(pass_count, fail_count):
    labels = ['Passed', 'Failed']
    sizes = [pass_count, fail_count]
    colors = ['green', 'red']
    explode = (0.1, 0)  # explode the 1st slice

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Test Results')
    plt.savefig('test_results_pie_chart.png')
    plt.show()

def generate_bar_chart(pass_count, fail_count):
    labels = ['Passed', 'Failed']
    counts = [pass_count, fail_count]
    colors = ['green', 'red']

    plt.bar(labels, counts, color=colors)
    plt.xlabel('Test Status')
    plt.ylabel('Count')
    plt.title('Test Results')
    plt.savefig('test_results_bar_chart.png')
    plt.show()

def test_title_verification(setup):
    driver = setup
    driver.get("https://10.20.170.151/predictivepolicing/login.php")
    expected_title = "PREDICTIVE POLICING"
    actual_title = driver.title

    try:
        assert actual_title == expected_title, f"Test Failed: Title is '{actual_title}' but expected '{expected_title}'"
        test_results["passed"] += 1
    except AssertionError as e:
        test_results["failed"] += 1
        print(e)

    take_screenshot(driver, 'title_verification')

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call":
        if rep.failed:
            test_results["failed"] += 1
        elif rep.passed:
            test_results["passed"] += 1

def pytest_sessionfinish(session, exitstatus):
    # Generate charts at the end of the session
    generate_pie_chart(test_results["passed"], test_results["failed"])
    generate_bar_chart(test_results["passed"], test_results["failed"])
