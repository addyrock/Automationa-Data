import requests
import pytest
# Base URL of the API (replace with your actual API endpoint)
base_url = "https://jsonplaceholder.typicode.com/posts"


# Fixture for post_id
@pytest.fixture
def post_id():
    return 1  # Assuming we are updating post with ID 1

### GET Request
def test_get_request():
    response = requests.get(base_url)
    if response.status_code == 200:
        print("GET Request successful:", response.json())
    else:
        print(f"GET request failed with status {response.status_code}")

def test_post_request():
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post(base_url, json=payload)
    if response.status_code == 200:
        print("POST Request successful:", response.json())
    else:
        print(f"POST request failed with status {response.status_code}")

### PUT Request
def test_put_request(post_id):
    update_payload = {
        "id": post_id,
        "title": "updated title",
        "body": "updated body",
        "userId": 2
    }
    response = requests.put(f"{base_url}/{post_id}", json=update_payload)
    if response.status_code == 200:
        print(f"PUT Request successful for post {post_id}:", response.json())
    else:
        print(f"PUT request failed with status {response.status_code}")

### PATCH Request
def test_patch_request(post_id):
    patch_payload = {
        "title": "patched title"
    }
    response = requests.patch(f"{base_url}/{post_id}", json=patch_payload)
    if response.status_code == 200:
        print(f"PATCH Request successful for post {post_id}:", response.json())
    else:
        print(f"PATCH request failed with status {response.status_code}")

### DELETE Request
def test_delete_request(post_id):
    response = requests.delete(f"{base_url}/{post_id}")
    if response.status_code == 200:
        print(f"DELETE Request successful for post {post_id}")
    else:
        print(f"DELETE request failed with status {response.status_code}")


# Running all the methods
if __name__ == "__main__":
    # Perform a GET request
    test_get_request()

    # Perform a POST request
    test_post_request()

    # Perform a PUT request (update post with ID 1)
    test_put_request(1)

    # Perform a PATCH request (update part of post with ID 1)
    test_patch_request(1)

    # Perform a DELETE request (delete post with ID 1)
    test_delete_request(1)
