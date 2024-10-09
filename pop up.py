import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_interact_with_modal(setup):
    driver = setup
    driver.get("http://10.22.16.115/")

    # Trigger the modal (assuming there's a button to open the modal)
    open_modal_button = driver.find_element(By.XPATH, "//button[@id='open-modal-button']")
    open_modal_button.click()

    # Wait for the modal to appear
    modal = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'modal-content'))
    )

    # Interact with the modal elements
    modal.find_element(By.NAME, "name").send_keys("Test Subtask Name")
    modal.find_element(By.NAME, "description").send_keys("Test Subtask Description")
    modal.find_element(By.NAME, "estimated_time").send_keys("2")

    status_dropdown = modal.find_element(By.NAME, "status")
    select = Select(status_dropdown)
    select.select_by_visible_text("In Progress")

    # Submit the form inside the modal
    submit_button = modal.find_element(By.XPATH, "//button[@type='submit' and text()='Add']")
    submit_button.click()

    # Verify the submission was successful (depends on what happens after submission)
    # Example: checking for a success message
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'success-message'))
    )
    assert success_message.is_displayed(), "Success message not displayed"

    print("Modal Form Interaction Test Passed")

# Run the test with:
# pytest -v test_modal_form_interaction.py
