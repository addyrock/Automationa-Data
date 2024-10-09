
def test_title_verification(setup):
    driver = setup
    driver.get("http://10.22.16.115/")
    expected_title = "PSCA | Log "
    actual_title = driver.title
    assert actual_title == expected_title, f"Test Failed: Title is '{actual_title}' but expected '{expected_title}'"
