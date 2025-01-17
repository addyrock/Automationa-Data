import requests
def test_sql_injection():
    url = "https://example.com/api/user"
    params = {"id": "12345' OR '1'='1"}
    response = requests.get(url, params=params)
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    print("Test passed: SQL injection protection")


test_sql_injection()